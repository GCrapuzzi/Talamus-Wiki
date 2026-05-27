---
type: operation
status: evergreen
aliases:
  - Custom LLM Benchmarking Playbook
  - Domain-Specific Evaluation
  - Ad-Hoc Model Testing
tags:
  - ai-engineering
  - evaluation
  - playbook
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/080-instruction-following-capability.md
    locator: pages 196-200
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You should curate your own benchmark to evaluate your model’s capability to follow your instructions using your own criteria.
      - If you need a model to output YAML, include YAML instructions in your benchmark. If you want a model to not say things like 'As a language model', evaluate the model on this instruction.
created: 2026-05-26T21:55:45.814886+00:00
updated: 2026-05-26T21:55:45.814886+00:00
ingestion_run: 8d527d59
---

# Custom LLM Benchmarking Playbook

## Summary

A systematic process for evaluating an LLM's performance against the specific, real-world instructions and constraints of a target application, rather than relying solely on generalized academic benchmarks.

## Core Idea

General benchmarks (like IFEval or INFOBench) are insufficient because they miss niche, domain-specific instructions. A model performing well on general tests may fail on proprietary business logic or unique output requirements.

## Practical Use

1. Identify all critical constraints (e.g., 'Must not mention X', 'Must use YAML format', 'Must address the user as a doctor'). 2. Create a test set of prompts that specifically test these constraints. 3. Evaluate the model's output against a human-defined rubric (yes/no criteria) for each constraint.

## Related

- [[Instruction-Following-Capability-IFC|Instruction-Following Capability (IFC)]]
