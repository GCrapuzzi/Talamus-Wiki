---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 157
section-title: Understanding Inference Optimization
source-location: pages 430-430
previous-section: AI Space/normalized/pdf/ai-engineering/sections/156-chapter-9.-inference-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/158-inference-overview.md
classification: reusable-knowledge-candidate
---
# Understanding Inference Optimization

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
