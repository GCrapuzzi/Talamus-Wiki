---
type: framework
status: evergreen
aliases:
  - Model Build vs. Buy Decision Framework
  - Model Deployment Strategy
  - Build vs Buy AI
tags:
  - ai-engineering
  - architecture
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/084-model-build-versus-buy.md
    locator: pages 205-214
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The question is whether to use commercial model APIs or host an open source model yourself.
      - The answer to this question can significantly reduce your candidate model pool.
created: 2026-05-26T21:55:45.836959+00:00
updated: 2026-05-26T21:55:45.836959+00:00
ingestion_run: 8d527d59
---

# Model Build vs. Buy Decision Framework

## Summary

A structured approach to determining whether to use commercial APIs (Buy) or host and manage open-source models internally (Build).

## Core Idea

The choice significantly impacts cost, control, performance ceiling, and legal risk. The decision is not binary and often requires evaluating performance needs against operational constraints.

## Practical Use

When starting a new AI feature, use this framework to evaluate options: 1. If maximum performance/speed-to-market is critical and budget allows, consider commercial APIs. 2. If data privacy, customization, or long-term cost control is paramount, evaluate open-source hosting. 3. If the model is commodity or requires minimal customization, an API might suffice.

## Related

- [[Model-Selection-Workflow|Model Selection Workflow]]
- Inference Service Optimization
