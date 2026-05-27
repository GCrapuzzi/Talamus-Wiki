---
type: pattern
status: evergreen
aliases:
  - Agentic Systems
  - Intelligent Agents
  - Autonomous Agents
  - Tool-Using LLMs
tags:
  - ai-engineering
  - agentic
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/116-agents.md
    locator: pages 299-299
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Tool use is a core characteristic of the agentic pattern.
      - Intelligent agents are considered by many to be the ultimate goal of AI.
      - Agents can help us create a website, gather data, plan a trip, do market research, manage a customer account, automate data entry, prepare us for interviews, interview our candidates, negotiate a deal, etc.
created: 2026-05-26T21:55:46.079716+00:00
updated: 2026-05-26T21:55:46.079716+00:00
ingestion_run: 8d527d59
---

# Agentic Systems

## Summary

A system architecture where a Large Language Model (LLM) operates autonomously by utilizing a defined set of external tools, planning multi-step workflows, and iterating until a complex goal is achieved.

## Core Idea

Agentic systems represent the evolution from single-prompt responses to goal-oriented, multi-step execution. They matter because they enable LLMs to perform complex, real-world tasks (e.g., market research, data entry, booking) that require external data access, planning, and sequential reasoning, moving AI toward autonomous capability.

## Practical Use

Design a workflow where the LLM acts as a planner: 1) Receive a high-level goal. 2) Determine necessary tools/APIs (e.g., database query, web search, calculator). 3) Execute the tools sequentially. 4) Synthesize the final, actionable response. For data retrieval, implement intermediate steps (like predicting necessary tables for Text-to-SQL) to manage context window limitations.

## Related

- Tool Use
- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
- Planning and Reasoning
