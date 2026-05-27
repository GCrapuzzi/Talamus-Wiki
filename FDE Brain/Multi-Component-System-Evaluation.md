---
type: pattern
status: evergreen
aliases:
  - Multi-Component System Evaluation
  - System Decomposition Testing
  - Pipeline Evaluation
  - Granular AI Testing
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/086-design-your-evaluation-pipeline.md
    locator: pages 224-224
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Evaluation can happen at different levels: per task, per turn, and per intermediate output."
      - If the model fails to extract the right current employer, it can be because of either step [in a two-step process].
      - If you don’t evaluate each component independently, you don’t know exactly where your system fails.
created: 2026-05-26T21:55:45.852272+00:00
updated: 2026-05-26T21:55:45.852272+00:00
ingestion_run: 8d527d59
---

# Multi-Component System Evaluation

## Summary

A structured methodology for evaluating complex, multi-stage AI applications by testing each component and intermediate output independently, rather than relying solely on end-to-end performance.

## Core Idea

Real-world AI applications are composed of multiple sequential or parallel components (e.g., PDF parsing -> Text Extraction -> Entity Recognition). To accurately diagnose failure points and improve reliability, evaluation must pinpoint *where* the system fails, not just *that* it failed. This requires evaluating components in isolation.

## Practical Use

When building a complex system (e.g., a document processing pipeline), first evaluate the foundational steps (e.g., OCR accuracy, text extraction similarity) using dedicated metrics. Then, evaluate the subsequent steps (e.g., NER accuracy) using the clean output of the previous step as input. This isolates failure modes.

## Related

- Evaluation Granularity
- Public Benchmarks (Contrast)
