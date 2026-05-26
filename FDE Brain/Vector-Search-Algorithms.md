---
type: concept
tags: [vector-search, ann, hnsw, faiss, lsh, ivf]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-algorithms
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Vector Search Algorithms

Given a query embedding, find the k nearest vectors in a database. Naive k-NN is exact but computationally heavy. Production systems use **Approximate Nearest Neighbor (ANN)** algorithms.

### Key Algorithms
- **LSH** (Locality-Sensitive Hashing): hashes similar vectors into same buckets. Trades accuracy for speed. Used in FAISS, Annoy.
- **HNSW** (Hierarchical Navigable Small World): multi-layer graph where edges connect similar vectors. High accuracy, fast queries, but expensive to build. Used in FAISS, Milvus.
- **Product Quantization**: decomposes vectors into lower-dimensional subvectors for faster distance computation. Core component of FAISS.
- **IVF** (Inverted File Index): K-means clustering of vectors; queries search nearest cluster centroids. Typical 100–10,000 vectors per cluster. Backbone of FAISS with PQ.
- **Annoy** (Spotify): tree-based; builds multiple binary trees with random splits. Open-sourced by Spotify.

### Libraries
FAISS (Meta), ScaNN (Google), Annoy (Spotify), Hnswlib

### Trade-off
Detailed index (e.g., HNSW) → high accuracy, fast queries, slow build. Simple index (e.g., LSH) → fast build, slower/less accurate queries.

### Evaluation metrics (ANN-Benchmarks)
Recall, queries per second (QPS), build time, index size.
