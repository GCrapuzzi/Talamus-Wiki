---
type: framework
status: evergreen
aliases:
  - Data Slicing for Evaluation
  - subset evaluation
  - granular testing
tags:
  - ai-engineering
  - data-governance
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/089-step-3.-define-evaluation-methods-and-data.md
    locator: pages 228-231
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Slicing means separating your data into subsets and looking at your system’s performance on each subset separately.
      - Avoid potential biases, such as biases against minority user groups.
      - Avoid falling for Simpson’s paradox
created: 2026-05-26T21:55:45.876299+00:00
updated: 2026-05-26T21:55:45.876299+00:00
ingestion_run: 8d527d59
---

# Data Slicing for Evaluation

## Summary

Separating the overall evaluation dataset into multiple, distinct subsets (slices) to analyze system performance on specific attributes, thereby gaining a finer-grained understanding of model weaknesses and biases.

## Core Idea

Aggregated performance metrics can mask significant failures. Slicing prevents falling for biases (e.g., minority groups) and avoids Simpson’s paradox, ensuring that performance improvements are robust across all operational segments.

## Practical Use

When evaluating a customer service chatbot, slice the data by 'user intent' (e.g., billing vs. technical support), 'input length' (short vs. long queries), or 'user tier' (paying vs. free) to identify specific failure modes before deployment.

## Related

- Bias Detection
- [[Evaluation-Set-Design-Principles|Evaluation Set Design Principles]]
