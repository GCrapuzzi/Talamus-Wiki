---
type: pattern
tags: [finetuning, transfer-learning, training-strategy]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-quantity
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Progressive Finetuning

Reduce the need for expensive high-quality data by first finetuning on cheaper/broader data, then refining on target data. Three variants:

1. **Self-supervised → supervised** — finetune on raw domain documents (e.g., legal texts) before finetuning on (question, answer) pairs
2. **Less-relevant → relevant** — finetune on adjacent-domain data (e.g., tweet sentiment) before target-domain data (e.g., product review sentiment)
3. **Synthetic → real** — finetune on AI-generated data first, then on limited real data. Harder to execute: requires coordinating two distinct finetuning jobs and managing the transition

This pattern exploits [[Transfer Learning]]—each stage narrows the model's distribution toward the target task.
