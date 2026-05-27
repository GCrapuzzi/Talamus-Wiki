---
type: method
status: evergreen
aliases:
  - Post-Training Alignment Pipeline
  - Model alignment
  - Supervised and Preference Tuning
tags:
  - ai-engineering
  - llm-alignment
  - finetuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/054-summary.md
    locator: pages 135-136
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "This is addressed by post-training, which consists of two steps: supervised finetuning and preference finetuning."
created: 2026-05-26T21:55:45.629333+00:00
updated: 2026-05-26T21:55:45.629333+00:00
ingestion_run: 8d527d59
---

# Post-Training Alignment Pipeline

## Summary

A two-step process applied after initial pre-training to align a foundation model's output with desired user preferences and safety guidelines.

## Core Idea

Pre-training data and self-supervision can lead to misaligned outputs. Post-training (SFT and Preference Tuning) is necessary to refine the model's behavior and make it useful for specific user contexts.

## Practical Use

Implement a pipeline sequence: 1. Supervised Finetuning (SFT) using high-quality, curated examples. 2. Preference Finetuning (e.g., RLHF/DPO) using human feedback data to rank and refine model responses based on quality and safety.

## Related

- Supervised Finetuning
- [[Preference-Finetuning|Preference Finetuning]]
- [[AI-Model-Hallucination-Detection|AI Model Hallucination Detection]]
