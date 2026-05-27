---
type: method
status: evergreen
aliases:
  - Retrieve-Then-Generate Pattern
  - Retrieval-Augmented Pattern
tags:
  - llm-workflow
  - vector-database
  - information-retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/111-rag.md
    locator: pages 277-279
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The retrieve-then-generate pattern was first introduced in 'Reading Wikipedia to Answer Open-Domain Questions' (Chen et al., 2017).
      - With RAG, only the information most relevant to the query, as determined by the retriever, is retrieved and input into the model.
created: 2026-05-26T21:55:46.044069+00:00
updated: 2026-05-26T21:55:46.044069+00:00
ingestion_run: 8d527d59
---

# Retrieve-Then-Generate Pattern

## Summary

A foundational two-step process where a system first retrieves relevant information (the 'Retrieve' step) from an external corpus, and then uses that retrieved context to guide the LLM's response generation (the 'Generate' step).

## Core Idea

This pattern ensures that the LLM's generation is constrained and informed by external facts, preventing the model from hallucinating or relying on outdated internal knowledge. It is the operational core of RAG.

## Practical Use

Building a robust knowledge retrieval system: 1) Indexing data chunks, 2) Embedding the query and chunks, 3) Performing vector similarity search to retrieve top-K chunks, 4) Passing the query + top-K chunks to the LLM prompt.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
