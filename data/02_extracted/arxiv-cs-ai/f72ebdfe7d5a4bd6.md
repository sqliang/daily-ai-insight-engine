---
title: 'Large Language Models Can Follow Instructions, But Not Many at Once: Phase
  Transitions in Compositional Constraint Satisfaction'
source: https://arxiv.org/abs/2608.12426
author:
- '[[Mariya I. Vasileva]]'
published: '2026-08-15'
created: '2026-08-15'
manifest_dates:
- '2026-08-15'
description: 'arXiv:2608.12426v1 Announce Type: new Abstract: Large language models
  are increasingly deployed in settings that require simultaneous adherence to multiple
  explicit constraints - reasoning structure, safety boundaries, output schemas. Individual
  constraints are handled proficiently, but the compositional regime, where many must
  hold jointly, remains poorly characterized: how rapidly does performance degrade,
  what governs the degradation, and can the collapse be mitigated? We introduce Constraint
  Saturation Evaluation (CSE), a procedurally generated benchmark that systematically
  varies the number of simultaneous constraints (k), with every constraint scored
  by a deterministic, rule-based verifier and zero LLM-judge involvement: 15 models,
  36 constraint types, 369,753 checks at k=1-12. Three findings emerge. First, per-constraint
  pass rate decays gradually and predictably, while the chance of satisfying all k
  constraints collapses - a model passing individual constraints at ~41% at k=8 succeeds
  on all eight just 5.7% of the time. Second, constraints do not degrade equally:
  structural constraints lose 2x more baseline capability per added constraint than
  lexical ones, ordered by a comprehension-maintenance gap that separates constraints
  requiring sustained tracking from binary decisions immune to composition. Third,
  failures are nearly independent, which is what makes the accumulation multiplicative;
  the residual coupling that does exist tracks shared output features rather than
  pairwise interference - a wrong sentence count fails every constraint that reads
  it. Reliable instruction following breaks down beyond 5-6 simultaneous constraints:
  probe-level success falls below 50% at 7 constraints for the strongest model, and
  at 3 or fewer for 12 of 15.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f72ebdfe7d5a4bd6
source_type: academic_paper
tldr: arXiv 论文提出 Constraint Saturation Evaluation (CSE) 程序化基准，系统评估 15 个模型在 1-12 个同时约束下的指令遵循能力。研究发现同时约束超过
  5-6 个时可靠遵循即失效：最强模型在 7 个约束时成功率跌破 50%，15 个模型中有 12 个在 3 个及以内约束时即低于该阈值。
objective_summary: 该论文针对大语言模型同时遵循多个显式约束的能力展开系统研究，提出程序化生成的基准 Constraint Saturation
  Evaluation (CSE)。实验覆盖 15 个模型、36 种约束类型，在 k=1 到 12 的范围内共完成 369,753 次检查，全部采用确定性规则验证器评分且无
  LLM 裁判参与。结果显示单个约束的通过率随约束数量增加而平缓衰减，但所有约束同时满足的概率急剧崩溃，且结构性约束每增加一个约束损失的基线能力约为词法约束的 2
  倍。可靠的指令遵循在超过 5-6 个同时约束时失效。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - LLM
  - CSE
  - Constraint Saturation Evaluation
  key_people: []
key_logic_flow:
- 论文提出 Constraint Saturation Evaluation (CSE) 基准，通过程序化生成方式系统变化同时约束的数量 k，每个约束由确定性规则验证器评分且全程无
  LLM 裁判参与。
- 实验覆盖 15 个模型、36 种约束类型，在 k=1 到 12 的范围内累计执行 369,753 次约束检查。
- 单个约束的通过率随 k 增加而平缓且可预测地衰减，但全部 k 个约束同时满足的概率急剧崩溃，例如某模型在 k=8 时单个约束通过率约 41%，而八个约束全部通过的概率仅
  5.7%。
- 不同约束的退化速度不均等，结构性约束每增加一个约束损失的基线能力是词法约束的 2 倍，对应持续追踪与二元决策类约束之间的理解维持差距。
- 失败事件近乎独立，使累积效应呈乘法增长，残存耦合主要追踪共享输出特征而非成对干扰。
- 可靠的指令遵循在同时约束超过 5-6 个时失效，最强模型在 7 个约束时探测级成功率跌破 50%，而 15 个模型中有 12 个在 3 个或更少约束时即低于该阈值。
object_mentions:
- object_type: paper
  name: 'Large Language Models Can Follow Instructions, But Not Many at Once: Phase
    Transitions in Compositional Constraint Satisfaction'
  canonical_name: 'Large Language Models Can Follow Instructions, But Not Many at
    Once: Phase Transitions in Compositional Constraint Satisfaction'
  url: https://arxiv.org/abs/2608.12426
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文针对大语言模型同时遵循多个显式约束的能力展开系统研究，并提出程序化生成的基准 Constraint Saturation Evaluation (CSE)。
  - 实验覆盖 15 个模型和 36 种约束类型，在 k=1 到 12 范围内累计完成 369,753 次约束检查。
  article_id: f72ebdfe7d5a4bd6
- object_type: project
  name: Constraint Saturation Evaluation (CSE)
  canonical_name: Constraint Saturation Evaluation (CSE)
  url: https://arxiv.org/abs/2608.12426
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - CSE 是程序化生成的基准，通过系统变化同时约束的数量 k 来评估模型，每个约束由确定性规则验证器评分且无 LLM 裁判参与。
  - 基于 CSE 的实验结果显示，可靠的指令遵循在同时约束超过 5-6 个时失效，最强模型在 7 个约束时成功率跌破 50%。
  article_id: f72ebdfe7d5a4bd6
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction

View PDF HTML (experimental)Abstract:Large language models are increasingly deployed in settings that require simultaneous adherence to multiple explicit constraints - reasoning structure, safety boundaries, output schemas. Individual constraints are handled proficiently, but the compositional regime, where many must hold jointly, remains poorly characterized: how rapidly does performance degrade, what governs the degradation, and can the collapse be mitigated? We introduce Constraint Saturation Evaluation (CSE), a procedurally generated benchmark that systematically varies the number of simultaneous constraints (k), with every constraint scored by a deterministic, rule-based verifier and zero LLM-judge involvement: 15 models, 36 constraint types, 369,753 checks at k=1-12. Three findings emerge. First, per-constraint pass rate decays gradually and predictably, while the chance of satisfying all k constraints collapses - a model passing individual constraints at ~41% at k=8 succeeds on all eight just 5.7% of the time. Second, constraints do not degrade equally: structural constraints lose 2x more baseline capability per added constraint than lexical ones, ordered by a comprehension-maintenance gap that separates constraints requiring sustained tracking from binary decisions immune to composition. Third, failures are nearly independent, which is what makes the accumulation multiplicative; the residual coupling that does exist tracks shared output features rather than pairwise interference - a wrong sentence count fails every constraint that reads it. Reliable instruction following breaks down beyond 5-6 simultaneous constraints: probe-level success falls below 50% at 7 constraints for the strongest model, and at 3 or fewer for 12 of 15.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.