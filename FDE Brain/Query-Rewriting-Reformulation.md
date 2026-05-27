---
type: method
status: evergreen
aliases:
  - Query Rewriting (Reformulation)
  - Query normalization
  - Query expansion
  - Contextual query reformulation
tags:
  - ai-engineering
  - rag
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/114-retrieval-optimization.md
    locator: pages 291-296
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The last question, “How about Emily Doe?”, is ambiguous without context. If you use this query verbatim to retrieve documents, you’ll likely get irrelevant results. You need to rewrite this query to reflect what the user is actually asking.
created: 2026-05-26T21:55:46.068176+00:00
updated: 2026-05-26T21:55:46.068176+00:00
ingestion_run: 8d527d59
---

# Query Rewriting (Reformulation)

## Summary

The process of taking an ambiguous, conversational, or incomplete user query and transforming it into a standalone, explicit, and highly specific query that can be used effectively by the retrieval system.

## Core Idea

In conversational AI or multi-turn dialogue, the user's intent is often implicit. Query rewriting bridges this gap by making the query explicit, ensuring the retriever searches for the user's true underlying need rather than the literal words used.

## Practical Use

When implementing a chatbot, use an LLM prompt (e.g., 'Given the following conversation, rewrite the last user input...') to rewrite ambiguous queries like 'How about Emily Doe?' into 'When was the last time Emily Doe bought something from us?'

## Related

- Contextual Retrieval
- [[Multi-Stage-Retrieval-Pipeline|Multi-Stage Retrieval Pipeline]]
