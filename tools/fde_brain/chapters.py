from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


@dataclass(frozen=True)
class Chapter:
    title: str
    anchor: str
    page_start: int
    page_end: int
    level: int


_ANCHOR_NORMALIZE_RE = re.compile(r"[^a-z0-9]+")


def chapter_anchor(title: str) -> str:
    lowered = title.lower()
    slug = _ANCHOR_NORMALIZE_RE.sub("-", lowered).strip("-")
    return slug or "section"


def _flatten_outline(outline: Any, level: int = 1) -> list[tuple[Any, int]]:
    flat: list[tuple[Any, int]] = []
    for entry in outline:
        if isinstance(entry, list):
            flat.extend(_flatten_outline(entry, level + 1))
        else:
            flat.append((entry, level))
    return flat


def extract_chapters_from_pdf(reader: Any) -> list[Chapter]:
    flat = _flatten_outline(getattr(reader, "outline", []) or [])
    if not flat:
        return []

    total_pages = len(reader.pages)
    resolved: list[tuple[str, int, int]] = []
    for item, level in flat:
        title = getattr(item, "title", None)
        if not title:
            continue
        try:
            page_index = reader.get_destination_page_number(item)
        except Exception:
            continue
        if page_index is None or page_index < 0 or page_index >= total_pages:
            continue
        resolved.append((title, page_index + 1, level))

    if not resolved:
        return []

    chapters: list[Chapter] = []
    for idx, (title, page_start, level) in enumerate(resolved):
        if idx + 1 < len(resolved):
            page_end = resolved[idx + 1][1] - 1
        else:
            page_end = total_pages
        if page_end < page_start:
            page_end = page_start
        chapters.append(
            Chapter(
                title=title,
                anchor=chapter_anchor(title),
                page_start=page_start,
                page_end=page_end,
                level=level,
            )
        )

    return chapters
