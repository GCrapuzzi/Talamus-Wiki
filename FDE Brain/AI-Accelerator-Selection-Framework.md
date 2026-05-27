---
type: framework
status: evergreen
aliases:
  - AI Accelerator Selection Framework
  - Hardware Selection Guide
  - Compute Platform Evaluation
tags:
  - ai-engineering
  - hardware-acceleration
  - deployment-strategy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
    locator: pages 443-449
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The main characteristics that matter across use cases are computational capabilities, memory size and bandwidth, and power consumption.
      - Training usually emphasizes throughput, whereas inference aims to minimize latency.
      - Chips designed for inference are often optimized for lower precision and faster memory access, rather than large memory capacity.
created: 2026-05-26T21:55:46.458730+00:00
updated: 2026-05-26T21:55:46.458730+00:00
ingestion_run: 8d527d59
---

# AI Accelerator Selection Framework

## Summary

A structured approach for selecting the optimal hardware (CPU, GPU, specialized accelerator) based on the workload's primary phase (training vs. inference), required performance metrics, and deployment environment (data center vs. edge).

## Core Idea

The optimal hardware choice is not based solely on peak computational power (FLOP/s) but requires balancing computational capabilities, memory bandwidth, power consumption, and the specific optimization goals of the workload (latency vs. throughput).

## Practical Use

When designing an AI system, first classify the workload: Is it primarily training (high memory, throughput focus) or inference (low latency, efficiency focus)? Then, evaluate candidate hardware against the required metrics (e.g., if low latency is critical for edge deployment, prioritize accelerators with fast memory access over raw compute power).

## Related

- [[Inference-Optimization|Inference Optimization]]
- [[Computational-Capabilities-Metrics|Computational Capabilities Metrics]]
- [[CPU-vs-GPU-Architecture|CPU vs GPU Architecture]]
