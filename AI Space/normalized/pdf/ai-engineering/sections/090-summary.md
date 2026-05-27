---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 090
section-title: Summary
source-location: pages 232-234
previous-section: AI Space/normalized/pdf/ai-engineering/sections/089-step-3.-define-evaluation-methods-and-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/091-chapter-5.-prompt-engineering.md
classification: reusable-knowledge-candidate
---
# Summary

29 For example, if there’s no correlation between a benchmark on translation and a benchmark on math, you
might be able to infer that improving a model’s translation capability has no impact on its math capability.
How correlated are your metrics?
As discussed in “Benchmark selection and aggregation” on page 191, if two met‐
rics are perfectly correlated, you don’t need both of them. On the other hand, if
two metrics are not at all correlated, this means either an interesting insight into
your model or that your metrics just aren’t trustworthy. 29
How much cost and latency does your evaluation pipeline add to your application?
Evaluation, if not done carefully, can add significant latency and cost to your
application. Some teams decide to skip evaluation in the hope of reducing
latency. It’s a risky bet.
Iterate
As your needs and user behaviors change, your evaluation criteria will also evolve,
and you’ll need to iterate on your evaluation pipeline. You might need to update the
evaluation criteria, change the scoring rubric, and add or remove examples. While
iteration is necessary, you should be able to expect a certain level of consistency from
your evaluation pipeline. If the evaluation process changes constantly, you won’t be
able to use the evaluation results to guide your application’s development.
As you iterate on your evaluation pipeline, make sure to do proper experiment track‐
ing: log all variables that could change in an evaluation process, including but not
limited to the evaluation data, the rubric, and the prompt and sampling configura‐
tions used for the AI judges.
Summary
This is one of the hardest, but I believe one of the most important, AI topics that I’ve
written about. Not having a reliable evaluation pipeline is one of the biggest blocks to
AI adoption. While evaluation takes time, a reliable evaluation pipeline will enable
you to reduce risks, discover opportunities to improve performance, and benchmark
progresses, which will all save you time and headaches down the line.
Given an increasing number of readily available foundation models, for most applica‐
tion developers, the challenge is no longer in developing models but in selecting the
right models for your application. This chapter discussed a list of criteria that are
often used to evaluate models for applications, and how they are evaluated. It dis‐
cussed how to evaluate both domain-specific capabilities and generation capabilities,
including factual consistency and safety. Many criteria to evaluate foundation models
evolved from traditional NLP, including fluency, coherence, and faithfulness.
208 | Chapter 4: Evaluate AI Systems

To help answer the question of whether to host a model or to use a model API, this
chapter outlined the pros and cons of each approach along seven axes, including data
privacy, data lineage, performance, functionality, control, and cost. This decision, like
all the build versus buy decisions, is unique to every team, depending not only on
what the team needs but also on what the team wants.
This chapter also explored the thousands of available public benchmarks. Public
benchmarks can help you weed out bad models, but they won’t help you find the best
models for your applications. Public benchmarks are also likely contaminated, as
their data is included in the training data of many models. There are public leader‐
boards that aggregate multiple benchmarks to rank models, but how benchmarks are
selected and aggregated is not a clear process. The lessons learned from public leader‐
boards are helpful for model selection, as model selection is akin to creating a private
leaderboard to rank models based on your needs.
This chapter ends with how to use all the evaluation techniques and criteria discussed
in the last chapter and how to create an evaluation pipeline for your application. No
perfect evaluation method exists. It’s impossible to capture the ability of a highdimensional system using one- or few-dimensional scores. Evaluating modern AI
systems has many limitations and biases. However, this doesn’t mean we shouldn’t
do it. Combining different methods and approaches can help mitigate many of these
challenges.
Even though dedicated discussions on evaluation end here, evaluation will come up
again and again, not just throughout the book but also throughout your application
development process. Chapter 6  explores evaluating retrieval and agentic systems,
while Chapters 7 and 9 focus on calculating a model’s memory usage, latency, and
costs. Data quality verification is addressed in Chapter 8, and using user feedback to
evaluate production applications is addressed in Chapter 10.
With that, let’s move onto the actual model adaptation process, starting with a topic
that many people associate with AI engineering: prompt engineering.
Summary | 209
