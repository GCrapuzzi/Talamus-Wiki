---
type: glossary
status: evergreen
aliases:
  - Log Probabilities (Logprobs)
  - log scale probabilities
tags:
  - ai-engineering
  - llm-math
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
    locator: pages 114-119
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Logprobs, short for log probabilities, are probabilities in the log scale.
      - Log scale helps reduce this problem [underflow].
created: 2026-05-26T21:55:45.588430+00:00
updated: 2026-05-26T21:55:45.588430+00:00
ingestion_run: 8d527d59
---

# Log Probabilities (Logprobs)

## Summary

Probabilities expressed in the logarithmic scale (log(p)).

## Core Idea

When dealing with large vocabularies, standard probabilities can become extremely small, leading to the 'underflow problem' (where the number is rounded down to zero by the machine). Working in log space prevents this numerical instability, making it essential for accurate calculations and model evaluation.

## Practical Use

Use logprobs when building applications that require precise probability analysis, such as classification tasks, model evaluation, or understanding model uncertainty. Be aware that access to logprobs is often limited by model providers.

## Related

- [[Softmax-Function|Softmax Function]]
- Underflow Problem
