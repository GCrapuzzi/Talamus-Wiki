---
type: concept
tags: [inference, attention, KV-cache, memory-optimization, transformer]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# KV Cache

Cache storing key and value vectors from previous tokens to avoid recomputation during autoregressive decoding. Used only during inference (training processes all tokens at once).

### Size formula
`2 × B × S × L × H × M`
- B = batch size, S = sequence length, L = transformer layers, H = model dimension, M = bytes per value

Example: Llama 2 13B (40 layers, dim 5120), batch 32, seq 2048, FP16 → **54 GB**. For 500B+ models the KV cache can reach 3 TB — 3× the model weights.

### Why it matters
- Attention computation grows O(n²) with sequence length; KV cache grows linearly but still dominates memory.
- KV cache size is the primary bottleneck for long-context serving and large batch sizes.
- Character.AI reduced KV cache >20× using multi-query attention + local/global attention interleaving + cross-layer attention, removing memory as their batch-size bottleneck.

### Optimization approaches
1. **Redesign attention**: local windowed attention, multi-query/grouped-query attention, cross-layer attention (training-time changes).
2. **Cache management**: PagedAttention (vLLM), KV cache quantization, adaptive compression, selective caching.
3. **Attention kernels**: FlashAttention — fuses attention operators for hardware-efficient computation.
