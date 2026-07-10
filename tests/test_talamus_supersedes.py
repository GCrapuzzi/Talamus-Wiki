"""Freshness by default: when a note supersedes an older one, the old note is
never deleted — it moves into the bitemporal record (open claims closed by the
successor, the handover itself recorded as a claim, a typed `supersedes` edge
in the graph) and default answers read only the successor. The past stays
reachable through history and --as-of."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from talamus.linking import NoteRegistry
from talamus.models import CanonicalNote, SourceRef
from talamus.naming import note_filename
from talamus.ontology import normalize_relation
from talamus.paths import TalamusPaths
from talamus.routing import StaticRouter
from talamus.store import load_notes, rebuild_indexes, render_note_markdown, write_note_json
from talamus.temporal import current_claims, record_claim, record_supersedes
from tests.support import FakeLLMProvider

OLD_TITLE = "Procedura Rimborsi 2025"
NEW_TITLE = "Procedura Rimborsi 2026"


def _note(note_id: str, title: str, summary: str) -> CanonicalNote:
    return CanonicalNote(
        note_id=note_id,
        title=title,
        aliases=[],
        folder="",
        tags=["procedure"],
        summary=summary,
        retrieval_text="procedura rimborsi spese expense reimbursement procedure",
        body_sections={"core_idea": summary},
        proposed_links=[],
        relations=[],
        sources=[
            SourceRef(
                raw_path="raw/procedure.md",
                normalized_path="normalized/procedure#1",
                locator="",
                source_hash="sha256:abc",
                supported_claims=[summary],
            )
        ],
        confidence=0.9,
    )


def _brain(tmp: str) -> TalamusPaths:
    paths = TalamusPaths(Path(tmp))
    paths.ensure_directories()
    old = _note("rimborsi-2025", OLD_TITLE, "Si invia il modulo cartaceo entro 30 giorni.")
    new = _note("rimborsi-2026", NEW_TITLE, "Si carica la ricevuta nel portale entro 15 giorni.")
    for note in (old, new):
        write_note_json(paths, note)
    registry = NoteRegistry.from_notes(load_notes(paths))
    for note in load_notes(paths):
        render_note_markdown(paths, note, registry)
    rebuild_indexes(paths)
    return paths


class SupersedesTypeTests(unittest.TestCase):
    def test_supersedes_is_a_system_relation_type(self) -> None:
        self.assertEqual("supersedes", normalize_relation("supersedes"))
        self.assertEqual("supersedes", normalize_relation("sostituisce"))
        self.assertEqual("supersedes", normalize_relation("replaces"))


class RecordSupersedesTests(unittest.TestCase):
    def test_old_note_is_kept_and_moves_into_the_bitemporal_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            open_claim = record_claim(paths, "rimborsi-2025", "Il modulo cartaceo è la via.")

            result = record_supersedes(paths, OLD_TITLE, NEW_TITLE)

            notes = {note.title: note for note in load_notes(paths)}
            # never deleted: the old note is still there, prose intact
            self.assertIn(OLD_TITLE, notes)
            self.assertIn("modulo cartaceo", notes[OLD_TITLE].summary)
            # its open claim was closed by the successor (invalidated, not removed)
            still_open = {c.claim_id for c in current_claims(paths, "rimborsi-2025")}
            self.assertNotIn(open_claim.claim_id, still_open)
            # the handover itself is recorded as a claim naming the successor
            self.assertTrue(
                any(NEW_TITLE in c.text for c in current_claims(paths, "rimborsi-2025"))
            )
            # the typed edge lives on the successor note and in the ontology
            new_note = notes[NEW_TITLE]
            self.assertTrue(
                any(
                    r.relation == "supersedes" and r.target == OLD_TITLE for r in new_note.relations
                )
            )
            self.assertEqual(OLD_TITLE, result["old"])
            self.assertEqual(NEW_TITLE, result["new"])

    def test_unknown_titles_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            with self.assertRaises(ValueError):
                record_supersedes(paths, "Nota Inesistente", NEW_TITLE)
            with self.assertRaises(ValueError):
                record_supersedes(paths, OLD_TITLE, OLD_TITLE)


class FreshAskTests(unittest.TestCase):
    def test_without_supersedes_both_notes_are_readable(self) -> None:
        from talamus.ask import answer_question

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            trace: dict = {}

            answer_question(
                paths,
                "come funziona la procedura rimborsi?",
                StaticRouter(FakeLLMProvider(["Risposta [1]."])),
                trace=trace,
            )

            read = " ".join(trace.get("items_read", []))
            self.assertIn(note_filename(NEW_TITLE), read)
            self.assertIn(note_filename(OLD_TITLE), read)

    def test_ask_today_reads_only_the_successor_and_sees_dates(self) -> None:
        from talamus.ask import answer_question

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            record_supersedes(paths, OLD_TITLE, NEW_TITLE)
            llm = FakeLLMProvider(["Risposta [1]."])
            trace: dict = {}

            answer = answer_question(
                paths,
                "come funziona la procedura rimborsi?",
                StaticRouter(llm),
                trace=trace,
            )

            read = " ".join(trace.get("items_read", []))
            self.assertIn(note_filename(NEW_TITLE), read)
            self.assertNotIn(note_filename(OLD_TITLE), read)
            self.assertIn("[1]", answer)
            # the answer prompt carries dates and the temporal contract
            prompt = llm.prompts[-1]
            self.assertIn("(updated ", prompt)
            self.assertIn("recently updated one", prompt)
            # the successor carries the handover notice from the bitemporal record
            self.assertIn(f"[fact validity] this note supersedes '{OLD_TITLE}'", prompt)


if __name__ == "__main__":
    unittest.main()
