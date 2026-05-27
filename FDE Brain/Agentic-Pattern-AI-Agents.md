---
type: pattern
status: evergreen
aliases:
  - Agentic Pattern (AI Agents)
  - AI Agents
tags:
  - ai-engineering
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/110-chapter-6.-rag-and-agents.md
    locator: pages 277-277
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The agentic pattern allows the model to use tools such as web search and news APIs to gather information.
      - External tools can help models address their shortcomings and expand their capabilities.
      - They give models the ability to directly interact with the world, enabling them to automate many aspects of our lives.
created: 2026-05-26T21:55:46.037806+00:00
updated: 2026-05-26T21:55:46.037806+00:00
ingestion_run: 8d527d59
---

# Agentic Pattern (AI Agents)

## Summary

A pattern allowing models to use external tools (such as web search or APIs) to gather information, interact with the world, and automate complex tasks.

## Core Idea

Agents expand model capabilities beyond simple text generation by giving them the ability to act, interact with external systems, and solve multi-step problems, addressing inherent model shortcomings.

## Practical Use

Building an automated workflow that requires multiple steps, such as searching the web for current news, processing the results, and then generating a structured summary report.

## Related

- Tool Use
- Orchestration
