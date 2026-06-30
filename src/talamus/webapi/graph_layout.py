"""Note-graph data for the web graph hero.

Note titles are the nodes; the typed relations from the ontology are the edges. The
*layout* is done client-side (d3-force) so the constellation is organic and radial like
Obsidian's graph — the server only ships nodes (id/label/degree) + edges, capped to the
most-connected notes on very large brains. No O(N^2) force settle here, so it is fast for
any brain size."""

from __future__ import annotations

from pathlib import Path

from talamus.ontology import load_ontology
from talamus.paths import TalamusPaths
from talamus.store import load_notes
from talamus.ui import physics

_NODE_CAP = 600


def compute_note_graph(root: Path) -> dict:
    paths = TalamusPaths(Path(root))
    titles = [note.title for note in load_notes(paths)]
    ontology = load_ontology(paths)
    edges = [
        (str(edge["source"]), str(edge["target"]), str(edge.get("type", "related")))
        for edge in ontology.get("edges", [])
    ]

    kept = set(physics.select_global(edges, titles, cap=_NODE_CAP))
    kept_edges = [(s, d, t) for (s, d, t) in edges if s in kept and d in kept]

    degree = dict.fromkeys(kept, 0)
    for src, dst, _type in kept_edges:
        degree[src] += 1
        degree[dst] += 1

    nodes = [{"id": title, "label": title, "degree": degree[title]} for title in sorted(kept)]
    out_edges = [
        {"source": src, "target": dst, "type": edge_type, "typed": edge_type != "related"}
        for src, dst, edge_type in kept_edges
    ]
    return {
        "nodes": nodes,
        "edges": out_edges,
        "total": len(titles),
        "shown": len(nodes),
    }
