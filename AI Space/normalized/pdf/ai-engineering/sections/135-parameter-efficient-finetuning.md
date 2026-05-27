---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 135
section-title: Parameter-Efficient Finetuning
source-location: pages 356-370
previous-section: AI Space/normalized/pdf/ai-engineering/sections/134-finetuning-techniques.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/136-model-merging-and-multi-task-finetuning.md
classification: reusable-knowledge-candidate
---
# Parameter-Efficient Finetuning

21 Personal anecdote: much of my team’s work at NVIDIA was on mixed precision training. See “Mixed Preci‐
sion Training for NLP and Speech Recognition with OpenSeq2Seq”  (Huyen et al., NVIDIA Developer Tech‐
nical Blog, October 2018).
are kept in lower precision.21 You can also have less-sensitive weight values computed
in lower precision and more-sensitive weight values computed in higher precision.
For example, LLM-QAT ( Liu et al., 2023 ) quantizes weights and activations into 4
bits but keeps embeddings in 16 bits.
The portions of the model that should be in lower precision can be set automatically
using the automatic mixed precision (AMP) functionality offered by many ML frame‐
works.
It’s also possible to have different phases of training in different precision levels. For
example, a model can be trained in higher precision but finetuned in lower precision.
This is especially common with foundation models, where the team training a model
from scratch might be an organization with sufficient compute for higher precision
training. Once the model is published, developers with less compute access can fine‐
tune that model in lower precision.
Finetuning Techniques
I hope that the previous section has made clear why finetuning large-scale models is
so memory-intensive. The more memory finetuning requires, the fewer people who
can afford to do it. Techniques that reduce a model’s memory footprint make fine‐
tuning more accessible, allowing more people to adapt models to their applications.
This section focuses on memory-efficient finetuning techniques, which centers
around parameter-efficient finetuning.
I’ll also cover model merging, an exciting but more experimental approach to creat‐
ing custom models. While model merging is generally not considered finetuning, I
include it in this section because it’s complementary to finetuning. Finetuning tailors
one model to specific needs. Model merging combines multiple models, often fine‐
tuned models, for the same purpose.
While combining multiple models isn’t a new concept, new types of models and fine‐
tuning techniques have inspired many creative model-merging techniques, making
this section especially fun to write about.
Parameter-Efficient Finetuning
In the early days of finetuning, models were small enough that people could finetune
entire models. This approach is called full finetuning. In full finetuning, the number
of trainable parameters is exactly the same as the number of parameters.
332 | Chapter 7: Finetuning

22 In partial finetuning, it’s common to finetune the layers closest to the output layer because those layers are
usually more task-specific, whereas earlier layers tend to capture more general features.
Full finetuning can look similar to training. The main difference is that training starts
with randomized model weights, whereas finetuning starts with model weights that
have been previously trained.
As discussed in “Memory Math” on page 322, the more trainable parameters there
are, the more memory is needed. Consider a 7B-parameter model:
• If you use a 16-bit format like FP16, loading the model’s weights alone requires
14 GB for memory.
• Full finetuning this model with the Adam optimizer, also in a 16-bit format,
requires an additional 7B × 3 × 2 bytes = 42 GB of memory.
• The total memory needed for the model’s weights, gradients, and optimizer
states is then 14 GB + 42 GB = 56 GB.
56 GB exceeds the memory capacity of most consumer GPUs, which typically come
with 12–24 GB of memory, with higher-end GPUs offering up to 48 GB. And this
memory estimation doesn’t yet take into account the memory required for
activations.
To fit a model on a given hardware, you can either reduce the
model’s memory footprint or find ways to use the hardware’s
memory more efficiently. Techniques like quantization and PEFT
help minimize the total memory footprint. Techniques that focus
on making better use of hardware memory include CPU offloading.
Instead of trying to fit the whole model on GPUs, you can offload
the excess memory onto CPUs, as demonstrated by DeepSpeed
(Rasley et al., 2020).
We also haven’t touched on the fact that full finetuning, especially supervised fine‐
tuning and preference finetuning, typically requires a lot of high-quality annotated
data that most people can’t afford. Due to the high memory and data requirements of
full finetuning, people started doing partial finetuning . In partial finetuning, only
some of the model’s parameters are updated. For example, if a model has ten layers,
you might freeze the first nine layers and finetune only the last layer, 22 reducing the
number of trainable parameters to 10% of full finetuning.
While partial finetuning can reduce the memory footprint, it’s parameter-inefficient.
Partial finetuning requires many trainable parameters to achieve performance close
to that of full finetuning. A study by Houlsby et al. (2019)  shows that with BERT
large (Devlin et al., 2018), you’d need to update approximately 25% of the parameters
Finetuning Techniques | 333

[Visual content extracted via GLM-OCR]

Full finetuning can look similar to training. The main difference is that training starts with randomized model weights, whereas finetuning starts with model weights that have been previously trained.

As discussed in “Memory Math” on page 322, the more trainable parameters there are, the more memory is needed. Consider a 7B-parameter model:

- If you use a 16-bit format like FP16, loading the model’s weights alone requires 14 GB for memory.
- Full finetuning this model with the Adam optimizer, also in a 16-bit format, requires an additional $7B \times 3 \times 2$ bytes = 42 GB of memory.
- The total memory needed for the model’s weights, gradients, and optimizer states is then $14GB + 42GB = 56GB$.

56 GB exceeds the memory capacity of most consumer GPUs, which typically come with 12–24 GB of memory, with higher-end GPUs offering up to 48 GB. And this memory estimation doesn’t yet take into account the memory required for activations.

To fit a model on a given hardware, you can either reduce the model’s memory footprint or find ways to use the hardware’s memory more efficiently. Techniques like quantization and PEFT help minimize the total memory footprint. Techniques that focus on making better use of hardware memory include CPU offloading. Instead of trying to fit the whole model on GPUs, you can offload the excess memory onto CPUs, as demonstrated by DeepSpeed (Rasley et al., 2020).

We also haven’t touched on the fact that full finetuning, especially supervised finetuning and preference finetuning, typically requires a lot of high-quality annotated data that most people can’t afford. Due to the high memory and data requirements of full finetuning, people started doing partial finetuning. In partial finetuning, only some of the model’s parameters are updated. For example, if a model has ten layers, you might freeze the first nine layers and finetune only the last layer, reducing the number of trainable parameters to 10% of full finetuning.

While partial finetuning can reduce the memory footprint, it’s parameter-inefficient. Partial finetuning requires many trainable parameters to achieve performance close to that of full finetuning. A study by Houlsby et al. (2019) shows that with BERT large (Devlin et al., 2018), you’d need to update approximately 25% of the parameters.

to achieve performance comparable to that of full finetuning on the GLUE bench‐
mark (Wang et al., 2018). Figure 7-7 shows the performance curve of partial finetun‐
ing with different numbers of trainable parameters.
Figure 7-7. The blue line shows that partial finetuning requires many trainable param‐
eters to achieve a performance comparable to full finetuning. Image from Houlsby et al.
(2019).
This brings up the question: How to achieve performance close to that of full finetun‐
ing while using significantly fewer trainable parameters? Finetuning techniques
resulting from this quest are parameter-efficient. There’s no clear threshold that a
finetuning method has to pass to be considered parameter-efficient. However, in gen‐
eral, a technique is considered parameter-efficient if it can achieve performance close
to that of full finetuning while using several orders of magnitude fewer trainable
parameters.
The idea of PEFT (parameter-efficient finetuning) was introduced by Houlsby et al.
(2019). The authors showed that by inserting additional parameters into the model in
the right places, you can achieve strong finetuning performance using a small num‐
ber of trainable parameters. They inserted two adapter modules into each trans‐
former block of a BERT model, as shown in Figure 7-8.
334 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

to achieve performance comparable to that of full finetuning on the GLUE benchmark (Wang et al., 2018). Figure 7-7 shows the performance curve of partial finetuning with different numbers of trainable parameters.

Figure 7-7. The blue line shows that partial finetuning requires many trainable parameters to achieve a performance comparable to full finetuning. Image from Houlsby et al. (2019).

This brings up the question: How to achieve performance close to that of full finetuning while using significantly fewer trainable parameters? Finetuning techniques resulting from this quest are parameter-efficient. There’s no clear threshold that a finetuning method has to pass to be considered parameter-efficient. However, in general, a technique is considered parameter-efficient if it can achieve performance close to that of full finetuning while using several orders of magnitude fewer trainable parameters.

The idea of PEFT (parameter-efficient finetuning) was introduced by Houlsby et al. (2019). The authors showed that by inserting additional parameters into the model in the right places, you can achieve strong finetuning performance using a small number of trainable parameters. They inserted two adapter modules into each transformer block of a BERT model, as shown in Figure 7-8.

Figure 7-8. By inserting two adapter modules into each transformer layer for a BERT
model and updating only the adapters, Houlsby et al. (2019) were able to achieve
strong finetuning performance using a small number of trainable parameters.
During finetuning, they kept the model’s original parameters unchanged and only
updated the adapters. The number of trainable parameters is the number of parame‐
ters in the adapters. On the GLUE benchmark, they achieved a performance within
0.4% of full finetuning using only 3% of the number of trainable parameters. The
orange line in Figure 7-7  shows the performance delta between full finetuning and
finetuning using different adapter sizes.
However, the downside of this approach is that it increases the inference latency of
the finetuned model. The adapters introduce additional layers, which add more com‐
putational steps to the forward pass, slowing inference.
PEFT enables finetuning on more affordable hardware, making it accessible to many
more developers. PEFT methods are generally not only parameter-efficient but also
sample-efficient. While full finetuning may need tens of thousands to millions of
examples to achieve notable quality improvements, some PEFT methods can deliver
strong performance with just a few thousand examples.
Given PEFT’s obvious appeal, PEFT techniques are being rapidly developed. The
next section will give an overview of these techniques before diving deeper into the
most common PEFT technique: LoRA.
Finetuning Techniques | 335

[Visual content extracted via GLM-OCR]

Figure 7-8. By inserting two adapter modules into each transformer layer for a BERT model and updating only the adapters, Houlsby et al. (2019) were able to achieve strong finetuning performance using a small number of trainable parameters.

During finetuning, they kept the model’s original parameters unchanged and only updated the adapters. The number of trainable parameters is the number of parameters in the adapters. On the GLUE benchmark, they achieved a performance within 0.4% of full finetuning using only 3% of the number of trainable parameters. The orange line in Figure 7-7 shows the performance delta between full finetuning and finetuning using different adapter sizes.

However, the downside of this approach is that it increases the inference latency of the finetuned model. The adapters introduce additional layers, which add more computational steps to the forward pass, slowing inference.

PEFT enables finetuning on more affordable hardware, making it accessible to many more developers. PEFT methods are generally not only parameter-efficient but also sample-efficient. While full finetuning may need tens of thousands to millions of examples to achieve notable quality improvements, some PEFT methods can deliver strong performance with just a few thousand examples.

Given PEFT’s obvious appeal, PEFT techniques are being rapidly developed. The next section will give an overview of these techniques before diving deeper into the most common PEFT technique: LoRA.

PEFT techniques
The existing prolific world of PEFT generally falls into two buckets: adapter-based
methods and soft prompt-based methods . However, it’s likely that newer buckets will
be introduced in the future.
Adapter-based methods  refer to all methods that involve additional modules to the
model weights, such as the one developed by Houlsby et al. (2019) . Because adapterbased methods involve adding parameters, they are also called additive methods.
As of this writing, LoRA ( Hu et al., 2021 ) is by far the most popular adapter-based
method, and it will be the topic of the following section. Other adapter-based meth‐
ods include BitFit ( Zaken et al., 2021 ), which came out around the same time LoRA
did. Newer adapter methods include IA3 (Liu et al., 2022), whose efficient mixed-task
batching strategy makes it particularly attractive for multi-task finetuning. It’s been
shown to outperform LoRA and even full finetuning in some cases. LongLoRA (Chen
et al., 2023) is a LoRA variant that incorporates attention-modification techniques to
expand context length.
If adapter-based methods add trainable parameters to the model’s architecture, soft
prompt-based methods modify how the model processes the input by introducing
special trainable tokens. These additional tokens are fed into the model alongside the
input tokens. They are called soft prompts  because, like the inputs (hard prompts),
soft prompts also guide the model’s behaviors. However, soft prompts differ from
hard prompts in two ways:
• Hard prompts are human-readable. They typically contain discrete tokens such
as “I”, “write”, “a”, and “lot”. In contrast, soft prompts are continuous vectors,
resembling embedding vectors, and are not human-readable.
• Hard prompts are static and not trainable, whereas soft prompts can be opti‐
mized through backpropagation during the tuning process, allowing them to be
adjusted for specific tasks.
336 | Chapter 7: Finetuning

23 I’ve never met a single person who could explain to me, on the spot, the differences between these techniques.
Some people describe soft prompting as a crossover between prompt engineering and
finetuning. Figure 7-9  visualizes how you can use soft prompts together with hard
prompts to guide a model’s behaviors.
Figure 7-9. Hard prompts and soft prompts can be combined to change a model’s
behaviors.
Soft prompt tuning as a subfield is characterized by a series of similar-sounding tech‐
niques that can be confusing, such as prefix-tuning ( Li and Liang, 2021 ), P-Tuning
(Liu et al., 2021 ), and prompt tuning ( Lester et al., 2021 ).23 They differ mainly on the
locations where the soft prompts are inserted. For example, prefix tuning prepends
soft prompt tokens to the input at every transformer layer, whereas prompt tuning
prepends soft prompt tokens to only the embedded input. If you want to use any of
them, many PEFT frameworks will implement them out of the box for you.
To get a sense of what PEFT methods are being used, I analyzed over 1,000 open
issues on the GitHub repository huggingface/peft in October 2024. The assumption is
that if someone uses a technique, they are more likely to report issues or ask ques‐
tions about it. Figure 7-10 shows the result. For “P-Tuning”, I searched for keywords
“p_tuning” and “p tuning” to account for different spellings.
Finetuning Techniques | 337

[Visual content extracted via GLM-OCR]

Some people describe soft prompting as a crossover between prompt engineering and finetuning. Figure 7-9 visualizes how you can use soft prompts together with hard prompts to guide a model’s behaviors.

Figure 7-9. Hard prompts and soft prompts can be combined to change a model’s behaviors.

Soft prompt tuning as a subfield is characterized by a series of similar-sounding techniques that can be confusing, such as prefix-tuning (Li and Liang, 2021), P-Tuning (Liu et al., 2021), and prompt tuning (Lester et al., 2021). They differ mainly on the locations where the soft prompts are inserted. For example, prefix tuning prepends soft prompt tokens to the input at every transformer layer, whereas prompt tuning prepends soft prompt tokens to only the embedded input. If you want to use any of them, many PEFT frameworks will implement them out of the box for you.

To get a sense of what PEFT methods are being used, I analyzed over 1,000 open issues on the GitHub repository huggingface/peft in October 2024. The assumption is that if someone uses a technique, they are more likely to report issues or ask questions about it. Figure 7-10 shows the result. For “P-Tuning”, I searched for keywords “p_tuning” and “p tuning” to account for different spellings.

23 I’ve never met a single person who could explain to me, on the spot, the differences between these techniques.

Figure 7-10. The number of issues corresponding to different finetuning techniques
from the GitHub repository huggingface/peft. This is a proxy to estimate the popularity
of each technique.
From this analysis, it’s clear that LoRA dominates. Soft prompts are less common,
but there seems to be growing interest from those who want more customization
than what is afforded by prompt engineering but who don’t want to invest in
finetuning.
Because of LoRA’s popularity, the next section focuses on how LoRA works and how
it solves the challenge posed by early adapter-based methods. Even if you don’t use
LoRA, this deep dive should provide a framework for you to explore other finetuning
methods.
LoRA
Unlike the original adapter method by Houlsby et al. (2019), LoRA (Low-Rank Adap‐
tation) ( Hu et al., 2021 ) incorporates additional parameters in a way that doesn’t
incur extra inference latency. Instead of introducing additional layers to the base
model, LoRA uses modules that can be merged back to the original layers.
338 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

Figure 7-10. The number of issues corresponding to different finetuning techniques from the GitHub repository huggingface/peft. This is a proxy to estimate the popularity of each technique.

From this analysis, it’s clear that LoRA dominates. Soft prompts are less common, but there seems to be growing interest from those who want more customization than what is afforded by prompt engineering but who don’t want to invest in finetuning.

Because of LoRA’s popularity, the next section focuses on how LoRA works and how it solves the challenge posed by early adapter-based methods. Even if you don’t use LoRA, this deep dive should provide a framework for you to explore other finetuning methods.

LoRA

Unlike the original adapter method by Houlsby et al. (2019), LoRA (Low-Rank Adaptation) (Hu et al., 2021) incorporates additional parameters in a way that doesn’t incur extra inference latency. Instead of introducing additional layers to the base model, LoRA uses modules that can be merged back to the original layers.

You can apply LoRA to individual weight matrices. Given a weight matrix, LoRA decomposes this matrix into the product of two smaller matrices, then updates these two smaller matrices before merging them back to the original matrix.

Consider the weight matrix $W$ of the dimension $n \times m$. LoRA works as follows:

1. First, choose the dimension of the smaller matrices. Let $r$ be the chosen value. Construct two matrices: $A$ (dimension $n \times r$) and $B$ (dimension $r \times m$). Their product is $W_{AB}$, which is of the same dimension as $W$. $r$ is the LoRA rank.

2. Add $W_{AB}$ to the original weight matrix $W$ to create a new weight matrix $W'$. Use $W'$ in place of $W$ as part of the model. You can use a hyperparameter $\alpha$ to determine how much $W_{AB}$ should contribute to the new matrix: $W' = W + \frac{\alpha}{r} W_{AB}$

3. During finetuning, update only the parameters in $A$ and $B$. $W$ is kept intact.

Figure 7-11 visualizes this process.

Figure 7-11. To apply LoRA to a weight matrix $W$, decompose it into the product of two matrices $A$ and $B$. During finetuning, only $A$ and $B$ are updated. $W$ is kept intact.

LoRA (Low-Rank Adaptation) is built on the concept of low-rank
factorization, a long-standing dimensionality reduction technique.
The key idea is that you can factorize a large matrix into a product
of two smaller matrices to reduce the number of parameters,
which, in turn, reduces both the computation and memory
requirements. For example, a 9 × 9  matrix can be factorized into
the product of two matrices of dimensions 9 × 1  and 1 × 9 . The
original matrix has 81 parameters, but the two product matrices
have only 18 parameters combined.
The number of columns in the first factorized matrix and the num‐
ber of columns in the second factorized matrix correspond to the
rank of the factorization. The original matrix is full-rank, while the
two smaller matrices represent a low-rank approximation.
While factorization can significantly reduce the number of param‐
eters, it’s lossy because it only approximates the original matrix.
The higher the rank, the more information from the original
matrix the factorization can preserve.
Like the original adapter method, LoRA is parameter-efficient and sample-efficient.
The factorization enables LoRA to use even fewer trainable parameters. The LoRA
paper showed that, for GPT-3, LoRA achieves comparable or better performance
with full finetuning on several tasks while using only ~4.7M trainable parameters,
0.0027% of full finetuning.
Why does LoRA work?    Parameter-efficient methods like LoRA have become so popular
that many people take them for granted. But why is parameter efficiency possible at
all? If a model requires a lot of parameters to learn certain behaviors during pretraining, shouldn’t it also require a lot of parameters to change its behaviors during
finetuning?
The same question can be raised for data. If a model requires a lot of data to learn a
behavior, shouldn’t it also require a lot of data to meaningfully change this behavior?
How is it possible that you need millions or billions of examples to pre-train a model,
but only a few hundreds or thousands of examples to finetune it?
Many papers have argued that while LLMs have many parameters, they have very low
intrinsic dimensions; see Li et al. (2018) ; Aghajanyan et al. (2020) ; and Hu et al.
(2021). They showed that pre-training implicitly minimizes the model’s intrinsic
dimension. Surprisingly, larger models tend to have lower intrinsic dimensions after
pre-training. This suggests that pre-training acts as a compression framework for
downstream tasks. In other words, the better trained an LLM is, the easier it is to
finetune the model using a small number of trainable parameters and a small amount
of data.
340 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

LoRA (Low-Rank Adaptation) is built on the concept of low-rank factorization, a long-standing dimensionality reduction technique. The key idea is that you can factorize a large matrix into a product of two smaller matrices to reduce the number of parameters, which, in turn, reduces both the computation and memory requirements. For example, a 9 × 9 matrix can be factorized into the product of two matrices of dimensions 9 × 1 and 1 × 9. The original matrix has 81 parameters, but the two product matrices have only 18 parameters combined.

The number of columns in the first factorized matrix and the number of columns in the second factorized matrix correspond to the rank of the factorization. The original matrix is full-rank, while the two smaller matrices represent a low-rank approximation.

While factorization can significantly reduce the number of parameters, it’s lossy because it only approximates the original matrix. The higher the rank, the more information from the original matrix the factorization can preserve.

Like the original adapter method, LoRA is parameter-efficient and sample-efficient. The factorization enables LoRA to use even fewer trainable parameters. The LoRA paper showed that, for GPT-3, LoRA achieves comparable or better performance with full finetuning on several tasks while using only ~4.7M trainable parameters, 0.0027% of full finetuning.

Why does LoRA work? Parameter-efficient methods like LoRA have become so popular that many people take them for granted. But why is parameter efficiency possible at all? If a model requires a lot of parameters to learn certain behaviors during pre-training, shouldn’t it also require a lot of parameters to change its behaviors during finetuning?

The same question can be raised for data. If a model requires a lot of data to learn a behavior, shouldn’t it also require a lot of data to meaningfully change this behavior? How is it possible that you need millions or billions of examples to pre-train a model, but only a few hundreds or thousands of examples to finetune it?

Many papers have argued that while LLMs have many parameters, they have very low intrinsic dimensions; see Li et al. (2018); Aghajanyan et al. (2020); and Hu et al. (2021). They showed that pre-training implicitly minimizes the model’s intrinsic dimension. Surprisingly, larger models tend to have lower intrinsic dimensions after pre-training. This suggests that pre-training acts as a compression framework for downstream tasks. In other words, the better trained an LLM is, the easier it is to finetune the model using a small number of trainable parameters and a small amount of data.

You might wonder, if low-rank factorization works so well, why don’t we use LoRA
for pre-training as well?  Instead of pre-training a large model and applying low-rank
factorization only during finetuning, could we factorize a model from the start for
pre-training? Low-rank pre-training can significantly reduce the model’s number of
parameters, significantly reducing the model’s pre-training time and cost.
Throughout the 2010s, many people tried training low-rank neural networks, exem‐
plified in studies such as “Low-Rank Matrix Factorization for Deep Neural Network
Training with High-Dimensional Output Targets” ( Sainath et al., 2013 ), “SemiOrthogonal Low-Rank Matrix Factorization for Deep Neural Networks” ( Povey et al.,
2018), and “Speeding up Convolutional Neural Networks with Low Rank Expan‐
sions” ( Jaderberg et al., 2014).
Low-rank factorization has proven to be effective at smaller scales. For example, by
applying various factorization strategies, including replacing 3 × 3 convolution with 1
× 1 convolution, SqueezeNet (Iandola et al., 2016) achieves AlexNet-level accuracy on
ImageNet using 50 times fewer parameters.
More recent attempts to train low-rank LLMs include ReLoRA ( Lialin et al., 2023 )
and GaLore ( Zhao et al., 2024 ). ReLoRA works for transformer-based models of up
to 1.3B parameters. GaLore achieves performance comparable to that of a full-rank
model at 1B parameters and promising performance at 7B parameters.
It’s possible that one day not too far in the future, researchers will develop a way to
scale up low-rank pre-training to hundreds of billions of parameters. However, if
Aghajanyan et al.’s argument  is correct—that pre-training implicitly compresses a
model’s intrinsic dimension—full-rank pre-training is still necessary to sufficiently
reduce the model’s intrinsic dimension to a point where low-rank factorization can
work. It would be interesting to study exactly how much full-rank training is neces‐
sary before it’s possible to switch to low-rank training.
LoRA configurations.    To apply LoRA, you need to decide what weight matrices to
apply LoRA to and the rank of each factorization. This section will discuss the con‐
siderations for each of these decisions.
LoRA can be applied to each individual weight matrix. The efficiency of LoRA, there‐
fore, depends not only on what matrices LoRA is applied to but also on the model’s
architecture, as different architectures have different weight matrices.
Finetuning Techniques | 341

24 To effectively use LoRA for a model, it’s necessary to understand that model’s architecture. Chapter 2 already
covered the weight composition of some transformer-based models. For the exact weight composition of a
model, refer to its paper.
While there have been examples of LoRA with other architectures, such as convolu‐
tional neural networks (Dutt et al., 2023; Zhong et al., 2024; Aleem et al., 2024), LoRA
has been primarily used for transformer models. 24 LoRA is most commonly applied
to the four weight matrices in the attention modules: the query ( Wq), key (Wk), value
(Wv), and output projection (Wo) matrices.
Typically, LoRA is applied uniformly to all matrices of the same type within a model.
For example, applying LoRA to the query matrix means applying LoRA to all query
matrices in the model.
Naively, you can apply LoRA to all these attention matrices. However, often, you’re
constrained by your hardware’s memory and can accommodate only a fixed number
of trainable parameters. Given a fixed budget of trainable parameters, what matrices
should you apply LoRA to, to maximize performance?
When finetuning GPT-3 175B, Hu et al. (2021) set their trainable parameter budget
at 18M, which is 0.01% of the model’s total number of parameters. This budget
allows them to apply LoRA to the following:
1. One matrix with the rank of 8
2. Two matrices with the rank of 4
3. All four matrices with the rank of 2
GPT-3 175B has 96 transformer layers with a model dimension of
12,288. Applying LoRA with rank = 2 to all four matrices would
yield (12,288 × 2 × 2) × 4 = 196,608 trainable parameters per layer,
or 18,874,368 trainable parameters for the whole model.
They found that applying LoRA to all four matrices with rank = 2 yields the best per‐
formance on the WikiSQL ( Zhong et al., 2017 ) and MultiNLI (Multi-Genre Natural
Language Inference) benchmarks ( Williams et al., 2017 ). Table 7-5  shows their
results. However, the authors suggested that if you can choose only two attention
matrices, the query and value matrices generally yield the best results.
342 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

While there have been examples of LoRA with other architectures, such as convolutional neural networks (Dutt et al., 2023; Zhong et al., 2024; Aleem et al., 2024), LoRA has been primarily used for transformer models. LoRA is most commonly applied to the four weight matrices in the attention modules: the query ($W_q$), key ($W_k$), value ($W_v$), and output projection ($W_o$) matrices.

Typically, LoRA is applied uniformly to all matrices of the same type within a model. For example, applying LoRA to the query matrix means applying LoRA to all query matrices in the model.

Naively, you can apply LoRA to all these attention matrices. However, often, you’re constrained by your hardware’s memory and can accommodate only a fixed number of trainable parameters. Given a fixed budget of trainable parameters, what matrices should you apply LoRA to, to maximize performance?

When finetuning GPT-3 175B, Hu et al. (2021) set their trainable parameter budget at 18M, which is 0.01% of the model’s total number of parameters. This budget allows them to apply LoRA to the following:

1. One matrix with the rank of 8
2. Two matrices with the rank of 4
3. All four matrices with the rank of 2

GPT-3 175B has 96 transformer layers with a model dimension of 12,288. Applying LoRA with rank = 2 to all four matrices would yield $(12,288 \times 2 \times 2) \times 4 = 196,608$ trainable parameters per layer, or 18,874,368 trainable parameters for the whole model.

They found that applying LoRA to all four matrices with rank = 2 yields the best performance on the WikiSQL (Zhong et al., 2017) and MultiNLI (Multi-Genre Natural Language Inference) benchmarks (Williams et al., 2017). Table 7-5 shows their results. However, the authors suggested that if you can choose only two attention matrices, the query and value matrices generally yield the best results.

24 To effectively use LoRA for a model, it’s necessary to understand that model’s architecture. Chapter 2 already covered the weight composition of some transformer-based models. For the exact weight composition of a model, refer to its paper.

25 As of this writing, some finetuning frameworks like Fireworks only allow a maximum LoRA rank of 32. How‐
ever, this constraint is unlikely due to performance and more likely due to their hardware’s memory con‐
straint.
Table 7-5. LoRA performance with the budget of 18M trainable parameters. Results from
LoRA (Hu et al., 2021).
Number of trainable parameters = 18M
Weight type Wq Wk Wv Wo Wq, Wk Wq, Wv Wq, Wk, Wv, Wo
Rank r 8 8 8 8 4 4 2
WikiSQL (± 0.5%) 70.4 70.0 73.0 73.2 71.4 73.7 73.7
MultiNLI (± 0.1%) 91.0 90.8 91.0 91.3 91.3 91.3 91.7
Empirical observations suggest that applying LoRA to more weight matrices, includ‐
ing the feedforward matrices, yields better results. For example, Databricks showed
that the biggest performance boost they got was from applying LoRA to all feedfor‐
ward layers ( Sooriyarachchi, 2023 ). Fomenko et al. (2024)  noted that feedforwardbased LoRA can be complementary to attention-based LoRA, though attention-based
LoRA typically offers greater efficacy within memory constraints.
The beauty of LoRA is that while its performance depends on its rank, studies have
shown that a small r, such as between 4 and 64, is usually sufficient for many use cases .
A smaller r means fewer LoRA parameters, which translates to a lower memory foot‐
print.
The LoRA authors observed that, to their surprise, increasing the value of r doesn’t
increase finetuning performance. This observation is consistent with Databricks’
report that “increasing r beyond a certain value may not yield any discernible
increase in quality of model output” (Sooriyarachchi, 2023). 25 Some argue that a
higher r might even hurt as it can lead to overfitting. However, in some cases, a
higher rank might be necessary. Raschka (2023) found that r = 256 achieved the best
performance on his tasks.
Another LoRA hyperparameter you can configure is the value α that determines how
much the product WAB should contribute to the new matrix during merging:
W ' = W +
α
r W AB. In practice, I’ve often seen ɑ chosen so that the ratio α:r is typi‐
cally between 1:8 and 8:1, but the optimal ratio varies. For example, if r is small, you
might want α to be larger, and if r is large, you might want α to be smaller. Experi‐
mentation is needed to determine the best (r,α) combination for your use case.
Serving LoRA adapters.    LoRA not only lets you finetune models using less memory
and data, but it also simplifies serving multiple models due to its modularity. To
understand this benefit, let’s examine how to serve a LoRA-finetuned model.
Finetuning Techniques | 343

In general, there are two ways to serve a LoRA-finetuned model:
1. Merge the LoRA weights A and B into the original model to create the new
matrix Wʹ prior to serving the finetuned model. Since no extra computation is
done during inference, no extra latency is added.
2. Keep W, A, and B separate during serving. The process of merging A and B back
to W happens during inference, which adds extra latency.
The first option is generally better if you have only one LoRA model to serve, whereas
the second is generally better for multi-LoRA serving— serving multiple LoRA models
that share the same base model. Figure 7-12  visualizes multi-LoRA serving if you
keep the LoRA adapters separate.
Figure 7-12. Keeping LoRA adapters separate allows reuse of the same full-rank matrix
W in multi-LoRA serving.
For multi-LoRA serving, while option 2 adds latency overhead, it significantly
reduces the storage needed. Consider the scenario in which you finetune a model for
each of your customers using LoRA. With 100 customers, you end up with 100 fine‐
tuned models, all sharing the same base model. With option 1, you have to store 100
full-rank matrices Wʹ. With option 2, you only have to store one full-rank matrix W,
and 100 sets of smaller matrices (A, B).
To put this in perspective, let’s say that the original matrix W is of the dimension
4096 × 4096 (16.8M parameters). If the LoRA’s rank is 8, the number of parameters
in A and B is 4096 × 8 × 2 = 65,536:
• In option 1, 100 full-rank matrices Wʹ totals 16.8M × 100 = 1.68B parameters.
• In option 2, one full-rank matrix W and 100 sets of small matrices ( A, B) totals:
16.8M + 65,536 × 100 = 23.3M parameters.
Option 2 also makes it faster to switch between tasks. Let’s say you’re currently serv‐
ing customer X using this customer’s model. To switch to serving customer Y,
instead of loading this customer’s full weight matrix, you only need to load Y’s LoRA
344 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

In general, there are two ways to serve a LoRA-finetuned model:

1. Merge the LoRA weights $A$ and $B$ into the original model to create the new matrix $W'$ prior to serving the finetuned model. Since no extra computation is done during inference, no extra latency is added.

2. Keep $W$, $A$, and $B$ separate during serving. The process of merging $A$ and $B$ back to $W$ happens during inference, which adds extra latency.

The first option is generally better if you have only one LoRA model to serve, whereas the second is generally better for multi-LoRA serving—serving multiple LoRA models that share the same base model. Figure 7-12 visualizes multi-LoRA serving if you keep the LoRA adapters separate.

For multi-LoRA serving, while option 2 adds latency overhead, it significantly reduces the storage needed. Consider the scenario in which you finetune a model for each of your customers using LoRA. With 100 customers, you end up with 100 finetuned models, all sharing the same base model. With option 1, you have to store 100 full-rank matrices $W'$. With option 2, you only have to store one full-rank matrix $W$, and 100 sets of smaller matrices $(A, B)$.

To put this in perspective, let’s say that the original matrix $W$ is of the dimension $4096 \times 4096$ (16.8M parameters). If the LoRA’s rank is 8, the number of parameters in $A$ and $B$ is $4096 \times 8 \times 2 = 65,536$:

- In option 1, 100 full-rank matrices $W'$ totals $16.8M \times 100 = 1.68B$ parameters.
- In option 2, one full-rank matrix $W$ and 100 sets of small matrices $(A, B)$ totals: $16.8M + 65,536 \times 100 = 23.3M$ parameters.

Option 2 also makes it faster to switch between tasks. Let’s say you’re currently serving customer $X$ using this customer’s model. To switch to serving customer $Y$, instead of loading this customer’s full weight matrix, you only need to load $Y$’s LoRA

26 Search for these adapters by tags “adapter”, “peft”, or “LoRA”.
adapter, which can significantly reduce the loading time. While keeping A and B sep‐
arate incurs additional latency, there are optimization techniques to minimize the
added latency. The book’s GitHub repository  contains a walkthrough of how to do
so.
Multi-LoRA serving makes it easy to combine multiple specialized models. Instead of
having one big powerful model for multiple tasks, you can have one LoRA adapter
for each task. For example, Apple used multiple LoRA adapters to adapt the same 3Bparameter base model to different iPhone features (2024). They utilized quantization
techniques to further reduce the memory footprint of this base model and adapters,
allowing the serving of all of them on-device.
The modularity of LoRA adapters means that LoRA adapters can be shared and
reused. There are publicly available finetuned LoRA adapters that you can use the
way you’d use pre-trained models. You can find them on Hugging Face 26 or initia‐
tives like AdapterHub.
You might be wondering: “LoRA sounds great, but what’s the catch?” The main
drawback of LoRA is that it doesn’t offer performance as strong as full finetuning.
It’s also more challenging to do than full finetuning as it involves modifying the
model’s implementation, which requires an understanding of the model’s architec‐
ture and coding skills. However, this is usually only an issue for less popular base
models. PEFT frameworks—such as Hugging Face’s PEFT , Axolotl, unsloth, and
LitGPT—likely support LoRA for popular base models right out of the box.
Quantized LoRA.    The rapid rise of LoRA has led to the development of numerous
LoRA variations. Some aim to reduce the number of trainable parameters even fur‐
ther. However, as illustrated in Table 7-6, the memory of a LoRA adapter is minimal
compared to the memory of the model’s weights. Reducing the number of LoRA
parameters decreases the overall memory footprint by only a small percentage.
Table 7-6. The memory needed by LoRA weights compared to that needed by the model’s
weights.
Model’s weights memory
(16 bits)
LoRA trainable params
(r=2, query & key matrices)
LoRA adapter memory
(16 bits)
Llama 2 (13B) 26 GB 3.28M 6.55 MB
GPT-3 (175B) 350 GB 18.87M 37.7 MB
Finetuning Techniques | 345

27 QLoRA isn’t the only quantized LoRA work. Many research labs have been working on quantized LoRA
without publicly discussing it.
Rather than trying to reduce LoRA’s number of parameters, you can reduce the
memory usage more effectively by quantizing the model’s weights, activations,
and/or gradients during finetuning. An early promising quantized version of LoRA is
QLoRA (Dettmers et al., 2023 ).27 In the original LoRA paper, during finetuning, the
model’s weights are stored using 16 bits. QLoRA stores the model’s weights in 4 bits
but dequantizes (converts) them back into BF16 when computing the forward and
backward pass.
The 4-bit format that QLoRA uses is NF4 (NormalFloat-4), which quantizes values
based on the insight that pre-trained weights usually follow a normal distribution
with a median of zero. On top of 4-bit quantization, QLoRA also uses paged optimiz‐
ers to automatically transfer data between the CPU and GPU when the GPU runs out
of memory, especially with long sequence lengths. These techniques allow a 65Bparameter model to be finetuned on a single 48 GB GPU.
The authors finetuned a variety of models, including Llama 7B to 65B, in the 4-bit
mode. The resulting family of models, called Guanaco, showed competitive perfor‐
mance on both public benchmarks and comparative evaluation. Table 7-7 shows the
Elo ratings of Guanaco models, GPT-4, and ChatGPT in May 2023, as judged by
GPT-4. While Guanaco 65B didn’t outperform GPT-4, it was often preferred to
ChatGPT.
Table 7-7. Elo ratings of Guanaco models compared to popular models in May 2023 using
GPT-4 as a judge. The experiment is from QLoRA (Dettmers et al., 2023).
Model Size Elo
GPT-4 - 1348 ± 1
Guanaco 65B 41 GB 1022 ± 1
Guanaco 33B 21 GB 992 ± 1
Vicuna 13B 26 GB 974 ± 1
ChatGPT - 966 ± 1
Guanaco 13B 10 GB 916 ± 1
Bard - 902 ± 1
Guanaco 7B 6 GB 879 ± 1
The main limitation of QLoRA is that NF4 quantization is expensive. While QLoRA
can reduce the memory footprint, it might increase training time due to the extra
time required by quantization and dequantization steps.
346 | Chapter 7: Finetuning
