---
type: pattern
status: evergreen
aliases:
  - Instruction Hierarchy
  - Priority Instruction Layering
  - Conflicting Instruction Resolution
tags:
  - ai-engineering
  - prompt-engineering
  - safety
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "The instruction hierarchy contains four levels of priority: System prompt, User prompt, Model outputs, Tool outputs."
      - In the event of conflicting instructions, the higher-priority instruction should be followed.
created: 2026-05-26T21:55:46.019122+00:00
updated: 2026-05-26T21:55:46.019122+00:00
ingestion_run: 8d527d59
---

# Instruction Hierarchy

## Summary

A defined priority order for instructions fed to an LLM, ensuring that higher-priority, more critical instructions override lower-priority or potentially malicious inputs.

## Core Idea

By explicitly structuring the input context, the model can be trained to follow a strict hierarchy, neutralizing indirect prompt injection attacks where malicious instructions might otherwise override system rules.

## Practical Use

When fine-tuning or designing system prompts, ensure that critical safety rules (e.g., 'Do not reveal private information') are placed in the highest priority context (System Prompt) and are reinforced during training.

## Related

- [[Prompt-Attack-Defense-Framework|Prompt Attack Defense Framework]]
