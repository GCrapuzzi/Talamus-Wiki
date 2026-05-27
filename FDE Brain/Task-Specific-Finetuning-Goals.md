---
type: pattern
status: evergreen
aliases:
  - Task-Specific Finetuning Goals
  - Improving Domain Specificity
  - Structured Output Training
tags:
  - ai-engineering
  - llm-finetuning
  - data-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/125-when-to-finetune.md
    locator: pages 335-335
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The primary reason for finetuning is to improve a model’s quality, in terms of both general capabilities and task-specific capabilities.
      - Finetuning is commonly used to improve a model’s ability to generate outputs following specific structures, such as JSON or YAML formats.
      - An out-of-the-box model might be good at converting from text to the standard SQL dialect but might fail with a less common SQL dialect. In this case, finetuning this model on data containing this SQL dialect will help.
created: 2026-05-26T21:55:46.178894+00:00
updated: 2026-05-26T21:55:46.178894+00:00
ingestion_run: 8d527d59
---

# Task-Specific Finetuning Goals

## Summary

Using finetuning to bridge the gap between a general-purpose model's capabilities and the specific requirements of a niche domain or output format.

## Core Idea

General-purpose models perform well on broad benchmarks but often fail on specific, non-standard tasks (e.g., niche dialects, proprietary formats). Finetuning on domain-specific data is necessary to improve task-specific quality.

## Practical Use

1. **Structured Output:** Finetune the model specifically on examples that require JSON or YAML output formatting. 2. **Dialect/Domain Adaptation:** If the model fails on a specific SQL dialect or customer-specific query pattern, collect and finetune the model using data containing those exact patterns.

## Related

- Prompt Engineering Best Practices
- Data Curation for LLMs
