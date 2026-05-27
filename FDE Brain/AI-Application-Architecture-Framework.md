---
type: framework
status: evergreen
aliases:
  - AI Application Architecture Framework
  - Modular AI System Design
  - Component Separation in LLM Apps
tags:
  - ai-engineering
  - system-design
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/178-summary.md
    locator: pages 516-518
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - this high-level architecture provides a framework for understanding how different components fit together.
      - While it’s necessary to separate components to keep your system modular and maintainable, this separation is fluid.
created: 2026-05-26T21:55:46.592953+00:00
updated: 2026-05-26T21:55:46.592953+00:00
ingestion_run: 8d527d59
---

# AI Application Architecture Framework

## Summary

A high-level, modular framework for building AI applications, emphasizing the separation of components (e.g., inference service, model gateway, standalone guardrails) while acknowledging their functional overlap.

## Core Idea

While modularity is essential for maintainability and capability enhancement, it increases system complexity and exposes the system to new failure modes. Understanding component interaction is critical for robust design.

## Practical Use

Use this framework to map out system components. When designing guardrails, determine if they belong in the inference service (runtime check), the model gateway (API layer check), or as a standalone component (pre-processing/post-processing).

## Related

- Observability in AI
- Guardrails
