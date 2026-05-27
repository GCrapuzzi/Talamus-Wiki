---
type: concept
status: evergreen
aliases:
  - Agent Failure Mode Taxonomy
  - AI Agent Failure Modes
  - Agent Failure Taxonomy
tags:
  - ai-engineering
  - agent-design
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
    locator: pages 322-323
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "The agent might generate a plan with one or more of these errors: Invalid tool, Valid tool, invalid parameters, Valid tool, incorrect parameter values."
      - "Another mode of planning failure is goal failure: the agent fails to achieve the goal."
      - An interesting mode of planning failure is caused by errors in reflection.
      - Tool failures happen when the correct tool is used, but the tool output is wrong.
created: 2026-05-26T21:55:46.120605+00:00
updated: 2026-05-26T21:55:46.120605+00:00
ingestion_run: 8d527d59
---

# Agent Failure Mode Taxonomy

## Summary

A structured classification of potential failure points in AI agents, covering planning, tool usage, and goal achievement.

## Core Idea

Agent reliability is not monolithic; failures must be categorized (e.g., planning vs. tool output) to enable targeted evaluation and mitigation. Failure points include invalid tool calls, incorrect parameters, goal misalignment, and faulty reflection.

## Practical Use

When designing or evaluating an agent, use this taxonomy to create a comprehensive test suite. If an agent fails, classify the failure (e.g., 'Planning failure: Invalid tool') to determine if the fix requires better prompting, fine-tuning, or tool replacement.

## Related

- Agent Evaluation Playbook
- [[Tool-Use-Failure-Modes|Tool Use Failure Modes]]
