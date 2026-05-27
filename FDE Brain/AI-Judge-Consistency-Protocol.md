---
type: method
status: evergreen
aliases:
  - AI Judge Consistency Protocol
  - Reproducibility Testing for LLM Judges
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
    locator: pages 165-168
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The same judge, on the same input, can output different scores if prompted differently. Even the same judge, prompted with the same instruction, can output different scores if run twice.
      - Zheng et al. (2023) showed that including evaluation examples in the prompt can increase the consistency of GPT-4 from 65% to 77.5%.
created: 2026-05-26T21:55:45.729254+00:00
updated: 2026-05-26T21:55:45.729254+00:00
ingestion_run: 8d527d59
---

# AI Judge Consistency Protocol

## Summary

Due to the probabilistic nature of LLMs, AI judges can exhibit inconsistency (different scores on the same input, even with the same prompt). To mitigate this, use structured sampling and prompt engineering techniques.

## Core Idea

Consistency (reliability) is a separate concern from accuracy. While techniques like providing evaluation examples in the prompt can increase consistency, this must be balanced against increased inference costs and prompt length.

## Practical Use

When running critical evaluations, run the judge multiple times (sampling) and analyze the variance in scores. If high consistency is required, incorporate few-shot examples into the prompt, but budget for the resulting increased API costs.

## Related

- Sampling Techniques
- [[Prompt-Engineering|Prompt Engineering]]
