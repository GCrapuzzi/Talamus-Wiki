---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 086
section-title: Design Your Evaluation Pipeline
source-location: pages 224-224
previous-section: AI Space/normalized/pdf/ai-engineering/sections/085-navigate-public-benchmarks.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/087-step-1.-evaluate-all-components-in-a-system.md
classification: reusable-knowledge-candidate
---
# Design Your Evaluation Pipeline

To combat data contamination, leaderboard hosts like Hugging Face plot standard
deviations of models’ performance on a given benchmark to spot outliers . Public
benchmarks should keep part of their data private and provide a tool for model
developers to automatically evaluate models against the private hold-out data.
Public benchmarks will help you filter out bad models, but they won’t help you find
the best models for your application. After using public benchmarks to narrow them
to a set of promising models, you’ll need to run your own evaluation pipeline to find
the best one for your application. How to design a custom evaluation pipeline will be
our next topic.
Design Your Evaluation Pipeline
The success of an AI application often hinges on the ability to differentiate good out‐
comes from bad outcomes. To be able to do this, you need an evaluation pipeline that
you can rely upon. With an explosion of evaluation methods and techniques, it can
be confusing to pick the right combination for your evaluation pipeline. This section
focuses on evaluating open-ended tasks. Evaluating close-ended tasks is easier, and its
pipeline can be inferred from this process.
Step 1. Evaluate All Components in a System
Real-world AI applications are complex. Each application might consist of many
components, and a task might be completed after many turns. Evaluation can happen
at different levels: per task, per turn, and per intermediate output.
You should evaluate the end-to-end output and each component’s intermediate out‐
put independently. Consider an application that extracts a person’s current employer
from their resume PDF, which works in two steps:
1. Extract all the text from the PDF.
2. Extract the current employer from the extracted text.
If the model fails to extract the right current employer, it can be because of either
step. If you don’t evaluate each component independently, you don’t know exactly
where your system fails. The first PDF-to-text step can be evaluated using similarity
between the extracted text and the ground truth text. The second step can be evalu‐
ated using accuracy: given the correctly extracted text, how often does the application
correctly extract the current employer?
If applicable, evaluate your application both per turn and per task. A turn can consist
of multiple steps and messages. If a system takes multiple steps to generate an output,
it’s still considered a turn.
200 | Chapter 4: Evaluate AI Systems
