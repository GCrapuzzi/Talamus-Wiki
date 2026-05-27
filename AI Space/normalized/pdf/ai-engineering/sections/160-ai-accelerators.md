---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 160
section-title: AI Accelerators
source-location: pages 443-449
previous-section: AI Space/normalized/pdf/ai-engineering/sections/159-inference-performance-metrics.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/161-inference-optimization.md
classification: reusable-knowledge-candidate
---
# AI Accelerators

13 In the 1960s, computers could run only one-layer neural networks, which had very limited capabilities. In
their famous 1969 book Perceptrons: An Introduction to Computational Geometry (MIT Press), two AI pio‐
neers, Marvin Minsky and Seymour Papert, argued that neural networks with hidden layers would still be
able to do little. Their exact quote was: “Virtually nothing is known about the computational capabilities of
this latter kind of machine. We believe that it can do little more than can a low order perceptron.” There
wasn’t sufficient compute power to dispute their argument, which was then cited by many people as a key
reason for the drying up of AI funding in the 1970s.
14 There have been discussions on whether to rename the GPU since it’s used for a lot more than graphics (Jon
Peddie, “Chasing Pixels,” July 2018). Jensen Huang, NVIDIA’s CEO, said in an interview (Stratechery, March
2022) that once the GPU took off and they added more capabilities to it, they considered renaming it to
something more general like GPGPU (general-purpose GPU) or XGU. They decided against renaming
because they assumed that people who buy GPUs will be smart enough to know what a GPU is good for
beyond its name.
Utilization metrics are helpful to track your system’s efficiency. Higher utilization
rates for similar workloads on the same hardware generally mean that your services
are becoming more efficient. However, the goal isn’t to get the chips with the highest
utilization. What you really care about is how to get your jobs done faster and
cheaper. A higher utilization rate means nothing if the cost and latency both increase.
AI Accelerators
How fast and cheap software can run depends on the hardware it runs on. While
there are optimization techniques that work across hardware, understanding hard‐
ware allows for deeper optimization. This section looks at hardware from an infer‐
ence perspective, but it can be applied to training as well.
The development of AI models and hardware has always been intertwined. The lack
of sufficiently powerful computers was one of the contributing factors to the first AI
winter in the 1970s.13
The revival of interest in deep learning in 2012 was also closely tied to compute. One
commonly acknowledged reason for the popularity of AlexNet ( Krizhevsky et al.,
2012) is that it was the first paper to successfully use GPUs, graphics processing units,
to train neural networks. 14 Before GPUs, if you wanted to train a model at AlexNet’s
scale, you’d have to use thousands of CPUs, like the one Google released just a few
months before AlexNet . Compared to thousands of CPUs, a couple of GPUs were a
lot more accessible to PhD students and researchers, setting off the deep learning
research boom.
Understanding Inference Optimization | 419

15 Matrix multiplication, affectionately known as matmul, is estimated to account for more than 90% of all float‐
ing point operations in a neural network, according to “Data Movement Is All You Need: A Case Study on
Optimizing Transformers”  (Ivanov et al., arXiv, v3, November 2021) and “Scalable MatMul-free Language
Modeling”  (Zhu et al., arXiv, June 2024).
What’s an accelerator?
An accelerator is a chip designed to accelerate a specific type of computational work‐
load. An AI accelerator is designed for AI workloads. The dominant type of AI accel‐
erator is GPUs, and the biggest economic driver during the AI boom in the early
2020s is undoubtedly NVIDIA.
The main difference between CPUs and GPUs is that CPUs are designed for generalpurpose usage, whereas GPUs are designed for parallel processing:
• CPUs have a few powerful cores, typically up to 64 cores for high-end consumer
machines. While many CPU cores can handle multi-threaded workloads effec‐
tively, they excel at tasks requiring high single-thread performance, such as run‐
ning an operating system, managing I/O (input/output) operations, or handling
complex, sequential processes.
• GPUs have thousands of smaller, less powerful cores optimized for tasks that can
be broken down into many smaller, independent calculations, such as graphics
rendering and machine learning. The operation that constitutes most ML work‐
loads is matrix multiplication, which is highly parallelizable.15
While the pursuit of efficient parallel processing increases computational capabilities,
it imposes challenges on memory design and power consumption.
The success of NVIDIA GPUs has inspired many accelerators designed to speed up
AI workloads, including Advanced Micro Devices (AMD)’s newer generations of
GPUs, Google’s TPU ( Tensor Processing Unit ), Intel’s Habana Gaudi , Graphcore’s
Intelligent Processing Unit (IPU), Groq’s Language Processing Unit  (LPU), Cerebras’
Wafer-Scale Quant Processing Unit (QPU), and many more being introduced.
While many chips can handle both training and inference, one big theme emerging is
specialized chips for inference. A survey by Desislavov et al. (2023)  shares that infer‐
ence can exceed the cost of training in commonly used systems, and that inference
accounts for up to 90% of the machine learning costs for deployed AI systems.
420 | Chapter 9: Inference Optimization

16 While a chip can be developed to run one model architecture, a model architecture can be developed to make
the most out of a chip, too. For example, the transformer was originally designed by Google to run fast on
TPUs and only later optimized on GPUs.
As discussed in Chapter 7, training demands much more memory due to backpropa‐
gation and is generally more difficult to perform in lower precision. Furthermore,
training usually emphasizes throughput, whereas inference aims to minimize latency.
Consequently, chips designed for inference are often optimized for lower precision
and faster memory access, rather than large memory capacity. Examples of such
chips include the Apple Neural Engine, AWS Inferentia, and MTIA (Meta Training
and Inference Accelerator). Chips designed for edge computing, like Google’s Edge
TPU and the NVIDIA Jetson Xavier, are also typically geared toward inference.
There are also chips specialized for different model architectures, such as chips speci‐
alized for the transformer. 16 Many chips are designed for data centers, with more and
more being designed for consumer devices (such as phones and laptops).
Different hardware architectures have different memory layouts and specialized com‐
pute units that evolve over time. These units are optimized for specific data types,
such as scalars, vectors, or tensors, as shown in Figure 9-6.
Figure 9-6. Different compute primitives. Image inspired by Chen et al. (2018).
A chip might have a mixture of different compute units optimized for various data
types. For example, GPUs traditionally supported vector operations, but many
modern GPUs now include tensor cores optimized for matrix and tensor computa‐
tions. TPUs, on the other hand, are designed with tensor operations as their primary
compute primitive. To efficiently operate a model on a hardware architecture, its
memory layout and compute primitives need to be taken into account.
A chip’s specifications contain many details that can be useful when evaluating this
chip for each specific use case. However, the main characteristics that matter across
use cases are computational capabilities, memory size and bandwidth, and power
consumption. I’ll use GPUs as examples to illustrate these characteristics.
Understanding Inference Optimization | 421

[Visual content extracted via GLM-OCR]

As discussed in Chapter 7, training demands much more memory due to backpropagation and is generally more difficult to perform in lower precision. Furthermore, training usually emphasizes throughput, whereas inference aims to minimize latency.

Consequently, chips designed for inference are often optimized for lower precision and faster memory access, rather than large memory capacity. Examples of such chips include the Apple Neural Engine, AWS Inferentia, and MTIA (Meta Training and Inference Accelerator). Chips designed for edge computing, like Google’s Edge TPU and the NVIDIA Jetson Xavier, are also typically geared toward inference.

There are also chips specialized for different model architectures, such as chips specialized for the transformer. Many chips are designed for data centers, with more and more being designed for consumer devices (such as phones and laptops).

Different hardware architectures have different memory layouts and specialized compute units that evolve over time. These units are optimized for specific data types, such as scalars, vectors, or tensors, as shown in Figure 9-6.

Figure 9-6. Different compute primitives. Image inspired by Chen et al. (2018).

A chip might have a mixture of different compute units optimized for various data types. For example, GPUs traditionally supported vector operations, but many modern GPUs now include tensor cores optimized for matrix and tensor computations. TPUs, on the other hand, are designed with tensor operations as their primary compute primitive. To efficiently operate a model on a hardware architecture, its memory layout and compute primitives need to be taken into account.

A chip’s specifications contain many details that can be useful when evaluating this chip for each specific use case. However, the main characteristics that matter across use cases are computational capabilities, memory size and bandwidth, and power consumption. I’ll use GPUs as examples to illustrate these characteristics.

16 While a chip can be developed to run one model architecture, a model architecture can be developed to make the most out of a chip, too. For example, the transformer was originally designed by Google to run fast on TPUs and only later optimized on GPUs.

Computational capabilities
Computational capabilities are typically measured by the number of operations a
chip can perform in a given time. The most common metric is FLOP/s, often written
as FLOPS, which measures the peak number of floating-point operations per second.
In reality, however, it’s very unlikely that an application can achieve this peak
FLOP/s. The ratio between the actual FLOP/s and the theoretical FLOP/s is one uti‐
lization metric.
The number of operations a chip can perform in a second depends on the numerical
precision—the higher the precision, the fewer operations the chip can execute. Think
about how adding two 32-bit numbers generally requires twice the computation of
adding two 16-bit numbers. The number of 32-bit operations a chip can perform in a
given time is not exactly half that of 16-bit operations because of different chips’ opti‐
mization. For an overview of numerical precision, revisit “Numerical Representa‐
tions” on page 325 .
Table 9-2 shows the FLOP/s specs for different precision formats for NVIDIA H100
SXM chips.
Table 9-2. FLOP/s specs for NVIDIA H100 SXM chips.
Numerical precision teraFLOP/s (trillion FLOP/s) with sparsity
TF32 Tensor Core a 989
BFLOAT16 Tensor Core 1,979
FP16 Tensor Core 1,979
FP8 Tensor Core 3,958
a Recall from Chapter 7 that TF32 is a 19-bit, not 32-bit, format.
Memory size and bandwidth
Because a GPU has many cores working in parallel, data often needs to be moved
from the memory to these cores, and, therefore, data transfer speed is important.
Data transfer is crucial when working with AI models that involve large weight
matrices and training data. These large amounts of data need to be moved quickly to
keep the cores efficiently occupied. Therefore, GPU memory needs to have higher
bandwidth and lower latency than CPU memory, and thus, GPU memory requires
more advanced memory technologies. This is one of the factors that makes GPU
memory more expensive than CPU memory.
422 | Chapter 9: Inference Optimization

17 Lower-end to mid-range GPUs might use GDDR (Graphics Double Data Rate) memory.
To be more specific, CPUs typically use DDR SDRAM (Double Data Rate Synchro‐
nous Dynamic Random-Access Memory), which has a 2D structure. GPUs, particu‐
larly high-end ones, often use HBM (high-bandwidth memory), which has a 3D
stacked structure.17
An accelerator’s memory is measured by its size and bandwidth. These numbers need
to be evaluated within the system an accelerator is part of. An accelerator, such as a
GPU, typically interacts with three levels of memory, as visualized in Figure 9-7:
CPU memory (DRAM)
Accelerators are usually deployed alongside CPUs, giving them access to the
CPU memory (also known as system memory, host memory, or just CPU
DRAM).
CPU memory usually has the lowest bandwidth among these memory types, with
data transfer speeds ranging from 25 GB/s to 50 GB/s. CPU memory size varies.
Average laptops might have around 16–64 GB, whereas high-end workstations
can have one TB or more.
GPU high-bandwidth memory (HBM)
This is the memory dedicated to the GPU, located close to the GPU for faster
access than CPU memory.
HBM provides significantly higher bandwidth, with data transfer speeds typically
ranging from 256 GB/s to over 1.5 TB/s. This speed is essential for efficiently
handling large data transfers and high-throughput tasks. A consumer GPU has
around 24–80 GB of HBM.
GPU on-chip SRAM
Integrated directly into the chip, this memory is used to store frequently accessed
data and instructions for nearly instant access. It includes L1 and L2 caches made
of SRAM, and, in some architectures, L3 caches as well. These caches are part of
the broader on-chip memory, which also includes other components like register
files and shared memory.
RAM has extremely high data transfer speeds, often exceeding 10 TB/s. The size
of GPU SRAM is small, typically 40 MB or under.
Understanding Inference Optimization | 423

18 A main challenge in building data centers with tens of thousands of GPUs is finding a location that can guar‐
antee the necessary electricity. Building large-scale data centers requires navigating electricity supply, speed,
and geopolitical constraints. For example, remote regions might provide cheaper electricity but can increase
network latency, making the data centers less appealing for use cases with stringent latency requirements like
inference.
Figure 9-7. The memory hierarchy of an AI accelerator. The numbers are for reference
only. The actual numbers vary for each chip.
A lot of GPU optimization is about how to make the most out of this memory hierar‐
chy. However, as of this writing, popular frameworks such as PyTorch and Tensor‐
Flow don’t yet allow fine-grained control of memory access. This has led many AI
researchers and engineers to become interested in GPU programming languages such
as CUDA (originally Compute Unified Device Architecture), OpenAI’s Triton , and
ROCm (Radeon Open Compute). The latter is AMD’s open source alternative to
NVIDIA’s proprietary CUDA.
Power consumption
Chips rely on transistors to perform computation. Each computation is done by tran‐
sistors switching on and off, which requires energy. A GPU can have billions of tran‐
sistors—an NVIDIA A100 has 54 billion transistors, while an NVIDIA H100 has 80
billion. When an accelerator is used efficiently, billions of transistors rapidly switch
states, consuming a substantial amount of energy and generating a nontrivial amount
of heat. This heat requires cooling systems, which also consume electricity, adding to
data centers’ overall energy consumption.
Chip energy consumption threatens to have a staggering impact on the environment,
increasing the pressure on companies to invest in technologies for green data centers.
An NVIDIA H100 running at its peak for a year consumes approximately 7,000 kWh.
For comparison, the average US household’s annual electricity consumption is 10,000
kWh. That’s why electricity is a bottleneck to scaling up compute. 18
424 | Chapter 9: Inference Optimization

[Visual content extracted via GLM-OCR]

A lot of GPU optimization is about how to make the most out of this memory hierarchy. However, as of this writing, popular frameworks such as PyTorch and TensorFlow don’t yet allow fine-grained control of memory access. This has led many AI researchers and engineers to become interested in GPU programming languages such as CUDA (originally Compute Unified Device Architecture), OpenAI’s Triton, and ROCm (Radeon Open Compute). The latter is AMD’s open source alternative to NVIDIA’s proprietary CUDA.

Power consumption

Chips rely on transistors to perform computation. Each computation is done by transistors switching on and off, which requires energy. A GPU can have billions of transistors—an NVIDIA A100 has 54 billion transistors, while an NVIDIA H100 has 80 billion. When an accelerator is used efficiently, billions of transistors rapidly switch states, consuming a substantial amount of energy and generating a nontrivial amount of heat. This heat requires cooling systems, which also consume electricity, adding to data centers’ overall energy consumption.

Chip energy consumption threatens to have a staggering impact on the environment, increasing the pressure on companies to invest in technologies for green data centers. An NVIDIA H100 running at its peak for a year consumes approximately 7,000 kWh. For comparison, the average US household’s annual electricity consumption is 10,000 kWh. That’s why electricity is a bottleneck to scaling up compute.

18 A main challenge in building data centers with tens of thousands of GPUs is finding a location that can guarantee the necessary electricity. Building large-scale data centers requires navigating electricity supply, speed, and geopolitical constraints. For example, remote regions might provide cheaper electricity but can increase network latency, making the data centers less appealing for use cases with stringent latency requirements like inference.

Accelerators typically specify their power consumption under maximum power draw
or a proxy metric TDP (thermal design power):
• Maximum power draw indicates the peak power that the chip could draw under
full load.
• TDP represents the maximum heat a cooling system needs to dissipate when the
chip operates under typical workloads. While it’s not an exact measure of power
consumption, it’s an indication of the expected power draw. For CPUs and
GPUs, the maximum power draw can be roughly 1.1 to 1.5 times the TDP,
though the exact relationship varies depending on the specific architecture and
workload.
If you opt for cloud providers, you won’t need to worry about cooling or electricity.
However, these numbers can still be of interest to understand the impact of accelera‐
tors on the environment and the overall electricity demand.
Selecting Accelerators
What accelerators to use depends on your workload. If your workloads are computebound, you might want to look for chips with more FLOP/s. If your workloads are
memory-bound, shelling out money for chips with higher bandwidth and more
memory will make your life easier.
When evaluating which chips to buy, there are three main questions:
• Can the hardware run your workloads?
• How long does it take to do so?
• How much does it cost?
FLOP/s, memory size, and memory bandwidth are the three big numbers that help
you answer the first two questions. The last question is straightforward. Cloud pro‐
viders’ pricing is typically usage-based and fairly similar across providers. If you buy
your hardware, the cost can be calculated based on the initial price and ongoing
power consumption.
Understanding Inference Optimization | 425
