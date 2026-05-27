---
type: pattern
status: evergreen
aliases:
  - AI Judge Scoring Best Practices
  - Prompting for Reliability
  - Scoring System Design
tags:
  - ai-engineering
  - prompt-engineering
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
    locator: pages 162-164
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Language models are generally better with text than with numbers.
      - AI judges work better with classification than with numerical scoring systems.
      - For numerical scoring systems, discrete scoring seems to work better than continuous scoring.
      - Prompts with examples have been shown to perform better.
created: 2026-05-26T21:55:45.723742+00:00
updated: 2026-05-26T21:55:45.723742+00:00
ingestion_run: 8d527d59
---

# AI Judge Scoring Best Practices

## Summary

Guidelines for optimizing the scoring system within an AI judge prompt to maximize reliability and consistency.

## Core Idea

LLMs perform best when evaluation is framed in text-based classification rather than pure numerical calculation. Providing detailed examples for each score level significantly improves performance.

## Practical Use

When designing a scoring prompt, prioritize classification (e.g., 'Good/Bad') over continuous numerical ranges (e.g., 0.0 to 1.0). If numerical scoring is necessary, use discrete scales (e.g., 1 to 5) and always include examples for each level.

## Related

- [[AI-Judge-Prompting-Framework|AI Judge Prompting Framework]]
