---
type: glossary
status: evergreen
aliases:
  - Utilization Metrics (MFU/MBU)
  - Resource efficiency
tags:
  - ai-engineering
  - resource-management
  - cost-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
    locator: pages 436-442
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Utilization metrics measure how efficiently a resource is being used.
created: 2026-05-26T21:55:46.456816+00:00
updated: 2026-05-26T21:55:46.456816+00:00
ingestion_run: 8d527d59
---

# Utilization Metrics (MFU/MBU)

## Summary

Metrics quantifying how efficiently computational resources (e.g., GPU cores) are being used. (Specific acronyms like MFU/MBU are mentioned but the concept is general utilization).

## Core Idea

High utilization indicates efficient resource use, which is critical for cost management. Monitoring this helps determine if the bottleneck is compute capacity or algorithmic efficiency.

## Practical Use

If utilization is low, investigate batching strategies or model quantization to increase the workload density on the hardware. If utilization is high, scaling up resources may be necessary.

## Related

- [[Throughput-Optimization|Throughput Optimization]]
