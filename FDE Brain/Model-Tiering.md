---
type: pattern
status: evergreen
aliases:
  - Model Tiering
  - Specialized Model Usage
  - Model Specialization
tags:
  - ai-engineering
  - architecture
  - cost-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/100-give-the-model-time-to-think.md
    locator: pages 251-252
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - It is common to use a weaker model for intent classification and a stronger model to generate user responses.
created: 2026-05-26T21:55:45.958194+00:00
updated: 2026-05-26T21:55:45.958194+00:00
ingestion_run: 8d527d59
---

# Model Tiering

## Summary

The practice of assigning different model sizes or capabilities to different stages of a multi-step workflow, based on the complexity of the required task.

## Core Idea

Optimizes the balance between cost, performance, and latency. Simple, high-volume tasks can use smaller, cheaper models, reserving larger, more powerful models for critical, complex reasoning or generation tasks.

## Practical Use

In customer support workflows, use a smaller model for initial intent classification (low cost) and reserve a larger, more capable model for generating nuanced user responses (high reliability).

## Related

- [[Prompt-Decomposition|Prompt Decomposition]]
