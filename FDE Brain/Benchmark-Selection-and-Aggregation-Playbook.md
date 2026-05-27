---
type: pattern
status: evergreen
aliases:
  - Benchmark Selection and Aggregation Playbook
  - Leaderboard Design Principles
  - Model Ranking Strategy
tags:
  - ai-engineering
  - evaluation
  - mlops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/085-navigate-public-benchmarks.md
    locator: pages 215-223
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Leaderboards must balance coverage and the number of benchmarks.
      - The selection process must consider computational constraints (e.g., excluding expensive benchmarks like MS MARCO).
      - The goal is to cover a wide range of capabilities (reasoning, factual consistency, domain-specific tasks).
created: 2026-05-26T21:55:45.845260+00:00
updated: 2026-05-26T21:55:45.845260+00:00
ingestion_run: 8d527d59
---

# Benchmark Selection and Aggregation Playbook

## Summary

A systematic approach to selecting and combining multiple public benchmarks to create a representative model leaderboard, addressing issues of coverage, correlation, and computational cost.

## Core Idea

A single benchmark is insufficient. Effective model comparison requires aggregating results from a diverse set of benchmarks that cover multiple capabilities (e.g., reasoning, factual consistency, domain-specific knowledge) while mitigating the risk of redundant or biased measurements.

## Practical Use

When designing an internal evaluation pipeline or interpreting public leaderboards, systematically ask: 1) What diverse capabilities must be tested? 2) Which benchmarks are computationally feasible? 3) Are the selected benchmarks highly correlated, and if so, which ones should be excluded?

## Related

- [[Benchmark-Correlation-Analysis|Benchmark Correlation Analysis]]
- [[AI-Model-Evaluation-Pipeline|AI Model Evaluation Pipeline]]
