import tempfile
import unittest
from pathlib import Path

from talamus.config import TalamusConfig, save_config
from talamus.paths import TalamusPaths
from talamus.services.diagnostics import inspect_diagnostics


class TalamusDiagnosticsServiceTests(unittest.TestCase):
    def test_initialized_brain_returns_typed_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            save_config(paths.config_path, TalamusConfig.default())

            result = inspect_diagnostics(tmp)

        self.assertTrue(result.success, result.message)
        report = result.data
        self.assertIsNotNone(report)
        assert report is not None
        self.assertTrue(report.ok)
        self.assertEqual(str(Path(tmp).resolve()), report.root)
        self.assertEqual(TalamusConfig.default().llm_provider, report.llm_provider)
        self.assertIsInstance(report.index_bytes, int)
        self.assertTrue(any(check.check_id == "config" for check in report.checks))
        self.assertTrue(any(check.check_id == "cache" for check in report.checks))

    def test_missing_config_returns_actionable_failure_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()

            result = inspect_diagnostics(tmp)

        self.assertFalse(result.success)
        self.assertEqual("diagnostics_not_initialized", result.code)
        self.assertIn("talamus init", result.message)
        report = result.data
        self.assertIsNotNone(report)
        assert report is not None
        config = next(check for check in report.checks if check.check_id == "config")
        self.assertEqual("error", config.status)
        self.assertIn("talamus init", config.action)

    def test_malformed_config_returns_config_error_without_raising(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            paths.config_path.write_text("{invalid json", encoding="utf-8")

            result = inspect_diagnostics(tmp)

        self.assertFalse(result.success)
        self.assertEqual("diagnostics_config_error", result.code)
        self.assertIn("config error", result.message)
        report = result.data
        self.assertIsNotNone(report)
        assert report is not None
        config = next(check for check in report.checks if check.check_id == "config")
        self.assertEqual("error", config.status)


if __name__ == "__main__":
    unittest.main()
