---
type: framework
status: evergreen
aliases:
  - Feedback Collection Timing Framework
  - AI feedback lifecycle
  - When to ask for feedback
tags:
  - ai-engineering
  - ux-design
  - operational-playbook
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
    locator: pages 504-513
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Feedback should be collected throughout the user journey.
      - Initial feedback should be optional to avoid friction.
      - Users must be able to report errors (hallucinations, blocks) when they occur.
      - When a model is uncertain, asking for user feedback (e.g., side-by-side comparison) can increase confidence.
created: 2026-05-26T21:55:46.576468+00:00
updated: 2026-05-26T21:55:46.576468+00:00
ingestion_run: 8d527d59
---

# Feedback Collection Timing Framework

## Summary

A structured approach to integrating feedback collection points throughout the user journey, optimizing for non-intrusiveness and relevance.

## Core Idea

Feedback collection should be contextual and timely. The optimal timing depends on the user state: initial calibration, failure state, or model uncertainty.

## Practical Use

Design the UI/UX to include feedback options at three key moments: 1. **Onboarding/Beginning:** For initial calibration (e.g., voice recognition, skill gauging). Keep it optional to minimize friction. 2. **Failure State:** When the model hallucinates, blocks a request, or performs poorly. Offer immediate remediation (e.g., down-vote, regenerate, edit the output). 3. **Low Confidence State:** When the model is uncertain about the best action, prompt the user for preference (e.g., side-by-side summaries).

## Related

- Inpainting for AI
- [[Comparative-Preference-Signals|Comparative Preference Signals]]
