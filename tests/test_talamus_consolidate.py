import json
import tempfile
import unittest
from pathlib import Path

from talamus.consolidate import apply_consolidation, find_duplicates
from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.store import load_notes, write_note
from tests.support import FakeLLMProvider


def _note(title: str) -> CanonicalNote:
    return CanonicalNote.minimal(
        title, sources=[SourceRef("raw", "norm", "loc", "sha256:x", ["claim"])]
    )


class ConsolidateTests(unittest.TestCase):
    def test_find_duplicates_lists_groups(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            write_note(paths, _note("Hybrid search"))
            write_note(paths, _note("Ricerca ibrida"))
            llm = FakeLLMProvider(
                [
                    json.dumps(
                        [
                            {
                                "canonical": "Hybrid search",
                                "members": ["Hybrid search", "Ricerca ibrida"],
                            }
                        ]
                    )
                ]
            )

            groups = find_duplicates(paths, llm)

            self.assertEqual(1, len(groups))
            self.assertEqual("Hybrid search", groups[0]["canonical"])

    def test_apply_merges_cross_language_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            write_note(paths, _note("Hybrid search"))
            write_note(paths, _note("Ricerca ibrida"))
            llm = FakeLLMProvider(
                [
                    json.dumps(
                        [
                            {
                                "canonical": "Hybrid search",
                                "members": ["Hybrid search", "Ricerca ibrida"],
                            }
                        ]
                    )
                ]
            )

            merged = apply_consolidation(paths, llm)

            self.assertEqual(1, merged)
            notes = load_notes(paths)
            self.assertEqual(1, len(notes))
            self.assertEqual("Hybrid search", notes[0].title)
            self.assertIn("Ricerca ibrida", notes[0].aliases)

    def test_no_duplicates_changes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            write_note(paths, _note("Alpha"))
            write_note(paths, _note("Beta"))

            merged = apply_consolidation(paths, FakeLLMProvider([json.dumps([])]))

            self.assertEqual(0, merged)
            self.assertEqual(2, len(load_notes(paths)))


if __name__ == "__main__":
    unittest.main()
