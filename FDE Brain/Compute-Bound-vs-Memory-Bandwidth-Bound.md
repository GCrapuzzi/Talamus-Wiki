---
type: concept
tags: [inference, optimization, hardware, roofline-model]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-overview
  - AI Space/normalized/pdf/ai-engineering.md#chapter-9-inference-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Compute-Bound vs Memory Bandwidth-Bound

Two fundamental computational bottlenecks in AI inference, introduced in the Roofline model (Williams et al., 2009).

- **Compute-bound**: time-to-complete determined by arithmetic operations needed. Mitigated by more chips or higher FLOP/s hardware.
- **Memory bandwidth-bound**: constrained by data transfer rate between memory and processors. Mitigated by chips with higher bandwidth.

Classified by **arithmetic intensity** = arithmetic operations per byte of memory access. Profiling tools (e.g., NVIDIA Nsight) render roofline charts to visualize which regime a workload falls in.

For transformer LLMs:
- **Prefill** is compute-bound (parallel input token processing, limited by hardware FLOP/s)
- **Decode** is memory bandwidth-bound (sequential token generation, limited by weight-loading speed)

Most current AI workloads are memory bandwidth-bound due to transformer prevalence and accelerator limitations. Image generators like Stable Diffusion are a notable exception (compute-bound).
