---
type: glossary
status: evergreen
aliases:
  - Jailbreaking
  - Prompt Attack
  - Safety Filter Subversion
tags:
  - ai-engineering
  - security
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/106-jailbreaking-and-prompt-injection.md
    locator: pages 262-266
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Jailbreaking a model means trying to subvert a model’s safety features.
      - They share the same ultimate goal—getting the model to express undesirable behaviors.
created: 2026-05-26T21:55:45.999512+00:00
updated: 2026-05-26T21:55:45.999512+00:00
ingestion_run: 8d527d59
---

# Jailbreaking

## Summary

The act of subverting a model’s safety features or guardrails to get it to express undesirable or restricted behaviors (e.g., generating instructions for dangerous activities).

## Core Idea

Jailbreaking and Prompt Injection share the goal of forcing the model to bypass its safety constraints. The underlying vulnerability is the model's strong adherence to instructions, regardless of ethical or safety guidelines.

## Practical Use

Treat jailbreaking as a continuous security threat model. Implement layered defenses (e.g., input filters, output validators, and secondary safety models) rather than relying on a single prompt instruction to enforce safety.

## Related

- [[Prompt-Injection|Prompt Injection]]
- AI Safety
- Red Teaming
