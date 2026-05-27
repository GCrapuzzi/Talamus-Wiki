---
type: method
status: evergreen
aliases:
  - Tool Use Data Generation
  - API Interaction Data
  - Agent Workflow Data
tags:
  - agent-engineering
  - data-curation
  - tool-use
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For example, if you want data to finetune a model to act as a personal assistant, you might want to ask professional personal assistants what types of tasks they usually perform, how they perform them, and what tools they need.
      - many rely on simulations and other synthetic techniques to generate tool use data
created: 2026-05-26T21:55:46.309381+00:00
updated: 2026-05-26T21:55:46.309381+00:00
ingestion_run: 8d527d59
---

# Tool Use Data Generation

## Summary

Creating specialized data that demonstrates how an AI agent should use external tools (e.g., APIs, code interpreters) to complete a task, including the sequence of actions and messages.

## Core Idea

Tool use requires structured data that goes beyond simple text turns, often involving multiple messages sent to different destinations (e.g., user, code interpreter) within a single turn.

## Practical Use

When training an agent to interact with external systems, use simulated or expert-generated data that specifies the tool call, the input parameters, and the subsequent interpretation of the tool's output.

## Related

- [[Multi-Message-Chat-Format|Multi-Message Chat Format]]
