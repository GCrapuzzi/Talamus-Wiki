---
type: concept
status: evergreen
aliases:
  - Reverse Prompt Engineering
  - Prompt Extraction
  - System Prompt Deduction
tags:
  - ai-engineering
  - security
  - llm-security
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/105-proprietary-prompts-and-reverse-prompt-engineering.md
    locator: pages 260-261
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Reverse prompt engineering is the process of deducing the system prompt used for a certain application.
      - Bad actors can use the leaked system prompt to replicate your application or manipulate it into doing undesirable actions.
created: 2026-05-26T21:55:45.990771+00:00
updated: 2026-05-26T21:55:45.990771+00:00
ingestion_run: 8d527d59
---

# Reverse Prompt Engineering

## Summary

The process of deducing or extracting the underlying system prompt used by an LLM application, often by analyzing outputs or tricking the model into repeating its instructions.

## Core Idea

The system prompt is the foundational instruction set that defines the model's behavior, guardrails, and persona. Exposing it allows bad actors to replicate the application's functionality or manipulate it into undesirable actions.

## Practical Use

1. **Security Testing:** Actively attempt to extract the system prompt during penetration testing to identify vulnerabilities. 2. **Defensive Design:** Assume the system prompt *will* be leaked and design the application logic to fail gracefully or refuse to answer critical instructions if extraction is attempted. 3. **Monitoring:** Implement input/output monitoring to detect attempts to bypass instructions or extract context.

## Related

- [[Defensive-Prompt-Engineering|Defensive Prompt Engineering]]
- [[Prompt-Injection|Prompt Injection]]
