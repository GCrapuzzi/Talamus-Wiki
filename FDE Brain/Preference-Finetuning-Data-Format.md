---
type: pattern
status: evergreen
aliases:
  - Preference Finetuning Data Format
  - RLHF Data
  - Comparison Data
tags:
  - data-format
  - rlhf
  - alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For preference finetuning, you need data in the (instruction, winning response, losing response) format.
created: 2026-05-26T21:55:46.304353+00:00
updated: 2026-05-26T21:55:46.304353+00:00
ingestion_run: 8d527d59
---

# Preference Finetuning Data Format

## Summary

Data structured to teach models human preferences by providing a prompt and multiple potential responses, identifying a 'winning' (preferred) and 'losing' (rejected) response.

## Core Idea

This format is essential for aligning models with human values and desired conversational styles, improving safety and helpfulness.

## Practical Use

When fine-tuning a model using Reinforcement Learning from Human Feedback (RLHF), collect pairs of responses for the same prompt and annotate which response is superior.

## Related

- Reward Model Training
- [[Instruction-Finetuning-Data-Format|Instruction Finetuning Data Format]]
