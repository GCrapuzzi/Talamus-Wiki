from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from brain.graph import query_graph
from brain.paths import BrainPaths
from brain.search import BM25Index


@dataclass(frozen=True)
class ContextBundle:
    question: str
    items: list[dict]

    def render(self) -> str:
        lines = [f"Question: {self.question}", ""]
        for idx, item in enumerate(self.items, start=1):
            lines.extend([f"[{idx}] {item['path']} ({item['route']})", item["content"], ""])
        return "\n".join(lines).strip() + "\n"


def _note_path(paths: BrainPaths, label: str) -> Path:
    filename = label.replace(" ", "-") + ".md"
    return paths.notes / filename


def build_context_bundle(
    paths: BrainPaths,
    graph: dict,
    search_index: BM25Index,
    question: str,
    limit: int = 5,
) -> ContextBundle:
    items: list[dict] = []
    for node in query_graph(graph, question, limit=limit):
        path = _note_path(paths, str(node["label"]))
        if not path.is_file():
            continue
        items.append({"route": "graph", "path": path.as_posix(), "content": path.read_text(encoding="utf-8")})
    if items:
        return ContextBundle(question=question, items=items)

    for result in search_index.search(question, limit=limit):
        path = paths.notes / f"{result['id']}.md"
        if not path.is_file():
            continue
        items.append({"route": "bm25", "path": path.as_posix(), "content": path.read_text(encoding="utf-8")})
    return ContextBundle(question=question, items=items)
