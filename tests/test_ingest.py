import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.fde_brain.distill import DistillResult
from tools.fde_brain.ingest import main
from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.preflight import CheckResult


def _setup_workspace(root: Path) -> WorkspacePaths:
    paths = WorkspacePaths(root)
    paths.ensure_directories()
    paths.agent_protocol.write_text("# protocol\n", encoding="utf-8")
    paths.runbook.write_text("# runbook\n", encoding="utf-8")
    paths.claude_entrypoint.write_text("# claude\n", encoding="utf-8")
    paths.codex_entrypoint.write_text("# codex\n", encoding="utf-8")
    return paths


def _all_ok_preflight() -> list[CheckResult]:
    return [
        CheckResult("Claude Code", True, "ok"),
        CheckResult("Codex CLI", True, "ok"),
        CheckResult("Ollama", True, "ok"),
        CheckResult("GLM-OCR model", True, "ok"),
        CheckResult("Graphify", True, "ok"),
        CheckResult("Git", True, "ok"),
    ]


class IngestIntegrationTests(unittest.TestCase):
    @patch("tools.fde_brain.ingest.distill_via_claude")
    @patch("tools.fde_brain.ingest.run_preflight", side_effect=_all_ok_preflight)
    def test_markdown_passes_through_without_promotion(self, _pf, distill_mock) -> None:
        distill_mock.return_value = DistillResult(
            ok=True, promoted=False, note_content=None, note_slug=None, raw_response="NO_PROMOTION"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = _setup_workspace(root)
            (paths.pending / "note.md").write_text("# Hello\nBody.", encoding="utf-8")

            exit_code = main(["--root", str(root), "--no-commit"])

            self.assertEqual(0, exit_code)
            self.assertFalse((paths.pending / "note.md").exists())
            raw_files = list(paths.raw_for("markdown").iterdir())
            raw_files = [p for p in raw_files if p.name != ".gitkeep"]
            self.assertEqual(1, len(raw_files))
            self.assertTrue(raw_files[0].name.endswith("note.md"))
            self.assertTrue((paths.normalized_for("markdown") / "note.md").exists())
            self.assertTrue(paths.registry_path.exists())
            data = json.loads(paths.registry_path.read_text(encoding="utf-8"))
            self.assertEqual(1, len(data["entries"]))
            self.assertEqual([], list(paths.fde_brain.glob("*.md")))
            log_files = list(paths.logs_runs.glob("*.json"))
            self.assertEqual(1, len(log_files))

    @patch("tools.fde_brain.ingest.distill_via_claude")
    @patch("tools.fde_brain.ingest.run_preflight", side_effect=_all_ok_preflight)
    def test_markdown_with_promotion_writes_fde_brain_note(self, _pf, distill_mock) -> None:
        promoted_md = (
            "---\ntype: concept\ntags: [demo]\nsources:\n  - x\n  - y\n"
            "captured-at: 2026-05-22\n---\n\n# Demo\n\nSummary.\n"
        )
        distill_mock.return_value = DistillResult(
            ok=True, promoted=True, note_content=promoted_md, note_slug="hello",
            raw_response=promoted_md,
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = _setup_workspace(root)
            (paths.pending / "hello.md").write_text("# Hello\nBody.", encoding="utf-8")

            exit_code = main(["--root", str(root), "--no-commit"])

            self.assertEqual(0, exit_code)
            promoted = paths.fde_brain / "hello.md"
            self.assertTrue(promoted.exists())
            self.assertEqual(promoted_md, promoted.read_text(encoding="utf-8"))

    @patch("tools.fde_brain.ingest.distill_via_claude")
    @patch("tools.fde_brain.ingest.run_preflight", side_effect=_all_ok_preflight)
    def test_unknown_extension_routes_to_review(self, _pf, distill_mock) -> None:
        distill_mock.return_value = DistillResult(
            ok=True, promoted=False, note_content=None, note_slug=None, raw_response="NO_PROMOTION"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = _setup_workspace(root)
            (paths.pending / "weird.xyz").write_bytes(b"binary blob")

            exit_code = main(["--root", str(root), "--no-commit"])

            self.assertEqual(0, exit_code)
            review_files = list((paths.review / "needs-human").glob("*.md"))
            self.assertEqual(1, len(review_files))
            distill_mock.assert_not_called()

    @patch("tools.fde_brain.ingest.run_preflight", side_effect=_all_ok_preflight)
    def test_empty_pending_no_changes(self, _pf) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _setup_workspace(root)

            exit_code = main(["--root", str(root), "--no-commit"])

            self.assertEqual(0, exit_code)

    @patch("tools.fde_brain.ingest.run_preflight")
    def test_preflight_failure_returns_one(self, pf_mock) -> None:
        pf_mock.return_value = [CheckResult("Graphify", False, "missing")]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _setup_workspace(root)

            exit_code = main(["--root", str(root), "--no-commit"])

            self.assertEqual(1, exit_code)


if __name__ == "__main__":
    unittest.main()
