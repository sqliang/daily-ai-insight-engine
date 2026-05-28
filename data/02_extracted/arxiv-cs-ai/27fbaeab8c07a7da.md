---
title: 'Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems'
source: https://arxiv.org/abs/2605.26302
author:
- '[[Jianing Zhu, Yeonju Ro, John Robertson, Kevin Wang, Junbo Li, Haris Vikalo, Aditya
  Akella, Zhangyang Wang]]'
published: '2026-05-27'
created: '2026-05-28'
description: 'arXiv:2605.26302v1 Announce Type: new Abstract: Long-lived AI agents
  are increasingly deployed as persistent operational systems, yet they are still
  evaluated like freshly initialized models. Day-one benchmarks miss a basic systems
  question: how long does an agent remain reliable after deployment? Even when model
  weights are frozen, an agent''s effective state keeps changing as it compresses
  interaction history, retrieves from a growing memory store, revises facts after
  updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan
  property of the full agent harness, not only a snapshot property of the base model.
  We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan
  engineering: measuring not only whether deployed agents degrade, but what form the
  degradation takes and where repair should target. AgingBench organizes agent aging
  into four mechanisms: compression aging, interference aging, revision aging, and
  maintenance aging. To diagnose these failures, AgingBench uses temporal dependency
  graphs and paired counterfactual probes that produce diagnostic profiles for the
  write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios,
  14 models, multiple memory policies, and both runner-controlled and autonomous agents,
  over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional:
  behavioral tests can remain clean while factual precision decays; derived-state
  tracking can collapse sharply within a single model; and the same wrong answer can
  require different repairs depending on what the diagnostic profile points to. These
  results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level
  diagnosis, and stage-targeted repair, not only stronger day-one models.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 27fbaeab8c07a7da
source_type: academic_paper
tldr: 提出 AgingBench 基准，揭示部署后的 AI Agent 即使模型权重冻结也会随时间退化，需用生命周期工程而非一次性评测来保障可靠性。
objective_summary: 研究者于 2026 年发布论文，提出 AgingBench 纵向可靠性基准，将 Agent 老化归为压缩老化、干扰老化、修订老化和维护老化四种机制，通过时序依赖图和反事实探针对
  7 个场景、14 个模型进行约 400 次运行，发现行为测试可能保持清洁而事实精度已衰退，同一错误答案需不同修复策略。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - AgingBench
  - temporal dependency graphs
  - counterfactual probes
  - memory pipeline
  key_people: []
key_logic_flow:
- 当前 Agent 评测体系依赖初始化时的快照测试，忽略部署后随时间持续运行的可靠性问题，即使模型权重冻结，Agent 的有效状态仍会因交互历史压缩、记忆库增长、事实修订和日常维护而变化。
- 提出 AgingBench 纵向可靠性基准，将 Agent 老化归纳为四种机制：压缩老化（compression aging）、干扰老化（interference
  aging）、修订老化（revision aging）和维护老化（maintenance aging）。
- 为诊断老化故障，AgingBench 使用时序依赖图和配对反事实探针，生成针对记忆管道写入、检索和利用三个阶段的诊断画像。
- 实验覆盖 7 个场景、14 个模型、多种记忆策略以及受控和自主两类 Agent，约 400 次运行跨越 8 至 200 个会话，结果表明 Agent 老化不是单维度的。
- 核心发现：行为测试可能保持清洁而事实精度已衰退，派生状态跟踪可在单一模型内急剧崩溃，且同一错误答案根据诊断画像指向的不同需要不同的修复策略。
- 结论：可靠的 Agent 部署需要生命周期评测、机制级诊断和阶段定向修复，而非仅依赖更强的初始模型。
---

# Computer Science > Artificial Intelligence

# Title:Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems

View PDF HTML (experimental)Abstract:Long-lived AI agents are increasingly deployed as persistent operational systems, yet they are still evaluated like freshly initialized models. Day-one benchmarks miss a basic systems question: how long does an agent remain reliable after deployment? Even when model weights are frozen, an agent's effective state keeps changing as it compresses interaction history, retrieves from a growing memory store, revises facts after updates, and undergoes routine maintenance. Reliability therefore becomes a lifespan property of the full agent harness, not only a snapshot property of the base model. We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan engineering: measuring not only whether deployed agents degrade, but what form the degradation takes and where repair should target. AgingBench organizes agent aging into four mechanisms: compression aging, interference aging, revision aging, and maintenance aging. To diagnose these failures, AgingBench uses temporal dependency graphs and paired counterfactual probes that produce diagnostic profiles for the write, retrieval, and utilization stages of the memory pipeline. Across 7 scenarios, 14 models, multiple memory policies, and both runner-controlled and autonomous agents, over ~400 runs spanning 8 - 200 sessions show that agent aging is not one-dimensional: behavioral tests can remain clean while factual precision decays; derived-state tracking can collapse sharply within a single model; and the same wrong answer can require different repairs depending on what the diagnostic profile points to. These results suggest that reliable agent deployment requires lifespan evaluation, mechanism-level diagnosis, and stage-targeted repair, not only stronger day-one models.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.