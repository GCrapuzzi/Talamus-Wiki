---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 159
section-title: Inference Performance Metrics
source-location: pages 436-442
previous-section: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/160-ai-accelerators.md
classification: reusable-knowledge-candidate
---
# Inference Performance Metrics

7 As discussed in “Prompt caching” on page 443 , it’s common to know in advance the system prompt of an appli‐
cation. It’s just the exact user queries that are hard to predict.
8 In the early days of chatbots, some people complained about chatbots responding too fast, which seemed
unnatural. See “Lufthansa Delays Chatbot’s Responses to Make It More ‘Human’”  (Ry Crozier, iTnews, May
2017). However, as people become more familiar with chatbots, this is no longer the case.
A batch API for foundation models differs from batch inference for
traditional ML. In traditional ML:
• Online inference means that predictions are computed after
requests have arrived.
• Batch inference means that predictions are precomputed
before requests have arrived.
Precompution is possible for use cases with finite and predictable
inputs like recommendation systems, where recommendations can
be generated for all users in advance. These precomputed predic‐
tions are fetched when requests arrive, e.g., when a user visits the
website. However, with foundation model use cases where the
inputs are open-ended, it’s hard to predict all user prompts. 7
Inference Performance Metrics
Before jumping into optimization, it’s important to understand what metrics to opti‐
mize for. From the user perspective, the central axis is latency (response quality is a
property of the model itself, not of the inference service). However, application devel‐
opers must also consider throughput and utilization as they determine the cost of
their applications.
Latency, TTFT, and TPOT
Latency measures the time from when users send a query until they receive the com‐
plete response. For autoregressive generation, especially in the streaming mode, the
overall latency can be broken into several metrics:
Time to first token
TTFT measures how quickly the first token is generated after users send a query.
It corresponds to the duration of the prefill step and depends on the input’s
length. Users might have different expectations for TTFT for different applica‐
tions. For example, for conversational chatbots, the TTFT should be instantane‐
ous.8 However, users might be willing to wait longer to summarize long
documents.
412 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

A batch API for foundation models differs from batch inference for traditional ML. In traditional ML:

- Online inference means that predictions are computed after requests have arrived.
- Batch inference means that predictions are precomputed before requests have arrived.

Precomputation is possible for use cases with finite and predictable inputs like recommendation systems, where recommendations can be generated for all users in advance. These precomputed predictions are fetched when requests arrive, e.g., when a user visits the website. However, with foundation model use cases where the inputs are open-ended, it’s hard to predict all user prompts.$^7$

Inference Performance Metrics

Before jumping into optimization, it’s important to understand what metrics to optimize for. From the user perspective, the central axis is latency (response quality is a property of the model itself, not of the inference service). However, application developers must also consider throughput and utilization as they determine the cost of their applications.

Latency, TTFT, and TPOT

Latency measures the time from when users send a query until they receive the complete response. For autoregressive generation, especially in the streaming mode, the overall latency can be broken into several metrics:

Time to first token

TTFT measures how quickly the first token is generated after users send a query. It corresponds to the duration of the prefill step and depends on the input’s length. Users might have different expectations for TTFT for different applications. For example, for conversational chatbots, the TTFT should be instantaneous.$^8$ However, users might be willing to wait longer to summarize long documents.

$^7$ As discussed in “Prompt caching” on page 443, it’s common to know in advance the system prompt of an application. It’s just the exact user queries that are hard to predict.

$^8$ In the early days of chatbots, some people complained about chatbots responding too fast, which seemed unnatural. See “Lufthansa Delays Chatbot’s Responses to Make It More ‘Human’” (Ry Crozier, iTnews, May 2017). However, as people become more familiar with chatbots, this is no longer the case.

9 Time between tokens (TBT) is used by LinkedIn and inter-token latency (ITL) is used by NVIDIA.
10 An experiment by Anyscale shows that 100 input tokens have approximately the same impact on the overall
latency as a single output token.
Time per output token
TPOT measures how quickly each output token is generated after the first token.
If each token takes 100 ms, a response of 1,000 tokens will take 100 s.
In the streaming mode, where users read each token as it’s generated, TPOT
should be faster than human reading speed but doesn’t have to be much faster. A
very fast reader can read 120 ms/token, so a TPOT of around 120 ms, or 6–8
tokens/second, is sufficient for most use cases.
Time between tokens and inter-token latency
Variations of this metric include time between tokens (TBT)  and i nter-token
latency (ITL).9 Both measure the time between output tokens.
The total latency will equal TTFT + TPOT × (number of output tokens).
Two applications with the same total latency can offer different user experiences with
different TTFT and TPOT. Would your users prefer instant first tokens with a longer
wait between tokens, or would they rather wait slightly longer for the first tokens but
enjoy faster token generation afterward? User studies will be necessary to determine
the optimal user experience. Reducing TTFT at the cost of higher TPOT is possible
by shifting more compute instances from decoding to prefilling and vice versa.10
It’s important to note that the TTFT and TPOT values observed by users might differ
from those observed by models, especially in scenarios involving CoT (chain-ofthought) or agentic queries where models generate intermediate steps not shown to
users. Some teams use the metric time to publish  to make it explicit that it measures
time to the first token users see.
Consider the scenario where, after a user sends a query, the model performs the fol‐
lowing steps:
1. Generate a plan, which consists of a sequence of actions. This plan isn’t shown to
the user.
2. Take actions and log their outputs. These outputs aren’t shown to the user.
3. Based on these outputs, generate a final response to show the user.
Understanding Inference Optimization | 413

From the model’s perspective, the first token is generated in step 1. This is when the
model internally begins its token generation process. The user, however, only sees the
first token of the final output generated in step 3. Thus, from their perspective, TTFT
is much longer.
Because latency is a distribution, the average can be misleading. Imagine you have 10
requests whose TTFT values are 100 ms, 102 ms, 100 ms, 100 ms, 99 ms, 104 ms, 110
ms, 90 ms, 3,000 ms, 95 ms. The average TTFT value is 390 ms, which makes your
inference service seem slower than it is. There might have been a network error that
slowed down one request or a particularly long prompt that took a much longer time
to prefill. Either way, you should investigate. With a large volume of requests, outliers
that skew the average latency are almost inevitable.
It’s more helpful to look at latency in percentiles, as they tell you something about a
certain percentage of your requests. The most common percentile is the 50th percen‐
tile, abbreviated as p50 (median). If the median is 100 ms, half of the requests take
longer than 100 ms to generate the first token, and half take less than 100 ms. Percen‐
tiles also help you discover outliers, which might be symptoms of something wrong.
Typically, the percentiles you’ll want to look at are p90, p95, and p99. It’s also helpful
to plot TTFT values against inputs’ lengths.
Throughput and goodput
Throughput measures the number of output tokens per second an inference service
can generate across all users and requests.
Some teams count both input and output tokens in throughput calculation. However,
since processing input tokens (prefilling) and generating output tokens (decoding)
have different computational bottlenecks and are often decoupled in modern infer‐
ence servers, input and output throughput should be counted separately. When
throughput is used without any modifier, it usually refers to output tokens.
Throughput is typically measured as tokens/s (TPS). If you serve multiple users,
tokens/s/user is also used to evaluate how the system scales with more users.
Throughput can also be measured as the number of completed requests during a
given time. Many applications use requests per second (RPS). However, for applica‐
tions built on top of foundation models, a request might take seconds to complete, so
many people use completed requests per minute (RPM) instead. Tracking this metric
is useful for understanding how an inference service handles concurrent requests.
Some providers might throttle your service if you send too many concurrent requests
at the same time.
414 | Chapter 9: Inference Optimization

Throughput is directly linked to compute cost. A higher throughput typically means
lower cost. If your system costs $2/h in compute and its throughput is 100 tokens/s, it
costs around $5.556 per 1M output tokens. If each request generates 200 output
tokens on average, the cost for decoding 1K requests would be $1.11.
The prefill cost can be similarly calculated. If your hardware costs $2 per hour and it
can prefill 100 requests per minute, the cost for prefilling 1K requests would be $0.33.
The total cost per request is the sum of the prefilling and decoding costs. In this
example, the total cost for 1K requests would be $1.11 + $0.33 = $1.44.
What’s considered good throughput depends on the model, the hardware, and the
workload. Smaller models and higher-end chips typically result in higher throughput.
Workloads with consistent input and output lengths are easier to optimize than
workloads with variable lengths.
Even for similarly sized models, hardware, and workloads, direct throughput com‐
parisons might be only approximate because token count depends on what consti‐
tutes a token, and different models have different tokenizers. It’s better to compare
the efficiency of inference servers using metrics such as cost per request.
Just like most other software applications, AI applications have the latency/through‐
put trade-off. Techniques like batching can improve throughput but reduce latency.
According to the LinkedIn AI team in their reflection after a year of deploying gener‐
ative AI products ( LinkedIn, 2024 ), it’s not uncommon to double or triple the
throughput if you’re willing to sacrifice TTFT and TPOT.
Due to this trade-off, focusing on an inference service based solely on its throughput
and cost can lead to a bad user experience. Instead, some teams focus on goodput, a
metric adapted from networking for LLM applications. Goodput measures the num‐
ber of requests per second that satisfies the SLO, software-level objective.
Imagine that your application has the following objectives: TTFT of at most 200 ms
and TPOT of at most 100 ms. Let’s say that your inference service can complete 100
requests per minute. However, out of these 100 requests, only 30 satisfy the SLO.
Then, the goodput of this service is 30 requests per minute. A visualization of this is
shown in Figure 9-4.
Understanding Inference Optimization | 415

Figure 9-4. If an inference service can complete 10 RPS but only 3 satisfy the SLO, then
its goodput is 3 RPS.
Utilization, MFU, and MBU
Utilization metrics measure how efficiently a resource is being used. It typically
quantifies the proportion of the resource actively being used compared to its total
available capacity.
A common but often misunderstood metric is GPU utilization, and NVIDIA is parti‐
ally to blame for this misunderstanding. The official NVIDIA tool for monitoring
GPU usage is nvidia-smi—SMI stands for System Management Interface. One met‐
ric this tool shows is GPU utilization, which represents the percentage of time during
which the GPU is actively processing tasks. For example, if you run inference on a
GPU cluster for 10 hours, and the GPUs are actively processing tasks for 5 of those
hours, your GPU utilization would be 50%.
However, actively processing tasks doesn’t mean doing so efficiently. For simplicity,
consider a tiny GPU capable of doing 100 operations per second. In nvidia-smi’s
definition of utilization, this GPU can report 100% utilization even if it’s only doing
one operation per second.
If you pay for a machine that can do 100 operations and use it for only 1 operation,
you’re wasting money. nvidia-smi’s GPU optimization metric is, therefore, not very
useful. A utilization metric you might care about, out of all the operations a machine
is capable of computing, is how many it’s doing in a given time. This metric is called
416 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Utilization, MFU, and MBU

Utilization metrics measure how efficiently a resource is being used. It typically quantifies the proportion of the resource actively being used compared to its total available capacity.

A common but often misunderstood metric is GPU utilization, and NVIDIA is partially to blame for this misunderstanding. The official NVIDIA tool for monitoring GPU usage is nvidia-smi—SMI stands for System Management Interface. One metric this tool shows is GPU utilization, which represents the percentage of time during which the GPU is actively processing tasks. For example, if you run inference on a GPU cluster for 10 hours, and the GPUs are actively processing tasks for 5 of those hours, your GPU utilization would be 50%.

However, actively processing tasks doesn’t mean doing so efficiently. For simplicity, consider a tiny GPU capable of doing 100 operations per second. In nvidia-smi’s definition of utilization, this GPU can report 100% utilization even if it’s only doing one operation per second.

If you pay for a machine that can do 100 operations and use it for only 1 operation, you’re wasting money. nvidia-smi’s GPU optimization metric is, therefore, not very useful. A utilization metric you might care about, out of all the operations a machine is capable of computing, is how many it’s doing in a given time. This metric is called

11 People have cared about FLOP/s utilization for a long time, but the term MFU was introduced in the PaLM
paper (Chowdhery et al., 2022).
MFU (Model FLOP/s Utilization) , which distinguishes it from the NVIDIA GPU uti‐
lization metric.
MFU is the ratio of the observed throughput (tokens/s) relative to the theoretical
maximum throughput of a system operating at peak FLOP/s. If at the peak FLOP/s
advertised by the chip maker, the chip can generate 100 tokens/s, but when used for
your inference service, it can generate only 20 tokens/s, your MFU is 20%.11
Similarly, because memory bandwidth is expensive, you might also want to know
how efficiently your hardware’s bandwidth is utilized. MBU (Model Bandwidth Uti‐
lization) measures the percentage of achievable memory bandwidth used. If the chip’s
peak bandwidth is 1 TB/s and your inference uses only 500 GB/s, your MBU is 50%.
Computing the memory bandwidth being used for LLM inference is straightforward:
parameter count × bytes/param × tokens/s
MBU is computed as follows:
(parameter count × bytes/param × tokens/s) / (theoretical bandwidth)
For example, if you use a 7B-parameter model in FP16 (two bytes per parameter) and
achieve 100 tokens/s, the bandwidth used is:
7B × 2 × 100 = 700 GB/s
This underscores the importance of quantization (discussed in Chapter 7 ). Fewer
bytes per parameter mean your model consumes less valuable bandwidth.
If this is done on an A100-80GB GPU with a theoretical 2 TB/s of memory band‐
width, the MBU is:
(700 GB/s) / (2 TB/s) = 70%
The relationships between throughput (tokens/s) and MBU and between throughput
and MFU are linear, so some people might use throughput to refer to MBU and
MFU.
What’s considered a good MFU and MBU depends on the model, hardware, and
workload. Compute-bound workloads typically have higher MFU and lower MBU,
while bandwidth-bound workloads often show lower MFU and higher MBU.
Because training can benefit from more efficient optimization (e.g., better batching),
thanks to having more predictable workloads, MFU for training is typically higher
than MFU for inference. For inference, since prefill is compute-bound and decode is
memory bandwidth-bound, MFU during prefilling is typically higher than MFU dur‐
ing decoding. For model training, as of this writing, an MFU above 50% is generally
Understanding Inference Optimization | 417

considered good, but it can be hard to achieve on specific hardware. Table 9-1 shows MFU for several models and accelerators.

Table 9-1. MFU examples from “PaLM: Scaling Language Modeling with Pathways” (Chowdhery et al., 2022).

| Model | Number of parameters (in billions) | Accelerator chips | Model FLOP/s utilization |
| :--- | :--- | :--- | :--- |
| GPT-3 | 175B | V100 | 21.3% |
| Gopher | 280B | 4096 TPU v3 | 32.5% |
| Megatron-Turing NLG | 530B | 2240 A100 | 30.2% |
| PaLM | 540B | 6144 TPU v4 | 46.2% |

Figure 9-5 shows the MBU for the inference process using Llama 2-70B in FP16 on different hardware. The decline is likely due to the higher computational load per second with more users, shifting the workload from being bandwidth-bound to compute-bound.

Figure 9-5. Bandwidth utilization for Llama 2-70B in FP16 across three different chips shows a decrease in MBU as the number of concurrent users increases. Image from “LLM Training and Inference with Intel Gaudi 2 AI Accelerators” (Databricks, 2024).

12 Chip makers might also be doing what I call peak FLOP/s hacking. This might run experiments in certain conditions, such as using sparse matrices with specific shapes, to increase their peak FLOP/s. Higher peak FLOP/s numbers make their chips more attractive, but it can be harder for users to achieve high MFU.
