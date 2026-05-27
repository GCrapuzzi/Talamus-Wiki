---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 043
section-title: Model Architecture
source-location: pages 82-90
previous-section: AI Space/normalized/pdf/ai-engineering/sections/042-modeling.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
classification: reusable-knowledge-candidate
---
# Model Architecture

5 ML fundamentals related to model training are outside the scope of this book. However, when relevant to the
discussion, I include some concepts. For example, self-supervision—where a model generates its own labels
from the data—is covered in Chapter 1, and backpropagation—how a model’s parameters are updated during
training based on the error—is discussed in Chapter 7.
Modeling
Before training a model, developers need to decide what the model should look like.
What architecture should it follow? How many parameters should it have? These
decisions impact not only the model’s capabilities but also its usability for
downstream applications.5 For example, a 7B-parameter model will be vastly easier to
deploy than a 175B-parameter model. Similarly, optimizing a transformer model for
latency is very different from optimizing another architecture. Let’s explore the fac‐
tors behind these decisions.
Model Architecture
As of this writing, the most dominant architecture for language-based foundation
models is the transformer architecture ( Vaswani et al., 2017 ), which is based on the
attention mechanism. It addresses many limitations of the previous architectures,
which contributed to its popularity. However, the transformer architecture has its
own limitations. This section analyzes the transformer architecture and its alterna‐
tives. Because it goes into the technical details of different architectures, it can be
technically dense. If you find any part too deep in the weeds, feel free to skip it.
Transformer architecture
To understand the transformer, let’s look at the problem it was created to solve. The
transformer architecture was popularized on the heels of the success of the seq2seq
(sequence-to-sequence) architecture. At the time of its introduction in 2014, seq2seq
provided significant improvement on then-challenging tasks: machine translation
and summarization. In 2016, Google incorporated seq2seq into Google Translate , an
update that they claimed to have given them the “largest improvements to date for
machine translation quality”. This generated a lot of interest in seq2seq, making it the
go-to architecture for tasks involving sequences of text.
At a high level, seq2seq contains an encoder that processes inputs and a decoder that
generates outputs. Both inputs and outputs are sequences of tokens, hence the name.
Seq2seq uses RNNs (recurrent neural networks) as its encoder and decoder. In its
most basic form, the encoder processes the input tokens sequentially, outputting the
final hidden state that represents the input. The decoder then generates output
tokens sequentially, conditioned on both the final hidden state of the input and the
previously generated token. A visualization of the seq2seq architecture is shown in
the top half of Figure 2-4.
58 | Chapter 2: Understanding Foundation Models

6 RNNs are especially prone to vanishing and exploding gradients due to their recursive structure. Gradients
must be propagated through many steps, and if they are small, repeated multiplication causes them to shrink
toward zero, making it difficult for the model to learn. Conversely, if the gradients are large, they grow expo‐
nentially with each step, leading to instability in the learning process.
Figure 2-4. Seq2seq architecture versus transformer architecture. For the transformer
architecture, the arrows show the tokens that the decoder attends to when generating
each output token.
There are two problems with seq2seq that Vaswani et al. (2017) addresses. First, the
vanilla seq2seq decoder generates output tokens using only the final hidden state of
the input. Intuitively, this is like generating answers about a book using the book
summary. This limits the quality of the generated outputs. Second, the RNN encoder
and decoder mean that both input processing and output generation are done
sequentially, making it slow for long sequences. If an input is 200 tokens long,
seq2seq has to wait for each input token to finish processing before moving on to the
next.6
The transformer architecture addresses both problems with the attention mecha‐
nism. The attention mechanism allows the model to weigh the importance of differ‐
ent input tokens when generating each output token. This is like generating answers
by referencing any page in the book. A simplified visualization of the transformer
architecture is shown in the bottom half of Figure 2-4.
Modeling | 59

[Visual content extracted via GLM-OCR]

There are two problems with seq2seq that Vaswani et al. (2017) addresses. First, the vanilla seq2seq decoder generates output tokens using only the final hidden state of the input. Intuitively, this is like generating answers about a book using the book summary. This limits the quality of the generated outputs. Second, the RNN encoder and decoder mean that both input processing and output generation are done sequentially, making it slow for long sequences. If an input is 200 tokens long, seq2seq has to wait for each input token to finish processing before moving on to the next.

The transformer architecture addresses both problems with the attention mechanism. The attention mechanism allows the model to weigh the importance of different input tokens when generating each output token. This is like generating answers by referencing any page in the book. A simplified visualization of the transformer architecture is shown in the bottom half of Figure 2-4.

6 RNNs are especially prone to vanishing and exploding gradients due to their recursive structure. Gradients must be propagated through many steps, and if they are small, repeated multiplication causes them to shrink toward zero, making it difficult for the model to learn. Conversely, if the gradients are large, they grow exponentially with each step, leading to instability in the learning process.

7 Bahdanau et al., “Neural Machine Translation by Jointly Learning to Align and Translate” .
While the attention mechanism is often associated with the trans‐
former model, it was introduced three years before the transformer
paper. The attention mechanism can also be used with other archi‐
tectures. Google used the attention mechanism with their seq2seq
architecture in 2016 for their GNMT (Google Neural Machine
Translation) model. However, it wasn’t until the transformer paper
showed that the attention mechanism could be used without RNNs
that it took off.7
The transformer architecture dispenses with RNNs entirely. With transformers, the
input tokens can be processed in parallel, significantly speeding up input processing.
While the transformer removes the sequential input bottleneck, transformer-based
autoregressive language models still have the sequential output bottleneck.
Inference for transformer-based language models, therefore, consists of two steps:
Prefill
The model processes the input tokens in parallel. This step creates the intermedi‐
ate state necessary to generate the first output token. This intermediate state
includes the key and value vectors for all input tokens.
Decode
The model generates one output token at a time.
As explored later in Chapter 9, the parallelizable nature of prefilling and the sequen‐
tial aspect of decoding both motivate many optimization techniques to make lan‐
guage model inference cheaper and faster.
Attention mechanism.    At the heart of the transformer architecture is the attention
mechanism. Understanding this mechanism is necessary to understand how trans‐
former models work. Under the hood, the attention mechanism leverages key, value,
and query vectors:
• The query vector (Q) represents the current state of the decoder at each decoding
step. Using the same book summary example, this query vector can be thought of
as the person looking for information to create a summary.
• Each key vector (K) represents a previous token. If each previous token is a page
in the book, each key vector is like the page number. Note that at a given decod‐
ing step, previous tokens include both input tokens and previously generated
tokens.
60 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

While the attention mechanism is often associated with the transformer model, it was introduced three years before the transformer paper. The attention mechanism can also be used with other architectures. Google used the attention mechanism with their seq2seq architecture in 2016 for their GNMT (Google Neural Machine Translation) model. However, it wasn’t until the transformer paper showed that the attention mechanism could be used without RNNs that it took off.

The transformer architecture dispenses with RNNs entirely. With transformers, the input tokens can be processed in parallel, significantly speeding up input processing. While the transformer removes the sequential input bottleneck, transformer-based autoregressive language models still have the sequential output bottleneck.

Inference for transformer-based language models, therefore, consists of two steps:

**Prefill**
The model processes the input tokens in parallel. This step creates the intermediate state necessary to generate the first output token. This intermediate state includes the key and value vectors for all input tokens.

**Decode**
The model generates one output token at a time.

As explored later in Chapter 9, the parallelizable nature of prefilling and the sequential aspect of decoding both motivate many optimization techniques to make language model inference cheaper and faster.

**Attention mechanism.** At the heart of the transformer architecture is the attention mechanism. Understanding this mechanism is necessary to understand how transformer models work. Under the hood, the attention mechanism leverages key, value, and query vectors:

- The query vector (Q) represents the current state of the decoder at each decoding step. Using the same book summary example, this query vector can be thought of as the person looking for information to create a summary.
- Each key vector (K) represents a previous token. If each previous token is a page in the book, each key vector is like the page number. Note that at a given decoding step, previous tokens include both input tokens and previously generated tokens.

7 Bahdanau et al., “Neural Machine Translation by Jointly Learning to Align and Translate”.

• Each value vector (V) represents the actual value of a previous token, as learned
by the model. Each value vector is like the page’s content.
The attention mechanism computes how much attention to give an input token by
performing a dot product between the query vector and its key vector. A high score
means that the model will use more of that page’s content (its value vector) when
generating the book’s summary. A visualization of the attention mechanism with the
key, value, and query vectors is shown in Figure 2-5. In this visualization, the query
vector is seeking information from the previous tokens How, are, you, ?, ¿ to gen‐
erate the next token.
Figure 2-5. An example of the attention mechanism in action next to its high-level visu‐
alization from the famous transformer paper, “Attention Is All You Need” (Vaswani et
al., 2017).
Because each previous token has a corresponding key and value vector, the longer
the sequence, the more key and value vectors need to be computed and stored. This
is one reason why it’s so hard to extend context length for transformer models. How
to efficiently compute and store key and value vectors comes up again in Chapters 7
and 9.
Let’s look into how the attention function works. Given an input x, the key, value,
and query vectors are computed by applying key, value, and query matrices to the
input. Let WK, WV, and WQ be the key, value, and query matrices. The key, value, and
query vectors are computed as follows:
Modeling | 61

[Visual content extracted via GLM-OCR]

Each value vector (V) represents the actual value of a previous token, as learned by the model. Each value vector is like the page’s content.

The attention mechanism computes how much attention to give an input token by performing a dot product between the query vector and its key vector. A high score means that the model will use more of that page’s content (its value vector) when generating the book’s summary. A visualization of the attention mechanism with the key, value, and query vectors is shown in Figure 2-5. In this visualization, the query vector is seeking information from the previous tokens How, are, you, ?, to generate the next token.

Figure 2-5. An example of the attention mechanism in action next to its high-level visualization from the famous transformer paper, “Attention Is All You Need” (Vaswani et al., 2017).

Because each previous token has a corresponding key and value vector, the longer the sequence, the more key and value vectors need to be computed and stored. This is one reason why it’s so hard to extend context length for transformer models. How to efficiently compute and store key and value vectors comes up again in Chapters 7 and 9.

Let’s look into how the attention function works. Given an input $x$, the key, value, and query vectors are computed by applying key, value, and query matrices to the input. Let $W_K$, $W_V$, and $W_Q$ be the key, value, and query matrices. The key, value, and query vectors are computed as follows:

8 Because input tokens are processed in batch, the actual input vector has the shape N × T × 4096, where N is the
batch size and T is the sequence length. Similarly, each resulting K, V, Q vector has the dimension of N × T ×
4096.
K = xWK
V = xWV
Q = xWQ
The query, key, and value matrices have dimensions corresponding to the model’s
hidden dimension. For example, in Llama 2-7B ( Touvron et al., 2023 ), the model’s
hidden dimension size is 4096, meaning that each of these matrices has a 4096 ×
4096 dimension. Each resulting K, V, Q vector has the dimension of 4096.8
The attention mechanism is almost always multi-headed. Multiple heads allow the
model to attend to different groups of previous tokens simultaneously. With multiheaded attention, the query, key, and value vectors are split into smaller vectors, each
corresponding to an attention head. In the case of Llama 2-7B, because it has 32
attention heads, each K, V, and Q vector will be split into 32 vectors of the dimension
128. This is because 4096 / 32 = 128.
Attention(Q, K , V ) = softmax(
Q K T
d )V
The outputs of all attention heads are then concatenated. An output projection
matrix is used to apply another transformation to this concatenated output before it’s
fed to the model’s next computation step. The output projection matrix has the same
dimension as the model’s hidden dimension.
Transformer block.    Now that we’ve discussed how attention works, let’s see how it’s
used in a model. A transformer architecture is composed of multiple transformer
blocks. The exact content of the block varies between models, but, in general, each
transformer block contains the attention module and the MLP (multi-layer percep‐
tron) module:
Attention module
Each attention module consists of four weight matrices: query, key, value, and
output projection.
MLP module
An MLP module consists of linear layers separated by nonlinear activation func‐
tions. Each linear layer is a weight matrix that is used for linear transformations,
whereas an activation function allows the linear layers to learn nonlinear pat‐
terns. A linear layer is also called a feedforward layer.
62 | Chapter 2: Understanding Foundation Models

9 Why do simple activation functions work for complex models like LLMs? There was a time when the research
community raced to come up with sophisticated activation functions. However, it turned out that fancier
activation functions didn’t work better. The model just needs a nonlinear function to break the linearity from
the feedforward layers. Simpler functions that are faster to compute are better, as the more sophisticated ones
take up too much training compute and memory.
Common nonlinear functions are ReLU, Rectified Linear Unit ( Agarap, 2018 ),
and GELU ( Hendrycks and Gimpel, 2016 ), which was used by GPT-2 and
GPT-3, respectively. Action functions are very simple. 9 For example, all ReLU
does is convert negative values to 0. Mathematically, it’s written as:
ReLU(x) = max(0, x)
The number of transformer blocks in a transformer model is often referred to as that
model’s number of layers. A transformer-based language model is also outfitted with
a module before and after all the transformer blocks:
An embedding module before the transformer blocks
This module consists of the embedding matrix and the positional embedding
matrix, which convert tokens and their positions into embedding vectors, respec‐
tively. Naively, the number of position indices determines the model’s maximum
context length. For example, if a model keeps track of 2,048 positions, its maxi‐
mum context length is 2,048. However, there are techniques that increase a
model’s context length without increasing the number of position indices.
An output layer after the transformer blocks
This module maps the model’s output vectors into token probabilities used to
sample model outputs (discussed in “Sampling”  on page 88). This module typi‐
cally consists of one matrix, which is also called the unembedding layer . Some
people refer to the output layer as the model head, as it’s the model’s last layer
before output generation.
Figure 2-6  visualizes a transformer model architecture. The size of a transformer
model is determined by the dimensions of its building blocks. Some of the key values
are:
• The model’s dimension determines the sizes of the key, query, value, and output
projection matrices in the transformer block.
• The number of transformer blocks.
• The dimension of the feedforward layer.
• The vocabulary size.
Modeling | 63

Larger dimension values result in larger model sizes. Table 2-4 shows these dimension values for different Llama 2 (Touvron et al., 2023) and Llama 3 (Dubey et al., 2024) models. Note that while the increased context length impacts the model’s memory footprint, it doesn’t impact the model’s total number of parameters.

Table 2-4. The dimension values of different Llama models.

| Model | # transformer blocks | Model dim | Feedforward dim | Vocab size | Context length |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Llama 2-7B | 32 | 4,096 | 11,008 | 32K | 4K |
| Llama 2-13B | 40 | 5,120 | 13,824 | 32K | 4K |
| Llama 2-70B | 80 | 8,192 | 22,016 | 32K | 4K |
| Llama 3-7B | 32 | 4,096 | 14,336 | 128K | 128K |
| Llama 3-70B | 80 | 8,192 | 28,672 | 128K | 128K |
| Llama 3-405B | 126 | 16,384 | 53,248 | 128K | 128K |

10 Fun fact: Ilya Sutskever, an OpenAI co-founder, is the first author on the seq2seq paper and the second
author on the AlexNet paper.
11 Ilya Sutskever has an interesting argument about why it’s so hard to develop new neural network architec‐
tures to outperform existing ones. In his argument, neural networks are great at simulating many computer
programs. Gradient descent, a technique to train neural networks, is in fact a search algorithm to search
through all the programs that a neural network can simulate to find the best one for its target task. This
means that new architectures can potentially be simulated by existing ones too. For new architectures to out‐
perform existing ones, these new architectures have to be able to simulate programs that existing architec‐
tures cannot. For more information, watch Sutskever’s talk at the Simons Institute at Berkeley (2023) .
12 The transformer was originally designed by Google to run fast on Tensor Processing Units (TPUs), and was
only later optimized on GPUs.
Other model architectures
While the transformer model dominates the landscape, it’s not the only architecture.
Since AlexNet revived the interest in deep learning in 2012, many architectures have
gone in and out of fashion. Seq2seq was in the limelight for four years (2014–2018).
GANs (generative adversarial networks) captured the collective imagination a bit
longer (2014–2019). Compared to architectures that came before it, the transformer
is sticky. It’s been around since 2017. 10 How long until something better comes
along?
Developing a new architecture to outperform transformers isn’t easy. 11 The trans‐
former has been heavily optimized since 2017. A new architecture that aims to
replace the transformer will have to perform at the scale that people care about, on
the hardware that people care about.12
However, there’s hope. While transformer-based models are dominating, as of this
writing, several alternative architectures are gaining traction.
One popular model is RWKV (Peng et al., 2023), an RNN-based model that can be
parallelized for training. Due to its RNN nature, in theory, it doesn’t have the same
context length limitation that transformer-based models have. However, in practice,
having no context length limitation doesn’t guarantee good performance with long
context.
Modeling long sequences remains a core challenge in developing LLMs. An architec‐
ture that has shown a lot of promise in long-range memory is SSMs (state space mod‐
els) ( Gu et al., 2021a ). Since the architecture’s introduction in 2021, multiple
techniques have been introduced to make the architecture more efficient, better at
long sequence processing, and scalable to larger model sizes. Here are a few of these
techniques, to illustrate the evolution of a new architecture:
Modeling | 65

• S4, introduced in “Efficiently Modeling Long Sequences with Structured State
Spaces” ( Gu et al., 2021b), was developed to make SSMs more efficient.
• H3, introduced in “Hungry Hungry Hippos: Towards Language Modeling with
State Space Models” ( Fu et al., 2022 ), incorporates a mechanism that allows the
model to recall early tokens and compare tokens across sequences. This mecha‐
nism’s purpose is akin to that of the attention mechanism in the transformer
architecture, but it is more efficient.
• Mamba, introduced in “Mamba: Linear-Time Sequence Modeling with Selective
State Spaces” ( Gu and Dao, 2023 ), scales SSMs to three billion parameters. On
language modeling, Mamba-3B outperforms transformers of the same size and
matches transformers twice its size. The authors also show that Mamba’s infer‐
ence computation scales linearly with sequence length (compared to quadratic
scaling for transformers). Its performance shows improvement on real data up to
million-length sequences.
• Jamba, introduced in “Jamba: A Hybrid Transformer–Mamba Language Model”
(Lieber et al., 2024 ), interleaves blocks of transformer and Mamba layers to scale
up SSMs even further. The authors released a mixture-of-experts model with 52B
total available parameters  (12B active parameters) designed to fit in a single 80
GB GPU. Jamba shows strong performance on standard language model bench‐
marks and long-context evaluations for up to a context length of 256K tokens. It
also has a small memory footprint compared to vanilla transformers.
Figure 2-7 visualizes the transformer, Mamba, and Jamba blocks.
While it’s challenging to develop an architecture that outperforms the transformer,
given its many limitations, there are a lot of incentives to do so. If another architec‐
ture does indeed overtake the transformer, some of the model adaptation techniques
discussed in this book might change. However, just as the shift from ML engineering
to AI engineering has kept many things unchanged, changing the underlying model
architecture won’t alter the fundamental approaches.
66 | Chapter 2: Understanding Foundation Models
