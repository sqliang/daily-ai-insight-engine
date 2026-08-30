---
title: No Universal Signal Predicts Sample-Level LLM Regression under Version Updates
source: https://arxiv.org/abs/2608.13607
author:
- '[[Jia Sheng, Yiwei Lu]]'
published: '2026-08-17'
created: '2026-08-17'
manifest_dates:
- '2026-08-17'
description: 'arXiv:2608.13607v1 Announce Type: new Abstract: Frontier LLMs are updated
  frequently and typically outperform their predecessors in aggregate. But aggregate
  gains say little about individual samples: an update can still cause sample-level
  regression, where a response correct under the old model becomes incorrect under
  the new one. This paper studies how to predict such regressions from signals available
  at inference time. We compare single-model signals (confidence, logit margin, attention
  entropy) against cross-version signals (output KL divergence, likelihood drift,
  token-level KL, representation drift) under a unified added-value test that isolates
  each signal''s gain over a confidence baseline. Across six benchmarks in three task
  families (multiple-choice question answering, or MCQ; math reasoning; code generation)
  and six model update pairs, we find that (1) signal effectiveness is task-dependent:
  confidence is strongest on MCQ and simpler math, while likelihood/KL signals give
  the most frequent gains on harder math and code; (2) no signal is universally best
  across model updates either; and (3) some cross-version signals stay informative
  even when confidence fails, including without labels, which supports a proof-of-concept
  selective fallback that routes high-risk samples back to the old model. Practitioners
  can use these task-level patterns to choose which regression signal to trust for
  a given update. Code is available at https://github.com/jiashengsally/llm-regression-signals.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c29d9def35f8de4c
source_type: academic_paper
tldr: 该论文研究大语言模型版本更新引发的样本级回归问题。对比六项基准上单模型与跨版本信号后发现，没有信号普遍最优，但部分跨版本信号在置信度失效时仍有效，可支撑将高风险样本回退到旧模型的选择性方案。
objective_summary: 这篇 arXiv 论文研究如何预测前沿大语言模型在版本更新后出现的样本级回归，即旧模型回答正确而新模型回答错误的样本。研究者在六项基准、三类任务（多项选择问答、数学推理、代码生成）和六组模型更新对上，用统一增值测试比较单模型信号（置信度、logit
  边际、注意力熵）与跨版本信号（输出 KL 散度、似然漂移、token 级 KL、表征漂移）相对置信度基线的增益。结果发现信号有效性因任务而异，置信度在多项选择和简单数学上最强，似然与
  KL 信号在更难的数学和代码上增益更频繁，且没有任何信号在所有模型更新上普遍最优。部分跨版本信号在置信度失效时仍具信息量且无需标签，支撑了将高风险样本路由回旧模型的概念验证方案，代码已公开。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - MCQ
  - logit margin
  - attention entropy
  - KL divergence
  - representation drift
  key_people: []
key_logic_flow:
- 论文研究了前沿大语言模型在版本更新时出现的样本级回归现象，即新模型在原本正确的样本上给出错误回答。
- 作者比较了单模型信号（置信度、logit 边际、注意力熵）与跨版本信号（输出 KL 散度、似然漂移、token 级 KL、表征漂移）对回归的预测能力。
- 实验在六项基准、三类任务（多项选择问答、数学推理、代码生成）和六组模型更新对上展开，用统一增值测试隔离每种信号相对置信度基线的增益。
- 结果显示信号有效性因任务而异：置信度在多项选择和简单数学上最强，似然与 KL 类信号在更难的数学和代码任务上增益更频繁。
- 没有任何单一信号在所有模型更新上普遍最优，部分跨版本信号在置信度失效时仍保持信息量，且无需标签。
- 作者据此提出概念验证的选择性回退方案，将高风险样本路由回旧模型，并已公开相关代码。
object_mentions:
- object_type: paper
  name: No Universal Signal Predicts Sample-Level LLM Regression under Version Updates
  canonical_name: No Universal Signal Predicts Sample-Level LLM Regression under Version
    Updates
  url: https://arxiv.org/abs/2608.13607
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文发表于 arXiv，编号为 2608.13607，研究大语言模型版本更新导致的样本级回归预测问题。
  - 论文对比了单模型信号与跨版本信号在六项基准、三类任务和六组模型更新上的预测能力，发现没有信号普遍最优。
  - 研究发现部分跨版本信号在置信度失效时仍具信息量，并提出了将高风险样本路由回旧模型的选择性回退方案，代码已公开。
  article_id: c29d9def35f8de4c
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:No Universal Signal Predicts Sample-Level LLM Regression under Version Updates

View PDF HTML (experimental)Abstract:Frontier LLMs are updated frequently and typically outperform their predecessors in aggregate. But aggregate gains say little about individual samples: an update can still cause sample-level regression, where a response correct under the old model becomes incorrect under the new one. This paper studies how to predict such regressions from signals available at inference time. We compare single-model signals (confidence, logit margin, attention entropy) against cross-version signals (output KL divergence, likelihood drift, token-level KL, representation drift) under a unified added-value test that isolates each signal's gain over a confidence baseline. Across six benchmarks in three task families (multiple-choice question answering, or MCQ; math reasoning; code generation) and six model update pairs, we find that (1) signal effectiveness is task-dependent: confidence is strongest on MCQ and simpler math, while likelihood/KL signals give the most frequent gains on harder math and code; (2) no signal is universally best across model updates either; and (3) some cross-version signals stay informative even when confidence fails, including without labels, which supports a proof-of-concept selective fallback that routes high-risk samples back to the old model. Practitioners can use these task-level patterns to choose which regression signal to trust for a given update. Code is available at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.