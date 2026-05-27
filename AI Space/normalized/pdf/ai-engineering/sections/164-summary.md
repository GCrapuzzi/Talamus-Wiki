---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 164
section-title: Summary
source-location: pages 471-472
previous-section: AI Space/normalized/pdf/ai-engineering/sections/163-inference-service-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/165-chapter-10.-ai-engineering-architecture-and-user-feedback.md
classification: reusable-knowledge-candidate
---
# Summary

While pipeline parallelism enables serving large models on multiple machines, it
increases the total latency for each request due to extra communication between
pipeline stages. Therefore, for applications with strict latency requirements, pipeline
parallelism is typically avoided in favor of replica parallelism. However, pipeline par‐
allelism is commonly used in training since it can help increase throughput.
Two techniques that are less common but might warrant a quick mention to illustrate
the diversity of techniques are context parallelism  and sequence parallelism . They
were both developed to make long input sequence processing more efficient, includ‐
ing context parallelism and sequence parallelism.
In context parallelism, the input sequence itself is split across different devices to be
processed separately. For example, the first half of the input is processed on machine
1 and the second half on machine 2.
In sequence parallelism , operators needed for the entire input are split across
machines. For example, if the input requires both attention and feedforward compu‐
tation, attention might be processed on machine 1 while feedforward is processed on
machine 2.
Summary
A model’s usability depends heavily on its inference cost and latency. Cheaper infer‐
ence makes AI-powered decisions more affordable, while faster inference enables the
integration of AI into more applications. Given the massive potential impact of infer‐
ence optimization, it has attracted many talented individuals who continually come
up with innovative approaches.
Before we start making things more efficient, we need to understand how efficiency is
measured. This chapter started with common efficiency metrics for latency, through‐
put, and utilization. For language model-based inference, latency can be broken into
time to first token (TTFT), which is influenced by the prefilling phase, and time per
output token (TPOT), which is influenced by the decoding phase. Throughput met‐
rics are directly related to cost. There’s a trade-off between latency and throughput.
You can potentially reduce cost if you’re okay with increased latency, and reducing
latency often involves increasing cost.
How efficiently a model can run depends on the hardware it is run on. For this rea‐
son, this chapter also provided a quick overview of AI hardware and what it takes to
optimize models on different accelerators.
The chapter then continued with different techniques for inference optimization.
Given the availability of model APIs, most application developers will use these APIs
with their built-in optimization instead of implementing these techniques them‐
selves. While these techniques might not be relevant to all application developers, I
Summary | 447

believe that understanding what techniques are possible can be helpful for evaluating
the efficiency of model APIs.
This chapter also focused on optimization at the model level and the inference service
level. Model-level optimization often requires changing the model itself, which can
lead to changes in the model behaviors. Inference service-level optimization, on the
other hand, typically keeps the model intact and only changes how it’s served.
Model-level techniques include model-agnostic techniques like quantization and dis‐
tillation. Different model architectures require their own optimization. For example,
because a key bottleneck of transformer models is in the attention mechanism, many
optimization techniques involve making attention more efficient, including KV cache
management and writing attention kernels. A big bottleneck for an autoregressive
language model is in its autoregressive decoding process, and consequently, many
techniques have been developed to address it, too.
Inference service-level techniques include various batching and parallelism strategies.
There are also techniques developed especially for autoregressive language models,
including prefilling/decoding decoupling and prompt caching.
The choice of optimization techniques depends on your workloads. For example, KV
caching is significantly more important for workloads with long contexts than those
with short contexts. Prompt caching, on the other hand, is crucial for workloads
involving long, overlapping prompt segments or multi-turn conversations. The
choice also depends on your performance requirements. For instance, if low latency
is a higher priority than cost, you might want to scale up replica parallelism. While
more replicas require additional machines, each machine handles fewer requests,
allowing it to allocate more resources per request and, thus, improve response time.
However, across various use cases, the most impactful techniques are typically quan‐
tization (which generally works well across models), tensor parallelism (which both
reduces latency and enables serving larger models), replica parallelism (which is rela‐
tively straightforward to implement), and attention mechanism optimization (which
can significantly accelerate transformer models).
Inference optimization concludes the list of model adaptation techniques covered in
this book. The next chapter will explore how to integrate these techniques into a
cohesive system.
448 | Chapter 9: Inference Optimization
