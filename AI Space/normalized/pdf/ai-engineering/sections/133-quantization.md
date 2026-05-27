---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 133
section-title: Quantization
source-location: pages 352-355
previous-section: AI Space/normalized/pdf/ai-engineering/sections/132-numerical-representations.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/134-finetuning-techniques.md
classification: reusable-knowledge-candidate
---
# Quantization

15 The FP16 and BF16 confusion continued with Llama 3.1. See X and Threads discussions: 1; 2, 3, 4; and
llama.cpp’s benchmark between BF16 and FP16, Bloke’s writeup , and Raschka’s writeup .
16 Designing numerical formats is a fascinating discipline. Being able to create a lower-precision format that
doesn’t compromise a system’s quality can make that system much cheaper and faster, enabling new use
cases.
When using a model, make sure to load the model in the format
it’s intended for. Loading a model into the wrong numerical
format can cause the model to change significantly. For example,
Llama 2 had its weights set to BF16 when it came out. However,
many teams loaded the model in FP16 and were subsequently frus‐
trated to find the model’s quality much worse than advertised .15
While this misunderstanding wasted a lot of people’s time, the
upside is that it forced many people to learn about numerical
representations.
The right format for you depends on the distribution of numerical values of your
workload (such as the range of values you need), how sensitive your workload is to
small numerical changes, and the underlying hardware.16
Quantization
The fewer bits needed to represent a model’s values, the lower the model’s memory
footprint will be. A 10B-parameter model in a 32-bit format requires 40 GB for its
weights, but the same model in a 16-bit format will require only 20 GB. Reducing
precision, also known as quantization, is a cheap and extremely effective way to
reduce a model’s memory footprint. It’s straightforward to do and generalizes over
tasks and architectures. In the context of ML, low precision generally refers to any
format with fewer bits than the standard FP32.
Quantization Versus Reduced Precision
Strictly speaking, it’s quantization only if the target format is integer. However, in
practice, quantization is used to refer to all techniques that convert values to a lowerprecision format. In this book, I use quantization to refer to precision reduction, to
keep it consistent with the literature.
328 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

When using a model, make sure to load the model in the format it’s intended for. Loading a model into the wrong numerical format can cause the model to change significantly. For example, Llama 2 had its weights set to BF16 when it came out. However, many teams loaded the model in FP16 and were subsequently frustrated to find the model’s quality much worse than advertised. While this misunderstanding wasted a lot of people’s time, the upside is that it forced many people to learn about numerical representations.

The right format for you depends on the distribution of numerical values of your workload (such as the range of values you need), how sensitive your workload is to small numerical changes, and the underlying hardware.

Quantization

The fewer bits needed to represent a model’s values, the lower the model’s memory footprint will be. A 10B-parameter model in a 32-bit format requires 40 GB for its weights, but the same model in a 16-bit format will require only 20 GB. Reducing precision, also known as quantization, is a cheap and extremely effective way to reduce a model’s memory footprint. It’s straightforward to do and generalizes over tasks and architectures. In the context of ML, low precision generally refers to any format with fewer bits than the standard FP32.

Quantization Versus Reduced Precision

Strictly speaking, it’s quantization only if the target format is integer. However, in practice, quantization is used to refer to all techniques that convert values to a lower-precision format. In this book, I use quantization to refer to precision reduction, to keep it consistent with the literature.

15 The FP16 and BF16 confusion continued with Llama 3.1. See X and Threads discussions: 1; 2, 3, 4; and llama.cpp’s benchmark between BF16 and FP16, Bloke’s writeup, and Raschka’s writeup.

16 Designing numerical formats is a fascinating discipline. Being able to create a lower-precision format that doesn’t compromise a system’s quality can make that system much cheaper and faster, enabling new use cases.

17 Another major contributor to the memory footprint of transformer-based models is the KV cache, which is
discussed in Chapter 9.
18 The smallest possible float size that follows all IEEE principles is 4-bit.
To do quantization, you need to decide what to quantize and when:
What to quantize
Ideally, you want to quantize whatever is consuming most of your memory, but
it also depends on what you can quantize without hurting performance too
much. As discussed in “Memory Math” on page 322, major contributors to a
model’s memory footprint during inference are the model’s weights and activa‐
tions.17 Weight quantization is more common than activation quantization, since
weight activation tends to have a more stable impact on performance with less
accuracy loss.
When to quantize
Quantization can happen during training or post-training. Post-training quanti‐
zation (PTQ) means quantizing a model after it’s been fully trained. PTQ is by
far the most common. It’s also more relevant to AI application developers who
don’t usually train models.
Inference quantization
In the early days of deep learning, it was standard to train and serve models using 32
bits with FP32. Since the late 2010s, it has become increasingly common to serve
models in 16 bits and in even lower precision. For example, Dettmers et al. (2022)
have done excellent work quantizing LLMs into 8 bits with LLM.int8() and 4 bits
with QLoRA (Dettmers et al., 2023).
A model can also be served in mixed precision, where values are reduced in precision
when possible and maintained in higher precision when necessary. To serve models
on the devices, Apple (2024) leveraged a quantization scheme that uses a mixture of
2-bit and 4-bit formats, averaging 3.5 bits-per-weight. Also in 2024, in anticipation of
4-bit neural networks, NVIDIA announced their new GPU architecture, Blackwell,
that supports model inference in 4-bit float.
Once you get to 8 bits and under, numerical representations get more tricky. You can
keep parameter values as floats using one of the minifloat formats, such as FP8 (8
bits) and FP4 (4 bits). 18 More commonly, however, parameter values are converted
into an integer format, such as INT8 or INT4.
Memory Bottlenecks | 329

19 The authors of the Xnor-Net paper spun off Xnor.ai, a startup that focused on model compression. In early
2020, it was acquired by Apple for a reported $200M.
Quantization is effective, but there’s a limit to how far it can go. You can’t have fewer
than 1 bit per value, and some have attempted the 1-bit representation, e.g., Binary‐
Connect ( Courbariaux et al., 2015 ), Xnor-Net ( Rastegari et al., 2016 ), and BitNet
(Wang et al., 2023).19
In 2024, Microsoft researchers (Ma et al.) declared that we’re entering the era of 1-bit
LLMs by introducing BitNet b1.58, a transformer-based language model that requires
only 1.58 bits per parameter and whose performance is comparable to 16-bit Llama 2
(Touvron et al., 2023) up to 3.9B parameters, as shown in Table 7-4.
Table 7-4. BitNet b1.58’s performance compared to that of Llama 2 16-bit on different
benchmarks and at different model sizes, up to 3.9B parameters. Results from Ma et al.
(2024).
Model Size ARCe ARCc HS BQ OQ PQ WGe Avg.
Llama LLM 700M 54.7 23.0 37.0 60.0 20.2 68.9 54.8 45.5
BitNet b1.58 700M 51.8 21.4 35.1 58.2 20.0 68.1 55.2 44.3
Llama LLM 1.3B 56.9 23.5 38.5 59.1 21.6 70.0 53.9 46.2
BitNet b1.58 1.3B 54.9 24.2 37.7 56.7 19.6 68.8 55.8 45.4
Llama LLM 3B 62.1 25.6 43.3 61.8 24.6 72.1 58.2 49.7
BitNet b1.58 3B 61.4 28.3 42.9 61.5 26.6 71.5 59.3 50.2
BitNet b1.58 3.9B 64.2 28.7 44.2 63.5 24.2 73.2 60.5 51.2
Reduced precision not only reduces the memory footprint but also often improves
computation speed. First, it allows a larger batch size, enabling the model to process
more inputs in parallel. Second, reduced precision speeds up computation, which
further reduces inference latency and training time. To illustrate this, consider the
addition of two numbers. If we perform the addition bit by bit, and each takes t nano‐
seconds, it’ll take 32t nanoseconds for 32 bits but only 16t nanoseconds for 16 bits.
However, reducing precision doesn’t always reduce latency due to the added compu‐
tation needed for format conversion.
There are downsides to reduced precision. Each conversion often causes a small value
change, and many small changes can cause a big performance change. If a value is
outside the range the reduced precision format can represent, it might be converted
to infinity or an arbitrary value, causing the model’s quality to further degrade. How
to reduce precision with minimal impact on model performance is an active area of
research, pursued by model developers as well as by hardware makers and applica‐
tion developers.
330 | Chapter 7: Finetuning

20 During training, the model’s weights are updated via multiple steps. Small rounding changes can compound
during the training process, making it difficult for the model to achieve the desirable performance. On top of
that, loss values require precise computation. Small changes in the loss value can point parameter updates in
the wrong direction.
Inference in lower precision has become a standard. A model is trained using a
higher-precision format to maximize performance, then its precision is reduced for
inference. Major ML frameworks, including PyTorch, TensorFlow, and Hugging
Face’s transformers, offer PTQ for free with a few lines of code.
Some edge devices only support quantized inference. Therefore, frameworks for ondevice inference, such as TensorFlow Lite and PyTorch Mobile, also offer PTQ.
Training quantization
Quantization during training is not yet as common as PTQ, but it’s gaining traction.
There are two distinct goals for training quantization:
1. To produce a model that can perform well in low precision during inference.
This is to address the challenge that a model’s quality might degrade during posttraining quantization.
2. To reduce training time and cost. Quantization reduces a model’s memory foot‐
print, allowing a model to be trained on cheaper hardware or allowing the train‐
ing of a larger model on the same hardware. Quantization also speeds up
computation, which further reduces costs.
A quantization technique might help achieve one or both of these goals.
Quantization-aware training (QAT) aims to create a model with high quality in low
precision for inference. With QAT, the model simulates low-precision (e.g., 8-bit)
behavior during training, which allows the model to learn to produce high-quality
outputs in low precision. However, QAT doesn’t reduce a model’s training time since
its computations are still performed in high precision. QAT can even increase train‐
ing time due to the extra work of simulating low-precision behavior.
On the other hand, training a model directly in lower precision can help with both
goals. People attempted to train models in reduced precision as early as 2016; see
Hubara et al. (2016)  and Jacob et al. (2017) . Character.AI (2024)  shared that they
were able to train their models entirely in INT8, which helped eliminate the training/
serving precision mismatch while also significantly improving training efficiency.
However, training in lower precision is harder to do, as backpropgation is more sen‐
sitive to lower precision.20
Lower-precision training is often done in mixed precision , where a copy of the
weights is kept in higher precision but other values, such as gradients and activations,
Memory Bottlenecks | 331
