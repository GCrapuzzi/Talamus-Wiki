---
type: concept
tags: [prompt-engineering, robustness, model-evaluation, sensitivity]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#introduction-to-prompting
  - AI Space/normalized/pdf/ai-engineering.md#write-clear-and-explicit-instructions
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Robustness

How sensitive a model's output is to minor prompt perturbations — changing "5" to "five", adding a newline, altering capitalization.

Robustness is **strongly correlated with overall model capability**. Stronger models tolerate more variation, reducing the need for prompt fiddling. Weaker models require more precise wording.

**Measurement:** Randomly perturb prompts (synonym substitution, formatting changes, reordering) and measure output variance.

**Practical implication:** Investing in a stronger model can save more engineering time than perfecting prompts for a weaker one. Stanford dropped robustness from their HELM Lite benchmark in late 2023, reflecting that frontier models had largely solved this.
