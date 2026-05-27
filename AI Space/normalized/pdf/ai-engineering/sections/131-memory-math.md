---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 131
section-title: Memory Math
source-location: pages 346-348
previous-section: AI Space/normalized/pdf/ai-engineering/sections/130-backpropagation-and-trainable-parameters.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/132-numerical-representations.md
classification: reusable-knowledge-candidate
---
# Memory Math

Figure 7-4. The forward and backward pass of a simple neural network.
During the backward pass, each trainable parameter comes with additional values, its
gradient, and its optimizer states. Therefore, the more trainable parameters there are,
the more memory is needed to store these additional values.
Memory Math
It’s useful to know how much memory a model needs so that you can use the right
hardware for it. Often, you might already have the hardware and need to calculate
whether you can afford to run a certain model. If a model requires 30 GB of memory
to do inference, a chip with 24 GB of memory won’t be sufficient.
A model’s memory footprint depends on the model as well as the workload and the
different optimization techniques used to reduce its memory usage. Because it’s
impossible to account for all optimization techniques and workloads, in this section,
I’ll outline only the formulas for approximate calculations, which should give you a
rough idea of how much memory you need to operate a model, both during inference
and training.
Inference and training having distinct memory profiles is one of
the reasons for the divergence in chips for training and inference,
as discussed in Chapter 9.
322 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

During the backward pass, each trainable parameter comes with additional values, its gradient, and its optimizer states. Therefore, the more trainable parameters there are, the more memory is needed to store these additional values.

Memory Math

It’s useful to know how much memory a model needs so that you can use the right hardware for it. Often, you might already have the hardware and need to calculate whether you can afford to run a certain model. If a model requires 30 GB of memory to do inference, a chip with 24 GB of memory won’t be sufficient.

A model’s memory footprint depends on the model as well as the workload and the different optimization techniques used to reduce its memory usage. Because it’s impossible to account for all optimization techniques and workloads, in this section, I’ll outline only the formulas for approximate calculations, which should give you a rough idea of how much memory you need to operate a model, both during inference and training.

Inference and training having distinct memory profiles is one of the reasons for the divergence in chips for training and inference, as discussed in Chapter 9.

8 Some might say that you’re not doing AI until you’ve seen a “RuntimeError: CUDA out of memory” error.
9 To learn more about inference memory calculation, check out Carol Chen’s “Transformer Inference Arith‐
metic” , kipply’s blog (March 2022).
Memory needed for inference
During inference, only the forward pass is executed. The forward pass requires mem‐
ory for the model’s weights. Let N be the model’s parameter count and M be the
memory needed for each parameter; the memory needed to load the model’s parame‐
ters is:
N × M
The forward pass also requires memory for activation values. Transformer models
need memory for key-value vectors for the attention mechanism. The memory for
both activation values and key-value vectors grows linearly with sequence length and
batch size.
For many applications, the memory for activation and key-value vectors can be
assumed to be 20% of the memory for the model’s weights. If your application uses a
longer context or larger batch size, the actual memory needed will be higher. This
assumption brings the model’s memory footprint to:
N × M × 1.2
Consider a 13B-parameter model. If each parameter requires 2 bytes, the model’s
weights will require 13B × 2 bytes = 26 GB. The total memory for inference will be 26
GB × 1.2 = 31.2 GB.
A model’s memory footprint grows rapidly with its size. As models become bigger,
memory becomes a bottleneck for operating them. 8 A 70B-parameter model with 2
bytes per parameter will require a whooping 140 GB of memory just for its weights.9
Memory needed for training
To train a model, you need memory for the model’s weights and activations, which
has already been discussed. Additionally, you need memory for gradients and opti‐
mizer states, which scales with the number of trainable parameters.
Overall, the memory needed for training is calculated as:
Training memory = model weights + activations + gradients + optimizer states
Memory Bottlenecks | 323

During the backward pass, each trainable parameter requires one value for gradient plus zero to two values for optimizer states, depending on the optimizer:

- A vanilla SGD optimizer has no state.
- A momentum optimizer stores one value per trainable parameter.
- An Adam optimizer stores two values per trainable parameter.

Imagine you’re updating all parameters in a 13B-parameter model using the Adam optimizer. Because each trainable parameter has three values for its gradient and optimizer states, if it takes two bytes to store each value, the memory needed for gradients and optimizer states will be:

$$13 \text{ billion} \times 3 \times 2 \text{ bytes} = 78 \text{ GB}$$

However, if you only have 1B trainable parameters, the memory needed for gradients and optimizer states will be only:

$$1 \text{ billion} \times 3 \times 2 \text{ bytes} = 6 \text{ GB}$$

One important thing to note is that in the previous formula, I assumed that the memory needed for activations is less than the memory needed for the model’s weights. However, in reality, the activation memory can be much larger. If activations are stored for gradient computation, the memory needed for activations can dwarf the memory needed for the model’s weights. Figure 7-5 shows the memory needed for activations compared to the memory needed for the model’s weights for different Megatron models at different scales, according to the paper “Reducing Activation Recomputation in Large Transformer Models”, by Korthikanti et al. (2022).

One way to reduce the memory needed for activations is not to store them. Instead of storing activations for reuse, you recompute activations when necessary. This technique is called gradient checkpointing or activation recomputation. While this reduces the memory requirements, it increases the time needed for training due to the recomputation.$^{10}$

$^{10}$ To learn more about training memory calculation, check out EleutherAI’s “Transformer Math 101” (Anthony et al., April 2023).
