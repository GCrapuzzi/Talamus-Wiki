---
type: framework
tags: [prompt-engineering, best-practices, output-format, persona, few-shot]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#prompt-engineering-best-practices
  - AI Space/normalized/pdf/ai-engineering.md#write-clear-and-explicit-instructions
  - AI Space/normalized/pdf/ai-engineering.md#provide-sufficient-context
  - AI Space/normalized/pdf/ai-engineering.md#iterate-on-your-prompts
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Engineering Best Practices

Distilled from OpenAI, Anthropic, Meta, and Google tutorials plus production deployment experience.

### 1. Write clear and explicit instructions
- **Remove ambiguity** — specify scoring scales, edge-case handling, whether to say "I don't know".
- **Assign a persona** — changes the evaluative perspective (a first-grade teacher scores differently than a college professor).
- **Provide examples** — reduces output ambiguity; prefer token-efficient example formats (`chickpea --> edible` over verbose `Input: chickpea\nOutput: edible`).
- **Specify output format** — ban preambles if unwanted; define JSON keys; use end-of-input markers to prevent the model from appending to the input instead of generating structured output.

### 2. Provide sufficient context
- Include reference material to reduce hallucination.
- To restrict the model to context-only answers: instruct it to quote sources, provide negative examples, say "answer using only the provided context". Note: prompting alone cannot guarantee compliance.

### 3. Break complex tasks into subtasks
See [[Prompt Decomposition]].

### 4. Give the model time to think
See [[Chain-of-Thought Prompting]].

### 5. Iterate systematically
- Version prompts. Use experiment tracking. Standardize eval metrics and data.
- Evaluate each prompt in the context of the whole system — a local improvement can degrade end-to-end performance.
- Read model-specific prompting guides; each model has unique quirks.
