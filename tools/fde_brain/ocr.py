from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import ollama

DEFAULT_OCR_MODEL = "glm-ocr:q8_0"
DEFAULT_OCR_NUM_CTX = 16384
OCR_PROMPT = (
    "Extract all text from this image. Return only the extracted text, "
    "preserving structure (paragraphs, lists, headings). No commentary."
)


def _model() -> str:
    return os.environ.get("OCR_MODEL", DEFAULT_OCR_MODEL)


def _num_ctx() -> int:
    raw = os.environ.get("OCR_NUM_CTX")
    if raw is None:
        return DEFAULT_OCR_NUM_CTX
    try:
        return int(raw)
    except ValueError:
        return DEFAULT_OCR_NUM_CTX


@dataclass(frozen=True)
class OcrResult:
    ok: bool
    text: str
    model: str
    error: str | None = None


def extract_text_from_image(image_path: Path) -> OcrResult:
    model = _model()
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": OCR_PROMPT,
                    "images": [str(image_path)],
                }
            ],
            options={"temperature": 0, "num_ctx": _num_ctx()},
        )
        text = response["message"]["content"].strip()
        return OcrResult(ok=True, text=text, model=model)
    except Exception as exc:
        return OcrResult(ok=False, text="", model=model, error=str(exc))
