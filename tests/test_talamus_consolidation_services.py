import json
import tempfile
import unittest
from pathlib import Path

from talamus.paths import TalamusPaths
from talamus.services.consolidation import (
    ConsolidationGroup,
    apply_consolidation_groups,
    list_consolidation_groups,
)
from talamus.store import load_notes, write_note
from tests.support import FakeLLMProvider
from tests.test_talamus_consolidate import _note


class TalamusConsolidationServiceTests(unittest.TestCase):
    def test_list_consolidation_groups_returns_typed_groups(self) -> None:
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

            result = list_consolidation_groups(tmp, llm)

        self.assertTrue(result.success, result.message)
        self.assertEqual("consolidation_groups_loaded", result.code)
        self.assertIsNotNone(result.data)
        assert result.data is not None
        self.assertEqual(1, len(result.data.groups))
        self.assertEqual("Hybrid search", result.data.groups[0].canonical)
        self.assertEqual(("Hybrid search", "Ricerca ibrida"), result.data.groups[0].members)

    def test_apply_reviewed_groups_merges_without_llm(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            write_note(paths, _note("Hybrid search"))
            write_note(paths, _note("Ricerca ibrida"))
            llm = FakeLLMProvider([])
            reviewed = [ConsolidationGroup("Hybrid search", ("Hybrid search", "Ricerca ibrida"))]

            result = apply_consolidation_groups(tmp, llm, reviewed)

            notes = load_notes(paths)

        self.assertTrue(result.success, result.message)
        self.assertEqual("consolidation_applied", result.code)
        self.assertEqual([], llm.prompts)
        self.assertEqual(1, len(notes))
        self.assertIsNotNone(result.data)
        assert result.data is not None
        self.assertEqual(1, result.data.merged)

    def test_apply_detected_groups_uses_existing_detection(self) -> None:
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

            result = apply_consolidation_groups(tmp, llm)

            notes = load_notes(paths)

        self.assertTrue(result.success, result.message)
        self.assertEqual(1, len(llm.prompts))
        self.assertEqual(1, len(notes))
        self.assertIsNotNone(result.data)
        assert result.data is not None
        self.assertEqual(1, result.data.merged)


if __name__ == "__main__":
    unittest.main()
