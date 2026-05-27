---
type: pattern
status: evergreen
aliases:
  - Position Bias in Feedback Systems
  - Order effect
  - First suggestion bias
tags:
  - ai-engineering
  - design-patterns
  - user-experience
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/177-feedback-limitations.md
    locator: pages 514-515
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The position in which an option is presented to users influences how this option is perceived.
      - When designing your feedback system, this bias can be mitigated by randomly varying the positions of your suggestions or by building a model to compute a suggestion’s true success rate based on its position.
created: 2026-05-26T21:55:46.583739+00:00
updated: 2026-05-26T21:55:46.583739+00:00
ingestion_run: 8d527d59
---

# Position Bias in Feedback Systems

## Summary

The tendency for users to favor or click on the option presented first, regardless of its actual quality or relevance.

## Core Idea

The mere placement of a suggestion significantly influences its perceived value. Relying solely on the order of presentation can lead to skewed data and poor decision-making.

## Practical Use

When designing A/B tests or comparative evaluation interfaces, mitigate position bias by randomly varying the order of suggestions. Alternatively, build a model that explicitly accounts for the suggestion's position to compute its true success rate.

## Related

- [[User-Feedback-Biases|User Feedback Biases]]
- A/B Testing Design
