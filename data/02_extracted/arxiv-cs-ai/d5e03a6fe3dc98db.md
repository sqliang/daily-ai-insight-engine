---
title: Scaling Scientific Discovery Environments for Turn-Level Agentic RL
source: https://arxiv.org/abs/2607.28990
author:
- '[[Yucheng Xu, Keyi Zhang, Yuyang Yu, Min Zhang, Shiyuan Meng, Pei Chu, Zhongying
  Tu]]'
published: '2026-08-04'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d5e03a6fe3dc98db
source_type: academic_paper
tldr: 论文提出 SciDisco 框架，通过 SciThèque 环境编译、DAG 轨迹合成与 DiscoPO 训练，为科学发现智能体构建过程可验证的强化学习环境，实验表明
  SciDisco-14B 在假设驱动的科学数据分析基准上达到当前最优水平。
objective_summary: 该论文针对大语言模型智能体在长期科学分析中缺乏过程监督环境的问题，提出 SciDisco 可扩展训练框架。SciThèque
  将假设、数据集、隐藏证据图与验证器编译为任务环境，使分析进展可在交互过程中被实时检查；DAG-grounded 轨迹合成利用这些环境构建经验证器过滤的多轮示范数据。DiscoPO
  将环境作为训练信号来源，为产生可验证分析证据的动作分配回合级信用。实验结果显示 SciDisco-14B 在假设驱动的科学数据分析基准上达到当前最优水平。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - SciDisco
  - SciThèque
  - DiscoPO
  - Agentic RL
  - DAG-grounded trajectory synthesis
  key_people: []
key_logic_flow:
- 论文指出，大语言模型智能体虽已在数据驱动的科学发现任务中展现能力，但长期科学分析受限于缺乏基于真实科学数据的过程监督环境。
- 论文提出 SciDisco，一个用于在过程可验证环境中训练科学发现智能体的可扩展框架。
- SciThèque 将假设、数据集、隐藏证据图和验证器编译为任务环境，使交互过程中的分析进展可以被实时检查。
- DAG-grounded 轨迹合成利用上述环境，构建经验证器过滤的多轮示范数据。
- DiscoPO 将环境作为训练信号来源，为产生可验证分析证据的动作分配回合级信用。
- 实验表明，SciDisco-14B 在假设驱动的科学数据分析基准上达到当前最优水平。
object_mentions:
- object_type: project
  name: SciDisco
  canonical_name: SciDisco
  url: https://arxiv.org/abs/2607.28990
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文引入 SciDisco，这是一个可扩展框架，用于在过程可验证的环境中训练科学发现智能体。
  article_id: d5e03a6fe3dc98db
- object_type: project
  name: SciThèque
  canonical_name: SciThèque
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - SciThèque 将假设、数据集、隐藏证据图和验证器编译为任务环境，使分析进展可在交互过程中被检查。
  article_id: d5e03a6fe3dc98db
- object_type: project
  name: DiscoPO
  canonical_name: DiscoPO
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - DiscoPO 将环境作为训练信号来源，为产生可验证分析证据的动作分配回合级信用。
  article_id: d5e03a6fe3dc98db
- object_type: model
  name: SciDisco-14B
  canonical_name: SciDisco-14B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 实验表明，SciDisco-14B 在假设驱动的科学数据分析基准上达到当前最优水平。
  article_id: d5e03a6fe3dc98db
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Scaling Scientific Discovery Environments for Turn-Level Agentic RL

View PDF HTML (experimental)Abstract:Large language model agents have shown promising capabilities in data-driven scientific discovery tasks, where an agent interacts with an execution environment and produces a statistical claim. Long-horizon scientific analysis remains constrained by the lack of process supervised environments over real-world scientific data. This paper introduces SciDisco, a scalable framework for training Scientific Discovery agents in process-verifiable environments. SciThèque compiles hypotheses, datasets, hidden evidence graphs, and verifiers into task environments where analytical progress can be checked during interaction. DAG-grounded trajectory synthesis uses these environments to construct verifier-filtered multi-turn demonstrations. DiscoPO then uses the environment as the source of training signal, assigning turn-level credit to actions that produce verifiable analytical evidence. Experiments show that SciDisco-14B reaches state-of-the-art on hypothesis-driven scientific data analysis benchmarks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.