from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

NO_PROMOTION_SENTINEL = "NO_PROMOTION"

DISTILL_PROMPT_TEMPLATE = """You are an Obsidian wiki curator. Given the following normalized source,
decide if there is a stable, reusable concept worth promoting to the
curated wiki.

If yes, output a single Obsidian-native markdown note with:
- frontmatter (type, tags, sources, captured-at)
- wikilinks where appropriate
- standard sections: Summary, Core Idea, Practical Use, Source Notes

The `sources:` frontmatter field must list both the raw and normalized paths.

If no stable concept emerges, output exactly: {sentinel}

Source path: {raw_path}
Normalized path: {normalized_path}
--- BEGIN CONTENT ---
{content}
--- END CONTENT ---
"""


@dataclass(frozen=True)
class DistillResult:
    ok: bool
    promoted: bool
    note_content: str | None
    note_slug: str | None
    raw_response: str
    error: str | None = None


def _slug_for(normalized_path: Path) -> str:
    return normalized_path.stem.lower().replace(" ", "-")


def distill_via_claude(
    normalized_path: Path,
    raw_path: Path,
    timeout_sec: int = 120,
) -> DistillResult:
    try:
        content = normalized_path.read_text(encoding="utf-8")
    except OSError as exc:
        return DistillResult(
            ok=False, promoted=False, note_content=None, note_slug=None,
            raw_response="", error=f"failed to read normalized file: {exc}",
        )

    prompt = DISTILL_PROMPT_TEMPLATE.format(
        sentinel=NO_PROMOTION_SENTINEL,
        raw_path=raw_path.as_posix(),
        normalized_path=normalized_path.as_posix(),
        content=content,
    )

    try:
        completed = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return DistillResult(
            ok=False, promoted=False, note_content=None, note_slug=None,
            raw_response="", error=f"claude cli timeout after {timeout_sec}s",
        )
    except FileNotFoundError as exc:
        return DistillResult(
            ok=False, promoted=False, note_content=None, note_slug=None,
            raw_response="", error=f"claude binary not found: {exc}",
        )

    if completed.returncode != 0:
        return DistillResult(
            ok=False, promoted=False, note_content=None, note_slug=None,
            raw_response=completed.stdout, error=completed.stderr.strip() or f"claude exited {completed.returncode}",
        )

    response = completed.stdout.strip()

    if response == NO_PROMOTION_SENTINEL or response.startswith(NO_PROMOTION_SENTINEL + "\n"):
        return DistillResult(
            ok=True, promoted=False, note_content=None, note_slug=None,
            raw_response=response,
        )

    if not response.startswith("---"):
        return DistillResult(
            ok=True, promoted=False, note_content=None, note_slug=None,
            raw_response=response,
        )

    return DistillResult(
        ok=True, promoted=True, note_content=response,
        note_slug=_slug_for(normalized_path), raw_response=response,
    )
