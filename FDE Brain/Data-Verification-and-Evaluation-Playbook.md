---
type: pattern
status: evergreen
aliases:
  - Data Verification and Evaluation Playbook
  - Data Validation Loop
  - Synthetic Data Quality Check
tags:
  - data-validation
  - llm-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/155-summary.md
    locator: pages 427-428
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Evaluating AI-generated data is just as tricky as evaluating other AI outputs, and people are more likely to use generated data that they can reliably evaluate.
      - It’s hard to annotate data, but it’s even harder to create annotation guidelines.
created: 2026-05-26T21:55:46.426436+00:00
updated: 2026-05-26T21:55:46.426436+00:00
ingestion_run: 8d527d59
---

# Data Verification and Evaluation Playbook

## Summary

A multi-stage process for rigorously testing and validating both real and synthetic data to ensure fitness for purpose before model training. This includes verifying annotation guidelines and data integrity.

## Core Idea

Data evaluation is a critical, non-automatable step. The reliability of the data is paramount; therefore, evaluation techniques must be robust and repeatable, especially for AI-generated content.

## Practical Use

Implement a validation playbook that includes: 1) Checking for statistical drift (coverage), 2) Testing edge cases (diversity), and 3) Having human review loops for annotation guidelines (quality).

## Related

- [[Synthetic-Data-Generation|Synthetic Data Generation]]
- [[Dataset-Design-Core-Criteria|Dataset Design Core Criteria]]
