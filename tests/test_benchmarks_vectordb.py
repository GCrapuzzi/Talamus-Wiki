import importlib.util
import os
import unittest

from benchmarks.shootout.runner import JudgedCorpus, run_shootout

_HAS_DEPS = importlib.util.find_spec("sentence_transformers") and importlib.util.find_spec("faiss")
# Heavy (loads/downloads an embedding model, ~1 min): off by default even when the
# deps are present, so `python dev.py` stays fast. Opt in with TALAMUS_BENCH_HEAVY=1.
_RUN_HEAVY = bool(_HAS_DEPS) and os.environ.get("TALAMUS_BENCH_HEAVY") == "1"


@unittest.skipUnless(_RUN_HEAVY, "set TALAMUS_BENCH_HEAVY=1 (and install bench deps) to run")
class VectorDBSystemTests(unittest.TestCase):
    def test_vectordb_finds_semantically_relevant_doc(self) -> None:
        from benchmarks.shootout.systems.vectordb_system import VectorDBSystem

        # the relevant doc shares no keyword with the query — only embeddings bridge it
        corpus = JudgedCorpus(
            docs=[
                ("d1", "Hallucination", "a model fabricates facts not grounded in any source"),
                ("d2", "Throughput", "tokens generated per second under load"),
                ("d3", "Sharding", "splitting a dataset across multiple machines"),
            ],
            queries={"q1": "the assistant makes things up"},
            qrels={"q1": {"d1": 1}},
        )
        result = run_shootout([VectorDBSystem()], corpus, k=2)
        self.assertEqual(result["systems"]["vectordb"]["hit_rate"], 1.0)
