---
type: operation
status: evergreen
aliases:
  - Degenerate Feedback Loop
  - Exposure bias
  - Popularity bias
  - Filter bubble effect
tags:
  - ai-engineering
  - system-design
  - feedback-loops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/177-feedback-limitations.md
    locator: pages 514-515
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A degenerate feedback loop can happen when the predictions themselves influence the feedback, which, in turn, influences the next iteration of the model, amplifying initial biases.
      - This issue is known as “exposure bias,” “popularity bias,” or “filter bubbles,” and it’s a well-studied problem.
created: 2026-05-26T21:55:46.586201+00:00
updated: 2026-05-26T21:55:46.586201+00:00
ingestion_run: 8d527d59
---

# Degenerate Feedback Loop

## Summary

A systemic issue where a model's predictions influence the feedback data it receives, which in turn amplifies the initial biases, leading to a self-reinforcing, non-representative state.

## Core Idea

The system only receives feedback on what it shows. If the model boosts certain items (A) because they were initially slightly better, those items receive more exposure and more clicks, making the system believe they are overwhelmingly superior, even if the initial difference was minor.

## Practical Use

In recommendation systems, actively monitor for this loop. Implement techniques like 'serendipity injection' or 'exploration quotas' to ensure that less popular or novel content receives sufficient exposure, preventing the system from becoming trapped in a narrow, popular subset of data.

## Related

- Exposure bias
- Recommendation Systems
- AI Bias Mitigation
