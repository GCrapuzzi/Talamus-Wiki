---
type: pattern
status: evergreen
aliases:
  - Context Construction Pattern
  - Feature Engineering for Foundation Models
tags:
  - ai-engineering
  - rag
  - context-window
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/168-step-2.-put-in-guardrails.md
    locator: pages 475-479
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Context construction is like feature engineering for foundation models.
      - It gives the model the necessary information to produce an output.
created: 2026-05-26T21:55:46.520162+00:00
updated: 2026-05-26T21:55:46.520162+00:00
ingestion_run: 8d527d59
---

# Context Construction Pattern

## Summary

The process of augmenting a model's input context using external tools (e.g., web search, APIs, databases) to provide necessary, up-to-date, or specific information, thereby improving output quality.

## Core Idea

LLMs are limited by their training data cutoff and lack of real-time context. Context construction bridges this gap, making the system's output quality dependent on the quality and breadth of the provided context, much like feature engineering in traditional ML.

## Practical Use

Implement Retrieval-Augmented Generation (RAG) pipelines or tool-calling mechanisms. When designing a system, identify all necessary external data sources (e.g., internal knowledge base, real-time weather APIs) and integrate them into the prompt context before calling the LLM.

## Related

- [[RAG-Architecture|RAG Architecture]]
- Tool Use Pattern
