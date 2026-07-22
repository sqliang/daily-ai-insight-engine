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
tldr: 该论文提出 AgingBench，一个用于评估已部署 AI 代理长期可靠性的纵向基准，识别了压缩老化、干扰老化、修订老化和维护老化四种机制，并通过约 400
  次实验发现代理老化是多维的，需要全生命周期评估而非仅依赖初始模型性能。
objective_summary: 研究者在一篇 arXiv 论文中提出了 AgingBench，这是一个用于衡量已部署 AI 代理长期可靠性的纵向基准，而非仅评估初始化时的模型性能。该基准将代理老化分为压缩老化、干扰老化、修订老化和维护老化四种机制，并使用时间依赖图和配对反事实探针诊断记忆管道的写入、检索和利用阶段故障。在
  7 个场景、14 个模型、多种记忆策略下进行的约 400 次实验表明，行为测试可能保持正常而事实精度已下降，不同老化模式需要不同的针对性修复。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - AgingBench
  - Agent Lifespan Engineering
  - Temporal Dependency Graphs
  - Counterfactual Probes
  key_people: []
key_logic_flow:
- 该论文指出长期部署的 AI 代理在模型权重冻结后，其有效状态仍会因交互历史压缩、记忆库增长、事实修订和日常维护而持续变化。
- 论文提出了 AgingBench 纵向可靠性基准，将代理老化机制分为压缩老化、干扰老化、修订老化和维护老化四类。
- AgingBench 使用时间依赖图和配对反事实探针来诊断记忆管道的写入、检索和利用阶段的具体故障并生成诊断画像。
- 在 7 个场景、14 个模型、多种记忆策略下进行的约 400 次实验覆盖了 8 到 200 个会话周期，横跨 runner 控制和自主代理两种类型。
- 实验表明代理老化并非一维：行为测试可能仍然正常而事实精度已经下降，衍生状态追踪可能在单个模型内急剧崩溃。
- 可靠的代理部署需要全生命周期评估、机制级别的诊断和分阶段针对性修复，而非仅依赖于更强的初始模型。
extract_result: success
object_mentions:
- object_type: project
  name: AgingBench
  canonical_name: AgingBench
  url: https://arxiv.org/abs/2605.26302
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文介绍了 AgingBench，一个用于代理生命周期工程的纵向可靠性基准，不仅衡量退化程度还诊断退化形式。
  - AgingBench 将代理老化组织为四种机制：压缩老化、干扰老化、修订老化和维护老化。
  - 在 7 个场景、14 个模型和多种记忆策略下的约 400 次实验说明代理老化是多维的，需要机制级别诊断和针对性修复。
  article_id: 27fbaeab8c07a7da
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