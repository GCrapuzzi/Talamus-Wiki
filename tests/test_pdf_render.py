import tempfile
import unittest
from pathlib import Path

from fpdf import FPDF

from tools.fde_brain.pdf_render import render_page_png, render_page_to_tempfile


def _make_one_page_pdf(target: Path, text: str = "Hello rendering") -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=20)
    pdf.cell(0, 10, text)
    pdf.output(str(target))


class RenderPagePngTests(unittest.TestCase):
    def test_returns_valid_png_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "sample.pdf"
            _make_one_page_pdf(pdf)

            data = render_page_png(pdf, 0)

            self.assertTrue(data.startswith(b"\x89PNG"))
            self.assertGreater(len(data), 200)

    def test_scale_changes_output_size(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "sample.pdf"
            _make_one_page_pdf(pdf)

            small = render_page_png(pdf, 0, scale=1.0)
            big = render_page_png(pdf, 0, scale=3.0)

            self.assertGreater(len(big), len(small))


class RenderPageToTempfileTests(unittest.TestCase):
    def test_writes_png_to_disk_caller_cleans_up(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "sample.pdf"
            _make_one_page_pdf(pdf)

            out: Path | None = None
            try:
                out = render_page_to_tempfile(pdf, 0)
                self.assertTrue(out.exists())
                self.assertEqual(".png", out.suffix)
                data = out.read_bytes()
                self.assertTrue(data.startswith(b"\x89PNG"))
            finally:
                if out is not None:
                    out.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
