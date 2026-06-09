import os
import tempfile
import unittest
from pathlib import Path

from talamus.config import TalamusConfig, load_config, load_or_default, save_config
from talamus.errors import ConfigError


class ConfigTests(unittest.TestCase):
    def test_load_or_default_when_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_or_default(Path(tmp) / "talamus.json")
            self.assertEqual(TalamusConfig.default(), cfg)

    def test_env_override(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "talamus.json"
            save_config(path, TalamusConfig.default())
            os.environ["TALAMUS_LLM_PROVIDER"] = "ollama"
            try:
                self.assertEqual("ollama", load_or_default(path).llm_provider)
            finally:
                del os.environ["TALAMUS_LLM_PROVIDER"]

    def test_invalid_json_raises_config_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "talamus.json"
            path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
