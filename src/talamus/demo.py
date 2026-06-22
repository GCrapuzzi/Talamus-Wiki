"""A small, LLM-free example brain so users can try Talamus instantly."""

from __future__ import annotations

from talamus.linking import NoteRegistry
from talamus.models import CanonicalNote, Relation, SourceRef
from talamus.paths import TalamusPaths
from talamus.store import load_notes, rebuild_indexes, render_note_markdown, write_note_json


def _note(title: str, summary: str, body: str, relations: list[tuple[str, str]]) -> CanonicalNote:
    return CanonicalNote(
        note_id=title.lower().replace(" ", "-"),
        title=title,
        aliases=[],
        folder="",
        tags=["demo"],
        summary=summary,
        retrieval_text=title.lower(),
        body_sections={"definizione": body},
        proposed_links=[],
        relations=[
            Relation(source=title, relation=rel, target=target, confidence=0.9)
            for rel, target in relations
        ],
        sources=[SourceRef("demo", "demo", "demo", "sha256:demo", [summary])],
        confidence=0.9,
    )


def _demo_notes() -> list[CanonicalNote]:
    return [
        _note(
            "Retrieval-Augmented Generation",
            "An architecture that gives an LLM context retrieved from an external knowledge base.",
            "RAG retrieves the relevant documents and passes them to the model as context, "
            "so the answer can cite up-to-date sources without retraining the model.",
            [("uses", "Embedding"), ("uses", "Reranking")],
        ),
        _note(
            "Embedding",
            "A vector representation of the meaning of a text.",
            "An embedding maps text into a numeric vector where similar meanings are close "
            "together; it is the building block of semantic search.",
            [("part-of", "Retrieval-Augmented Generation")],
        ),
        _note(
            "Reranking",
            "A second retrieval stage that reorders the candidates by relevance.",
            "Reranking reorders the raw retrieval results to bring the most relevant to the "
            "question to the top, improving the context passed to the model.",
            [("part-of", "Retrieval-Augmented Generation")],
        ),
    ]


def create_demo_brain(paths: TalamusPaths) -> int:
    """Write a few pre-baked, cross-linked notes and build the indexes. Returns the note count."""
    paths.ensure_directories()
    notes = _demo_notes()
    for note in notes:
        write_note_json(paths, note)
    registry = NoteRegistry.from_notes(load_notes(paths))
    for note in notes:
        render_note_markdown(paths, note, registry)
    rebuild_indexes(paths)
    return len(notes)
