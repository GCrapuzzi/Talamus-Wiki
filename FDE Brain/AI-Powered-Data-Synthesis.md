---
type: method
tags: [synthetic-data, data-synthesis, instruction-tuning, llama]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-powered-data-synthesis
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI-Powered Data Synthesis

Using AI models to generate training data at scale. Key techniques:

### Instruction Synthesis
- Generate instructions from topic/keyword lists or templates (both can be AI-generated)
- Generate responses per instruction (one or many)
- **Reverse instruction:** take existing high-quality content (books, Wikipedia) and generate prompts that would elicit it—avoids hallucinations in responses

### Augmentation via AI
- **Paraphrasing** — e.g., MetaMath rewrote 15K examples into ~400K, outperforming larger models
- **Translation** — cross-lingual and cross-programming-language transfer; quality verified via Back-Translation
- **Back-translation for code** — generate explanations from code, then regenerate code from explanations; keep only faithful pairs

### Self-Play
- AI agents play both sides (customer + support, chess opponents, negotiators)
- OpenAI's Dota 2 bot played ~180 years of games per day via self-play

### Simulation
- AI simulates API outcomes (StableToolBench) to avoid costly real calls
- Simulate tool-use action sequences, execute them, validate outcomes

### Llama 3 Coding Pipeline (comprehensive example)
1. AI generates problem descriptions across diverse topics
2. AI generates solutions per problem per language
3. AI generates unit tests to verify solutions
4. Failed solutions get AI-driven error correction with parser/linter/test feedback
5. Code translation to other languages (filtered by test passage)
6. Back-translation generates explanations/docs (filtered by faithfulness)

Result: 2.7M synthetic coding examples for Llama 3.1 SFT.
