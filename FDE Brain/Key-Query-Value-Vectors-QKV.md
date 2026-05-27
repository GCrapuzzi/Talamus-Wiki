---
type: glossary
status: evergreen
aliases:
  - Key/Query/Value Vectors (QKV)
  - Attention vectors
tags:
  - ai-engineering
  - glossary
  - nlp
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
    locator: pages 82-90
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The query vector (Q) represents the current state of the decoder at each decoding step.
      - Each key vector (K) represents a previous token.
      - Each value vector (V) represents the actual value of a previous token, as learned by the model.
created: 2026-05-26T21:55:45.530325+00:00
updated: 2026-05-26T21:55:45.530325+00:00
ingestion_run: 8d527d59
---

# Key/Query/Value Vectors (QKV)

## Summary

The three vector representations used in the attention mechanism: Query (Q) represents the current state/searcher; Key (K) represents the index/page number; and Value (V) represents the content/actual information.

## Core Idea

Q is used to query information, K determines if the information is relevant (the match score), and V provides the content to be aggregated if the match is strong. This structure enables non-sequential information retrieval.

## Practical Use

When debugging or optimizing attention layers, understanding which vector (Q, K, or V) is bottlenecking performance or causing memory issues is essential. Q is typically derived from the decoder state.

## Related

- [[Attention-Mechanism|Attention Mechanism]]
- [[Transformer-Architecture|Transformer Architecture]]
