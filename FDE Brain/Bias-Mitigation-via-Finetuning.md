---
type: concept
status: evergreen
aliases:
  - Bias Mitigation via Finetuning
  - Bias Correction
  - Bias Alignment
tags:
  - ai-engineering
  - ethics-ai
  - bias-mitigation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/127-reasons-not-to-finetune.md
    locator: pages 336-339
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - if the base model perpetuates certain biases from its training data, exposing it to carefully curated data during finetuning can counteract these biases
created: 2026-05-26T21:55:46.195907+00:00
updated: 2026-05-26T21:55:46.195907+00:00
ingestion_run: 8d527d59
---

# Bias Mitigation via Finetuning

## Summary

Using finetuning on carefully curated, balanced datasets to counteract or mitigate specific biases (e.g., gender, racial) that a base model may have inherited from its general training data.

## Core Idea

While base models reflect the biases of their vast training corpora, targeted finetuning can be used as a corrective measure to steer the model's output toward desired, equitable representations.

## Practical Use

If a model consistently exhibits a demographic bias (e.g., associating certain professions with one gender), curate a dataset that explicitly counteracts this pattern and finetune the model on it.

## Related

- Alignment Tax
- Data Curation
