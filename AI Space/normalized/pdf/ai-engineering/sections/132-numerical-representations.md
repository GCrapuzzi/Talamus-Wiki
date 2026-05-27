---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 132
section-title: Numerical Representations
source-location: pages 349-351
previous-section: AI Space/normalized/pdf/ai-engineering/sections/131-memory-math.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/133-quantization.md
classification: reusable-knowledge-candidate
---
# Numerical Representations

Figure 7-5. The memory needed for activations can dwarf the memory needed for the
model’s weights. Image from Korthikanti et al., 2022.
Numerical Representations
In the memory calculation so far, I’ve assumed that each value takes up two bytes of
memory. The memory required to represent each value in a model contributes
directly to the model’s overall memory footprint. If you reduce the memory needed
for each value by half, the memory needed for the model’s weights is also reduced by
half.
Before discussing how to reduce the memory needed for each value, it’s useful to
understand numerical representations. Numerical values in neural networks are tra‐
ditionally represented as float numbers. The most common family of floating point
formats is the FP family, which adheres to the Institute of Electrical and Electronics
Engineers (IEEE) standard for Floating-Point Arithmetic (IEEE 754):
• FP32 uses 32 bits (4 bytes) to represent a float. This format is called single
precision.
• FP64 uses 64 bits (8 bytes) and is called double precision.
• FP16 uses 16 bits (2 bytes) and is called half precision.
Memory Bottlenecks | 325

[Visual content extracted via GLM-OCR]

Numerical Representations

In the memory calculation so far, I’ve assumed that each value takes up two bytes of memory. The memory required to represent each value in a model contributes directly to the model’s overall memory footprint. If you reduce the memory needed for each value by half, the memory needed for the model’s weights is also reduced by half.

Before discussing how to reduce the memory needed for each value, it’s useful to understand numerical representations. Numerical values in neural networks are traditionally represented as float numbers. The most common family of floating point formats is the FP family, which adheres to the Institute of Electrical and Electronics Engineers (IEEE) standard for Floating-Point Arithmetic (IEEE 754):

- FP32 uses 32 bits (4 bytes) to represent a float. This format is called single precision.
- FP64 uses 64 bits (8 bytes) and is called double precision.
- FP16 uses 16 bits (2 bytes) and is called half precision.

11 Google introduced BFloat16 as “the secret to high performance on Cloud TPUs” .
12 Integer formats are also called fixed point formats.
13 Range bits are called exponents. Precision bits are called significands.
14 Note that usually the number at the end of a format’s name signifies how many bits it occupies, but TF32
actually has 19 bits, not 32 bits. I believe it was named so to suggest its functional compatibility with FP32.
But honestly, why it’s called TF32 and not TF19 keeps me up at night. An ex-coworker at NVIDIA volun‐
teered his conjecture that people might be skeptical of weird formats (19-bit), so naming this format TF32
makes it look more friendly.
While FP64 is still used in many computations—as of this writing, FP64 is the default
format for NumPy and pandas—it’s rarely used in neural networks because of its
memory footprint. FP32 and FP16 are more common. Other popular floating point
formats in AI workloads include BF16 (BFloat16) and TF32 (TensorFloat-32). BF16
was designed by Google to optimize AI performance on TPUs and TF32 was
designed by NVIDIA for GPUs.11
Numbers can also be represented as integers. Even though not yet as common as
floating formats, integer representations are becoming increasingly popular. Com‐
mon integer formats are INT8 (8-bit integers) and INT4 (4-bit integers).12
Each float format usually has 1 bit to represent the number’s sign, i.e., negative or
positive. The rest of the bits are split between range and precision:13
Range
The number of range bits determines the range of values the format can repre‐
sent. More bits means a wider range. This is similar to how having more digits
lets you represent a wider range of numbers.
Precision
The number of precision bits determines how precisely a number can be repre‐
sented. Reducing the number of precision bits makes a number less precise. For
example, if you convert 10.1234 to a format that can support only two decimal
digits, this value becomes 10.12, which is less precise than the original value.
Figure 7-6 shows different floating point formats along with their range and precision
bits.14
326 | Chapter 7: Finetuning

Figure 7-6. Different numerical formats with their range and precision.

Formats with more bits are considered higher precision. Converting a number with a high-precision format into a low-precision format (e.g., from FP32 to FP16) means reducing its precision. Reducing precision can cause a value to change or result in errors. Table 7-3 shows how FP32 values can be converted into FP16, BF16, and TF32.

Table 7-3. Convert from FP32 values to lower-precision formats. Resultant inaccuracies are in italics.

| FP32 | FP16 | BF16 | TF32 |
| :--- | :--- | :--- | :--- |
| 0.0123456789 | 0.0123443603515625 | 0.0123291 | 0.0123443603515625 |
| 0.123456789 | 0.12347412109375 | 0.123535 | 0.1234130859375 |
| 1.23456789 | 1.234375 | 1.23438 | 1.234375 |
| 12.3456789 | 12.34375 | 12.375 | 12.34375 |
| 123.456789 | 123.4375 | 123.5 | 123.4375 |
| 1234.56789 | 1235.0 | 1232.0 | 1234.0 |
| 12345.6789 | 12344.0 | 12352.0 | 12344.0 |
| 123456.789 | INF | 123392.0 | 123456.0 |
| 1234567.89 | INF | 1236990.0 | 1233920.0 |

a Values out of bound in FP16 are rounded to infinity.

Note in Table 7-3 that even though BF16 and FP16 have the same number of bits, BF16 has more bits for range and fewer bits for precision. This allows BF16 to represent large values that are out-of-bound for FP16. However, this also makes BF16 less precise than FP16. For example, 1234.56789 is 1235.0 in FP16 (0.035% value change) but 1232.0 in BF16 (0.208% value change).
