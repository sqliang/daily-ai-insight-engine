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
tldr: SEAGym 是一个用于评估自进化 LLM 代理框架（agent harness）的多维度测试环境。
objective_summary: 研究团队提出 SEAGym，一个用于评估自进化 LLM 代理框架更新的测试环境，覆盖训练、验证、测试、回放和成本记录。在 Terminal-Bench
  2.0 和 HLE 上对比 ACE、TF-GRPO、AHE 三种方法，发现频繁更新不一定提升保留集性能，中间快照可能后续失效。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - SEAGym
  - LLM
  - ACE
  - TF-GRPO
  - AHE
  - Terminal-Bench 2.0
  - HLE
  - Harbor
  key_people: []
key_logic_flow:
- SEAGym 是一个专为自进化 LLM 代理框架（agent harness）设计的评估环境，覆盖训练、验证、测试、回放和成本记录五个维度。
- 现有评估方法将代理进化简化为孤立任务分数或单条序列曲线，无法判断更新是否产生可复用改进、过拟合、增加成本或损害旧行为。
- SEAGym 将 Harbor 兼容的基准测试转化为动态自进化任务源，提供训练批次、冻结更新验证、ID/OOD 迁移视图、回放诊断及快照记录。
- 研究者在 Terminal-Bench 2.0 和 HLE 上对 ACE、TF-GRPO 和 AHE 三种方法进行了对比实验。
- 实验发现：频繁更新未必提升保留集性能，有用的中间快照可能在后续训练中失效，来源多样性和模型后端影响代理框架的可靠性。
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