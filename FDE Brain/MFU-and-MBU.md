---
type: concept
tags: [inference, hardware, utilization, MFU, MBU, metrics]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-performance-metrics
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# MFU and MBU

Utilization metrics that measure how efficiently hardware is actually used, as opposed to nvidia-smi's GPU utilization (which only tracks % time the GPU is busy, not how efficiently).

- **MFU (Model FLOP/s Utilization)**: ratio of observed throughput to theoretical maximum throughput at peak FLOP/s. Term introduced in the PaLM paper (Chowdhery et al., 2022). Training MFU > 50% is considered good.
- **MBU (Model Bandwidth Utilization)**: percentage of achievable memory bandwidth used.
  - Formula: `(parameter_count × bytes_per_param × tokens_per_sec) / theoretical_bandwidth`
  - Example: 7B params × 2 bytes (FP16) × 100 tokens/s = 700 GB/s; on A100 (2 TB/s) → MBU = 35%.

Compute-bound workloads → higher MFU, lower MBU. Bandwidth-bound workloads → lower MFU, higher MBU. MBU decreases as concurrent users increase (workload shifts toward compute-bound).

The goal is faster and cheaper jobs, not higher utilization numbers per se.
