import math
import unittest

from talamus.ui.physics import (
    build_layout,
    domain_colors,
    hit_test,
    select_global,
    select_neighborhood,
    settle,
    step,
)

EDGES = [
    ("A", "B", "uses"),
    ("B", "C", "related"),
    ("A", "C", "part-of"),
    ("D", "E", "related"),
]
NODES = ["A", "B", "C", "D", "E", "F"]  # F is isolated


def _distance(layout, a: str, b: str) -> float:
    na, nb = layout.nodes[a], layout.nodes[b]
    return math.hypot(na.x - nb.x, na.y - nb.y)


class LayoutTests(unittest.TestCase):
    def test_build_is_deterministic_and_degree_aware(self) -> None:
        one = build_layout(NODES, EDGES, seed=7)
        two = build_layout(NODES, EDGES, seed=7)
        self.assertEqual(
            [(n.x, n.y) for n in one.nodes.values()],
            [(n.x, n.y) for n in two.nodes.values()],
        )
        self.assertEqual(one.nodes["A"].degree, 2)
        self.assertEqual(one.nodes["F"].degree, 0)
        self.assertGreater(one.radius("A"), one.radius("F"))

    def test_settles_without_nan_and_inside_canvas(self) -> None:
        layout = build_layout(NODES, EDGES)
        steps = settle(layout, max_steps=400)
        self.assertLessEqual(steps, 400)
        for node in layout.nodes.values():
            self.assertFalse(math.isnan(node.x) or math.isnan(node.y))
            self.assertTrue(0 <= node.x <= layout.width)
            self.assertTrue(0 <= node.y <= layout.height)

    def test_connected_nodes_end_closer_than_unconnected(self) -> None:
        layout = build_layout(NODES, EDGES)
        settle(layout, max_steps=400)
        connected = _distance(layout, "A", "B")
        unconnected = _distance(layout, "A", "E")
        self.assertLess(connected, unconnected)

    def test_movement_decreases_as_it_settles(self) -> None:
        layout = build_layout(NODES, EDGES)
        early = step(layout)
        for _ in range(150):
            late = step(layout)
        self.assertLess(late, early)


class SelectionTests(unittest.TestCase):
    def test_global_selection_prefers_connected(self) -> None:
        chosen = select_global(EDGES, NODES, cap=3)
        self.assertEqual(len(chosen), 3)
        self.assertIn("A", chosen)
        self.assertNotIn("F", chosen)  # the isolate loses to connected nodes

    def test_neighborhood_bfs_with_cap(self) -> None:
        hood = select_neighborhood(EDGES, "A", hops=1)
        self.assertEqual(set(hood), {"A", "B", "C"})
        capped = select_neighborhood(EDGES, "A", hops=2, cap=2)
        self.assertEqual(len(capped), 2)
        self.assertEqual(capped[0], "A")  # focus always first


class HitTestTests(unittest.TestCase):
    def test_hit_inside_radius_and_miss_outside(self) -> None:
        layout = build_layout(["X"], [])
        node = layout.nodes["X"]
        self.assertEqual(hit_test(layout, node.x + 2, node.y + 2), "X")
        self.assertIsNone(hit_test(layout, node.x + 200, node.y + 200))


class ColorTests(unittest.TestCase):
    def test_stable_palette_assignment(self) -> None:
        colors = domain_colors(["Tempo", "Recupero", "Tempo"])
        self.assertEqual(len(colors), 2)
        self.assertEqual(colors, domain_colors(["Recupero", "Tempo"]))


if __name__ == "__main__":
    unittest.main()
