---
type: framework
status: evergreen
aliases:
  - Prompt Attack Taxonomy
  - LLM Risk Assessment Framework
  - AI Misuse Vectors
tags:
  - ai-engineering
  - risk-management
  - security
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/105-proprietary-prompts-and-reverse-prompt-engineering.md
    locator: pages 260-261
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Social harms: AI models help attackers gain knowledge and tutorials about dangerous or criminal activities."
      - "Misinformation: Attackers might manipulate models to output misinformation to support their agenda."
      - "Service interruption and subversion: ...A malicious instruction that asks the model to refuse to answer all the questions can cause service interruption."
      - "Brand risk: Having politically incorrect and toxic statements next to your logo can cause a PR crisis."
created: 2026-05-26T21:55:45.993065+00:00
updated: 2026-05-26T21:55:45.993065+00:00
ingestion_run: 8d527d59
---

# Prompt Attack Taxonomy

## Summary

A structured framework for classifying potential malicious uses and risks associated with deployed LLM applications, moving beyond simple prompt injection.

## Core Idea

AI risks are multi-faceted and impact business operations, reputation, and safety. A comprehensive risk assessment must consider social, operational, and brand-level harms.

## Practical Use

Use this framework during the design phase (Threat Modeling) to identify necessary guardrails. For example, if 'Service Interruption' is a risk, implement mandatory input validation and fail-safe mechanisms that prevent the model from refusing to answer all questions.

## Related

- [[Defensive-Prompt-Engineering|Defensive Prompt Engineering]]
- AI Governance
