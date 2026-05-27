---
type: pattern
status: evergreen
aliases:
  - Structured Code Example Conventions
  - Code Documentation Standards
  - Technical Writing for AI
tags:
  - ai-engineering
  - documentation
  - prompting
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/010-using-code-examples.md
    locator: pages 20-20
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Constant width is used for program listings, variable names, function names, and input prompts into models.
      - Constant width bold shows commands that should be typed literally by the user.
      - Constant width italic shows text that should be replaced with user-supplied values or by values determined by context.
created: 2026-05-26T21:55:45.308902+00:00
updated: 2026-05-26T21:55:45.308902+00:00
ingestion_run: 8d527d59
---

# Structured Code Example Conventions

## Summary

A set of conventions for differentiating code listings, literal commands, variables, and user-supplied inputs within technical documentation and prompts.

## Core Idea

Ambiguity in technical instructions is a major failure point. By establishing clear visual and structural conventions (e.g., constant width, bold, italic), engineers ensure that the reader knows whether a piece of text is fixed code, a variable placeholder, or a literal command to be typed.

## Practical Use

When documenting an AI pipeline or prompt template, use these conventions: 1. Use constant width for full code blocks and variable names. 2. Use constant width bold for literal commands (e.g., `run_script`). 3. Use constant width italic for placeholders that the user must supply (e.g., *[user_input_topic]*).

## Related

- [[Prompt-Engineering|Prompt Engineering]]
- Technical Documentation Best Practices
