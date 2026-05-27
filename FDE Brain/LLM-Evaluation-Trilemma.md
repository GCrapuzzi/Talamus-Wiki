---
type: framework
status: evergreen
aliases:
  - LLM Evaluation Trilemma
  - Model Selection Trade-offs
  - Quality-Cost-Latency Balance
tags:
  - ai-engineering
  - model-selection
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/081-cost-and-latency.md
    locator: pages 201-202
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When evaluating models, it’s important to balance model quality, latency, and cost.
      - Many companies opt for lower-quality models if they provide better cost and latency.
created: 2026-05-26T21:55:45.820000+00:00
updated: 2026-05-26T21:55:45.820000+00:00
ingestion_run: 8d527d59
---

# LLM Evaluation Trilemma

## Summary

The necessity of balancing model quality, operational latency, and cost when selecting or deploying a foundation model. High performance is useless if the cost or speed makes it impractical.

## Core Idea

Model selection is rarely about maximizing one metric; it requires finding the optimal balance point (the 'sweet spot') where all three constraints are met. Companies often prioritize cost and latency over marginal gains in quality.

## Practical Use

When faced with multiple model options, first define the non-negotiable constraints (e.g., 'Latency must be < 200ms' or 'Cost must be < $15/1M tokens'). Then, evaluate the remaining models against the remaining objectives.

## Related

- [[Pareto-Optimization-for-LLM-Selection|Pareto Optimization for LLM Selection]]
- [[Comprehensive-LLM-Evaluation-Checklist|Comprehensive LLM Evaluation Checklist]]
