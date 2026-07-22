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
tldr: 该论文提出 CEO-Bench，一个多智能体基准测试，评估大语言模型在模拟企业环境中进行跨部门战略资源重新分配的能力。实验发现前沿模型在结构有效性上表现良好，但在战略校准层面出现严重分化，并揭示了单一顾问依赖、模糊情境下保守决策和历史遗忘等系统性失败模式。
objective_summary: arXiv 在 2026 年 6 月发表的论文中提出了 CEO-Bench，这是一个多智能体基准测试框架，用于评估大语言模型在模拟
  CEO 角色下进行多轮战略资源重新分配的能力。LLM 代理需要综合来自 CFO、CTO、COO、CMO 四位角色化 C 级顾问的冲突建议，并在信息不对称和组织约束下制定资本分配方案，评估维度包括角色整合、条件性果断、历史敏感判断和计划有效性。在
  5 个前沿模型和 13 个场景上的实验显示，所有模型在结构有效性维度得分较高，但在战略校准等更高能力层出现显著分化。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - CEO-Bench
  key_people: []
key_logic_flow:
- 论文指出现有 LLM 评估基准局限于孤立的认知任务，如推理、知识检索和风格化经济理性，缺乏对真实高管决策环境的模拟。
- 作者提出了 CEO-Bench，一个多智能体基准测试，要求 LLM 代理扮演 CEO 角色，在信息不对称和约束条件下整合四位 C 级顾问的冲突建议并制定资本分配方案。
- 评估体系包含四个维度：角色整合、条件性果断、历史敏感判断和计划有效性，覆盖从低到高三个能力层。
- 在 5 个前沿模型和 13 个场景上的实验显示，所有模型在结构有效性上表现良好，但在战略校准这一最高能力层出现显著分化。
- 论文识别出三种系统性失败模式：单一顾问捕获、模糊情境下保守默认决策和历史遗忘。
- 研究还发现了一个结构性的整合-果断权衡：模型越深入参与冲突观点的综合，其行动决策往往越不果断。
extract_result: success
object_mentions:
- object_type: project
  name: CEO-Bench
  canonical_name: CEO-Bench
  url: https://arxiv.org/abs/2606.17459
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 CEO-Bench，一个多智能体基准测试，用于评估 LLM 在 CEO 级别的战略资源重新分配能力。
  - CEO-Bench 要求 LLM 代理整合四位角色化 C 级顾问（CFO、CTO、COO、CMO）的冲突建议，制定跨业务单元的资本分配计划。
  - 实验在 5 个前沿模型和 13 个场景上运行，发现模型在战略校准层面存在系统性失败模式。
  article_id: ccceb9b00a5406ce
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