---
type: operation
tags: [hyperparameters, finetuning, learning-rate, batch-size, gradient-accumulation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#finetuning-tactics
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Finetuning Hyperparameters

Key hyperparameters for finetuning LLMs:

**Learning rate** (typically 1e-7 to 1e-3):
- Start from pre-training's final LR × constant (0.1–1.0)
- Loss curve fluctuating → LR too high; stable but slow → LR too low
- Use learning rate schedules (larger early, smaller late)

**Batch size**:
- Too small (< 8) → unstable training
- Larger → more stable updates, faster throughput, but more memory
- **Gradient accumulation**: simulate larger batch by accumulating gradients across multiple small batches before updating weights

**Number of epochs**:
- Large datasets (millions): 1–2 epochs often sufficient
- Small datasets (thousands): 4–10 epochs may help
- Training loss ↓ but validation loss ↑ → overfitting, reduce epochs

**Prompt loss weight** (for instruction finetuning):
- Controls how much prompt tokens vs response tokens contribute to loss
- Default typically 10% — model learns mostly from responses since prompts are user-provided at inference time
