import unittest

from benchmarks.profiler.scale import dense_resident_overhead_mb, talamus_scale


class ScaleTests(unittest.TestCase):
    def test_talamus_scale_returns_latency_and_footprint(self) -> None:
        rows = talamus_scale([20])  # tiny size keeps the synthetic build fast
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["n_notes"], 20)
        self.assertIn("search_p50_ms", row)
        self.assertIn("index_bytes", row)

    def test_dense_overhead_reports_a_contrast(self) -> None:
        out = dense_resident_overhead_mb()
        # whether or not deps are present, it returns a structured contrast line
        self.assertIn("model", out)
        self.assertIn("note", out)


if __name__ == "__main__":
    unittest.main()
