---
type: concept
status: evergreen
aliases:
  - Borderline Request Handling
  - Ambiguous Prompting
  - Safety-Helpfulness Balance
tags:
  - ai-engineering
  - safety
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A borderline request is a one that can invoke both safe and unsafe responses.
      - A better system should recognize this possibility and suggest legal solutions, such as contacting a locksmith, thus balancing safety with helpfulness.
created: 2026-05-26T21:55:46.022177+00:00
updated: 2026-05-26T21:55:46.022177+00:00
ingestion_run: 8d527d59
---

# Borderline Request Handling

## Summary

Handling user queries that are ambiguous and could potentially invoke both safe and unsafe responses. The goal is to avoid overly cautious refusal while mitigating risk.

## Core Idea

A system must balance safety with utility. Instead of outright refusal (overly cautious) or providing dangerous instructions (unsafe), the model should identify the ambiguity and guide the user toward safe, legal, or helpful alternatives.

## Practical Use

When designing safety guardrails, train the model on 'borderline' examples (e.g., 'How to break into a locked room?'). The desired response should not be a refusal, but a suggestion of legal recourse (e.g., 'Contact a locksmith').

## Related

- [[Prompt-Attack-Defense-Framework|Prompt Attack Defense Framework]]
