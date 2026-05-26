---
type: framework
tags: [training-data, data-formats, finetuning, chain-of-thought, tool-use]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-curation
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Training Data Formats by Task

Different training phases and objectives require different data structures:

| Training type | Data format |
|---|---|
| Self-supervised finetuning | Sequences of tokens |
| Instruction finetuning | (instruction, response) |
| Preference finetuning | (instruction, winning response, losing response) |
| Reward model training | ((instruction, response), score) |
| Chain-of-Thought training | (instruction, step-by-step reasoning + answer) |
| Tool use training | Multi-message format with headers specifying source/destination + special termination tokens |
| Multi-turn | Purpose-built conversation scenarios with clarification and correction turns |

**CoT data** is scarce because explaining step-by-step is much harder than providing final answers.

**Tool use data** is challenging because human tool-use patterns differ from optimal AI patterns (humans prefer GUIs; models prefer APIs). Llama 3 designed a multi-message chat format with message headers and special tokens to handle tool calls within conversations.

**Quantity units differ:** pre-training measures in tokens; SFT measures in examples.
