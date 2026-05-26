---
type: framework
tags: [prompt-engineering, system-prompt, chat-template, prompt-structure]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#introduction-to-prompting
  - AI Space/normalized/pdf/ai-engineering.md#system-prompt-and-user-prompt
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Anatomy

A prompt generally consists of three parts:

| Component | Purpose | Example |
|---|---|---|
| **Task description** | What the model should do, its role, output format | "Extract all entities. Output comma-separated list." |
| **Example(s)** | Demonstrations of desired input→output behavior | NER few-shot pairs |
| **Task input** | The concrete instance to process | The text to extract entities from |

These map onto the API-level split:
- **System prompt** → task description + persona + constraints
- **User prompt** → task input + context

Under the hood, system and user prompts are concatenated into a single sequence via a **chat template** (model-specific). Any performance boost from system prompts likely comes from (1) positional advantage (instructions at the start) and (2) post-training that teaches the model to prioritize system-level instructions (see [[Instruction Hierarchy]]).

### Chat template hygiene
- Match the model's documented template exactly — wrong templates cause silent performance degradation.
- Verify third-party tools use the correct template; mismatches are common.
- Print the final assembled prompt before sending to catch formatting errors.
