---
type: pattern
status: evergreen
aliases:
  - Multimodal RAG
  - Multimodal Retrieval-Augmented Generation
tags:
  - ai-engineering
  - rag
  - multimodal
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/115-rag-beyond-texts.md
    locator: pages 297-298
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If your generator is multimodal, its contexts might be augmented not only with text documents but also with images, videos, audio, etc.
      - Given a query, the retriever fetches both texts and images relevant to it.
created: 2026-05-26T21:55:46.072811+00:00
updated: 2026-05-26T21:55:46.072811+00:00
ingestion_run: 8d527d59
---

# Multimodal RAG

## Summary

An extension of RAG that incorporates non-textual data (images, video, audio) into the context provided to the LLM.

## Core Idea

When the generator is multimodal, the retriever must fetch and process multiple data types (text, images, etc.) relevant to the query, moving beyond simple text document retrieval.

## Practical Use

Used when the query requires visual or auditory context (e.g., 'What is the color of the house in this picture?'). Retrieval can be augmented either by fetching content based on metadata (captions, tags) or by comparing content embeddings.

## Related

- [[Multimodal-Embedding-Models|Multimodal Embedding Models]]
- Vector Databases
