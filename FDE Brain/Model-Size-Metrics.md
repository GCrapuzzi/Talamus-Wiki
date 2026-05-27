---
type: glossary
status: evergreen
aliases:
  - Model Size Metrics
  - LLM scale measurement
  - Model capacity metrics
tags:
  - ai-engineering
  - llm-architecture
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/054-summary.md
    locator: pages 135-136
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "The scale of a model can be measured by three key numbers: the number of parameters, the number of training tokens, and the number of FLOPs needed for training."
created: 2026-05-26T21:55:45.633110+00:00
updated: 2026-05-26T21:55:45.633110+00:00
ingestion_run: 8d527d59
---

# Model Size Metrics

## Summary

Three key quantitative measures used to characterize the scale and computational requirements of a foundation model: Parameters, Training Tokens, and FLOPs.

## Core Idea

These metrics provide a standardized way to compare model capacity and computational cost. Model performance is influenced by the interplay between these three factors.

## Practical Use

Use these metrics to benchmark models and estimate training costs. A model's performance is influenced by both its size (parameters) and the amount of data it sees (tokens).

## Related

- [[Scaling-Law-Optimization|Scaling Law Optimization]]
- [[Transformer-Architecture|Transformer Architecture]]
