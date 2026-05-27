---
type: pattern
status: evergreen
aliases:
  - Data Scarcity Finetuning Strategies
  - Transfer Learning for Data Augmentation
  - Multi-stage Finetuning
tags:
  - ai-engineering
  - data-curation
  - transfer-learning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/143-data-quantity.md
    locator: pages 396-400
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can first finetune your model on legal documents in a self-supervised manner, then further finetune the model on (question, answer) pairs.
      - You can first finetune your model to classify tweet sentiments, then further finetune it to classify product sentiments.
created: 2026-05-26T21:55:46.336992+00:00
updated: 2026-05-26T21:55:46.336992+00:00
ingestion_run: 8d527d59
---

# Data Scarcity Finetuning Strategies

## Summary

A structured approach to reduce the need for high-quality, task-specific data by sequentially finetuning a model on related, lower-quality, or synthetic data before fine-tuning on the target data.

## Core Idea

By first training the model on a broad domain (e.g., legal documents) or a related task (e.g., tweet sentiment), the model learns foundational knowledge or general features, making the subsequent fine-tuning on the scarce, specific data more effective.

## Practical Use

1. **Self-supervised $\rightarrow$ supervised:** Pre-train on large, unlabeled domain data (e.g., legal documents) before fine-tuning on small (Q, A) pairs. 2. **Less-relevant $\rightarrow$ relevant:** Train on a related domain (e.g., general product reviews) before fine-tuning on the target domain (e.g., specific product reviews). 3. **Synthetic $\rightarrow$ real:** Use generative models to create initial data volume, followed by fine-tuning on limited real data.

## Related

- [[Data-Scaling-and-Finetuning-Strategy|Data Scaling and Finetuning Strategy]]
- Data Quality and Diversity
