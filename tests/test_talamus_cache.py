import tempfile
import unittest
from pathlib import Path

from talamus.paths import TalamusPaths
from talamus.store import CACHE_VERSION, cache_is_current, cache_version, rebuild_indexes


class CacheVersionTests(unittest.TestCase):
    def test_missing_cache_is_not_current(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            self.assertIsNone(cache_version(paths))
            self.assertFalse(cache_is_current(paths))

    def test_rebuild_writes_current_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            rebuild_indexes(paths)
            self.assertEqual(CACHE_VERSION, cache_version(paths))
            self.assertTrue(cache_is_current(paths))


if __name__ == "__main__":
    unittest.main()
