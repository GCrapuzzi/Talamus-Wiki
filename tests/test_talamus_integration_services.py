import json
import tempfile
import unittest
from pathlib import Path

from talamus.services.integrations import (
    build_hook_snippet,
    inspect_integrations,
    install_mcp_config,
)


class TalamusIntegrationServiceTests(unittest.TestCase):
    def test_install_mcp_config_preserves_other_servers_and_reports_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config_path = root / ".mcp.json"
            config_path.write_text(
                json.dumps({"mcpServers": {"other": {"command": "other-mcp"}}}),
                encoding="utf-8",
            )

            result = install_mcp_config(root)
            status = inspect_integrations(root)

            data = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertTrue(result.success, result.message)
        self.assertIsNotNone(result.data)
        self.assertEqual(str(config_path), result.data.config_path)
        self.assertIn("other", data["mcpServers"])
        self.assertEqual("talamus-mcp", data["mcpServers"]["talamus"]["command"])
        self.assertEqual(["--root", str(root)], data["mcpServers"]["talamus"]["args"])
        self.assertTrue(status.success, status.message)
        self.assertIsNotNone(status.data)
        assert status.data is not None
        self.assertTrue(status.data.mcp_installed)

    def test_hook_snippet_contains_session_end_command_for_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            result = build_hook_snippet(root)

        self.assertTrue(result.success, result.message)
        snippet = result.data
        self.assertIsNotNone(snippet)
        assert snippet is not None
        self.assertIn(str(root), snippet.command)
        self.assertEqual(
            snippet.settings["hooks"]["SessionEnd"][0]["hooks"][0]["command"],
            snippet.command,
        )

    def test_inspect_integrations_reports_absent_mcp_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = inspect_integrations(Path(tmp))

        self.assertTrue(result.success, result.message)
        report = result.data
        self.assertIsNotNone(report)
        assert report is not None
        self.assertFalse(report.mcp_installed)
        self.assertTrue(report.mcp_config_path.endswith(".mcp.json"))


if __name__ == "__main__":
    unittest.main()
