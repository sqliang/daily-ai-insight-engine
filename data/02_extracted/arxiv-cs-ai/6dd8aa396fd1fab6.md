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
tldr: DecisionBench 是一个用于评估长周期 AI 智能体工作流中紧急委派能力的基准测试平台，基于 GAIA、tau-bench、BFCL 三个任务套件和
  11 个模型的参考评估发现：各意识条件下的终端任务质量无统计显著差异，但路由保真度差异巨大（7.5% 至 29.5%），且完美委派上限与实际表现之间存在 15
  到 31 个百分点的差距。
objective_summary: 研究者提出了 DecisionBench，这是一个用于评估长周期 AI 智能体工作流中紧急委派能力的标准化基准测试平台。该平台固定了任务套件（GAIA、tau-bench、BFCL
  multi-turn）、同行模型池（来自 7 个供应商家族的 11 个模型）、委派接口（call_model 加可选的 read_profile 通道）、确定性技能标注层和多维度评估指标套件。通过对全部模型池进行五条件参考扫描（n=23,375
  个任务实例），研究发现仅评估质量会遗漏编排信号，路由保真度在各条件下差异显著（7.5% 至 29.5%），且反事实分析显示完美委派上限与实际表现之间存在 15
  到 31 个百分点的提升空间。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - GAIA
  - tau-bench
  - BFCL
  key_people: []
key_logic_flow:
- DecisionBench 是一个用于评估长周期 AI 智能体工作流中紧急委派能力的基准测试平台，固定了任务套件、模型池、委派接口、技能标注层和多维度评估指标。
- 任务套件包括 GAIA、tau-bench 和 BFCL multi-turn 三个基准，模型池涵盖来自 7 个供应商家族的 11 个模型。
- 研究通过五条件参考扫描对全部模型池进行表征分析，总任务实例数为 23,375 个。
- 终端任务质量在各意识条件下无统计显著差异，仅评估质量会遗漏编排信号。
- 路由保真度在不同条件下差异巨大（7.5% 至 29.5%），且交付渠道（按需工具 vs 预加载描述）的影响超过描述内容。
- 反事实完美委派上限在所有任务套件上均高于实测表现 15 至 31 个百分点，表明编排方法仍有巨大提升空间。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: project
  name: DecisionBench
  canonical_name: DecisionBench
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - DecisionBench 是一个由研究者提出的、用于评估长周期 AI 智能体工作流中紧急委派能力的标准化基准测试平台。
  - 该平台固定了 GAIA、tau-bench、BFCL multi-turn 三个任务套件和来自 7 个供应商家族的 11 个模型的同行模型池。
  - 研究通过 23,375 个任务实例的五条件参考扫描发现完美委派上限与实际表现之间存在 15 到 31 个百分点的差距。
  article_id: 6dd8aa396fd1fab6
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