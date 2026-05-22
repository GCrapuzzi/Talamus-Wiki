import json
import tempfile
import unittest
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.run_log import FileOutcome, RunLog, write_run_log


class RunLogTests(unittest.TestCase):
    def test_write_creates_file_in_logs_runs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()

            log = RunLog(
                run_id="abc12345",
                started_at="2026-05-22T12:34:56+00:00",
                finished_at="2026-05-22T12:35:10+00:00",
                files=[
                    FileOutcome(
                        pending_name="note.md",
                        raw_path="AI Space/raw/markdown/2026-05-22-note.md",
                        normalized_path="AI Space/normalized/markdown/note.md",
                        routed_to="normalized",
                        category="markdown",
                        promoted_to=None,
                        error=None,
                    )
                ],
                commit_hash="0123abc",
                overall_ok=True,
            )

            out = write_run_log(paths, log)

            self.assertTrue(out.exists())
            self.assertEqual(paths.logs_runs, out.parent)
            self.assertTrue(out.name.endswith(".json"))
            self.assertIn("abc12345", out.name)

    def test_filename_uses_started_at_without_colons(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()
            log = RunLog(run_id="ff00", started_at="2026-05-22T12:34:56+00:00")

            out = write_run_log(paths, log)

            self.assertNotIn(":", out.name)
            self.assertIn("2026-05-22T123456", out.name)

    def test_content_is_json_with_expected_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()
            log = RunLog(
                run_id="zz",
                started_at="2026-05-22T12:00:00+00:00",
                overall_ok=False,
            )

            out = write_run_log(paths, log)
            data = json.loads(out.read_text(encoding="utf-8"))

            self.assertEqual("zz", data["run_id"])
            self.assertEqual("2026-05-22T12:00:00+00:00", data["started_at"])
            self.assertFalse(data["overall_ok"])
            self.assertEqual([], data["files"])


if __name__ == "__main__":
    unittest.main()
