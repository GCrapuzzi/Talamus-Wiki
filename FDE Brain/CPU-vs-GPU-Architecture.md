---
type: concept
status: evergreen
aliases:
  - CPU vs GPU Architecture
  - General Purpose vs Parallel Processing
  - Core Design Comparison
tags:
  - ai-engineering
  - architecture
  - parallel-computing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
    locator: pages 443-449
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - CPUs are designed for general-purpose usage, whereas GPUs are designed for parallel processing.
      - CPUs... excel at tasks requiring high single-thread performance, such as running an operating system, managing I/O (input/output), or handling complex, sequential processes.
      - GPUs... optimized for tasks that can be broken down into many smaller, independent calculations, such as graphics rendering and machine learning.
created: 2026-05-26T21:55:46.460113+00:00
updated: 2026-05-26T21:55:46.460113+00:00
ingestion_run: 8d527d59
---

# CPU vs GPU Architecture

## Summary

CPUs are designed for general-purpose usage, excelling at sequential, complex, or I/O-heavy tasks using a few powerful cores. GPUs are designed for massive parallel processing, utilizing thousands of smaller cores optimized for highly parallelizable tasks like matrix multiplication.

## Core Idea

The fundamental difference lies in core design: CPUs prioritize high single-thread performance and sequential logic, while GPUs prioritize massive parallelism, making them ideal for workloads like deep learning where operations can be broken down into many independent calculations.

## Practical Use

Determine if the core computational bottleneck is sequential (favoring CPU) or highly parallel (favoring GPU/accelerator). For ML workloads, assume the need for parallel processing and investigate GPU or specialized accelerators.

## Related

- [[AI-Accelerator-Selection-Framework|AI Accelerator Selection Framework]]
- Matrix Multiplication (MatMul)
