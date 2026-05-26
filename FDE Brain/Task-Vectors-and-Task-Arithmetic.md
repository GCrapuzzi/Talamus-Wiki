---
type: concept
tags: [task-vectors, task-arithmetic, model-merging, TIES, DARE]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-merging-and-multi-task-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Task Vectors and Task Arithmetic

A **task vector** (also called delta parameters) is obtained by subtracting the base model weights from a finetuned model's weights. It captures the essence of what the model learned for that task. With [[LoRA]], the task vector is simply the LoRA adapter weights.

Task vectors enable **task arithmetic** (Ilharco et al., 2022):
- **Addition**: combine task vectors to merge capabilities from multiple tasks
- **Subtraction**: remove specific capabilities or undesirable behaviors (e.g., facial recognition bias, pre-training biases)

Pruning insight (Yadav et al., 2023): most task vector parameters are redundant—keeping only the top 20% gives comparable performance to 100%. Pruning before merging (TIES, DARE) significantly improves merged model quality by reducing inter-task interference.
