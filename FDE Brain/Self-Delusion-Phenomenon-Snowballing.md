---
type: concept
status: evergreen
aliases:
  - Self-Delusion Phenomenon (Snowballing)
  - Model Self-Correction Failure
  - Snowballing Hallucination
tags:
  - ai-engineering
  - llm-theory
  - error-analysis
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/053-the-probabilistic-nature-of-ai.md
    locator: pages 129-134
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The first hypothesis... is that a language model hallucinates because it can’t differentiate between the data it’s given and the data it generates.
      - Zhang et al. (2023) call this phenomenon snowballing hallucinations.
created: 2026-05-26T21:55:45.619903+00:00
updated: 2026-05-26T21:55:45.619903+00:00
ingestion_run: 8d527d59
---

# Self-Delusion Phenomenon (Snowballing)

## Summary

A form of hallucination where the model treats its own generated, incorrect output as a given fact, using it as context to generate subsequent, increasingly wrong information.

## Core Idea

The model lacks the ability to differentiate between external, provided facts (observations) and internally generated assumptions (actions). This leads to a compounding error effect.

## Practical Use

When designing multi-step reasoning chains, structure the prompt to force the model to explicitly state its assumptions and the evidence for those assumptions, rather than allowing it to seamlessly integrate generated assumptions into the final answer.

## Related

- [[Hallucination-Detection-and-Mitigation|Hallucination Detection and Mitigation]]
- [[Reinforcement-Learning-from-Human-Feedback-RLHF|Reinforcement Learning from Human Feedback (RLHF)]]
