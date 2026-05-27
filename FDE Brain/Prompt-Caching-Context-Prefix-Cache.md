---
type: pattern
status: evergreen
aliases:
  - Prompt Caching (Context/Prefix Cache)
  - Context cache
  - Prefix cache
tags:
  - ai-engineering
  - llm-serving
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/163-inference-service-optimization.md
    locator: pages 464-470
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A prompt cache stores these overlapping segments for reuse, so you only need to process them once.
      - With a prompt cache, the system prompt needs to be processed just once for the first query.
created: 2026-05-26T21:55:46.488401+00:00
updated: 2026-05-26T21:55:46.488401+00:00
ingestion_run: 8d527d59
---

# Prompt Caching (Context/Prefix Cache)

## Summary

A mechanism that stores and reuses overlapping text segments (like system prompts or long document context) across multiple user queries or turns in a conversation.

## Core Idea

Instead of forcing the model to re-process the same context (e.g., a system prompt) with every query, caching allows the model to process the segment only once, drastically reducing redundant computation and improving efficiency.

## Practical Use

Essential for applications involving long-context retrieval (RAG) or multi-turn conversations. Cache the system prompt and the retrieved document chunks to ensure that the model only pays the computational cost for the unique parts of the input.

## Related

- [[Attention-Mechanism|Attention Mechanism]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval Augmented Generation (RAG)]]
