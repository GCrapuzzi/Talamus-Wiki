---
type: pattern
status: evergreen
aliases:
  - Pareto Optimization for LLM Selection
  - Multi-objective Optimization
  - Constraint-First Model Selection
tags:
  - ai-engineering
  - decision-framework
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/081-cost-and-latency.md
    locator: pages 201-202
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Optimizing for multiple objectives is an active field of study called Pareto optimization.
      - If latency is something you can’t compromise on, you start with latency expectations for different models, filter out all the models that don’t meet your latency requirements, and then pick the best among the rest.
created: 2026-05-26T21:55:45.821479+00:00
updated: 2026-05-26T21:55:45.821479+00:00
ingestion_run: 8d527d59
---

# Pareto Optimization for LLM Selection

## Summary

A decision-making pattern used when optimizing for multiple, potentially conflicting objectives (e.g., minimizing cost while maximizing quality). It requires identifying which objectives are absolute 'must-haves' (hard constraints).

## Core Idea

Instead of trying to improve all metrics simultaneously, the process involves setting hard boundaries (e.g., 'Latency cannot exceed 100ms'). This filters the candidate pool, allowing the engineer to then select the best model among the remaining, viable options.

## Practical Use

If the application requires real-time user interaction, latency is a hard constraint. Start by filtering out all models that fail the latency test, regardless of their quality score, before comparing the remaining models on cost.

## Related

- [[LLM-Evaluation-Trilemma|LLM Evaluation Trilemma]]
- [[Comprehensive-LLM-Evaluation-Checklist|Comprehensive LLM Evaluation Checklist]]
