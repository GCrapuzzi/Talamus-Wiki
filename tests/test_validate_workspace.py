import tempfile
import unittest
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.validate_workspace import ValidationIssue, validate_workspace


class ValidateWorkspaceTests(unittest.TestCase):
    def test_reports_missing_required_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issues = validate_workspace(Path(tmp))

            codes = {issue.code for issue in issues}

            self.assertIn("missing-directory", codes)

    def test_reports_missing_protocol_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()

            issues = validate_workspace(root)

            missing_files = [issue for issue in issues if issue.code == "missing-file"]
            self.assertTrue(any("AGENT_PROTOCOL.md" in issue.path for issue in missing_files))
            self.assertTrue(any("CLAUDE.md" in issue.path for issue in missing_files))
            self.assertTrue(any("AGENTS.md" in issue.path for issue in missing_files))

    def test_clean_workspace_has_no_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()
            paths.agent_protocol.write_text("# Protocol\n", encoding="utf-8")
            paths.runbook.write_text("# Runbook\n", encoding="utf-8")
            paths.claude_entrypoint.write_text("# Claude\n", encoding="utf-8")
            paths.codex_entrypoint.write_text("# Codex\n", encoding="utf-8")

            issues = validate_workspace(root)

            self.assertEqual([], issues)

    def test_validation_issue_formats_as_text(self) -> None:
        issue = ValidationIssue("missing-file", "AGENTS.md", "Create AGENTS.md")

        self.assertEqual("missing-file: AGENTS.md - Create AGENTS.md", str(issue))


if __name__ == "__main__":
    unittest.main()
