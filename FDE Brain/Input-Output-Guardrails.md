---
type: pattern
status: evergreen
aliases:
  - Input/Output Guardrails
  - LLM Safety Filters
  - Content Moderation Layers
tags:
  - ai-engineering
  - safety
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/109-summary.md
    locator: pages 275-276
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You should also place guardrails both to the inputs and outputs.
      - On the input side, you can have a list of keywords to block, known prompt attack patterns to match the inputs against, or a model to detect suspicious requests.
      - For example, a guardrail can check if an output contains PII or toxic information.
created: 2026-05-26T21:55:46.029952+00:00
updated: 2026-05-26T21:55:46.029952+00:00
ingestion_run: 8d527d59
---

# Input/Output Guardrails

## Summary

A defensive architecture requiring checks on both the user input (prompt) and the model output to prevent harmful, illegal, or sensitive content generation.

## Core Idea

LLMs are powerful but prone to generating undesirable content (PII, toxicity) even from seemingly harmless inputs. Guardrails must be implemented at both the ingress (input) and egress (output) points to maintain safety and compliance.

## Practical Use

Implement a multi-stage validation pipeline: 1. Input validation (keyword blocking, known attack pattern matching, intent analysis). 2. Output validation (PII detection, toxicity scoring, adherence to format/schema). This is critical for high-stakes, regulated environments.

## Related

- [[Adversarial-Prompt-Detection|Adversarial Prompt Detection]]
- [[Contextual-Grounding|Contextual Grounding]]
