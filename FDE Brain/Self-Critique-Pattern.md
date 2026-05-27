---
type: pattern
status: evergreen
aliases:
  - Self-Critique Pattern
  - Self-Ask
  - Self-Correction Loop
tags:
  - ai-engineering
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Beyond sanity checks, asking a model to evaluate itself can nudge a model to revise and improve its responses.
created: 2026-05-26T21:55:45.742139+00:00
updated: 2026-05-26T21:55:45.742139+00:00
ingestion_run: 8d527d59
---

# Self-Critique Pattern

## Summary

A method where an AI model is prompted to evaluate its own initial response, leading to a revised and improved final output.

## Core Idea

Self-critique moves beyond simple generation by forcing the model to engage in metacognition (thinking about its own thinking). This process can improve reliability and accuracy, especially for sanity checks.

## Practical Use

Implement a three-stage prompt structure: 1. Generate initial response. 2. Prompt the model: 'Critique the previous answer for accuracy/completeness.' 3. Prompt the model: 'Based on your critique, provide the final, revised answer.'

## Related

- [[AI-Judge-Evaluation-Framework|AI Judge Evaluation Framework]]
