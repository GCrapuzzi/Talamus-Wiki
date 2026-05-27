---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 158
section-title: Inference Overview
source-location: pages 430-435
previous-section: AI Space/normalized/pdf/ai-engineering/sections/157-understanding-inference-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
classification: reusable-knowledge-candidate
---
# Inference Overview

1 As discussed in Chapter 7, inference involves the forward pass while training involves both the forward and
backward passes.
2 A friend, Mark Saroufim, pointed me to an interesting relationship between a model’s training cost and infer‐
ence cost. Imagine you’re a model provider. Let T be the total training cost, p be the cost you’re charging per
inference, and N be the number of inference calls you can sell. Developing a model only makes sense if the
money you can recover from inference for a model is more than its training cost, i.e., T <= p × N. The more a
model is used in production, the more model providers can reduce inference cost. However, this doesn’t
apply for third-party API providers who sell inference calls on top of open source models.
This chapter also covers performance metrics and trade-offs. Sometimes, a technique
that speeds up a model can also reduce its cost. For example, reducing a model’s pre‐
cision makes it smaller and faster. But often, optimization requires trade-offs. For
example, the best hardware might make your model run faster but at a higher cost.
Given the growing availability of open source models, more teams are building their
own inference services. However, even if you don’t implement these inference opti‐
mization techniques, understanding these techniques will help you evaluate inference
services and frameworks. If your application’s latency and cost are hurting you, read
on. This chapter might help you diagnose the causes and potential solutions.
Understanding Inference Optimization
There are two distinct phases in an AI model’s lifecycle: training and inference.
Training refers to the process of building a model. Inference refers to the process of
using a model to compute an output for a given input. 1 Unless you train or finetune a
model, you’ll mostly need to care about inference. 2
This section starts with an overview of inference that introduces a shared vocabulary
to discuss the rest of the chapter. If you’re already familiar with these concepts, feel
free to skip to the section of interest.
Inference Overview
In production, the component that runs model inference is called an inference server.
It hosts the available models and has access to the necessary hardware. Based on
requests from applications (e.g., user prompts), it allocates resources to execute the
appropriate models and returns the responses to users. An inference server is part of
a broader inference service, which is also responsible for receiving, routing, and pos‐
sibly preprocessing requests before they reach the inference server. A visualization of
a simple inference service is shown in Figure 9-1.
406 | Chapter 9: Inference Optimization

.
Figure 9-1. A simple inference service.
Model APIs like those provided by OpenAI and Google are inference services. If you
use one of these services, you won’t be implementing most of the techniques dis‐
cussed in this chapter. However, if you host a model yourself, you’ll be responsible
for building, optimizing, and maintaining its inference service.
Computational bottlenecks
Optimization is about identifying bottlenecks and addressing them. For example, to
optimize traffic, city planners might identify congestion points and take measures to
alleviate congestion. Similarly, an inference server should be designed to address the
computational bottlenecks of the inference workloads it serves. There are two main
computational bottlenecks, compute-bound and memory bandwidth-bound:
Compute-bound
This refers to tasks whose time-to-complete is determined by the computation
needed for the tasks. For example, password decryption is typically computebound due to the intensive mathematical calculations required to break encryp‐
tion algorithms.
Memory bandwidth-bound
These tasks are constrained by the data transfer rate within the system, such as
the speed of data movement between memory and processors. For example, if
you store your data in the CPU memory and train a model on GPUs, you have to
move data from the CPU to the GPU, which can take a long time. This can be
Understanding Inference Optimization | 407

[Visual content extracted via GLM-OCR]

Model APIs like those provided by OpenAI and Google are inference services. If you use one of these services, you won’t be implementing most of the techniques discussed in this chapter. However, if you host a model yourself, you’ll be responsible for building, optimizing, and maintaining its inference service.

Computational bottlenecks

Optimization is about identifying bottlenecks and addressing them. For example, to optimize traffic, city planners might identify congestion points and take measures to alleviate congestion. Similarly, an inference server should be designed to address the computational bottlenecks of the inference workloads it serves. There are two main computational bottlenecks, compute-bound and memory bandwidth-bound:

Compute-bound

This refers to tasks whose time-to-complete is determined by the computation needed for the tasks. For example, password decryption is typically compute-bound due to the intensive mathematical calculations required to break encryption algorithms.

Memory bandwidth-bound

These tasks are constrained by the data transfer rate within the system, such as the speed of data movement between memory and processors. For example, if you store your data in the CPU memory and train a model on GPUs, you have to move data from the CPU to the GPU, which can take a long time. This can be

3 Anecdotally, I find that people coming from a system background (e.g., optimization engineers and GPU
engineers) use memory-bound to refer to bandwidth-bound, and people coming from an AI background (e.g.,
ML and AI engineers) use to memory-bound to refer to memory capacity-bound.
4 The Roofline paper uses the term memory-bound to refer to memory-bandwidth bound.
shortened as bandwidth-bound. In literature, memory bandwidth-bound is often
referred to as memory-bound.
Terminology Ambiguity: Memory-Bound Versus Bandwidth-Bound
Memory-bound is also used by some people to refer to tasks whose time-to-complete
is constrained by memory capacity instead of memory bandwidth. This occurs when
your hardware doesn’t have sufficient memory to handle the task, for example, if your
machine doesn’t have enough memory to store the entire internet. This memory is
often manifested in the error recognizable by engineers everywhere: OOM, out-ofmemory.3
However, this situation can often be mitigated by splitting your task into smaller
pieces. For example, if you’re constrained by GPU memory and cannot fit an entire
model into the GPU, you can split the model across GPU memory and CPU memory.
This splitting will slow down your computation because of the time it takes to trans‐
fer data between the CPU and GPU. However, if data transfer is fast enough, this
becomes less of an issue. Therefore, the memory capacity limitation is actually more
about memory bandwidth.
The concepts of compute-bound or memory bandwidth-bound were introduced in
the paper “Roofline” ( Williams et al., 2009 ).4 Mathematically, an operation can be
classified as compute-bound or memory bandwidth-bound based on its arithmetic
intensity, which is the number of arithmetic operations per byte of memory access.
Profiling tools like NVIDIA Nsight will show you a roofline chart to tell you whether
your workload is compute-bound or memory bandwidth-bound, as shown in
Figure 9-2. This chart is a roofline chart because it resembles a roof. Roofline charts
are common in hardware performance analyses.
Different optimization techniques aim to mitigate different bottlenecks. For example,
a compute-bound workload might be sped up by spreading it out to more chips or by
leveraging chips with more computational power (e.g., a higher FLOP/s number). A
memory bandwidth-bound workload might be sped up by leveraging chips with
higher bandwidth.
408 | Chapter 9: Inference Optimization

5 Prefilling effectively populates the initial KV cache for the transformer model.
Figure 9-2. The roofline chart can help you visualize whether an operation is computebound or memory bandwidth-bound. This graph is on a log scale.
Different model architectures and workloads result in different computational bottle‐
necks. For example, inference for image generators like Stable Diffusion is typically
compute-bound, whereas inference for autoregression language models is typically
memory bandwidth-bound.
As an illustration, let’s look into language model inference. Recall from Chapter 2
that inference for a transformer-based language model consists of two steps, prefill‐
ing and decoding:
Prefill
The model processes the input tokens in parallel. 5 How many tokens can be pro‐
cessed at once is limited by the number of operations your hardware can execute
in a given time. Therefore, prefilling is compute-bound.
Decode
The model generates one output token at a time. At a high level, this step typi‐
cally involves loading large matrices (e.g., model weights) into GPUs, which is
limited by how quickly your hardware can load data into memory. Decoding is,
therefore, memory bandwidth-bound.
Figure 9-3 visualizes prefilling and decoding.
Understanding Inference Optimization | 409

[Visual content extracted via GLM-OCR]

Figure 9-2. The rooftline chart can help you visualize whether an operation is compute-bound or memory bandwidth-bound. This graph is on a log scale.

Different model architectures and workloads result in different computational bottlenecks. For example, inference for image generators like Stable Diffusion is typically compute-bound, whereas inference for autoregression language models is typically memory bandwidth-bound.

As an illustration, let’s look into language model inference. Recall from Chapter 2 that inference for a transformer-based language model consists of two steps, prefilling and decoding:

**Prefill**
The model processes the input tokens in parallel. How many tokens can be processed at once is limited by the number of operations your hardware can execute in a given time. Therefore, prefilling is compute-bound.

**Decode**
The model generates one output token at a time. At a high level, this step typically involves loading large matrices (e.g., model weights) into GPUs, which is limited by how quickly your hardware can load data into memory. Decoding is, therefore, memory bandwidth-bound.

Figure 9-3 visualizes prefilling and decoding.

5 Prefilling effectively populates the initial KV cache for the transformer model.

Figure 9-3. Autoregressive language models follow two steps for inference: prefill and
decode. <eos> denotes the end of the sequence token.
Because prefill and decode have different computational profiles, they are often
decoupled in production with separate machines. This technique will be discussed
“Inference Service Optimization” on page 440 .
The factors that affect the amount of prefilling and decoding computation in an LLM
inference server, and therefore its bottlenecks, include context length, output length,
and request batching strategies. Long context typically results in a memory
bandwidth-bound workload, but clever optimization techniques, such as those dis‐
cussed later in this chapter, can remove this bottleneck.
As of this writing, due to the prevalence of the transformer architecture and the limi‐
tations of the existing accelerator technologies, many AI and data workloads are
memory bandwidth-bound. However, future software and hardware advancements
will be able to make AI and data workloads compute-bound.
Online and batch inference APIs
Many providers offer two types of inference APIs, online and batch:
• Online APIs optimize for latency. Requests are processed as soon as they arrive.
• Batch APIs optimize for cost. If your application doesn’t have strict latency
requirements, you can send them to batch APIs for more efficient processing.
Higher latency allows a broader range of optimization techniques, including
batching requests together and using cheaper hardware. For example, as of this
writing, both Google Gemini and OpenAI offer batch APIs at a 50% cost
410 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Because prefill and decode have different computational profiles, they are often decoupled in production with separate machines. This technique will be discussed “Inference Service Optimization” on page 440.

The factors that affect the amount of prefilling and decoding computation in an LLM inference server, and therefore its bottlenecks, include context length, output length, and request batching strategies. Long context typically results in a memory bandwidth-bound workload, but clever optimization techniques, such as those discussed later in this chapter, can remove this bottleneck.

As of this writing, due to the prevalence of the transformer architecture and the limitations of the existing accelerator technologies, many AI and data workloads are memory bandwidth-bound. However, future software and hardware advancements will be able to make AI and data workloads compute-bound.

Online and batch inference APIs

Many providers offer two types of inference APIs, online and batch:

• Online APIs optimize for latency. Requests are processed as soon as they arrive.
• Batch APIs optimize for cost. If your application doesn’t have strict latency requirements, you can send them to batch APIs for more efficient processing. Higher latency allows a broader range of optimization techniques, including batching requests together and using cheaper hardware. For example, as of this writing, both Google Gemini and OpenAI offer batch APIs at a 50% cost.

6 If you run an inference service, separating your inference APIs into online and batch can help you prioritize
latency for requests where latency matters the most. Let’s say that your inference server can serve only a maxi‐
mum of X requests/second without latency degradation, you have to serve Y requests/second, and Y is larger
than X. In an ideal world, users with less-urgent requests can send their requests to the batch API, so that
your service can focus on processing the online API requests first.
reduction and significantly higher turnaround time, i.e., in the order of hours
instead of seconds or minutes.6
Online APIs might still batch requests together as long as it doesn’t significantly
impact latency, as discussed in “Batching” on page 440 . The only real difference is that
an online API focuses on lower latency, whereas a batch API focuses on higher
throughput.
Customer-facing use cases, such as chatbots and code generation, typically require
lower latency, and, therefore, tend to use online APIs. Use cases with less stringent
latency requirements, which are ideal for batch APIs, include the following:
• Synthetic data generation
• Periodic reporting, such as summarizing Slack messages, sentiment analysis of
brand mentions on social media, and analyzing customer support tickets
• Onboarding new customers who require processing of all their uploaded
documents
• Migrating to a new model that requires reprocessing of all the data
• Generating personalized recommendations or newsletters for a large customer
base
• Knowledge base updates by reindexing an organization’s data
APIs usually return complete responses by default. However, with autoregressive
decoding, it can take a long time for a model to complete a response, and users are
impatient. Many online APIs offer streaming mode, which returns each token as it’s
generated. This reduces the time the users have to wait until the first token. The
downside of this approach is that you can’t score a response before showing it to
users, increasing the risk of users seeing bad responses. However, you can still retro‐
spectively update or remove a response as soon as the risk is detected.
Understanding Inference Optimization | 411
