---
type: concept
status: evergreen
aliases:
  - Data Relevance Principle
  - Task-Specific Data Filtering
tags:
  - ai-engineering
  - data-curation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/141-data-quality.md
    locator: pages 392-392
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The training examples should be relevant to the task you’re training the model to do.
      - For example, if the task is to answer legal questions today, a legal dataset from the 19th century might not be relevant.
created: 2026-05-26T21:55:46.319584+00:00
updated: 2026-05-26T21:55:46.319584+00:00
ingestion_run: 8d527d59
---

# Data Relevance Principle

## Summary

The principle that training data must be directly applicable to the specific domain and time frame of the task at hand, even if the data is generally accurate.

## Core Idea

Data relevance is context-dependent. A dataset must match the scope of the problem (e.g., legal questions today vs. 19th-century law) to be effective.

## Practical Use

Before ingesting a dataset, define the precise scope (e.g., 'US tax law changes 2020-2024'). Filter out any examples that fall outside this defined temporal or topical boundary, regardless of their overall quality.

## Related

- [[Data-Quality-Checklist-for-Finetuning|Data Quality Checklist for Finetuning]]
