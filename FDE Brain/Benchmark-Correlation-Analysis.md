---
type: concept
status: evergreen
aliases:
  - Benchmark Correlation Analysis
  - Benchmark Redundancy Check
  - Pearson Correlation in LLMs
tags:
  - ai-engineering
  - statistics
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/085-navigate-public-benchmarks.md
    locator: pages 215-223
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If two benchmarks are perfectly correlated, you don’t want both of them.
      - Strongly correlated benchmarks can exaggerate biases.
created: 2026-05-26T21:55:45.847437+00:00
updated: 2026-05-26T21:55:45.847437+00:00
ingestion_run: 8d527d59
---

# Benchmark Correlation Analysis

## Summary

The statistical analysis of the relationship between two or more benchmarks. High correlation (e.g., Pearson score close to 1) indicates that the benchmarks measure the same underlying capability, suggesting redundancy.

## Core Idea

Strongly correlated benchmarks do not provide independent information and can exaggerate biases in model ranking. If two benchmarks test the same skill, including both is unnecessary and potentially misleading.

## Practical Use

Before finalizing an evaluation suite, calculate the correlation matrix for all candidate benchmarks. If a high correlation is found, select only one representative benchmark from the correlated group to maintain diversity and prevent bias.

## Related

- [[Benchmark-Selection-and-Aggregation-Playbook|Benchmark Selection and Aggregation Playbook]]
