---
type: framework
status: evergreen
aliases:
  - Evaluation Granularity Framework
  - Multi-Level Testing
  - System Depth Evaluation
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/086-design-your-evaluation-pipeline.md
    locator: pages 224-224
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You should evaluate the end-to-end output and each component’s intermediate output independently.
      - If applicable, evaluate your application both per turn and per task.
created: 2026-05-26T21:55:45.854554+00:00
updated: 2026-05-26T21:55:45.854554+00:00
ingestion_run: 8d527d59
---

# Evaluation Granularity Framework

## Summary

A tiered approach to testing AI systems that dictates evaluation at multiple levels of abstraction: the overall task, the conversational turn, and the individual component output.

## Core Idea

The level of evaluation must match the complexity of the task. For multi-step or conversational systems, simply measuring the final output is insufficient. The framework mandates testing at the lowest necessary level (component/intermediate output) to ensure robustness.

## Practical Use

For a chatbot that requires multiple steps (e.g., 'Find me a flight and book it'), the engineer must test: 1) The final booking confirmation (Per Task). 2) The multi-step dialogue flow (Per Turn). 3) The API call component (e.g., the flight search API call) (Per Component).

## Related

- [[Multi-Component-System-Evaluation|Multi-Component System Evaluation]]
