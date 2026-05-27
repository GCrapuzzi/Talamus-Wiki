---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 153
section-title: Clean and Filter Data
source-location: pages 425-425
previous-section: AI Space/normalized/pdf/ai-engineering/sections/152-deduplicate-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/154-format-data.md
classification: reusable-knowledge-candidate
---
# Clean and Filter Data

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
