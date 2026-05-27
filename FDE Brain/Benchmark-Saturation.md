---
type: concept
status: evergreen
aliases:
  - Benchmark Saturation
  - Evaluation Benchmark Decay
  - Benchmark Obsolescence
tags:
  - ai-engineering
  - evaluation
  - ml-benchmarking
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/056-challenges-of-evaluating-foundation-models.md
    locator: pages 138-141
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A benchmark becomes saturated for a model once the model achieves the perfect score.
      - The benchmark GLUE (General Language Understanding Evaluation) came out in 2018 and became saturated in just a year, necessitating the introduction of Super-GLUE in 2019.
created: 2026-05-26T21:55:45.642187+00:00
updated: 2026-05-26T21:55:45.642187+00:00
ingestion_run: 8d527d59
---

# Benchmark Saturation

## Summary

The phenomenon where a standardized evaluation benchmark (e.g., GLUE, MMLU) becomes insufficient or too easy for advanced Foundation Models, requiring the rapid development of successor benchmarks.

## Core Idea

As AI models improve, they quickly achieve perfect or near-perfect scores on existing benchmarks. This saturation means the benchmark no longer measures the model's true potential or weakness, necessitating the creation of more complex, specialized, or 'Super' versions of the test.

## Practical Use

When selecting or designing evaluation tests, assume that existing, general-purpose benchmarks will become saturated. Focus on creating domain-specific, multi-step reasoning benchmarks that require deep knowledge or complex task chaining to prevent the model from simply memorizing the test answers.

## Related

- [[Open-Ended-Evaluation-Framework|Open-Ended Evaluation Framework]]
- Super-Benchmark Design
