import tempfile
import unittest
from pathlib import Path

from talamus.eval import EvalCase, evaluate, search_retriever
from talamus.graph import load_graph, query_graph
from talamus.models import CanonicalNote, SourceRef
from talamus.paths import TalamusPaths
from talamus.rank import RankWeights, rerank_candidates
from talamus.store import rebuild_indexes, write_note


def _note(title: str, retrieval: str, aliases: list[str] | None = None) -> CanonicalNote:
    src = SourceRef("raw/a.md", "norm/a#1", "section 1", "sha256:x", ["claim"])
    return CanonicalNote(
        note_id=title.lower().replace(" ", "-"),
        title=title,
        aliases=aliases or [],
        folder="",
        tags=[],
        summary=f"{title}.",
        retrieval_text=retrieval,
        body_sections={"definizione": retrieval},
        proposed_links=[],
        relations=[],
        sources=[src],
        confidence=0.9,
    )


class RerankUnitTests(unittest.TestCase):
    def test_union_keeps_notes_either_signal_finds(self) -> None:
        ranked = rerank_candidates(
            "q",
            graph_hits=[("Only-Graph", 3.0)],
            bm25_hits=[("Only-Bm25", 4.0)],
            aliases_by_title={},
            limit=5,
        )
        titles = {t for t, _ in ranked}
        self.assertEqual(titles, {"Only-Graph", "Only-Bm25"})

    def test_exact_name_hit_boosts(self) -> None:
        # Hub dominates graph; the right note only wins via BM25 + exact-name boost.
        ranked = rerank_candidates(
            "come funziona raft",
            graph_hits=[("Hub", 10.0), ("Raft", 1.0)],
            bm25_hits=[("Raft", 5.0), ("Hub", 1.0)],
            aliases_by_title={"Raft": []},
            limit=5,
        )
        self.assertEqual(ranked[0][0], "Raft")

    def test_alias_also_triggers_exact_boost(self) -> None:
        ranked = rerank_candidates(
            "spiega il consenso rpc",
            graph_hits=[("Other", 5.0)],
            bm25_hits=[("Remote Procedure Call", 1.0), ("Other", 1.0)],
            aliases_by_title={"Remote Procedure Call": ["RPC"]},
            limit=5,
            weights=RankWeights(exact=2.0),
        )
        self.assertEqual(ranked[0][0], "Remote Procedure Call")

    def test_empty_inputs(self) -> None:
        self.assertEqual(rerank_candidates("q", [], [], {}, limit=5), [])


class RerankBeatsGraphFirstTests(unittest.TestCase):
    """The honest proof: measure reranked vs the old graph-first on the same cases."""

    def _brain(self, tmp: str) -> TalamusPaths:
        paths = TalamusPaths(Path(tmp))
        paths.ensure_directories()
        # A hub note repeating boilerplate query words (wins raw graph-overlap, which has no idf)
        write_note(
            paths,
            _note(
                "Guida Generale",
                "come funziona il modulo come funziona il servizio come funziona il sistema",
            ),
        )
        # Filler notes spread the boilerplate across the corpus, so "come/funziona/il" become
        # low-idf (non-discriminative) for BM25 — like a real brain full of similar phrasing.
        for n in ("uno", "due", "tre"):
            write_note(paths, _note(f"Sezione {n}", f"come funziona il componente {n}"))
        # The real answer: rare discriminative terms (wins BM25 + the exact-name boost)
        write_note(paths, _note("Raft", "raft consenso elezione leader replica log"))
        rebuild_indexes(paths)
        return paths

    def _graph_first(self, paths: TalamusPaths):
        graph = load_graph(paths.graph_file)
        return lambda q, k: [str(n.get("label", "")) for n in query_graph(graph, q, limit=k)]

    def test_reranked_outranks_graph_first(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = self._brain(tmp)
            cases = [EvalCase("come funziona il consenso raft?", ["Raft"])]
            baseline = evaluate(cases, self._graph_first(paths), k=3)
            reranked = evaluate(cases, search_retriever(paths), k=3)
            # graph-first ranks the hub note first; rerank puts the right note first
            self.assertEqual(reranked.cases[0].retrieved[0], "Raft")
            self.assertGreater(reranked.mrr, baseline.mrr)


if __name__ == "__main__":
    unittest.main()
