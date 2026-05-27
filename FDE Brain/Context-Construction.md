---
type: concept
status: evergreen
aliases:
  - Context Construction
  - Context Engineering
tags:
  - llm-prompting
  - data-pipeline
  - feature-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/111-rag.md
    locator: pages 277-279
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Context construction for foundation models is equivalent to feature engineering for classical ML models.
      - RAG as a technique to construct context specific to each query, instead of using the same context for all queries.
created: 2026-05-26T21:55:46.042473+00:00
updated: 2026-05-26T21:55:46.042473+00:00
ingestion_run: 8d527d59
---

# Context Construction

## Summary

The process of preparing and supplying the most relevant, query-specific information to an LLM input, rather than using a single, static context for all queries.

## Core Idea

Context construction is analogous to feature engineering in classical machine learning. Its purpose is to manage the model's input space, ensuring that the model receives only the necessary information to process an input, thereby improving focus and efficiency.

## Practical Use

Designing the input pipeline for an LLM application. Instead of passing a large document, the system must first filter or retrieve the specific paragraphs or data points relevant to the user's query before calling the model.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
