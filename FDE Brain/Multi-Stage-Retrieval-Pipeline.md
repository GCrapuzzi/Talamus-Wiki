---
type: pattern
status: evergreen
aliases:
  - Multi-Stage Retrieval Pipeline
  - Two-stage retrieval
  - Cascading retriever
tags:
  - ai-engineering
  - rag
  - retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/114-retrieval-optimization.md
    locator: pages 291-296
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - First, a cheap, less precise retriever, such as a term-based system, fetches candidates. Then, a more precise but more expensive mechanism, such as k-nearest neighbors, finds the best of these candidates.
created: 2026-05-26T21:55:46.059466+00:00
updated: 2026-05-26T21:55:46.059466+00:00
ingestion_run: 8d527d59
---

# Multi-Stage Retrieval Pipeline

## Summary

Using a sequence of retrieval mechanisms, starting with a cheap, broad retriever (e.g., term-based) to generate candidates, followed by a more precise, expensive mechanism (e.g., k-NN vector search) to refine the final set.

## Core Idea

This pattern improves accuracy and efficiency by separating the broad candidate generation phase from the precise ranking phase. It prevents the expensive, high-precision model from running on the entire corpus, saving computational resources while maintaining high relevance.

## Practical Use

When building a RAG system, first use keyword matching or basic filtering to narrow down documents by topic (e.g., 'X'), and then use vector search (k-NN) only on that subset of documents to find the most contextually relevant passages.

## Related

- Reranking
- Contextual Retrieval
