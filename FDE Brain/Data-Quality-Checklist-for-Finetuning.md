---
type: framework
status: evergreen
aliases:
  - Data Quality Checklist for Finetuning
  - High-Quality Data Criteria
  - Data Quality for LLMs
tags:
  - ai-engineering
  - data-quality
  - finetuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/141-data-quality.md
    locator: pages 392-392
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Data is considered high-quality if it helps you do your job efficiently and reliably.
      - "Data can be considered high-quality if it has the following six characteristics: relevant, aligned with task requirements, consistent, correctly formatted, unique, and compliant."
created: 2026-05-26T21:55:46.317139+00:00
updated: 2026-05-26T21:55:46.317139+00:00
ingestion_run: 8d527d59
---

# Data Quality Checklist for Finetuning

## Summary

A set of six core characteristics used to evaluate if a dataset is suitable for finetuning an LLM, ensuring the data is efficient and reliable for the intended task.

## Core Idea

High-quality data is defined not by volume, but by its adherence to specific criteria (relevant, aligned, consistent, etc.). Using a small amount of highly curated data is often superior to large amounts of noisy or inconsistent data.

## Practical Use

When curating a dataset for instruction tuning or RAG, use this checklist to audit the data. For example, if the task requires factual consistency, ensure the data is 'aligned with task requirements' by including both the score and the justification, not just the score.

## Related

- Dataset Engineering
- Instruction Tuning
- Data Curation Playbook
