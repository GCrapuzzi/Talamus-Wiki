import dataclasses
import tempfile
import unittest
from pathlib import Path

from benchmarks.profiler.stages import cost_per_answer, token_efficiency, verifiability

from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.store import rebuild_indexes, write_note


def _note(title: str) -> CanonicalNote:
    src = SourceRef("raw/a.md", "raw/a.md#1", "s", "sha256:x", ["c"])
    return dataclasses.replace(
        CanonicalNote.minimal(title, sources=[src]),
        summary=f"{title} summary",
        retrieval_text=f"{title} keywords",
    )


def _brain(tmp: str) -> TalamusPaths:
    paths = TalamusPaths(Path(tmp))
    paths.ensure_directories()
    (Path(tmp) / "raw").mkdir(exist_ok=True)
    (Path(tmp) / "raw" / "a.md").write_text("source", encoding="utf-8")
    for t in ("Alpha", "Beta", "Gamma"):
        write_note(paths, _note(t))
    rebuild_indexes(paths)
    return paths


class ProfilerTests(unittest.TestCase):
    def test_token_efficiency_recall_cheaper_than_load_all(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            stats = token_efficiency(paths)
            self.assertEqual(stats["notes"], 3)
            self.assertGreater(stats["load_all_tokens"], 0)
            self.assertLessEqual(stats["search_avg_tokens"], stats["load_all_tokens"])

    def test_verifiability_reports_resolvable_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            stats = verifiability(paths)
            self.assertEqual(stats["notes"], 3)
            self.assertIn("source_resolves_pct", stats)
            self.assertIn("status_counts", stats)

    def test_cost_per_answer_is_zero_eur_by_default(self) -> None:
        out = cost_per_answer(context_tokens=4000, answer_tokens=200, ingest_tokens=100000)
        self.assertEqual(out["eur_per_answer"], 0.0)  # subscription/local = free
        self.assertGreater(out["tokens_per_answer"], 4000)

    def test_cost_per_answer_with_a_price(self) -> None:
        out = cost_per_answer(1000, 0, 0, price_per_1k_tokens_eur=0.01)
        self.assertAlmostEqual(out["eur_per_answer"], 0.01, places=6)


if __name__ == "__main__":
    unittest.main()
