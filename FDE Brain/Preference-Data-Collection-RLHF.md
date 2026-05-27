---
type: pattern
status: evergreen
aliases:
  - Preference Data Collection (RLHF)
  - Human Preference Alignment
  - Winning/Losing Response Pairing
tags:
  - ai-engineering
  - rlhf
  - model-alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/175-extracting-conversational-feedback.md
    locator: pages 499-503
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Each user edit makes up a preference example, with the original generated response being the losing response and the edited response being the winning response.
created: 2026-05-26T21:55:46.570948+00:00
updated: 2026-05-26T21:55:46.570948+00:00
ingestion_run: 8d527d59
---

# Preference Data Collection (RLHF)

## Summary

Systematically collecting user preference data, typically in the format of (query, winning response, losing response), to align a model to human judgment (Reinforcement Learning from Human Feedback).

## Core Idea

User edits and regeneration choices are powerful, implicit sources of preference data. The original generated response becomes the 'losing' response, and the user-edited or selected response becomes the 'winning' response, providing direct signal for model alignment.

## Practical Use

When a user edits generated code or text, log the original output and the final edited version. When a user chooses a regenerated response, log the comparison. These pairs form the core dataset for preference modeling and model refinement.

## Related

- [[Conversational-Feedback-Loop|Conversational Feedback Loop]]
- User Edits Signal
