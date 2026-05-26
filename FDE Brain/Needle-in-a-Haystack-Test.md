---
type: method
tags: [evaluation, context-window, long-context, NIAH, prompt-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#context-length-and-context-efficiency
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Needle in a Haystack Test

An evaluation method for measuring a model's **context efficiency** — how well it retrieves and uses information at different positions within a long prompt.

**Procedure:** Insert a random fact (the needle) at varying positions in a long document (the haystack). Query the model for that fact. Measure retrieval accuracy by position.

**Key finding** (Liu et al., 2023): Models perform best when target information is near the **beginning or end** of the prompt, and worst in the **middle** — the "lost in the middle" effect.

**Practical variant:** Use real questions from real documents (e.g., drug names from a doctor visit transcript) instead of synthetic strings. Use private information to prevent the model from answering from parametric memory rather than context.

Extended benchmarks like **RULER** (Hsieh et al., 2024) generalize this to evaluate long-context processing quality. If performance degrades sharply with length, shorten your prompts or restructure so critical info sits at prompt boundaries.
