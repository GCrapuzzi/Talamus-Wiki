---
type: concept
status: evergreen
aliases:
  - Intent Classification for Agents
  - Goal Scoping
  - Query Intent Analysis
tags:
  - ai-engineering
  - prompt-engineering
  - pre-processing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/119-planning.md
    locator: pages 305-321
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Planning requires understanding the intention behind a task: what’s the user trying to do with this query?"
      - The intent classification mechanism can be considered another agent in your multi-agent system.
created: 2026-05-26T21:55:46.115190+00:00
updated: 2026-05-26T21:55:46.115190+00:00
ingestion_run: 8d527d59
---

# Intent Classification for Agents

## Summary

The mechanism of using a dedicated model or prompt to determine the user's underlying goal, scope, and required domain knowledge from a natural language query before planning begins.

## Core Idea

Knowing the user's intent allows the agent to select the correct tools and constrain the planning process, preventing the agent from wasting computational resources on impossible or irrelevant solutions.

## Practical Use

Integrate an intent classifier as the first step in the agent workflow. If the classification is 'IRRELEVANT' or 'OUT OF SCOPE', the agent should politely reject the query instead of attempting a complex plan.

## Related

- [[Agent-Planning-Framework|Agent Planning Framework]]
- Tool Selection
