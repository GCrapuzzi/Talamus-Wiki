---
type: framework
tags: [evaluation, agents, failure-modes, planning-failures, tool-failures]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#agent-failure-modes-and-evaluation
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Agent Failure Modes

Agents have unique failure modes beyond standard AI failures. Evaluate by identifying each mode and measuring frequency.

### Planning failures
- **Invalid tool**: plan references tool not in inventory
- **Valid tool, invalid parameters**: wrong number/type of parameters
- **Valid tool, incorrect parameter values**: right structure, wrong values
- **Goal failure**: plan doesn't solve the task or violates constraints (wrong destination, over budget)
- **Time failure**: agent finishes after the deadline
- **Reflection errors**: agent falsely believes task is complete (assigns 40/50 people, insists it's done)

### Planning evaluation metrics
1. % of valid plans generated
2. Average plans needed to get a valid one
3. % of valid tool calls
4. Frequency of invalid tools, invalid parameters, incorrect values

### Tool failures
- Tool gives wrong output (bad image caption, wrong SQL)
- Translation errors (high-level plan → executable commands)
- Missing tools for the task domain

### Efficiency
- Steps to complete task
- Cost per task
- Time per action

Compare to baseline (another agent or human operator), noting different efficiency profiles.
