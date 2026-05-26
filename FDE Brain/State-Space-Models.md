---
type: concept
tags: [SSM, mamba, jamba, architecture, long-context]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-architecture
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# State Space Models

Alternative architecture to [[Transformer Architecture]], showing promise for long-range sequence modeling. Evolution:

- **SSM** (Gu et al., 2021): foundational state space model architecture
- **S4**: made SSMs more efficient for long sequences
- **H3** ("Hungry Hungry Hippos"): added a recall mechanism akin to attention but more efficient
- **Mamba** (Gu & Dao, 2023): scaled SSMs to 3B params. Inference scales linearly with sequence length (vs. quadratic for transformers). Mamba-3B outperforms same-size transformers and matches 2x-size transformers
- **Jamba** (Lieber et al., 2024): hybrid transformer–Mamba layers. 52B total / 12B active params (MoE), fits in single 80GB GPU, supports 256K context

RWKV is another alternative: RNN-based but parallelizable for training, theoretically no context length limit.

Developing a new architecture that outperforms transformers is hard because transformers have been heavily optimized since 2017 and new architectures must perform at the scale and on the hardware people care about.
