---
type: operational-playbook
status: evergreen
aliases:
  - Comprehensive LLM Evaluation Checklist
  - Model Selection Criteria
  - LLM Benchmarking Metrics
tags:
  - ai-engineering
  - playbook
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/081-cost-and-latency.md
    locator: pages 201-202
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Table 4-3 shows criteria you might use to evaluate models for your application.
      - "Criteria: Cost, Scale, Latency, Overall model quality."
created: 2026-05-26T21:55:45.824979+00:00
updated: 2026-05-26T21:55:45.824979+00:00
ingestion_run: 8d527d59
---

# Comprehensive LLM Evaluation Checklist

## Summary

A structured checklist for evaluating foundation models across five critical dimensions: Cost, Scale, Latency, Quality, and Operational Constraints.

## Core Idea

Model evaluation must be systematic. The checklist forces the engineer to define quantitative benchmarks (Hard Requirement vs. Ideal) for every metric, preventing subjective decision-making.

## Practical Use

Use this checklist as a mandatory step in the MLOps pipeline. For example, when evaluating a model, record the P90 latency for both 'Time to first token' and 'Time per total query' using the specific internal user prompt dataset.

## Related

- [[LLM-Evaluation-Trilemma|LLM Evaluation Trilemma]]
- [[LLM-Latency-Metrics|LLM Latency Metrics]]
