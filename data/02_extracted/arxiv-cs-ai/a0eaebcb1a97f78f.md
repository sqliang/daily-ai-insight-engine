---
title: 'PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection'
source: https://arxiv.org/abs/2607.16199
author:
- '[[Yuhang Wang]]'
published: '2026-07-21'
created: '2026-07-21'
manifest_dates:
- '2026-07-21'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a0eaebcb1a97f78f
source_type: academic_paper
tldr: PlanFlip 提出了四种针对多智能体 LLM 系统规划阶段的提示注入攻击方法。实验发现 GPT-5 的攻击成功率最高（0.68），推翻"更强模型更安全"的假设，异构模型多样性才是多智能体系统安全的前提条件。
objective_summary: arXiv 论文 PlanFlip 识别了多智能体 LLM 系统中 Planner 作为关键攻击面，提出四种规划阶段提示注入攻击：GoalSubstitution
  (PF-1)、PriorityInversion (PF-2)、ContextPollution (PF-3) 和 RoleConfusion (PF-4)，每种均伪装成工具输出以绕过关键词过滤。在
  9 个前沿模型、3479 个 episode 的评估中发现：GPT-5 攻击成功率最高（0.68），同质化流水线存在相关智能体盲区，而推理增强模型 DeepSeek-R1
  对所有攻击的 StepShift 均为 0.00。论文提出 GoalAnchorCheck (D1) 和 CrossAgentConsensus (D2) 两种防御机制，检测率最高达
  1.00。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Meta
  - DeepSeek
  technologies:
  - PlanFlip
  - Multi-Agent LLM Systems
  - Prompt Injection
  - GoalSubstitution (PF-1)
  - PriorityInversion (PF-2)
  - ContextPollution (PF-3)
  - RoleConfusion (PF-4)
  - GoalAnchorCheck (D1)
  - CrossAgentConsensus (D2)
  - StepShift
  key_people: []
key_logic_flow:
- 多智能体 LLM 系统依赖 Planner 将目标分解为子任务序列，再由 Executor 和 Critic 执行与审计，规划阶段因此成为关键攻击面。
- PlanFlip 框架提出了四种伪装成工具输出的规划阶段提示注入攻击方法，可有效绕过关键词过滤器并污染所有下游子任务。
- 在 9 个前沿模型、3479 个 episode 的实验中，GPT-5 的攻击成功率最高（0.68），表明更强的模型反而更容易受到规划阶段注入攻击。
- 同质化流水线存在相关智能体盲区：GPT-4o 和 Llama-3.3-70B 的攻击成功率接近 0，但攻击成功重构了计划流程而相同骨干网络的 Critic 仍报告一致。
- 推理增强模型 DeepSeek-R1 在所有攻击下的 StepShift 均为 0.00，表现出对规划阶段提示注入的完全抵抗能力。
- 异构模型多样性是多智能体系统的安全前提条件，同质化骨干网络的冗余无法提供对规划阶段攻击的有效防护。
object_mentions:
- object_type: paper
  name: 'PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection'
  canonical_name: PlanFlip
  url: https://arxiv.org/abs/2607.16199
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - PlanFlip 框架提出了四种规划阶段提示注入攻击方法：GoalSubstitution、PriorityInversion、ContextPollution
    和 RoleConfusion，每种都伪装成工具输出以绕过关键词过滤。
  - 在 9 个前沿模型、3479 个 episode 的实验中，GPT-5 的攻击成功率最高，推翻了更强模型更安全的假设。
  - 论文的核心发现是异构模型多样性是多智能体系统安全的前提条件，同质化骨干网络的冗余无法防御规划阶段攻击。
  article_id: a0eaebcb1a97f78f
- object_type: project
  name: GoalAnchorCheck (D1)
  canonical_name: GoalAnchorCheck
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GoalAnchorCheck (D1) 作为防御机制，在 16 个实验单元中的 15 个实现了最高 1.00 的检测率。
  - 该防御方法专门针对规划阶段的提示注入攻击进行检测，性能优于同骨干网络基线方案。
  article_id: a0eaebcb1a97f78f
- object_type: project
  name: CrossAgentConsensus (D2)
  canonical_name: CrossAgentConsensus
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - CrossAgentConsensus (D2) 通过异构智能体之间的共识机制检测规划阶段注入攻击。
  - 该防御在 16 个实验单元中的 15 个优于同骨干网络基线方案，检测率最高达到 1.00。
  article_id: a0eaebcb1a97f78f
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection

View PDF HTML (experimental)Abstract:Multi-agent LLM systems increasingly rely on a Planner to decompose goals into sub-task sequences that downstream Executor and Critic agents execute and audit. We identify the planning phase as a critical attack surface: a single injection into the Planner's context achieves cascade amplification, corrupting all downstream sub-tasks simultaneously. We introduce PlanFlip, a framework comprising four planning-phase prompt injection attacks -- GoalSubstitution (PF-1), PriorityInversion (PF-2), ContextPollution (PF-3), and RoleConfusion (PF-4) -- each disguised as plausible tool outputs to evade keyword filters. Evaluating nine frontier LLMs across 3,479 episodes, we uncover three findings: (1) capability amplifies vulnerability -- GPT-5 achieves the highest attack success rate (ASR = 0.68), contradicting the assumption that stronger models are inherently more secure; (2) homogeneous pipelines exhibit a correlated-agent blind spot -- GPT-4o and Llama-3.3-70B show ASR near 0 yet Stealth = 1.00 and StepShift > 0, with attacks restructuring plans while the same-backbone Critic reports alignment (two independent judges confirm -0.20 to -0.32 semantic deviation, r = 0.943); (3) reasoning-augmented models resist injections -- DeepSeek-R1 achieves StepShift = 0.00 across all attacks. We propose GoalAnchorCheck (D1) and CrossAgentConsensus (D2), achieving detection rates up to 1.00 and outperforming same-backbone baselines in 15 of 16 cells. Our key insight: heterogeneous model diversity is a security prerequisite for multi-agent systems; redundancy within a homogeneous backbone provides no protection against planning-phase attacks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.