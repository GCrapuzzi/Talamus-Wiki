---
type: pattern
status: evergreen
aliases:
  - AI Feature Interaction Model
  - AI System Design Taxonomy
  - AI Feature Classification
tags:
  - ai-engineering
  - system-design
  - ux-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/029-use-case-evaluation.md
    locator: pages 53-55
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If an app can still work without AI, AI is complementary to the app.
      - A reactive feature shows its responses in reaction to users’ requests or specific actions, whereas a proactive feature shows its responses when there’s an opportunity for it.
      - Dynamic features are updated continually with user feedback, whereas static features are updated periodically.
created: 2026-05-26T21:55:45.445717+00:00
updated: 2026-05-26T21:55:45.445717+00:00
ingestion_run: 8d527d59
---

# AI Feature Interaction Model

## Summary

A set of dimensions (Criticality, Timing, Update Frequency) used to classify how an AI component interacts with a core application function, guiding reliability and UX requirements.

## Core Idea

The role of AI determines the engineering requirements. Critical AI demands high reliability; Proactive AI demands high quality to avoid user annoyance; Dynamic AI requires continuous data pipelines.

## Practical Use

When designing an AI feature, classify it along these axes: 1. Is it Critical or Complementary? 2. Is it Reactive or Proactive? 3. Is it Dynamic or Static? This dictates the required latency, error tolerance, and update mechanism.

## Related

- [[Human-in-the-Loop-HITL|Human-in-the-Loop (HITL)]]
