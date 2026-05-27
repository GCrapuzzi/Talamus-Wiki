---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 064
section-title: Functional Correctness
source-location: pages 150-150
previous-section: AI Space/normalized/pdf/ai-engineering/sections/063-exact-evaluation.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
classification: reusable-knowledge-candidate
---
# Functional Correctness

Functional Correctness
Functional correctness evaluation means evaluating a system based on whether it
performs the intended functionality. For example, if you ask a model to create a web‐
site, does the generated website meet your requirements? If you ask a model to make
a reservation at a certain restaurant, does the model succeed?
Functional correctness is the ultimate metric for evaluating the performance of any
application, as it measures whether your application does what it’s intended to do.
However, functional correctness isn’t always straightforward to measure, and its
measurement can’t be easily automated.
Code generation is an example of a task where functional correctness measurement
can be automated. Functional correctness in coding is sometimes execution accuracy.
Say you ask the model to write a Python function, gcd(num1, num2) , to find the
greatest common denominator (gcd) of two numbers, num1 and num2. The gener‐
ated code can then be input into a Python interpreter to check whether the code is
valid and if it is, whether it outputs the correct result of a given pair (num1, num2).
For example, given the pair (num1=15, num2=20) , if the function gcd(15, 20)
doesn’t return 5, the correct answer, you know that the function is wrong.
Long before AI was used for writing code, automatically verifying code’s functional
correctness was standard practice in software engineering. Code is typically validated
with unit tests where code is executed in different scenarios to ensure that it gener‐
ates the expected outputs. Functional correctness evaluation is how coding platforms
like LeetCode and HackerRank validate the submitted solutions.
Popular benchmarks for evaluating AI’s code generation capabilities, such as
OpenAI’s HumanEval  and Google’s MBPP  (Mostly Basic Python Problems Dataset)
use functional correctness as their metrics. Benchmarks for text-to-SQL (generating
SQL queries from natural languages) like Spider ( Yu et al., 2018 ), BIRD-SQL (Big
Bench for Large-scale Database Grounded Text-to-SQL Evaluation) ( Li et al., 2023 ),
and WikiSQL (Zhong, et al., 2017) also rely on functional correctness.
A benchmark problem comes with a set of test cases. Each test case consists of a sce‐
nario the code should run and the expected output for that scenario. Here’s an exam‐
ple of a problem and its test cases in HumanEval:
Problem
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
      """ Check if in given list of numbers, are any two numbers closer to each
      other than given threshold.
      >>> has_close_elements([1.0, 2.0, 3.0], 0.5) False
      >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) True
      """
126 | Chapter 3: Evaluation Methodology
