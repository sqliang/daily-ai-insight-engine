---
title: Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models
source: https://arxiv.org/abs/2605.05026
author:
- '[[Bartlomiej Sobieski, Matthew Tivnan, Dawid P{\l}udowski, Micha{\l} Jan W{\l}odarczyk,
  Pengfei Jin, Przemyslaw Biecek, Quanzheng Li]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05026v1 Announce Type: cross Abstract: Diffusion models are
  prone to generating structural hallucinations - samples that match the statistical
  properties of the training data yet defy underlying structural rules, resulting
  in anomalies like hands with more than five fingers. Recent research studied this
  failure mode from several viewpoints, offering partial explanations to their occurrence,
  such as mode interpolation. In this work, we propose a complementary perspective
  that treats hallucinations as instabilities on the model-induced manifold. We begin
  by showing that a hallucination filter based on such instabilities matches or exceeds
  the performance of the recently proposed temporal one. By tracing the source of
  these instabilities, we identify local intrinsic dimension (LID) as their primary
  driver and propose Intrinsic Quenching (IQ), a direct corrective mechanism that
  deflates it to alleviate hallucinations. IQ consistently outperforms standard hallucination
  reduction baselines across a wide array of benchmarks and offers a highly promising
  solution for enforcing anatomical consistency in downstream medical imaging tasks.'
tags:
- clippings
id: e6aa1724f27feffb
source_type: academic_paper
tldr: 研究发现局部本征维度(LID)是扩散模型产生幻觉的根源，并提出Intrinsic Quenching(IQ)机制来消除幻觉。
objective_summary: 该学术论文提出一种新视角，将扩散模型的结构性幻觉视为模型诱导流形上的不稳定性。研究团队证明基于这种不稳定性的幻觉检测方法优于或持平于现有的时间维度方法，并发现局部本征维度(LID)是导致不稳定性的主要因素。他们提出Intrinsic
  Quenching(IQ)修正机制，通过降低LID来缓解幻觉，
event_type: infrastructure_update
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Diffusion Models
  - Local Intrinsic Dimension (LID)
  - Intrinsic Quenching (IQ)
  key_people: []
key_logic_flow:
- 扩散模型容易生成结构性幻觉，即样本符合训练数据的统计特征但违反底层结构规则（如生成六指手掌）。
- 已有研究从模式插值等角度给出了部分解释，但该论文提出将幻觉视为模型诱导流形上的不稳定性这一互补视角。
- 基于该不稳定性构建的幻觉检测过滤器，其性能匹配或超过近期提出的基于时间维度的幻觉检测方法。
- 通过追溯不稳定性的来源，论文发现局部本征维度(LID)是导致幻觉的主要驱动因素。
- 论文提出Intrinsic Quenching(IQ)机制，通过抑制LID来直接修正幻觉问题。
- IQ在多个基准测试中一致优于现有的幻觉消减基线方法，并在下游医学影像任务中展现出强制解剖一致性的潜力。
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:Local Intrinsic Dimension Unveils Hallucinations in Diffusion Models

View PDF HTML (experimental)Abstract:Diffusion models are prone to generating structural hallucinations - samples that match the statistical properties of the training data yet defy underlying structural rules, resulting in anomalies like hands with more than five fingers. Recent research studied this failure mode from several viewpoints, offering partial explanations to their occurrence, such as mode interpolation. In this work, we propose a complementary perspective that treats hallucinations as instabilities on the model-induced manifold. We begin by showing that a hallucination filter based on such instabilities matches or exceeds the performance of the recently proposed temporal one. By tracing the source of these instabilities, we identify local intrinsic dimension (LID) as their primary driver and propose Intrinsic Quenching (IQ), a direct corrective mechanism that deflates it to alleviate hallucinations. IQ consistently outperforms standard hallucination reduction baselines across a wide array of benchmarks and offers a highly promising solution for enforcing anatomical consistency in downstream medical imaging tasks.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.