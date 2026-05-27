---
type: pattern
status: evergreen
aliases:
  - Obfuscation Attacks
  - Keyword Bypass
  - Character Manipulation
tags:
  - ai-engineering
  - security
  - data-filtering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/106-jailbreaking-and-prompt-injection.md
    locator: pages 262-266
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If a model blocks certain keywords, attackers can intentionally misspell a keyword... to bypass this keyword filter.
      - The malicious keywords can also be hidden in a mixture of languages or Unicode.
created: 2026-05-26T21:55:46.000837+00:00
updated: 2026-05-26T21:55:46.000837+00:00
ingestion_run: 8d527d59
---

# Obfuscation Attacks

## Summary

Techniques used to bypass safety filters by intentionally altering the input format, such as misspelling keywords, mixing languages, or inserting unusual characters.

## Core Idea

Attackers exploit the model's ability to understand meaning despite input corruption. Simple keyword filters are ineffective because modern LLMs are robust enough to correct typos and understand context.

## Practical Use

Defensive measures must move beyond simple keyword blocking. Implement fuzzy matching and semantic analysis on user inputs to detect malicious intent, even if the keywords are misspelled or mixed with Unicode characters.

## Related

- Input Sanitization
- Unicode Filtering
