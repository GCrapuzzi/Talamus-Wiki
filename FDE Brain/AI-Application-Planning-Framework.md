---
type: framework
tags: [planning, use-case-evaluation, human-in-the-loop, last-mile, product-strategy]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#use-case-evaluation
  - AI Space/normalized/pdf/ai-engineering.md#setting-expectations
  - AI Space/normalized/pdf/ai-engineering.md#milestone-planning
  - AI Space/normalized/pdf/ai-engineering.md#maintenance
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Application Planning Framework

A structured approach to deciding whether and how to build an AI application.

### Use Case Evaluation
Three risk levels driving the decision:
1. **Existential threat** — competitors with AI can make you obsolete (7% of Gartner respondents). Common in document processing, creative work.
2. **Missed opportunity** — AI boosts profits/productivity across acquisition, retention, sales, internal ops.
3. **Strategic hedging** — unsure where AI fits but can't afford to be left behind.

### Role of AI in the Product
Three dimensions (per Apple's framework):
- **Critical vs complementary** — can the app work without AI? More critical → higher accuracy bar.
- **Reactive vs proactive** — reactive needs low latency; proactive needs higher quality (users didn't ask for it).
- **Dynamic vs static** — dynamic = continually updated per user; static = periodic model updates.

### Human-in-the-Loop
Microsoft's **Crawl-Walk-Run** framework for increasing automation:
1. Crawl: human involvement mandatory
2. Walk: AI interacts with internal employees
3. Run: AI interacts directly with external users

### The Last Mile Challenge
Initial demos are misleadingly easy. LinkedIn's experience: 1 month to 80% quality, then 4 more months to reach 95%. Each subsequent 1% gain is slower and more discouraging.

### Usefulness Threshold Metrics
- Quality, latency (TTFT, TPOT, total), cost, interpretability, fairness.
