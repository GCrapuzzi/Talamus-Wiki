---
type: method
status: evergreen
aliases:
  - Error Correction Pattern
  - Rephrasing Attempt Detection
  - Intent Misunderstanding Signal
tags:
  - ai-engineering
  - prompt-engineering
  - debugging
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
    locator: pages 499-503
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If a user starts their follow-up with “No, …” or “I meant, …”, the model’s response is likely off the mark.
      - "For example, if a user asks the model to summarize a story and the model confuses a character, this user can give feedback such as: “Bill is the suspect, not the victim.”"
created: 2026-05-26T21:55:46.569635+00:00
updated: 2026-05-26T21:55:46.569635+00:00
ingestion_run: 8d527d59
---

# Error Correction Pattern

## Summary

The user explicitly correcting the model's output or misunderstanding, often by rephrasing the request or providing factual corrections (e.g., 'Bill is the suspect, not the victim').

## Core Idea

Error correction is a direct signal of model failure or misinterpretation of intent. Analyzing the correction allows engineers to pinpoint the exact failure mode (e.g., character confusion, factual inaccuracy) and improve the model's grounding or reasoning.

## Practical Use

Implement a dedicated module to capture the original prompt, the model's response, and the user's corrective follow-up. Use these triplets as high-priority examples for model fine-tuning and prompt refinement, especially in agentic workflows.

## Related

- [[Conversational-Feedback-Loop|Conversational Feedback Loop]]
- [[Natural-Language-Feedback-Signals|Natural Language Feedback Signals]]
