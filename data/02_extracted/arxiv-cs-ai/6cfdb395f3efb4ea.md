---
title: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
source: https://arxiv.org/abs/2607.28802
author:
- '[[Harsh Raj, Vipul Gupta, Anas Mahmoud, Razvan-Gabriel Dumitru, Darvin Yi, Aakash
  Sabharwal, Yunzhong He]]'
published: '2026-08-03'
created: '2026-08-03'
manifest_dates:
- '2026-08-03'
description: 'arXiv:2607.28802v1 Announce Type: new Abstract: Existing evaluations
  often reduce agent failures to system-level outcomes, obscuring where the fault
  originated and which intervention would improve the agent system. This creates a
  repair-assignment problem: the same visible failure may call for model post-training,
  harness engineering, environment redesign, or benchmark repair depending on its
  source. Because agent behavior emerges from interactions among models, harnesses,
  users, tools, memory, and environments, outcome-level labels are often insufficient
  for improvement. Most failure taxonomies do little to resolve this problem because
  they are benchmark-specific and lack a shared structure. We introduce an interaction-centric
  taxonomy that localizes failures to the interactions in which they originate and
  identifies the responsible component. It organizes 41 failure modes by assigning
  each to an edge between two components and a fault side indicating where the repair
  belongs. This makes the taxonomy actionable: model-side failures identify targets
  for post-training, harness-side failures point to scaffolding and tool-integration
  fixes, and environment or grader failures reveal evaluation conditions requiring
  redesign. The schema applies across agent architectures, from coding assistants
  to long-horizon personal assistants and multi-agent systems. We ground the taxonomy
  in worked examples from public benchmarks, model system cards, published reports,
  and logged agent trajectories, and evaluate its reproducibility using independent
  reasoning agents as judges. Across four frontier models, the strongest judge reaches
  Cohen''s $\kappa=0.76$ against human category labels, suggesting that the categories
  capture shared structure rather than annotator-specific preferences.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6cfdb395f3efb4ea
source_type: academic_paper
tldr: 本文提出一种以交互为中心的智能体失败分类体系，将41种失败模式定位到组件间交互边与故障归属侧，区分模型侧、框架侧与评测侧修复责任。在四个前沿模型上，最强评判者对人工标签的
  Cohen's κ 达 0.76。
objective_summary: 一篇 arXiv 预印本论文提出以交互为中心的智能体失败分类体系，旨在解决现有评测只报告系统级结果、掩盖故障来源、导致修复分配困难的普遍问题。该体系将41种失败模式分配到模型、框架、用户、工具、记忆与环境等组件之间的交互边，并标明责任侧，使模型侧失败对应后训练目标、框架侧对应脚手架与工具集成修复、评测侧对应环境重设计。研究者用公开基准、模型系统卡片、已发表报告与智能体轨迹日志验证该分类，并用独立推理智能体作为评判者评估可复现性，在四个前沿模型上最强评判者的
  Cohen's κ 达 0.76。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - AI Agent
  - LLM
  - Multi-Agent Systems
  key_people: []
key_logic_flow:
- 现有评测常把智能体失败简化为系统级结果，掩盖故障来源，导致同一可见失败可能对应模型后训练、框架工程、环境重设计或基准修复等不同干预。
- 作者提出以交互为中心的失败分类体系，将41种失败模式分别指派到两个组件之间的交互边，并标注责任侧以定位需要修复的对象。
- 该分类具有可操作性：模型侧失败对应后训练目标，框架侧失败对应脚手架与工具集成修复，环境或评分器失败对应评测条件重设计。
- 该体系可跨智能体架构迁移，覆盖编码助手、长时程个人助手和多智能体系统。
- 研究者从公开基准、模型系统卡片、已发表报告和记录的智能体轨迹中取得实例来支撑该分类体系。
- 可复现性评估使用独立推理智能体作为评判者，在四个前沿模型上最强评判者对人工类别标签的 Cohen's κ 达到 0.76。
object_mentions:
- object_type: paper
  name: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
  canonical_name: Model or Harness? An Interaction-Centric Taxonomy for Localizing
    Agent Failures
  url: https://arxiv.org/abs/2607.28802
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者提出一种以交互为中心的失败分类体系，将41种失败模式分配到组件之间的交互边上，并标明故障归属一侧，从而定位责任组件。
  - 该体系具有可操作性：模型侧失败指向后训练目标，框架侧失败指向脚手架与工具集成修复，环境或评分器失败指向评测条件重设计。
  - 在四个前沿模型上，最强评判者对人工类别标签达到 Cohen's κ=0.76，表明这些类别捕捉的是共享结构而非标注者特定偏好。
  article_id: 6cfdb395f3efb4ea
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

View PDF HTML (experimental)Abstract:Existing evaluations often reduce agent failures to system-level outcomes, obscuring where the fault originated and which intervention would improve the agent system. This creates a repair-assignment problem: the same visible failure may call for model post-training, harness engineering, environment redesign, or benchmark repair depending on its source. Because agent behavior emerges from interactions among models, harnesses, users, tools, memory, and environments, outcome-level labels are often insufficient for improvement. Most failure taxonomies do little to resolve this problem because they are benchmark-specific and lack a shared structure. We introduce an interaction-centric taxonomy that localizes failures to the interactions in which they originate and identifies the responsible component. It organizes 41 failure modes by assigning each to an edge between two components and a fault side indicating where the repair belongs. This makes the taxonomy actionable: model-side failures identify targets for post-training, harness-side failures point to scaffolding and tool-integration fixes, and environment or grader failures reveal evaluation conditions requiring redesign. The schema applies across agent architectures, from coding assistants to long-horizon personal assistants and multi-agent systems. We ground the taxonomy in worked examples from public benchmarks, model system cards, published reports, and logged agent trajectories, and evaluate its reproducibility using independent reasoning agents as judges. Across four frontier models, the strongest judge reaches Cohen's $\kappa=0.76$ against human category labels, suggesting that the categories capture shared structure rather than annotator-specific preferences.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.