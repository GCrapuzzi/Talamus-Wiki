---
type: concept
tags: [transfer-learning, finetuning, foundation-models, sample-efficiency]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#finetuning-overview
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Transfer Learning

Transfer learning focuses on transferring knowledge gained from one task to accelerate learning for a new, related task. First introduced by Bozinovski and Fulgosi (1976).

Two main forms:
- **Finetuning-based transfer**: adjust model weights on a target task starting from a pre-trained checkpoint
- **Feature-based transfer**: extract embeddings from a pre-trained model and feed them to a downstream model (e.g., ImageNet features for object detection)

Transfer learning improves Sample Efficiency—a finetuned model can match from-scratch performance with orders of magnitude fewer examples. OpenAI's InstructGPT paper (2022) framed finetuning as *unlocking* capabilities already present in the base model but hard to elicit via prompting alone.

For LLMs, knowledge from self-supervised pre-training on text completion transfers to specialized tasks (legal QA, text-to-SQL) that have limited labeled data.
