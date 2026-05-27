---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 033
section-title: The AI Engineering Stack
source-location: pages 59-60
previous-section: AI Space/normalized/pdf/ai-engineering/sections/032-maintenance.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/034-three-layers-of-the-ai-stack.md
classification: reusable-knowledge-candidate
---
# The AI Engineering Stack

However, even these good changes can cause friction in your workflows. You’ll have
to constantly be on your guard and run a cost-benefit analysis of each technology
investment. The best option today might turn into the worst option tomorrow. You
may decide to build a model in-house because it seems cheaper than paying for
model providers, only to find out after three months that model providers have
dropped their prices in half, making in-house the expensive option. You might invest
in a third-party solution and tailor your infrastructure around it, only for the pro‐
vider to go out of business after failing to secure funding.
Some changes are easier to adapt to. For example, as model providers converge to the
same API, it’s becoming easier to swap one model API for another. However, as each
model has its quirks, strengths, and weaknesses, developers working with the new
model will need to adjust their workflows, prompts, and data to this new model.
Without proper infrastructure for versioning and evaluation in place, the process can
cause a lot of headaches.
Some changes are harder to adapt to, especially those around regulations. Technolo‐
gies surrounding AI are considered national security issues for many countries,
meaning resources for AI, including compute, talent, and data, are heavily regulated.
The introduction of Europe’s General Data Protection Regulation (GDPR), for exam‐
ple, was estimated to cost businesses $9 billion to become compliant. Compute avail‐
ability can change overnight as new laws put more restrictions on who can buy and
sell compute resources (see the US October 2023 Executive Order). If your GPU ven‐
dor is suddenly banned from selling GPUs to your country, you’re in trouble.
Some changes can even be fatal. For example, regulations around intellectual prop‐
erty (IP) and AI usage are still evolving. If you build your product on top of a model
trained using other people’s data, can you be certain that your product’s IP will
always belong to you? Many IP-heavy companies I’ve talked to, such as game studios,
hesitate to use AI for fear of losing their IPs later on.
Once you’ve committed to building an AI product, let’s look into the engineering
stack needed to build these applications.
The AI Engineering Stack
AI engineering’s rapid growth also induced an incredible amount of hype and FOMO
(fear of missing out). The number of new tools, techniques, models, and applications
introduced every day can be overwhelming. Instead of trying to keep up with the
constantly shifting sand, let’s look into the fundamental building blocks of AI
engineering.
The AI Engineering Stack | 35

To understand AI engineering, it’s important to recognize that AI engineering
evolved out of ML engineering. When a company starts experimenting with founda‐
tion models, it’s natural that its existing ML team should lead the effort. Some com‐
panies treat AI engineering the same as ML engineering, as shown in Figure 1-12.
Figure 1-12. Many companies put AI engineering and ML engineering under the same
umbrella, as shown in the job headlines on LinkedIn from December 17, 2023.
Some companies have separate job descriptions for AI engineering, as shown in
Figure 1-13.
Regardless of where organizations position AI engineers and ML engineers, their
roles have significant overlap. Existing ML engineers can add AI engineering to their
lists of skills to expand their job prospects. However, there are also AI engineers with
no previous ML experience.
To best understand AI engineering and how it differs from traditional ML engineer‐
ing, the following section breaks down different layers of the AI application building
process and looks at the role each layer plays in AI engineering and ML engineering.
36 | Chapter 1: Introduction to Building AI Applications with Foundation Models

[Visual content extracted via GLM-OCR]

To understand AI engineering, it’s important to recognize that AI engineering evolved out of ML engineering. When a company starts experimenting with foundation models, it’s natural that its existing ML team should lead the effort. Some companies treat AI engineering the same as ML engineering, as shown in Figure 1-12.

Figure 1-12. Many companies put AI engineering and ML engineering under the same umbrella, as shown in the job headlines on LinkedIn from December 17, 2023.

Some companies have separate job descriptions for AI engineering, as shown in Figure 1-13.

Regardless of where organizations position AI engineers and ML engineers, their roles have significant overlap. Existing ML engineers can add AI engineering to their lists of skills to expand their job prospects. However, there are also AI engineers with no previous ML experience.

To best understand AI engineering and how it differs from traditional ML engineering, the following section breaks down different layers of the AI application building process and looks at the role each layer plays in AI engineering and ML engineering.
