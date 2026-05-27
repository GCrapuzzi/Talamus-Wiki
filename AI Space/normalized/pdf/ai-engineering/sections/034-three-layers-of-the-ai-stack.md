---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 034
section-title: Three Layers of the AI Stack
source-location: pages 61-62
previous-section: AI Space/normalized/pdf/ai-engineering/sections/033-the-ai-engineering-stack.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/035-ai-engineering-versus-ml-engineering.md
classification: reusable-knowledge-candidate
---
# Three Layers of the AI Stack

Figure 1-13. Some companies have separate job descriptions for AI engineering, as
shown in the job headlines on LinkedIn from December 17, 2023.
Three Layers of the AI Stack
There are three layers to any AI application stack: application development, model
development, and infrastructure. When developing an AI application, you’ll likely
start from the top layer and move down as needed:
Application development
With models readily available, anyone can use them to develop applications. This
is the layer that has seen the most action in the last two years, and it is still rap‐
idly evolving. Application development involves providing a model with good
prompts and necessary context. This layer requires rigorous evaluation. Good
applications also demand good interfaces.
Model development
This layer provides tooling for developing models, including frameworks for
modeling, training, finetuning, and inference optimization. Because data is cen‐
tral to model development, this layer also contains dataset engineering. Model
development also requires rigorous evaluation.
Infrastructure
At the bottom is the stack is infrastructure, which includes tooling for model
serving, managing data and compute, and monitoring.
The AI Engineering Stack | 37

[Visual content extracted via GLM-OCR]

Three Layers of the AI Stack

There are three layers to any AI application stack: application development, model development, and infrastructure. When developing an AI application, you’ll likely start from the top layer and move down as needed:

Application development
With models readily available, anyone can use them to develop applications. This is the layer that has seen the most action in the last two years, and it is still rapidly evolving. Application development involves providing a model with good prompts and necessary context. This layer requires rigorous evaluation. Good applications also demand good interfaces.

Model development
This layer provides tooling for developing models, including frameworks for modeling, training, finetuning, and inference optimization. Because data is central to model development, this layer also contains dataset engineering. Model development also requires rigorous evaluation.

Infrastructure
At the bottom is the stack is infrastructure, which includes tooling for model serving, managing data and compute, and monitoring.

These three layers and examples of responsibilities for each layer are shown in
Figure 1-14.
Figure 1-14. Three layers of the AI engineering stack.
To get a sense of how the landscape has evolved with foundation models, in March
2024, I searched GitHub for all AI-related repositories with at least 500 stars. Given
the prevalence of GitHub, I believe this data is a good proxy for understanding the
ecosystem. In my analysis, I also included repositories for applications and models,
which are the products of the application development and model development lay‐
ers, respectively. I found a total of 920 repositories. Figure 1-15 shows the cumulative
number of repositories in each category month-over-month.
Figure 1-15. Cumulative count of repositories by category over time.
38 | Chapter 1: Introduction to Building AI Applications with Foundation Models

[Visual content extracted via GLM-OCR]

These three layers and examples of responsibilities for each layer are shown in Figure 1-14.

Figure 1-14. Three layers of the AI engineering stack.

To get a sense of how the landscape has evolved with foundation models, in March 2024, I searched GitHub for all AI-related repositories with at least 500 stars. Given the prevalence of GitHub, I believe this data is a good proxy for understanding the ecosystem. In my analysis, I also included repositories for applications and models, which are the products of the application development and model development layers, respectively. I found a total of 920 repositories. Figure 1-15 shows the cumulative number of repositories in each category month-over-month.

Figure 1-15. Cumulative count of repositories by category over time.
