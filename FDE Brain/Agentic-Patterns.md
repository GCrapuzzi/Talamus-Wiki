---
type: pattern
status: evergreen
aliases:
  - Agentic Patterns
  - Complex Application Flow
  - Looping AI Agents
tags:
  - ai-engineering
  - agentic
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/171-step-5.-add-agent-patterns.md
    locator: pages 487-488
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - an application flow can be more complex with loops, parallel execution, and conditional branching.
      - after the system generates an output, it might determine that it hasn’t accomplished the task and that it needs to perform another retrieval to gather more information. This creates a loop.
created: 2026-05-26T21:55:46.540137+00:00
updated: 2026-05-26T21:55:46.540137+00:00
ingestion_run: 8d527d59
---

# Agentic Patterns

## Summary

Architectural patterns that enable AI applications to move beyond simple sequential queries by incorporating loops, conditional branching, and parallel execution, allowing the system to self-correct or gather more information iteratively.

## Core Idea

AI applications often require iterative reasoning (e.g., 'If X, then retrieve Y, then re-evaluate'). Agentic patterns formalize this feedback loop, allowing the model's output to feed back into the system for further processing or retrieval, enabling complex task completion.

## Practical Use

When building a system that requires multiple steps of reasoning or data gathering (e.g., a research assistant that needs to perform multiple searches and synthesize results), implement a loop where the model's output triggers a new retrieval or processing step.

## Related

- [[Write-Actions|Write Actions]]
- System Observability
