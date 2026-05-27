---
type: framework
status: evergreen
aliases:
  - AI Agent Framework
  - Autonomous Agent
tags:
  - ai-engineering
  - agentic-systems
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/122-summary.md
    locator: pages 329-330
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The RAG pattern can be seen as a special case of agent where the retriever is a tool the model can use.
      - In an AI-powered agent, AI is the planner that analyzes its given task, considers different solutions, and picks the most promising one.
      - A complex task can require many steps to solve, which requires a powerful model to plan.
created: 2026-05-26T21:55:46.143520+00:00
updated: 2026-05-26T21:55:46.143520+00:00
ingestion_run: 8d527d59
---

# AI Agent Framework

## Summary

A system where the LLM acts as a planner, analyzing a complex task, considering multiple solutions, and executing steps using external tools and memory to achieve a goal.

## Core Idea

Agents elevate LLMs from simple prompt-response systems to goal-oriented problem solvers. They overcome context limitations by managing multi-step processes and utilizing external capabilities (tools).

## Practical Use

Design an agent when the task is complex, multi-step, and requires decision-making or interaction with external systems (e.g., booking travel, running complex data analysis pipelines). Engineers must prioritize robust defensive mechanisms due to the increased security risk associated with tool use.

## Related

- RAG
- Tool Use
- Memory System
