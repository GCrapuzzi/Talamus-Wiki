---
type: framework
status: evergreen
aliases:
  - Dataset Design Core Criteria
  - Data Quality Checklist
  - Training Data Requirements
tags:
  - data-engineering
  - llm-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/155-summary.md
    locator: pages 427-428
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "dataset design across training phases shares the same three core criteria: quality, coverage, and quantity."
      - A small amount of high-quality data can outperform a large amount of noisy data.
created: 2026-05-26T21:55:46.421361+00:00
updated: 2026-05-26T21:55:46.421361+00:00
ingestion_run: 8d527d59
---

# Dataset Design Core Criteria

## Summary

The three universal criteria for designing a dataset: Quality, Coverage, and Quantity. High quality and sufficient coverage are often more critical than sheer volume.

## Core Idea

Effective dataset design requires balancing these three criteria. A small amount of high-quality, diverse data can outperform a large volume of noisy data.

## Practical Use

When scoping a new model project, use this framework to guide data acquisition. Prioritize improving data diversity and quality (e.g., through better annotation guidelines) before simply seeking more data points.

## Related

- Data Governance Roles
- [[Synthetic-Data-Generation|Synthetic Data Generation]]
