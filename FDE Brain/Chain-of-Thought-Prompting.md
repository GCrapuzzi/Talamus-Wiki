---
type: method
tags: [prompt-engineering, chain-of-thought, reasoning, CoT, self-critique]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#give-the-model-time-to-think
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Chain-of-Thought Prompting

Explicitly ask the model to reason step-by-step before producing a final answer. Introduced by Wei et al. (2022), CoT improved performance across LaMDA, GPT-3, and PaLM on math and reasoning benchmarks. LinkedIn found CoT also **reduces hallucinations**.

### Variants
| Variant | Technique |
|---|---|
| **Zero-shot CoT** | Append "think step by step" or "explain your rationale" — model invents its own reasoning steps |
| **Zero-shot CoT (prescribed)** | Specify the exact steps: "1. Find X, 2. Find Y, 3. Compare" |
| **Few-shot CoT** | Include example(s) showing the desired reasoning chain |

### Complementary: Self-critique
Ask the model to review and verify its own output (also called self-eval). Nudges critical thinking similar to CoT.

### Trade-offs
- More reasoning tokens → higher latency and cost.
- Unpredictable length when the model invents steps on its own.
- Best suited for tasks where reasoning quality matters more than speed.
