import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from talamus.ask import build_context_bundle
from talamus.budget import context_budget, estimate_tokens, fit_to_budget
from talamus.graph import load_graph
from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.search import BM25Index
from talamus.store import rebuild_indexes, write_note


class EstimateTokensTests(unittest.TestCase):
    def test_empty_is_zero(self) -> None:
        self.assertEqual(estimate_tokens(""), 0)

    def test_longer_text_costs_more(self) -> None:
        self.assertGreater(estimate_tokens("a" * 400), estimate_tokens("a" * 40))

    def test_word_floor_over_char_estimate(self) -> None:
        # 10 one-char words: chars/4 = 4, but the word floor keeps it at 10.
        self.assertEqual(estimate_tokens("a b c d e f g h i j"), 10)


class ContextBudgetTests(unittest.TestCase):
    def test_default_and_override(self) -> None:
        self.assertEqual(context_budget(1234), 1234)
        self.assertGreater(context_budget(), 0)

    def test_env_override(self) -> None:
        with mock.patch.dict(os.environ, {"TALAMUS_CONTEXT_BUDGET": "777"}):
            self.assertEqual(context_budget(), 777)

    def test_explicit_beats_env(self) -> None:
        with mock.patch.dict(os.environ, {"TALAMUS_CONTEXT_BUDGET": "777"}):
            self.assertEqual(context_budget(50), 50)


class FitToBudgetTests(unittest.TestCase):
    def _items(self, n: int, chars: int) -> list[dict]:
        return [{"content": "x" * chars, "path": f"n{i}"} for i in range(n)]

    def test_keeps_prefix_within_budget(self) -> None:
        items = self._items(5, 400)  # ~100 tokens each
        kept = fit_to_budget(items, budget=250)
        self.assertEqual(len(kept), 2)  # 2*100 <= 250, a 3rd would exceed

    def test_first_oversize_item_is_truncated_not_dropped(self) -> None:
        kept = fit_to_budget([{"content": "x" * 4000}], budget=100)
        self.assertEqual(len(kept), 1)
        self.assertLessEqual(estimate_tokens(kept[0]["content"]), 100)

    def test_zero_budget_returns_nothing(self) -> None:
        self.assertEqual(fit_to_budget(self._items(3, 100), budget=0), [])


def _big_note(title: str) -> CanonicalNote:
    body = "argomento comune " + ("lorem ipsum dolor sit amet " * 80)
    src = SourceRef("raw/a.md", "norm/a#1", "s", "sha256:x", ["c"])
    return CanonicalNote(
        note_id=title.lower().replace(" ", "-"),
        title=title,
        aliases=[],
        folder="",
        tags=[],
        summary="argomento comune",
        retrieval_text=body,
        body_sections={"definizione": body},
        proposed_links=[],
        relations=[],
        sources=[src],
        confidence=0.9,
    )


class BudgetCapsContextTests(unittest.TestCase):
    """The flat-cost proof: many big matching notes, small budget -> capped context."""

    def test_budget_caps_assembled_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            for i in range(5):
                write_note(paths, _big_note(f"Nota {i}"))
            rebuild_indexes(paths)
            graph = load_graph(paths.graph_file)
            index = BM25Index.load(paths.index_file)

            tight = build_context_bundle(paths, graph, index, "argomento comune", budget_tokens=300)
            total = sum(estimate_tokens(i["content"]) for i in tight.items)
            self.assertLessEqual(total, 300)
            self.assertLess(len(tight.items), 5)

            roomy = build_context_bundle(
                paths, graph, index, "argomento comune", budget_tokens=1_000_000
            )
            self.assertGreater(len(roomy.items), len(tight.items))


if __name__ == "__main__":
    unittest.main()
