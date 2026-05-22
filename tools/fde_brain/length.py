from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.fde_brain.chapters import extract_chapters_from_pdf


def is_long_pdf(reader: Any, *, min_chapters: int = 3, min_pages: int = 50) -> bool:
    chapters = extract_chapters_from_pdf(reader)
    if len(chapters) >= min_chapters:
        return True
    return len(reader.pages) > min_pages
