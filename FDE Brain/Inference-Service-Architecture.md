---
type: pattern
status: evergreen
aliases:
  - Inference Service Architecture
  - AI Inference Pipeline
  - Model Serving Stack
tags:
  - ai-engineering
  - mlops
  - inference
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
    locator: pages 430-435
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In production, the component that runs model inference is called an inference server.
      - It hosts the available models and has access to the necessary hardware.
      - An inference server is part of a broader inference service, which is also responsible for receiving, routing, and possibly preprocessing requests.
created: 2026-05-26T21:55:46.437145+00:00
updated: 2026-05-26T21:55:46.437145+00:00
ingestion_run: 8d527d59
---

# Inference Service Architecture

## Summary

A structured system for running models in production, comprising an Inference Service layer and an Inference Server layer.

## Core Idea

The Inference Service handles request management (receiving, routing, preprocessing), while the Inference Server is the dedicated component that hosts the models and executes the actual forward pass computation. This separation allows for scalable, modular optimization.

## Practical Use

When designing a production ML endpoint, define the boundaries: the service layer handles API gateway logic, authentication, and request queuing; the server layer focuses purely on optimized computation (e.g., using Triton or TorchServe).

## Related

- [[Computational-Bottlenecks|Computational Bottlenecks]]
- [[Online-vs.-Batch-Inference|Online vs. Batch Inference]]
