"""Batteria 'modello ostile': il prodotto deve restare eccellente anche con
motori deboli (regola di prodotto, 2026-06-12 — il focus è QUALSIASI utente,
non il brain di prova). I modelli economici rispondono con JSON troncato,
malformato, vuoto, avvolto in prosa, control character letterali: ogni punto
del motore che consuma output LLM deve degradare con grazia, mai corrompere."""

import tempfile
import unittest
from pathlib import Path

from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.store import rebuild_indexes, write_note
from tests.support import FakeLLMProvider

HOSTILE = [
    "",  # vuoto
    "Sure! Here are the results you asked for.",  # prosa senza JSON
    '[{"title": "Rotto",',  # troncato
    '{"oggetto": "non array"}',  # tipo sbagliato
    '```json\n[{"id": 1}]\n```extra',  # fence + spazzatura
]


def _note(title: str) -> CanonicalNote:
    return CanonicalNote.minimal(
        title, sources=[SourceRef("raw/a.md", "raw/a.md#1", "s", "sha256:x", ["c"])]
    )


def _brain(tmp: str, titles: list[str]) -> TalamusPaths:
    paths = TalamusPaths(Path(tmp))
    paths.ensure_directories()
    for title in titles:
        write_note(paths, _note(title))
    rebuild_indexes(paths)
    return paths


class HostileExtractionTests(unittest.TestCase):
    def test_extract_raises_actionable_error_not_garbage(self) -> None:
        from talamus.extract import extract_notes
        from talamus.normalize import normalize_text

        package = normalize_text("raw/a.md", "Testo sorgente.")
        for raw in HOSTILE:
            try:
                notes = extract_notes(package, FakeLLMProvider([raw]))
            except ValueError:
                continue  # errore pulito e azionabile: accettabile
            self.assertEqual(notes, [])  # altrimenti lista vuota: MAI note corrotte

    def test_control_characters_in_strings_are_tolerated(self) -> None:
        from talamus.extract import _extract_json_array

        raw = '[{"title": "Nota\ncon a capo", "summary": "ok"}]'
        parsed = _extract_json_array(raw)
        self.assertEqual(len(parsed), 1)


class HostileRoutingTests(unittest.TestCase):
    def test_garbage_routing_falls_back_to_index_path(self) -> None:
        from talamus.ask import answer_question
        from talamus.domains import save_overview

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp, ["Concetto"])
            save_overview(paths, [{"name": "Dominio", "description": "d", "members": ["Concetto"]}])
            for raw in HOSTILE:
                trace: dict = {}
                llm = FakeLLMProvider([raw, raw, raw, "Risposta [1]."])
                answer = answer_question(paths, "concetto", llm, trace=trace)
                self.assertNotIn("Traceback", answer)
                self.assertTrue(trace["items_read"])  # qualcosa viene SEMPRE letto


class HostileDomainsTests(unittest.TestCase):
    def test_batched_induction_survives_garbage(self) -> None:
        from talamus.domains import _name_domains_batched

        clusters = [[f"N{i}" for i in range(30)], ["A", "B", "C"], ["Sola"]]
        summaries = {t: "s" for c in clusters for t in c}
        for raw in HOSTILE:
            domains = _name_domains_batched(clusters, summaries, FakeLLMProvider([raw] * 5))
            members = sorted(m for d in domains for m in d["members"])
            self.assertEqual(members, sorted(summaries))  # ogni nota resta mappata


class HostileEnrichTests(unittest.TestCase):
    def test_enrich_never_pollutes_retrieval_text(self) -> None:
        from talamus.enrich import enrich_notes
        from talamus.store import load_notes

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp, ["Concetto"])
            original = load_notes(paths)[0].retrieval_text
            junk = (
                '[{"id": "concetto", "symptoms": "' + "x" * 800 + '"}]',  # oltre il tetto
                '[{"id": "concetto", "symptoms": "{\\"json\\": \\"dentro\\"}"}]',  # struttura
                *HOSTILE,
            )
            for raw in junk:
                report = enrich_notes(paths, FakeLLMProvider([raw]))
                self.assertEqual(report["enriched"], 0)
            self.assertEqual(load_notes(paths)[0].retrieval_text, original)


class HostileConsolidateTests(unittest.TestCase):
    def test_detection_returns_empty_not_wrong(self) -> None:
        from talamus.consolidate import find_duplicates

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp, ["Alfa", "Beta"])
            for raw in HOSTILE:
                self.assertEqual(find_duplicates(paths, FakeLLMProvider([raw])), [])


if __name__ == "__main__":
    unittest.main()
