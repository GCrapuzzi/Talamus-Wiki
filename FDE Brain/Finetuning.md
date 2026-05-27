---
type: method
status: evergreen
aliases:
  - Finetuning
  - Model Adaptation
  - Post-training refinement
tags:
  - ai-engineering
  - llm-deployment
  - model-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
    locator: pages 332-334
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Finetuning is one way to do transfer learning.
      - Finetuning is an extension of model pre-training.
      - Ideally, much of what the model needs to learn is already present in the base model, and finetuning just refines the model’s behavior.
created: 2026-05-26T21:55:46.160909+00:00
updated: 2026-05-26T21:55:46.160909+00:00
ingestion_run: 8d527d59
---

# Finetuning

## Summary

An extension of model pre-training where a pre-trained base model is further trained on a specific, task-related dataset to refine its behavior and optimize performance for a narrow application.

## Core Idea

Finetuning assumes that the base model already possesses most of the necessary knowledge; the goal is not to teach it everything, but to 'unlock' or refine its existing capabilities to align with human usage and specific task requirements.

## Practical Use

After selecting a foundation model, finetuning is the primary step to specialize it. The choice of finetuning technique (SFT, Preference, etc.) depends on the type of data available and the desired alignment goal.

## Related

- Supervised Finetuning
- [[Self-supervised-Finetuning|Self-supervised Finetuning]]
- [[Preference-Finetuning|Preference Finetuning]]
