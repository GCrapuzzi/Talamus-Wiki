---
type: pattern
status: evergreen
aliases:
  - Data Quality vs. Quantity Principle
  - High-quality data focus
  - Data efficiency
tags:
  - data-curation
  - llm-training
  - performance-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/040-multilingual-models.md
    locator: pages 75-79
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - a model trained with a smaller amount of high-quality data might outperform a model trained with a large amount of low-quality data.
created: 2026-05-26T21:55:45.511384+00:00
updated: 2026-05-26T21:55:45.511384+00:00
ingestion_run: 8d527d59
---

# Data Quality vs. Quantity Principle

## Summary

Prioritizing smaller amounts of highly curated, domain-specific data over massive volumes of low-quality, general internet data.

## Core Idea

Model performance is often limited by data quality, not just quantity. A smaller, high-signal dataset can outperform a much larger, noisy dataset, especially for specialized tasks.

## Practical Use

When designing a training regimen, identify the most critical, high-signal data sources (e.g., specific code repositories, curated domain documents) and focus fine-tuning efforts there, rather than simply scraping the entire web.

## Related

- [[Curated-Dataset-Strategy|Curated Dataset Strategy]]
- [[Domain-Specific-Models|Domain-Specific Models]]
