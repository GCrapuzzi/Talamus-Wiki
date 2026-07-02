import json
import tempfile
import unittest
from pathlib import Path

from talamus.models import CanonicalNote, Relation, SourceRef
from talamus.ontology import build_ontology
from talamus.ontology_lab import (
    cluster_unexplained,
    collect_evidence,
    coverage,
    induce_candidates,
    load_schema,
    ontology_eval,
    promote_candidate,
    read_history,
    reject_candidate,
    stability,
    surface_key,
)
from talamus.paths import TalamusPaths
from talamus.routing import StaticRouter
from talamus.store import load_notes, rebuild_indexes, write_note
from tests.support import FakeLLMProvider


def _note(title: str, retrieval: str, relations: list[tuple[str, str]]) -> CanonicalNote:
    src = SourceRef("raw/a.md", "norm/a#1", "s", "sha256:x", ["c"])
    return CanonicalNote(
        note_id=title.lower().replace(" ", "-"),
        title=title,
        aliases=[],
        folder="",
        tags=[],
        summary=f"{title}.",
        retrieval_text=retrieval,
        body_sections={"d": retrieval},
        proposed_links=[],
        relations=[Relation(title, rel, target, 0.9) for rel, target in relations],
        sources=[src],
        confidence=0.9,
    )


def _brain(tmp: str) -> TalamusPaths:
    """Three notes whose relations use the free-form surface 'alimenta' — a surface
    the fixed types flatten to `related` (the information the lab must recover)."""
    paths = TalamusPaths(Path(tmp))
    paths.ensure_directories()
    write_note(paths, _note("Compilatore", "compilatore note schede", [
        ("collegato a", "Archivio"),      # genuinely vague -> related
        ("alimenta", "Hub Sync"),  # unexplained surface -> candidate material
    ]))  # fmt: skip
    write_note(paths, _note("Estrattore", "estrattore llm concetti", [("alimenta", "Compilatore")]))
    write_note(paths, _note("Scanner", "scanner repository codice", [("alimenta", "Compilatore")]))
    write_note(paths, _note("Hub Sync", "hub sync puntatori brain", []))
    write_note(paths, _note("Archivio", "deposito vecchi fascicoli", []))
    rebuild_indexes(paths)
    return paths


def _naming_response(key: str) -> str:
    return json.dumps(
        [
            {
                "cluster_key": key,
                "name": "alimenta",
                "definition": "Il soggetto fornisce dati o contenuto al bersaglio.",
                "inverse": "alimentato-da",
            }
        ]
    )


class _IsolatedHomeTest(unittest.TestCase):
    """Each test gets its own TALAMUS_HOME: the ontology schema is machine-wide
    by default (global scope), so schema-writing tests must never share state
    or touch the developer's real home."""

    def setUp(self) -> None:
        import os
        from unittest.mock import patch as _patch

        self._home = tempfile.TemporaryDirectory()
        patcher = _patch.dict(os.environ, {"TALAMUS_HOME": self._home.name})
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self._home.cleanup)


class EvidenceTests(_IsolatedHomeTest):
    def test_collects_raw_surfaces_with_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            evidence = collect_evidence(paths)
            surfaces = {e.predicate_surface for e in evidence}
            self.assertIn("alimenta", surfaces)
            record = next(e for e in evidence if e.predicate_surface == "alimenta")
            self.assertTrue(record.source_ref)
            self.assertEqual(record.suggested_type, "related")  # fixed types can't explain it

    def test_clusters_only_unexplained(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            clusters = cluster_unexplained(collect_evidence(paths))
            self.assertIn(surface_key("alimenta"), clusters)
            self.assertEqual(len(clusters[surface_key("alimenta")]), 3)


class InductionTests(_IsolatedHomeTest):
    def test_induces_candidate_with_support_and_examples(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            self.assertEqual(len(created), 1)
            candidate = created[0]
            self.assertEqual(candidate.status, "candidate")
            self.assertEqual(candidate.support, 3)
            self.assertEqual(candidate.distinct_notes, 3)
            self.assertTrue(candidate.examples)
            # persisted in the schema + history event + review item
            self.assertIsNotNone(load_schema(paths).by_id(candidate.id))
            self.assertTrue(any(e["event"] == "candidate_induced" for e in read_history(paths)))

    def test_reinduction_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            induce_candidates(paths, StaticRouter(FakeLLMProvider([_naming_response(key)])))
            again = induce_candidates(paths, StaticRouter(FakeLLMProvider([_naming_response(key)])))
            self.assertEqual(again, [])  # surface already known to the schema

    def test_candidates_do_not_touch_runtime(self) -> None:
        """F5.10: a candidate must NOT re-type edges until promoted."""
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            induce_candidates(paths, StaticRouter(FakeLLMProvider([_naming_response(key)])))
            rebuild_indexes(paths)
            cov = coverage(paths)
            self.assertEqual(cov["non_related"], 0)  # everything still `related`


class PromotionTests(_IsolatedHomeTest):
    def test_under_supported_candidate_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            ok, message = promote_candidate(paths, created[0].id)
            self.assertFalse(ok)  # support 3 < 8 (rule 12.6)
            self.assertIn("12.6", message)

    def test_forced_promotion_retypes_edges_and_raises_coverage(self) -> None:
        """The end-to-end loop: promote -> build_ontology re-types -> coverage up."""
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            ok, _ = promote_candidate(paths, created[0].id, force=True)
            self.assertTrue(ok)
            cov = coverage(paths)
            self.assertEqual(cov["non_related"], 3)  # the three 'alimenta' edges
            schema = load_schema(paths)
            self.assertEqual(schema.by_id(created[0].id).status, "active")
            self.assertGreaterEqual(schema.version, 2)  # promotion bumps the version
            self.assertTrue(any(e["event"] == "promoted" for e in read_history(paths)))

    def test_reject_keeps_the_candidate_in_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            ok, _ = reject_candidate(paths, created[0].id, "non convincente")
            self.assertTrue(ok)
            kept = load_schema(paths).by_id(created[0].id)
            self.assertEqual(kept.status, "deprecated")  # kept, never deleted
            self.assertTrue(any(e["event"] == "rejected" for e in read_history(paths)))


class RetrievalLiftTests(_IsolatedHomeTest):
    def test_promoted_type_reorders_expansion_deterministically(self) -> None:
        """The honest proof that MEANING earns its keep: with the promoted type,
        the typed edge is expanded BEFORE the vague `related` one — so when the
        context limit cuts, the right note makes it in. Tested on the expansion
        ordering itself (deterministic, immune to lexical-channel noise)."""
        from talamus.ontology import build_ontology, neighbors
        from talamus.ontology_lab import active_surface_map

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            notes = load_notes(paths)

            def first_expanded(ontology: dict) -> str:
                ordered = sorted(
                    neighbors(ontology, "Compilatore"),
                    key=lambda n: 0 if n.get("relation") != "related" else 1,
                )
                return str(ordered[0]["title"])

            baseline_first = first_expanded(build_ontology(notes, None))
            self.assertEqual(baseline_first, "Archivio")  # edge order: the vague edge
            promote_candidate(paths, created[0].id, force=True)
            emergent_first = first_expanded(build_ontology(notes, active_surface_map(paths)))
            self.assertEqual(emergent_first, "Hub Sync")  # the typed edge wins the cut

    def test_ontology_eval_reports_structure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            created = induce_candidates(
                paths, StaticRouter(FakeLLMProvider([_naming_response(key)]))
            )
            promote_candidate(paths, created[0].id, force=True)
            cases_file = Path(tmp) / "cases.json"
            cases_file.write_text(
                json.dumps(
                    [{"question": "compilatore", "relevant": ["Compilatore"], "category": "o"}]
                ),
                encoding="utf-8",
            )
            report = ontology_eval(paths, cases_file, k=3)
            self.assertIn("baseline", report)
            self.assertIn("emergent", report)
            self.assertGreaterEqual(report["lift"]["recall_at_k"], 0.0)
            self.assertGreater(report["coverage"]["non_related"], 0)


class StabilityTests(_IsolatedHomeTest):
    def test_unchanged_corpus_is_fully_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            result = stability(paths, runs=3)
            self.assertEqual(result["jaccard"], 1.0)


class CliOntologyTests(_IsolatedHomeTest):
    def test_full_cli_flow(self) -> None:
        import io
        from contextlib import redirect_stdout

        from talamus.cli import main

        with tempfile.TemporaryDirectory() as tmp:
            paths = _brain(tmp)
            key = surface_key("alimenta")
            llm = FakeLLMProvider([_naming_response(key)])
            self.assertEqual(0, main(["ontology", "induce", "--root", tmp], llm=llm))
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(0, main(["ontology", "review", "--root", tmp]))
            self.assertIn("rel:alimenta", out.getvalue())
            self.assertEqual(
                0, main(["ontology", "apply", "rel:alimenta", "--force", "--root", tmp])
            )
            self.assertEqual(0, main(["ontology", "status", "--root", tmp]))
            self.assertEqual(0, main(["ontology", "history", "--root", tmp]))
            self.assertEqual(0, main(["ontology", "export", "--root", tmp]))
            self.assertEqual(0, main(["ontology", "stability", "--root", tmp]))
            # notes never moved: still 5 markdown files
            self.assertEqual(len(list(load_notes(paths))), 5)

    def test_apply_without_force_fails_below_thresholds(self) -> None:
        import io
        from contextlib import redirect_stderr

        from talamus.cli import main

        with tempfile.TemporaryDirectory() as tmp:
            _brain(tmp)
            key = surface_key("alimenta")
            main(
                ["ontology", "induce", "--root", tmp], llm=FakeLLMProvider([_naming_response(key)])
            )
            err = io.StringIO()
            with redirect_stderr(err):
                code = main(["ontology", "apply", "rel:alimenta", "--root", tmp])
            self.assertEqual(1, code)


class BuildOntologyHookTests(_IsolatedHomeTest):
    def test_emergent_surfaces_param_types_edges(self) -> None:
        notes = [
            _note("A", "a", [("alimenta", "B")]),
            _note("B", "b", []),
        ]
        plain = build_ontology(notes)
        self.assertEqual(plain["edges"][0]["type"], "related")
        typed = build_ontology(notes, {surface_key("alimenta"): "alimenta"})
        self.assertEqual(typed["edges"][0]["type"], "alimenta")


if __name__ == "__main__":
    unittest.main()
