---
type: framework
status: evergreen
aliases:
  - Defensive Prompt Engineering
  - LLM Security
  - Prompt Hardening
tags:
  - ai-engineering
  - security
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/104-defensive-prompt-engineering.md
    locator: pages 259-259
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Once your application is made available, it can be used by both intended users and malicious attackers who may try to exploit it.
      - "There are three main types of prompt attacks that, as application developers, you want to defend against: Prompt extraction, Jailbreaking and prompt injection, Information extraction."
      - Remote code or tool execution... Bad actors can extract private information about your system and your users.
created: 2026-05-26T21:55:45.984800+00:00
updated: 2026-05-26T21:55:45.984800+00:00
ingestion_run: 8d527d59
---

# Defensive Prompt Engineering

## Summary

A set of practices and strategies designed to secure LLM applications against malicious inputs, exploitation, and data leakage after deployment.

## Core Idea

LLM applications must be treated as attack surfaces. Defense requires anticipating three main types of attacks: prompt extraction, jailbreaking/injection, and information extraction.

## Practical Use

When deploying an LLM-powered feature, implement input validation, use sandboxing for tool/code execution, and establish prompt guardrails to mitigate unauthorized actions (e.g., SQL queries, unauthorized emails).

## Related

- [[Prompt-Attack-Taxonomy|Prompt Attack Taxonomy]]
- [[Prompt-Cataloging-and-Versioning|Prompt Cataloging and Versioning]]
