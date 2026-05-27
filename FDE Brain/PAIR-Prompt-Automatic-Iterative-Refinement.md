---
type: method
status: evergreen
aliases:
  - PAIR (Prompt Automatic Iterative Refinement)
  - AI-Powered Attack Loop
tags:
  - ai-engineering
  - testing
  - security
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/106-jailbreaking-and-prompt-injection.md
    locator: pages 262-266
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - PAIR uses an AI model to act as an attacker. This attacker AI is tasked with an objective...
      - 1. Generate a prompt. 2. Send the prompt to the target AI. 3. Based on the response from the target, revise the prompt until the objective is achieved.
created: 2026-05-26T21:55:46.006486+00:00
updated: 2026-05-26T21:55:46.006486+00:00
ingestion_run: 8d527d59
---

# PAIR (Prompt Automatic Iterative Refinement)

## Summary

A systematic, automated approach to generating jailbreaks where an attacker AI iteratively refines prompts based on the target AI's responses until the objective (e.g., eliciting objectionable content) is achieved.

## Core Idea

This method models AI safety as an iterative optimization problem. The attacker AI acts as a feedback loop, generating, testing, and refining prompts far faster than a human attacker.

## Practical Use

When red-teaming or stress-testing a model, adopt an automated, iterative approach. Use a secondary LLM (the 'attacker') to systematically generate and test prompt variations against the target model, simulating a continuous attack cycle.

## Related

- Red Teaming
- Adversarial Testing
