---
type: pattern
status: evergreen
aliases:
  - Human-in-the-Loop (HITL) Oversight
  - Human Validation Gate
  - Human-in-the-Loop Control
tags:
  - ai-engineering
  - safety
  - governance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/119-planning.md
    locator: pages 305-321
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In reality, humans can be involved at any of those stages to aid with the process and mitigate risks.
      - If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval before executing.
created: 2026-05-26T21:55:46.117607+00:00
updated: 2026-05-26T21:55:46.117607+00:00
ingestion_run: 8d527d59
---

# Human-in-the-Loop (HITL) Oversight

## Summary

A safety and reliability pattern where human experts are integrated into the agent workflow to provide high-level plans, validate risky steps, or execute critical parts of the plan.

## Core Idea

For high-stakes or complex tasks, full automation is too risky. HITL provides necessary oversight, mitigating risks associated with autonomous actions (e.g., updating databases, merging code changes).

## Practical Use

Define the level of automation for each action. For risky operations, the system must pause and request explicit human approval before proceeding with execution.

## Related

- [[Agent-Planning-Framework|Agent Planning Framework]]
- Safety Engineering
