---
type: concept
status: evergreen
aliases:
  - Probabilistic Output Handling
  - Stochastic Output
  - Confidence Thresholding
tags:
  - ai-engineering
  - risk-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/048-sampling.md
    locator: pages 112-112
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Sampling makes AI’s outputs probabilistic.
      - For a classification model... The model computes the probability of each of these two outcomes.
      - if you decide that any email with a spam probability higher than 50% should be marked as spam, an email with a 90% spam probability will be marked as spam.
created: 2026-05-26T21:55:45.571122+00:00
updated: 2026-05-26T21:55:45.571122+00:00
ingestion_run: 8d527d59
---

# Probabilistic Output Handling

## Summary

Recognizing that LLM outputs are not deterministic but are generated based on computed probabilities for possible outcomes. This requires implementing decision logic based on probability thresholds rather than absolute certainty.

## Core Idea

AI outputs are inherently probabilistic. This means the model can exhibit inconsistency or hallucination. Engineers must design systems that account for this uncertainty by defining clear decision boundaries (thresholds) for acceptable risk.

## Practical Use

For classification tasks (e.g., spam detection), do not rely solely on the generated text. Instead, use the model's raw output probabilities (e.g., P(spam) > 0.5) to make a definitive, quantifiable decision.

## Related

- [[LLM-Sampling|LLM Sampling]]
- Decision Frameworks
