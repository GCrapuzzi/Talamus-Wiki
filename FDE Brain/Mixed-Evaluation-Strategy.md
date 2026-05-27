---
type: pattern
status: evergreen
aliases:
  - Mixed Evaluation Strategy
  - hybrid evaluation
  - multi-tier scoring
tags:
  - ai-engineering
  - evaluation
  - cost-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/089-step-3.-define-evaluation-methods-and-data.md
    locator: pages 228-231
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - you might have a cheap classifier that gives low-quality signals on 100% of your data, and an expensive AI judge to give high-quality signals on 1% of the data.
created: 2026-05-26T21:55:45.871622+00:00
updated: 2026-05-26T21:55:45.871622+00:00
ingestion_run: 8d527d59
---

# Mixed Evaluation Strategy

## Summary

Combining low-cost, high-volume automatic metrics (e.g., cheap classifiers) with high-cost, low-volume expert judgment (e.g., AI judges) to maintain confidence while managing operational costs.

## Core Idea

No single evaluation method is sufficient. By mixing methods, engineers can gain broad coverage (cheap signals on 100% of data) and deep, reliable insights (expensive signals on critical 1% of data), optimizing the signal-to-cost ratio.

## Practical Use

When evaluating a new LLM feature, use a fast, cheap classifier (e.g., keyword presence) to screen 100% of production traffic for basic quality signals, and reserve the expensive AI judge for a small, highly curated subset of data to measure nuanced criteria like factual consistency.

## Related

- [[Human-Evaluation-as-North-Star|Human Evaluation as North Star]]
- [[Data-Slicing-for-Evaluation|Data Slicing for Evaluation]]
