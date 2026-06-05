from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

from kortex.adapters.llm import LLMProvider
from kortex.extract import extract_notes
from kortex.linking import NoteRegistry
from kortex.normalize import NormalizedPackage, normalize_text
from kortex.paths import KortexPaths
from kortex.session import normalize_session, session_worth_remembering
from kortex.store import load_notes, rebuild_indexes, render_note_markdown, write_note_json


def _compile_package(paths: KortexPaths, package: NormalizedPackage, llm: LLMProvider) -> int:
    """Estrae le note dal pacchetto, le scrive e risolve i wikilink a lotto, ricostruisce gli indici."""
    notes = extract_notes(package, llm)
    # Fase 1: persisti tutti gli oggetti canonici, così l'intero lotto è noto.
    for note in notes:
        write_note_json(paths, note)
    # Fase 2: rendi il Markdown con un registro dell'INTERO lotto (+ note esistenti),
    # così i wikilink tra note dello stesso lotto si risolvono senza link rotti.
    registry = NoteRegistry.from_notes(load_notes(paths))
    for note in notes:
        render_note_markdown(paths, note, registry)
    rebuild_indexes(paths)
    return len(notes)


def ingest_file(paths: KortexPaths, file_path: Path, llm: LLMProvider) -> dict:
    paths.ensure_directories()
    text = file_path.read_text(encoding="utf-8")
    raw_copy = paths.raw / file_path.name
    shutil.copyfile(file_path, raw_copy)
    package = normalize_text(raw_copy.as_posix(), text)
    written = _compile_package(paths, package, llm)
    return {"notes_written": written, "source": file_path.name}


def remember_session(paths: KortexPaths, transcript: str, diff: str, llm: LLMProvider) -> dict:
    """Una sessione-agente (transcript + diff) diventa note, se supera il gate."""
    paths.ensure_directories()
    if not session_worth_remembering(transcript, diff):
        return {"skipped": True, "notes_written": 0}
    digest = hashlib.sha256((transcript + "\n" + diff).encode("utf-8")).hexdigest()[:8]
    raw_path = paths.raw / f"session-{digest}.md"
    raw_path.write_text(
        transcript + ("\n\n---\n\n" + diff if diff.strip() else ""), encoding="utf-8"
    )
    package = normalize_session(raw_path.as_posix(), transcript, diff)
    written = _compile_package(paths, package, llm)
    return {"skipped": False, "notes_written": written}
