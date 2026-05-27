---
type: pattern
status: evergreen
aliases:
  - Tool-Augmented AI
  - Function Calling
  - Tool Use
tags:
  - ai-engineering
  - llm-development
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/117-agent-overview.md
    locator: pages 300-301
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The set of actions an AI agent can perform is augmented by the tools it has access to.
      - ChatGPT is an agent. It can search the web, execute Python code, and generate images. RAG systems are agents, and text retrievers, image retrievers, and SQL executors are their tools.
created: 2026-05-26T21:55:46.089916+00:00
updated: 2026-05-26T21:55:46.089916+00:00
ingestion_run: 8d527d59
---

# Tool-Augmented AI

## Summary

The practice of equipping a generative AI model with external, specialized functions (tools) to extend its capabilities beyond pure text generation (e.g., web search, code execution, database querying).

## Core Idea

Tools transform a language model from a knowledge source into an active problem-solver. The model's role shifts from merely generating text to generating structured calls (JSON/API calls) that interact with the external world.

## Practical Use

Implement tool use by defining clear function signatures (name, description, required parameters) and instructing the LLM to output these structured calls when external data or computation is required.

## Related

- [[AI-Agent-Definition-and-Components|AI Agent Definition and Components]]
- [[Agent-Planning-Cycle-Reasoning-Loop|Agent Planning Cycle (Reasoning Loop)]]
