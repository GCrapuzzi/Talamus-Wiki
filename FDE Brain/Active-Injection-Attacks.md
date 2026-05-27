---
type: pattern
status: evergreen
aliases:
  - Active Injection Attacks
  - Prompt Injection
  - Contextual Attack
tags:
  - ai-engineering
  - security
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/107-information-extraction.md
    locator: pages 267-271
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An attacker can send an email with malicious instructions that confuse the assistant.
      - An attacker could sign up with a username that the model interprets as a command to delete all data.
created: 2026-05-26T21:55:46.008921+00:00
updated: 2026-05-26T21:55:46.008921+00:00
ingestion_run: 8d527d59
---

# Active Injection Attacks

## Summary

Proactively sending malicious instructions disguised as legitimate user input or context to confuse the LLM and force unauthorized actions.

## Core Idea

LLMs process all input (system prompts, user messages, tool outputs) as context. Attackers exploit this by embedding malicious commands that override or ignore initial system instructions, leading to data leakage or unauthorized function calls.

## Practical Use

When designing multi-step AI workflows (e.g., RAG systems, tool-calling agents), treat all external inputs (user input, retrieved documents, tool outputs) as potentially hostile. Implement input sanitization and instruction prioritization layers to ensure core system instructions cannot be overridden.

## Related

- [[Defense-against-Data-Extraction|Defense against Data Extraction]]
- System Prompt Guardrails
