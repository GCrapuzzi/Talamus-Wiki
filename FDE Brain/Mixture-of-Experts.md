---
type: concept
tags: [mixture-of-experts, MoE, sparse-models, architecture, efficiency]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-size
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Mixture of Experts

A sparse model architecture where parameters are divided into expert groups, and only a subset of experts is active per token. This decouples total parameter count from inference cost.

**Example**: Mixtral 8x7B has 46.7B total parameters (not 56B due to shared params). At each layer, only 2 of 8 experts are active per token → effective cost of a 12.9B-parameter model.

Key properties:
- Total params ≠ active params → parameter count can be misleading
- Sparsity enables more efficient storage and computation
- A large sparse model can require less compute than a small dense model

The [[Chinchilla Scaling Law]] was developed for dense models; adapting it for MoE is an active research area.

See also: [[State Space Models]] (Jamba uses MoE with hybrid transformer-Mamba blocks).
