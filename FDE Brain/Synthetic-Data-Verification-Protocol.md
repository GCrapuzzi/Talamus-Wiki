---
type: operational-playbook
status: evergreen
aliases:
  - Synthetic Data Verification Protocol
  - Data quality filtering
  - Synthetic data validation
tags:
  - ai-engineering
  - data-curation
  - mlops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/150-data-processing.md
    locator: pages 420-420
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - training indiscriminately on self-generated data doesn’t improve the model’s performance and can even degrade it.
      - by introducing mechanisms to verify the quality of synthetic data and using only verified synthetic data, they were able to continually improve a model using its generated data.
created: 2026-05-26T21:55:46.392505+00:00
updated: 2026-05-26T21:55:46.392505+00:00
ingestion_run: 8d527d59
---

# Synthetic Data Verification Protocol

## Summary

A mandatory process for curating synthetic data to ensure that the data quality does not degrade the performance of the target model. This involves implementing mechanisms to verify the coherence, diversity, and factual accuracy of generated examples.

## Core Idea

While synthetic data is scalable, training indiscriminately on self-generated data can lead to model degradation (model collapse). Verification protocols are necessary to ensure the synthetic data acts as a genuine improvement signal, not just noise.

## Practical Use

Before using synthetic data for finetuning, implement a multi-stage validation pipeline: 1) Filter for diversity (avoiding repetitive patterns). 2) Check for factual consistency (grounding). 3) Use a secondary, smaller model to score the quality of the generated data points, discarding low-confidence examples.

## Related

- [[Synthetic-Data-Tuning-with-Adapters|Synthetic Data Tuning with Adapters]]
