import dataclasses
import tempfile
import unittest
from pathlib import Path

from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.store import write_note
from talamus.timeline import note_history


def _note(title: str, summary: str) -> CanonicalNote:
    base = CanonicalNote.minimal(title, sources=[SourceRef("r", "n", "l", "sha256:x", ["c"])])
    return dataclasses.replace(base, summary=summary, confidence=0.9)


class TimelineTests(unittest.TestCase):
    def test_history_preserves_past_versions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            write_note(paths, _note("X", "first version"))
            write_note(paths, _note("X", "second version"))

            versions = note_history(paths, "X")

            self.assertGreaterEqual(len(versions), 2)
            self.assertTrue(versions[-1].get("updated_at"))

    def test_history_empty_for_unknown_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            self.assertEqual([], note_history(paths, "Nope"))


if __name__ == "__main__":
    unittest.main()
