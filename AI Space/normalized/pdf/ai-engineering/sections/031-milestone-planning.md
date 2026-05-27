---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 031
section-title: Milestone Planning
source-location: pages 57-57
previous-section: AI Space/normalized/pdf/ai-engineering/sections/030-setting-expectations.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/032-maintenance.md
classification: reusable-knowledge-candidate
---
# Milestone Planning

A chatbot can answer more messages, but that doesn’t mean it’ll make users happy,
so it’s important to track customer satisfaction and customer feedback in general.
“User Feedback” on page 474  discusses how to design a feedback system.
To ensure a product isn’t put in front of customers before it’s ready, have clear
expectations on its usefulness threshold: how good it has to be for it to be useful. Use‐
fulness thresholds might include the following metrics groups:
• Quality metrics to measure the quality of the chatbot’s responses.
• Latency metrics including TTFT (time to first token), TPOT (time per output
token), and total latency. What is considered acceptable latency depends on your
use case. If all of your customer requests are currently being processed by
humans with a median response time of an hour, anything faster than this might
be good enough.
• Cost metrics: how much it costs per inference request.
• Other metrics such as interpretability and fairness.
If you’re not yet sure what metrics you want to use, don’t worry. The rest of the book
will cover many of these metrics.
Milestone Planning
Once you’ve set measurable goals, you need a plan to achieve these goals. How to get
to the goals depends on where you start. Evaluate existing models to understand their
capabilities. The stronger the off-the-shelf models, the less work you’ll have to do. For
example, if your goal is to automate 60% of customer support tickets and the off-theshelf model you want to use can already automate 30% of the tickets, the effort you
need to put in might be less than if it can automate no tickets at all.
It’s likely that your goals will change after evaluation. For example, after evaluation,
you may realize that the resources needed to get the app to the usefulness threshold
will be more than its potential return, and, therefore, you no longer want to pursue it.
Planning an AI product needs to account for its last mile challenge. Initial success
with foundation models can be misleading. As the base capabilities of foundation
models are already quite impressive, it might not take much time to build a fun
demo. However, a good initial demo doesn’t promise a good end product. It might
take a weekend to build a demo but months, and even years, to build a product.
In the paper UltraChat, Ding et al. (2023)  shared that “the journey from 0 to 60 is
easy, whereas progressing from 60 to 100 becomes exceedingly challenging.”
LinkedIn (2024) shared the same sentiment. It took them one month to achieve 80%
of the experience they wanted. This initial success made them grossly underestimate
how much time it’d take them to improve the product. They found it took them four
Planning AI Applications | 33
