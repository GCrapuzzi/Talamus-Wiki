"""Server-side note-graph layout for the web graph hero.

Reuses the deterministic pure-Python force layout (talamus.ui.physics) so the client
only renders. Data comes from the graph service (the same seam the CLI/MCP use): note
nodes + the relations between them."""

from __future__ import annotations

from pathlib import Path

from talamus.services.graph import get_graph_snapshot
from talamus.ui import physics


def compute_note_graph(root: Path, width: float = 900.0, height: float = 600.0) -> dict:
    result = get_graph_snapshot(root)
    snapshot = result.data
    if snapshot is None:
        return {"nodes": [], "edges": [], "width": width, "height": height}
    note_ids = {node.id for node in snapshot.nodes if node.kind == "note"}
    labels = {node.id: node.label for node in snapshot.nodes if node.kind == "note"}
    edges = [
        (edge.source, edge.target, edge.type)
        for edge in snapshot.edges
        if edge.source in note_ids and edge.target in note_ids
    ]
    layout = physics.build_layout(sorted(note_ids), edges, width=width, height=height)
    physics.settle(layout)
    nodes = [
        {
            "id": node_id,
            "label": labels.get(node_id, node_id),
            "x": round(node.x, 1),
            "y": round(node.y, 1),
            "r": round(layout.radius(node_id), 1),
            "degree": node.degree,
        }
        for node_id, node in layout.nodes.items()
    ]
    out_edges = [
        {"source": src, "target": dst, "type": edge_type, "typed": edge_type != "related"}
        for src, dst, edge_type in layout.edges
    ]
    return {"nodes": nodes, "edges": out_edges, "width": width, "height": height}
