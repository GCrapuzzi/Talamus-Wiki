---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 137
section-title: Finetuning Tactics
source-location: pages 381-384
previous-section: AI Space/normalized/pdf/ai-engineering/sections/136-model-merging-and-multi-task-finetuning.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
classification: reusable-knowledge-candidate
---
# Finetuning Tactics

34 I debated for a long time whether to include the concatenation technique in this book, and decided to include
it for completeness.
35 In college, I made the painful mistake of letting my model train overnight, only to have it crash after eight
hours because I tried to save the checkpoint in a nonexistent folder. All that progress was lost.
Concatenation isn’t recommended because it doesn’t reduce the memory footprint
compared to serving different models separately. Concatenation might give better
performance, but the incremental performance might not be worth the number of
extra parameters.34
Finetuning Tactics
This chapter has discussed multiple finetuning approaches, what problems they
solve, and how they work. In this last section, I’ll focus on more practical finetuning
tactics.
Finetuning frameworks and base models
While many things around finetuning—deciding whether to finetune, acquiring data,
and maintaining finetuned models—are hard, the actual process of finetuning is
more straightforward. There are three things you need to choose: a base model, a
finetuning method, and a framework for finetuning.
Base models.    Chapter 4 already covered the criteria for model selection that can be
applied to both prompt-based methods and finetuning. Some of the criteria discussed
include model size, licenses, and benchmark performance. At the beginning of an AI
project, when you’re still exploring the feasibility of your task, it’s useful to start with
the most powerful model you can afford. If this model struggles to produce good
results, weaker models are likely to perform even worse. If the strongest model meets
your needs, you can then explore weaker models, using the initial model as a bench‐
mark for comparison.
For finetuning, the starting models vary for different projects. OpenAI’s finetuning
best practices document  gives examples of two development paths: the progression
path and the distillation path.
The progression path looks like this:
1. Test your finetuning code using the cheapest and fastest model to make sure the
code works as expected.35
2. Test your data by finetuning a middling model. If the training loss doesn’t go
down with more data, something might be wrong.
Finetuning Techniques | 357

3. Run a few more experiments with the best model to see how far you can push
performance.
4. Once you have good results, do a training run with all models to map out the
price/performance frontier and select the model that makes the most sense for
your use case.
The distillation path might look as follows:
1. Start with a small dataset and the strongest model you can afford. Train the best
possible model with this small dataset. Because the base model is already strong,
it requires less data to achieve good performance.
2. Use this finetuned model to generate more training data.
3. Use this new dataset to train a cheaper model.
Because finetuning usually comes after experiments with prompt engineering, by the
time you start to finetune, ideally, you should have a pretty good understanding of
different models’ behaviors. You should plan your finetuning development path
based on this understanding.
Finetuning methods.    Recall that adapter techniques like LoRA are cost-effective but
typically don’t deliver the same level of performance as full finetuning. If you’re just
starting with finetuning, try something like LoRA, and attempt full finetuning later.
The finetuning methods to use also depend on your data volume. Depending on the
base model and the task, full finetuning typically requires at least thousands of exam‐
ples and often many more. PEFT methods, however, can show good performance
with a much smaller dataset. If you have a small dataset, such as a few hundred exam‐
ples, full finetuning might not outperform LoRA.
Take into account how many finetuned models you need and how you want to serve
them when deciding on a finetuning method. Adapter-based methods like LoRA
allow you to more efficiently serve multiple models that share the same base model.
With LoRA, you only need to serve a single full model, whereas full finetuning
requires serving multiple full models.
Finetuning frameworks.    The easiest way to finetune is to use a finetuning API where
you can upload data, select a base model, and get back a finetuned model. Like model
inference APIs, finetuning APIs can be provided by model providers, cloud service
providers, and third-party providers. A limitation of this approach is that you’re limi‐
ted to the base models that the API supports. Another limitation is that the API
might not expose all the knobs you can use for optimal finetuning performance.
Finetuning APIs are suitable for those who want something quick and easy, but they
might be frustrating for those who want more customization.
358 | Chapter 7: Finetuning

You can also finetune using one of many great finetuning frameworks available, such
as LLaMA-Factory, unsloth, PEFT, Axolotl, and LitGPT. They support a wide range
of finetuning methods, especially adapter-based techniques. If you want to do full
finetuning, many base models provide their open source training code on GitHub
that you can clone and run with your own data. Llama Police has a more comprehen‐
sive and up-to-date list of finetuning frameworks and model repositories.
Doing your own finetuning gives you more flexibility, but you’ll have to provision the
necessary compute. If you do only adapter-based techniques, a mid-tier GPU might
suffice for most models. If you need more compute, you can choose a framework that
integrates seamlessly with your cloud provider.
To finetune a model using more than one machine, you’ll need a framework that
helps you do distributed training, such as DeepSpeed, PyTorch Distributed , and
ColossalAI.
Finetuning hyperparameters
Depending on the base model and the finetuning method, there are many hyperpara‐
meters you can tune to improve finetuning efficiency. For specific hyperparameters
for your use case, check out the documentation of the base model or the finetuning
framework you use. Here, I’ll cover a few important hyperparameters that frequently
appear.
Learning rate.    The learning rate determines how fast the model’s parameters should
change with each learning step. If you think of learning as finding a path toward a
goal, the learning rate is the step size. If the step size is too small, it might take too
long to get to the goal. If the step size is too big, you might overstep the goal, and,
hence, the model might never converge.
A universal optimal learning rate doesn’t exist. You’ll have to experiment with differ‐
ent learning rates, typically between the range of 1e-7 to 1e-3, to see which one works
best. A common practice is to take the learning rate at the end of the pre-training
phase and multiply it with a constant between 0.1 and 1.
The loss curve can give you hints about the learning rate. If the loss curve fluctuates a
lot, it’s likely that the learning rate is too big. If the loss curve is stable but takes a long
time to decrease, the learning is likely too small. Increase the learning rate as high as
the loss curve remains stable.
You can vary learning rates during the training process. You can use larger learning
rates in the beginning and smaller learning rates near the end. Algorithms that
determine how learning rates should change throughout the training process are
called learning rate schedules.
Finetuning Techniques | 359

36 While it’s commonly acknowledged that small batch sizes lead to unstable training, I wasn’t able to find good
explanations for why that’s the case. If you have references about this, please feel free to send them my way.
37 I tried to find the first paper where gradient accumulation was introduced but couldn’t. Its use in deep learn‐
ing was mentioned as early as 2016 in “Ako: Decentralised Deep Learning with Partial Gradient Exchange”
(Watcharapichat et al., Proceedings of the Seventh ACM Symposium on Cloud Computing, 2016). The concept
seems to come from distributed training, where gradients computed on different machines need to be accu‐
mulated and used to update the model’s weights.
Batch size.    The batch size determines how many examples a model learns from in
each step to update its weights. A batch size that is too small, such as fewer than
eight, can lead to unstable training. 36 A larger batch size helps aggregate the signals
from different examples, resulting in more stable and reliable updates.
In general, the larger the batch size, the faster the model can go through training
examples. However, the larger the batch size, the more memory is needed to run your
model. Thus, batch size is limited by the hardware you use.
This is where you see the cost versus efficiency trade-off. More expensive compute
allows faster finetuning.
As of this writing, compute is still a bottleneck for finetuning. Often, models are so
large, and memory is so constrained, that only small batch sizes can be used. This can
lead to unstable model weight updates. To address this, instead of updating the
model weights after each batch, you can accumulate gradients across several batches
and update the model weights once enough reliable gradients are accumulated. This
technique is called gradient accumulation.37
When compute cost isn’t the most important factor, you can experiment with differ‐
ent batch sizes to see which gives the best model performance.
Number of epochs.    An epoch is a pass over the training data. The number of epochs
determines how many times each training example is trained on.
Small datasets may need more epochs than large datasets. For a dataset with millions
of examples, 1–2 epochs might be sufficient. A dataset with thousands of examples
might still see performance improvement after 4–10 epochs.
The difference between the training loss and the validation loss can give you hints
about epochs. If both the training loss and the validation loss still steadily decrease,
the model can benefit from more epochs (and more data). If the training loss still
decreases but the validation loss increases, the model is overfitting to the training
data, and you might try lowering the number of epochs.
360 | Chapter 7: Finetuning
