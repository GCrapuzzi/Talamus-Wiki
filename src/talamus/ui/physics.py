"""Force-directed graph layout in pure Python — the physics behind the graph view.

No UI framework, no dependencies: a deterministic (seeded) spring-embedder in the spirit
of Fruchterman–Reingold / ForceAtlas: Coulomb repulsion between every pair,
Hooke springs along edges, a soft pull toward the center, velocity damping.
``step()`` returns the total movement so callers can animate until settled.

Kept separate from the rendering so the physics is testable headless and the
canvas layer stays thin. O(N²) per step is fine at the visible-node caps the
graph view uses (≤ ~150 nodes).
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass, field

REPULSION = 12000.0  # Coulomb constant: how hard nodes push each other apart
SPRING = 0.06  # Hooke constant: how hard edges pull their endpoints together
SPRING_LENGTH = 90.0  # rest length of an edge
GRAVITY = 0.015  # soft pull toward the canvas center
DAMPING = 0.85  # velocity decay per step (prevents oscillation)
MAX_SPEED = 40.0  # per-step displacement cap (stability)


@dataclass
class Node:
    id: str
    x: float
    y: float
    vx: float = 0.0
    vy: float = 0.0
    degree: int = 0
    domain: str = ""
    pinned: bool = False


@dataclass
class Layout:
    width: float
    height: float
    nodes: dict[str, Node] = field(default_factory=dict)
    edges: list[tuple[str, str, str]] = field(default_factory=list)  # (src, dst, type)

    def radius(self, node_id: str) -> float:
        """Visual radius: grows with the square root of the degree."""
        node = self.nodes[node_id]
        return min(6.0 + 2.0 * math.sqrt(node.degree), 18.0)


def build_layout(
    node_ids: list[str],
    edges: list[tuple[str, str, str]],
    width: float = 900.0,
    height: float = 600.0,
    domains: dict[str, str] | None = None,
    seed: int = 42,
) -> Layout:
    """Seeded initial placement on a circle + jitter, degrees from the edge list."""
    rng = random.Random(seed)
    layout = Layout(width=width, height=height)
    n = max(len(node_ids), 1)
    ring = min(width, height) * 0.35
    for index, node_id in enumerate(node_ids):
        angle = (2 * math.pi * index) / n
        layout.nodes[node_id] = Node(
            id=node_id,
            x=width / 2 + ring * math.cos(angle) + rng.uniform(-20, 20),
            y=height / 2 + ring * math.sin(angle) + rng.uniform(-20, 20),
            domain=(domains or {}).get(node_id, ""),
        )
    known = set(layout.nodes)
    for src, dst, edge_type in edges:
        if src in known and dst in known and src != dst:
            layout.edges.append((src, dst, edge_type))
            layout.nodes[src].degree += 1
            layout.nodes[dst].degree += 1
    return layout


def step(layout: Layout) -> float:
    """One physics tick. Returns total movement (px) — small means settled."""
    nodes = list(layout.nodes.values())
    forces: dict[str, list[float]] = {node.id: [0.0, 0.0] for node in nodes}
    # pairwise repulsion
    for i, a in enumerate(nodes):
        for b in nodes[i + 1 :]:
            dx = a.x - b.x
            dy = a.y - b.y
            dist_sq = dx * dx + dy * dy
            if dist_sq < 1.0:
                dx, dy, dist_sq = 1.0, 1.0, 2.0  # unstick coincident nodes
            force = REPULSION / dist_sq
            dist = math.sqrt(dist_sq)
            fx, fy = force * dx / dist, force * dy / dist
            forces[a.id][0] += fx
            forces[a.id][1] += fy
            forces[b.id][0] -= fx
            forces[b.id][1] -= fy
    # springs along edges
    for src, dst, _type in layout.edges:
        a, b = layout.nodes[src], layout.nodes[dst]
        dx = b.x - a.x
        dy = b.y - a.y
        dist = math.sqrt(dx * dx + dy * dy) or 1.0
        pull = SPRING * (dist - SPRING_LENGTH)
        fx, fy = pull * dx / dist, pull * dy / dist
        forces[src][0] += fx
        forces[src][1] += fy
        forces[dst][0] -= fx
        forces[dst][1] -= fy
    # gravity toward the center + integration
    movement = 0.0
    cx, cy = layout.width / 2, layout.height / 2
    for node in nodes:
        if node.pinned:
            node.vx = node.vy = 0.0
            continue
        fx = forces[node.id][0] + (cx - node.x) * GRAVITY
        fy = forces[node.id][1] + (cy - node.y) * GRAVITY
        node.vx = (node.vx + fx) * DAMPING
        node.vy = (node.vy + fy) * DAMPING
        speed = math.sqrt(node.vx * node.vx + node.vy * node.vy)
        if speed > MAX_SPEED:
            node.vx *= MAX_SPEED / speed
            node.vy *= MAX_SPEED / speed
        node.x += node.vx
        node.y += node.vy
        # keep inside the canvas with a small margin
        node.x = min(max(node.x, 20.0), layout.width - 20.0)
        node.y = min(max(node.y, 20.0), layout.height - 20.0)
        movement += abs(node.vx) + abs(node.vy)
    return movement


def settle(layout: Layout, max_steps: int = 300, threshold: float = 0.5) -> int:
    """Run steps until movement-per-node drops under threshold. Returns steps used."""
    for index in range(max_steps):
        movement = step(layout)
        if movement / max(len(layout.nodes), 1) < threshold:
            return index + 1
    return max_steps


def hit_test(layout: Layout, x: float, y: float, slop: float = 6.0) -> str | None:
    """The node under (x, y), if any — used to open a note on tap."""
    best: tuple[float, str] | None = None
    for node in layout.nodes.values():
        radius = layout.radius(node.id) + slop
        dx, dy = x - node.x, y - node.y
        dist_sq = dx * dx + dy * dy
        if dist_sq <= radius * radius and (best is None or dist_sq < best[0]):
            best = (dist_sq, node.id)
    return best[1] if best else None


def select_global(
    edges: list[tuple[str, str, str]], all_nodes: list[str], cap: int = 120
) -> list[str]:
    """The most connected nodes for the global view (plus isolates if room)."""
    degree: dict[str, int] = {node: 0 for node in all_nodes}
    for src, dst, _type in edges:
        if src in degree:
            degree[src] += 1
        if dst in degree:
            degree[dst] += 1
    ranked = sorted(all_nodes, key=lambda n: (-degree[n], n))
    return ranked[:cap]


def select_neighborhood(
    edges: list[tuple[str, str, str]], focus: str, hops: int = 2, cap: int = 60
) -> list[str]:
    """Focus node + its neighborhood up to ``hops`` (BFS), capped."""
    adjacency: dict[str, set[str]] = {}
    for src, dst, _type in edges:
        adjacency.setdefault(src, set()).add(dst)
        adjacency.setdefault(dst, set()).add(src)
    seen = [focus]
    frontier = {focus}
    for _ in range(hops):
        frontier = {
            neighbor
            for node in frontier
            for neighbor in adjacency.get(node, set())
            if neighbor not in seen
        }
        for neighbor in sorted(frontier):
            if len(seen) >= cap:
                return seen
            seen.append(neighbor)
    return seen


PALETTE = [
    "#4FC3F7", "#FFB74D", "#81C784", "#E57373", "#BA68C8", "#FFD54F",
    "#4DB6AC", "#F06292", "#9575CD", "#AED581", "#FF8A65", "#90A4AE",
]  # fmt: skip


def domain_colors(domains: list[str]) -> dict[str, str]:
    """Stable domain -> color assignment (12-color palette, llm_wiki-style)."""
    return {name: PALETTE[i % len(PALETTE)] for i, name in enumerate(sorted(set(domains)))}
