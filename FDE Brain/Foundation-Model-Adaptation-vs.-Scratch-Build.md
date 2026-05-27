---
type: pattern
status: evergreen
aliases:
  - Foundation Model Adaptation vs. Scratch Build
  - Buy vs. Build Decision Framework
tags:
  - ai-engineering
  - strategy
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/018-from-foundation-models-to-ai-engineering.md
    locator: pages 36-39
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Adapting an existing powerful model to your task is generally a lot easier than building a model for your task from scratch...
      - there are still many benefits to task-specific models, for example, they might be a lot smaller, making them faster and cheaper to use.
created: 2026-05-26T21:55:45.353596+00:00
updated: 2026-05-26T21:55:45.353596+00:00
ingestion_run: 8d527d59
---

# Foundation Model Adaptation vs. Scratch Build

## Summary

A decision framework comparing the effort, data requirements, and time-to-market between adapting an existing Foundation Model and training a model from scratch.

## Core Idea

Adapting an existing FM is significantly faster and cheaper than building a model from scratch, especially when data is limited. However, task-specific models may still be preferred if smaller size, speed, or specialized performance is critical.

## Practical Use

Use this framework to estimate project feasibility. If the required data volume is massive (millions of examples) or the timeline is long (months), prioritize FM adaptation. If the performance gain from specialization outweighs the development cost, consider a custom build.

## Related

- [[AI-Engineering|AI Engineering]]
- Model Selection Strategy
