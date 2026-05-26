---
type: method
tags: [retrieval, embeddings, semantic-search, vector-database]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-algorithms
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Embedding-Based Retrieval

Ranks documents by semantic similarity rather than lexical overlap. Also called **semantic retrieval**.

### Workflow
1. **Indexing**: convert data chunks into embeddings using an embedding model; store in a Vector Database
2. **Query embedding**: convert query into an embedding using the same model
3. **Vector search**: fetch k chunks whose embeddings are closest to the query embedding

Real-world systems add components like rerankers and caches.

### Pros
- Captures meaning, not just surface terms
- Supports natural-language queries
- Can outperform term-based retrieval with finetuning

### Cons
- Embedding generation adds cost (especially with frequent data changes)
- Can obscure specific keywords (error codes, product names)
- Vector storage and search can be expensive (often 20-50% of model API spend)
- Slower indexing and querying than term-based

Embedding quality is evaluated via MTEB Benchmark and task-specific metrics.
