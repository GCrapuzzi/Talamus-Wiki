---
type: method
status: evergreen
aliases:
  - Semantic Caching
  - Similarity Caching
tags:
  - ai-engineering
  - caching
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/170-step-4.-reduce-latency-with-caches.md
    locator: pages 484-486
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Unlike in exact caching, cached items are used even if they are only semantically similar, not identical, to the incoming query.
      - This approach requires a vector database to store the embeddings of cached queries.
created: 2026-05-26T21:55:46.536872+00:00
updated: 2026-05-26T21:55:46.536872+00:00
ingestion_run: 8d527d59
---

# Semantic Caching

## Summary

A caching mechanism that allows the reuse of a cached result even if the incoming query is not identical, but is semantically similar to a previously stored query.

## Core Idea

This increases the cache hit rate by accommodating variations in user phrasing. It relies on generating embeddings and using vector search to determine similarity, but introduces complexity and potential performance risks.

## Practical Use

Use when query phrasing variability is high (e.g., user-generated content). Requires a vector database and a reliable similarity threshold. Must be evaluated carefully for efficiency and risk.

## Related

- Embedding Model
- [[Vector-Search|Vector Search]]
