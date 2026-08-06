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
pipeline_stage: ingested
id: eacfcd5e2d1a7d8a
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