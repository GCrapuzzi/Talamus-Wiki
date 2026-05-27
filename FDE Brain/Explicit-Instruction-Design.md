---
type: method
status: evergreen
aliases:
  - Explicit Instruction Design
  - Clear Prompting
  - Instruction Clarity
tags:
  - prompt-engineering
  - llm-design
  - data-structuring
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/096-prompt-engineering-best-practices.md
    locator: pages 244-244
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Communicating with AI is the same as communicating with humans: clarity helps."
      - Explain, without ambiguity, what you want the model to do
      - If the model outputs fractional scores (4.5) and you don’t want fractional scores, update your prompt to tell the model to output only integer scores.
created: 2026-05-26T21:55:45.927485+00:00
updated: 2026-05-26T21:55:45.927485+00:00
ingestion_run: 8d527d59
---

# Explicit Instruction Design

## Summary

The practice of writing prompts that leave no ambiguity regarding the desired model output, format, or constraints.

## Core Idea

AI models perform best when instructions are unambiguous, detailed, and explicitly define the expected behavior and output structure. Ambiguity leads to unpredictable or undesirable model outputs.

## Practical Use

When designing a prompt, explicitly define the scoring system (e.g., 'Use a 1-5 scale'), the required data type (e.g., 'Output only integers'), and the fallback behavior (e.g., 'If uncertain, output 'N/A''). This minimizes hallucination and ensures structured data.

## Related

- Prompt Components (System, User, Examples, Context)
- Output Constraint Definition
