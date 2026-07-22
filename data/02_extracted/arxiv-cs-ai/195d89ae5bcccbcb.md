---
title: 'SEAGym: An Evaluation Environment for Self-Evolving LLM Agents'
source: https://arxiv.org/abs/2606.17546
author:
- '[[Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang]]'
published: '2026-06-17'
created: '2026-06-17'
description: 'arXiv:2606.17546v1 Announce Type: new Abstract: Self-evolving LLM-based
  agents improve mainly by changing their agent harness: the structured execution
  layer around a base model, including prompts, memory, tools, middleware, runtime
  state, and the model-tool interaction loop. Existing evaluations often reduce this
  process to isolated task scores or a single sequential curve, obscuring whether
  an update produces reusable improvement, overfits recent tasks, increases cost,
  or harms older behavior. We introduce SEAGym, an evaluation environment for measuring
  agent harness updates across training, validation, test, replay, and cost records.
  SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources
  with train batches, frozen update-validation, held-out ID and OOD transfer views,
  replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym
  on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch
  protocol. The results show that these evaluation views provide complementary signals
  about the evolution process: frequent updates may fail to improve held-out performance,
  useful intermediate snapshots may collapse later, and source diversity and model
  backend can affect harness reliability.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 195d89ae5bcccbcb
source_type: academic_paper
tldr: SEAGym 是一个用于评估自进化 LLM Agent 框架更新的评测环境，在 Terminal-Bench 2.0 和 HLE 上对比了 ACE、TF-GRPO
  和 AHE 三种方法，发现频繁更新可能无法提升留出性能且中间快照可能在后继更新中崩溃。
objective_summary: 研究者提出了 SEAGym，一个专为自进化 LLM Agent 设计的评测环境，用于衡量 agent harness（包括提示词、记忆、工具、中间件、运行时状态及模型-工具交互循环）的更新效果。SEAGym
  提供训练、验证、测试、回放和成本记录五个维度的评估视图，将 Harbor 兼容基准测试转化为动态自进化任务源。研究者在 Terminal-Bench 2.0 和
  HLE 上实例化 SEAGym，对比了 ACE、TF-GRPO 和 AHE 三种方法，结果表明频繁更新可能无法提升留出测试集性能，有用中间快照可能在后继更新中崩溃，且源多样性与模型后端影响框架可靠性。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - SEAGym
  - ACE
  - TF-GRPO
  - AHE
  - Terminal-Bench 2.0
  - HLE
  - Harbor
  key_people: []
key_logic_flow:
- SEAGym 是一个专门用于评估自进化 LLM Agent 的评测环境，核心关注 agent harness 层面的更新，包括提示词、记忆、工具、中间件和运行时状态。
- 现有评估方法通常将自进化过程简化为孤立任务分数或单一序列曲线，无法判断更新是否产生可复用改进、是否过拟合近期任务或是否损害旧行为。
- SEAGym 提供训练、验证、测试、回放和成本记录五个评估维度，并将 Harbor 兼容基准测试转化为动态自进化任务源。
- 研究者在 Terminal-Bench 2.0 和 HLE 两个基准上实例化 SEAGym，对比了 ACE、TF-GRPO 和 AHE 三种自进化方法在统一 epoch/batch
  协议下的表现。
- 实验结果表明频繁更新可能无法提升留出测试集性能，有用的中间快照可能在后续更新中性能衰退，且源多样性与模型后端选择会影响 agent 框架的整体可靠性。
extract_result: success
object_mentions:
- object_type: project
  name: SEAGym
  canonical_name: SEAGym
  url: https://arxiv.org/abs/2606.17546
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SEAGym 是一个用于测量 agent harness 更新效果的评测环境，覆盖训练、验证、测试、回放和成本记录五个维度。
  - SEAGym 将 Harbor 兼容基准测试转化为动态自进化任务源，支持训练批次、冻结更新验证、留出 ID 和 OOD 迁移视图以及回放诊断。
  article_id: 195d89ae5bcccbcb
- object_type: dataset
  name: Terminal-Bench 2.0
  canonical_name: Terminal-Bench 2.0
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者将 SEAGym 实例化在 Terminal-Bench 2.0 和 HLE 两个基准上，用于对比不同自进化方法的效果。
  article_id: 195d89ae5bcccbcb
- object_type: dataset
  name: HLE
  canonical_name: HLE
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者将 SEAGym 实例化在 Terminal-Bench 2.0 和 HLE 两个基准上，用于对比不同自进化方法的效果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: ACE
  canonical_name: ACE
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: TF-GRPO
  canonical_name: TF-GRPO
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: AHE
  canonical_name: AHE
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 研究者在统一 epoch/batch 协议下，使用 SEAGym 对比了 ACE、TF-GRPO 和 AHE 三种自进化方法的评估结果。
  article_id: 195d89ae5bcccbcb
- object_type: project
  name: Harbor
  canonical_name: Harbor
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - SEAGym 将 Harbor 兼容的基准测试转化为动态自进化任务源，以支持训练批次和冻结更新验证等功能。
  article_id: 195d89ae5bcccbcb
---

# Computer Science > Artificial Intelligence

# Title:SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

View PDF HTML (experimental)Abstract:Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.