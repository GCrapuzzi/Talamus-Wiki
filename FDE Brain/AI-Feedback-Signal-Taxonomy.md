---
type: glossary
status: evergreen
aliases:
  - AI Feedback Signal Taxonomy
  - AI user signals
  - AI interaction metrics
tags:
  - ai-engineering
  - product-design
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
    locator: pages 504-513
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Conversation length can be a positive signal (AI companions) or a negative signal (productivity chatbots).
      - Dialogue diversity (distinct token/topic count) helps detect looping or stagnation.
      - Implicit feedback is abundant but noisier; explicit feedback is clearer but sparse.
created: 2026-05-26T21:55:46.573671+00:00
updated: 2026-05-26T21:55:46.573671+00:00
ingestion_run: 8d527d59
---

# AI Feedback Signal Taxonomy

## Summary

A classification of measurable user interactions used to gauge model performance and user satisfaction, ranging from explicit input to behavioral metrics.

## Core Idea

Relying on a single feedback source is insufficient. Combining multiple signal types (e.g., conversation length, explicit ratings, behavioral patterns) provides a richer, more robust understanding of user intent and model quality.

## Practical Use

When designing an AI product, map out all potential signals: (1) Explicit (thumbs up/down, ratings); (2) Implicit/Behavioral (rephrasing, sharing, time spent); and (3) Conversational Metrics (turn count, topic diversity). Determine which signals are most reliable for the specific application domain (e.g., high diversity for creative tools, low turn count for productivity bots).

## Related

- Implicit Feedback Collection
- [[Comparative-Preference-Signals|Comparative Preference Signals]]
