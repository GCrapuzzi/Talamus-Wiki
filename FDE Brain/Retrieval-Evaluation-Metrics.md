---
type: concept
tags: [evaluation, retrieval, metrics, precision, recall, ndcg, beir]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-algorithms
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Retrieval Evaluation Metrics

### Retriever Quality
- **Context precision** (context relevance): of all retrieved documents, what % is relevant?
- **Context recall**: of all relevant documents, what % is retrieved?
- Context precision is simpler — only compare retrieved docs to query (AI judge suffices). Context recall requires annotating relevance of all documents.

### Ranking Quality
- **NDCG** (Normalized Discounted Cumulative Gain)
- **MAP** (Mean Average Precision)
- **MRR** (Mean Reciprocal Rank)

### Embedding Quality
Evaluate independently (similar docs → closer embeddings) or task-specifically via MTEB Benchmark.

### System-level
- **BEIR** (Benchmarking IR): evaluation harness across 14 retrieval benchmarks
- Ultimately evaluate end-to-end: does the retriever help the system generate high-quality answers?

### RAG evaluation should cover all three levels:
1. Retrieval quality
2. Final RAG output quality
3. Embedding quality (for embedding-based retrieval)
