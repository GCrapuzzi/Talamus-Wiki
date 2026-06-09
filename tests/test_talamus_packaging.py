import unittest
from pathlib import Path

import talamus


class PackagingTests(unittest.TestCase):
    def test_py_typed_marker_ships(self) -> None:
        """PEP 561: the marker must sit next to the package so SDK users get types."""
        marker = Path(talamus.__file__).parent / "py.typed"
        self.assertTrue(marker.is_file())

    def test_version_is_exposed(self) -> None:
        self.assertTrue(talamus.__version__)


if __name__ == "__main__":
    unittest.main()
