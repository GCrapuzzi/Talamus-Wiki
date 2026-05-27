---
type: method
status: evergreen
aliases:
  - Data Quality Improvement Techniques
  - data augmentation
  - edge case mining
  - data cleaning
tags:
  - ai-engineering
  - data-quality
  - implementation-method
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/139-chapter-8.-dataset-engineering.md
    locator: pages 387-388
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Participants needed to improve upon the same base dataset by applying techniques such as fixing incorrect labels, adding edge case examples, augmenting data, etc.
created: 2026-05-26T21:55:46.295003+00:00
updated: 2026-05-26T21:55:46.295003+00:00
ingestion_run: 8d527d59
---

# Data Quality Improvement Techniques

## Summary

Specific techniques used to enhance the robustness and coverage of a dataset, moving beyond simple data collection to actively improve data fidelity.

## Core Idea

High data quality is achieved by addressing systematic flaws, not just increasing volume. Key techniques include fixing incorrect labels, adding examples that represent rare or difficult scenarios (edge cases), and deduplicating redundant information.

## Practical Use

When performance plateaus, apply these techniques: 1. Review failure modes to identify missing edge cases. 2. Implement automated label validation and human review loops. 3. Use augmentation techniques to expand data variety.

## Related

- [[Data-Centric-AI|Data-Centric AI]]
- [[Dataset-Engineering-Lifecycle|Dataset Engineering Lifecycle]]
