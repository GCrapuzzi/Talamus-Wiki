"""A1 (D3): setup verifies the chosen engine with one live probe call and, on
failure, gives an actionable per-engine hint instead of declaring success."""

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

from talamus.cli import main
from talamus.errors import EngineFailed
from tests.support import FakeLLMProvider


class _DownLLM:
    def complete(self, prompt: str) -> str:
        raise EngineFailed("boom: engine unreachable")


class SetupEngineVerifyTests(unittest.TestCase):
    def test_verify_engine_probes_and_reports_success(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            llm = FakeLLMProvider(["ok"])
            out = io.StringIO()
            with redirect_stdout(out):
                code = main(["setup", "--root", tmp, "--capture", "no", "--verify-engine"], llm=llm)

            self.assertEqual(0, code)
            self.assertEqual(1, len(llm.prompts))
            self.assertIn("engine verified", out.getvalue().lower())

    def test_verify_engine_failure_prints_actionable_hint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = io.StringIO()
            err = io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                code = main(
                    [
                        "setup",
                        "--root",
                        tmp,
                        "--engine",
                        "opencode",
                        "--capture",
                        "no",
                        "--verify-engine",
                    ],
                    llm=_DownLLM(),
                )

            self.assertEqual(0, code)  # brain + MCP + hook are still valid work
            combined = out.getvalue() + err.getvalue()
            self.assertIn("not verified", combined.lower())
            self.assertIn("opencode auth login", combined)

    def test_non_interactive_setup_skips_the_probe_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            llm = FakeLLMProvider(["ok"])
            fake_stdin = io.StringIO()  # isatty() False
            with redirect_stdout(io.StringIO()), mock.patch("sys.stdin", fake_stdin):
                code = main(["setup", "--root", tmp, "--capture", "no"], llm=llm)

            self.assertEqual(0, code)
            self.assertEqual(0, len(llm.prompts))

    def test_no_verify_engine_flag_forces_skip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            llm = FakeLLMProvider(["ok"])
            with redirect_stdout(io.StringIO()):
                code = main(
                    ["setup", "--root", tmp, "--capture", "no", "--no-verify-engine"], llm=llm
                )

            self.assertEqual(0, code)
            self.assertEqual(0, len(llm.prompts))


if __name__ == "__main__":
    unittest.main()
