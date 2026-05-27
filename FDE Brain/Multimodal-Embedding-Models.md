---
type: method
status: evergreen
aliases:
  - Multimodal Embedding Models
  - CLIP-like models
tags:
  - ai-engineering
  - embedding
  - multimodal
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/115-rag-beyond-texts.md
    locator: pages 297-298
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If queries are texts, you’ll need a multimodal embedding model that can generate embeddings for both images and texts.
      - Generate CLIP embeddings for all your data, both texts and images, and store them in a vector database.
created: 2026-05-26T21:55:46.075571+00:00
updated: 2026-05-26T21:55:46.075571+00:00
ingestion_run: 8d527d59
---

# Multimodal Embedding Models

## Summary

Models (e.g., CLIP) that generate a unified embedding space, allowing the comparison of different data types (text, images) within the same vector space.

## Core Idea

To retrieve content based on its inherent meaning rather than just keywords, the model must project both the query and the data into a shared vector space, enabling semantic similarity search across modalities.

## Practical Use

Implementing content-based retrieval for images using text queries. The workflow involves generating embeddings for all data (text and image) and then querying the vector database using the query's embedding.

## Related

- [[Multimodal-RAG|Multimodal RAG]]
- Vector Databases
