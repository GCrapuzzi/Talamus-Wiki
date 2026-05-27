"""Rerun local section distillation for an existing V2 normalized package."""

from __future__ import annotations

import argparse
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.fde_brain.distill_local import (
    DEFAULT_DISTILL_MODEL,
    DEFAULT_DISTILL_NUM_CTX,
    LocalDistillResult,
    distill_normalized_sections,
)
from tools.fde_brain.graphify import mark_graph_stale
from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.registry import RegistryEntry, load_registry, save_registry
from tools.fde_brain.run_log import FileOutcome, RunLog, write_run_log


_SLUG_SAFE_RE = re.compile(r"[^A-Za-z0-9._-]+")


def _title_to_filename(title: str) -> str:
    cleaned = _SLUG_SAFE_RE.sub("-", title).strip("-")
    return cleaned or "note"


def _sanitize_name(name: str) -> str:
    cleaned = _SLUG_SAFE_RE.sub("-", name).strip("-")
    return cleaned or "source"


def _rel(path: Path | None, root: Path) -> str | None:
    if path is None:
        return None
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _load_manifest(package_dir: Path) -> tuple[Path, dict[str, Any]]:
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")
    return manifest_path, json.loads(manifest_path.read_text(encoding="utf-8"))


def _section_paths(root: Path, manifest: dict[str, Any]) -> list[Path]:
    section_paths: list[Path] = []
    for section in manifest.get("sections", []):
        path_text = section.get("path")
        if not path_text:
            continue
        section_path = (root / path_text).resolve()
        if section_path.exists():
            section_paths.append(section_path)
    return section_paths


def _write_distill_review(
    paths: WorkspacePaths,
    run_id: str,
    source_name: str,
    review_items: list[dict[str, Any]],
) -> None:
    if not review_items:
        return
    paths.logs_decisions.mkdir(parents=True, exist_ok=True)
    out = paths.logs_decisions / f"{run_id}-{_sanitize_name(source_name)}-distill-review.json"
    payload = {"run_id": run_id, "source": source_name, "review_items": review_items}
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _write_notes(result: LocalDistillResult, paths: WorkspacePaths) -> list[Path]:
    paths.fde_brain.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for note in result.notes:
        promoted_path = paths.fde_brain / f"{_title_to_filename(note.title)}.md"
        promoted_path.write_text(note.content, encoding="utf-8")
        written.append(promoted_path)
    return written


def _normalized_paths(root: Path, package_dir: Path, manifest_path: Path, manifest: dict[str, Any]) -> list[str]:
    paths = [manifest_path]
    paths.extend(_section_paths(root, manifest))
    quality = package_dir / "quality-report.json"
    if quality.exists():
        paths.append(quality)
    return [rel for rel in (_rel(path, root) for path in paths) if rel]


def _upsert_registry(
    paths: WorkspacePaths,
    run_id: str,
    manifest_path: Path,
    package_dir: Path,
    manifest: dict[str, Any],
    promoted_paths: list[Path],
) -> None:
    source = manifest.get("source", {})
    raw_path_text = str(source.get("raw_path") or "")
    raw_path = paths.root / raw_path_text if raw_path_text else None
    entry = RegistryEntry(
        raw_path=raw_path_text,
        raw_hash=str(source.get("raw_hash") or ""),
        raw_size=raw_path.stat().st_size if raw_path and raw_path.exists() else 0,
        normalized_paths=_normalized_paths(paths.root, package_dir, manifest_path, manifest),
        category=str(source.get("source_type") or ""),
        parser=str(manifest.get("parser") or ""),
        captured_at=str(source.get("captured_at") or ""),
        ingestion_run=run_id,
        promoted_to=[rel for rel in (_rel(path, paths.root) for path in promoted_paths) if rel],
    )
    manifest_rel = _rel(manifest_path, paths.root)
    entries = [
        existing
        for existing in load_registry(paths.registry_path)
        if not (manifest_rel and manifest_rel in existing.normalized_paths)
    ]
    entries.append(entry)
    save_registry(paths.registry_path, entries)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rerun local distillation for a normalized V2 package.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--package", required=True, help="Normalized package path relative to root.")
    parser.add_argument("--distill-model", default=DEFAULT_DISTILL_MODEL, help="Ollama model for local distillation.")
    parser.add_argument(
        "--distill-num-ctx",
        type=int,
        default=DEFAULT_DISTILL_NUM_CTX,
        help="Ollama num_ctx for local section distillation.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    paths = WorkspacePaths(root)
    package_dir = (root / args.package).resolve()
    started_at = datetime.now(timezone.utc).isoformat()
    run_id = uuid.uuid4().hex[:8]
    log = RunLog(run_id=run_id, started_at=started_at)

    try:
        manifest_path, manifest = _load_manifest(package_dir)
        section_paths = _section_paths(root, manifest)
        if not section_paths:
            raise ValueError(f"no section files found in manifest: {manifest_path}")
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    safe_source = _sanitize_name(package_dir.name)
    progress_path = paths.logs_progress / f"{run_id}-{safe_source}-distill-progress.jsonl"
    print(
        f"rerun_local_distill: run_id={run_id} sections={len(section_paths)} "
        f"model={args.distill_model} num_ctx={args.distill_num_ctx}",
        flush=True,
    )
    print(f"progress: {_rel(progress_path, root)}", flush=True)

    result = distill_normalized_sections(
        section_paths=section_paths,
        paths=paths,
        run_id=run_id,
        model=args.distill_model,
        num_ctx=args.distill_num_ctx,
        progress_path=progress_path,
    )
    promoted_paths: list[Path] = []
    if not result.ok:
        log.overall_ok = False
        print(f"ERROR: distill failed: {result.error}", file=sys.stderr)
    else:
        _write_distill_review(paths, run_id, package_dir.name, result.review_items)
        promoted_paths = _write_notes(result, paths)
        _upsert_registry(paths, run_id, manifest_path, package_dir, manifest, promoted_paths)
        mark_graph_stale(paths.source_graph, f"normalized source distilled: {package_dir.name}")
        if promoted_paths:
            mark_graph_stale(paths.brain_graph, f"FDE Brain notes changed: {package_dir.name}")

    log.files.append(
        FileOutcome(
            pending_name=package_dir.name,
            raw_path=str(manifest.get("source", {}).get("raw_path") or ""),
            normalized_path=_rel(manifest_path, root),
            routed_to="normalized" if result.ok else "failed",
            category=str(manifest.get("source", {}).get("source_type") or ""),
            promoted_to=[rel for rel in (_rel(path, root) for path in promoted_paths) if rel],
            error=result.error,
        )
    )
    log.finished_at = datetime.now(timezone.utc).isoformat()
    write_run_log(paths, log)

    print(f"done: {len(promoted_paths)} notes written to FDE Brain", flush=True)
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
