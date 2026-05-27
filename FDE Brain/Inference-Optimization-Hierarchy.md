---
type: framework
status: evergreen
aliases:
  - Inference Optimization Hierarchy
  - AI Model Optimization Levels
  - Model-Hardware-Service Optimization
tags:
  - ai-engineering
  - deployment
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
    locator: pages 450-463
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Inference optimization can be done at the model, hardware, or service level.
      - Model-level optimization is like crafting better arrows.
      - Hardware-level optimization is like training a stronger and better archer.
      - Service-level optimization is like refining the entire shooting process.
created: 2026-05-26T21:55:46.470919+00:00
updated: 2026-05-26T21:55:46.470919+00:00
ingestion_run: 8d527d59
---

# Inference Optimization Hierarchy

## Summary

A structured approach to optimizing AI model deployment by considering three distinct layers: Model, Hardware, and Service. Optimization efforts should ideally span multiple levels for maximum efficiency.

## Core Idea

Optimization is not monolithic. By segmenting the problem into Model (algorithmic changes), Hardware (physical compute improvements), and Service (system/pipeline refinement), engineers can systematically identify bottlenecks and apply targeted solutions. This prevents over-reliance on a single optimization technique.

## Practical Use

When faced with latency or cost issues, first determine if the bottleneck is algorithmic (e.g., model size/architecture), hardware-related (e.g., memory bandwidth), or systemic (e.g., inefficient API calls, batching strategy). For example, if the model is too large, apply Model Optimization (e.g., quantization). If the service is slow, apply Service Optimization (e.g., caching).

## Related

- Model Compression
- [[Speculative-Decoding|Speculative Decoding]]
