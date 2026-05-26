---
type: framework
tags: [inference, parallelism, tensor-parallelism, pipeline-parallelism, distributed-systems]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-service-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Inference Parallelism Strategies

Parallelism strategies for distributing inference across multiple devices.

### Replica parallelism
Duplicate the entire model across machines. Simplest to implement; directly increases request capacity. Fitting mixed model sizes onto heterogeneous GPUs is a bin-packing problem.

### Tensor parallelism (intra-operator)
Partition tensors within an operator across devices (e.g., split a weight matrix column-wise for matmul). Enables serving models too large for one device **and** reduces latency. Communication overhead partially offsets latency gains.

### Pipeline parallelism
Divide model into sequential stages, each on a different device. Micro-batches overlap across stages. Increases total per-request latency due to inter-stage communication, so typically avoided for latency-sensitive inference; more common in training for throughput.

### Context parallelism
Split the input sequence itself across devices (e.g., first half on machine 1, second half on machine 2). Targets long-input workloads.

### Sequence parallelism
Split different operators (e.g., attention vs feedforward) across machines for the same input.

**Most impactful for inference**: tensor parallelism (latency + large model support) and replica parallelism (simple, scalable).
