---
type: method
status: evergreen
aliases:
  - Embedding-based Retrieval
  - Semantic Retrieval
  - Vector Search
tags:
  - ai-engineering
  - rag
  - embeddings
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
    locator: pages 281-290
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Term-based retrieval computes relevance at a lexical level rather than a semantic level.
      - Embedding-based retrieval is typically considered dense.
created: 2026-05-26T21:55:46.055849+00:00
updated: 2026-05-26T21:55:46.055849+00:00
ingestion_run: 8d527d59
---

# Embedding-based Retrieval

## Summary

A retrieval mechanism that determines relevance by mapping both the query and the document chunks into a high-dimensional vector space (embeddings). Relevance is calculated by measuring the geometric distance (e.g., cosine similarity) between these vectors.

## Core Idea

This approach captures semantic meaning, allowing the system to retrieve documents that are conceptually related to the query, even if they do not share the same keywords. It moves beyond simple lexical matching.

## Practical Use

Used when the user's intent is conceptual rather than literal (e.g., querying 'vehicle for travel' to retrieve documents containing 'automobile'). Requires robust embedding models and vector databases.

## Related

- [[Retrieval-Algorithms-Overview|Retrieval Algorithms Overview]]
- [[Sparse-vs.-Dense-Retrieval|Sparse vs. Dense Retrieval]]
