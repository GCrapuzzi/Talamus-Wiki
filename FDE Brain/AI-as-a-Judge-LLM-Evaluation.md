---
type: method
status: evergreen
aliases:
  - AI as a Judge (LLM Evaluation)
  - LLM Evaluation
  - AI Grading
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/079-generation-capability.md
    locator: pages 187-195
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The most straightforward evaluation approach is AI as a judge.
      - AI judges can be asked to evaluate anything, including factual consistency.
created: 2026-05-26T21:55:45.807378+00:00
updated: 2026-05-26T21:55:45.807378+00:00
ingestion_run: 8d527d59
---

# AI as a Judge (LLM Evaluation)

## Summary

Using a powerful, separate LLM (the 'Judge') to programmatically evaluate the quality, consistency, or adherence to rules of a target model's output, rather than relying solely on predefined metrics.

## Core Idea

AI judges can evaluate complex, subjective criteria (like tone, coherence, or factual consistency) that traditional metrics cannot capture. This method is highly effective for measuring nuanced qualities.

## Practical Use

Implement a structured prompt for the Judge LLM, providing the original prompt, the source context, and the model's output. Instruct the Judge to output a structured JSON response detailing scores for specific criteria (e.g., 'Factual Consistency: High/Medium/Low', 'Tone: Neutral/Biased').

## Related

- [[Factual-Consistency-Evaluation|Factual Consistency Evaluation]]
- [[Generation-Capability-Metrics-NLG|Generation Capability Metrics (NLG)]]
