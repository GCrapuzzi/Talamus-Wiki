---
type: pattern
status: evergreen
aliases:
  - Hybrid Evaluation Pipeline
  - Multi-Modal Evaluation
  - Comprehensive Model Testing
tags:
  - ai-engineering
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/075-summary.md
    locator: pages 180-182
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - While promising, AI judges should be supplemented with exact evaluation, human evaluation, or both.
created: 2026-05-26T21:55:45.778791+00:00
updated: 2026-05-26T21:55:45.778791+00:00
ingestion_run: 8d527d59
---

# Hybrid Evaluation Pipeline

## Summary

A robust evaluation strategy that combines multiple evaluation types—exact metrics, subjective AI judging, and human review—to mitigate the weaknesses of any single method.

## Core Idea

Because open-ended, powerful models are challenging to evaluate, and no single metric is reliable (AI judges change, exact metrics fail on open-ended tasks), a combination of methods is necessary for reliable benchmarking.

## Practical Use

Design an evaluation suite that mandates three components: 1) Exact metrics (for functional checks), 2) AI-as-Judge (for scalable subjective scoring), and 3) Human evaluation (for essential sanity checks and ground truth validation).

## Related

- [[Comparative-Evaluation|Comparative Evaluation]]
- Human-in-the-Loop
