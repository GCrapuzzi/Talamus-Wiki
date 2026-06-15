from __future__ import annotations

import tempfile
import time

from benchmarks.shootout.systems.base import Doc, IngestStats

_EMBED_DIMS = 384  # all-MiniLM-L6-v2; mem0 defaults qdrant to 1536 (OpenAI) — must match


class Mem0System:
    """The agent-memory peer (mem0), run fully local & free: ollama LLM
    (gemma4:e4b) + a local sentence-transformers embedder.

    IMPORTANT design note: mem0 EXTRACTS memories from each document via an LLM
    call at ingest. That is its design point (conversational memory), not
    document-corpus IR — so a full 5k-doc run is thousands of local LLM calls
    (days). We therefore characterize mem0 at SMALL scale: its per-doc ingest
    cost and behavior, plus the capability matrix. Honest, not a full recall
    comparison."""

    name = "mem0"

    def __init__(self, model: str = "gemma4:e4b", infer: bool = True) -> None:
        self._model = model
        self._infer = infer
        self._memory = None
        self._user = "bench"
        self._llm_calls = 0
        # qdrant holds a sqlite lock; ignore Windows temp cleanup races at exit
        self._tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)

    def _config(self) -> dict:
        return {
            "llm": {"provider": "ollama", "config": {"model": self._model}},
            "embedder": {
                "provider": "huggingface",
                "config": {
                    "model": "sentence-transformers/all-MiniLM-L6-v2",
                    "embedding_dims": _EMBED_DIMS,
                },
            },
            "vector_store": {
                "provider": "qdrant",
                "config": {"embedding_model_dims": _EMBED_DIMS, "path": self._tmp.name},
            },
        }

    def ingest(self, docs: list[Doc]) -> IngestStats:
        from mem0 import Memory

        start = time.perf_counter()
        self._memory = Memory.from_config(self._config())
        self._memory.reset()
        for doc in docs:
            self._memory.add(
                f"{doc.title}. {doc.text}",
                user_id=self._user,
                metadata={"doc_id": doc.doc_id},
                infer=self._infer,
            )
            self._llm_calls += 1 if self._infer else 0
        return IngestStats(seconds=time.perf_counter() - start, llm_calls=self._llm_calls)

    def query(self, q: str, k: int) -> list[str]:
        if self._memory is None:
            return []
        hits = self._memory.search(q, filters={"user_id": self._user}, limit=k)
        results = hits.get("results", hits) if isinstance(hits, dict) else hits
        out: list[str] = []
        for item in results:
            meta = item.get("metadata") or {}
            doc_id = meta.get("doc_id")
            if doc_id and doc_id not in out:
                out.append(doc_id)
        return out[:k]
