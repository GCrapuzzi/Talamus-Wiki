---
type: operation
status: evergreen
aliases:
  - Long-context Finetuning
  - Context Extension
  - Positional Embedding Adjustment
tags:
  - ai-engineering
  - llm-architecture
  - deployment-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
    locator: pages 332-334
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Long-context finetuning typically requires modifying the model’s architecture, such as adjusting the positional embeddings.
      - A long sequence means more possible positions for tokens, and positional embeddings should be able to handle them.
created: 2026-05-26T21:55:46.172843+00:00
updated: 2026-05-26T21:55:46.172843+00:00
ingestion_run: 8d527d59
---

# Long-context Finetuning

## Summary

A specialized finetuning operation required to enable a model to process and retain information from sequences significantly longer than its original training context window (e.g., increasing context from 4k to 16k tokens).

## Core Idea

The limitation is often architectural, specifically related to positional embeddings. To handle longer sequences, the model's positional embeddings must be modified or adjusted to account for the increased number of possible token positions.

## Practical Use

When working with specialized data like long code files, full legal transcripts, or extensive scientific papers, this technique must be applied to ensure the model can process the entire document contextually without losing information from the beginning.

## Related

- [[Finetuning|Finetuning]]
- Positional Embeddings
