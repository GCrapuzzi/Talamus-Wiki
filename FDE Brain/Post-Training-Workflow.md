---
type: pattern
status: evergreen
aliases:
  - Post-Training Workflow
  - Model Alignment
  - LLM Refinement
tags:
  - ai-engineering
  - llm-deployment
  - alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/045-post-training.md
    locator: pages 102-103
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Post-training generally consists of two steps: Supervised finetuning and Preference finetuning."
      - Post-training optimizes the model to generate responses that users prefer, unlike pre-training which optimizes token-level quality.
created: 2026-05-26T21:55:45.543584+00:00
updated: 2026-05-26T21:55:45.543584+00:00
ingestion_run: 8d527d59
---

# Post-Training Workflow

## Summary

The multi-stage process of refining a pre-trained foundation model to optimize it for conversational quality, safety, and human preference, moving beyond simple token prediction.

## Core Idea

Pre-trained models optimize for token-level quality (completion), but users require high-level response quality (conversation). Post-training addresses two core issues: optimizing for conversation vs. completion, and mitigating toxic/unaligned outputs from indiscriminate internet data.

## Practical Use

When deploying a foundation model, this pattern dictates the necessary steps: 1. Supervised Finetuning (SFT) to teach conversational format. 2. Preference Finetuning (e.g., RLHF/DPO) to ensure alignment with desired human values and safety standards.

## Related

- [[Supervised-Finetuning-SFT|Supervised Finetuning (SFT)]]
- [[Preference-Finetuning|Preference Finetuning]]
- Foundation Model Lifecycle
