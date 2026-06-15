"""Scale curves: latency + index footprint as the brain grows. Reuses the
package's own LLM-free scale bench (synthetic corpora) and adds the dense
competitor's footprint (an embedding model in RAM) for contrast.

Scale is a STRUCTURAL property, so synthetic corpora are honest here — no LLM
spend. The dense model carries a fixed ~80-90 MB resident cost that Talamus and
BM25 do not."""

from __future__ import annotations


def talamus_scale(sizes: list[int] | None = None) -> list[dict]:
    """Talamus search latency + index size at growing synthetic corpus sizes."""
    from talamus.bench import run_scale

    rows = run_scale(sizes or [100, 1000, 10000])
    return [
        {
            "n_notes": r["n_notes"],
            "search_p50_ms": r["search"]["p50_ms"],
            "search_p95_ms": r["search"]["p95_ms"],
            "index_bytes": r["index"].get("bytes", 0),
            "backend": r["index"].get("backend", "?"),
        }
        for r in rows
    ]


def dense_resident_overhead_mb(model_name: str = "all-MiniLM-L6-v2") -> dict:
    """The fixed cost a vector DB pays that we do not: the embedding model loaded
    in RAM. Reported as a contrast line, measured if the dep is present."""
    try:
        import faiss  # noqa: F401
        from sentence_transformers import SentenceTransformer
    except ImportError:
        return {"model": model_name, "resident_mb": None, "note": "deps not installed"}
    model = SentenceTransformer(model_name)
    params = sum(p.numel() for p in model.parameters())
    return {
        "model": model_name,
        "params_millions": round(params / 1e6, 1),
        "resident_mb_approx": round(params * 4 / 1e6, 1),  # fp32 params, rough
        "note": "Talamus and BM25 load no model: 0 MB resident",
    }
