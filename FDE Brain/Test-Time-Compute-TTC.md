---
type: method
status: evergreen
aliases:
  - Test Time Compute (TTC)
  - Self-Correction Sampling
  - Multiple Sampling
tags:
  - ai-engineering
  - reliability
  - llm-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/052-structured-outputs.md
    locator: pages 123-128
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Picking out the most common output among a set of outputs can be especially useful for tasks that expect exact answers.
      - A model is considered robust if it doesn’t dramatically change its outputs with small variations in the input.
created: 2026-05-26T21:55:45.603566+00:00
updated: 2026-05-26T21:55:45.603566+00:00
ingestion_run: 8d527d59
---

# Test Time Compute (TTC)

## Summary

A technique to improve model robustness and accuracy by generating multiple outputs (sampling) for a single query and then aggregating or selecting the most consistent or frequent result.

## Core Idea

Brittle models can fail due to input variations or internal stochasticity. By running the query multiple times, the variance in the outputs can be reduced, allowing the system to select the most reliable answer (e.g., majority vote for multiple-choice, mode for math problems).

## Practical Use

For critical tasks (e.g., classification, mathematical problem solving), run the LLM 3-5 times with the same prompt and use a post-processing step to determine the mode or consensus answer, significantly increasing reliability over a single pass.

## Related

- Robustness Testing
- [[Structured-Outputs|Structured Outputs]]
