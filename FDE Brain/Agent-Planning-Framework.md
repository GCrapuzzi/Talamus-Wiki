---
type: framework
status: evergreen
aliases:
  - Agent Planning Framework
  - Task Decomposition Workflow
  - Autonomous Agent Planning Cycle
tags:
  - ai-engineering
  - agent-design
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/119-planning.md
    locator: pages 305-321
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The output of the planning process is a plan, which is a roadmap outlining the steps needed to accomplish a task.
      - The process involves generating a plan, validating it, and then executing it.
      - "The overall process involves: 1. Plan generation, 2. Reflection and error correction (plan validation), 3. Execution, 4. Reflection and error correction (outcome evaluation)."
created: 2026-05-26T21:55:46.110258+00:00
updated: 2026-05-26T21:55:46.110258+00:00
ingestion_run: 8d527d59
---

# Agent Planning Framework

## Summary

A structured, multi-stage process for complex AI agents to achieve a goal by generating, validating, and executing a roadmap (plan) rather than attempting direct, monolithic execution.

## Core Idea

Complex tasks must be broken down into a sequence of manageable, verifiable steps. The process is iterative: Plan -> Validate -> Execute -> Evaluate -> Correct/Refine.

## Practical Use

When designing an agent, implement a three-component loop: 1) Plan Generator (outputs the roadmap), 2) Plan Validator (checks feasibility/safety), and 3) Plan Executor (runs the steps). This prevents costly, fruitless execution.

## Related

- [[Decoupling-Planning-and-Execution|Decoupling Planning and Execution]]
- Multi-Agent System Architecture
- Reflection and Error Correction
