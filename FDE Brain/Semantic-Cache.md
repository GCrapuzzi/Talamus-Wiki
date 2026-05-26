---
type: concept
tags: [caching, latency, vector-search, production-systems]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#step-4-reduce-latency-with-caches
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Semantic Cache

A caching strategy that returns cached results for queries that are *semantically similar* (not identical) to a previous query. Mechanism:

1. Embed the incoming query.
2. Vector-search the cache for the nearest stored embedding.
3. If similarity exceeds a threshold, return the cached result; otherwise compute fresh and cache.

Requires a vector database for cached embeddings.

### Risks and limitations
- **Correctness** — wrong similarity threshold → incorrect cached answers served.
- **Quality dependency chain** — relies on good embeddings, functional vector search, and a reliable similarity metric.
- **Latency overhead** — the vector search itself consumes time and compute, scaling with cache size.
- **Data leaks** — user-specific results cached as generic can expose private information to other users.

Contrast with **exact caching** (deterministic key match, simple LRU/LFU/FIFO eviction, implemented in Redis/PostgreSQL/in-memory). Exact caching is safer and cheaper; semantic caching is only worthwhile when cache hit rate is high enough to justify the complexity.

Both are especially valuable for multi-step queries (chain-of-thought, retrieval, SQL, web search).
