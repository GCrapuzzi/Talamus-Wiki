---
type: method
tags: [LoRA, PEFT, low-rank-factorization, finetuning, adapters]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#parameter-efficient-finetuning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# LoRA

**Low-Rank Adaptation** (Hu et al., 2021) — the dominant PEFT technique. Decomposes weight updates into low-rank matrices that merge back into original weights with zero inference latency overhead.

**Mechanism**:
1. For weight matrix `W` (n × m), construct `A` (n × r) and `B` (r × m) where r is the LoRA rank
2. New weight: `W' = W + (α/r) × A·B`
3. During finetuning, only `A` and `B` are updated; `W` is frozen

**Why it works**: Pre-trained LLMs have very low intrinsic dimensions. Pre-training acts as a compression framework—the better trained a model is, the easier it is to finetune with few parameters. GPT-3 achieved full-finetuning-comparable performance with ~4.7M trainable params (0.0027% of total).

**Configuration guidelines**:
- **Which matrices**: apply to all four attention matrices (Wq, Wk, Wv, Wo) at lower rank rather than fewer matrices at higher rank. Adding feedforward layers can help further
- **Rank**: r = 4–64 usually sufficient. Higher r doesn't reliably improve performance and may overfit. Some cases need r = 256
- **Alpha (α)**: ratio α:r typically 1:8 to 8:1; experiment to find optimal (r, α)

**Serving modes**:
1. **Merged**: combine A, B into W' before serving → no latency overhead, best for single model
2. **Separate**: keep W, A, B apart → enables multi-LoRA serving (share one base W across 100 customer-specific adapters). Dramatically reduces storage (23.3M vs 1.68B params for 100 models)

LoRA adapters are modular and shareable (Hugging Face, AdapterHub). Apple used multiple LoRA adapters on one 3B base model for different iPhone features.
