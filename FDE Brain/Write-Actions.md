---
type: pattern
status: evergreen
aliases:
  - Write Actions
  - Tool Use
  - Environment Interaction
tags:
  - ai-engineering
  - automation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/171-step-5.-add-agent-patterns.md
    locator: pages 487-488
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A model’s outputs also can be used to invoke write actions, such as composing an email, placing an order, or initializing a bank transfer.
      - Write actions allow a system to make changes to its environment directly.
      - Giving a model access to write actions should be done with the utmost care.
created: 2026-05-26T21:55:46.542214+00:00
updated: 2026-05-26T21:55:46.542214+00:00
ingestion_run: 8d527d59
---

# Write Actions

## Summary

The capability for an AI model's output to invoke external write actions, allowing the system to directly make changes to its environment (e.g., composing emails, placing orders, initializing bank transfers).

## Core Idea

Write actions transform an AI system from a purely informational tool into an active agent. While vastly increasing capability, they also significantly increase the system's risk profile and require careful implementation.

## Practical Use

Integrate write actions when the goal of the AI system is not just to inform, but to execute a transaction or modify a state in an external system (e.g., booking a flight, updating a CRM record). Always implement guardrails and human review for high-risk actions.

## Related

- [[Agentic-Patterns|Agentic Patterns]]
- Risk Management
