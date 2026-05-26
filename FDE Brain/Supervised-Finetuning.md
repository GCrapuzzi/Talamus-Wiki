---
type: method
tags: [finetuning, supervised-learning, instruction-tuning, RLHF]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#finetuning-overview
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Supervised Finetuning

Training a pre-trained model on (input, output) pairs to align it with human usage and preference.

- **Input**: instruction or prompt
- **Output**: desired response (open-ended like summaries, or close-ended like classification labels)

High-quality instruction data is challenging and expensive to create, especially for tasks requiring factual consistency, domain expertise, or political correctness.

Variants of post-training finetuning:
- **Supervised finetuning (SFT)**: learn from (instruction, response) pairs
- **Preference finetuning**: learn from (instruction, winning response, losing response) triples via reinforcement learning
- **Long-context finetuning**: modify positional embeddings to extend context length (harder, may degrade short-sequence performance)

Model developers typically apply multiple finetuning stages before release. Application developers usually finetune an already post-trained model, reducing the adaptation work needed.
