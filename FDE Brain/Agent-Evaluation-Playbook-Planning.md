---
type: method
status: evergreen
aliases:
  - Agent Evaluation Playbook (Planning)
  - Agent Planning Benchmarking
  - Planning Dataset Metrics
tags:
  - ai-engineering
  - evaluation
  - benchmarking
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
    locator: pages 322-323
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To evaluate an agent for planning failures, one option is to create a planning dataset where each example is a tuple (task, tool inventory).
      - "Compute the following metrics: 1. Out of all generated plans, how many are valid? 2. For a given task, how many plans does the agent have to generate, on average, to get a valid plan? 3. Out of all tool calls, how many are valid? 4. How often are invalid tools called? 5. How often are valid tools called with invalid parameters? 6. How often are valid tools called with incorrect parameter values?"
created: 2026-05-26T21:55:46.127626+00:00
updated: 2026-05-26T21:55:46.127626+00:00
ingestion_run: 8d527d59
---

# Agent Evaluation Playbook (Planning)

## Summary

A structured, quantitative methodology for evaluating an agent's planning capabilities using a dedicated dataset (task, tool inventory).

## Core Idea

Evaluation must move beyond simple pass/fail. By generating multiple plans (K plans) for a given task, engineers can calculate specific failure rates, pinpointing the weakest links in the agent's reasoning chain.

## Practical Use

To benchmark an agent: 1. Create a dataset of (task, tool inventory). 2. For each task, generate K plans. 3. Calculate the following metrics to quantify failure rates: [List of 6 metrics]. 4. Analyze patterns to identify consistently difficult tools or task types.

## Related

- [[Agent-Failure-Mode-Taxonomy|Agent Failure Mode Taxonomy]]
- [[Tool-Use-Failure-Modes|Tool Use Failure Modes]]
