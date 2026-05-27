---
type: concept
status: evergreen
aliases:
  - Planning Failure Modes
  - Agent Planning Errors
  - Goal Misalignment Failures
tags:
  - ai-engineering
  - planning
  - agent-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
    locator: pages 322-323
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Invalid tool: ...it generates a plan that contains bing_search, but bing_search isn’t in the agent’s tool inventory."
      - "Valid tool, invalid parameters: ...requires only one parameter, lbs."
      - "Valid tool, incorrect parameter values: ...uses the value 100 for lbs when it should be 120."
      - "Goal failure: the agent fails to achieve the goal."
      - A common constraint that is often overlooked by agent evaluation is time.
      - "errors in reflection: The agent is convinced that it’s accomplished a task when it hasn’t."
created: 2026-05-26T21:55:46.122942+00:00
updated: 2026-05-26T21:55:46.122942+00:00
ingestion_run: 8d527d59
---

# Planning Failure Modes

## Summary

Specific ways an agent's planning process can fail, ranging from structural errors in tool calls to conceptual failures in achieving the overall objective.

## Core Idea

Planning failures are often localized to the interaction between the plan and the environment/tools. Identifying these specific failure types allows engineers to improve the planning module (e.g., better constraints, more examples).

## Practical Use

When an agent fails to plan, first check the type of failure: Is it a syntax error (invalid tool/parameters)? Or is it a semantic error (goal failure/time constraint)? This dictates whether the fix is prompt engineering or system redesign.

## Related

- [[Agent-Failure-Mode-Taxonomy|Agent Failure Mode Taxonomy]]
- Goal Failure
