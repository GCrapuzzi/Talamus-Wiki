---
type: method
status: evergreen
aliases:
  - Evaluation Criteria Definition
  - Metric Definition
  - Domain Capability Measurement
tags:
  - ai-engineering
  - metrics
  - llm-evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/076-chapter-4.-evaluate-ai-systems.md
    locator: pages 183-183
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - How is factual consistency detected?
      - How are domain-specific capabilities like math, science, reasoning, and summarization measured?
created: 2026-05-26T21:55:45.785659+00:00
updated: 2026-05-26T21:55:45.785659+00:00
ingestion_run: 8d527d59
---

# Evaluation Criteria Definition

## Summary

The systematic process of identifying, defining, and calculating quantitative and qualitative metrics that measure specific domain capabilities (e.g., factual consistency, reasoning, summarization) relevant to the application's goals.

## Core Idea

Evaluation criteria must move beyond simple accuracy scores. They must address specific failure modes and domain requirements, such as detecting factual inconsistencies or measuring complex reasoning chains.

## Practical Use

For a financial application, do not just measure 'coherence.' Define criteria like 'Regulatory Compliance Score' or 'Numerical Accuracy on Financial Statements.' Use human-in-the-loop validation to ground these metrics.

## Related

- [[Contextual-AI-Evaluation|Contextual AI Evaluation]]
