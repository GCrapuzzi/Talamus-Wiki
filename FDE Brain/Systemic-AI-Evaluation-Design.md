---
type: framework
status: evergreen
aliases:
  - Systemic AI Evaluation Design
  - Failure Mode Evaluation
  - Contextual AI Testing
  - Risk-Based Evaluation
tags:
  - ai-engineering
  - evaluation
  - risk-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/055-chapter-3.-evaluation-methodology.md
    locator: pages 137-137
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Evaluation aims to mitigate risks and uncover opportunities.
      - Evaluation has to be considered in the context of a whole system, not in isolation.
      - To mitigate risks, you first need to identify the places where your system is likely to fail and design your evaluation around them.
created: 2026-05-26T21:55:45.634406+00:00
updated: 2026-05-26T21:55:45.634406+00:00
ingestion_run: 8d527d59
---

# Systemic AI Evaluation Design

## Summary

A methodology that treats AI evaluation not as a standalone metric check, but as an integral part of the overall system design, focusing specifically on identifying and testing anticipated failure points.

## Core Idea

AI risk is high and complex; therefore, evaluation must be systemic. Instead of testing general performance, the process must first identify the specific points where the system is most likely to fail (failure modes) and design the evaluation around mitigating those risks. This often requires redesigning the system to enhance visibility into potential failures.

## Practical Use

When deploying an AI application (e.g., a legal chatbot or medical assistant), do not rely solely on standard benchmarks. Instead, conduct a Failure Mode and Effects Analysis (FMEA) to map out high-risk scenarios (e.g., hallucination, providing false evidence, giving dangerous advice). Design specific guardrails, human-in-the-loop checks, and targeted tests for these identified failure paths.

## Related

- AI Safety
- System Redesign for Observability
- Risk Mitigation Playbook
