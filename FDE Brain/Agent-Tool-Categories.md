---
type: framework
tags: [agents, tools, function-calling, capability-extension, knowledge-augmentation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#tools
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Agent Tool Categories

Three categories of tools to consider for an agent's inventory:

### 1. Knowledge Augmentation (Context Construction)
Tools that give the agent information: text retriever, image retriever, SQL executor, people search, inventory API, Slack retrieval, email reader, **web browsing** (search APIs, news APIs, GitHub APIs, social media APIs). Prevents model staleness.

### 2. Capability Extension
Tools that address inherent model limitations:
- Simple: calculator, calendar, timezone converter, unit converter, translator
- Complex: **code interpreters** (enable coding assistance, data analysis, experiment running — but risk code injection)
- **Modality bridging**: text-to-image models (e.g., DALL-E), image captioning, transcription, OCR, LaTeX compiler, browser rendering

Chameleon (Lu et al., 2023): GPT-4 + 13 tools outperformed GPT-4 alone by 11.37% on ScienceQA and 17% on TabMWP.

### 3. Write Actions
Tools that modify the environment: send emails, initiate transfers, update databases, merge code changes. Enable full workflow automation but require trust in system reliability and security.

**Read-only actions** perceive the environment; **write actions** change it.
