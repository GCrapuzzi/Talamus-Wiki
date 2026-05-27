---
type: glossary
status: evergreen
aliases:
  - Pre-training vs. Finetuning vs. Post-training
  - Training Phases Spectrum
  - Model Training Lifecycle
tags:
  - ai-engineering
  - ml-ops
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/035-ai-engineering-versus-ml-engineering.md
    locator: pages 63-69
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Pre-training refers to training a model from scratch—the model weights are randomly initialized.
      - Finetuning means continuing to train a previously trained model—the model weights are obtained from the previous training process.
      - Conceptually, post-training and finetuning are the same and can be used interchangeably.
created: 2026-05-26T21:55:45.482521+00:00
updated: 2026-05-26T21:55:45.482521+00:00
ingestion_run: 8d527d59
---

# Pre-training vs. Finetuning vs. Post-training

## Summary

Defines the stages of model weight modification. Pre-training is training from scratch; Finetuning is continuing training on a pre-trained model; Post-training is conceptually similar to finetuning, often used by model developers.

## Core Idea

These phases represent a spectrum of resource intensity and knowledge acquisition. Pre-training is the most resource-intensive, establishing foundational knowledge, while finetuning specializes that knowledge.

## Practical Use

Understand that while 'training' is a general term, these specific phases define the scope of work. If you are an application developer, you are most likely dealing with the outcomes of pre-training and finetuning.

## Related

- [[Finetuning|Finetuning]]
- Pre-training
