---
type: method
status: evergreen
aliases:
  - Retrieval-Augmented Generation (RAG) Strategy
  - Data Grounding Pipeline
  - External Knowledge Integration
tags:
  - ai-engineering
  - rag
  - data-grounding
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/129-memory-bottlenecks.md
    locator: pages 343-343
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the model frequently fails due to missing information, connect it to data sources.
      - Begin by using basic retrieval methods like term-based search.
      - Advanced RAG methods, such as embedding-based retrieval, can be used.
created: 2026-05-26T21:55:46.207985+00:00
updated: 2026-05-26T21:55:46.207985+00:00
ingestion_run: 8d527d59
---

# Retrieval-Augmented Generation (RAG) Strategy

## Summary

A structured method to improve LLM accuracy and reduce hallucinations by connecting the model to external, verifiable data sources.

## Core Idea

RAG mitigates the knowledge cutoff and hallucination risks inherent in LLMs by providing context at inference time. Starting with basic retrieval and progressing to embedding-based methods ensures scalable improvement.

## Practical Use

When the model fails due to missing or outdated information, implement RAG. Start with simple term-based search. If performance plateaus, upgrade the retrieval mechanism to use vector embeddings for semantic search.

## Related

- [[LLM-Performance-Improvement-Workflow|LLM Performance Improvement Workflow]]
- [[Embedding-based-Retrieval|Embedding-based Retrieval]]
