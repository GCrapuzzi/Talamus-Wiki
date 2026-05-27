---
type: method
status: evergreen
aliases:
  - Prompt Construction Validation Playbook
  - Prompt Debugging Checklist
  - Pre-flight Prompt Check
tags:
  - ai-engineering
  - llm-ops
  - debugging
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/094-system-prompt-and-user-prompt.md
    locator: pages 239-241
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you use a third-party tool to construct prompts, verify that this tool uses the correct chat template.
      - Before sending a query to a model, print out the final prompt to double-check if it follows the expected template.
created: 2026-05-26T21:55:45.916799+00:00
updated: 2026-05-26T21:55:45.916799+00:00
ingestion_run: 8d527d59
---

# Prompt Construction Validation Playbook

## Summary

A mandatory three-step process to ensure prompt integrity before sending a query to a foundation model, minimizing template-related failures.

## Core Idea

Template errors are common and often cause 'silent failures' (the model does something reasonable even if the template is wrong). This playbook forces verification at the input stage to catch structural errors.

## Practical Use

1. **Tool Verification:** If using a third-party tool, verify its use of the correct chat template. 2. **Input Construction:** Ensure all inputs (system, user, context) are correctly formatted according to the model's documentation. 3. **Final Output Check:** Before API call, print the final, concatenated prompt string to visually confirm it matches the expected template structure.

## Related

- [[Chat-Template-Adherence-Protocol|Chat Template Adherence Protocol]]
