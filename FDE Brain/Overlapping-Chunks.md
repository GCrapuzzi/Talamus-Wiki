---
type: pattern
status: evergreen
aliases:
  - Overlapping Chunks
  - Contextual overlap
tags:
  - ai-engineering
  - rag
  - data-indexing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/114-retrieval-optimization.md
    locator: pages 291-296
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Overlapping ensures that important boundary information is included in at least one chunk.
created: 2026-05-26T21:55:46.064095+00:00
updated: 2026-05-26T21:55:46.064095+00:00
ingestion_run: 8d527d59
---

# Overlapping Chunks

## Summary

A chunking technique where adjacent chunks share a defined amount of text (overlap). This ensures that critical information or context that spans a boundary is included in at least one chunk.

## Core Idea

Overlap mitigates the risk of 'context loss' that occurs when a document is split cleanly at a natural break point, thereby improving the chances that the retriever captures the full meaning of a passage.

## Practical Use

When setting up a chunking pipeline, always implement a small overlap (e.g., 10-20% of the chunk size) to ensure continuity, especially for narrative or technical documents.

## Related

- [[Chunking-Strategy-Design|Chunking Strategy Design]]
