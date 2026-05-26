---
type: method
tags: [tool-selection, agents, ablation, tool-transition]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#planning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Agent Tool Selection

Choosing the right tool inventory for an agent. More tools = more capabilities but harder to use effectively.

### Range in literature
- Toolformer: 5 tools
- Chameleon: 13 tools
- Gorilla: 1,645 APIs

### Selection techniques
- Compare agent performance across different tool sets
- **Ablation study**: remove tools one at a time; if performance doesn't drop, remove permanently
- Identify tools the agent frequently misuses — if unfixable via prompting/finetuning, swap for easier alternatives
- Plot **tool call distributions** to see most/least used tools
- Study **tool transitions**: after tool X, how likely is tool Y? Frequently co-used tools can be combined

### Key findings (Chameleon)
- Different tasks require different tools (ScienceQA relies on knowledge retrieval; TabMWP does not)
- Different models have different tool preferences (GPT-4 uses wider set; ChatGPT favors image captioning)

### Tool evolution
Agents can potentially compose new tools from existing ones. Voyager (Wang et al., 2023) maintains a **skill library** where successful tool compositions are stored for reuse.
