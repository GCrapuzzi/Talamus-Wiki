import unittest

from benchmarks.profiler.capability_matrix import COLUMNS, MATRIX, YES, render_markdown


class CapabilityMatrixTests(unittest.TestCase):
    def test_every_talamus_cell_has_evidence(self) -> None:
        for cell in MATRIX["talamus"]:
            self.assertEqual(cell.mark, YES)
            self.assertTrue(cell.evidence.strip(), "a Talamus YES must cite evidence")

    def test_each_system_covers_every_column(self) -> None:
        for system, cells in MATRIX.items():
            self.assertEqual(len(cells), len(COLUMNS), f"{system} missing a column")

    def test_render_lists_systems_and_columns(self) -> None:
        md = render_markdown()
        self.assertIn("talamus", md)
        self.assertIn("vectordb", md)
        self.assertIn("TIME", md)
        self.assertIn("VERIFIABILITY", md)


if __name__ == "__main__":
    unittest.main()
