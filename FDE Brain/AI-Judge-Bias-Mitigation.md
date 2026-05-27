---
type: concept
status: evergreen
aliases:
  - AI Judge Bias Mitigation
  - AI evaluation bias
  - LLM judging bias
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - GPT-4 favors itself with a 10% higher win rate, while Claude-v1 favors itself with a 25% higher win rate.
      - Many AI models have first-position bias.
      - Humans tend to favor the answer they see last, which is called recency bias.
      - Wu and Aji (2023) found that both GPT-4 and Claude-1 prefer longer responses (~100 words) with factual errors over shorter, correct responses (~50 words).
created: 2026-05-26T21:55:45.738053+00:00
updated: 2026-05-26T21:55:45.738053+00:00
ingestion_run: 8d527d59
---

# AI Judge Bias Mitigation

## Summary

Systematic biases inherent in AI models when used for evaluation, including favoring the first answer (first-position bias), favoring length (verbosity bias), and positional bias.

## Core Idea

AI judges do not evaluate neutrally. They exhibit biases (e.g., favoring the first option or longer responses) that differ from human biases (e.g., recency bias). Recognizing these biases is crucial for designing robust evaluation protocols.

## Practical Use

When designing an evaluation suite, mitigate bias by repeating tests with randomized orderings, using carefully crafted prompts, and normalizing response lengths or content complexity.

## Related

- Position Bias
- Verbosity Bias
