"""Retrieval research lab — hypothesis-driven ablations, no embeddings (Fase RS).

The M0/M4 error analysis showed three dominant failure classes on the real
eval-set: (1) Italian questions vs English-titled notes — zero token overlap;
(2) huge hub notes matching everything; (3) cross-source questions needing
graph structure. Each hypothesis below is an in-memory retriever variant,
measured on the same 120-case harness as production. Winners (and only
winners) get wired into the real index.

Variants:
- V0  baseline: current production behavior (stemmed BM25 + exact boost)
- V1  bilingual stemming (English suffixes stripped too)
- V2  character-trigram title channel (cognate bridge IT<->EN, no embeddings)
- V3  field weighting (title x3, aliases x2 in the haystack)
- V4  graph score propagation (1-hop, decayed, over typed edges)
- V5+ combinations of the above
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Callable

from talamus.models import CanonicalNote
from talamus.ontology import load_ontology
from talamus.paths import TalamusPaths
from talamus.store import load_notes
from talamus.textutil import tokens as tokens_it

Retriever = Callable[[str, int], list[str]]

_WORD = re.compile(r"[a-zà-ÿ0-9]+")

# light English suffix strip, mirroring the Italian stemmer's philosophy
_EN_SUFFIXES = (
    "ations", "ation", "ings", "ements", "ement", "ities", "ity",
    "ables", "able", "ing", "ed", "es", "s", "ly", "al", "ive",
)  # fmt: skip
_MIN_STEM = 4


def tokens_bilingual(text: str) -> list[str]:
    """Italian stemming first; surviving tokens also lose English suffixes."""
    result = []
    for token in tokens_it(text):
        for suffix in _EN_SUFFIXES:
            if token.endswith(suffix) and len(token) - len(suffix) >= _MIN_STEM:
                token = token[: -len(suffix)]
                break
        result.append(token)
    return result


def trigrams(text: str) -> set[str]:
    """Character 3-grams of the normalized words — the cognate bridge."""
    grams: set[str] = set()
    for word in _WORD.findall(text.lower()):
        if len(word) < 3:
            continue
        for i in range(len(word) - 2):
            grams.add(word[i : i + 3])
    return grams


def _dice(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return 2 * len(a & b) / (len(a) + len(b))


class MemoryIndex:
    """In-memory BM25 for fast ablations (the corpus is small in experiments)."""

    def __init__(
        self,
        notes: list[CanonicalNote],
        tokenizer: Callable[[str], list[str]],
        title_weight: int = 1,
        alias_weight: int = 1,
    ) -> None:
        self.tokenizer = tokenizer
        self.notes = {note.title: note for note in notes}
        self.docs: dict[str, Counter[str]] = {}
        self.lengths: dict[str, int] = {}
        self.df: Counter[str] = Counter()
        self.title_tri: dict[str, set[str]] = {}
        for note in notes:
            haystack = " ".join(
                [
                    *([note.title] * title_weight),
                    *([" ".join(note.aliases)] * alias_weight),
                    " ".join(note.tags),
                    note.retrieval_text,
                    note.summary,
                ]
            )
            counts = Counter(tokenizer(haystack))
            self.docs[note.title] = counts
            self.lengths[note.title] = sum(counts.values())
            for term in counts:
                self.df[term] += 1
            self.title_tri[note.title] = trigrams(f"{note.title} {' '.join(note.aliases)}")

    def bm25(self, query: str) -> dict[str, float]:
        terms = self.tokenizer(query)
        if not self.docs:
            return {}
        avgdl = sum(self.lengths.values()) / len(self.lengths)
        scores: dict[str, float] = {}
        n = len(self.docs)
        for title, counts in self.docs.items():
            score = 0.0
            for term in terms:
                tf = counts.get(term, 0)
                if not tf:
                    continue
                df = self.df.get(term, 1)
                idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
                denom = tf + 1.5 * (1 - 0.75 + 0.75 * self.lengths[title] / avgdl)
                score += idf * tf * 2.5 / denom
            if score > 0:
                scores[title] = score
        return scores

    def trigram_scores(self, query: str) -> dict[str, float]:
        query_tri = trigrams(query)
        return {
            title: dice
            for title, grams in self.title_tri.items()
            if (dice := _dice(query_tri, grams)) > 0
        }


def _normalize(scores: dict[str, float]) -> dict[str, float]:
    top = max(scores.values(), default=0.0)
    if top <= 0:
        return {}
    return {k: v / top for k, v in scores.items()}


def make_variant(
    paths: TalamusPaths,
    bilingual: bool = False,
    trigram_weight: float = 0.0,
    title_weight: int = 1,
    alias_weight: int = 1,
    propagation: float = 0.0,
) -> Retriever:
    """Compose a retriever variant from the hypothesis knobs."""
    notes = load_notes(paths)
    tokenizer = tokens_bilingual if bilingual else tokens_it
    index = MemoryIndex(notes, tokenizer, title_weight, alias_weight)
    neighbors_map: dict[str, list[str]] = {}
    if propagation > 0:
        for edge in load_ontology(paths).get("edges", []):
            neighbors_map.setdefault(str(edge["source"]), []).append(str(edge["target"]))
            neighbors_map.setdefault(str(edge["target"]), []).append(str(edge["source"]))

    def run(question: str, k: int) -> list[str]:
        scores = _normalize(index.bm25(question))
        if trigram_weight > 0:
            for title, dice in _normalize(index.trigram_scores(question)).items():
                scores[title] = scores.get(title, 0.0) + trigram_weight * dice
        if propagation > 0 and scores:
            spread: dict[str, float] = {}
            for title, score in scores.items():
                for neighbor in neighbors_map.get(title, []):
                    spread[neighbor] = max(spread.get(neighbor, 0.0), propagation * score)
            for title, bonus in spread.items():
                scores[title] = scores.get(title, 0.0) + bonus
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        return [title for title, _ in ranked[:k]]

    return run


VARIANTS: dict[str, dict] = {
    "V0-baseline": {},
    "V1-bilingual": {"bilingual": True},
    "V2-trigram": {"trigram_weight": 0.8},
    "V3-fields": {"title_weight": 3, "alias_weight": 2},
    "V4-propagation": {"propagation": 0.4},
    "V12": {"bilingual": True, "trigram_weight": 0.8},
    "V123": {"bilingual": True, "trigram_weight": 0.8, "title_weight": 3, "alias_weight": 2},
    "V1234": {
        "bilingual": True,
        "trigram_weight": 0.8,
        "title_weight": 3,
        "alias_weight": 2,
        "propagation": 0.4,
    },
}


def run_ablations(paths: TalamusPaths, cases_file, k: int = 5) -> dict[str, dict]:
    """Evaluate every variant on the real eval-set. Returns per-variant metrics."""
    from talamus.eval import evaluate, load_cases

    cases = load_cases(cases_file)
    results: dict[str, dict] = {}
    for name, knobs in VARIANTS.items():
        retriever = make_variant(paths, **knobs)
        report = evaluate(cases, retriever, k=k)
        results[name] = {
            "recall_at_k": round(report.recall_at_k, 4),
            "mrr": round(report.mrr, 4),
            "hit_rate": round(report.hit_rate, 4),
            "categories": {cat: stats["recall_at_k"] for cat, stats in report.categories.items()},
        }
    return results
