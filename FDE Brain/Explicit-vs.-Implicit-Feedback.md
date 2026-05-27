---
type: glossary
status: evergreen
aliases:
  - Explicit vs. Implicit Feedback
  - Direct vs. Indirect Feedback
  - User Signal Types
tags:
  - ai-engineering
  - data-collection
  - user-behavior
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
    locator: pages 499-503
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Explicit feedback is information users provide in response to explicit requests for feedback...
      - Implicit feedback is information inferred from user actions.
created: 2026-05-26T21:55:46.566634+00:00
updated: 2026-05-26T21:55:46.566634+00:00
ingestion_run: 8d527d59
---

# Explicit vs. Implicit Feedback

## Summary

Categorization of user feedback: Explicit feedback is direct, intentional input (e.g., thumbs up/down, star rating). Implicit feedback is inferred from user actions or patterns (e.g., clicking a recommended product, modifying generated code).

## Core Idea

Relying solely on explicit feedback limits understanding. Implicit feedback, especially in conversational AI, provides richer, context-dependent signals about user intent and preference that must be systematically captured and analyzed.

## Practical Use

When designing an AI application, map out all possible user actions (clicks, edits, follow-up questions, abandonment) and determine what preference or performance signal each action represents. Prioritize capturing implicit signals where explicit options are limited.

## Related

- [[Conversational-Feedback-Loop|Conversational Feedback Loop]]
