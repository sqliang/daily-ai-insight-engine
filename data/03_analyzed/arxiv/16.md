---
title: A Foundation Model for Zero-Shot Logical Rule Induction
source: https://arxiv.org/abs/2605.04916
author:
- '[[Yin Jun Phua]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04916v1 Announce Type: new Abstract: Inductive Logic Programming
  (ILP) learns interpretable logical rules from data. Existing methods are transductive:
  their learned parameters are bound to specific predicates and require retraining
  for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for
  zero-shot rule induction. Rather than encoding literal identities, NRI represents
  literals using domain-agnostic statistical properties such as class-conditional
  rates, entropy, and co-occurrence, which generalize across variable identities and
  counts without retraining. The model consists of a statistical encoder and a parallel
  slot-based decoder. Parallel decoding preserves the permutation invariance of logical
  disjunction; an autoregressive decoder would instead impose an arbitrary clause
  order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end
  training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness
  to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks,
  and we believe this work opens up the possibility of foundation models for symbolic
  reasoning. Code and the reference checkpoint are available at https://github.com/phuayj/neural-rule-inducer.'
tags:
- clippings
id: d2b0e38ffa61cc0f
source_type: academic_paper
tldr: 提出 Neural Rule Inducer (NRI) 模型，首次实现零样本逻辑规则归纳，无需针对新任务重新训练。
objective_summary: 论文提出 Neural Rule Inducer (NRI)，一种用于零样本规则归纳的预训练模型。NRI 用统计编码器表示文字的统计属性（如类条件概率、熵、共现率），替代传统
  ILP 中绑定于具体谓词的参数；采用并行槽位解码器保持逻辑析取的置换不变性，并通过 Product T-norm
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Inductive Logic Programming (ILP)
  - Neural Rule Inducer (NRI)
  - Product T-norm
  key_people: []
key_logic_flow:
- 传统归纳逻辑编程（ILP）是转导式的，其学习参数绑定于特定谓词，每遇到新任务都需要重新训练。
- NRI 不编码文字的字面标识，而是使用域无关的统计属性（类条件概率、熵、共现率）来表示文字，这些属性在不同任务间可泛化。
- 模型由统计编码器和并行槽位解码器组成；并行解码保持了逻辑析取的置换不变性，而自回归解码器会强加任意子句顺序。
- 通过 Product T-norm 松弛使规则执行过程可微分，从而可以仅基于预测准确率进行端到端训练。
- 实验评估了 NRI 在规则恢复、对标签噪声和虚假相关性的鲁棒性，以及在真实世界基准上的零样本迁移能力。
impact_score:
  score: 6.5
  reason: 该论文提出的 Neural Rule Inducer 首次实现了零样本逻辑规则归纳，通过统计属性替代谓词绑定参数，解决了传统 ILP 每任务需重新训练的核心瓶颈。这是一个有意义的学术贡献，结合了神经方法与符号推理，但尚处于研究验证阶段，实验基于基准数据集而非大规模生产场景，距离行业范式转移还有距离。评分
    6.5 分：改变了神经符号推理局部竞争格局，但未达到行业颠覆级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 零样本逻辑规则归纳是否真正可迁移到实际复杂任务
hype_assessment:
  level: medium
  reason: 论文标题使用了 'Foundation Model' 这一当前热门术语，有一定包装成分。但论文的技术贡献是真实的：统计编码器+并行槽位解码器+Product
    T-norm 松弛的组合有实质创新。实验包含消融研究和鲁棒性分析，并非空洞概念炒作，整体属于'有实质但包装略过度'。
information_entropy: high
domain_disruption:
  technical_innovation: 提出用域无关的统计属性（类条件概率、熵、共现率）替代传统 ILP 中绑定于具体谓词的参数表示，使规则归纳可在不同谓词集和谓词数量间零样本泛化；并行槽位解码器保持逻辑析取的置换不变性，避免了自回归解码强加的子句顺序偏差；Product
    T-norm 松弛使离散规则执行过程可微分，实现基于预测准确率的端到端训练。
  business_model: 无（纯学术论文，不涉及商业模式重塑）
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: NRI 提出了统计编码器+并行槽位解码器的全新架构范式，首次在归纳逻辑编程领域实现零样本迁移，打破了传统 ILP 每任务必重新训练的转导式局限。其核心创新在于用域无关的统计属性替代文字标识编码，使得规则归纳可在不同谓词集合间泛化——这是一个架构级别的突破。如果该方向被验证可规模化，有望成为神经符号推理的基础设施层，在可解释
    AI、合规审计、结构化推理等场景中产生长期复利效应。但需清醒认知：目前仅为单一学术论文（arXiv 预印本），缺乏大规模基准验证、真实场景鲁棒性测试及企业级背书。从学术成果到产业基础设施仍需跨越模型规模扩展、训练数据构建、工程化部署等多重鸿沟。现阶段不宜过度定价，建议持续跟踪后续扩展研究、开源社区采纳度及潜在产业合作动向。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- DeepMind
- OpenAI
- Anthropic
- Microsoft Research
competitive_casualty:
- 传统 ILP 工具体系
- 纯黑箱深度学习厂商
market_opportunities:
- 企业可基于NRI构建跨领域可迁移的规则归纳服务，在金融风控、医疗诊断、合规审计等需要可解释决策的场景中实现零样本规则提取，大幅降低每接入一个新客户所需的模型定制成本
- 数据分析平台可集成NRI作为"即时规则发现"功能，让非技术用户通过输入少量标注数据即可获得可读的逻辑规则，填补现有BI工具在可解释自动化洞察方面的空白
- AI安全审计工具可借助NRI的零样本规则归纳能力，自动从黑盒模型中提取逻辑规则用于行为对齐检测，形成模型可解释性合规的差异化卖点
risk_matrix:
  regulatory: 无（NRI生成的逻辑规则天然具有可解释性，反而有助于满足AI Act等法规对可解释AI的要求）
  technological: NRI依赖统计属性替代传统谓词绑定，在高度依赖罕见或长尾模式的任务上可能精度不足；另外符号推理与神经网络融合领域迭代迅速，后续更优架构（如结合LLM+符号推理）可能取代当前方案
  competitive: 传统ILP工具链已有多年生态积累（如Popper、ALEPH），且大语言模型在零样本规则生成方面也展现出潜力，NRI需要在效果和易用性上明显超越才可能获得市场采纳
  ethical: 自动归纳出的逻辑规则可能放大数据中的偏见（如从偏差数据中学到歧视性规则），且规则的可读性可能让偏见被包装成"客观逻辑"而难以被质疑
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:A Foundation Model for Zero-Shot Logical Rule Induction

View PDF HTML (experimental)Abstract:Inductive Logic Programming (ILP) learns interpretable logical rules from data. Existing methods are transductive: their learned parameters are bound to specific predicates and require retraining for each new task. We introduce Neural Rule Inducer (NRI), a pretrained model for zero-shot rule induction. Rather than encoding literal identities, NRI represents literals using domain-agnostic statistical properties such as class-conditional rates, entropy, and co-occurrence, which generalize across variable identities and counts without retraining. The model consists of a statistical encoder and a parallel slot-based decoder. Parallel decoding preserves the permutation invariance of logical disjunction; an autoregressive decoder would instead impose an arbitrary clause order. Product T-norm relaxation makes rule execution differentiable, allowing end-to-end training on prediction accuracy alone. We evaluate NRI on rule recovery, robustness to label noise and spurious correlations, and zero-shot transfer to real-world benchmarks, and we believe this work opens up the possibility of foundation models for symbolic reasoning. Code and the reference checkpoint are available at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.