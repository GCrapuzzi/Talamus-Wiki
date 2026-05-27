---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 041
section-title: Domain-Specific Models
source-location: pages 80-81
previous-section: AI Space/normalized/pdf/ai-engineering/sections/040-multilingual-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/042-modeling.md
classification: reusable-knowledge-candidate
---
# Domain-Specific Models

3 “Inside the Secret List of Websites That Make AI like ChatGPT Sound Smart” , Washington Post, 2023.
4 For texts, you can use domain keywords as heuristics, but there are no obvious heuristics for images. Most
analyses I could find about vision datasets are about image sizes, resolutions, or video lengths.
Domain-Specific Models
General-purpose models like Gemini, GPTs, and Llamas can perform incredibly well
on a wide range of domains, including but not limited to coding, law, science, busi‐
ness, sports, and environmental science. This is largely thanks to the inclusion of
these domains in their training data. Figure 2-3  shows the distribution of domains
present in Common Crawl according to the Washington Post’s 2023 analysis. 3
Figure 2-3. Distribution of domains in the C4 dataset. Reproduced from the statistics
from the Washington Post. One caveat of this analysis is that it only shows the cate‐
gories that are included, not the categories missing.
As of this writing, there haven’t been many analyses of domain distribution in vision
data. This might be because images are harder to categorize than texts.4 However, you
can infer a model’s domains from its benchmark performance. Table 2-3 shows how
two models, CLIP and Open CLIP, perform on different benchmarks . These bench‐
marks show how well these two models do on birds, flowers, cars, and a few more
categories, but the world is so much bigger and more complex than these few
categories.
56 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Domain-Specific Models

General-purpose models like Gemini, GPTs, and Llamas can perform incredibly well on a wide range of domains, including but not limited to coding, law, science, business, sports, and environmental science. This is largely thanks to the inclusion of these domains in their training data. Figure 2-3 shows the distribution of domains present in Common Crawl according to the Washington Post’s 2023 analysis.

Figure 2-3. Distribution of domains in the C4 dataset. Reproduced from the statistics from the Washington Post. One caveat of this analysis is that it only shows the categories that are included, not the categories missing.

As of this writing, there haven’t been many analyses of domain distribution in vision data. This might be because images are harder to categorize than texts. However, you can infer a model’s domains from its benchmark performance. Table 2-3 shows how two models, CLIP and Open CLIP, perform on different benchmarks. These benchmarks show how well these two models do on birds, flowers, cars, and a few more categories, but the world is so much bigger and more complex than these few categories.

3 “Inside the Secret List of Websites That Make AI like ChatGPT Sound Smart”, Washington Post, 2023.

4 For texts, you can use domain keywords as heuristics, but there are no obvious heuristics for images. Most analyses I could find about vision datasets are about image sizes, resolutions, or video lengths.

Table 2-3. Open CLIP and CLIP’s performance on different image datasets.
Dataset CLIP
Accuracy of ViT-B/32 (OpenAI)
Open CLIP
Accuracy of ViT-B/32 (Cade)
ImageNet 63.2 62.9
ImageNet v2 – 62.6
Birdsnap 37.8 46.0
Country211 17.8 14.8
Oxford 102 Category Flower 66.7 66.0
German Traffic Sign Recognition Benchmark 32.2 42.0
Stanford Cars 59.4 79.3
UCF101 64.5 63.1
Even though general-purpose foundation models can answer everyday questions
about different domains, they are unlikely to perform well on domain-specific tasks,
especially if they never saw these tasks during training. Two examples of domainspecific tasks are drug discovery and cancer screening. Drug discovery involves pro‐
tein, DNA, and RNA data, which follow specific formats and are expensive to
acquire. This data is unlikely to be found in publicly available internet data. Similarly,
cancer screening typically involves X-ray and fMRI (functional magnetic resonance
imaging) scans, which are hard to obtain due to privacy.
To train a model to perform well on these domain-specific tasks, you might need to
curate very specific datasets. One of the most famous domain-specific models is per‐
haps DeepMind’s AlphaFold , trained on the sequences and 3D structures of around
100,000 known proteins. NVIDIA’s BioNeMo  is another model that focuses on bio‐
molecular data for drug discovery. Google’s Med-PaLM2  combined the power of an
LLM with medical data to answer medical queries with higher accuracy.
Domain-specific models are especially common for biomedicine,
but other fields can benefit from domain-specific models too. It’s
possible that a model trained on architectural sketches can help
architects much better than Stable Diffusion, or a model trained on
factory plans can be optimized for manufacturing processes much
better than a generic model like ChatGPT.
This section gave a high-level overview of how training data impacts a model’s per‐
formance. Next, let’s explore the impact of how a model is designed on its
performance.
Training Data | 57

[Visual content extracted via GLM-OCR]

Even though general-purpose foundation models can answer everyday questions about different domains, they are unlikely to perform well on domain-specific tasks, especially if they never saw these tasks during training. Two examples of domain-specific tasks are drug discovery and cancer screening. Drug discovery involves protein, DNA, and RNA data, which follow specific formats and are expensive to acquire. This data is unlikely to be found in publicly available internet data. Similarly, cancer screening typically involves X-ray and fMRI (functional magnetic resonance imaging) scans, which are hard to obtain due to privacy.

To train a model to perform well on these domain-specific tasks, you might need to curate very specific datasets. One of the most famous domain-specific models is perhaps DeepMind’s AlphaFold, trained on the sequences and 3D structures of around 100,000 known proteins. NVIDIA’s BioNeMo is another model that focuses on biomolecular data for drug discovery. Google’s Med-PaLM2 combined the power of an LLM with medical data to answer medical queries with higher accuracy.

Domain-specific models are especially common for biomedicine, but other fields can benefit from domain-specific models too. It’s possible that a model trained on architectural sketches can help architects much better than Stable Diffusion, or a model trained on factory plans can be optimized for manufacturing processes much better than a generic model like ChatGPT.

This section gave a high-level overview of how training data impacts a model’s performance. Next, let’s explore the impact of how a model is designed on its performance.
