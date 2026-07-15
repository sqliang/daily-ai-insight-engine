---
title: 'ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability'
source: https://arxiv.org/abs/2607.02686
author:
- '[[Juarez Monteiro, Nathan Gavenski, Guilherme Lima, Francisco Galuppo, Odinaldo
  Rodrigues, Adriano Veloso]]'
published: '2026-07-07'
created: '2026-07-07'
description: 'arXiv:2607.02686v1 Announce Type: new Abstract: Reinforcement learning
  agents operating under partial observability must act on incomplete information,
  making them natural candidates for guidance from small language models (SLMs) that
  carry broad reasoning priors. Yet integrating SLM guidance into this setting has
  proven difficult: across all test environments, vanilla uncertainty-gated approaches
  achieve an overwrite rate at or near zero, meaning the SLM almost never contributes
  an independent action. We trace this failure to the bare egocentric prompt, which
  provides insufficient context for genuine reasoning, and identify it as a context
  problem rather than a capacity problem. We propose ASK+, which supplies the SLM
  with trajectory-aware context (a partially revealed map, visited positions, and
  action history) and structured chain-of-thought reasoning, converting it from a
  passive redundancy check into a more informative consultant that occasionally corrects
  the policy. We further establish that the predictive entropy signal used for selective
  querying measures action uncertainty rather than state uncertainty and remains informative
  in POMDPs, making uncertainty-gated assistance viable beyond fully observable settings.
  The stateful prompt drives substantial gains: on DoorKey, where vanilla ASK matches
  PPO (both 89%), ASK+ reaches 93% success; on FourRooms, success climbs from 53%
  to 70%; on HigherLower, accuracy reaches 73.7%, matching the SLM-only upper bound.
  Across all environments, Qwen3.5-2B matches or exceeds Qwen3.5-4B, confirming that
  prompt design and selective gating dominate the impact of model scale, enabling
  guidance without large models.'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 19c7cd5c4fe4af3c
manifest_dates:
- '2026-07-07'
---

# Computer Science > Artificial Intelligence

# Title:ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability

View PDF HTML (experimental)Abstract:Reinforcement learning agents operating under partial observability must act on incomplete information, making them natural candidates for guidance from small language models (SLMs) that carry broad reasoning priors. Yet integrating SLM guidance into this setting has proven difficult: across all test environments, vanilla uncertainty-gated approaches achieve an overwrite rate at or near zero, meaning the SLM almost never contributes an independent action. We trace this failure to the bare egocentric prompt, which provides insufficient context for genuine reasoning, and identify it as a context problem rather than a capacity problem. We propose ASK+, which supplies the SLM with trajectory-aware context (a partially revealed map, visited positions, and action history) and structured chain-of-thought reasoning, converting it from a passive redundancy check into a more informative consultant that occasionally corrects the policy. We further establish that the predictive entropy signal used for selective querying measures action uncertainty rather than state uncertainty and remains informative in POMDPs, making uncertainty-gated assistance viable beyond fully observable settings. The stateful prompt drives substantial gains: on DoorKey, where vanilla ASK matches PPO (both 89%), ASK+ reaches 93% success; on FourRooms, success climbs from 53% to 70%; on HigherLower, accuracy reaches 73.7%, matching the SLM-only upper bound. Across all environments, Qwen3.5-2B matches or exceeds Qwen3.5-4B, confirming that prompt design and selective gating dominate the impact of model scale, enabling guidance without large models.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.