---
type: pattern
status: evergreen
aliases:
  - Temperature Sampling
  - Temperature scaling
  - Adjusting logits for creativity
tags:
  - ai-engineering
  - llm-tuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
    locator: pages 114-119
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Temperature is a constant used to adjust the logits before the softmax transformation.
      - For a given temperature T, the adjusted logit for the $i^{th}$ token is $x_i/T$. Softmax is then applied on this adjusted logit instead of on $x_i$.
      - The higher the temperature, the less likely it is that the model is going to pick the most obvious value... The lower the temperature, the more likely it is that the model is going to pick the most obvious value.
created: 2026-05-26T21:55:45.583171+00:00
updated: 2026-05-26T21:55:45.583171+00:00
ingestion_run: 8d527d59
---

# Temperature Sampling

## Summary

A method that adjusts the logits by dividing them by a constant temperature (T) before applying the softmax function. Higher T increases randomness and creativity; lower T increases predictability and consistency.

## Core Idea

Temperature acts as a control knob for the probability distribution. Dividing logits by T redistributes probabilities: high T flattens the distribution, allowing lower-probability tokens to surface (more creative); low T sharpens the distribution, emphasizing the most likely tokens (more predictable).

## Practical Use

Use Temperature to fine-tune model output style. For creative writing or brainstorming, use a higher T (e.g., 0.7). For factual summarization or code generation where consistency is paramount, use a low T (approaching 0).

## Related

- Sampling Strategies
- Argmax Function
