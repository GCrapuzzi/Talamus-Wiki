---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 163
section-title: Inference Service Optimization
source-location: pages 464-470
previous-section: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/164-summary.md
classification: reusable-knowledge-candidate
---
# Inference Service Optimization

24 Many companies consider their kernels their trade secrets. Having kernels that allow them to run models
faster and cheaper than their competitors is a competitive advantage.
Compilers can be standalone tools, such as Apache TVM  and MLIR (Multi-Level
Intermediate Representation) or integrated into ML and inference frameworks, like
torch.compile (a feature in PyTorch), XLA (Accelerated Linear Algebra, originally
developed by TensorFlow, with an open source version called OpenXLA), and the
compiler built into the TensorRT, which is optimized for NVIDIA GPUs. AI compa‐
nies might have their own compilers, with their proprietary kernels designed to speed
up their own workloads.24
Inference Service Optimization
Most service-level optimization techniques focus on resource management. Given a
fixed amount of resources (compute and memory) and dynamic workloads (infer‐
ence requests from users that may involve different models), the goal is to efficiently
allocate resources to these workloads to optimize for latency and cost. Unlike many
model-level techniques, service-level techniques don’t modify models and shouldn’t
change the output quality.
Batching
One of the easiest ways to reduce your cost is batching. In production, your inference
service might receive multiple requests simultaneously. Instead of processing each
request separately, batching the requests that arrive around the same time together
can significantly reduce the service’s throughput. If processing each request sepa‐
rately is like everyone driving their own car, batching is like putting them together on
a bus. A bus can move more people, but it can also make each person’s journey
longer. However, if you do it intelligently, the impact on latency can be minimal.
The three main techniques for batching are: static batching, dynamic batching, and
continuous batching.
The simplest batching technique is static batching. The service groups a fixed number
of inputs together in a batch. It’s like a bus that waits until every seat is filled before
departing. The drawback of static batching is that all requests have to wait until the
batch is full to be executed. Thus the first request in a batch is delayed until the
batch’s last request arrives, no matter how late the last request is.
440 | Chapter 9: Inference Optimization

Dynamic batching, on the other hand, sets a maximum time window for each batch.
If the batch size is four and the window is 100 ms, the server processes the batch
either when it has four requests or when 100 ms has passed, whichever happens first.
It’s like a bus that leaves on a fixed schedule or when it’s full. This approach keeps
latency under control, so earlier requests aren’t held up by later ones. The downside
is that batches may not always be full when processed, possibly leading to wasted
compute. Static batching and dynamic batching are visualized in Figure 9-15.
Figure 9-15. Dynamic batching keeps the latency manageable but might be less
compute-efficient.
In naive batching implementations, all batch requests have to be completed before
their responses are returned. For LLMs, some requests might take much longer than
others. If one request in a batch generates only 10 response tokens and another
request generates 1,000 response tokens, the short response has to wait until the long
response is completed before being returned to the user. This results in unnecessary
latency for short requests.
Continuous batching allows responses in a batch to be returned to users as soon as
they are completed. It works by selectively batching operations that don’t cause the
generation of one response to hold up another, as introduced in the paper Orca ( Yu
et al., 2022 ). After a request in a batch is completed and its response returned, the
service can add another request into the batch in its place, making the batching con‐
tinuous. It’s like a bus that, after dropping off one passenger, can immediately pick
up another passenger to maximize its occupancy rate. Continuous batching, also
called in-flight batching, is visualized in Figure 9-16.
Inference Optimization  | 441

[Visual content extracted via GLM-OCR]

Dynamic batching, on the other hand, sets a maximum time window for each batch. If the batch size is four and the window is 100 ms, the server processes the batch either when it has four requests or when 100 ms has passed, whichever happens first. It’s like a bus that leaves on a fixed schedule or when it’s full. This approach keeps latency under control, so earlier requests aren’t held up by later ones. The downside is that batches may not always be full when processed, possibly leading to wasted compute. Static batching and dynamic batching are visualized in Figure 9-15.

Figure 9-15. Dynamic batching keeps the latency manageable but might be less compute-efficient.

In naive batching implementations, all batch requests have to be completed before their responses are returned. For LLMs, some requests might take much longer than others. If one request in a batch generates only 10 response tokens and another request generates 1,000 response tokens, the short response has to wait until the long response is completed before being returned to the user. This results in unnecessary latency for short requests.

Continuous batching allows responses in a batch to be returned to users as soon as they are completed. It works by selectively batching operations that don’t cause the generation of one response to hold up another, as introduced in the paper Orca (Yu et al., 2022). After a request in a batch is completed and its response returned, the service can add another request into the batch in its place, making the batching continuous. It’s like a bus that, after dropping off one passenger, can immediately pick up another passenger to maximize its occupancy rate. Continuous batching, also called in-flight batching, is visualized in Figure 9-16.

Figure 9-16. With continuous batching, completed responses can be returned immedi‐
ately to users, and new requests can be processed in their place.
Decoupling prefill and decode
LLM inference consists of two steps: prefill and decode. Because prefill is computebound and decode is memory bandwidth-bound, using the same machine to perform
both can cause them to inefficiently compete for resources and significantly slow
down both TTFT and TPOT. Imagine a GPU that is already handling prefilling and
decoding near its peak computational capacity. It might be able to handle another
low computational job like decoding. However, adding a new query to this GPU
means introducing a prefilling job along with a decoding job. This one prefilling job
can drain computational resources from existing decoding jobs, slowing down TPOT
for these requests.
One common optimization technique for inference servers is to disaggregate prefill
and decode. “DistServe” ( Zhong et al., 2024 ) and “Inference Without Interference”
(Hu et al., 2024) show that for various popular LLMs and applications, assigning pre‐
fill and decode operations to different instances (e.g., different GPUs) can signifi‐
cantly improve the volume of processed requests while adhering to latency
requirements. Even though decoupling requires transferring intermediate states from
prefill instances to decode instances, the paper shows communication overhead is not
substantial in modern GPU clusters with high-bandwidth connections such as
NVLink within a node.
442 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Decoupling prefill and decode

LLM inference consists of two steps: prefill and decode. Because prefill is compute-bound and decode is memory bandwidth-bound, using the same machine to perform both can cause them to inefficiently compete for resources and significantly slow down both TTFT and TPOT. Imagine a GPU that is already handling prefilling and decoding near its peak computational capacity. It might be able to handle another low computational job like decoding. However, adding a new query to this GPU means introducing a prefilling job along with a decoding job. This one prefilling job can drain computational resources from existing decoding jobs, slowing down TPOT for these requests.

One common optimization technique for inference servers is to disaggregate prefill and decode. “DistServe” (Zhong et al., 2024) and “Inference Without Interference” (Hu et al., 2024) show that for various popular LLMs and applications, assigning prefill and decode operations to different instances (e.g., different GPUs) can significantly improve the volume of processed requests while adhering to latency requirements. Even though decoupling requires transferring intermediate states from prefill instances to decode instances, the paper shows communication overhead is not substantial in modern GPU clusters with high-bandwidth connections such as NVLink within a node.

25 Talks mentioning the prefill to decode instance ratio include “Llama Inference at Meta”  (Meta, 2024).
The ratio of prefill instances to decode instances depends on many factors, such as
the workload characteristics (e.g., longer input lengths require more prefill compute)
and latency requirements (e.g., whether you want lower TTFT or TPOT). For exam‐
ple, if input sequences are usually long and you want to prioritize TTFT, this ratio
can be between 2:1 and 4:1. If input sequences are short and you want to prioritize
TPOT, this ratio can be 1:2 to 1:1.25
Prompt caching
Many prompts in an application have overlapping text segments. A prompt cache
stores these overlapping segments for reuse, so you only need to process them once.
A common overlapping text segment in different prompts is the system prompt.
Without a prompt cache, your model needs to process the system prompt with every
query. With a prompt cache, the system prompt needs to be processed just once for
the first query.
Prompt caching is useful for queries that involve long documents. For example, if
many of your user queries are related to the same long document (such as a book or a
codebase), this long document can be cached for reuse across queries. It’s also useful
for long conversations when the processing of earlier messages can be cached and
reused when predicting future messages.
A prompt cache is visualized in Figure 9-17. It’s also called a context cache or prefix
cache.
Figure 9-17. With a prompt cache, overlapping segments in different prompts can be
cached and reused.
Inference Optimization  | 443

[Visual content extracted via GLM-OCR]

The ratio of prefill instances to decode instances depends on many factors, such as the workload characteristics (e.g., longer input lengths require more prefill compute) and latency requirements (e.g., whether you want lower TTFT or TPOT). For example, if input sequences are usually long and you want to prioritize TTFT, this ratio can be between 2:1 and 4:1. If input sequences are short and you want to prioritize TPOT, this ratio can be 1:2 to 1:1.25

Prompt caching

Many prompts in an application have overlapping text segments. A prompt cache stores these overlapping segments for reuse, so you only need to process them once. A common overlapping text segment in different prompts is the system prompt. Without a prompt cache, your model needs to process the system prompt with every query. With a prompt cache, the system prompt needs to be processed just once for the first query.

Prompt caching is useful for queries that involve long documents. For example, if many of your user queries are related to the same long document (such as a book or a codebase), this long document can be cached for reuse across queries. It’s also useful for long conversations when the processing of earlier messages can be cached and reused when predicting future messages.

A prompt cache is visualized in Figure 9-17. It’s also called a context cache or prefix cache.

![Figure 9-17. With a prompt cache, overlapping segments in different prompts can be cached and reused.](image)

25 Talks mentioning the prefill to decode instance ratio include “Llama Inference at Meta” (Meta, 2024).

26 While llama.cpp also has prompt caching, it seems to cache only whole prompts and work for queries in the
same chat session, as of this writing. Its documentation is limited, but my guess from reading the code is that
in a long conversation, it caches the previous messages and processes only the newest message.
For applications with long system prompts, prompt caching can significantly reduce
both latency and cost. If your system prompt is 1,000 tokens, and your application
generates one million model API calls daily, a prompt cache will save you from pro‐
cessing approximately one billion repetitive input tokens a day! However, this isn’t
entirely free. Like the KV cache, prompt cache size can be quite large and take up
memory space. Unless you use a model API with this functionality, implementing
prompt caching can require significant engineering effort.
Since its introduction in November 2023 by Gim et al. , the prompt cache has been
rapidly incorporated into model APIs. As of this writing, Google Gemini offers this
functionality, with cached input tokens given a 75% discount compared to regular
input tokens, but you’ll have to pay extra for cache storage (as of writing, $1.00/one
million tokens per hour). Anthropic offers prompt caching that promises up to 90%
cost savings (the longer the cached context, the higher the savings) and up to 75%
latency reduction. The impact of prompt caching on the cost and latency of different
scenarios is shown in Table 9-3.26
Table 9-3. Cost and latency reduced by prompt caching. Information from Anthropic
(2024).
Use case Latency w/o caching
(time to first token)
Latency with caching
(time to first token)
Cost reduction
Chat with a book (100,000token cached prompt)
11.5 s 2.4 s (–79%) –90%
Many-shot prompting
(10,000-token prompt)
1.6 s 1.1 s (–31%) –86%
Multi-turn conversation (10turn convo with a long system
prompt)
~10 s ~2.5 s (–75%) –53%
Parallelism
Accelerators are designed for parallel processing, and parallelism strategies are the
backbone of high-performance computing. Many new parallelization strategies are
being developed. This section covers only a few of them for reference. Two families of
parallelization strategies that can be applied across all models are data parallelism and
model parallelism. A family of strategies applied specifically for LLMs is context and
sequence parallelism. An optimization technique might involve multiple parallelism
strategies.
444 | Chapter 9: Inference Optimization

27 During training, the same technique is called data parallelism.
Replica parallelism is the most straightforward strategy to implement. It simply cre‐
ates multiple replicas of the model you want to serve. 27 More replicas allow you to
handle more requests at the same time, potentially at the cost of using more chips.
Trying to fit models of different sizes onto different chips is a bin-packing problem,
which can get complicated with more models, more replicas, and more chips.
Let’s say you have a mixture of models of different sizes (e.g., 8B, 13B, 34B, and 70B
parameters) and access to GPUs of different memory capabilities (e.g., 24 GB, 40 GB,
48 GB, and 80 GB). For simplicity, assume that all models are in the same precision, 8
bits:
• If you have a fixed number of chips, you need to decide how many replicas to
create for each model and what GPUs to use for each replica to maximize your
metrics. For example, should you place three 13B models on a 40 GB GPU, or
should you reserve this GPU for one 34B model?
• If you have a fixed number of model replicas, you need to decide what chips to
acquire to minimize the cost. This situation, however, rarely occurs.
Often, your model is so big that it can’t fit into one machine. Model parallelism refers
to the practice of splitting the same model across multiple machines. Fitting models
onto chips can become an even more complicated problem with model parallelism.
There are several ways to split a model. The most common approach for inference is
tensor parallelism , also known as intra-operator parallelism . Inference involves a
sequence of operators on multidimensional tensors, such as matrix multiplication. In
this approach, tensors involved in an operator are partitioned across multiple devices,
effectively breaking up this operator into smaller pieces to be executed in parallel,
thus speeding up the computation. For example, when multiplying two matrices, you
can split one of the matrices columnwise, as shown in Figure 9-18.
Tensor parallelism provides two benefits. First, it makes it possible to serve large
models that don’t fit on single machines. Second, it reduces latency. The latency ben‐
efit, however, might be reduced due to extra communication overhead.
Inference Optimization  | 445

Figure 9-18. Tensor parallelism for matrix multiplication.
Another way to split a model is pipeline parallelism , which involves dividing a
model’s computation into distinct stages and assigning each stage to a different
device. As data flows through the model, each stage processes one part while others
process subsequent parts, enabling overlapping computations. Figure 9-19  shows
what pipeline parallelism looks like on four machines.
Figure 9-19. Pipeline parallelism enables model splits to be executed in parallel.
Figure 9-19  shows a batch can be split into smaller micro-batches. After a microbatch is processed on one machine, its output is passed onto the next part of the
model on the next machine.
446 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Another way to split a model is pipeline parallelism, which involves dividing a model’s computation into distinct stages and assigning each stage to a different device. As data flows through the model, each stage processes one part while others process subsequent parts, enabling overlapping computations. Figure 9-19 shows what pipeline parallelism looks like on four machines.

Figure 9-19. Pipeline parallelism enables model splits to be executed in parallel.

Figure 9-19 shows a batch can be split into smaller micro-batches. After a micro-batch is processed on one machine, its output is passed onto the next part of the model on the next machine.
