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
tldr: DecisionBench 提出评估多智能体长期委托协作能力的标准化基准框架
objective_summary: 研究者在 arXiv 发布 DecisionBench 基准，用于评估长周期智能体工作流中的委托协作能力。该基准包含 GAIA、tau-bench、BFCL
  multi-turn 三个任务套件、11 个模型（来自 7 个供应商家族）和多项评估指标，在 23,375 个实例上完成参考扫描。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - DecisionBench
  - GAIA
  - tau-bench
  - BFCL multi-turn
  key_people: []
key_logic_flow:
- DecisionBench 是一个标准化基准框架，专门用于评估长周期智能体工作流中的委托协作能力，包含任务套件、模型池、委托接口、技能标注层和多维度评估指标。
- 框架包含三个任务套件（GAIA、tau-bench、BFCL multi-turn），11 个模型组成同伴模型池（来自 7 个供应商家族），委托接口为 call_model
  加可选 read_profile 通道。
- 研究者在全部模型池上执行了五个条件的参考扫描，累计 23,375 个任务实例。
- 四种感知条件下的平均任务质量无统计学显著差异（|beta| <= 0.010, p >= 0.21），说明仅凭质量指标会遗漏委托编排信号。
- Top-1 路由保真度在不同条件间从 7.5% 到 29.5% 不等，且交付通道（按需工具 vs. 预加载描述）对结果的影响远大于描述内容本身。
- 反事实天花板分析表明，完美委托相比当前实测性能还有 15 到 31 个百分点的未实现提升空间，表明未来的编排方法仍有很大潜力。
pipeline_stage: fact_extracted
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