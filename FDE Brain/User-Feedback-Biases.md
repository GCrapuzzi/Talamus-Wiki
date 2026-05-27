---
type: concept
status: evergreen
aliases:
  - User Feedback Biases
  - Cognitive biases in data
  - Feedback limitations
tags:
  - ai-engineering
  - data-bias
  - user-experience
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/177-feedback-limitations.md
    locator: pages 514-515
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - It’s important to inspect your user feedback to uncover its biases. Understanding these biases will help you interpret the feedback correctly, avoiding misleading product decisions.
created: 2026-05-26T21:55:46.587842+00:00
updated: 2026-05-26T21:55:46.587842+00:00
ingestion_run: 8d527d59
---

# User Feedback Biases

## Summary

A collection of cognitive biases that skew user input, requiring careful analysis and mitigation during the data collection and model training phases.

## Core Idea

User feedback is not objective truth. Understanding these biases (e.g., recency, preference, leniency) is crucial for correctly interpreting data and avoiding misleading product decisions.

## Practical Use

Before deploying a feedback mechanism, audit the expected data distribution for known biases. If comparing two items, ensure the comparison is not unduly influenced by the order (Position Bias) or the last item seen (Recency Bias).

## Related

- [[Leniency-Bias-in-Feedback|Leniency Bias in Feedback]]
- [[Position-Bias-in-Feedback-Systems|Position Bias in Feedback Systems]]
- [[Degenerate-Feedback-Loop|Degenerate Feedback Loop]]
