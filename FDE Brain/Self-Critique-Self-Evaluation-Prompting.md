---
type: pattern
status: evergreen
aliases:
  - Self-Critique/Self-Evaluation Prompting
  - Self-eval
  - Internal validation loop
tags:
  - ai-engineering
  - prompt-engineering
  - validation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/101-iterate-on-your-prompts.md
    locator: pages 253-253
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Self-critique means asking the model to check its own outputs.
      - Similar to CoT, self-critique can increase the latency per‐ceived by users.
created: 2026-05-26T21:55:45.961333+00:00
updated: 2026-05-26T21:55:45.961333+00:00
ingestion_run: 8d527d59
---

# Self-Critique/Self-Evaluation Prompting

## Summary

A pattern where the LLM is explicitly prompted to review, critique, and refine its own initial output based on defined criteria, enhancing the robustness and quality of the final result.

## Core Idea

This technique leverages the model's ability to perform meta-cognition, forcing it to identify potential flaws or biases in its own reasoning chain, thereby increasing reliability.

## Practical Use

Use when the output must meet high standards of accuracy or objectivity (e.g., legal summaries, technical reports). Structure the prompt to first generate the output, and then generate a separate critique/revision step.

## Related

- [[Chain-of-Thought-CoT-Prompting|Chain-of-Thought (CoT) Prompting]]
