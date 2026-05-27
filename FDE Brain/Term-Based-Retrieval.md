---
type: method
status: evergreen
aliases:
  - Term-based Retrieval
  - Lexical Retrieval
  - Keyword Search
tags:
  - ai-engineering
  - rag
  - search
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
    locator: pages 281-290
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Given a query, the most straightforward way to find relevant documents is with key-words.
      - Term-based retrieval computes relevance at a lexical level rather than a semantic level.
created: 2026-05-26T21:55:46.054597+00:00
updated: 2026-05-26T21:55:46.054597+00:00
ingestion_run: 8d527d59
---

# Term-based Retrieval

## Summary

A retrieval mechanism that determines relevance by matching explicit keywords and terms between the query and the document, typically using statistical scoring methods like TF-IDF or BM25.

## Core Idea

This approach is highly effective when the query contains specific, unique terminology. Its limitation is that it fails to capture semantic meaning or synonyms (e.g., if the query uses 'automobile' but the document uses 'car').

## Practical Use

Ideal for domain-specific searches where exact terminology is expected (e.g., searching for specific product codes or legal statutes). Requires preprocessing steps like tokenization and stop word removal.

## Related

- [[TF-IDF-Scoring|TF-IDF Scoring]]
- [[BM25-Scoring|BM25 Scoring]]
- [[Tokenization|Tokenization]]
