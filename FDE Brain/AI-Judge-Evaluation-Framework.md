---
type: framework
status: evergreen
aliases:
  - AI Judge Evaluation Framework
  - Model Judge Selection
  - AI Evaluation Strategy
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The judge can either be stronger, weaker, or the same as the model being judged.
      - You might not have the budget to use the stronger model to generate all responses, so you use it to evaluate a subset of responses.
      - This technique is sometimes referred to as self-critique or self-ask.
created: 2026-05-26T21:55:45.739604+00:00
updated: 2026-05-26T21:55:45.739604+00:00
ingestion_run: 8d527d59
---

# AI Judge Evaluation Framework

## Summary

A decision framework for selecting the appropriate model (judge) relative to the models being evaluated (candidates), considering trade-offs between performance, cost, and latency.

## Core Idea

The judge model can be stronger, weaker, or the same as the candidate models. The choice depends on resource constraints (cost/latency) and the specific evaluation goal (e.g., sanity checks vs. general ranking).

## Practical Use

1. **Stronger Judge:** Use for high-stakes evaluation or guiding weaker models. 2. **Weaker Judge:** Use when cost/latency is critical, but the judge must still be reliable. 3. **Self-Critique/Self-Ask:** Use when the model needs to revise its own output, serving as a sanity check or revision nudge.

## Related

- [[Self-Critique-Pattern|Self-Critique Pattern]]
- Specialized Judge Types
