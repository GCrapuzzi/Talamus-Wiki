---
type: pattern
status: evergreen
aliases:
  - Prompt Decomposition
  - Task Decomposition
  - Decomposing Prompts
tags:
  - ai-engineering
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/100-give-the-model-time-to-think.md
    locator: pages 251-252
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Prompt decomposition can increase latency but improves performance and reliability.
      - Decomposition allows using cheaper models for simpler steps (e.g., intent classification) and stronger models for complex generation.
created: 2026-05-26T21:55:45.954553+00:00
updated: 2026-05-26T21:55:45.954553+00:00
ingestion_run: 8d527d59
---

# Prompt Decomposition

## Summary

Breaking a single, complex prompt into multiple, smaller, sequential prompts, each targeting a specific subtask.

## Core Idea

Decomposition improves the reliability and performance of complex AI applications by managing complexity and allowing for specialized model usage. It can also optimize costs by enabling the use of cheaper models for simpler steps.

## Practical Use

When a prompt exceeds a manageable token limit or when a task requires distinct stages of reasoning (e.g., first classifying intent, then generating a response). This pattern is crucial for maintaining performance as applications scale.

## Related

- Chain-of-Thought Prompting
- [[Model-Tiering|Model Tiering]]
