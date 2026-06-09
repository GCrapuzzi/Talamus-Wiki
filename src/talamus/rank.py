"""Deterministic, stdlib reranking of retrieval candidates — no LLM, no embeddings.

First-stage retrieval gives two weak signals: graph term-overlap and BM25. Taking
only one (the old "graph first, BM25 only if empty") loses notes the other would
rank higher. This blends both — each normalized to 0..1 — plus a precise boost when
the query literally names the note (title/alias). The exact boost is safe against the
hub-domination failure of additive graph routing: it only fires on a literal name hit.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RankWeights:
    bm25: float = 1.0
    graph: float = 1.0
    exact: float = 0.5


DEFAULT_WEIGHTS = RankWeights()


def _normalize(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    top = max(scores.values())
    if top <= 0:
        return {title: 0.0 for title in scores}
    return {title: value / top for title, value in scores.items()}


def _exact_hit(query_lower: str, title: str, aliases: list[str]) -> bool:
    """True when the query literally contains the note's name or one of its aliases."""
    names = [title, *aliases]
    return any(name.strip() and name.strip().lower() in query_lower for name in names)


def rerank_candidates(
    query: str,
    graph_hits: list[tuple[str, float]],
    bm25_hits: list[tuple[str, float]],
    aliases_by_title: dict[str, list[str]],
    limit: int = 5,
    weights: RankWeights = DEFAULT_WEIGHTS,
) -> list[tuple[str, float]]:
    """Blend graph + BM25 candidates into one ranking. Returns (title, score) best-first."""
    graph_norm = _normalize(dict(graph_hits))
    bm25_norm = _normalize(dict(bm25_hits))
    query_lower = query.lower()
    titles = set(graph_norm) | set(bm25_norm)
    combined: dict[str, float] = {}
    for title in titles:
        score = weights.graph * graph_norm.get(title, 0.0)
        score += weights.bm25 * bm25_norm.get(title, 0.0)
        if _exact_hit(query_lower, title, aliases_by_title.get(title, [])):
            score += weights.exact
        combined[title] = score
    ranked = sorted(combined.items(), key=lambda item: (item[1], item[0]), reverse=True)
    return ranked[:limit]
