---
type: framework
status: evergreen
aliases:
  - Input Guardrails
  - Prompt Input Validation
  - PII Leakage Prevention
tags:
  - ai-engineering
  - security
  - guardrails
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/168-step-2.-put-in-guardrails.md
    locator: pages 475-479
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Input guardrails typically protect against two types of risks: leaking private information to external APIs and executing bad prompts that compromise your system."
      - You can use one of the many available tools that automatically detect sensitive data.
created: 2026-05-26T21:55:46.521491+00:00
updated: 2026-05-26T21:55:46.521491+00:00
ingestion_run: 8d527d59
---

# Input Guardrails

## Summary

Mechanisms placed at the entry point of the LLM system to protect against two primary risks: 1) leaking private information (PII) to external APIs, and 2) executing malicious or 'bad' prompts that compromise system integrity.

## Core Idea

Input guardrails act as a security perimeter, ensuring that data sent to the model is sanitized and that the prompt adheres to defined usage policies before processing. This is critical when using third-party APIs.

## Practical Use

Implement a pre-processing layer that utilizes sensitive data detection tools (e.g., regex, specialized AI models) to scan user inputs. If sensitive data (PII, proprietary keywords) is detected, the system must either block the query entirely or mask/redact the sensitive information before passing it to the LLM.

## Related

- PII Masking
- Prompt Injection Defense
