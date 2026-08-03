---
title: 'RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge
  Injection'
source: https://arxiv.org/abs/2607.24771
author:
- '[[Yan Hong, Wei Li, Kedong Xiu, Jun Lan, Shuheng Zhou, Zhongcai Lyu, Huijia Zhu,
  Weiqiang Wang, Jianfu Zhang]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24771v1 Announce Type: new Abstract: Knowledge injection
  updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting
  full authoritative answers can cause drift in non-updated behavior. Online distillation
  mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned
  distillation provides coarse supervision: it can under-emphasize reference-supported
  rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE,
  a rollout-conditioned online distillation objective for knowledge injection. RoCo
  uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate
  additional distillation weight to reference-supported rollout tokens, while ACE
  adds sparse reference-side anchored correction for authoritative anchors omitted
  from the rollout without full-answer imitation. Across three knowledge-injection
  settings, six retention benchmarks, multiple baselines, and multiple base models,
  RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while
  keeping evaluated retention close to the base model.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cad91fd0607cafa5
source_type: academic_paper
tldr: RoCo-ACE 论文提出一种 rollout 条件在线蒸馏目标，用于向预训练多模态大模型注入新知识，在三种知识注入设置和六项保留基准上取得最佳注入准确率，同时保留性能接近基础模型。
objective_summary: 该 arXiv 论文提出 RoCo-ACE，一种面向知识注入的 rollout 条件在线蒸馏目标，用于向预训练多模态大模型（MLLM）注入新的事实或领域知识。方法由两部分组成：RoCo
  通过同 rollout 的参考无关与参考条件似然对比，为受参考支持的 rollout token 重新分配额外蒸馏权重；ACE 则为 rollout 中遗漏的权威锚点添加稀疏的参考侧锚定修正，避免完整答案模仿。实验覆盖三种知识注入设置、六项保留基准、多个基线模型与基础模型，结果显示
  RoCo-ACE 的注入知识准确率优于所有对比方法，且评估保留能力接近基础模型。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - RoCo-ACE
  - MLLM
  - online distillation
  - knowledge injection
  key_people: []
key_logic_flow:
- 知识注入以新事实或领域知识更新预训练多模态大模型，但直接拟合完整权威答案会导致非更新行为出现漂移。
- 在线蒸馏通过在模型自身生成的 rollout 上训练来缓解漂移，但统一的参考条件蒸馏监督较粗糙，会低估受参考支持的 token 并仅间接监督被遗漏的事实。
- RoCo 采用同 rollout 的参考无关与参考条件似然对比，为受参考支持的 rollout token 重新分配额外的蒸馏权重。
- ACE 增加稀疏的参考侧锚定修正，在不进行完整答案模仿的情况下处理 rollout 中遗漏的权威锚点。
- 实验在三种知识注入设置、六个保留基准、多个基线与基础模型上进行，RoCo-ACE 的注入知识准确率优于对比方法，保留性能接近基础模型。
object_mentions:
- object_type: paper
  name: RoCo-ACE
  canonical_name: RoCo-ACE
  url: https://arxiv.org/abs/2607.24771
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - RoCo-ACE 是一种面向知识注入的 rollout 条件在线蒸馏目标，用于用新事实或领域知识更新预训练多模态大模型。
  - 在三种知识注入设置、六项保留基准、多个基线与基础模型上，RoCo-ACE 取得了所有对比方法中最佳的注入知识准确率。
  article_id: cad91fd0607cafa5
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection

View PDF HTML (experimental)Abstract:Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior. Online distillation mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned distillation provides coarse supervision: it can under-emphasize reference-supported rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection. RoCo uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate additional distillation weight to reference-supported rollout tokens, while ACE adds sparse reference-side anchored correction for authoritative anchors omitted from the rollout without full-answer imitation. Across three knowledge-injection settings, six retention benchmarks, multiple baselines, and multiple base models, RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while keeping evaluated retention close to the base model.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.