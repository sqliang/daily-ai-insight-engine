---
title: A survey detection channel overrides the pixels in an astronomical foundation
  model, and biases tomographic mean redshifts
source: https://arxiv.org/abs/2608.23626
author:
- '[[Ihor Kendiukhov]]'
published: '2026-08-26'
created: '2026-08-26'
manifest_dates:
- '2026-08-26'
- '2026-08-27'
description: 'arXiv:2608.23626v1 Announce Type: new Abstract: Foundation models for
  astronomy are trained on survey pixels together with the catalogue products derived
  from those pixels. Those catalogues are incomplete at a measurable rate, and a model
  trained on both inherits that incompleteness as a systematic. We audit AION-1, a
  39-modality transformer trained on more than 200 million objects, using causal interventions
  on its inputs. Holding the image tokens byte-identical and editing only the survey
  segmentation map changes every quantity the model reports -- flux, size, ellipticity,
  redshift -- by 110-4400 times a matched placebo. The mechanism is detection gating,
  presence at the field centre (r = 0.47), not the light the mask encloses (r = 0.30);
  across 322 real blends the model ignores how the pipeline partitioned the light
  (R = -0.006). Nor is the preference specific to that channel: contradicted catalogue
  photometry leaves the model nine times worse than supplying no metadata at all.
  The Legacy Survey pipeline leaves 3.68% of targets with no segment covering their
  position. Propagating that rate, with a miss represented by the fields the pipeline
  actually returns, shifts tomographic mean redshifts by a median 0.71 times the LSST
  DESC requirement over 40 assignments and exceeds it in 12; observed positional errors
  take the worst bin to 8.3 times. Drawing the misses by their measured magnitude
  dependence rather than uniformly does not change it. Spectroscopy removes the effect,
  withholding the detection channel removes it at no measurable cost, and the effect
  grows with model scale. Two further limits lie in the tokeniser: its image codec
  resolves 28 effective states on source patches against 934 for the spectrum codec,
  and the redshift readout is quantisation-limited. Sparse dictionaries are unreliable
  causal handles: across 15, recovery spans 26-75% and moves up to 18 points on the
  seed alone.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3fcba86f0c2cae9d
source_type: academic_paper
tldr: 一篇 arXiv 论文审计天文学基础模型 AION-1，发现它主要依赖巡天检测通道而非图像像素输出结果：仅编辑分割图就让流量、红移等所有量变化 110-4400
  倍。该系统性偏差会以 Legacy Survey 缺失率传播，使断层扫描平均红移偏移中位数达 LSST DESC 要求的 0.71 倍；光谱或移除检测通道可消除。
objective_summary: 该论文审计了 AION-1，一个基于超过 2 亿天体对象训练的 39 模态天文学 transformer 基础模型。因果干预显示，保持图像
  token 不变、仅编辑巡天分割图，模型报告的流量、大小、椭圆率和红移即变化 110 到 4400 倍，机制是检测门控而非像素光。Legacy Survey 流水线有
  3.68% 的天体无分割覆盖，传播该缺失率使断层扫描平均红移偏移中位数达 LSST DESC 要求的 0.71 倍，最差分箱达 8.3 倍。提供矛盾星表测光比不提供任何元数据差
  9 倍；光谱可消除该效应，且效应随模型规模增大而增强。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - Legacy Survey
  - LSST DESC
  technologies:
  - foundation model
  - transformer
  - causal intervention
  - detection gating
  - tomographic mean redshifts
  - spectroscopy
  key_people: []
key_logic_flow:
- 论文审计了 AION-1 天文学基础模型，这是一个基于超过 2 亿天体对象训练的 39 模态 transformer，模型同时使用了巡天像素及其派生的星表产品。
- 因果干预实验表明，保持图像 token 逐字节不变、仅编辑巡天分割图，模型报告的流量、大小、椭圆率和红移就会以 110 到 4400 倍于安慰剂对照的幅度发生变化。
- 模型偏向的机制是检测门控，即天体是否出现在视场中心（r=0.47），而非掩膜包围的光量（r=0.30）；面对 322 个真实混合天体时，模型完全忽略流水线如何划分光（R=-0.006）。
- 提供被矛盾的星表测光会使模型表现比完全不提供元数据差 9 倍，说明模型过度信任检测通道而忽略图像证据。
- Legacy Survey 流水线有 3.68% 的天体没有分割覆盖，按该缺失率传播后，断层扫描平均红移的偏移中位数达到 LSST DESC 要求的 0.71
  倍，并在 12 次分配中超过要求，最差分箱达 8.3 倍。
- 光谱数据可消除该效应，去除检测通道可在无可测代价下消除它，且效应随模型规模增大而增强；此外图像编码器在源补丁上只解析出 28 个有效状态（光谱编码器为 934），红移读出受量化限制。
object_mentions:
- object_type: model
  name: AION-1
  canonical_name: AION-1
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文审计了 AION-1，这是一个在超过 2 亿天体对象上训练的 39 模态天文学 transformer 基础模型。
  - 对 AION-1 的因果干预显示，保持图像 token 逐字节不变、仅编辑巡天分割图，就使模型报告的所有物理量产生 110 到 4400 倍于安慰剂的变化。
  article_id: 3fcba86f0c2cae9d
- object_type: project
  name: Legacy Survey
  canonical_name: Legacy Survey
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Legacy Survey 流水线有 3.68% 的目标天体没有任何分割覆盖其位置，论文将该缺失率传播到红移测量中以评估系统性偏移。
  article_id: 3fcba86f0c2cae9d
- object_type: project
  name: LSST DESC
  canonical_name: LSST DESC
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 传播 Legacy Survey 缺失率后，断层扫描平均红移的偏移中位数达到 LSST DESC 要求的 0.71 倍，并在 12 次分配中超过该要求。
  article_id: 3fcba86f0c2cae9d
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:A survey detection channel overrides the pixels in an astronomical foundation model, and biases tomographic mean redshifts

View PDF HTML (experimental)Abstract:Foundation models for astronomy are trained on survey pixels together with the catalogue products derived from those pixels. Those catalogues are incomplete at a measurable rate, and a model trained on both inherits that incompleteness as a systematic. We audit AION-1, a 39-modality transformer trained on more than 200 million objects, using causal interventions on its inputs.

Holding the image tokens byte-identical and editing only the survey segmentation map changes every quantity the model reports -- flux, size, ellipticity, redshift -- by 110-4400 times a matched placebo. The mechanism is detection gating, presence at the field centre (r = 0.47), not the light the mask encloses (r = 0.30); across 322 real blends the model ignores how the pipeline partitioned the light (R = -0.006). Nor is the preference specific to that channel: contradicted catalogue photometry leaves the model nine times worse than supplying no metadata at all.

The Legacy Survey pipeline leaves 3.68% of targets with no segment covering their position. Propagating that rate, with a miss represented by the fields the pipeline actually returns, shifts tomographic mean redshifts by a median 0.71 times the LSST DESC requirement over 40 assignments and exceeds it in 12; observed positional errors take the worst bin to 8.3 times. Drawing the misses by their measured magnitude dependence rather than uniformly does not change it. Spectroscopy removes the effect, withholding the detection channel removes it at no measurable cost, and the effect grows with model scale.

Two further limits lie in the tokeniser: its image codec resolves 28 effective states on source patches against 934 for the spectrum codec, and the redshift readout is quantisation-limited. Sparse dictionaries are unreliable causal handles: across 15, recovery spans 26-75% and moves up to 18 points on the seed alone.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.