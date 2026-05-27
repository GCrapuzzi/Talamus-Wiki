---
type: pattern
status: evergreen
aliases:
  - Multi-Component Evaluation Pipeline
  - System Decomposition Evaluation
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/087-step-1.-evaluate-all-components-in-a-system.md
    locator: pages 224-225
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the model fails to extract the right current employer, it can be because of either step [PDF-to-text or NER].
      - If you don’t evaluate each component independently, you don’t know exactly where your system fails.
created: 2026-05-26T21:55:45.856071+00:00
updated: 2026-05-26T21:55:45.856071+00:00
ingestion_run: 8d527d59
---

# Multi-Component Evaluation Pipeline

## Summary

A methodology for evaluating complex AI systems by breaking them down into independent, smaller components and testing each one separately, rather than relying solely on end-to-end output.

## Core Idea

Real-world AI applications are complex pipelines. Failure at the end-to-end level can originate from any component (e.g., PDF parsing, NER, or final reasoning). Evaluating components independently isolates the failure point, allowing for targeted debugging and improvement.

## Practical Use

When building a system (e.g., resume parsing), evaluate the PDF-to-text step using similarity metrics against ground truth, and then evaluate the subsequent NER step using accuracy metrics on the extracted text, rather than just checking the final output.

## Related

- [[AI-Evaluation-Granularity|AI Evaluation Granularity]]
- [[Task-Based-Evaluation|Task-Based Evaluation]]
