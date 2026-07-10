"""Supersedes detection at ingest: a new note that replaces an older one is
recognized — applied automatically when the model is confident, proposed to
the review queue when it is not, and always reversible (nothing deleted).
Hostile model output and the kill switch degrade to a plain ingest."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from talamus.ingest import ingest_text
from talamus.linking import NoteRegistry
from talamus.models import CanonicalNote, SourceRef
from talamus.ontology import load_ontology
from talamus.paths import TalamusPaths
from talamus.review import ReviewQueue
from talamus.routing import StaticRouter
from talamus.services.review import apply_review_item
from talamus.store import load_notes, rebuild_indexes, render_note_markdown, write_note_json
from talamus.temporal import current_claims
from tests.support import FakeLLMProvider

OLD_TITLE = "Procedura Rimborsi 2025"


def _old_brain(tmp: str) -> TalamusPaths:
    paths = TalamusPaths(Path(tmp))
    paths.ensure_directories()
    note = CanonicalNote(
        note_id="rimborsi-2025",
        title=OLD_TITLE,
        aliases=[],
        folder="",
        tags=["procedure"],
        summary="Si invia il modulo cartaceo entro 30 giorni.",
        retrieval_text="procedura rimborsi spese expense reimbursement",
        body_sections={"core_idea": "Modulo cartaceo."},
        proposed_links=[],
        relations=[],
        sources=[
            SourceRef(
                raw_path="raw/p.md",
                normalized_path="normalized/p#1",
                locator="",
                source_hash="sha256:abc",
                supported_claims=["Modulo cartaceo."],
            )
        ],
        confidence=0.9,
    )
    write_note_json(paths, note)
    registry = NoteRegistry.from_notes(load_notes(paths))
    render_note_markdown(paths, note, registry)
    rebuild_indexes(paths)
    return paths


def _extraction(title: str) -> str:
    return json.dumps(
        [
            {
                "title": title,
                "retrieval_text": "procedura rimborsi spese portale",
                "summary": "Si carica la ricevuta nel portale entro 15 giorni.",
                "supported_claims": ["Portale."],
                "confidence": 0.9,
            }
        ]
    )


def _verdict(supersedes: bool, confidence: float) -> str:
    return json.dumps(
        {"supersedes": supersedes, "confidence": confidence, "reason": "newer procedure"}
    )


def _supersedes_edges(paths: TalamusPaths) -> list[dict]:
    return [e for e in load_ontology(paths).get("edges", []) if e.get("type") == "supersedes"]


class SupersedesDetectionTests(unittest.TestCase):
    def test_confident_verdict_is_applied_and_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _old_brain(tmp)
            llm = FakeLLMProvider([_extraction("Procedura Rimborsi 2026"), _verdict(True, 0.95)])

            result = ingest_text(paths, "nuova procedura rimborsi", StaticRouter(llm))

            self.assertEqual(1, len(result["supersedes"]["applied"]))
            self.assertEqual(OLD_TITLE, result["supersedes"]["applied"][0]["old"])
            self.assertEqual(1, len(_supersedes_edges(paths)))
            # the handover claim landed on the old note; the old note still exists
            titles = {note.title for note in load_notes(paths)}
            self.assertIn(OLD_TITLE, titles)
            self.assertTrue(any("2026" in c.text for c in current_claims(paths, "rimborsi-2025")))

    def test_uncertain_verdict_goes_to_review_and_apply_records_it(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _old_brain(tmp)
            llm = FakeLLMProvider([_extraction("Procedura Rimborsi 2026"), _verdict(True, 0.5)])

            result = ingest_text(paths, "nuova procedura rimborsi", StaticRouter(llm))

            self.assertEqual(1, len(result["supersedes"]["proposed"]))
            self.assertEqual([], _supersedes_edges(paths))
            pending = [i for i in ReviewQueue(paths).list("pending") if i.kind == "supersedes"]
            self.assertEqual(1, len(pending))

            applied = apply_review_item(str(paths.project_root), pending[0].item_id)

            self.assertTrue(applied.success)
            self.assertEqual(1, len(_supersedes_edges(paths)))

    def test_negative_or_hostile_verdict_changes_nothing(self) -> None:
        for judge in (_verdict(False, 0.99), "not json at all {{{"):
            with tempfile.TemporaryDirectory() as tmp:
                paths = _old_brain(tmp)
                llm = FakeLLMProvider([_extraction("Procedura Rimborsi 2026"), judge])

                result = ingest_text(paths, "nuova procedura", StaticRouter(llm))

                self.assertNotIn("supersedes", result)
                self.assertEqual([], _supersedes_edges(paths))

    def test_unrelated_note_costs_no_extra_llm_call(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _old_brain(tmp)
            llm = FakeLLMProvider([_extraction("Fotosintesi Clorofilliana")])

            ingest_text(paths, "nota di biologia", StaticRouter(llm))

            self.assertEqual(1, len(llm.prompts))  # extraction only, no judge call

    def test_kill_switch_disables_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _old_brain(tmp)
            llm = FakeLLMProvider([_extraction("Procedura Rimborsi 2026")])
            os.environ["TALAMUS_SUPERSEDES_DETECTION"] = "0"
            try:
                result = ingest_text(paths, "nuova procedura", StaticRouter(llm))
            finally:
                del os.environ["TALAMUS_SUPERSEDES_DETECTION"]

            self.assertNotIn("supersedes", result)
            self.assertEqual(1, len(llm.prompts))


if __name__ == "__main__":
    unittest.main()
