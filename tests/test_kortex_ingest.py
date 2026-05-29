import json
import tempfile
import unittest
from pathlib import Path

from kortex.ingest import ingest_file
from kortex.paths import KortexPaths
from kortex.store import load_notes
from tests.support import FakeLLMProvider


class IngestTests(unittest.TestCase):
    def test_ingest_file_creates_note_raw_and_cache(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = KortexPaths(root)
            paths.ensure_directories()
            source = root / "rag.md"
            source.write_text("# RAG\nRAG collega il modello a fonti esterne.", encoding="utf-8")
            llm = FakeLLMProvider([json.dumps([
                {"title": "Retrieval-Augmented Generation", "aliases": ["RAG"],
                 "retrieval_text": "rag fonti esterne", "summary": "RAG collega a fonti esterne.",
                 "supported_claims": ["RAG collega a fonti esterne."], "confidence": 0.9}
            ])])

            result = ingest_file(paths, source, llm)

            self.assertEqual(1, result["notes_written"])
            self.assertEqual(1, len(load_notes(paths)))
            self.assertTrue(any(paths.raw.glob("*.md")))
            self.assertTrue(paths.graph_file.is_file())


if __name__ == "__main__":
    unittest.main()
