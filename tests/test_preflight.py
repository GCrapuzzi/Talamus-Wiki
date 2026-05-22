import subprocess
import unittest
from unittest.mock import patch

from tools.fde_brain.preflight import CheckResult, check_cli, check_ollama_model


class PreflightTests(unittest.TestCase):
    @patch("tools.fde_brain.preflight.shutil.which", return_value="C:/bin/claude.cmd")
    def test_check_cli_reports_present_command(self, _which) -> None:
        result = check_cli("Claude Code", "claude")

        self.assertEqual(CheckResult("Claude Code", True, "C:/bin/claude.cmd"), result)

    @patch("tools.fde_brain.preflight.shutil.which", return_value=None)
    def test_check_cli_reports_missing_command(self, _which) -> None:
        result = check_cli("Graphify", "graphify")

        self.assertEqual("Graphify", result.name)
        self.assertFalse(result.ok)
        self.assertEqual("graphify not found on PATH", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_reports_present_model(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nglm-ocr:latest abc 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertTrue(result.ok)
        self.assertEqual("GLM-OCR model", result.name)
        self.assertEqual("glm-ocr found in ollama list", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_reports_missing_model(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nllama3 abc 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertFalse(result.ok)
        self.assertEqual("glm-ocr not found in ollama list", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_rejects_model_name_substrings(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout=(
                "NAME ID SIZE MODIFIED\n"
                "not-glm-ocr:latest abc 1 GB today\n"
                "glm-ocr2 def 1 GB today\n"
            ),
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertFalse(result.ok)
        self.assertEqual("glm-ocr not found in ollama list", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_rejects_metadata_only_matches(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nllama3 glm-ocr 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertFalse(result.ok)
        self.assertEqual("glm-ocr not found in ollama list", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_tagged_request_requires_exact_model_name(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nglm-ocr:latest abc 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr:latest")

        self.assertTrue(result.ok)
        self.assertEqual("glm-ocr:latest found in ollama list", result.detail)


if __name__ == "__main__":
    unittest.main()
