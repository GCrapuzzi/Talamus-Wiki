from __future__ import annotations

import shutil
from pathlib import Path

from kortex.adapters.llm import LLMProvider
from kortex.extract import extract_notes
from kortex.normalize import normalize_text
from kortex.paths import KortexPaths
from kortex.store import rebuild_indexes, write_note


def ingest_file(paths: KortexPaths, file_path: Path, llm: LLMProvider) -> dict:
    paths.ensure_directories()
    text = file_path.read_text(encoding="utf-8")

    raw_copy = paths.raw / file_path.name
    shutil.copyfile(file_path, raw_copy)

    package = normalize_text(raw_copy.as_posix(), text)
    notes = extract_notes(package, llm)
    for note in notes:
        write_note(paths, note)
    rebuild_indexes(paths)
    return {"notes_written": len(notes), "source": file_path.name}
