---
type: method
status: evergreen
aliases:
  - Model Distillation (Knowledge Distillation)
  - Knowledge Distillation
tags:
  - ai-engineering
  - llm-deployment
  - model-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/149-model-distillation.md
    locator: pages 419-419
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model distillation is a method in which a small model (student) is trained to mimic a larger model (teacher).
      - The goal is to produce smaller models for deployment because deploying a big model can be resource-intensive.
      - Distillation can produce a smaller, faster student model that retains performance comparable to the teacher.
      - Examples include DistilBERT (reducing size by 40% while retaining 97% of capabilities) and Alpaca (finetuning Llama-7B on examples from text-davinci-003).
created: 2026-05-26T21:55:46.386739+00:00
updated: 2026-05-26T21:55:46.386739+00:00
ingestion_run: 8d527d59
---

# Model Distillation (Knowledge Distillation)

## Summary

A technique where a smaller, resource-efficient model (student) is trained to replicate the performance and knowledge of a larger, more complex model (teacher).

## Core Idea

The goal is to transfer the 'knowledge' of a high-performing, resource-intensive model into a compact model suitable for deployment on edge devices or environments with limited computational resources, while retaining most of the original performance.

## Practical Use

When deploying a large LLM (e.g., a 175B parameter model) that is too slow or resource-intensive for production environments, an AI engineer can use distillation to train a smaller student model (e.g., 7B parameters) that mimics the teacher's outputs and capabilities, significantly reducing latency and size (e.g., using techniques like DistilBERT or Alpaca).

## Related

- Model Compression
- [[Quantization|Quantization]]
- Student-Teacher Learning
