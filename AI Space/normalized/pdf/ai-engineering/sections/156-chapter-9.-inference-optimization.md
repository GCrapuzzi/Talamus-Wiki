---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 156
section-title: Chapter 9. Inference Optimization
source-location: pages 429-429
previous-section: AI Space/normalized/pdf/ai-engineering/sections/155-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/157-understanding-inference-optimization.md
classification: reusable-knowledge-candidate
---
# Chapter 9. Inference Optimization

CHAPTER 9
Inference Optimization
New models come and go, but one thing will always remain relevant: making them
better, cheaper, and faster. Up until now, the book has discussed various techniques
for making models better. This chapter focuses on making them faster and cheaper.
No matter how good your model is, if it’s too slow, your users might lose patience, or
worse, its predictions might become useless—imagine a next-day stock price predic‐
tion model that takes two days to compute each outcome. If your model is too expen‐
sive, its return on investment won’t be worth it.
Inference optimization can be done at the model, hardware, and service levels. At the
model level, you can reduce a trained model’s size or develop more efficient architec‐
tures, such as one without the computation bottlenecks in the attention mechanism
often used in transformer models. At the hardware level, you can design more power‐
ful hardware.
The inference service runs the model on the given hardware to accommodate user
requests. It can incorporate techniques that optimize models for specific hardware. It
also needs to consider usage and traffic patterns to efficiently allocate resources to
reduce latency and cost.
Because of this, inference optimization is an interdisciplinary field that often sees col‐
laboration among model researchers, application developers, system engineers, com‐
piler designers, hardware architects, and even data center operators.
This chapter discusses bottlenecks for AI inference and techniques to overcome
them. It’ll focus mostly on optimization at the model and service levels, with an over‐
view of AI accelerators.
