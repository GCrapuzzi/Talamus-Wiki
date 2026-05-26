---
type: method
tags: [inference, kernels, optimization, FlashAttention, compiler, CUDA]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Kernel Optimization Techniques

Kernels are specialized code optimized for specific accelerators. Four core techniques for speeding up computation:

1. **Vectorization**: process multiple contiguous data elements simultaneously instead of one at a time; reduces data I/O latency.
2. **Parallelization**: divide arrays into independent chunks processed on different cores/threads.
3. **Loop tiling**: reorder data access patterns to match hardware memory layout and cache structure. Hardware-dependent — CPU-optimal tiling may not work on GPUs.
4. **Operator fusion**: combine multiple operators into a single pass to avoid redundant memory reads/writes. Requires understanding of model-specific operators. FlashAttention is a prominent example — fuses several attention operators.

Kernels are hardware-architecture-specific (e.g., FlashAttention for A100, FlashAttention-3 for H100). A **compiler** lowers model code to hardware-compatible instructions, substituting specialized kernels where possible. Examples: `torch.compile`, XLA/OpenXLA, TensorRT, Apache TVM, MLIR.

### PyTorch case study (Llama-7B on A100-80GB)
Cumulative throughput gains: torch.compile → INT8 quantization → INT4 quantization → speculative decoding.
