---
type: concept
status: evergreen
aliases:
  - Human Evaluation as North Star
  - gold standard metric
  - expert review
tags:
  - ai-engineering
  - production-monitoring
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/089-step-3.-define-evaluation-methods-and-data.md
    locator: pages 228-231
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Given the challenges of evaluating openended responses, many teams are looking at human evaluation as the North Star metric to guide their application development.
      - Think about what kinds of feedback you want from users, how user feedback correlates to other evaluation metrics, and how to use user feedback to improve your application.
created: 2026-05-26T21:55:45.882738+00:00
updated: 2026-05-26T21:55:45.882738+00:00
ingestion_run: 8d527d59
---

# Human Evaluation as North Star

## Summary

Recognizing that human judgment remains the ultimate, most reliable metric for evaluating complex, open-ended AI outputs, even when automated metrics are available.

## Core Idea

While automatic metrics are scalable, human evaluation provides the highest fidelity signal regarding quality, safety, and user experience. It should be integrated into the production monitoring loop to detect performance degradation or unusual usage patterns immediately.

## Practical Use

In production, dedicate a small, continuous stream of live user conversations (e.g., 500 daily conversations) to human experts for manual review. This acts as a real-time canary test for model drift or unexpected usage patterns.

## Related

- [[Mixed-Evaluation-Strategy|Mixed Evaluation Strategy]]
- Operational Playbook
