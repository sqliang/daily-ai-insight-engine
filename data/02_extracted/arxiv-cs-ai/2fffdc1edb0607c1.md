---
title: Taming Outlier Tokens in Diffusion Transformers
source: https://arxiv.org/abs/2605.05206
author:
- '[[Xiaoyu Wu, Yifei Wang, Tsu-Jui Fu, Liang-Chieh Chen, Zhe Gan, Chen Wei]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.05206v1 Announce Type: cross Abstract: We study outlier tokens
  in Diffusion Transformers (DiTs) for image generation. Prior work has shown that
  Vision Transformers (ViTs) can produce a small number of high-norm tokens that attract
  disproportionate attention while carrying limited local information, but their role
  in generative models remains underexplored. We show that this phenomenon appears
  in both the encoder and denoiser of modern Representation Autoencoder (RAE)-DiT
  pipelines: pretrained ViT encoders can produce outlier representations, and DiTs
  themselves can develop internal outlier tokens, especially in intermediate layers.
  Moreover, simply masking high-norm tokens does not improve performance, indicating
  that the problem is not only caused by a few extreme values, but is more closely
  related to corrupted local patch semantics. To address this issue, we introduce
  Dual-Stage Registers (DSR), a register-based intervention for both components: trained
  registers when available, recursive test-time registers otherwise, and diffusion
  registers for the denoiser. Across ImageNet and large-scale text-to-image generation,
  these interventions consistently reduce outlier artifacts and improve generation
  quality. Our results highlight outlier-token control as an important ingredient
  in building stronger DiTs.'
tags:
- clippings
id: 2fffdc1edb0607c1
source_type: academic_paper
tldr: 研究Diffusion Transformer中的异常token问题，提出双阶段寄存器(DSR)方法改善生成质量。
objective_summary: 该论文研究了扩散变换器(DiT)在图像生成中的异常token现象，发现预训练ViT编码器和DiT去噪器均会产生高范数异常token。作者提出双阶段寄存器(DSR)方法，通过在编码器和去噪器中插入寄存器来减少异常伪影，在ImageNet和文本到图像生成任务中提升了生成质量。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Diffusion Transformer (DiT)
  - Vision Transformer (ViT)
  - Representation Autoencoder (RAE)
  - Dual-Stage Registers (DSR)
  - ImageNet
  key_people: []
key_logic_flow:
- 研究发现，在RAE-DiT图像生成流程中，预训练ViT编码器和DiT去噪器均会产生高范数异常token，且该现象在中间层尤为突出。
- 简单掩码掉高范数token并不能改善性能，表明问题不仅是少数极端值导致的，而是与局部patch语义损坏更为相关。
- 作者提出双阶段寄存器(DSR)方法，为编码器和去噪器分别设计了训练寄存器、测试时递归寄存器和扩散寄存器三种干预手段。
- 在ImageNet分类数据集和大规模文本到图像生成任务上的实验表明，DSR方法能持续减少异常伪影并提升生成质量。
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:Taming Outlier Tokens in Diffusion Transformers

View PDF HTML (experimental)Abstract:We study outlier tokens in Diffusion Transformers (DiTs) for image generation. Prior work has shown that Vision Transformers (ViTs) can produce a small number of high-norm tokens that attract disproportionate attention while carrying limited local information, but their role in generative models remains underexplored. We show that this phenomenon appears in both the encoder and denoiser of modern Representation Autoencoder (RAE)-DiT pipelines: pretrained ViT encoders can produce outlier representations, and DiTs themselves can develop internal outlier tokens, especially in intermediate layers. Moreover, simply masking high-norm tokens does not improve performance, indicating that the problem is not only caused by a few extreme values, but is more closely related to corrupted local patch semantics. To address this issue, we introduce Dual-Stage Registers (DSR), a register-based intervention for both components: trained registers when available, recursive test-time registers otherwise, and diffusion registers for the denoiser. Across ImageNet and large-scale text-to-image generation, these interventions consistently reduce outlier artifacts and improve generation quality. Our results highlight outlier-token control as an important ingredient in building stronger DiTs.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.