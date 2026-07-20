import json
import subprocess
import sys
import tempfile
import tomllib
import unittest
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MCPB_ROOT = ROOT / "packaging" / "mcpb"


class McpbPackageTests(unittest.TestCase):
    def _manifest(self) -> dict[str, Any]:
        return json.loads((MCPB_ROOT / "manifest.json").read_text(encoding="utf-8"))

    def test_bundle_metadata_tracks_the_python_release(self) -> None:
        with (ROOT / "pyproject.toml").open("rb") as handle:
            project = tomllib.load(handle)["project"]
        with (MCPB_ROOT / "pyproject.toml").open("rb") as handle:
            launcher = tomllib.load(handle)["project"]
        manifest = self._manifest()

        version = project["version"]
        self.assertEqual(version, manifest["version"])
        self.assertEqual(version, launcher["version"])
        self.assertEqual([f"talamus[mcp]=={version}"], launcher["dependencies"])

    def test_manifest_references_files_inside_the_bundle(self) -> None:
        manifest = self._manifest()
        server = manifest["server"]

        self.assertEqual("uv", server["type"])
        self.assertTrue((MCPB_ROOT / server["entry_point"]).is_file())
        self.assertTrue((MCPB_ROOT / manifest["icon"]).is_file())
        self.assertTrue((MCPB_ROOT / "uv.lock").is_file())
        self.assertIn("${user_config.brain_directory}", server["mcp_config"]["args"])

    def test_manifest_declares_the_full_mcp_tool_set(self) -> None:
        manifest = self._manifest()
        names = {tool["name"] for tool in manifest["tools"]}
        self.assertEqual(
            {
                "ask",
                "history",
                "ingest_text",
                "neighbors",
                "ontology_status",
                "overview",
                "propose_note",
                "read_note",
                "recall",
                "remember",
                "review_apply",
                "review_list",
                "review_reject",
                "search",
                "sources",
                "verify",
            },
            names,
        )

    def test_smithery_bundle_contains_runtime_tool_schemas(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "talamus-smithery.mcpb"
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "build_smithery_mcpb.py"),
                    str(output),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            with zipfile.ZipFile(output) as archive:
                manifest = json.loads(archive.read("manifest.json"))

        self.assertEqual("python", manifest["server"]["type"])
        self.assertEqual("uv", manifest["server"]["mcp_config"]["command"])
        self.assertEqual(16, len(manifest["tools"]))
        for tool in manifest["tools"]:
            self.assertEqual("object", tool["inputSchema"]["type"])
            self.assertEqual("object", tool["outputSchema"]["type"])


if __name__ == "__main__":
    unittest.main()
