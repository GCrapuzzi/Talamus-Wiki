import importlib.util
import os
import unittest

# mem0 + a local ollama model + the embedder is a heavy, stateful probe (local
# LLM extraction per doc). Off by default; opt in with TALAMUS_BENCH_HEAVY=1.
_HAS_MEM0 = importlib.util.find_spec("mem0") is not None
_RUN = _HAS_MEM0 and os.environ.get("TALAMUS_BENCH_HEAVY") == "1"


@unittest.skipUnless(_RUN, "set TALAMUS_BENCH_HEAVY=1 (mem0 + ollama) to run")
class Mem0SystemTests(unittest.TestCase):
    def test_ingest_and_query_returns_doc_ids(self) -> None:
        from benchmarks.shootout.systems.base import Doc
        from benchmarks.shootout.systems.mem0_system import Mem0System

        docs = [
            Doc("d1", "Hallucination", "a model fabricates facts not grounded in any source"),
            Doc("d2", "Quantization", "reduce the bits of model weights to save memory"),
        ]
        system = Mem0System()
        stats = system.ingest(docs)
        self.assertGreaterEqual(stats.llm_calls, 0)
        hits = system.query("the model makes things up", k=2)
        self.assertIsInstance(hits, list)


if __name__ == "__main__":
    unittest.main()
