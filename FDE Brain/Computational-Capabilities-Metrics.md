---
type: glossary
status: evergreen
aliases:
  - Computational Capabilities Metrics
  - FLOP/s
  - Peak Performance Measurement
tags:
  - ai-engineering
  - performance-metrics
  - benchmarking
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
    locator: pages 443-449
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The most common metric is FLOP/s, often written as FLOPS, which measures the peak number of floating-point operations per second.
      - The ratio between the actual FLOP/s and the theoretical FLOP/s is one utilization metric.
      - The number of operations a chip can perform in a second depends on the numerical precision—the higher the precision, the fewer operations the chip can execute.
created: 2026-05-26T21:55:46.463065+00:00
updated: 2026-05-26T21:55:46.463065+00:00
ingestion_run: 8d527d59
---

# Computational Capabilities Metrics

## Summary

Metrics used to quantify a chip's processing power. Key metrics include FLOP/s (Floating-Point Operations Per Second), which measures peak performance, and the utilization ratio (Actual FLOP/s / Theoretical FLOP/s), which measures real-world efficiency.

## Core Idea

Peak FLOP/s is a theoretical maximum and rarely achievable. Engineers must track the utilization ratio to understand the true efficiency of an application on a given chip. Furthermore, the required numerical precision (e.g., FP8, BF16) significantly impacts the achievable FLOP/s.

## Practical Use

When benchmarking hardware, do not rely solely on advertised peak FLOP/s. Instead, measure the utilization ratio under representative workloads and select data types (e.g., BF16 or FP8) that maximize the achievable operations per second for the target hardware.

## Related

- Numerical Precision Formats
- [[AI-Accelerator-Selection-Framework|AI Accelerator Selection Framework]]
