---
type: concept
tags: [agents, ai-agent, tool-use, environment]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#agents
  - AI Space/normalized/pdf/ai-engineering.md#agent-overview
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Agent

An agent is anything that can **perceive its environment** and **act upon it**. Characterized by:
- **Environment**: defined by use case (game, internet, kitchen, road system)
- **Actions**: augmented by its tool inventory

In an AI agent, the AI model is the **brain** that processes information, plans action sequences, and determines task completion.

### Key properties
- Environment and tools are strongly coupled — environment determines possible tools; tools restrict operable environment
- Agents require more powerful models than non-agent use cases because of **compound mistakes** (95% per-step accuracy → 60% over 10 steps → 0.6% over 100 steps) and **higher stakes** from tool access
- Multi-step tasks take time and money, but autonomous agents can save human time

### Agent success depends on:
1. Tool inventory
2. Strength of AI planner

Examples: ChatGPT (web search, code execution, image generation), RAG systems (retrievers as tools), SWE-agent (file system navigation, search, editing).
