---
type: concept
tags: [model-merging, task-arithmetic, SLERP, TIES, frankenmerging, federated-learning]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-merging-and-multi-task-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Merging

Combining multiple models into a single model that provides more value than using them separately. Complementary to finetuning—can be done without GPUs.

**Use cases**:
- Improve performance by combining models good at different subtasks
- Reduce memory by merging task-specific adapters into one model
- Multi-task finetuning without catastrophic forgetting (finetune tasks in parallel, then merge)
- On-device deployment (one multi-task model instead of several)
- Federated learning (merge device-specific model copies)
- Model upscaling (create larger models from smaller ones)

**Three main approaches**:

1. **Summing**
   - *Linear combination*: weighted average of parameters. Most effective for models finetuned on same base. Enables Task Arithmetic—add task vectors to combine capabilities, subtract to remove behaviors
   - *SLERP*: spherical interpolation between two models on a hypersphere surface. Interpolation factor 0–1 controls contribution balance. Only merges two models at a time
   - *Pruning before merging* (TIES, DARE): reset redundant task-vector parameters (top 20% often sufficient) to reduce interference between merged tasks

2. **Layer stacking (frankenmerging)**: take layers from different models and stack them. Creates novel architectures. Goliath-120B merged two Llama 2-70B models. Can create MoE models via sparse upcycling. Enables depthwise scaling for model upscaling (SOLAR 10.7B from 7B)

3. **Concatenation**: concat adapter parameters (e.g., LoRA rank r1 + r2). Not recommended—no memory savings over serving separately

Many top models on Hugging Face's Open LLM Leaderboard are merged models.
