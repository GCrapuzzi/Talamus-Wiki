---
type: framework
status: evergreen
aliases:
  - Constraint-Based Evaluation Framework
  - Yes/No Criteria Evaluation
  - Multi-Criteria Scoring
tags:
  - ai-engineering
  - evaluation
  - framework
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/080-instruction-following-capability.md
    locator: pages 196-200
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A model is considered to successfully follow an instruction if its output meets all the criteria for this instruction.
      - If the instruction has three criteria and the evaluator determines that a model’s output meets two of them, the model’s score for this instruction is 2/3.
created: 2026-05-26T21:55:45.816315+00:00
updated: 2026-05-26T21:55:45.816315+00:00
ingestion_run: 8d527d59
---

# Constraint-Based Evaluation Framework

## Summary

An evaluation methodology where an instruction is broken down into multiple, discrete, verifiable criteria (yes/no questions). The model's score is calculated by the fraction of criteria met.

## Core Idea

This framework moves beyond simple pass/fail testing. By quantifying adherence to multiple criteria, it provides a granular measure of how well a model satisfies complex, multi-faceted instructions (e.g., 'Is it a questionnaire?' AND 'Is it for hotel guests?' AND 'Is it helpful?').

## Practical Use

When developing a complex prompt, define the success criteria upfront. For every constraint (e.g., tone, length, content inclusion), formulate a binary (yes/no) question that can be programmatically or manually verified against the output.

## Related

- [[Instruction-Following-Capability-IFC|Instruction-Following Capability (IFC)]]
