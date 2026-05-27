---
type: method
status: evergreen
aliases:
  - Semantic Similarity
  - Meaning similarity
  - Embedding distance
tags:
  - ai-engineering
  - evaluation
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
    locator: pages 151-157
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Semantic similarity aims to compute the similarity in semantics. This first requires transforming a text into a numerical representation, which is called an embedding.
created: 2026-05-26T21:55:45.697217+00:00
updated: 2026-05-26T21:55:45.697217+00:00
ingestion_run: 8d527d59
---

# Semantic Similarity

## Summary

A reference-based metric that computes the similarity between two texts based on their underlying meaning (semantics), rather than their literal word overlap.

## Core Idea

It requires transforming text into a numerical vector representation (embedding). Texts with similar meanings will have vectors that are close together in the embedding space, even if they use completely different words.

## Practical Use

Use this method for open-ended tasks (e.g., summarization, translation) where multiple correct phrasings are possible. It is generally superior to lexical similarity for complex language generation tasks.

## Related

- Embeddings
- Vector Space Models
