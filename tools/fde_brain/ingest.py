from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.fde_brain.classify import classify
from tools.fde_brain.distill import distill_via_claude
from tools.fde_brain.normalize import NormalizedOutput, normalize_source
from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.preflight import run_preflight
from tools.fde_brain.registry import RegistryEntry, append_entry
from tools.fde_brain.run_log import FileOutcome, RunLog, write_run_log
from tools.fde_brain.validate_workspace import validate_workspace


_SAFE_NAME_RE = re.compile(r"[^A-Za-z0-9._-]+")


def _sanitize_name(name: str) -> str:
    cleaned = _SAFE_NAME_RE.sub("-", name).strip("-")
    return cleaned or "file"


def _sha256_of(path: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
            size += len(chunk)
    return f"sha256:{digest.hexdigest()}", size


def _archive(src: Path, paths: WorkspacePaths, category: str, captured_at: datetime) -> Path:
    target_dir = paths.raw_for(category) if category != "unknown" else (paths.raw / "unknown")
    target_dir.mkdir(parents=True, exist_ok=True)
    date_prefix = captured_at.strftime("%Y-%m-%d")
    safe = _sanitize_name(src.name)
    target = target_dir / f"{date_prefix}-{safe}"
    counter = 1
    while target.exists():
        target = target_dir / f"{date_prefix}-{counter}-{safe}"
        counter += 1
    shutil.move(str(src), str(target))
    return target


def _rel(path: Path | None, root: Path) -> str | None:
    if path is None:
        return None
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def _process_one(
    src: Path,
    paths: WorkspacePaths,
    run_id: str,
    captured_at: datetime,
) -> FileOutcome:
    pending_name = src.name
    raw_hash, raw_size = _sha256_of(src)
    category = classify(src)

    raw_path = _archive(src, paths, category, captured_at)

    normalized: NormalizedOutput = normalize_source(
        raw_path=raw_path,
        category=category,
        raw_hash=raw_hash,
        captured_at=captured_at,
        paths=paths,
    )

    promoted_path: Path | None = None
    if normalized.routed_to == "normalized" and normalized.output_path is not None:
        distill_result = distill_via_claude(
            normalized_path=normalized.output_path,
            raw_path=raw_path,
        )
        if distill_result.ok and distill_result.promoted and distill_result.note_content:
            slug = distill_result.note_slug or normalized.output_path.stem
            promoted_path = paths.fde_brain / f"{slug}.md"
            paths.fde_brain.mkdir(parents=True, exist_ok=True)
            promoted_path.write_text(distill_result.note_content, encoding="utf-8")

    entry = RegistryEntry(
        raw_path=_rel(raw_path, paths.root) or raw_path.as_posix(),
        raw_hash=raw_hash,
        raw_size=raw_size,
        normalized_paths=[_rel(normalized.output_path, paths.root) or ""] if normalized.output_path else [],
        category=category,
        parser=normalized.parser,
        captured_at=captured_at.isoformat(),
        ingestion_run=run_id,
        promoted_to=[_rel(promoted_path, paths.root) or ""] if promoted_path else [],
    )
    append_entry(paths.registry_path, entry)

    return FileOutcome(
        pending_name=pending_name,
        raw_path=_rel(raw_path, paths.root),
        normalized_path=_rel(normalized.output_path, paths.root),
        routed_to=normalized.routed_to,
        category=category,
        promoted_to=_rel(promoted_path, paths.root),
        error=normalized.error,
    )


def _git(root: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True, text=True, check=False,
    )


def _commit_changes(root: Path, message: str) -> str | None:
    _git(root, ["add", "AI Space", "FDE Brain"])
    diff = _git(root, ["diff", "--cached", "--quiet"])
    if diff.returncode == 0:
        return None
    result = _git(root, ["commit", "-m", message])
    if result.returncode != 0:
        return None
    rev = _git(root, ["rev-parse", "HEAD"])
    return rev.stdout.strip() or None


def _short_uuid() -> str:
    return uuid.uuid4().hex[:8]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the FDE Brain ingestion pipeline.")
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--no-commit", action="store_true", help="Skip the final git commit.")
    parser.add_argument("--dry-run", action="store_true", help="Plan only; do not write logs or commit.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    paths = WorkspacePaths(root)

    issues = validate_workspace(root)
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1

    preflight = run_preflight()
    if not all(r.ok for r in preflight):
        for result in preflight:
            print(result.status_text(), file=sys.stderr)
        return 1

    captured_at = datetime.now(timezone.utc)
    log = RunLog(run_id=_short_uuid(), started_at=captured_at.isoformat())

    pending_files = sorted(
        p for p in paths.pending.iterdir()
        if p.is_file() and p.name != ".gitkeep"
    )

    for src in pending_files:
        try:
            outcome = _process_one(src, paths, log.run_id, captured_at)
        except Exception as exc:
            outcome = FileOutcome(
                pending_name=src.name,
                raw_path=None,
                normalized_path=None,
                routed_to="failed",
                category="unknown",
                promoted_to=None,
                error=f"orchestrator exception: {exc}",
            )
            log.overall_ok = False
        if outcome.routed_to == "failed" and outcome.error:
            log.overall_ok = False
        log.files.append(outcome)
        print(f"[{outcome.routed_to}] {outcome.pending_name} -> {outcome.normalized_path or outcome.raw_path}")

    log.finished_at = datetime.now(timezone.utc).isoformat()

    if args.dry_run:
        print(f"dry-run complete; {len(log.files)} files processed")
        return 0 if log.overall_ok else 1

    write_run_log(paths, log)

    if not args.no_commit and log.files:
        commit_msg = f"chore(ai-pipeline): ingest pending batch {captured_at.strftime('%Y-%m-%d')}"
        commit_hash = _commit_changes(root, commit_msg)
        log.commit_hash = commit_hash
        write_run_log(paths, log)

    return 0 if log.overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
