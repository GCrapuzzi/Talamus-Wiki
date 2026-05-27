---
type: concept
status: evergreen
aliases:
  - Memory Bandwidth and Data Movement
  - Data Transfer Bottleneck
  - Memory I/O Constraint
tags:
  - ai-engineering
  - hardware-bottleneck
  - memory-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
    locator: pages 443-449
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - data often needs to be moved from the memory to these cores, and, therefore, data transfer speed is important.
      - These large amounts of data need to be moved quickly to keep the cores efficiently occupied.
      - Therefore, GPU memory needs to have higher bandwidth and lower latency than CPU memory...
created: 2026-05-26T21:55:46.464986+00:00
updated: 2026-05-26T21:55:46.464986+00:00
ingestion_run: 8d527d59
---

# Memory Bandwidth and Data Movement

## Summary

For large AI models, the speed at which data (weights and input data) can be moved from memory to the compute cores (memory bandwidth) is often the primary bottleneck, sometimes more critical than the raw computational power (FLOP/s).

## Core Idea

Because modern AI models involve large weight matrices, keeping the compute cores efficiently occupied requires high-bandwidth, low-latency memory (e.g., GDDR). If data movement is slow, the cores sit idle, regardless of their theoretical FLOP/s.

## Practical Use

When diagnosing performance issues, if the utilization ratio is low, investigate memory bandwidth and latency. Prioritize hardware with advanced memory technologies (like HBM or GDDR) if the model size or batch size is large.

## Related

- [[AI-Accelerator-Selection-Framework|AI Accelerator Selection Framework]]
- [[Computational-Capabilities-Metrics|Computational Capabilities Metrics]]
