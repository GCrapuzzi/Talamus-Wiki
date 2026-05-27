---
type: concept
status: evergreen
aliases:
  - Observability vs. Monitoring
  - System Observability
  - AI System Observability
tags:
  - observability
  - ai-engineering
  - system-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/172-monitoring-and-observability.md
    locator: pages 489-495
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Monitoring makes no assumption about the relationship between the internal state of a system and its outputs.
      - "Observability... makes an assumption stronger than traditional monitoring: that a system’s internal states can be inferred from knowledge of its external outputs."
created: 2026-05-26T21:55:46.544902+00:00
updated: 2026-05-26T21:55:46.544902+00:00
ingestion_run: 8d527d59
---

# Observability vs. Monitoring

## Summary

Monitoring tracks external outputs to detect failures, while Observability assumes that internal system states can be inferred from knowledge of external outputs (logs and metrics) without deploying new code.

## Core Idea

Observability represents a stronger assumption than traditional monitoring: that sufficient information about a system's runtime is collected and analyzed such that when something goes wrong, the root cause can be figured out by examining logs and metrics. It is about instrumentation, not just tracking.

## Practical Use

When designing an AI application, prioritize deep instrumentation (observability) over simple output tracking (monitoring). Ensure that logs and metrics capture enough context (e.g., model parameters, full prompts, intermediate steps) to diagnose failures without requiring code changes.

## Related

- [[AI-Monitoring-Playbook|AI Monitoring Playbook]]
- [[AI-Engineering-Architecture|AI Engineering Architecture]]
