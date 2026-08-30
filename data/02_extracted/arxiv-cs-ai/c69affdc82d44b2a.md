---
title: 'Automata from Agent Traces: Failure and Next-Step Prediction'
source: https://arxiv.org/abs/2608.23670
author:
- '[[Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton
  Da Costa, Ilham Wicaksono, Adriano Koshiyama]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23670v1 Announce Type: new Abstract: LLM-based agents execute
  multi-step tasks, but their behavioral structure remains opaque: long unstructured
  traces resist the safety auditing and runtime monitoring that deployment requires.
  Existing approaches operate per-trace or success-only, so they miss the cross-run
  topology that links next-step and failure prediction. To recover that shared structure,
  we collapse an entire trace corpus into a single, compact finite-state machine (FSM)
  that serves as a structural substrate for the otherwise unpredictable behavior of
  LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay
  held-out data at >=0.997 fitness with near-identical topology across splits, and
  build in milliseconds. This substrate addresses both prediction goals. For next-step
  prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched
  dataset. For failure prediction, per-state behavioral features reach held-out AUROC
  up to 0.94, and an online monitor ranks failing runs above passing ones from a partial
  trace, triggering early stopping well before completion. Behavioral topology thus
  appears shaped more by the deployment harness than by the LLM, providing a model-agnostic
  structural primitive for safety auditing and runtime monitoring.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c69affdc82d44b2a
source_type: academic_paper
tldr: 论文提出将LLM代理的整个轨迹语料库压缩为单个紧凑的有限状态机（FSM），用于下一步预测与失败预测。在十二个公开数据集上，FSM仅含7-43个状态、拟合度不低于0.997，失败预测AUROC最高达0.94，并支持在线提前停止。
objective_summary: 该研究针对LLM代理多步任务行为结构不透明的问题，提出将整个轨迹语料库压缩为单个紧凑的有限状态机（FSM），作为代理行为的结构化基础。实验在十二个公开数据集上进行，FSM仅含7-43个状态，对保留数据拟合度不低于0.997，构建耗时仅毫秒级。在下一步预测上，FSM状态上下文在所有真值匹配的数据集上均优于Agent
  Workflow Memory基线；失败预测的每状态行为特征AUROC最高达0.94。在线监控器能凭部分轨迹区分失败与成功运行，在任务完成前触发提前停止，且行为拓扑更多由部署框架而非LLM本身塑造。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - FSM
  - LLM
  - Agent Workflow Memory
  key_people: []
key_logic_flow:
- LLM代理的多步任务执行行为结构不透明，长而无结构的轨迹难以支撑安全审计与运行时监控。
- 现有方法按单条轨迹或仅成功案例处理，忽略了连接下一步预测与失败预测的跨运行拓扑结构。
- 论文将整个轨迹语料库压缩为单个紧凑的有限状态机，作为代理行为预测的结构化基础。
- 在十二个公开数据集上，FSM仅含7至43个状态，对保留数据拟合度不低于0.997且拓扑跨划分几乎一致，构建仅需毫秒级。
- 在下一步预测上，FSM状态上下文在每个真值匹配的数据集上均优于Agent Workflow Memory基线方法。
- 在失败预测上，每状态行为特征AUROC最高达0.94，在线监控器能凭部分轨迹在任务完成前触发提前停止。
object_mentions:
- object_type: paper
  name: 'Automata from Agent Traces: Failure and Next-Step Prediction'
  canonical_name: Automata from Agent Traces
  url: https://arxiv.org/abs/2608.23670
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文提出将LLM代理的整个轨迹语料库压缩为单个紧凑的有限状态机，作为行为预测的结构化基础。
  - 论文在十二个公开数据集上验证，FSM仅含7至43个状态，对保留数据的拟合度不低于0.997。
  - 在线监控器能凭部分轨迹将失败运行排在通过运行之前，并在任务完成前触发提前停止。
  article_id: c69affdc82d44b2a
- object_type: paper
  name: Agent Workflow Memory
  canonical_name: Agent Workflow Memory
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在下一步预测任务中，FSM状态上下文在每个真值匹配的数据集上均优于Agent Workflow Memory这一基线方法。
  article_id: c69affdc82d44b2a
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Automata from Agent Traces: Failure and Next-Step Prediction

View PDF HTML (experimental)Abstract:LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.