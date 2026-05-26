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
impact_score:
  score: 5.5
  reason: 该论文系统性地揭示了Diffusion Transformer中异常token问题存在于编码器和去噪器两个阶段，并提出了双阶段寄存器(DSR)干预方法。这一发现对提升DiT生成质量有实际价值，但属于渐进式改进而非范式级突破。论文基于已有的ViT异常token研究进行扩展，实验验证在ImageNet和文本到图像任务上有效，未展示跨模态或跨架构的通用性验证，影响力有限。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: DSR方法在更大规模模型和不同架构上的泛化能力及额外计算开销
hype_assessment:
  level: low
  reason: 该论文为学术论文，语言克制严谨，使用'improve'、'reduce artifacts'等中性表述，无'revolutionary'、'breakthrough'等PR词汇。实验部分提供了充分的消融研究和定量指标，未发现过度包装或概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 首次系统分析了DiT图像生成流程中异常token在预训练ViT编码器和DiT去噪器两个阶段的分布特性，并发现简单掩码高范数token无效，表明问题本质是局部patch语义损坏而非极端值干扰。提出双阶段寄存器(DSR)方法，涵盖训练时寄存器、测试时递归寄存器和扩散寄存器三种干预手段。
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: DSR方法本质上是DiT推理管线中的一项优化技术，解决的是生成质量中的异常token伪影问题，而非底层架构的颠覆性突破。其价值在于：①作为开源方法论，可被任何DiT项目低成本集成，具有横向复用的潜力；②双阶段设计（编码器+去噪器）覆盖了完整管线，不是单点修补；③但该方法高度依赖DiT架构（尤其是RAE-DiT范式），如果未来视觉生成转向非Transformer架构（如Mamba、RWKV等），其适用性将大幅缩水。综合来看，这是一个有机构建基础组件价值的改进，但受限于架构绑定，长期复合效应中等，5-10分制下给予5.5分。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Stability AI
- OpenAI
- Midjourney
competitive_casualty:
- 拥有专有图像质量优化技术的闭源模型厂商
- 依赖ViT编码器但尚未解决异常token问题的中小型生成模型团队
market_opportunities:
- 基于DSR双阶段寄存器方法可显著提升DiT文生图模型的输出质量，商业图像生成平台可将其集成到现有管线中以增强产品竞争力
- 异常token检测与控制可作为AI生成内容质量控制的新维度，衍生出面向生成模型生产环境的诊断、监控与修复工具链
- 寄存器机制为DiT架构优化开辟了新方向，技术团队可基于此开发面向特定垂直领域（如医学影像、设计辅助）的微调与部署方案
risk_matrix:
  regulatory: 无
  technological: DSR方法尚未在大规模多样化数据集和更宽模型族上得到充分验证，存在被后续更优方案（如架构级而非补丁级修复）替代的风险；论文自身指出简单掩码高范数token无效，表明对异常根源的理解仍不完整
  competitive: 开源社区可能快速复现并迭代DSR方法，导致早期投入者的技术差异化优势被快速摊薄；头部厂商（如OpenAI、Stability AI）内部可能已有类似或更成熟的解决方案，形成生态挤压
  ethical: 图像生成质量的持续提升可被滥用于制造高度逼真的深度伪造内容，加剧虚假信息、版权侵权和欺诈风险；异常token的消除可能使AI生成图像更难被检测工具识别
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
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