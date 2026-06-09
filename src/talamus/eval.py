"""Retrieval evaluation harness — measure recall@k/precision@k/MRR, don't guess.

A *case* is a question plus the note titles that SHOULD be retrieved. A *retriever*
maps (question, k) to a ranked list of note titles. The harness runs every case
through a retriever and reports deterministic metrics, so a change to retrieval
(reranking, budgets, graph-routing) can be judged by numbers, not vibes.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from talamus.paths import TalamusPaths
from talamus.recall import search_notes

# (question, k) -> ranked note titles, best first.
Retriever = Callable[[str, int], list[str]]


def _norm(title: str) -> str:
    return title.strip().lower()


@dataclass(frozen=True)
class EvalCase:
    question: str
    relevant: list[str]  # note titles that a good retriever must surface


@dataclass(frozen=True)
class CaseResult:
    question: str
    retrieved: list[str]
    relevant: list[str]
    hit: bool
    recall: float
    precision: float
    reciprocal_rank: float

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "retrieved": self.retrieved,
            "relevant": self.relevant,
            "hit": self.hit,
            "recall": round(self.recall, 4),
            "precision": round(self.precision, 4),
            "reciprocal_rank": round(self.reciprocal_rank, 4),
        }


@dataclass(frozen=True)
class EvalReport:
    k: int
    n_cases: int
    recall_at_k: float
    precision_at_k: float
    mrr: float
    hit_rate: float
    cases: list[CaseResult]

    def to_dict(self) -> dict:
        return {
            "k": self.k,
            "n_cases": self.n_cases,
            "recall_at_k": round(self.recall_at_k, 4),
            "precision_at_k": round(self.precision_at_k, 4),
            "mrr": round(self.mrr, 4),
            "hit_rate": round(self.hit_rate, 4),
            "cases": [c.to_dict() for c in self.cases],
        }

    def format_table(self) -> str:
        lines = [
            f"Valutazione recupero — {self.n_cases} casi, k={self.k}",
            f"  recall@{self.k}    {self.recall_at_k:.3f}",
            f"  precision@{self.k} {self.precision_at_k:.3f}",
            f"  MRR          {self.mrr:.3f}",
            f"  hit-rate     {self.hit_rate:.3f}",
        ]
        misses = [c for c in self.cases if not c.hit]
        if misses:
            lines.append(f"  mancati ({len(misses)}):")
            lines.extend(f"    - {c.question}" for c in misses)
        return "\n".join(lines)


def evaluate_case(case: EvalCase, retriever: Retriever, k: int) -> CaseResult:
    retrieved = retriever(case.question, k)[:k]
    retrieved_norm = [_norm(t) for t in retrieved]
    relevant_norm = {_norm(t) for t in case.relevant}
    matched = relevant_norm.intersection(retrieved_norm)
    recall = len(matched) / len(relevant_norm) if relevant_norm else 0.0
    precision = len(matched) / len(retrieved) if retrieved else 0.0
    rr = 0.0
    for rank, title in enumerate(retrieved_norm, start=1):
        if title in relevant_norm:
            rr = 1.0 / rank
            break
    return CaseResult(
        question=case.question,
        retrieved=retrieved,
        relevant=case.relevant,
        hit=bool(matched),
        recall=recall,
        precision=precision,
        reciprocal_rank=rr,
    )


def evaluate(cases: list[EvalCase], retriever: Retriever, k: int = 5) -> EvalReport:
    results = [evaluate_case(case, retriever, k) for case in cases]
    n = len(results) or 1
    return EvalReport(
        k=k,
        n_cases=len(results),
        recall_at_k=sum(r.recall for r in results) / n,
        precision_at_k=sum(r.precision for r in results) / n,
        mrr=sum(r.reciprocal_rank for r in results) / n,
        hit_rate=sum(1 for r in results if r.hit) / n,
        cases=results,
    )


def search_retriever(paths: TalamusPaths) -> Retriever:
    """The production retriever (`search_notes`) wrapped as a title-ranking function."""
    return lambda question, k: [r["title"] for r in search_notes(paths, question, limit=k)]


def load_cases(path: Path) -> list[EvalCase]:
    """Read cases from JSON: a list of {"question", "relevant": [...]} or {"cases": [...]}."""
    data = json.loads(path.read_text(encoding="utf-8"))
    raw = data["cases"] if isinstance(data, dict) else data
    cases: list[EvalCase] = []
    for entry in raw:
        question = str(entry["question"]).strip()
        relevant = [str(t) for t in entry.get("relevant", [])]
        if question and relevant:
            cases.append(EvalCase(question=question, relevant=relevant))
    return cases
