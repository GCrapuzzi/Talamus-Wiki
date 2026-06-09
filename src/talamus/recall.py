from __future__ import annotations

from talamus.ask import build_context_bundle
from talamus.graph import load_graph, query_graph_scored
from talamus.naming import note_filename, note_slug
from talamus.ontology import load_ontology, neighbors
from talamus.paths import TalamusPaths
from talamus.rank import rerank_candidates
from talamus.search import BM25Index
from talamus.store import load_notes


def _load_graph_and_index(paths: TalamusPaths):
    graph = (
        load_graph(paths.graph_file) if paths.graph_file.is_file() else {"nodes": {}, "edges": []}
    )
    index = BM25Index.load(paths.index_file) if paths.index_file.is_file() else BM25Index()
    return graph, index


def search_notes(paths: TalamusPaths, query: str, limit: int = 5) -> list[dict]:
    """Candidati pertinenti: unione grafo + BM25, riordinata (rerank). {title, summary}."""
    notes_by_title = {note.title: note for note in load_notes(paths)}
    graph, index = _load_graph_and_index(paths)
    pool = max(limit * 2, limit)
    graph_hits = [
        (str(node.get("label", "")), float(score))
        for node, score in query_graph_scored(graph, query, limit=pool)
        if str(node.get("label", "")) in notes_by_title
    ]
    slug_to_title = {note_slug(title): title for title in notes_by_title}
    bm25_hits = [
        (slug_to_title[hit["id"]], float(hit["score"]))
        for hit in index.search(query, limit=pool)
        if hit["id"] in slug_to_title
    ]
    aliases_by_title = {title: note.aliases for title, note in notes_by_title.items()}
    ranked = rerank_candidates(query, graph_hits, bm25_hits, aliases_by_title, limit=limit)
    results: list[dict] = []
    for title, _score in ranked:
        note = notes_by_title.get(title)
        if note is not None:
            results.append({"title": title, "summary": note.summary})
    return results


def read_note_text(paths: TalamusPaths, title: str) -> str | None:
    """Contenuto Markdown di una scheda dato il titolo (fallback case-insensitive)."""
    path = paths.notes / note_filename(title)
    if path.is_file():
        return path.read_text(encoding="utf-8")
    for note in load_notes(paths):
        if note.title.lower() == title.lower():
            candidate = paths.notes / note_filename(note.title)
            if candidate.is_file():
                return candidate.read_text(encoding="utf-8")
    return None


def concept_neighbors(paths: TalamusPaths, concept: str) -> list[dict]:
    """Vicini tipizzati di un concetto nella mappa (ontologia): per navigare le connessioni."""
    return neighbors(load_ontology(paths), concept)


def recall_context(paths: TalamusPaths, question: str, limit: int = 5) -> str:
    """Contesto pertinente (schede reali) per una domanda.
    L'agente è l'LLM: ritorna risorse, non risposte."""
    graph, index = _load_graph_and_index(paths)
    bundle = build_context_bundle(paths, graph, index, question, limit=limit)
    if not bundle.items:
        return "Nessun contesto pertinente trovato nel brain."
    return bundle.render()
