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