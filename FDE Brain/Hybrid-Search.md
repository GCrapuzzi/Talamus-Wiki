---
type: pattern
tags: [hybrid-search, retrieval, rrf, reranking, ensemble]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-algorithms
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Hybrid Search

Combining term-based and embedding-based retrieval to leverage the strengths of each.

### Sequential combination
Cheap retriever (term-based) fetches candidates → precise mechanism (vector search or reranker) selects the best. Example: keyword fetch all docs mentioning "transformer", then vector search to find those about the neural architecture.

### Parallel combination (ensemble)
Multiple retrievers fetch candidates simultaneously; rankings are merged.

### Reciprocal Rank Fusion (RRF)
Algorithm for combining rankings from multiple retrievers:

`Score(D) = ∑ 1/(k + rᵢ(D))`

Where rᵢ(D) is document D's rank from retriever i, k is a smoothing constant (typically 60).

Higher-ranked documents by any retriever get higher final scores. Documents ranked highly by multiple retrievers are boosted further.
