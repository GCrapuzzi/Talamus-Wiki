---
type: concept
status: evergreen
aliases:
  - Contextual Grounding
  - RAG Principle
  - Knowledge Injection
tags:
  - ai-engineering
  - data-retrieval
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/109-summary.md
    locator: pages 275-276
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - to accomplish a task, a model needs not just instructions but also relevant context.
created: 2026-05-26T21:55:46.034571+00:00
updated: 2026-05-26T21:55:46.034571+00:00
ingestion_run: 8d527d59
---

# Contextual Grounding

## Summary

The principle that achieving a task requires not only clear instructions (the prompt) but also the provision of relevant, external, and accurate information (the context).

## Core Idea

Foundation models are powerful, but their knowledge is limited by their training data and the immediate prompt. To ensure factual accuracy and relevance, the model must be explicitly provided with the necessary source material or context.

## Practical Use

Before calling the LLM, retrieve relevant documents or data snippets based on the user's query. Structure the prompt to include a section like: 'Use ONLY the following context to answer the question. If the context does not contain the answer, state that you do not know.'

## Related

- [[Prompt-Engineering|Prompt Engineering]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
