---
type: framework
status: evergreen
aliases:
  - Agent Tool Categorization Framework
  - Tool Function Taxonomy
  - Agent Capability Expansion Model
tags:
  - ai-engineering
  - architecture
  - tooling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
    locator: pages 302-304
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Actions that allow an agent to perceive the environment are read-only actions, whereas actions that allow an agent to act upon the environment are write actions.
      - "There are three categories of tools that you might want to consider: knowledge augmentation, capability extension, and tools that let your agent act upon its environment."
created: 2026-05-26T21:55:46.094652+00:00
updated: 2026-05-26T21:55:46.094652+00:00
ingestion_run: 8d527d59
---

# Agent Tool Categorization Framework

## Summary

A structured approach to classifying external tools based on their function: Knowledge Augmentation (Read-Only), Capability Extension (Computation/Utility), and Environment Action (Read/Write).

## Core Idea

Tools are not monolithic. Understanding their function (read-only perception, write action, or pure computation) allows engineers to strategically integrate them to address specific model limitations (e.g., math, currency, timeliness).

## Practical Use

Before integrating a tool, classify it: 1) Does it provide external data (Knowledge Augmentation)? 2) Does it solve a mathematical or logical limitation (Capability Extension)? 3) Does it modify state (Write Action)? This guides the planner's decision-making process.

## Related

- [[Read-Write-Tool-Actions|Read-Write Tool Actions]]
- Knowledge Augmentation
