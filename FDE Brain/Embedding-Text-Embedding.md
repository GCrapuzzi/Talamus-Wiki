---
type: glossary
status: evergreen
aliases:
  - Embedding (Text Embedding)
  - Vector representation
  - Numerical text encoding
tags:
  - ai-engineering
  - nlp
  - glossary
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
    locator: pages 151-157
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Semantic similarity aims to compute the similarity in semantics. This first requires transforming a text into a numerical representation, which is called an embedding.
created: 2026-05-26T21:55:45.699308+00:00
updated: 2026-05-26T21:55:45.699308+00:00
ingestion_run: 8d527d59
---

# Embedding (Text Embedding)

## Summary

The process of transforming textual data (sentences, paragraphs) into a dense, multi-dimensional numerical vector (embedding). The position of the vector in the space captures the semantic meaning of the text.

## Core Idea

The distance between two embeddings (e.g., cosine similarity) serves as a proxy for the semantic distance between the original texts. This is the foundational mechanism for calculating semantic similarity.

## Practical Use

When implementing semantic evaluation, the first step is selecting or training an appropriate embedding model (e.g., BERT, specialized LLM embedding) to ensure the vectors accurately capture the domain-specific meaning of the text.

## Related

- [[Semantic-Similarity|Semantic Similarity]]
