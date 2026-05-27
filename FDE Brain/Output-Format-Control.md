---
type: pattern
status: evergreen
aliases:
  - Output Format Control
  - Conciseness Directives
  - Preambles Suppression
tags:
  - ai-engineering
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/098-provide-sufficient-context.md
    locator: pages 247-247
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you want the model to be concise, tell it so.
      - If the model tends to begin its response with preambles such as 'Based on the content of this essay, I’d give it a score of...', make explicit that you don’t want preambles.
created: 2026-05-26T21:55:45.946687+00:00
updated: 2026-05-26T21:55:45.946687+00:00
ingestion_run: 8d527d59
---

# Output Format Control

## Summary

The practice of explicitly instructing the LLM on the desired length, tone, and structure of the response to prevent unnecessary preamble, verbosity, or boilerplate text.

## Core Idea

LLMs often default to conversational or explanatory tones, which can waste tokens and increase latency. Explicitly demanding conciseness or prohibiting preambles ensures the output is immediately usable by downstream systems.

## Practical Use

If the model tends to start responses with phrases like 'Based on the content of this essay...', include a negative constraint in the prompt: 'Do not include any introductory phrases, disclaimers, or preambles. Provide only the score.'

## Related

- System Prompting
- Token Efficiency
