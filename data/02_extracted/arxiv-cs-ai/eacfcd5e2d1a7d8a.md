---
title: Improving scDiffusion with Sparsity-Biased Classifier-Free Guidance
source: https://arxiv.org/abs/2607.29043
author:
- '[[Yu Song, Hao Sun, Ikuko Nishikawa, Yen-Wei Chen]]'
published: '2026-08-04'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: eacfcd5e2d1a7d8a
source_type: academic_paper
tldr: 论文提出稀疏偏置无分类器引导（SB-CFG）策略改进 scDiffusion 的 scRNA-seq 数据生成。SB-CFG 用刻意稀疏、不含基因身份信息的参考作为无条件分支，放大条件与无条件预测的对比。在五个公开数据集上，其在标记基因保真度、细胞类型一致性和稀疏性保持上均优于标准
  CFG。
objective_summary: 《Improving scDiffusion with Sparsity-Biased Classifier-Free Guidance》论文发表于
  arXiv，提出稀疏偏置无分类器引导（SB-CFG）用于单细胞 RNA 测序（scRNA-seq）条件生成。现有分类器引导与无分类器引导依赖近似真实边缘分布的无条件分支，可能保留基因特异结构并限制引导效果。SB-CFG
  以刻意信息不足的稀疏参考替代中性的无条件分支，仅保留粗略稀疏统计并去除基因身份，从而放大条件与无条件预测的对比。作者在五个公开 scRNA-seq 数据集上以免训练采样修改的方式评估，结果显示其在标记基因表达保真度、细胞类型一致性和稀疏性保持方面一致优于标准
  CFG。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - scDiffusion
  - SB-CFG
  - classifier-free guidance
  - classifier guidance
  - diffusion models
  - scRNA-seq
  key_people: []
key_logic_flow:
- 单细胞 RNA 测序（scRNA-seq）是现代细胞生物学的重要工具，生成高质量的合成 scRNA-seq 数据日益重要。
- 现有扩散模型的条件生成引导策略（分类器引导和无分类器引导）依赖一个近似真实边缘分布的无条件分支，可能保留大量基因特异结构，从而限制引导效果。
- 论文提出稀疏偏置无分类器引导（SB-CFG），用刻意信息不足的稀疏参考作为无条件分支，去除基因身份而只保留粗略的稀疏统计。
- 这种刻意劣化的参考放大了条件与无条件预测之间的对比，使采样过程中产生更强、更有效的引导。
- SB-CFG 作为免训练的采样修改在五个公开 scRNA-seq 数据集上被评估，结果显示其在标记基因表达保真度、细胞类型一致性和稀疏性保持方面一致优于标准 CFG。
object_mentions:
- object_type: paper
  name: Improving scDiffusion with Sparsity-Biased Classifier-Free Guidance
  canonical_name: Improving scDiffusion with Sparsity-Biased Classifier-Free Guidance
  url: https://arxiv.org/abs/2607.29043
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文在 arXiv 发表，提出一种用于 scRNA-seq 数据生成的稀疏偏置无分类器引导（SB-CFG）策略。
  - 论文在五个公开 scRNA-seq 数据集上评估 SB-CFG，结果显示其在标记基因表达保真度、细胞类型一致性和稀疏性保持方面一致优于标准 CFG。
  article_id: eacfcd5e2d1a7d8a
- object_type: model
  name: scDiffusion
  canonical_name: scDiffusion
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 论文标题明确针对 scDiffusion 模型提出改进，说明该模型是条件 scRNA-seq 生成中采用的扩散模型。
  article_id: eacfcd5e2d1a7d8a
extract_result: success
---

# Quantitative Biology > Genomics

# Title:Improving scDiffusion with Sparsity-Biased Classifier-Free Guidance

View PDF HTML (experimental)Abstract:Single-cell RNA sequencing (scRNA-seq) has become an essential tool in modern cellular biology, and generating accurate synthetic scRNA-seq data is becoming increasingly important. Although diffusion models have achieved promising results in conditional scRNA-seq generation, existing guidance strategies, including classifier guidance and classifier-free guidance (CFG), rely on an unconditional branch trained to approximate the true marginal distribution, which may retain substantial gene-specific structure and limit guidance effectiveness. Inspired by recent work showing that diffusion models can be effectively guided using intentionally degraded references, we propose a sparsity-biased classifier-free guidance (SB-CFG) strategy for scRNA-seq generation. Rather than approximating the assumed "neutral" marginal distribution, SB-CFG introduces a deliberately under-informative sparse reference for the unconditional branch, removing gene identity while preserving only coarse sparsity statistics. This "bad" reference amplifies the contrast between conditional and unconditional predictions, leading to stronger and more effective guidance during sampling. We evaluated SB-CFG as a training-free sampling modification on five publicly available scRNA-seq datasets. Experimental results demonstrate consistent improvements over standard CFG-based sampling in terms of marker gene expression fidelity, cell-type consistency, and sparsity preservation, indicating that SB-CFG better captures biologically meaningful gene expression patterns.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.