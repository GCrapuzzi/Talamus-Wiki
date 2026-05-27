---
type: pattern
status: evergreen
aliases:
  - Single-Turn vs. Multi-Turn Data
  - Instructional vs. Conversational Data
  - Atomic vs. Sequential Data
tags:
  - data-format
  - conversational-ai
  - data-curation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When curating data for applications with conversation interfaces, you need to consider whether you require single-turn data, multi-turn data, or both.
      - Single-turn data helps train a model to respond to individual instructions. Multi-turn data, on the other hand, teaches the model how to solve tasks
created: 2026-05-26T21:55:46.312911+00:00
updated: 2026-05-26T21:55:46.312911+00:00
ingestion_run: 8d527d59
---

# Single-Turn vs. Multi-Turn Data

## Summary

A classification of training data based on interaction complexity: Single-turn data handles isolated instructions, while multi-turn data teaches the model to maintain context and solve tasks through back-and-forth dialogue.

## Core Idea

The choice of data type dictates the model's capability: single-turn for simple responses, multi-turn for complex, real-world task completion (e.g., clarification, iterative refinement).

## Practical Use

If the application requires the model to clarify intent or handle corrections, prioritize collecting and curating multi-turn conversational data. If the task is simple and self-contained, single-turn data suffices.

## Related

- [[Data-Curation-Lifecycle|Data Curation Lifecycle]]
