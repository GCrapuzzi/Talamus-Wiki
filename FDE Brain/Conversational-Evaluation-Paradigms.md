---
type: framework
status: evergreen
aliases:
  - Conversational Evaluation Paradigms
  - Turn-based vs Task-based Evaluation
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/087-step-1.-evaluate-all-components-in-a-system.md
    locator: pages 224-225
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Turn-based evaluation evaluates the quality of each output. Task-based evaluation evaluates whether a system completes a task.
      - It makes a big difference if a system is able to solve a problem in two turns or in twenty turns.
created: 2026-05-26T21:55:45.861362+00:00
updated: 2026-05-26T21:55:45.861362+00:00
ingestion_run: 8d527d59
---

# Conversational Evaluation Paradigms

## Summary

A decision framework for evaluating generative AI applications (like chatbots) that determines whether the focus should be on the quality of individual responses (Turn-based) or the successful completion of the overall objective (Task-based).

## Core Idea

While Turn-based evaluation measures the quality of each output, Task-based evaluation measures the system's ability to guide the user to a solution. The shift in focus from local quality (turn) to global outcome (task) is crucial for assessing real-world utility.

## Practical Use

When designing a chatbot benchmark, prioritize defining clear task boundaries and success criteria (e.g., 'Did the system help fix the bug?') over simply scoring the coherence or fluency of the model's responses.

## Related

- [[Task-Based-Evaluation|Task-Based Evaluation]]
- [[AI-Evaluation-Granularity|AI Evaluation Granularity]]
