---
type: framework
status: evergreen
aliases:
  - Compute-Bound vs. Memory Bandwidth-Bound Workloads
  - Computational Bottleneck Analysis
  - Roofline Analysis
tags:
  - ai-engineering
  - performance-optimization
  - hardware-acceleration
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
    locator: pages 430-435
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Compute-bound refers to tasks whose time-to-complete is determined by the computation needed for the tasks.
      - Memory bandwidth-bound tasks are constrained by the data transfer rate within the system.
      - A compute-bound workload might be sped up by spreading it out to more chips or by leveraging chips with more computational power.
      - A memory bandwidth-bound workload might be sped up by leveraging chips with higher bandwidth.
created: 2026-05-26T21:55:46.438664+00:00
updated: 2026-05-26T21:55:46.438664+00:00
ingestion_run: 8d527d59
---

# Compute-Bound vs. Memory Bandwidth-Bound Workloads

## Summary

A method for classifying computational workloads based on whether their performance is limited by the raw computational power (Compute-bound) or the speed of data movement (Memory Bandwidth-bound).

## Core Idea

Understanding the bottleneck is critical because optimization techniques differ drastically. Compute-bound tasks require more processing units (e.g., higher FLOP/s), while memory bandwidth-bound tasks require faster data transfer rates (e.g., high memory bus speed).

## Practical Use

Use profiling tools (like NVIDIA Nsight) to generate a roofline chart. If the workload falls closer to the computation line, focus on parallelization or specialized compute hardware. If it falls closer to the memory line, focus on data locality, caching, or memory optimization.

## Related

- Roofline Chart
- Memory Bandwidth Optimization
