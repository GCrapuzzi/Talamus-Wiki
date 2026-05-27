import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.fde_brain.distill_local import LocalDistillResult, LocalPromotedNote
from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.rerun_local_distill import main


class RerunLocalDistillTests(unittest.TestCase):
    @patch("tools.fde_brain.rerun_local_distill.distill_normalized_sections")
    def test_package_rerun_writes_notes_registry_run_log_and_progress(self, distill_mock) -> None:
        promoted_md = (
            "---\ntype: concept\nstatus: evergreen\naliases:\n  - Test Concept\n"
            "tags:\n  - ai-engineering\nsources:\n  - raw_path: x\n    normalized_path: y\n"
            "created: 2026-05-26\nupdated: 2026-05-26\n---\n\n# Test Concept\n\n"
            "## Summary\n\nSummary.\n\n## Core Idea\n\nCore.\n\n## Practical Use\n\nUse.\n\n## Related\n\n- \n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()
            raw = paths.raw_for("pdf") / "book.pdf"
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(b"pdf")
            package = paths.normalized_for("pdf") / "book"
            sections = package / "sections"
            sections.mkdir(parents=True, exist_ok=True)
            section = sections / "001-book.md"
            section.write_text("---\n---\n\n# Book\n", encoding="utf-8")
            quality = package / "quality-report.json"
            quality.write_text("{}", encoding="utf-8")
            manifest = package / "manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "source": {
                            "raw_path": "AI Space/raw/pdf/book.pdf",
                            "raw_hash": "sha256:abc",
                            "source_type": "pdf",
                            "captured_at": "2026-05-26T10:00:00+00:00",
                        },
                        "parser": "pypdf",
                        "sections": [
                            {
                                "section_id": "001",
                                "title": "Book",
                                "path": "AI Space/normalized/pdf/book/sections/001-book.md",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            distill_mock.return_value = LocalDistillResult(
                ok=True,
                notes=[
                    LocalPromotedNote(
                        title="Test Concept",
                        type="concept",
                        content=promoted_md,
                        source_section=section,
                        confidence=0.9,
                    )
                ],
            )

            exit_code = main(
                [
                    "--root",
                    str(root),
                    "--package",
                    "AI Space/normalized/pdf/book",
                    "--distill-num-ctx",
                    "32768",
                ]
            )

            self.assertEqual(0, exit_code)
            self.assertTrue((paths.fde_brain / "Test-Concept.md").exists())
            distill_mock.assert_called_once()
            self.assertEqual(32768, distill_mock.call_args.kwargs["num_ctx"])
            self.assertIn("progress", distill_mock.call_args.kwargs["progress_path"].as_posix())
            registry = json.loads(paths.registry_path.read_text(encoding="utf-8"))
            self.assertEqual("AI Space/raw/pdf/book.pdf", registry["entries"][0]["raw_path"])
            self.assertEqual(["FDE Brain/Test-Concept.md"], registry["entries"][0]["promoted_to"])
            self.assertTrue(paths.brain_graph_stale.exists())
            self.assertTrue(paths.source_graph_stale.exists())
            self.assertEqual(1, len(list(paths.logs_runs.glob("*.json"))))


if __name__ == "__main__":
    unittest.main()
