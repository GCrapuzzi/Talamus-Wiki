from __future__ import annotations

import io
import sys
import tempfile
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pypdfium2 as pdfium


def render_page_png(pdf_path: Path, page_index: int, *, scale: float = 2.0) -> bytes:
    doc = pdfium.PdfDocument(str(pdf_path))
    try:
        page = doc[page_index]
        bitmap = page.render(scale=scale)
        pil = bitmap.to_pil()
        buf = io.BytesIO()
        pil.save(buf, format="PNG")
        return buf.getvalue()
    finally:
        doc.close()


def render_page_to_tempfile(pdf_path: Path, page_index: int, *, scale: float = 2.0) -> Path:
    data = render_page_png(pdf_path, page_index, scale=scale)
    fd, tmp_name = tempfile.mkstemp(suffix=".png", prefix=f"fdebrain-page-{page_index}-")
    tmp = Path(tmp_name)
    try:
        with open(fd, "wb") as fh:
            fh.write(data)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    return tmp
