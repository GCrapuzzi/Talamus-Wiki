import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.fde_brain.distill import DistillResult, distill_via_claude


def _make_note(tmp: Path, name: str = "note.md", body: str = "Some content") -> Path:
    p = tmp / name
    p.write_text(body, encoding="utf-8")
    return p


VALID_PROMOTED = (
    "---\n"
    "type: concept\n"
    "tags: [example]\n"
    "sources:\n  - AI Space/raw/x.md\n  - AI Space/normalized/markdown/x.md\n"
    "captured-at: 2026-05-22\n"
    "---\n\n"
    "# Example concept\n\nSummary text.\n"
)


class DistillTests(unittest.TestCase):
    @patch("tools.fde_brain.distill.subprocess.run")
    def test_promoted_when_response_has_frontmatter(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["claude"], returncode=0, stdout=VALID_PROMOTED, stderr=""
        )
        with tempfile.TemporaryDirectory() as tmp:
            note = _make_note(Path(tmp))

            result = distill_via_claude(normalized_path=note, raw_path=note)

            self.assertTrue(result.ok)
            self.assertTrue(result.promoted)
            self.assertTrue(result.note_content and result.note_content.startswith("---"))
            self.assertEqual("note", result.note_slug)

    @patch("tools.fde_brain.distill.subprocess.run")
    def test_no_promotion_keyword(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["claude"], returncode=0, stdout="NO_PROMOTION", stderr=""
        )
        with tempfile.TemporaryDirectory() as tmp:
            note = _make_note(Path(tmp))

            result = distill_via_claude(normalized_path=note, raw_path=note)

            self.assertTrue(result.ok)
            self.assertFalse(result.promoted)
            self.assertIsNone(result.note_content)

    @patch("tools.fde_brain.distill.subprocess.run")
    def test_timeout_returns_error(self, run_mock) -> None:
        run_mock.side_effect = subprocess.TimeoutExpired(cmd="claude", timeout=10)
        with tempfile.TemporaryDirectory() as tmp:
            note = _make_note(Path(tmp))

            result = distill_via_claude(normalized_path=note, raw_path=note, timeout_sec=10)

            self.assertFalse(result.ok)
            self.assertFalse(result.promoted)
            self.assertIn("timeout", (result.error or "").lower())

    @patch("tools.fde_brain.distill.subprocess.run")
    def test_response_without_frontmatter_not_promoted(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["claude"], returncode=0, stdout="Just a plain response without frontmatter.", stderr=""
        )
        with tempfile.TemporaryDirectory() as tmp:
            note = _make_note(Path(tmp))

            result = distill_via_claude(normalized_path=note, raw_path=note)

            self.assertTrue(result.ok)
            self.assertFalse(result.promoted)
            self.assertIsNone(result.note_content)

    @patch("tools.fde_brain.distill.subprocess.run")
    def test_nonzero_exit_returns_error(self, run_mock) -> None:
        run_mock.return_value = subprocess.CompletedProcess(
            args=["claude"], returncode=2, stdout="", stderr="auth required"
        )
        with tempfile.TemporaryDirectory() as tmp:
            note = _make_note(Path(tmp))

            result = distill_via_claude(normalized_path=note, raw_path=note)

            self.assertFalse(result.ok)
            self.assertIn("auth required", result.error or "")

    def test_result_dataclass_is_frozen(self) -> None:
        r = DistillResult(ok=True, promoted=False, note_content=None, note_slug=None, raw_response="x")
        with self.assertRaises(Exception):
            r.promoted = True  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()
