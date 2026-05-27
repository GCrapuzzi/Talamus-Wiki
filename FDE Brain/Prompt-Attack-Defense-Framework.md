---
type: framework
status: evergreen
aliases:
  - Prompt Attack Defense Framework
  - LLM Security Defense Strategy
  - Adversarial Prompt Defense
tags:
  - ai-engineering
  - security
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Defenses against prompt attacks can be implemented at the model, prompt, and system levels.
created: 2026-05-26T21:55:46.017070+00:00
updated: 2026-05-26T21:55:46.017070+00:00
ingestion_run: 8d527d59
---

# Prompt Attack Defense Framework

## Summary

A multi-layered approach to securing LLM applications by implementing defenses at the model, prompt, and system levels.

## Core Idea

Security cannot be solved by a single layer. Robust defense requires understanding potential attack vectors (e.g., prompt injection) and implementing safeguards across the entire stack to minimize risk, acknowledging that complete elimination of risk is impossible.

## Practical Use

When designing an LLM application, use this framework to checklist security requirements: 1) Model-level (fine-tuning, hierarchy); 2) Prompt-level (constraints, duplication); 3) System-level (isolation, gates).

## Related

- [[Instruction-Hierarchy|Instruction Hierarchy]]
- [[Red-Teaming-Playbook|Red Teaming Playbook]]
- [[Borderline-Request-Handling|Borderline Request Handling]]
