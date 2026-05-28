import tempfile
import unittest
from pathlib import Path

from brain.ask import build_context_bundle
from brain.cli import main
from brain.graph import build_graph, save_graph
from brain.models import CanonicalNote, SourceRef
from brain.paths import BrainPaths
from brain.search import BM25Index


def source_ref() -> SourceRef:
    return SourceRef(
        raw_path="knowledge/raw/pdf/book.pdf",
        normalized_path="knowledge/normalized/pdf/book/sections/001.md",
        locator="pages 1-2",
        source_hash="sha256:abc",
        supported_claims=["RAG retrieves context."],
    )


class BrainAskTests(unittest.TestCase):
    def test_context_uses_graph_before_bm25(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = BrainPaths(Path(tmp))
            paths.ensure_directories()
            note = CanonicalNote(
                note_id="rag",
                title="Retrieval-Augmented Generation",
                aliases=["RAG"],
                folder="Retrieval",
                tags=["retrieval"],
                summary="RAG connects models to external knowledge.",
                retrieval_text="external documents retrieval augmented generation",
                body_sections={"core_idea": "RAG retrieves context."},
                proposed_links=[],
                relations=[],
                sources=[source_ref()],
                confidence=0.9,
            )
            note_path = paths.notes / "Retrieval-Augmented-Generation.md"
            note_path.write_text("# Retrieval-Augmented Generation\n\nRAG retrieves context.", encoding="utf-8")
            graph = build_graph([note])
            search = BM25Index()
            search.add("wrong", "external documents")

            bundle = build_context_bundle(paths, graph, search, "How do I use external documents?", limit=1)

            self.assertEqual("graph", bundle.items[0]["route"])
            self.assertIn("Retrieval-Augmented-Generation.md", bundle.items[0]["path"])
            self.assertIn("RAG retrieves context", bundle.items[0]["content"])

    def test_ask_context_cli_reads_real_note_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = BrainPaths(Path(tmp))
            paths.ensure_directories()
            note = CanonicalNote(
                note_id="rag",
                title="Retrieval-Augmented Generation",
                aliases=["RAG"],
                folder="Retrieval",
                tags=["retrieval"],
                summary="RAG connects models to external knowledge.",
                retrieval_text="external documents retrieval augmented generation",
                body_sections={"core_idea": "RAG retrieves context."},
                proposed_links=[],
                relations=[],
                sources=[source_ref()],
                confidence=0.9,
            )
            (paths.notes / "Retrieval-Augmented-Generation.md").write_text(
                "# Retrieval-Augmented Generation\n\nRAG retrieves context.",
                encoding="utf-8",
            )
            save_graph(paths.graph / "graph.json", build_graph([note]))
            search = BM25Index()
            search.save(paths.index / "bm25.json")

            code = main(["ask", "context", "How do I use external documents?", "--root", tmp])

            self.assertEqual(0, code)


if __name__ == "__main__":
    unittest.main()
