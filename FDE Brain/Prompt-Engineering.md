---
type: method
status: evergreen
aliases:
  - Prompt Engineering
  - Instruction Crafting
  - LLM Prompting Best Practices
tags:
  - ai-engineering
  - prompting
  - llm-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/109-summary.md
    locator: pages 275-276
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The process of crafting an instruction to get a model to do what you want is called prompt engineering.
      - clear instructions with examples and relevant information are essential.
      - Simple tricks like asking the model to slow down and think step by step can yield surprising improvements.
created: 2026-05-26T21:55:46.031656+00:00
updated: 2026-05-26T21:55:46.031656+00:00
ingestion_run: 8d527d59
---

# Prompt Engineering

## Summary

The systematic process of crafting clear, detailed instructions and providing relevant examples to guide a foundation model toward a desired, predictable output.

## Core Idea

LLMs are highly sensitive to prompt phrasing. Effective prompting requires treating the interaction as structured human-AI communication, moving beyond simple queries to detailed instructions that specify format, tone, and constraints.

## Practical Use

When designing a prompt, always include: 1. A clear role/persona for the model. 2. Specific constraints (e.g., 'Do not exceed 3 bullet points'). 3. Few-shot examples (input/desired output pairs). 4. Techniques like 'think step-by-step' to force chain-of-thought reasoning.

## Related

- [[Contextual-Grounding|Contextual Grounding]]
- Chain-of-Thought Prompting
