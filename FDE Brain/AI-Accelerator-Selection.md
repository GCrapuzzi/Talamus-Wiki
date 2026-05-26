---
type: framework
tags: [hardware, GPU, TPU, accelerators, cost-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-accelerators
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Accelerator Selection

Three questions when evaluating accelerator hardware:
1. **Can it run your workload?** — memory capacity must fit model + KV cache.
2. **How fast?** — FLOP/s for compute-bound work; bandwidth for memory-bound work.
3. **How much does it cost?** — cloud pricing (usage-based) or purchase price + ongoing power.

### Key specs
- **FLOP/s**: peak floating-point ops/sec; precision-dependent (FP8 > FP16 > TF32). NVIDIA H100 SXM: 3,958 teraFLOP/s at FP8.
- **Memory size**: HBM capacity (24–80 GB consumer GPU).
- **Memory bandwidth**: HBM transfer speed (256 GB/s – 1.5+ TB/s).
- **Power / TDP**: H100 ≈ 7,000 kWh/year at peak (vs ~10,000 kWh avg US household).

### Landscape
- **Training + inference**: NVIDIA GPUs, AMD GPUs, Google TPU, Intel Gaudi
- **Inference-specialized**: Apple Neural Engine, AWS Inferentia, Meta MTIA, edge chips (Google Edge TPU, NVIDIA Jetson)
- **Architecture-specialized**: chips optimized for transformers, using tensor compute primitives over vector/scalar

Match workload profile to hardware: compute-bound → more FLOP/s; bandwidth-bound → more bandwidth + memory.
