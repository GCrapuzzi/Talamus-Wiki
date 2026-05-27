---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 155
section-title: Summary
source-location: pages 427-428
previous-section: AI Space/normalized/pdf/ai-engineering/sections/154-format-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/156-chapter-9.-inference-optimization.md
classification: reusable-knowledge-candidate
---
# Summary

• “burger”: missing the end arrow
• “Item: burger -->”: extra prefix
• “burger --> ”: extra space appended
Summary
Even though the actual process of creating training data is incredibly intricate, the
principles of creating a dataset are surprisingly straightforward. To build a dataset to
train a model, you start by thinking through the behaviors you want your model to
learn and then design a dataset to show these behaviors. Due to the importance of
data, teams are introducing dedicated data roles responsible for acquiring appropri‐
ate datasets while ensuring privacy and compliance.
What data you need depends not only on your use case but also on the training
phase. Pre-training requires different data from instruction finetuning and preferred
finetuning. However, dataset design across training phases shares the same three core
criteria: quality, coverage, and quantity.
While how much data a model is trained on grabs headlines, having high-quality data
with sufficient coverage is just as important. A small amount of high-quality data can
outperform a large amount of noisy data. Similarly, many teams have found that
increasing the diversity of their datasets is key to improving their models’ perfor‐
mance.
Due to the challenge of acquiring high-quality data, many teams have turned to syn‐
thetic data. While generating data programmatically has long been a goal, it wasn’t
until AI could create realistic, complex data that synthetic data became a practical
solution for many more use cases. This chapter discussed different techniques for
data synthesis with a deep dive into synthesizing instruction data for finetuning.
Just like real data, synthetic data must be evaluated to ensure its quality before being
used to train models. Evaluating AI-generated data is just as tricky as evaluating
other AI outputs, and people are more likely to use generated data that they can relia‐
bly evaluate.
Data is challenging because many steps in dataset creation aren’t easily automatable.
It’s hard to annotate data, but it’s even harder to create annotation guidelines. It’s
hard to automate data generation, but it’s even harder to automate verifying it. While
data synthesis helps generate more data, you can’t automate thinking through what
data you want. You can’t easily automate annotation guidelines. You can’t automate
paying attention to details.
However, challenging problems lead to creative solutions. One thing that stood out to
me when doing research for this chapter is how much creativity is involved in dataset
Summary | 403

design. There are so many ways people construct and evaluate data. I hope that the
range of data synthesis and verification techniques discussed in this chapter will give
you inspiration for how to design your dataset.
Let’s say that you’ve curated a wonderful dataset that allows you to train an amazing
model. How should you serve this model? The next chapter will discuss how to opti‐
mize inference for latency and cost.
404 | Chapter 8: Dataset Engineering
