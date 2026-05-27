---
type: pattern
status: evergreen
aliases:
  - Agent Planning Cycle (Reasoning Loop)
  - Goal-Oriented Agent Workflow
  - Iterative Agent Execution
tags:
  - ai-engineering
  - llm-workflow
  - planning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/117-agent-overview.md
    locator: pages 300-301
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - AI is the brain that processes the information it receives, including the task and feedback from the environment, plans a sequence of actions to achieve this task, and determines whether the task has been accomplished.
      - "The agent might perform the following sequence of actions: 1. Reason... 2. Invoke SQL query generation... 3. Invoke SQL query execution... 4. Reason about the tool outputs..."
created: 2026-05-26T21:55:46.084775+00:00
updated: 2026-05-26T21:55:46.084775+00:00
ingestion_run: 8d527d59
---

# Agent Planning Cycle (Reasoning Loop)

## Summary

A structured, iterative process where the agent uses its internal reasoning (AI 'brain') to plan a sequence of actions, execute those actions using tools, and then use the resulting feedback to refine or adjust the plan until the goal is met.

## Core Idea

Agents do not execute a single command; they perform a loop: Reason -> Plan -> Act (Tool Invocation) -> Observe (Feedback) -> Re-Reason. This iterative loop is crucial for handling complex, multi-step tasks.

## Practical Use

Implement the agent logic using a structured prompt that forces the model to output intermediate reasoning steps (Chain-of-Thought) before calling a tool. Use the tool output as the primary input for the next reasoning step.

## Related

- Chain-of-Thought
- Self-Correction
