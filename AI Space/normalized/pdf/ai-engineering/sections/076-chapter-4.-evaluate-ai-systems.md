---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 076
section-title: Chapter 4. Evaluate AI Systems
source-location: pages 183-183
previous-section: AI Space/normalized/pdf/ai-engineering/sections/075-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/077-evaluation-criteria.md
classification: reusable-knowledge-candidate
---
# Chapter 4. Evaluate AI Systems

CHAPTER 4
Evaluate AI Systems
A model is only useful if it works for its intended purposes. You need to evaluate
models in the context of your application. Chapter 3 discusses different approaches
to automatic evaluation. This chapter discusses how to use these approaches to evalu‐
ate models for your applications.
This chapter contains three parts. It starts with a discussion of the criteria you might
use to evaluate your applications and how these criteria are defined and calculated.
For example, many people worry about AI making up facts—how is factual consis‐
tency detected? How are domain-specific capabilities like math, science, reasoning,
and summarization measured?
The second part focuses on model selection. Given an increasing number of founda‐
tion models to choose from, it can feel overwhelming to choose the right model for
your application. Thousands of benchmarks have been introduced to evaluate these
models along different criteria. Can these benchmarks be trusted? How do you select
what benchmarks to use? How about public leaderboards that aggregate multiple
benchmarks?
The model landscape is teeming with proprietary models and open source models. A
question many teams will need to visit over and over again is whether to host their
own models or to use a model API. This question has become more nuanced with the
introduction of model API services built on top of open source models.
The last part discusses developing an evaluation pipeline that can guide the develop‐
ment of your application over time. This part brings together the techniques we’ve
learned throughout the book to evaluate concrete applications.
