---
type: framework
status: evergreen
aliases:
  - LLM Performance Improvement Workflow
  - AI Model Optimization Funnel
  - Prompting to Finetuning Progression
tags:
  - ai-engineering
  - llm-deployment
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/129-memory-bottlenecks.md
    locator: pages 343-343
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The process starts with prompting alone.
      - Adding examples (1-50) is the next step.
      - Connecting to data sources (RAG) addresses missing information.
      - Advanced RAG (embedding-based) addresses information failures.
      - Finetuning addresses behavioral issues.
      - Combining RAG and finetuning offers maximum performance.
created: 2026-05-26T21:55:46.205740+00:00
updated: 2026-05-26T21:55:46.205740+00:00
ingestion_run: 8d527d59
---

# LLM Performance Improvement Workflow

## Summary

A systematic, staged approach for improving LLM performance, moving from simple prompting to complex data integration and model fine-tuning.

## Core Idea

Model improvement should be iterative and escalate in complexity. Start with the lowest-cost intervention (prompting) before moving to high-cost, high-complexity methods (finetuning).

## Practical Use

When an LLM fails, follow this hierarchy: 1. Improve prompts (Systematic Prompt Versioning). 2. Add examples (Few-Shot Learning). 3. Integrate external data (RAG). 4. If information is missing, upgrade RAG (e.g., to embedding-based). 5. If behavior is wrong, consider finetuning. 6. Combine RAG and finetuning for maximum boost.

## Related

- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- [[Prompt-Engineering|Prompt Engineering]]
- Finetuning Strategy
