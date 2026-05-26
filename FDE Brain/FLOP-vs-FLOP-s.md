---
type: glossary
tags: [FLOPs, compute, hardware, GPU, training-cost]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#model-size
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# FLOP vs FLOP/s

Two commonly confused compute metrics:

- **FLOP** (floating point operation): a single arithmetic operation on floating-point numbers
- **FLOPs** (plural): total count of floating point operations for a task. Measures **compute requirement**. E.g., GPT-3-175B training: 3.14 × 10²³ FLOPs
- **FLOP/s** (per second): a machine's peak throughput. Measures **hardware performance**. E.g., H100 NVL: 60 TeraFLOP/s (FP32)

OpenAI uses **FLOP/s-day** (= 86,400 FLOPs) to avoid notation confusion.

**Utilization**: fraction of peak FLOP/s actually achieved. 50% is acceptable; 70%+ is great.

**Example calculation**: 256 H100s at peak capacity → GPT-3-175B training takes ~236 days. At 70% utilization and $2/hr per H100, cost ≈ $4.1M.
