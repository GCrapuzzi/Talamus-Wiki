---
type: concept
tags: [hardware, GPU, memory-hierarchy, HBM, SRAM, CUDA]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-accelerators
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# GPU Memory Hierarchy

Three-level memory hierarchy for AI accelerators, each trading capacity for bandwidth:

| Level | Type | Bandwidth | Typical size |
|---|---|---|---|
| CPU memory (DRAM) | DDR SDRAM (2D) | 25–50 GB/s | 16 GB – 1+ TB |
| GPU HBM | HBM (3D stacked) | 256 GB/s – 1.5+ TB/s | 24–80 GB |
| GPU on-chip SRAM | L1/L2 cache, registers | 10+ TB/s | ≤ 40 MB |

GPU memory uses HBM (high-bandwidth memory) with 3D stacking, making it significantly more expensive than CPU DDR. Much of GPU optimization focuses on exploiting this hierarchy — keeping data in faster tiers and minimizing transfers.

Popular frameworks (PyTorch, TensorFlow) don't yet offer fine-grained memory-tier control, driving interest in GPU programming languages: **CUDA** (NVIDIA, proprietary), **Triton** (OpenAI, for custom kernels), **ROCm** (AMD, open source).
