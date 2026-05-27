---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 162
section-title: Model Optimization
source-location: pages 450-463
previous-section: AI Space/normalized/pdf/ai-engineering/sections/161-inference-optimization.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/163-inference-service-optimization.md
classification: reusable-knowledge-candidate
---
# Model Optimization

Inference Optimization
Inference optimization can be done at the model, hardware, or service level. To illus‐
trate their differences, consider archery. Model-level optimization is like crafting bet‐
ter arrows. Hardware-level optimization is like training a stronger and better archer.
Service-level optimization is like refining the entire shooting process, including the
bow and aiming conditions.
Ideally, optimizing a model for speed and cost shouldn’t change the model’s quality.
However, many techniques might cause model degradation. Figure 9-8  shows the
same Llama models’ performance on different benchmarks, served by different infer‐
ence service providers.
Figure 9-8. An inference service provider might use optimization techniques that can
alter a model’s behavior, causing different providers to have slight model quality varia‐
tions. The experiment was conducted by Cerebras (2024).
Since hardware design is outside the scope of this book, I’ll discuss techniques at the
model and service levels. While the techniques are discussed separately, keep in mind
that, in production, optimization typically involves techniques at more than one
level.
Model Optimization
Model-level optimization aims to make the model more efficient, often by modifying
the model itself, which can alter its behavior. As of this writing, many foundation
models follow the transformer architecture and include an autoregressive language
model component. These models have three characteristics that make inference
resource-intensive: model size, autoregressive decoding, and the attention mecha‐
nism. Let’s discuss approaches to address these challenges.
426 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

Inference Optimization

Inference optimization can be done at the model, hardware, or service level. To illustrate their differences, consider archery. Model-level optimization is like crafting better arrows. Hardware-level optimization is like training a stronger and better archer. Service-level optimization is like refining the entire shooting process, including the bow and aiming conditions.

Ideally, optimizing a model for speed and cost shouldn’t change the model’s quality. However, many techniques might cause model degradation. Figure 9-8 shows the same Llama models’ performance on different benchmarks, served by different inference service providers.

Figure 9-8. An inference service provider might use optimization techniques that can alter a model’s behavior, causing different providers to have slight model quality variations. The experiment was conducted by Cerebras (2024).

Since hardware design is outside the scope of this book, I’ll discuss techniques at the model and service levels. While the techniques are discussed separately, keep in mind that, in production, optimization typically involves techniques at more than one level.

Model Optimization

Model-level optimization aims to make the model more efficient, often by modifying the model itself, which can alter its behavior. As of this writing, many foundation models follow the transformer architecture and include an autoregressive language model component. These models have three characteristics that make inference resource-intensive: model size, autoregressive decoding, and the attention mechanism. Let’s discuss approaches to address these challenges.

Model compression
Model compression involves techniques that reduce a model’s size. Making a model
smaller can also make it faster. This book has already discussed two model compres‐
sion techniques: quantization and distillation. Quantization, reducing the precision
of a model to reduce its memory footprint and increase its throughput, is discussed in
Chapter 7 . Model distillation, training a small model to mimic the behavior of the
large model, is discussed in Chapter 8.
Model distillation suggests that it’s possible to capture a large model’s behaviors
using fewer parameters. Could it be that within the large model, there exists a subset
of parameters capable of capturing the entire model’s behavior? This is the core con‐
cept behind pruning.
Pruning, in the context of neural networks, has two meanings. One is to remove
entire nodes of a neural network, which means changing its architecture and reduc‐
ing its number of parameters. Another is to find parameters least useful to predic‐
tions and set them to zero. In this case, pruning doesn’t reduce the total number of
parameters, only the number of non-zero parameters. This makes the model more
sparse, which both reduces the model’s storage space and speeds up computation.
Pruned models can be used as-is or be further finetuned to adjust the remaining
parameters and restore any performance degradation caused by the pruning process.
Pruning can help discover promising model architectures ( Liu et al., 2018 ). These
pruned architectures, smaller than the pre-pruned architectures, can also be trained
from scratch (Zhu et al., 2017).
In the literature, there have been many encouraging pruning results. For example,
Frankle and Carbin (2019)  showed that pruning techniques can reduce the non-zero
parameter counts of certain trained networks by over 90%, decreasing memory foot‐
prints and improving speed without compromising accuracy. However, in practice,
as of this writing, pruning is less common. It’s harder to do, as it requires an under‐
standing of the original model’s architecture, and the performance boost it can bring
is often much less than that of other approaches. Pruning also results in sparse mod‐
els, and not all hardware architectures are designed to take advantage of the resulting
sparsity.
Weight-only quantization is by far the most popular approach since it’s easy to use,
works out of the box for many models, and is extremely effective.  Reducing a model’s
precision from 32 bits to 16 bits reduces its memory footprint by half. However, we’re
close to the limit of quantization—we can’t go lower than 1 bit per value. Distillation
is also common because it can result in a smaller model whose behavior is compara‐
tive to that of a much larger one for your needs.
Inference Optimization  | 427

19 Each token generation step necessitates the transfer of the entire model’s parameters from the accelerator’s
high-bandwidth memory to its compute units. This makes this operation bandwidth-heavy. Because the
model can produce only one token at a time, the process consumes only a small number of FLOP/s, resulting
in computational inefficiency.
Overcoming the autoregressive decoding bottleneck
As discussed in Chapter 2, autoregressive language models generate one token after
another. If it takes 100 ms to generate one token, a response of 100 tokens will take
10 s.19 This process is not just slow, it’s also expensive. Across model API providers,
an output token costs approximately two to four times an input token. In an experi‐
ment, Anyscale found that a single output token can have the same impact on latency
as 100 input tokens ( Kadous et al., 2023 ). Improving the autoregressive generation
process by a small percentage can significantly improve user experience.
As the space is rapidly evolving, new techniques are being developed to overcome
this seemingly impossible bottleneck. Perhaps one day, there will be architectures
that don’t have this bottleneck. The techniques covered here are to illustrate what the
solution might look like, but the techniques are still evolving.
Speculative decoding.    Speculative decoding (also called speculative sampling) uses a
faster but less powerful model to generate a sequence of tokens, which are then veri‐
fied by the target model. The target model is the model you want to use. The faster
model is called the draft or proposal model because it proposes the draft output.
Imagine the input tokens are x1, x2, …, xt:
1. The draft model generates a sequence of K tokens: xt + 1, xt + 2, …, xt + K.
2. The target model verifies these K generated tokens in parallel.
3. The target model accepts the longest subsequence of draft tokens, from left to
right, which the target model agrees to use.
4. Let’s say the target model accepts j draft tokens, xt + 1 , xt + 2 , …, xt + j. The target
model then generates one extra token, xt + j + 1.
The process returns to step 1, with the draft model generating K tokens conditioned
on x1, x2, …, xt, xt + 1, xt + 2, …, xt + j. The process is visualized in Figure 9-9.
If no draft token is accepted, this loop produces only one token generated by the tar‐
get model. If all draft tokens are accepted, this loop produces K + 1 tokens, with K
generated by the draft model and one by the target model.
428 | Chapter 9: Inference Optimization

20 This also means that if your MFU is already maxed out, speculative decoding makes less sense.
Figure 9-9. A draft model generates a sequence of K tokens, and the main model accepts
the longest subsequence that it agrees with. The image is from “Blockwise Parallel
Decoding for Deep Autoregressive Models” ( Stern et al., 2018).
If all draft sequences are rejected, the target model must generate the entire response
in addition to verifying it, potentially leading to increased latency. However, this can
be avoided because of these three insights:
1. The time it takes for the target model to verify a sequence of tokens is less than
the time it takes to generate it, because verification is parallelizable, while genera‐
tion is sequential. Speculative decoding effectively turns the computation profile
of decoding into that of prefilling.
2. In an output token sequence, some tokens are easier to predict than others. It’s
possible to find a weaker draft model capable of getting these easier-to-predict
tokens right, leading to a high acceptance rate of the draft tokens.
3. Decoding is memory bandwidth-bound, which means that during the coding
process, there are typically idle FLOPs that can be used for free verification.20
Acceptance rates are domain-dependent. For texts that follow specific structures like
code, the acceptance rate is typically higher. Larger values of K mean fewer verifying
calls for the target model but a low acceptance rate of the draft tokens. The draft
model can be of any architecture, though ideally it should share the same vocabulary
and tokenizer as the target model. You can train a custom draft model or use an
existing weaker model.
Inference Optimization  | 429

[Visual content extracted via GLM-OCR]

Figure 9-9. A draft model generates a sequence of $K$ tokens, and the main model accepts the longest subsequence that it agrees with. The image is from “Blockwise Parallel Decoding for Deep Autoregressive Models” (Stern et al., 2018).

If all draft sequences are rejected, the target model must generate the entire response in addition to verifying it, potentially leading to increased latency. However, this can be avoided because of these three insights:

1. The time it takes for the target model to verify a sequence of tokens is less than the time it takes to generate it, because verification is parallelizable, while generation is sequential. Speculative decoding effectively turns the computation profile of decoding into that of prefilling.

2. In an output token sequence, some tokens are easier to predict than others. It’s possible to find a weaker draft model capable of getting these easier-to-predict tokens right, leading to a high acceptance rate of the draft tokens.

3. Decoding is memory bandwidth-bound, which means that during the coding process, there are typically idle FLOPs that can be used for free verification.

Acceptance rates are domain-dependent. For texts that follow specific structures like code, the acceptance rate is typically higher. Larger values of $K$ mean fewer verifying calls for the target model but a low acceptance rate of the draft tokens. The draft model can be of any architecture, though ideally it should share the same vocabulary and tokenizer as the target model. You can train a custom draft model or use an existing weaker model.

20 This also means that if your MFU is already maxed out, speculative decoding makes less sense.

For example, to speed up the decoding process of Chinchilla-70B, DeepMind trained
a 4B-parameter draft model of the same architecture ( Chen et al., 2023 ). The draft
model can generate a token eight times faster than the target model (1.8 ms/token
compared to 14.1 ms/token). This reduces the overall response latency by more than
half without compromising response quality. A similar speed-up was achieved for
T5-XXL (Laviathan et al., 2022).
This approach has gained traction because it’s relatively easy to implement and
doesn’t change a model’s quality. For example, it’s possible to do so in 50 lines of
code in PyTorch . It’s been incorporated into popular inference frameworks such as
vLLM, TensorRT-LLM, and llama.cpp.
Inference with reference.    Often, a response needs to reference tokens from the input.
For example, if you ask your model a question about an attached document, the
model might repeat a chunk of text verbatim from the document. Another example is
if you ask the model to fix bugs in a piece of code, the model might reuse the majority
of the original code with minor changes. Instead of making the model generate these
repeated tokens, what if we copy these tokens from the input to speed up the genera‐
tion? This is the core idea behind inference with reference.
Inference with reference is similar to speculative decoding, but instead of using a
model to generate draft tokens, it selects draft tokens from the input. The key chal‐
lenge is to develop an algorithm to identify the most relevant text span from the con‐
text at each decoding step. The simplest option is to find a text span that matches the
current tokens.
Unlike speculative decoding, inference with reference doesn’t require an extra model.
However, it’s useful only in generation scenarios where there’s a significant overlap
between contexts and outputs, such as in retrieval systems, coding, or multi-turn
conversations. In “Inference with Reference: Lossless Acceleration of Large Language
Models” ( Yang et al., 2023 ), this technique helps achieve two times generation
speedup in such use cases.
Examples of how inference with reference works are shown in Figure 9-10.
430 | Chapter 9: Inference Optimization

Figure 9-10. Two examples of inference with reference. The text spans that are success‐
fully copied from the input are in red and green. Image from Yang et al. (2023). The
image is licensed under CC BY 4.0.
Inference Optimization  | 431

[Visual content extracted via GLM-OCR]

Figure 9-10. Two examples of inference with reference. The text spans that are successfully copied from the input are in red and green. Image from Yang et al. (2023). The image is licensed under CC BY 4.0.

21 The Jacobi method is an iterative algorithm where multiple parts of a solution can be updated simultaneously
and independently.
Parallel decoding.    Instead of making autoregressive generation faster with draft
tokens, some techniques aim to break the sequential dependency. Given an existing
sequence of tokens x1, x2,…, xt, these techniques attempt to generate xt + 1, xt + 2,…, xt + k
simultaneously. This means that the model generates xt + 2  before it knows that the
token before it is xt + 1.
This can work because the knowledge of the existing sequence often is sufficient to
predict the next few tokens. For example, given “the cat sits”, without knowing that
the next token is “on”, “under”, or “behind”, you might still predict that the word
after it is “the”.
The parallel tokens can be generated by the same decoder, as in Lookahead decoding
(Fu et al., 2024 ), or by different decoding heads, as in Medusa ( Cai et al., 2024 ). In
Medusa, the original model is extended with multiple decoding heads, and each head
is a small neural network layer that is then trained to predict a future token at a spe‐
cific position. If the original model is trained to predict the next token xt + 1 , the kth
head will predict the token xt + k + 1. These heads are trained together with the original
model, but the original model is frozen. NVIDIA claimed Medusa helped boost
Llama 3.1 token generation by up to 1.9× on their HGX H200 GPUs ( Eassa et al.,
2024).
However, because these tokens aren’t generated sequentially, they need to be verified
to make sure that they fit together. An essential part of parallel decoding is verifica‐
tion and integration. Lookahead decoding uses the Jacobi method21 to verify the gen‐
erated tokens, which works as follows:
1. K future tokens are generated in parallel.
2. These K tokens are verified for coherence and consistency with the context.
3. If one or more tokens fail verification, instead of aggregating all K future tokens,
the model regenerates or adjusts only these failed tokens.
The model keeps refining the generated tokens until they all pass verification and are
integrated into the final output. This family of parallel decoding algorithms is also
called Jacobi decoding.
On the other hand, Medusa uses a tree-based attention mechanism to verify and inte‐
grate tokens. Each Medusa head produces several options for each position. These
options are then organized into a tree-like structure to select the most promising
combination. The process is visualized in Figure 9-11.
432 | Chapter 9: Inference Optimization

Figure 9-11. In Medusa (Cai et al., 2024), each head predicts several options for a token position. The most promising sequence from these options is selected. Image adapted from the paper, which is licensed under CC BY 4.0.

While the perspective of being able to circumvent sequential dependency is appealing, parallel decoding is not intuitive, and some techniques, like Medusa, can be challenging to implement.

Attention mechanism optimization

Recall from Chapter 2 that generating the next token requires the key and value vectors for all previous tokens. This means that the following applies:

• Generating token $x_t$ requires the key and value vectors for tokens $x_1, x_2, \ldots, x_{t-1}$.
• Generating token $x_{t+1}$ requires the key and value vectors for tokens $x_1, x_2, \ldots, x_{t-1}, x_t$.

When generating token $x_{t+1}$, instead of computing the key and value vectors for tokens $x_1, x_2, \ldots, x_{t-1}$ again, you reuse these vectors from the previous step. This means that you’ll need to compute the key and value vectors for only the most recent token, $x_t$. The cache that stores key and value vectors for reuse is called the KV cache. The newly computed key and value vectors are then added to the KV cache, which is visualized in Figure 9-12.

22 The number of attention computations for an autoregressive model is O(n2).
Figure 9-12. To avoid recomputing the key and value vectors at each decoding step, use
a KV cache to store these vectors to reuse.
A KV cache is used only during inference, not training. During
training, because all tokens in a sequence are known in advance,
next token generation can be computed all at once instead of
sequentially, as during inference. Therefore, there’s no need for a
KV cache.
Because generating a token requires computing the attention scores with all previous
tokens, the number of attention computations grows exponentially with sequence
length.22 The KV cache size, on the other hand, grows linearly with sequence length.
The KV cache size also grows with larger batch sizes. A Google paper calculated that
for a 500B+ model with multi-head attention, batch size 512, and context length
2048, the KV cache totals 3TB (Pope et al., 2022) . This is three times the size of that
model’s weights.
The KV cache size is ultimately limited by the available hardware storage, creating a
bottleneck for running applications with long context. A large cache size also takes
time to load into memory, which can be an issue for applications with strict latency.
The computation and memory requirements of the attention mechanism are one of
the reasons why it’s so hard to have longer context.
Many techniques have been developed to make the attention mechanism more effi‐
cient. In general, they fall into three buckets: redesigning the attention mechanism,
optimizing the KV cache, and writing kernels for attention computation.
434 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

A KV cache is used only during inference, not training. During training, because all tokens in a sequence are known in advance, next token generation can be computed all at once instead of sequentially, as during inference. Therefore, there’s no need for a KV cache.

Because generating a token requires computing the attention scores with all previous tokens, the number of attention computations grows exponentially with sequence length. The KV cache size, on the other hand, grows linearly with sequence length.

The KV cache size also grows with larger batch sizes. A Google paper calculated that for a 500B+ model with multi-head attention, batch size 512, and context length 2048, the KV cache totals 3TB (Pope et al., 2022). This is three times the size of that model’s weights.

The KV cache size is ultimately limited by the available hardware storage, creating a bottleneck for running applications with long context. A large cache size also takes time to load into memory, which can be an issue for applications with strict latency.

The computation and memory requirements of the attention mechanism are one of the reasons why it’s so hard to have longer context.

Many techniques have been developed to make the attention mechanism more efficient. In general, they fall into three buckets: redesigning the attention mechanism, optimizing the KV cache, and writing kernels for attention computation.

22 The number of attention computations for an autoregressive model is $O(n^2)$.

Calculating the KV Cache Size
The memory needed for the KV cache, without any optimization, is calculated as
follows:
2 × B × S × L × H × M
• B: batch size
• S: sequence length
• L: number of transformer layers
• H: model dimension
• M: memory needed for the cache’s numerical representation (e.g., FP16 or FP32).
This value can become substantial as the context length increases. For example,
LLama 2 13B has 40 layers and a model dimension of 5,120. With a batch size of 32,
sequence length of 2,048, and 2 bytes per value, the memory needed for its KV cache,
without any optimization, is 2 × 32 × 2,048 × 40 × 5,120 × 2 = 54 GB.
Redesigning the attention mechanism.    These techniques involve altering how the atten‐
tion mechanism works. Even though these techniques help optimize inference,
because they change a model’s architecture directly, they can be applied only during
training or finetuning.
For example, when generating a new token, instead of attending to all previous
tokens, local windowed attention attends only to a fixed size window of nearby tokens
(Beltagy et al., 2020 ). This reduces the effective sequence length to a fixed size win‐
dow, reducing both the KV cache and the attention computation. If the average
sequence length is 10,000 tokens, attending to a window size of 1,000 tokens reduces
the KV cache size by 10 times.
Local windowed attention can be interleaved with global attention, with local atten‐
tion capturing nearby context; the global attention captures task-specific information
across the document.
Both cross-layer attention (Brandon et al., 2024 ) and multi-query attention (Shazeer,
2019) reduce the memory footprint of the KV cache by reducing the number of keyvalue pairs. Cross-layer attention shares key and value vectors across adjacent layers.
Having three layers sharing the same key-value vectors means reducing the KV cache
three times. On the other hand, multi-query attention shares key-value vectors across
query heads.
Inference Optimization  | 435

Grouped-query attention (Ainslie et al., 2023) is a generalization of multi-query atten‐
tion. Instead of using only one set of key-value pairs for all query heads, its groupedquery attention puts query heads into smaller groups and shares key-value pairs only
among query heads in the same group. This allows for a more flexible balance
between the number of query heads and the number of key-value pairs.
Character.AI, an AI chatbot application, shares that their average conversation has a
dialogue history of 180 messages (2024). Given the typically long sequences, the pri‐
mary bottleneck for inference throughput is the KV cache size. Three attention
mechanism designs—multi-query attention, interleaving local attention and global
attention, and cross-layer attention—help them reduce KV cache by over 20 times .
More importantly, this significant KV cache reduction means that memory is no
longer a bottleneck for them for serving large batch sizes.
Optimizing the KV cache size.    The way the KV cache is managed is critical in mitigating
the memory bottleneck during inference and enabling a larger batch size, especially
for applications with long context. Many techniques are actively being developed to
reduce and manage the KV cache.
One of the fastest growing inference frameworks, vLLM, gained popularity for intro‐
ducing PagedAttention, which optimizes memory management by dividing the KV
cache into non-contiguous blocks, reducing fragmentation, and enabling flexible
memory sharing to improve LLM serving efficiency (Kwon et al., 2023).
Other techniques include KV cache quantization ( Hooper et al., 2024 ; Kang et al.,
2024), adaptive KV cache compression ( Ge et al., 2023 ), and selective KV cache ( Liu
et al., 2024).
Writing kernels for attention computation.    Instead of changing the mechanism design
or optimizing the storage, this approach looks into how attention scores are compu‐
ted and finds ways to make this computation more efficient. This approach is the
most effective when it takes into account the hardware executing the computation.
The code optimized for a specific chip is called a kernel. Kernel writing will be dis‐
cussed further in the next section.
One of the most well-known kernels optimized for attention computation is FlashAt‐
tention (Dao et al., 2022). This kernel fused together many operations commonly
used in a transformer-based model to make them run faster, as shown in Figure 9-13.
436 | Chapter 9: Inference Optimization

23 Convolution operations are often used in image generation models like Stable Diffusion.
Figure 9-13. FlashAttention is a kernel that fuses together several common operators.
Adapted from an original image licensed under BSD 3-Clause.
Kernels and compilers
Kernels are specialized pieces of code optimized for specific hardware accelerators,
such as GPUs or TPUs. They are typically written to perform computationally inten‐
sive routines that need to be executed repeatedly, often in parallel, to maximize the
performance of these accelerators.
Common AI operations, including matrix multiplication, attention computation, and
convolution operation, all have specialized kernels to make their computation more
efficient on different hardware.23
Writing kernels requires a deep understanding of the underlying hardware architec‐
ture. This includes knowledge about how the memory hierarchy is structured (such
as caches, global memory, shared memory, and registers) and how data is accessed
and moved between these different levels.
Moreover, kernels are typically written in lower-level programming languages like
CUDA (for NVIDIA GPUs), Triton (a language developed by OpenAI for writing
custom kernels), and ROCm (for AMD GPUs). These languages allow fine-grained
control over thread management and memory access but are also harder to learn
than the languages that most AI engineers are familiar with, like Python.
Due to this entry barrier, writing kernels used to be a dark art practiced by a few.
Chip makers like NVIDIA and AMD employ optimization engineers to write kernels
to make their hardware efficient for AI workloads, whereas AI frameworks like
Inference Optimization  | 437

[Visual content extracted via GLM-OCR]

Kernels and compilers

Kernels are specialized pieces of code optimized for specific hardware accelerators, such as GPUs or TPUs. They are typically written to perform computationally intensive routines that need to be executed repeatedly, often in parallel, to maximize the performance of these accelerators.

Common AI operations, including matrix multiplication, attention computation, and convolution operation, all have specialized kernels to make their computation more efficient on different hardware.$^{23}$

Writing kernels requires a deep understanding of the underlying hardware architecture. This includes knowledge about how the memory hierarchy is structured (such as caches, global memory, shared memory, and registers) and how data is accessed and moved between these different levels.

Moreover, kernels are typically written in lower-level programming languages like CUDA (for NVIDIA GPUs), Triton (a language developed by OpenAI for writing custom kernels), and ROCm (for AMD GPUs). These languages allow fine-grained control over thread management and memory access but are also harder to learn than the languages that most AI engineers are familiar with, like Python.

Due to this entry barrier, writing kernels used to be a dark art practiced by a few. Chip makers like NVIDIA and AMD employ optimization engineers to write kernels to make their hardware efficient for AI workloads, whereas AI frameworks like

$^{23}$ Convolution operations are often used in image generation models like Stable Diffusion.

PyTorch and TensorFlow employ kernel engineers to optimize their frameworks on
different accelerators.
However, with the rising demand for inference optimization and the ubiquity of
accelerators, more AI engineers have taken an interest in writing kernels. There are
many great online tutorials for kernel writing. Here, I’ll cover four common tech‐
niques often used to speed up computation:
Vectorization
Given a loop or a nested loop, instead of processing one data element at a time,
simultaneously execute multiple data elements that are contiguous in memory.
This reduces latency by minimizing data I/O operations.
Parallelization
Divide an input array (or n-dimensional array) into independent chunks that can
be processed simultaneously on different cores or threads, speeding up the com‐
putation.
Loop tiling
Optimize the data accessing order in a loop for the hardware’s memory layout
and cache. This optimization is hardware-dependent. An efficient CPU tiling
pattern may not work well on GPUs.
Operator fusion
Combine multiple operators into a single pass to avoid redundant memory
access. For example, if two loops operate over the same array, they can be fused
into one, reducing the number of times data is read and written.
While vectorization, parallelization, and loop tiling can be applied broadly across
different models, operator fusion requires a deeper understanding of a model’s
specific operators and architecture. As a result, operator fusion demands more
attention from optimization engineers.
Kernels are optimized for a hardware architecture. This means that whenever a new
hardware architecture is introduced, new kernels need to be developed. For example,
FlashAttention (Dao et al., 2022) was originally developed primarily for NVIDIA
A100 GPUs. Later on, FlashAttention-3 was introduced for H100 GPUs ( Shah et al.,
2024).
A model script specifies a series of operations that need to be performed to execute
that model. To run this code on a piece of hardware, such as a GPU, it has to be con‐
verted into a language compatible with that hardware. This process is called lowering.
A tool that lowers code to run a specific hardware is called a compiler. Compilers
bridge ML models and the hardware they run on. During the lowering process,
whenever possible, these operations are converted into specialized kernels to run
faster on the target hardware.
438 | Chapter 9: Inference Optimization

Inference Optimization Case Study from PyTorch
Figure 9-14 shows how much throughput improvement the PyTorch team could give
to Llama-7B through the following optimization steps (PyTorch, 2023):
1. Call torch.compile to compile the model into more efficient kernels.
2. Quantize the model weights to INT8.
3. Further quantize the model weights to INT4.
4. Add speculative decoding.
Figure 9-14. Throughput improvement by different optimization techniques in
PyTorch. Image from PyTorch (2023).
The experiment was run on an A100 GPU with 80 GB of memory. It was unclear how
these optimization steps impact the model’s output quality.
Inference Optimization  | 439

[Visual content extracted via GLM-OCR]

Inference Optimization Case Study from PyTorch

Figure 9-14 shows how much throughput improvement the PyTorch team could give to Llama-7B through the following optimization steps (PyTorch, 2023):

1. Call torch.compile to compile the model into more efficient kernels.
2. Quantize the model weights to INT8.
3. Further quantize the model weights to INT4.
4. Add speculative decoding.

Figure 9-14. Throughput improvement by different optimization techniques in PyTorch. Image from PyTorch (2023).

The experiment was run on an A100 GPU with 80 GB of memory. It was unclear how these optimization steps impact the model’s output quality.
