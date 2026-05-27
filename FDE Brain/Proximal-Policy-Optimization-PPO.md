---
type: method
status: evergreen
aliases:
  - Proximal Policy Optimization (PPO)
  - PPO algorithm
tags:
  - ai-engineering
  - rl
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/047-preference-finetuning.md
    locator: pages 107-111
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - This training process is often done with proximal policy optimization (PPO), a reinforcement learning algorithm released by OpenAI in 2017.
created: 2026-05-26T21:55:45.565444+00:00
updated: 2026-05-26T21:55:45.565444+00:00
ingestion_run: 8d527d59
---

# Proximal Policy Optimization (PPO)

## Summary

A specific and widely used reinforcement learning algorithm designed to update a policy (the LLM) by taking small, controlled steps away from the current policy, ensuring stable and efficient learning.

## Core Idea

PPO is the standard optimization technique used in the final stage of RLHF. It minimizes the risk of the LLM making drastic, destabilizing changes to its behavior while maximizing its reward signal based on the RM.

## Practical Use

After the Reward Model is trained, PPO is applied to the base LLM. The LLM generates responses, the RM scores them, and PPO uses this score to adjust the LLM's weights, making it more likely to generate high-scoring responses in the future.

## Related

- RLHF
- Reinforcement Learning
