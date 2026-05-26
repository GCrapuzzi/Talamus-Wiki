---
type: method
tags: [rrf, hybrid-search, retrieval, ranking]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Reciprocal Rank Fusion

Algorithm for combining document rankings from multiple retrievers (Cormack et al., 2009).

### Formula
`Score(D) = ∑ᵢ 1/(k + rᵢ(D))`

Where:
- `n` = number of ranked lists (one per retriever)
- `rᵢ(D)` = rank of document D by retriever i
- `k` = smoothing constant (typical value: 60) to avoid division by zero and control influence of lower-ranked documents

### Intuition
A document ranked 1st by one retriever and 2nd by another gets a higher combined score than a document ranked 1st by one but absent from another. Documents consistently ranked highly across retrievers are boosted.

Used in [[Hybrid Search]] to merge term-based and embedding-based retrieval results.
