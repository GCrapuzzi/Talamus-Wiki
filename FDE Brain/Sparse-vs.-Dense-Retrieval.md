---
type: framework
status: evergreen
aliases:
  - Sparse vs. Dense Retrieval
  - Term-based vs. Embedding-based Retrieval
tags:
  - ai-engineering
  - vector-databases
  - retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/113-retrieval-algorithms.md
    locator: pages 281-290
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Sparse retrievers represent data using sparse vectors.
      - Dense retrievers represent data using dense vectors.
      - Term-based versus embedding-based division avoids this miscategorization.
created: 2026-05-26T21:55:46.049540+00:00
updated: 2026-05-26T21:55:46.049540+00:00
ingestion_run: 8d527d59
---

# Sparse vs. Dense Retrieval

## Summary

A classification of retrieval algorithms based on the vector representation used: Sparse retrievers use vectors with mostly zero values (e.g., one-hot encoding), while Dense retrievers use vectors where most values are non-zero (embeddings).

## Core Idea

This distinction is critical for understanding how relevance is calculated. Term-based methods are inherently sparse, while modern embedding methods are typically dense. Using 'term-based vs. embedding-based' avoids miscategorizing algorithms like SPLADE.

## Practical Use

When selecting a retrieval model, an engineer must determine if the required relevance signal is lexical (sparse) or semantic (dense).

## Related

- [[Term-based-Retrieval|Term-based Retrieval]]
- [[Embedding-based-Retrieval|Embedding-based Retrieval]]
