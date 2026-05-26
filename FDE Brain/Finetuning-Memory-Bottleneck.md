---
type: concept
tags: [memory, finetuning, GPU, training, optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#memory-bottlenecks
  - AI Space/normalized/pdf/ai-engineering.md#backpropagation-and-trainable-parameters
  - AI Space/normalized/pdf/ai-engineering.md#memory-math
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Finetuning Memory Bottleneck

Training memory = model weights + activations + gradients + optimizer states.

**Inference memory** (forward pass only):
- Model weights: `N × M` (N = param count, M = bytes per param)
- With activations + KV cache: ~`N × M × 1.2` (20% overhead assumption for typical workloads)
- Example: 13B params × 2 bytes = 26 GB weights → 31.2 GB total

**Training memory** adds per-trainable-parameter overhead:
- Gradient: 1 value per trainable param
- Optimizer states: 0 (SGD), 1 (momentum), or 2 (Adam) values per trainable param
- Adam on all 13B params at 2 bytes: `13B × 3 × 2 = 78 GB` for gradients + optimizer alone
- Adam on only 1B trainable params: `1B × 3 × 2 = 6 GB`

Activation memory can dwarf weight memory and scales with sequence length and batch size. [[Gradient Checkpointing]] trades recomputation time for activation memory savings.

**Key lever**: reducing trainable parameters (motivation for PEFT) or reducing bits per value (motivation for [[Quantization]]).
