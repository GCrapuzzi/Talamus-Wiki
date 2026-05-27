---
type: method
status: evergreen
aliases:
  - Training Data Scale Measurement
  - Data Scaling Metrics
  - Data Quantity Assessment
tags:
  - ai-engineering
  - data-engineering
  - foundation-models
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
    locator: pages 91-101
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A book is worth a lot more than a sentence, so the number of training samples is no longer a good metric to measure dataset sizes.
      - A better measurement is the number of tokens in the dataset.
      - The number of training tokens measures the tokens that the model is trained on. If a dataset contains 1 trillion tokens and a model is trained on that dataset for two epochs... the number of training tokens is 2 trillion.
created: 2026-05-26T21:55:45.540082+00:00
updated: 2026-05-26T21:55:45.540082+00:00
ingestion_run: 8d527d59
---

# Training Data Scale Measurement

## Summary

A framework for assessing the scale of training data, prioritizing token count over simple sample count, and recognizing the importance of data quality and diversity.

## Core Idea

While model size (parameters) and data quantity are critical, the most robust metrics are the total number of tokens (measure of content volume) and the data quality/diversity. The number of training tokens must account for the number of epochs (passes) over the dataset.

## Practical Use

When comparing foundation models, always request the dataset size in tokens and the number of training epochs. Never rely solely on the number of training samples, as this metric is misleading for large-scale data.

## Related

- Data Quality and Diversity
- Training Tokens
