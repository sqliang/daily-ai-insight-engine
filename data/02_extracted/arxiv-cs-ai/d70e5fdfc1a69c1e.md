---
title: 'Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled
  Beam Arbitration for Strict Zero-Shot Image Captioning'
source: https://arxiv.org/abs/2607.28986
author:
- '[[Duy Tran Thanh, Thien-Phuc Doan, Long Nguyen-Vu, Ngo Tan Vu Khanh]]'
published: '2026-08-04'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d70e5fdfc1a69c1e
source_type: academic_paper
tldr: Adjudicated Captioning 是面向严格零样本图像描述的新框架，在不变更 IFCap 生成器的前提下，通过多智能体对齐评分与共识蒸馏波束仲裁，在
  COCO Karpathy 上将 CIDEr 从 108.0 提升至 117.6，并无需重训即可迁移到 Flickr30k 与 NoCaps。
objective_summary: 该论文提出 Adjudicated Captioning，一个推理期多智能体框架，针对零样本图像描述在解码阶段缺乏视觉接地反馈、自
  2024 年以来进展停滞的问题。方法在输入端安装更强的冻结检索编码器，在检索与解码之间插入冻结交叉注意力验证器将 top-9 重排为 top-5，并在输出波束端挂载由
  TriFuse 多层感知机与 MemAttend 记忆注意力 Transformer 组成的学习型重排器，通过 Borda 共识蒸馏自监督训练。在 COCO Karpathy
  基准上达到 CIDEr 117.6 与 SPICE 21.9，较基线 IFCap 提升 9.6 CIDEr，并领先最强合成图像增强方法 NES 达 7.7 个点；该方案无需重训描述器即可迁移到
  Flickr30k 与 NoCaps。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Zero-shot Image Captioning (ZIC)
  - IFCap
  - TriFuse
  - MemAttend
  - CIDEr
  - SPICE
  - Borda Consensus Distillation
  - Cross-Attention Verifier
  key_people: []
key_logic_flow:
- 现有检索增强的零样本图像描述方法只在检索时进行一次图文对齐评分，解码仅依赖语言模型概率，缺少后续视觉接地反馈，导致自 2024 年以来该领域无方法取得严格基准上的进展。
- Adjudicated Captioning 提出推理期多智能体框架，在输入、检索与解码之间、输出波束三个检查点恢复视觉接地反馈，且不改动原有 IFCap 生成器。
- 输入端安装更强的冻结检索编码器，检索与解码之间插入冻结交叉注意力验证器，将 top-9 检索结果重排为 top-5，输出波束端挂载学习型重排器。
- 学习型重排器由多层感知机 TriFuse 与记忆注意力 Transformer MemAttend 组成，通过三个冻结评分器的 Borda 共识蒸馏以自监督方式训练，不使用配对图文标签或参考描述。
- 在 COCO Karpathy 上达到 CIDEr 117.6 与 SPICE 21.9，较 IFCap 的 108.0 与 20.3 提升 9.6 CIDEr，并比最强合成图像增强方法
  NES 的 109.9 高出 7.7 个点。
- 无训练的固定融合基线达到 115.8 CIDEr，说明 9.6 的提升中 7.8 来自非学习架构干预、剩余 1.8 来自学习型重排器；方案无需重训描述器即在 Flickr30k
  提升 8.1 CIDEr、在 NoCaps 提升 5.7。
object_mentions:
- object_type: paper
  name: Adjudicated Captioning
  canonical_name: Adjudicated Captioning
  url: https://arxiv.org/abs/2607.28986
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 Adjudicated Captioning，一个推理期多智能体框架，在不变更 IFCap 生成器的情况下于输入、检索与解码之间和输出波束三个检查点恢复视觉接地反馈。
  - 该框架在 COCO Karpathy 基准上达到 CIDEr 117.6 与 SPICE 21.9，较 IFCap 提升 9.6 CIDEr，并领先最强合成图像增强方法
    NES 达 7.7 个点。
  article_id: d70e5fdfc1a69c1e
- object_type: model
  name: IFCap
  canonical_name: IFCap
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 框架在不变更 IFCap 生成器的前提下，将其在 COCO Karpathy 上的 CIDEr 从 108.0 提升到 117.6，SPICE 从 20.3
    提升到 21.9。
  article_id: d70e5fdfc1a69c1e
- object_type: model
  name: NES
  canonical_name: NES
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - NES 是最强的合成图像增强方法，在 COCO Karpathy 上取得 CIDEr 109.9，而 Adjudicated Captioning 以 117.6
    领先其 7.7 个点。
  article_id: d70e5fdfc1a69c1e
- object_type: model
  name: TriFuse
  canonical_name: TriFuse
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - 输出波束端挂载的学习型重排器包含多层感知机 TriFuse，它与 MemAttend 记忆注意力 Transformer 共同构成该管道中仅有的学习组件。
  article_id: d70e5fdfc1a69c1e
- object_type: model
  name: MemAttend
  canonical_name: MemAttend
  url: null
  confidence: low
  article_role: ecosystem_context
  evidence_snippets:
  - 学习型重排器由 TriFuse 与 MemAttend 组成，两者通过三个冻结评分器的 Borda 共识蒸馏以自监督方式训练，不使用配对图文标签或参考描述。
  article_id: d70e5fdfc1a69c1e
extract_result: success
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:Adjudicated Captioning: Multi-Agent Alignment Scoring and Consensus-Distilled Beam Arbitration for Strict Zero-Shot Image Captioning

View PDF HTML (experimental)Abstract:Zero-shot image captioning (ZIC) describes images without paired image-caption supervision during captioner training, relying on text-only corpora and frozen pretrained image-text scorers. Existing retrieval-augmented methods score image-text alignment once, at retrieval, then commit the captioner's autoregressive beam under language-model probability alone, leaving the decoder without further visual grounding feedback. Progress has stalled, with no method improving on the strict-regime best since 2024.

We propose Adjudicated Captioning, an inference-time multi-agent framework that restores grounding feedback at multiple checkpoints over an unchanged IFCap captioner. First, we install a stronger frozen Retrieval Encoder at the input. Second, between retrieval and decoding we insert a frozen Cross-Attention Verifier that re-ranks the top-9 retrievals to top-5. Third, at the output beam we attach a learned Reranker pairing TriFuse, a multilayer perceptron, with MemAttend, a memory-attended transformer, the pipeline's only learned components; both are trained self-supervised by Borda-consensus distillation across the three frozen scorers, using no paired image-caption labels and no reference captions.

Under the inductive headline protocol, with rerankers fit on the disjoint COCO Karpathy validation beam and applied frozen to test, the framework reaches CIDEr 117.6 and SPICE 21.9 on COCO Karpathy, up from 108.0 and 20.3 for IFCap, a +9.6 CIDEr gain, and +7.7 above NES, the strongest synthetic-image-augmented method at 109.9, without retraining the captioner. A training-free fixed-fusion baseline reaches 115.8 CIDEr, so +7.8 of the +9.6 gain comes from the non-learned architectural intervention and the remaining +1.8 from the learned rerankers. The same recipe transfers off-COCO without captioner retraining: +8.1 CIDEr on Flickr30k Karpathy and +5.7 on NoCaps overall.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.