---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 130
section-title: Backpropagation and Trainable Parameters
source-location: pages 344-345
previous-section: AI Space/normalized/pdf/ai-engineering/sections/129-memory-bottlenecks.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/131-memory-math.md
classification: reusable-knowledge-candidate
---
# Backpropagation and Trainable Parameters

Because memory calculation requires a breakdown of low-level ML and computing
concepts, this section is technically dense. If you’re already familiar with these con‐
cepts, feel free to skip them.
Key Takeaways for Understanding Memory Bottlenecks
If you decide to skip this section, here are a few key takeaways. If you find any of
these takeaways unfamiliar, the concepts in this section should help explain it:
1. Because of the scale of foundation models, memory is a bottleneck for working
with them, both for inference and for finetuning. The memory needed for fine‐
tuning is typically much higher than the memory needed for inference because of
the way neural networks are trained.
2. The key contributors to a model’s memory footprint during finetuning are its
number of parameters, its number of trainable parameters, and its numerical
representations.
3. The more trainable parameters, the higher the memory footprint. You can
reduce memory requirement for finetuning by reducing the number of trainable
parameters. Reducing the number of trainable parameters is the motivation for
PEFT, parameter-efficient finetuning.
4. Quantization refers to the practice of converting a model from a format with
more bits to a format with fewer bits. Quantization is a straightforward and effi‐
cient way to reduce a model’s memory footprint. For a model of 13 billion
parameters, using FP32 means 4 bytes per weight or 52 GB for the whole weights.
If you can reduce each value to only 2 bytes, the memory needed for the model’s
weights decreases to 26 GB.
5. Inference is typically done using as few bits as possible, such as 16 bits, 8 bits, and
even 4 bits.
6. Training is more sensitive to numerical precision, so it’s harder to train a model
in lower precision. Training is typically done in mixed precision, with some
operations done in higher precision (e.g., 32-bit) and some in lower precision
(e.g., 16-bit or 8-bit).
Backpropagation and Trainable Parameters
A key factor that determines a model’s memory footprint during finetuning is its
number of trainable parameters . A trainable parameter is a parameter that can be
updated during finetuning. During pre-training, all model parameters are updated.
During inference, no model parameters are updated. During finetuning, some or all
model parameters may be updated. The parameters that are kept unchanged are fro‐
zen parameters.
320 | Chapter 7: Finetuning

6 Other than backpropagation, a promising approach to training neural networks is evolutionary strategy. One
example, described by Maheswaranathan et al., combines random search with surrogate gradients, instead of
using real gradients, to update model weights. Another interesting approach is direct feedback alignment
(Arild Nøkland, 2016).
7 If a parameter is not trainable, it doesn’t need to be updated and, therefore, there’s no need to compute its
gradient.
The memory needed for each trainable parameter results from the way a model is
trained. As of this writing, neural networks are typically trained using a mechanism
called backpropagation.6 With backpropagation, each training step consists of two
phases:
1. Forward pass: the process of computing the output from the input.
2. Backward pass: the process of updating the model’s weights using the aggregated
signals from the forward pass.
During inference, only the forward pass is executed. During training, both passes are
executed. At a high level, the backward pass works as follows:
1. Compare the computed output from the forward pass against the expected out‐
put (ground truth). If they are different, the model made a mistake, and the
parameters need to be adjusted. The difference between the computed output
and the expected output is called the loss.
2. Compute how much each trainable parameter contributes to the mistake. This
value is called the gradient. Mathematically, gradients are computed by taking
the derivative of the loss with respect to each trainable parameter. There’s one
gradient value per trainable parameter. 7 If a parameter has a high gradient, it sig‐
nificantly contributes to the loss and should be adjusted more.
3. Adjust trainable parameter values using their corresponding gradient. How
much each parameter should be readjusted, given its gradient value, is deter‐
mined by the optimizer. Common optimizers include SGD (stochastic gradient
descent) and Adam. For transformer-based models, Adam is, by far, the most
widely used optimizer.
The forward and backward pass for a hypothetical neural network with three param‐
eters and one nonlinear activation function is visualized in Figure 7-4 . I use this
dummy neural network to simplify the visualization.
Memory Bottlenecks | 321
