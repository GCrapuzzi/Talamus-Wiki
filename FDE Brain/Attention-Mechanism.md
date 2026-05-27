---
type: concept
status: evergreen
aliases:
  - Attention Mechanism
  - Scaled Dot-Product Attention
  - QKV mechanism
tags:
  - ai-engineering
  - nlp
  - mechanism
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
    locator: pages 82-90
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The attention mechanism allows the model to weigh the importance of different input tokens when generating each output token.
      - The attention mechanism leverages key, value, and query vectors.
      - The attention mechanism computes how much attention to give an input token by performing a dot product between the query vector and its key vector.
created: 2026-05-26T21:55:45.528335+00:00
updated: 2026-05-26T21:55:45.528335+00:00
ingestion_run: 8d527d59
---

# Attention Mechanism

## Summary

A mechanism that allows a model to weigh the importance of different input tokens relative to the current token being generated, enabling context-aware processing.

## Core Idea

Instead of relying on sequential processing, attention calculates relevance by comparing a Query vector (Q) against all Key vectors (K) to determine how much 'attention' to pay to each corresponding Value vector (V).

## Practical Use

Implementing or analyzing attention layers when building custom NLP models. Understanding the QKV relationship is crucial for optimizing memory usage and extending context length (e.g., using techniques like FlashAttention).

## Related

- [[Transformer-Architecture|Transformer Architecture]]
- Key/Query/Value Vectors
