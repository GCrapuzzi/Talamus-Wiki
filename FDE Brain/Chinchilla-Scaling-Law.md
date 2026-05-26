---
type: framework
tags: [scaling-law, chinchilla, compute-optimal, training, FLOPs]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-size
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Chinchilla Scaling Law

Rule for computing the optimal model size and dataset size given a fixed compute budget (DeepMind, 2022). Derived from training 400 models (70M–16B params) on 5–500B tokens.

**Core finding**: for compute-optimal training, the number of training tokens should be ~20x the model size. A 3B-param model needs ~60B training tokens. Model size and token count should scale equally: doubling model size → double the training tokens.

**Three numbers signal a model's scale:**
1. **Number of parameters** — proxy for learning capacity
2. **Number of training tokens** — proxy for how much the model learned
3. **Number of FLOPs** — proxy for training cost

**Practical note**: Chinchilla optimizes for model quality, not usability. Llama intentionally chose smaller-than-optimal models because they're easier to deploy and cheaper to run inference on. Sardana et al. (2023) modified the scaling law to account for inference demand.

**Cost context**: at $2/hr per H100, 256 GPUs at 70% utilization, training GPT-3-175B costs ~$4.1M over ~236 days.

Limitations: developed for dense models on human-generated data. Adapting for MoE and synthetic data is open research.

See also: [[Mixture of Experts]], [[Inverse Scaling]].
