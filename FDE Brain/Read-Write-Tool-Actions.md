---
type: pattern
status: evergreen
aliases:
  - Read-Write Tool Actions
  - State Modification Tools
  - Actionable Tools
tags:
  - ai-engineering
  - security
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
    locator: pages 302-304
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Actions that allow an agent to perceive the environment are read-only actions, whereas actions that allow an agent to act upon the environment are write actions.
      - A SQL executor can retrieve a data table (read) but can also change or delete the table.
created: 2026-05-26T21:55:46.107822+00:00
updated: 2026-05-26T21:55:46.107822+00:00
ingestion_run: 8d527d59
---

# Read-Write Tool Actions

## Summary

Tools that allow the agent not only to perceive data (read) but also to modify or create data within the environment (write).

## Core Idea

While read-only tools are common for information retrieval, write actions give the agent the ability to perform impactful, state-changing tasks (e.g., updating a database record, sending an email). This increases utility but demands the highest level of security and validation.

## Practical Use

Implement write actions only after rigorous human-in-the-loop validation or when the task criticality is extremely high. Use transaction logging and rollback mechanisms to ensure data integrity.

## Related

- SQL Executor Tool
- System Integration
