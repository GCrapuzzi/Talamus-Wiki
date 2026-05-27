---
type: method
status: evergreen
aliases:
  - Scope Definition and Guardrails
  - Out-of-Scope Topic Filtering
  - Domain Restriction
tags:
  - ai-engineering
  - prompt-engineering
  - guardrails
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To reduce the chance of your application talking about topics it’s not prepared for, you can define out-of-scope topics for your application.
created: 2026-05-26T21:55:46.028152+00:00
updated: 2026-05-26T21:55:46.028152+00:00
ingestion_run: 8d527d59
---

# Scope Definition and Guardrails

## Summary

Explicitly defining the boundaries and acceptable topics of the application, and implementing filters or guardrails to prevent the model from discussing or answering questions outside of its intended domain.

## Core Idea

Limiting the domain of the application reduces the attack surface. By defining what the system *should* talk about, you implicitly restrict what it *should not* talk about.

## Practical Use

If building a customer support chatbot, the system prompt and input validation must include instructions to reject or redirect any queries related to politics, social issues, or topics outside the defined product scope.

## Related

- [[Prompt-Attack-Defense-Framework|Prompt Attack Defense Framework]]
