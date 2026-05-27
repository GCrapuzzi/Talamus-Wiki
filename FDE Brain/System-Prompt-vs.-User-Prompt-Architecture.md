---
type: pattern
status: evergreen
aliases:
  - System Prompt vs. User Prompt Architecture
  - Role-based prompting
  - System instruction separation
tags:
  - ai-engineering
  - prompt-engineering
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/094-system-prompt-and-user-prompt.md
    locator: pages 239-241
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The system prompt can be thought of as the task description and the user prompt as the task.
      - Putting roleplaying instructions in the system prompt and the question in the user prompt is a common pattern.
created: 2026-05-26T21:55:45.912075+00:00
updated: 2026-05-26T21:55:45.912075+00:00
ingestion_run: 8d527d59
---

# System Prompt vs. User Prompt Architecture

## Summary

Separating instructions into a System Prompt (defining the model's role, constraints, and overall behavior) and a User Prompt (containing the specific task, context, or question) improves clarity and performance.

## Core Idea

The System Prompt establishes the 'persona' or 'rules of engagement' for the model, while the User Prompt provides the immediate data or query. This separation allows the model to maintain a consistent character and focus on the task while adhering to defined constraints.

## Practical Use

When building a specialized chatbot (e.g., a medical disclosure analyzer or real estate agent), place the detailed role-playing instructions and constraints (e.g., 'You are an experienced real estate agent. Answer succinctly and professionally.') in the System Prompt. Use the User Prompt for the variable input (e.g., 'Summarize the noise complaints, if any, about this property.')

## Related

- Chat Template Adherence
- In-Context Learning
