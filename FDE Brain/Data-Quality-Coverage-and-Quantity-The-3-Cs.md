---
type: framework
status: evergreen
aliases:
  - Data Quality, Coverage, and Quantity (The 3 Cs)
  - Data Completeness Criteria
  - Data Mix Assessment
tags:
  - data-curation
  - data-governance
  - ai-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "At a high level, however, data curation follows the three criteria: data quality, data coverage, and data quantity."
created: 2026-05-26T21:55:46.315336+00:00
updated: 2026-05-26T21:55:46.315336+00:00
ingestion_run: 8d527d59
---

# Data Quality, Coverage, and Quantity (The 3 Cs)

## Summary

The three fundamental criteria for assessing and curating a dataset: Quality (accuracy/purity), Coverage (breadth of topics/scenarios), and Quantity (sheer volume of examples).

## Core Idea

Model performance is limited by the weakest data characteristic. High-quality data is useless if it lacks coverage, and comprehensive coverage is impractical without sufficient quantity.

## Practical Use

Before training, audit the dataset against these three axes. If the model fails on a specific type of query, the issue is likely low coverage. If the model gives factually incorrect answers, the issue is low quality.

## Related

- [[Data-Curation-Lifecycle|Data Curation Lifecycle]]
