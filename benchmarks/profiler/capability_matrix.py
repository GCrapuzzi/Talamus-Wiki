"""The honest capability matrix: which systems have TIME / MEANING /
VERIFIABILITY / LOCAL-FREE. Every Talamus cell links to evidence (a test, a
measured number, or a module) — never a marketing claim. Competitor cells
reflect their documented design, marked conservatively.

This is the Layer-2 complement to the retrieval shootout: SciFact-style
benchmarks say nothing about time, meaning or verifiability — the moats live
here, and the competitors score ✗ by construction (no embeddings/vector DB has
bitemporal facts, an emergent ontology, or active provenance)."""

from __future__ import annotations

from dataclasses import dataclass

YES, NO, PARTIAL = "yes", "no", "partial"

_MARK = {YES: "✓", NO: "✗", PARTIAL: "partial"}


@dataclass(frozen=True)
class Cell:
    mark: str  # YES / NO / PARTIAL
    evidence: str  # a test, a measured number, or a module — required for our YES


# columns
COLUMNS = ["TIME (as-of, invalidation)", "MEANING (emergent ontology)",
           "VERIFIABILITY (provenance, citations)", "LOCAL-FREE (no embeddings/infra)"]  # fmt: skip

MATRIX: dict[str, list[Cell]] = {
    "talamus": [
        Cell(YES, "temporal.py claims.jsonl + ask --as-of; test_talamus_temporal"),
        Cell(YES, "ontology_lab.py promotion rules; test_talamus_ontology*"),
        Cell(YES, "correct.py provenance + ask citations; test_talamus_verify_batch"),
        Cell(YES, "stdlib core, no embeddings; bench shootout ties dense at 0 infra"),
    ],
    "vectordb (MiniLM+FAISS)": [
        Cell(NO, "no temporal model"),
        Cell(NO, "flat vectors, no typed ontology"),
        Cell(NO, "no source-grounding / citations"),
        Cell(NO, "loads an embedding model in RAM"),
    ],
    "mem0": [
        Cell(NO, "no valid-time / as-of"),
        Cell(NO, "no emergent typed schema"),
        Cell(PARTIAL, "stores source refs, no active verify"),
        Cell(NO, "LLM + vector store; API by default"),
    ],
    "zep/graphiti": [
        Cell(PARTIAL, "bi-temporal edges, no note-level as-of read"),
        Cell(PARTIAL, "typed graph, not emergent/promoted"),
        Cell(NO, "no source-correction loop"),
        Cell(NO, "hosted service + embeddings"),
    ],
    "llm_wiki": [
        Cell(NO, "no temporal model"),
        Cell(PARTIAL, "LLM-built wiki links, no promotion rules"),
        Cell(PARTIAL, "cites sources, no verify/invalidate"),
        Cell(NO, "calls a hosted LLM"),
    ],
}


def render_markdown() -> str:
    header = "| system | " + " | ".join(COLUMNS) + " |"
    sep = "| --- " * (len(COLUMNS) + 1) + "|"
    lines = [header, sep]
    for system, cells in MATRIX.items():
        marks = " | ".join(_MARK.get(c.mark, c.mark) for c in cells)
        lines.append(f"| {system} | {marks} |")
    lines.append("")
    lines.append("Talamus evidence per column:")
    for col, cell in zip(COLUMNS, MATRIX["talamus"], strict=True):
        lines.append(f"- **{col}**: {cell.evidence}")
    return "\n".join(lines) + "\n"
