---
type: glossary
status: evergreen
aliases:
  - Embedding
  - Vector Representation
  - Numerical Embedding
tags:
  - ai-engineering
  - llm-architecture
  - vector-databases
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/066-introduction-to-embedding.md
    locator: pages 158-159
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An embedding is a numerical representation that aims to capture the meaning of the original data.
      - The goal of the embedding algorithm is to produce embeddings that capture the essence of the original data.
created: 2026-05-26T21:55:45.703622+00:00
updated: 2026-05-26T21:55:45.703622+00:00
ingestion_run: 8d527d59
---

# Embedding

## Summary

A numerical vector representation that converts complex data (text, images, etc.) into a lower-dimensional space, aiming to capture the semantic meaning of the original data.

## Core Idea

Since computers process numbers, embeddings translate abstract concepts into quantifiable coordinates. The goal is that the geometric distance between two vectors reflects the semantic similarity between the original data points.

## Practical Use

Used as the foundational step for Retrieval-Augmented Generation (RAG), classification, and similarity search. Engineers must select an embedding model (e.g., OpenAI, Cohere, BERT) appropriate for the data modality and task.

## Related

- [[Joint-Embedding-Space|Joint Embedding Space]]
- Cosine Similarity
- MTEB
