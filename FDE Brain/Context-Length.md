---
type: glossary
status: evergreen
aliases:
  - Context Length
  - Context Window
  - Token Limit
tags:
  - llm-architecture
  - prompt-engineering
  - system-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/095-context-length-and-context-efficiency.md
    locator: pages 242-243
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Models' maximum context length has increased rapidly in recent years.
      - A 2M context length can fit approximately 2,000 Wikipedia pages and a reasonably complex codebase.
created: 2026-05-26T21:55:45.920956+00:00
updated: 2026-05-26T21:55:45.920956+00:00
ingestion_run: 8d527d59
---

# Context Length

## Summary

The maximum amount of input data (measured in tokens) that an LLM can process and consider at one time. Modern models are rapidly expanding this limit (e.g., 1K to 2M tokens).

## Core Idea

Context length dictates the scope and complexity of tasks an LLM can handle. A larger context window allows the model to process entire documents, codebases, or long conversations in a single prompt, moving beyond simple essay-length inputs.

## Practical Use

When designing a system, determine if the required input data (e.g., a legal document, a full codebase, a transcript) exceeds the model's context length. If so, implement chunking, summarization, or retrieval-augmented generation (RAG) strategies.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- Context Efficiency
