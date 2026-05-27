---
type: method
status: evergreen
aliases:
  - Supervised Finetuning (SFT)
  - Instruction Finetuning
  - Supervised Fine-Tuning
tags:
  - ai-engineering
  - llm-alignment
  - data-labeling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
    locator: pages 332-334
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Supervised finetuning uses high-quality annotated data to refine the model to align with human usage and preference.
      - "During supervised finetuning, the model is trained using (input, output) pairs: the input can be an instruction and the output can be a response."
created: 2026-05-26T21:55:46.162924+00:00
updated: 2026-05-26T21:55:46.162924+00:00
ingestion_run: 8d527d59
---

# Supervised Finetuning (SFT)

## Summary

Training a model using high-quality, labeled (input, output) pairs, where the input is typically an instruction and the output is the desired response. This is the most common method for aligning models to specific tasks.

## Core Idea

SFT teaches the model to follow explicit instructions and adopt a desired format or style. It is crucial for aligning the model's output to human-defined usage patterns.

## Practical Use

Use SFT when you have a dataset of high-quality examples of (Instruction, Ideal Response) pairs. This is necessary for tasks requiring specific formatting, domain expertise, or adherence to complex rules (e.g., summarizing legal documents according to a specific template).

## Related

- Instruction Tuning
- [[Prompt-Engineering|Prompt Engineering]]
