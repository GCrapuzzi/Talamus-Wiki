---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 154
section-title: Format Data
source-location: pages 425-426
previous-section: AI Space/normalized/pdf/ai-engineering/sections/153-clean-and-filter-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/155-summary.md
classification: reusable-knowledge-candidate
---
# Format Data

Clean and Filter Data
Data needs to be cleaned to make your model performant and safe.
First, you might want to remove extraneous formatting tokens. Since many public
datasets are scraped from the internet, extraneous HTML tags are quite common.
Unless you want to train your model on HMTL tags, remove them. Databricks found
that removing extraneous Markdown and HTML tokens improved their model’s
accuracy by 20% while reducing their input token lengths by 60%.
You need to clean your data of anything that isn’t compliant with your policies, such
as PII, sensitive data, copyrighted data, or data that is considered toxic. Techniques
discussed in Chapter 4 can help. Remove all the fields that you’re not allowed to use,
such as zip code, name, and gender.
You also might want to remove low-quality data, using techniques discussed in “Data
verification” on page 391  to detect low-quality data.
Manual inspection of data is especially important in this step. Staring at data might
help you notice patterns that you can use as heuristics to detect low-quality data.
Heuristics to detect low-quality data might be non-obvious. For example, Kern et al.
(2024) found that annotations made in the second half of an annotation session are of
lower quality, likely due to annotator boredom or fatigue.
If there is more data than you need or can afford to use (e.g., due to your compute
budget), you can further filter your data. For example, you can use active learning
techniques to select examples that are the most helpful for your model to learn from.
You can also use importance sampling to find examples that are most important to
your task. Their efficiencies depend on whether you have a good way to evaluate the
importance of each training example. Meta researchers, in their paper on data prun‐
ing (Sorscher et al., 2022), concluded that the discovery of good data-pruning metrics
can significantly reduce the resource costs of modern deep learning.
Format Data
Once you’ve deduplicated and cleaned your data, you need to get it into the right for‐
mat expected by the model you’re finetuning. Each model uses a specific tokenizer
and expects data in a specific chat template, as discussed in Chapter 5. Getting data
into the wrong chat template can cause strange bugs in your model.
If you’re doing supervised finetuning, your data is most likely in the format (instruc‐
tion, response). Instructions can be further decomposed into (system prompt, user
prompt). If you’ve graduated to finetuning from prompt engineering, the
instructions used for finetuning might be different from the instructions used during
prompt engineering. During finetuning, instructions typically don’t need task
Data Processing | 401

descriptions or examples. If you have sufficient training examples, the model can
learn the expected behavior of the task from the examples directly.
As an example, imagine that you’ve been using this three-shot instruction for your
food classification task with a base model:
Label the following item as either edible or inedible.
Item: burger
Label: edible
Item: car
Label: inedible
Item: mushroom
Label: edible
Item: {INPUT}
Label:
For finetuning, all the examples included in the 3-shot prompt can be converted into
training examples. The training data for finetuning will look like Table 8-4.
Table 8-4. Example training data used for a food classification task.
Example ID Input Output
1 burger --> edible
2 car --> inedible
3 mushroom --> edible
… … …
Once the model is finetuned, you can use a prompt as simple as:
  {INPUT} -->
This is much shorter than the prompt used with the base model. Therefore, if you’re
worried about the input tokens of your instructions, finetuning can be one way to
help manage the cost.
Different finetuning data formats can impact your finetuned model’s performance.
Experiments to determine the best format for you can be helpful.
When you use the finetuned model, make sure that the prompts you use match the
format of the finetuning data. For example, if the training data uses the prompt in the
format “burger -->”, any of the following prompts can cause issues:
402 | Chapter 8: Dataset Engineering
