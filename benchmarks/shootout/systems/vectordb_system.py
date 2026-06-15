from __future__ import annotations

import time

from benchmarks.shootout.systems.base import Doc, IngestStats


class VectorDBSystem:
    """The classic dense-RAG competitor: sentence-transformers embeddings + FAISS.

    Exact inner-product index (IndexFlatIP) over L2-normalized embeddings =
    cosine similarity. Exact (not HNSW) so the vector DB gets its BEST possible
    recall at this corpus size — we do not sabotage the competition. The default
    model is the standard strong CPU baseline."""

    name = "vectordb"

    def __init__(self, model_name: str = "all-MiniLM-L6-v2") -> None:
        self._model_name = model_name
        self._ids: list[str] = []
        self._model = None
        self._index = None

    def ingest(self, docs: list[Doc]) -> IngestStats:
        import faiss
        from sentence_transformers import SentenceTransformer

        start = time.perf_counter()
        self._model = SentenceTransformer(self._model_name)
        self._ids = [doc.doc_id for doc in docs]
        texts = [f"{doc.title} {doc.text}" for doc in docs]
        emb = self._model.encode(
            texts, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False
        )
        self._index = faiss.IndexFlatIP(emb.shape[1])
        self._index.add(emb)
        return IngestStats(seconds=time.perf_counter() - start, index_bytes=int(emb.nbytes))

    def query(self, q: str, k: int) -> list[str]:
        if self._index is None or self._model is None:
            return []
        qe = self._model.encode(
            [q], normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False
        )
        _scores, idx = self._index.search(qe, min(k, len(self._ids)))
        return [self._ids[i] for i in idx[0] if i != -1]
