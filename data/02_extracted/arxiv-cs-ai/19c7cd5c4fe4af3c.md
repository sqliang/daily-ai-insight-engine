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
pipeline_stage: fact_extracted
id: 19c7cd5c4fe4af3c
manifest_dates:
- '2026-07-07'
source_type: academic_paper
tldr: 该论文提出 ASK+ 方法，通过为小语言模型提供轨迹感知上下文（部分地图、位置和动作历史）和结构化思维链推理，解决了在部分可观测环境下 SLM 几乎从不主动干预策略的问题。在
  DoorKey 任务上，ASK+ 成功率从 89% 提升至 93%；在 FourRooms 上从 53% 提升至 70%。
objective_summary: 该研究针对部分可观测环境下的强化学习问题，提出了一种基于不确定性门控的小语言模型辅助方法 ASK+。研究人员发现，原始的 ASK
  方法因缺少上下文而导致小语言模型几乎从不主动改写策略。ASK+ 通过提供轨迹感知上下文（部分地图、已访问位置和动作历史）并引入结构化思维链推理，将小语言模型从被动的冗余检查转变为信息丰富的咨询者。实验表明，ASK+
  在 DoorKey 任务上达到 93% 的成功率，在 FourRooms 上达到 70%，在 HigherLower 上达到 73.7%。研究还确认，预测熵信号在部分可观测马尔可夫决策过程中仍然有效，且
  Qwen3.5-2B 的表现匹配或超过 Qwen3.5-4B，证明提示工程和选择性门控比模型规模的影响更大。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Alibaba
  technologies:
  - SLM
  - PPO
  - POMDP
  - LLM
  - RL
  - ASK+
  - Chain-of-Thought
  key_people: []
key_logic_flow:
- 在部分可观测环境下，强化学习代理必须基于不完整信息行动，自然适合从小语言模型获取引导。
- 原始的 ASK 方法因使用过于简化的自我中心提示，未能提供足够上下文，导致小语言模型在所有测试环境中几乎从不主动改写策略。
- 研究人员将此失败归因为上下文问题而非模型能力问题，并提出了 ASK+ 方法。
- ASK+ 向小语言模型提供轨迹感知上下文（部分地图、已访问位置和动作历史）和结构化思维链推理，使其能有效纠正策略。
- 实验证明，预测熵信号在部分可观测马尔可夫决策过程中仍然有效，不确定性门控辅助不仅在完全可观测环境下可行。
- Qwen3.5-2B 在所有环境中匹配或超过 Qwen3.5-4B 的表现，说明提示设计和选择性门控对效果的影响超过模型规模。
specialized_tags:
  paper:
    paperTitle: 'ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: RL
    methodType: RL-based
extract_result: success
object_mentions:
- object_type: paper
  name: 'ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability'
  canonical_name: 'ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial
    Observability'
  url: https://arxiv.org/abs/2607.02686
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出 ASK+ 方法，通过提供轨迹感知上下文和结构化思维链推理，将小语言模型从被动冗余检查转变为信息丰富的咨询者。
  - 实验结果表明 ASK+ 在 DoorKey 上达到 93% 成功率，在 FourRooms 上达到 70%，在 HigherLower 上达到 73.7%。
  article_id: 19c7cd5c4fe4af3c
- object_type: model
  name: Qwen3.5-2B
  canonical_name: Qwen3.5-2B
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Qwen3.5-2B 在所有测试环境中匹配或超过 Qwen3.5-4B 的表现，证明提示设计和选择性门控比模型规模的影响更大。
  article_id: 19c7cd5c4fe4af3c
- object_type: model
  name: Qwen3.5-4B
  canonical_name: Qwen3.5-4B
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Qwen3.5-4B 作为对比基准模型，被用于验证模型规模对 ASK+ 方法效果的影响。
  article_id: 19c7cd5c4fe4af3c
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