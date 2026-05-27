---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 136
section-title: Model Merging and Multi-Task Finetuning
source-location: pages 371-380
previous-section: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
classification: reusable-knowledge-candidate
---
# Model Merging and Multi-Task Finetuning

Due to its memory-saving promise, quantized LoRA is an active area of research.
Other than QLoRA, quantized LoRA works include QA-LoRA ( Xu et al., 2023 ),
ModuLoRA (Yin et al., 2023), and IR-QLoRA (Qin et al., 2024).
Model Merging and Multi-Task Finetuning
If finetuning allows you to create a custom model by altering a single model, model
merging allows you to create a custom model by combining multiple models. Model
merging offers you greater flexibility than finetuning alone. You can take two avail‐
able models and merge them together to create a new, hopefully more useful, model.
You can also finetune any or all of the constituent models before merging them
together.
While you don’t have to further finetune the merged model, its performance can
often be improved by finetuning. Without finetuning, model merging can be done
without GPUs, making merging particularly attractive to indie model developers that
don’t have access to a lot of compute.
The goal of model merging is to create a single model that provides more value than
using all the constituent models separately. The added value can come from
improved performance. For example, if you have two models that are good at differ‐
ent things on the same task, you can merge them into a single model that is better
than both of them on that task. Imagine one model that can answer the first 60% of
the questions and another model that can answer the last 60% of the questions. Com‐
bined, perhaps they can answer 80% of the questions.
The added value can also come from a reduced memory footprint, which leads to
reduced costs. For example, if you have two models that can do different tasks, they
can be merged into one model that can do both tasks but with fewer parameters. This
is particularly attractive for adapter-based models. Given two models that were fine‐
tuned on top of the same base model, you can combine their adapters into a single
adapter.
One important use case of model merging is multi-task finetuning. Without model
merging, if you want to a finetune a model for multiple tasks, you generally have to
follow one of these approaches:
Simultaneous finetuning
You create a dataset with examples for all the tasks and finetune the model on
this dataset to make the model learn all the tasks simultaneously. However,
because it’s generally harder to learn multiple skills at the same time, this
approach typically requires more data and more training.
Finetuning Techniques | 347

28 My book, Designing Machine Learning Systems has a section on “ML on the Cloud and on the Edge.”
Sequential finetuning
You can finetune the model on each task separately but sequentially. After train‐
ing a model on task A, train it on task B, and so on. The assumption is that it’s
easier for models to learn one task at a time. Unfortunately, neural networks are
prone to catastrophic forgetting ( Kirkpatrick et al., 2016 ). A model can forget
how to do an old task when it’s trained on a new task, leading to a significant
performance drop on earlier tasks.
Model merging offers another method for multi-task finetuning. You can finetune
the model on different tasks separately but in parallel. Once done, these different
models are merged together. Finetuning on each task separately allows the model to
learn that task better. Because there’s no sequential learning, there’s less risk of cata‐
strophic forgetting.
Model merging is also appealing when you have to deploy models to devices such as
phones, laptops, cars, smartwatches, and warehouse robots. On-device deployment is
often challenging because of limited on-device memory capacity. Instead of squeez‐
ing multiple models for different tasks onto a device, you can merge these models
together into one model that can perform multiple tasks while requiring much less
memory.
On-device deployment is necessary for use cases where data can’t leave the device
(often due to privacy), or where there’s limited or unreliable internet access. Ondevice deployment can also significantly reduce inference costs. The more computa‐
tion you can offload to user devices, the less you have to pay to data centers.28
Model merging is one way to do federated learning (McMahan et al., 2016), in which
multiple devices train the same model using separate data. For example, if you deploy
model X to multiple devices, each copy of X can continue learning separately from
the on-device data. After a while, you have multiple copies of X, all trained on differ‐
ent data. You can merge these copies together into one new base model that contains
the learning of all constituent models.
The idea of combining models together to obtain better performance started with
model ensemble methods . According to Wikipedia, ensembling combines “multiple
learning algorithms to obtain better predictive performance than could be obtained
from any of the constituent learning algorithms alone.” If model merging typically
involves mixing parameters of constituent models together, ensembling typically
combines only model outputs while keeping each constituent model intact.
348 | Chapter 7: Finetuning

29 You can read more about ensemble methods in my book Designing Machine Learning Systems.
For example, in ensembling, given a query, you might use three models to generate
three different answers. Then, a final answer is generated based on these three
answers, using a simple majority vote or another trainable ML module. 29 While
ensembling can generally improve performance, it has a higher inference cost since it
requires multiple inference calls per request.
Figure 7-13  compares ensembling and model merging. Just like model ensembles
used to dominate leaderboards, many models on top of the Hugging Face’s Open
LLM Leaderboard are merged models.
Figure 7-13. How ensembling and model merging work.
Many model-merging techniques are experimental and might become outdated as
the community gains a better understanding of the underlying theory. For this rea‐
son, I’ll focus on the high-level merging approaches instead of any individual
technique.
Model merging approaches differ in how the constituent parameters are combined.
Three approaches covered here are summing, layer stacking, and concatenation.
Figure 7-14 shows their high-level differences.
Finetuning Techniques | 349

[Visual content extracted via GLM-OCR]

For example, in ensembling, given a query, you might use three models to generate three different answers. Then, a final answer is generated based on these three answers, using a simple majority vote or another trainable ML module. While ensembling can generally improve performance, it has a higher inference cost since it requires multiple inference calls per request.

Figure 7-13 compares ensembling and model merging. Just like model ensembles used to dominate leaderboards, many models on top of the Hugging Face’s Open LLM Leaderboard are merged models.

Figure 7-13. How ensembling and model merging work.

Many model-merging techniques are experimental and might become outdated as the community gains a better understanding of the underlying theory. For this reason, I’ll focus on the high-level merging approaches instead of any individual technique.

Model merging approaches differ in how the constituent parameters are combined. Three approaches covered here are summing, layer stacking, and concatenation. Figure 7-14 shows their high-level differences.

29 You can read more about ensemble methods in my book Designing Machine Learning Systems.

Figure 7-14. Three main approaches to model merging: summing, layer stacking, and
concatenation.
You can mix these approaches when merging models, e.g., summing some layers and
stacking others. Let’s explore each of these approaches.
Summing
This approach involves adding the weight values of constituent models together. I’ll
discuss two summing methods: linear combination and spherical linear interpola‐
tion. If the parameters in two models are in different scales, e.g., one model’s parame‐
ter values are much larger than the other’s, you can rescale the models before
summing so that their parameter values are in the same range.
Linear combination.    Linear combination includes both an average and a weighted
average. Given two models, A and B, their weighted average is:
Merge(A, B) =
W AA + W B B
W A + W B
Figure 7-15 shows how to linearly combine two layers when wA = wB = 1.
350 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

You can mix these approaches when merging models, e.g., summing some layers and stacking others. Let’s explore each of these approaches.

Summing

This approach involves adding the weight values of constituent models together. I’ll discuss two summing methods: linear combination and spherical linear interpolation. If the parameters in two models are in different scales, e.g., one model’s parameter values are much larger than the other’s, you can rescale the models before summing so that their parameter values are in the same range.

Linear combination. Linear combination includes both an average and a weighted average. Given two models, A and B, their weighted average is:

$$\text{Merge}(A, B) = \frac{W_A A + W_B B}{W_A + W_B}$$

Figure 7-15 shows how to linearly combine two layers when $w_A = w_B = 1$.

30 Averaging works not just with weights but also with embeddings. For example, given a sentence, you can use
a word embedding algorithm to generate an embedding vector for each word in the sentence, then average all
these word embeddings into a sentence embedding. When I started out in ML, I couldn’t believe that averag‐
ing seems to just work. It’s magical when simple components, when used correctly, can create something so
wonderfully perplexing, like AI.
Figure 7-15. Merging parameters by averaging them.
Linear combination works surprisingly well, given how simple it is. 30 The idea that
multiple models can be linearly combined to create a better one was studied as early
as the early 1990s ( Perrone, 1993 ). Linear combination is often used in federated
learning (Wang et al., 2020).
You can linearly combine entire models or parts of models. Model soups ( Wortsman
et al., 2022 ) showed how averaging the entire weights of multiple finetuned models
can improve accuracy without increasing inference time. However, it’s more com‐
mon to merge models by linearly combining specific components, such as their
adapters.
While you can linearly combine any set of models, linear combination is the most
effective for models finetuned on top of the same base model. In this case, linear combi‐
nation can be viewed through the concept of task vectors. The idea is that once you’ve
finetuned a model for a specific task, subtracting the base model from it should give
you a vector that captures the essence of the task. Task vectors are also called delta
parameters. If you finetune using LoRA, you can construct the task vector from the
LoRA weights.
Task vectors allow us to do task arithmetic (Ilharco et al., 2022 ), such as adding two
task vectors to combine task capabilities or subtracting a task vector to reduce spe‐
cific capabilities. Task subtraction can be useful for removing undesirable model
behaviors, such as invasive capabilities like facial recognition or biases obtained dur‐
ing pre-training.
Linear combination is straightforward when the components to be merged are of the
same architecture and of the same size. However, it can also work for models that
don’t share the same architecture or the same size. For example, if one model’s layer
Finetuning Techniques | 351

[Visual content extracted via GLM-OCR]

Linear combination works surprisingly well, given how simple it is. The idea that multiple models can be linearly combined to create a better one was studied as early as the early 1990s (Perrone, 1993). Linear combination is often used in federated learning (Wang et al., 2020).

You can linearly combine entire models or parts of models. Model soups (Wortsman et al., 2022) showed how averaging the entire weights of multiple finetuned models can improve accuracy without increasing inference time. However, it’s more common to merge models by linearly combining specific components, such as their adapters.

While you can linearly combine any set of models, linear combination is the most effective for models finetuned on top of the same base model. In this case, linear combination can be viewed through the concept of task vectors. The idea is that once you’ve finetuned a model for a specific task, subtracting the base model from it should give you a vector that captures the essence of the task. Task vectors are also called delta parameters. If you finetune using LoRA, you can construct the task vector from the LoRA weights.

Task vectors allow us to do task arithmetic (Ilharco et al., 2022), such as adding two task vectors to combine task capabilities or subtracting a task vector to reduce specific capabilities. Task subtraction can be useful for removing undesirable model behaviors, such as invasive capabilities like facial recognition or biases obtained during pre-training.

Linear combination is straightforward when the components to be merged are of the same architecture and of the same size. However, it can also work for models that don’t share the same architecture or the same size. For example, if one model’s layer

30 Averaging works not just with weights but also with embeddings. For example, given a sentence, you can use a word embedding algorithm to generate an embedding vector for each word in the sentence, then average all these word embeddings into a sentence embedding. When I started out in ML, I couldn’t believe that averaging seems to just work. It’s magical when simple components, when used correctly, can create something so wonderfully perplexing, like AI.

is larger than that of the other model, you can project one or both layers into the
same dimension.
Some people proposed aligning models before averaging to ensure that functionally
related parameters are averaged together, such as in “Model Fusion via Optimal
Transport” ( Singh and Jaggi, 2020 ), “Git Re-Basin: Merging Models Modulo Permu‐
tation Symmetries” ( Ainsworth et al., 2022 ), and “Merging by Matching Models in
Task Parameter Subspaces” ( Tam et al., 2023 ). While it makes sense to combine
aligned parameters, aligning parameters can be challenging to do, and, therefore, this
approach is less common on naive linear combinations.
Spherical linear interpolation (SLERP).    Another common model summing method is
SLERP, which is based on the mathematical operator of the same name, Spherical
LinEar inteRPolation.
Interpolation means estimating unknown values based on known
values. In the case of model merging, the unknown value is the
merged model, and the known values are the constituent models.
Linear combination is one interpolation technique. SLERP is
another.
Because the formula for SLERP is mathy, and model-merging tools typically imple‐
ment it for you, I won’t go into the details here. Intuitively, you can think of each
component (vector) to be merged as a point on a sphere. To merge two vectors, you
first draw the shortest path between these two points along the sphere’s surface. This
is similar to drawing the shortest path between two cities along the Earth’s surface.
The merged vector of these two vectors is a point along their shortest path. Where
exactly the point falls along the path depends on the interpolation factor, which you
can set to be between 0 and 1. Factor values less than 0.5 bring the merged vector
closer to the first vector, which means that the first task vector will contribute more
to the result. A factor of 0.5 means that you pick a point exactly halfway. This middle
point is the blue point in Figure 7-16.
SLERP, as a mathematical operation, is defined with only two vectors, which means
that you can merge only two vectors at a time. If you want to merge more than two
vectors, you can potentially do SLERP sequentially, i.e., merging A with B, and then
merging that result with C.
352 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

is larger than that of the other model, you can project one or both layers into the same dimension.

Some people proposed aligning models before averaging to ensure that functionally related parameters are averaged together, such as in “Model Fusion via Optimal Transport” (Singh and Jaggi, 2020), “Git Re-Basin: Merging Models Modulo Permutation Symmetries” (Ainsworth et al., 2022), and “Merging by Matching Models in Task Parameter Subspaces” (Tam et al., 2023). While it makes sense to combine aligned parameters, aligning parameters can be challenging to do, and, therefore, this approach is less common on naive linear combinations.

Spherical linear interpolation (SLERP). Another common model summing method is SLERP, which is based on the mathematical operator of the same name, Spherical LinEar inteRPolation.

Interpolation means estimating unknown values based on known values. In the case of model merging, the unknown value is the merged model, and the known values are the constituent models. Linear combination is one interpolation technique. SLERP is another.

Because the formula for SLERP is mathy, and model-merging tools typically implement it for you, I won’t go into the details here. Intuitively, you can think of each component (vector) to be merged as a point on a sphere. To merge two vectors, you first draw the shortest path between these two points along the sphere’s surface. This is similar to drawing the shortest path between two cities along the Earth’s surface. The merged vector of these two vectors is a point along their shortest path. Where exactly the point falls along the path depends on the interpolation factor, which you can set to be between 0 and 1. Factor values less than 0.5 bring the merged vector closer to the first vector, which means that the first task vector will contribute more to the result. A factor of 0.5 means that you pick a point exactly halfway. This middle point is the blue point in Figure 7-16.

SLERP, as a mathematical operation, is defined with only two vectors, which means that you can merge only two vectors at a time. If you want to merge more than two vectors, you can potentially do SLERP sequentially, i.e., merging A with B, and then merging that result with C.

31 The assumption is that the parameters that undergo the most substantial changes during finetuning are the
ones most crucial for the target task.
Figure 7-16. How SLERP works for two vectors t1 and t2. The red line is their shortest
path on the spherical surface. Depending on the interpolation, the merged vector can be
any point along this path. The blue vector is the resulting merged vector when the inter‐
polation factor is 0.5.
Pruning redundant task-specific parameters.    During finetuning, many models’ parame‐
ters are adjusted. However, most of these adjustments are minor and don’t signifi‐
cantly contribute to the model’s performance on the task. 31 Adjustments that don’t
contribute to the model’s performance are considered redundant.
In the paper “TIES-Merging: Resolving Interference When Merging Models”, Yadav
et al. (2023) showed that you can reset a large portion of task vector parameters with
minimal performance degradation, as shown in Figure 7-17. Resetting means chang‐
ing the finetuned parameter to its original value in the base model, effectively setting
the corresponding task vector parameter to zero. (Recall that the task vector can be
obtained by subtracting the base model from the finetuned model.)
Figure 7-17. In Yadav et al.’s experiments, keeping the top 20% of the task vector
parameters gives comparable performance to keeping 100% of the parameters.
Finetuning Techniques | 353

[Visual content extracted via GLM-OCR]

Figure 7-16. How SLERP works for two vectors $t_1$ and $t_2$. The red line is their shortest path on the spherical surface. Depending on the interpolation, the merged vector can be any point along this path. The blue vector is the resulting merged vector when the interpolation factor is 0.5.

Pruning redundant task-specific parameters. During finetuning, many models’ parameters are adjusted. However, most of these adjustments are minor and don’t significantly contribute to the model’s performance on the task. Adjustments that don’t contribute to the model’s performance are considered redundant.

In the paper “TIES-Merging: Resolving Interference When Merging Models”, Yadav et al. (2023) showed that you can reset a large portion of task vector parameters with minimal performance degradation, as shown in Figure 7-17. Resetting means changing the finetuned parameter to its original value in the base model, effectively setting the corresponding task vector parameter to zero. (Recall that the task vector can be obtained by subtracting the base model from the finetuned model.)

Figure 7-17. In Yadav et al.’s experiments, keeping the top 20% of the task vector parameters gives comparable performance to keeping 100% of the parameters.

31 The assumption is that the parameters that undergo the most substantial changes during finetuning are the ones most crucial for the target task.

32 TIES is abbreviated from “TrIm, Elect Sign, and merge,” while DARE is from “Drop And REscale.” I know,
these abbreviations pain me too.
33 When task vectors are pruned, they become more sparse, but the finetuned model doesn’t. Pruning, in this
case, isn’t to reduce the memory footprint or inference latency, but to improve performance.
These redundant parameters, while not harmful to one model, might be harmful to
the merged model. Merging techniques such as TIES (Yadav et al., 2023) and DARE
(Yu et al., 2023) first prune the redundant parameters from task vectors before merg‐
ing them.32 Both papers showed that this practice can significantly improve the qual‐
ity of the final merged models. The more models there are to merge, the more
important pruning is because there are more opportunities for redundant parameters
in one task to interfere with other tasks.33
Layer stacking
In this approach, you take different layers from one or more models and stack them
on top of each other. For example, you might take the first layer from model 1 and
the second layer from model 2. This approach is also called passthrough or franken‐
merging. It can create models with unique architectures and numbers of parameters.
Unlike the merging by summing approach, the merged models resulting from layer
stacking typically require further finetuning to achieve good performance.
One early success of frankenmerging is Goliath-120B (alpindale, 2023), which was
merged from two finetuned Llama 2-70B models, Xwin and Euryale. It took 72 out of
80 layers from each model and merged them together.
Layer stacking can be used to train mixture-of-experts (MoE) models, as introduced
in “Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints”
(Komatsuzaki et al., 2022 ). Rather than training an MOE from scratch, you take a
pre-trained model and make multiple copies of certain layers or modules. A router is
then added to send each input to the most suitable copy. You then further train the
merged model along with the router to refine their performance. Figure 7-18 illus‐
trates this process.
Komatsuzaki et al. showed that layer stacking can produce models that outperform
MoE models trained from scratch. Using this approach, Together AI mixed six
weaker open source models together to create Mixture-of-Agents, which achieved
comparable performance to OpenAI’s GPT-4o in some benchmarks ( Wang et al.,
2024).
354 | Chapter 7: Finetuning

Figure 7-18. You can create an MoE model from a pre-trained model. Image adapted
from Komatsuzaki et al. (2022).
An interesting use case of layer stacking is model upscaling. Model upscaling is the
study of how to create larger models using fewer resources. Sometimes, you might
want a bigger model than what you already have, presumably because bigger models
give better performance. For example, your team might have originally trained a
model to fit on your 40 GB GPU. However, you obtained a new machine with 80 GB,
which allows you to serve a bigger model. Instead of training a new model from
scratch, you can use layer stacking to create a larger model from the existing model.
One approach to layer upscaling is depthwise scaling. Kim et al. (2023) used this tech‐
nique to create SOLAR 10.7B from one 7B-parameter model with 32 layers. The pro‐
cedure works as follows:
1. Make a copy of the original pre-trained model.
2. Merge these two copies by summing certain layers (summing two layers and
turning them into one layer) and stacking the rest. The layers to be summed are
carefully selected to match the target model size. For SOLAR 10.7B, 16 layers are
summed, leaving the final model with 32 × 2 - 16 = 48 layers.
3. Further train this upscaled model toward the target performance.
Figure 7-19 illustrates this process.
Finetuning Techniques | 355

[Visual content extracted via GLM-OCR]

An interesting use case of layer stacking is model upscaling. Model upscaling is the study of how to create larger models using fewer resources. Sometimes, you might want a bigger model than what you already have, presumably because bigger models give better performance. For example, your team might have originally trained a model to fit on your 40 GB GPU. However, you obtained a new machine with 80 GB, which allows you to serve a bigger model. Instead of training a new model from scratch, you can use layer stacking to create a larger model from the existing model.

One approach to layer upscaling is depthwise scaling. Kim et al. (2023) used this technique to create SOLAR 10.7B from one 7B-parameter model with 32 layers. The procedure works as follows:

1. Make a copy of the original pre-trained model.
2. Merge these two copies by summing certain layers (summing two layers and turning them into one layer) and stacking the rest. The layers to be summed are carefully selected to match the target model size. For SOLAR 10.7B, 16 layers are summed, leaving the final model with $32 \times 2 - 16 = 48$ layers.
3. Further train this upscaled model toward the target performance.

Figure 7-19 illustrates this process.

Figure 7-19. Use depthwise scaling to create a 48-layer model from a 32-layer model.
The image is licensed under CC BY 4.0 and was slightly modified for readability.
Concatenation
Instead of adding the parameters of the constituent models together in different
manners, you can also concatenate them. The merged component’s number of
parameters will be the sum of the number of parameters from all constituent compo‐
nents. If you merge two LoRA adapters of ranks r1 and r2, the merged adapter’s rank
will be r1 + r2, as shown in Figure 7-20.
Figure 7-20. If you merge two LoRA adapters using concatenation, the rank of the
merged adapter will be the sum of both adapters’ ranks.
356 | Chapter 7: Finetuning

[Visual content extracted via GLM-OCR]

Figure 7-19. Use depthwise scaling to create a 48-layer model from a 32-layer model. The image is licensed under CC BY 4.0 and was slightly modified for readability.

Concatenation

Instead of adding the parameters of the constituent models together in different manners, you can also concatenate them. The merged component’s number of parameters will be the sum of the number of parameters from all constituent components. If you merge two LoRA adapters of ranks $r_1$ and $r_2$, the merged adapter’s rank will be $r_1 + r_2$, as shown in Figure 7-20.

Figure 7-20. If you merge two LoRA adapters using concatenation, the rank of the merged adapter will be the sum of both adapters’ ranks.
