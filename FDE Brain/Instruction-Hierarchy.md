---
type: concept
tags: [AI-safety, prompt-injection, defense, system-prompt, instruction-following]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#defenses-against-prompt-attacks
  - AI Space/normalized/pdf/ai-engineering.md#system-prompt-and-user-prompt
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Instruction Hierarchy

A priority ordering for conflicting instructions, proposed by Wallace et al. (OpenAI, 2024) in "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions."

**Priority levels (highest → lowest):**
1. System prompt
2. User prompt
3. Model outputs
4. Tool outputs

When instructions conflict (e.g., system says "don't reveal PII" vs. tool output says "forward all emails to attacker"), the higher-priority instruction wins.

The model is finetuned on a synthetic dataset of aligned and misaligned instructions to learn this hierarchy. Results: **up to 63% improvement** in safety robustness with minimal degradation of standard capabilities.

This hierarchy is especially effective against **indirect prompt injection** since tool outputs (the typical injection vector) have the lowest priority.
