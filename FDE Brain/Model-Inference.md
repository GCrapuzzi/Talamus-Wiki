---
type: glossary
status: evergreen
aliases:
  - Model Inference
  - AI Computation
  - Model Execution
tags:
  - ai-engineering
  - mlops
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/032-maintenance.md
    locator: pages 58-58
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model inference, the process of computing an output given an input, is getting faster and cheaper.
created: 2026-05-26T21:55:45.465057+00:00
updated: 2026-05-26T21:55:45.465057+00:00
ingestion_run: 8d527d59
---

# Model Inference

## Summary

The process of computing an output (prediction or text generation) given an input using a trained machine learning model.

## Core Idea

Model inference is the operational phase of an AI application. Its cost, speed, and efficiency are critical metrics for determining the feasibility and scalability of an AI product. The trend shows rapid decreases in both cost and time.

## Practical Use

When selecting a model or architecture, evaluate the inference cost (e.g., cost per token) and latency (speed) against the required performance benchmark. Optimize the deployment environment (e.g., quantization, specialized hardware) to minimize inference overhead.

## Related

- [[Foundation-Model|Foundation Model]]
- LLM Cost Optimization
