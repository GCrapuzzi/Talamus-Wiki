---
type: framework
status: evergreen
aliases:
  - Chunking Strategy Design
  - Document splitting strategy
  - Indexing unit design
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
      - The simplest strategy is to chunk documents into chunks of equal length based on a certain unit. Common units are characters, words, sentences, and paragraphs.
      - When a document is split into chunks without overlap, the chunks might be cut off in the middle of important context...
      - The chunk size shouldn’t exceed the maximum context length of the generative model.
created: 2026-05-26T21:55:46.062064+00:00
updated: 2026-05-26T21:55:46.062064+00:00
ingestion_run: 8d527d59
---

# Chunking Strategy Design

## Summary

A decision framework for determining how large documents should be split into smaller, manageable chunks (text units) for indexing and retrieval. The choice impacts context preservation, retrieval diversity, and computational cost.

## Core Idea

Chunking is not arbitrary. The strategy must align with the intended retrieval method and the generative model's constraints. Key considerations include chunk size, overlap, and the unit of splitting (tokens, sentences, paragraphs).

## Practical Use

Before indexing, analyze the document type (e.g., code, Q&A, narrative). If the content is highly technical, use token-based chunking. If context continuity is paramount, use overlapping chunks and recursive splitting.

## Related

- Token-based Chunking
- [[Overlapping-Chunks|Overlapping Chunks]]
