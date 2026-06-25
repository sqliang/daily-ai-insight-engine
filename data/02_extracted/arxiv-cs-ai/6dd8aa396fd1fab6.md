---
title: 'DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic
  Workflows'
source: https://arxiv.org/abs/2605.19099
author:
- '[[Yuxuan Gao, Megan Wang, Yi Ling Yu, Zijian Carl Ma, Ao Qu]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'arXiv:2605.19099v1 Announce Type: new Abstract: We introduce DecisionBench,
  a benchmark substrate for emergent delegation in long-horizon agentic workflows.
  The substrate fixes a task suite (GAIA, tau-bench, BFCL multi-turn), a peer-model
  pool (11 models, 7 vendor families), a delegation interface (call_model plus an
  optional read_profile channel), a deterministic skill-annotation layer, and a multi-axis
  metric suite covering quality, cost, latency, delegation rate, routing fidelity-at-k,
  vendor self-preference, and a counterfactual-delegation ceiling. The substrate is
  agnostic to how peer information is generated or delivered, so learned routers,
  richer peer memories, adaptive profile construction, and multi-step delegation can
  all be evaluated against it. We characterize the substrate with a five-condition
  reference sweep on the full pool (n=23,375 task instances). Three benchmark-level
  findings emerge: (i) mean end-task quality is statistically indistinguishable across
  the four awareness conditions (|beta| = 0.21), so quality-only evaluation would
  miss the orchestration signal; (ii) routing fidelity-at-1 ranges from 7.5% to 29.5%
  across conditions at near-equal mean quality, with delivery channel (on-demand tool
  vs. preloaded description) dominating description content; (iii) a counterfactual
  ceiling places perfect delegation 15-31 percentage points above measured performance
  on every suite, locating large unrealized headroom for future orchestration methods.
  We release the substrate, annotation layer, reference intervention suite, analysis
  pipeline, and 220 per-condition run archives.'
tags:
- clippings
extraction_status: success
id: 6dd8aa396fd1fab6
source_type: academic_paper
tldr: DecisionBench发布：用于评估长周期Agent工作流中涌现式委托行为的基准测试平台，覆盖11模型×3任务套件×23375实例。
objective_summary: 学术团队在arXiv发布DecisionBench基准测试平台，整合GAIA、tau-bench、BFCL三个任务套件与11个模型的委托评估框架。在23375个任务实例上进行五条件参考扫描，发现质量指标无法区分委托策略优劣，路由保真度仅7.5%-29.5%，完美委托上限比实测高15-31个百分点。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - DecisionBench
  - GAIA
  - tau-bench
  - BFCL
  - emergent delegation
  - agentic workflow
  - model routing
  key_people: []
key_logic_flow:
- DecisionBench是一个用于评估长周期Agent工作流中涌现式委托行为的基准测试平台，固定了任务套件、模型池、委托接口和指标体系四个核心要素
- 平台使用3个任务套件（GAIA、tau-bench、BFCL多轮）和11个模型（来自7个供应商家族），通过call_model接口和可选的read_profile通道实现委托
- 评估指标涵盖质量、成本、延迟、委托率、路由保真度@k、供应商自偏好以及反事实委托上限共七个维度
- 在23375个任务实例上的五条件参考扫描发现：四种awareness条件下端任务质量在统计上无显著差异（|beta|≤0.010, p≥0.21），仅靠质量评估会遗漏编排信号
- 路由保真度@1在不同条件下仅为7.5%-29.5%，交付通道（按需工具vs预加载描述）的影响远大于描述内容本身
- 反事实上限分析表明，完美委托比当前实测性能高出15-31个百分点，揭示了未来编排方法的巨大提升空间
pipeline_stage: fact_extracted
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows

View PDF HTML (experimental)Abstract:We introduce DecisionBench, a benchmark substrate for emergent delegation in long-horizon agentic workflows. The substrate fixes a task suite (GAIA, tau-bench, BFCL multi-turn), a peer-model pool (11 models, 7 vendor families), a delegation interface (call_model plus an optional read_profile channel), a deterministic skill-annotation layer, and a multi-axis metric suite covering quality, cost, latency, delegation rate, routing fidelity-at-k, vendor self-preference, and a counterfactual-delegation ceiling. The substrate is agnostic to how peer information is generated or delivered, so learned routers, richer peer memories, adaptive profile construction, and multi-step delegation can all be evaluated against it. We characterize the substrate with a five-condition reference sweep on the full pool (n=23,375 task instances). Three benchmark-level findings emerge: (i) mean end-task quality is statistically indistinguishable across the four awareness conditions (|beta| <= 0.010, p >= 0.21), so quality-only evaluation would miss the orchestration signal; (ii) routing fidelity-at-1 ranges from 7.5% to 29.5% across conditions at near-equal mean quality, with delivery channel (on-demand tool vs. preloaded description) dominating description content; (iii) a counterfactual ceiling places perfect delegation 15-31 percentage points above measured performance on every suite, locating large unrealized headroom for future orchestration methods. We release the substrate, annotation layer, reference intervention suite, analysis pipeline, and 220 per-condition run archives.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.