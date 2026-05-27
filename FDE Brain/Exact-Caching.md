---
type: method
status: evergreen
aliases:
  - Exact Caching
  - Deterministic Caching
tags:
  - ai-engineering
  - caching
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/170-step-4.-reduce-latency-with-caches.md
    locator: pages 484-486
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - With exact caching, cached items are used only when these exact items are requested.
      - Caching is especially appealing for queries that involve multiple steps (e.g., chain-of-thought) and/or time-consuming actions (e.g., retrieval, SQL execution, or web search).
created: 2026-05-26T21:55:46.534710+00:00
updated: 2026-05-26T21:55:46.534710+00:00
ingestion_run: 8d527d59
---

# Exact Caching

## Summary

A caching mechanism where a cached item is retrieved only if the incoming request exactly matches a previously stored request key. The cache key must be deterministic.

## Core Idea

This method provides high reliability and predictability because the cache lookup is based on strict equality. It is ideal for time-consuming, multi-step, or retrieval-heavy operations where the input query is expected to repeat precisely.

## Practical Use

Use for caching results from complex chains (e.g., chain-of-thought), expensive database queries (SQL execution), or embedding-based retrieval results to avoid redundant vector searches. Implement using fast storage like Redis or PostgreSQL.

## Related

- [[Semantic-Caching|Semantic Caching]]
- [[Vector-Search|Vector Search]]
