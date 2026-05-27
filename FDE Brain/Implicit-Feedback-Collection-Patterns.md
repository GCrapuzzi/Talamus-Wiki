---
type: pattern
status: evergreen
aliases:
  - Implicit Feedback Collection Patterns
  - Behavioral signal extraction
  - User collaboration loops
tags:
  - ai-engineering
  - implementation-method
  - data-collection
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/176-feedback-design.md
    locator: pages 504-513
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the model wrongly categorizes a product, users can edit the category.
      - Inpainting allows users to select a region and describe how to make it better.
      - Rephrasing a question after sharing a link may indicate unmet expectations.
created: 2026-05-26T21:55:46.578200+00:00
updated: 2026-05-26T21:55:46.578200+00:00
ingestion_run: 8d527d59
---

# Implicit Feedback Collection Patterns

## Summary

Methods for gathering high-quality feedback by allowing users to interact with and correct AI outputs, rather than requiring them to fill out forms.

## Core Idea

The most valuable feedback is often embedded in the user's attempt to complete a task. By making the user 'collaborate' with the AI, the system gains actionable data on failure modes and desired improvements.

## Practical Use

Implement features that allow user correction or refinement: 1. **Editing/Correction:** If the model miscategorizes a product, allow the user to edit the category. 2. **Inpainting/Region Selection:** For image generation, allow the user to select a specific region and prompt for modification (e.g., DALL-E inpainting). 3. **Rephrasing/Refinement:** If the user rephrases a question after sharing a link, treat this as a signal that the initial response was insufficient.

## Related

- [[Feedback-Collection-Timing-Framework|Feedback Collection Timing Framework]]
- AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf#Figure 10-14
