---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 081
section-title: Cost and Latency
source-location: pages 201-202
previous-section: AI Space/normalized/pdf/ai-engineering/sections/080-instruction-following-capability.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/082-model-selection.md
classification: reusable-knowledge-candidate
---
# Cost and Latency

RoleLLM AI judge to rank models based on their ability to play a certain role. For the
full prompt, please check out Wang et al. (2023).
System Instruction:
You are a role−playing performance comparison assistant. You should rank
the models based on the role characteristics and text quality of their
responses. The rankings are then output using Python dictionaries and
lists.
User Prompt:
The models below are to play the role of ‘‘{role_name}’’. The role
description of ‘‘{role_name}’’ is ‘‘{role_description_and_catchphra
ses}’’. I need to rank the following models based on the two criteria
below:
1. Which one has more pronounced role speaking style, and speaks more in
line with the role description. The more distinctive the speaking style,
the better.
2. Which one’s output contains more knowledge and memories related to the
role; the richer, the better. (If the question contains reference
answers, then the role −specific knowledge and memories are based on the
reference answer.)
Cost and Latency
A model that generates high-quality outputs but is too slow and expensive to run will
not be useful. When evaluating models, it’s important to balance model quality,
latency, and cost. Many companies opt for lower-quality models if they provide bet‐
ter cost and latency. Cost and latency optimization are discussed in detail in Chap‐
ter 9, so this section will be quick.
Optimizing for multiple objectives is an active field of study called Pareto optimiza‐
tion. When optimizing for multiple objectives, it’s important to be clear about what
objectives you can and can’t compromise on. For example, if latency is something
you can’t compromise on, you start with latency expectations for different models,
filter out all the models that don’t meet your latency requirements, and then pick the
best among the rest.
There are multiple metrics for latency for foundation models, including but not limi‐
ted to time to first token, time per token, time between tokens, time per query, etc.
It’s important to understand what latency metrics matter to you.
Latency depends not only on the underlying model but also on each prompt and
sampling variables. Autoregressive language models typically generate outputs token
by token. The more tokens it has to generate, the higher the total latency. You can
control the total latency observed by users by careful prompting, such as instructing
Evaluation Criteria | 177

9 However, the electricity cost might be different, depending on the usage.
the model to be concise, setting a stopping condition for generation (discussed in
Chapter 2), or other optimization techniques (discussed in Chapter 9).
When evaluating models based on latency, it’s important to differ‐
entiate between the must-have and the nice-to-have. If you ask
users if they want lower latency, nobody will ever say no. But high
latency is often an annoyance, not a deal breaker.
If you use model APIs, they typically charge by tokens. The more input and output
tokens you use, the more expensive it is. Many applications then try to reduce the
input and output token count to manage cost.
If you host your own models, your cost, outside engineering cost, is compute. To
make the most out of the machines they have, many people choose the largest models
that can fit their machines. For example, GPUs usually come with 16 GB, 24 GB, 48
GB, and 80 GB of memory. Therefore, many popular models are those that max out
these memory configurations. It’s not a coincidence that many models today have 7
billion or 65 billion parameters.
If you use model APIs, your cost per token usually doesn’t change much as you scale.
However, if you host your own models, your cost per token can get much cheaper as
you scale. If you’ve already invested in a cluster that can serve a maximum of 1 billion
tokens a day, the compute cost remains the same whether you serve 1 million tokens
or 1 billion tokens a day. 9 Therefore, at different scales, companies need to reevaluate
whether it makes more sense to use model APIs or to host their own models.
Table 4-3 shows criteria you might use to evaluate models for your application. The
row scale is especially important when evaluating model APIs, because you need a
model API service that can support your scale.
Table 4-3. An example of criteria used to select models for a fictional application.
Criteria Metric Benchmark Hard requirement Ideal
Cost Cost per output token X < $30.00 /
1M tokens
< $15.00 /
1M tokens
Scale TPM (tokens per minute) X > 1M TPM > 1M TPM
Latency Time to first token (P90) Internal user prompt
dataset
< 200ms < 100ms
Latency Time per total query (P90) Internal user prompt
dataset
< 1m < 30s
Overall model
quality
Elo score Chatbot Arena’s
ranking
> 1200 > 1250
178 | Chapter 4: Evaluate AI Systems

[Visual content extracted via GLM-OCR]

the model to be concise, setting a stopping condition for generation (discussed in Chapter 2), or other optimization techniques (discussed in Chapter 9).

When evaluating models based on latency, it’s important to differentiate between the must-have and the nice-to-have. If you ask users if they want lower latency, nobody will ever say no. But high latency is often an annoyance, not a deal breaker.

If you use model APIs, they typically charge by tokens. The more input and output tokens you use, the more expensive it is. Many applications then try to reduce the input and output token count to manage cost.

If you host your own models, your cost, outside engineering cost, is compute. To make the most out of the machines they have, many people choose the largest models that can fit their machines. For example, GPUs usually come with 16 GB, 24 GB, 48 GB, and 80 GB of memory. Therefore, many popular models are those that max out these memory configurations. It’s not a coincidence that many models today have 7 billion or 65 billion parameters.

If you use model APIs, your cost per token usually doesn’t change much as you scale. However, if you host your own models, your cost per token can get much cheaper as you scale. If you’ve already invested in a cluster that can serve a maximum of 1 billion tokens a day, the compute cost remains the same whether you serve 1 million tokens or 1 billion tokens a day. Therefore, at different scales, companies need to reevaluate whether it makes more sense to use model APIs or to host their own models.

Table 4-3 shows criteria you might use to evaluate models for your application. The row scale is especially important when evaluating model APIs, because you need a model API service that can support your scale.

| Criteria | Metric | Benchmark | Hard requirement | Ideal |
| :--- | :--- | :--- | :--- | :--- |
| Cost | Cost per output token | X | < $30.00 / 1M tokens | < $15.00 / 1M tokens |
| Scale | TPM (tokens per minute) | X | > 1M TPM | > 1M TPM |
| Latency | Time to first token (P90) | Internal user prompt dataset | < 200ms | < 100ms |
| Latency | Time per total query (P90) | Internal user prompt dataset | < 1m | < 30s |
| Overall model quality | Elo score | Chatbot Arena’s ranking | > 1200 | > 1250 |

9 However, the electricity cost might be different, depending on the usage.
