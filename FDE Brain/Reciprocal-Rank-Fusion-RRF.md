---
type: method
status: evergreen
aliases:
  - Reciprocal Rank Fusion (RRF)
  - Ensemble ranking algorithm
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
      - "An algorithm for combining different rankings is called reciprocal rank fusion (RRF)... The actual formula for a document D is more complicated, as follows: Score(D) = ∑i=1 n 1 / (k + r_i(D))"
created: 2026-05-26T21:55:46.060809+00:00
updated: 2026-05-26T21:55:46.060809+00:00
ingestion_run: 8d527d59
---

# Reciprocal Rank Fusion (RRF)

## Summary

A mathematical formula used to combine multiple ranking lists (from different retrievers) into a single, unified score for each document. It assigns a score based on a document's rank across all input lists.

## Core Idea

RRF allows multiple specialized retrievers (e.g., keyword, vector, graph) to contribute to a single document's final score without requiring them to be perfectly correlated. The score is calculated as the sum of contributions from each retriever, where the contribution decreases as the rank increases.

## Practical Use

Implement RRF when combining the outputs of diverse retrieval systems (e.g., combining a BM25 score with a cosine similarity score) to generate a robust final ranking list for the LLM context.

## Related

- Ensemble Retrieval
- Retrieval Optimization
