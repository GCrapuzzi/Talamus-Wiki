---
type: overview
tags: [overview]
sources:
  - AI Space/normalized/pdf/ai-engineering.md
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# ai-engineering Overview

# AI Engineering — Building Applications with Foundation Models

**Source**: *AI Engineering* by Chip Huyen (O'Reilly, 2024). A comprehensive guide to building production AI applications on top of foundation models, aimed at practitioners who consume models rather than train them from scratch.

## Core Thesis

[[AI Engineering]] emerges as a distinct discipline from [[AI Engineering vs ML Engineering]]: where ML engineering centres on training models, AI engineering centres on *using* pre-trained [[Foundation Model]]s to build products. The [[Scaling Hypothesis]] and the rise of [[Model as a Service]] APIs have lowered barriers so that application developers—not just researchers—can ship AI features. [[Lindy's Law]] is invoked to argue that foundation models represent a durable paradigm shift rather than a passing trend.

## Foundations (Chapters 1–2)

The book grounds readers in the [[AI Engineering Stack]] (infrastructure → model → application layers) and the [[Language Model]] lineage from [[Self-Supervised Learning]] through the [[Transformer Architecture]] and [[Attention Mechanism]] to modern alternatives like [[State Space Models]] and [[Mixture of Experts]]. [[Chinchilla Scaling Law]] and [[Inverse Scaling]] frame the relationship between compute, data, and capability. The [[Post-Training Pipeline]]—[[Supervised Finetuning]], preference tuning—bridges pre-training to usability, while [[Sampling Strategies]], [[Test Time Compute]], and [[Structured Outputs]] govern how models produce output. [[Hallucination]] is introduced as a fundamental probabilistic limitation.

## Evaluation (Chapters 3–4)

A major theme is [[Evaluation-Driven Development]]: measure before you optimise. The [[AI Evaluation Criteria Taxonomy]] spans [[Perplexity]], [[Cross Entropy]], [[Functional Correctness Evaluation]], [[Lexical Similarity]], [[Semantic Similarity]], and [[AI as a Judge]]. [[Comparative Evaluation]] and [[Benchmark Selection and Aggregation]] address model ranking, while [[Benchmark Data Contamination]] and [[Simpson's Paradox]] warn of pitfalls. The [[Model Selection Workflow]] and [[Model Build vs Buy Decision]] frameworks help practitioners choose or commission the right model. [[Evaluation Pipeline Design]] and [[Evaluation Challenges for Foundation Models]] round out the methodology.

## Prompt Engineering (Chapter 5)

Prompting is the first—and often sufficient—adaptation lever. [[Prompt Anatomy]] defines the structural elements; [[In-Context Learning]], [[Chain-of-Thought Prompting]], and [[Prompt Decomposition]] are key techniques. [[Prompt Engineering Best Practices]] and [[Prompt Versioning and Organization]] bring engineering rigour. Security surfaces via the [[Prompt Attack Taxonomy]], [[Instruction Hierarchy]], and [[Prompt Attack Defenses]]. [[Prompt Robustness]] and [[Automated Prompt Optimization]] address reliability and scale.

## RAG (Chapter 6)

[[Retrieval-Augmented Generation]] grounds model output in external knowledge. The [[RAG Architecture]] combines [[Term-Based Retrieval]], [[Embedding-Based Retrieval]], and [[Hybrid Search]] (fused via [[Reciprocal Rank Fusion]]). [[Vector Search Algorithms]] power the embedding path. [[Chunking Strategy]], [[Query Rewriting]], and [[Contextual Retrieval]] improve relevance, measured by [[Retrieval Evaluation Metrics]]. [[Multimodal RAG]] extends the pattern beyond text.

## Agents (Chapter 7)

The [[AI Agent]] concept adds planning and action to generation. [[Agent Planning]], [[Agent Tool Categories]], [[Function Calling]], and the [[ReAct Pattern]] define the building blocks. [[Agent Control Flows]] and [[Agent Tool Selection]] govern execution, while [[Agent Failure Modes]] and [[Compound Error in Agents]] quantify risk. [[AI Memory Systems]] give agents persistent state.

## Finetuning & Dataset Engineering (Chapters 8–9)

[[Transfer Learning]] underpins all adaptation. [[Continued Pre-Training]] injects domain knowledge; [[Supervised Finetuning]] teaches task-specific behaviour. The [[Finetuning vs RAG Decision Framework]], [[Reasons to Finetune]], and [[Reasons Not to Finetune]] guide the decision. Efficiency techniques—[[Quantization]], [[Parameter-Efficient Finetuning]], [[LoRA]], [[QLoRA]], [[Gradient Checkpointing]]—address the [[Finetuning Memory Bottleneck]]. [[Model Merging]] and [[Task Vectors and Task Arithmetic]] enable post-hoc composition; [[Distillation]] and [[Model Distillation]] compress capability. [[Finetuning Hyperparameters]] covers practical tuning.

Dataset engineering is treated as equally critical via [[Data-Centric AI]]. [[Data Quality Criteria for Finetuning]], [[Data Coverage and Diversity]], and [[Finetuning Data Quantity Guidelines]] set standards. [[AI-Powered Data Synthesis]], [[Synthetic Data Verification]], [[Reverse Instruction]], and [[Training Data Processing Pipeline]] address data creation, while [[Model Collapse]] warns against recursive synthetic data. The [[Data Flywheel]] and [[Progressive Finetuning]] patterns sustain continuous improvement. [[Training Data Formats by Task]] provides practical templates.

## Inference Optimization (Chapter 10)

Serving at scale requires understanding [[Compute-Bound vs Memory Bandwidth-Bound]] regimes, [[Inference Performance Metrics]], [[MFU and MBU]], and the [[GPU Memory Hierarchy]]. Techniques include [[KV Cache]] management, [[Speculative Decoding]], [[Parallel Decoding]], [[Inference Batching Strategies]], [[Prefill-Decode Disaggregation]], [[Prompt Caching]], [[Kernel Optimization Techniques]], and [[Inference Parallelism Strategies]]. [[Online vs Batch Inference API]] and [[Inference with Reference]] address serving patterns. [[AI Accelerator Selection]] rounds out hardware decisions.

## AI Application Architecture (Chapter 11)

[[AI Application Architecture Progression]] traces the path from simple prompt to production system. Key components include [[Input and Output Guardrails]], [[Model Router]], [[Model Gateway]], [[Semantic Cache]], and [[AI Pipeline Orchestration]]. [[AI Observability Metrics]] and [[Logging and Tracing for AI Systems]] enable monitoring. [[Conversational Feedback Signals]], [[Feedback Design Principles]], and [[Feedback Bias and Degenerate Feedback Loops]] close the loop from users back to model improvement.

## Planning & Process

The [[AI Application Planning Framework]] and [[AI Application Development Loop]] provide end-to-end process guidance, from use-case selection through [[Domain-Specific Models]], [[Training Data Distribution]], and [[Low-Resource Languages in LLMs]] considerations, to iterative deployment and maintenance.
