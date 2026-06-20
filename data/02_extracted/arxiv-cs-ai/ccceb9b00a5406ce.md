---
title: Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role
  Agent Simulation
source: https://arxiv.org/abs/2606.17459
author:
- '[[Yuyang Dai, Xueqing Peng, Lingfei Qian, Zhuohan Xie]]'
published: '2026-06-17'
created: '2026-06-17'
description: 'arXiv:2606.17459v1 Announce Type: new Abstract: Evaluating the decision-making
  capabilities of large language models (LLMs) is a growing research priority, yet
  existing benchmarks focus on isolated cognitive tasks such as reasoning, knowledge
  retrieval, and economic rationality in stylized settings. These evaluations overlook
  the defining challenge of real executive decision-making: integrating conflicting
  recommendations from specialized stakeholders under information asymmetry, organizational
  constraints, and temporal dependencies. We introduce \textsc{CEO-Bench}, a multi-agent
  benchmark that evaluates LLMs on CEO-level strategic resource reallocation -- the
  process of redirecting capital across business units in a multi-round, constraint-rich
  organizational environment. In \textsc{CEO-Bench}, LLM agents receive conflicting
  advice from four role-conditioned C-suite advisors (CFO, CTO, COO, CMO), each with
  private signals and distinct priorities, and must synthesize these into a concrete
  allocation plan evaluated along four dimensions: role integration, conditional boldness,
  history-sensitive judgment, and plan validity. Experiments across five frontier
  models on 13 scenarios reveal that all models achieve high structural validity but
  diverge sharply on strategic calibration -- the hardest capability layer. We identify
  systematic failure modes including single-advisor capture, conservative default
  under ambiguity, and historical amnesia, and uncover a structural integration-boldness
  tradeoff: models that engage more deeply with conflicting perspectives tend to produce
  less decisive action. These findings delineate the current capability boundary of
  LLMs as organizational decision-makers and inform the design of future AI-assisted
  executive systems.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ccceb9b00a5406ce
source_type: academic_paper
tldr: 提出CEO-Bench基准，评估LLM在多角色CEO战略资源再分配决策中的能力。
objective_summary: 研究者提出了CEO-Bench，一个多智能体基准，让LLM接收CFO/CTO/COO/CMO四类高管的冲突建议，在约束丰富的多轮环境中测试CEO级战略资源再分配决策。实验覆盖5个前沿模型的13个场景，发现所有模型结构有效性高但战略校准差异显著，存在单顾问捕获、保守默认和历史遗忘等系统性失效。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - CEO-Bench
  - Multi-Agent System
  key_people: []
key_logic_flow:
- 现有LLM基准仅关注孤立认知任务，缺少对CEO级战略决策（在信息不对称、组织约束和时间依赖下整合冲突建议）的评估。
- 提出CEO-Bench基准，让LLM代理接收CFO、CTO、COO、CMO四位角色化高管的冲突建议，制定资本再分配方案。
- 评估四个维度：角色整合、条件性大胆、历史敏感判断和计划有效性。
- 在5个前沿模型的13个场景上实验发现，所有模型结构有效性高但在战略校准上差异显著。
- 识别出系统性失效模式：单一顾问捕获、模糊情境下的保守默认和历史遗忘。
- 发现结构整合-大胆性权衡：越深入参与冲突观点整合的模型，其决策果断性越低。
---

# Computer Science > Artificial Intelligence

# Title:Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation with Multi-Role Agent Simulation

View PDF HTML (experimental)Abstract:Evaluating the decision-making capabilities of large language models (LLMs) is a growing research priority, yet existing benchmarks focus on isolated cognitive tasks such as reasoning, knowledge retrieval, and economic rationality in stylized settings. These evaluations overlook the defining challenge of real executive decision-making: integrating conflicting recommendations from specialized stakeholders under information asymmetry, organizational constraints, and temporal dependencies. We introduce \textsc{CEO-Bench}, a multi-agent benchmark that evaluates LLMs on CEO-level strategic resource reallocation -- the process of redirecting capital across business units in a multi-round, constraint-rich organizational environment. In \textsc{CEO-Bench}, LLM agents receive conflicting advice from four role-conditioned C-suite advisors (CFO, CTO, COO, CMO), each with private signals and distinct priorities, and must synthesize these into a concrete allocation plan evaluated along four dimensions: role integration, conditional boldness, history-sensitive judgment, and plan validity. Experiments across five frontier models on 13 scenarios reveal that all models achieve high structural validity but diverge sharply on strategic calibration -- the hardest capability layer. We identify systematic failure modes including single-advisor capture, conservative default under ambiguity, and historical amnesia, and uncover a structural integration-boldness tradeoff: models that engage more deeply with conflicting perspectives tend to produce less decisive action. These findings delineate the current capability boundary of LLMs as organizational decision-makers and inform the design of future AI-assisted executive systems.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.