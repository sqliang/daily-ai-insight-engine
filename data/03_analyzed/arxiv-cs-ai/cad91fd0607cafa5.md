---
title: 'RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge
  Injection'
source: https://arxiv.org/abs/2607.24771
author:
- '[[Yan Hong, Wei Li, Kedong Xiu, Jun Lan, Shuheng Zhou, Zhongcai Lyu, Huijia Zhu,
  Weiqiang Wang, Jianfu Zhang]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24771v1 Announce Type: new Abstract: Knowledge injection
  updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting
  full authoritative answers can cause drift in non-updated behavior. Online distillation
  mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned
  distillation provides coarse supervision: it can under-emphasize reference-supported
  rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE,
  a rollout-conditioned online distillation objective for knowledge injection. RoCo
  uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate
  additional distillation weight to reference-supported rollout tokens, while ACE
  adds sparse reference-side anchored correction for authoritative anchors omitted
  from the rollout without full-answer imitation. Across three knowledge-injection
  settings, six retention benchmarks, multiple baselines, and multiple base models,
  RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while
  keeping evaluated retention close to the base model.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cad91fd0607cafa5
source_type: academic_paper
tldr: RoCo-ACE 论文提出一种 rollout 条件在线蒸馏目标，用于向预训练多模态大模型注入新知识，在三种知识注入设置和六项保留基准上取得最佳注入准确率，同时保留性能接近基础模型。
objective_summary: 该 arXiv 论文提出 RoCo-ACE，一种面向知识注入的 rollout 条件在线蒸馏目标，用于向预训练多模态大模型（MLLM）注入新的事实或领域知识。方法由两部分组成：RoCo
  通过同 rollout 的参考无关与参考条件似然对比，为受参考支持的 rollout token 重新分配额外蒸馏权重；ACE 则为 rollout 中遗漏的权威锚点添加稀疏的参考侧锚定修正，避免完整答案模仿。实验覆盖三种知识注入设置、六项保留基准、多个基线模型与基础模型，结果显示
  RoCo-ACE 的注入知识准确率优于所有对比方法，且评估保留能力接近基础模型。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - RoCo-ACE
  - MLLM
  - online distillation
  - knowledge injection
  key_people: []
key_logic_flow:
- 知识注入以新事实或领域知识更新预训练多模态大模型，但直接拟合完整权威答案会导致非更新行为出现漂移。
- 在线蒸馏通过在模型自身生成的 rollout 上训练来缓解漂移，但统一的参考条件蒸馏监督较粗糙，会低估受参考支持的 token 并仅间接监督被遗漏的事实。
- RoCo 采用同 rollout 的参考无关与参考条件似然对比，为受参考支持的 rollout token 重新分配额外的蒸馏权重。
- ACE 增加稀疏的参考侧锚定修正，在不进行完整答案模仿的情况下处理 rollout 中遗漏的权威锚点。
- 实验在三种知识注入设置、六个保留基准、多个基线与基础模型上进行，RoCo-ACE 的注入知识准确率优于对比方法，保留性能接近基础模型。
object_mentions:
- object_type: paper
  name: RoCo-ACE
  canonical_name: RoCo-ACE
  url: https://arxiv.org/abs/2607.24771
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - RoCo-ACE 是一种面向知识注入的 rollout 条件在线蒸馏目标，用于用新事实或领域知识更新预训练多模态大模型。
  - 在三种知识注入设置、六项保留基准、多个基线与基础模型上，RoCo-ACE 取得了所有对比方法中最佳的注入知识准确率。
  article_id: cad91fd0607cafa5
extract_result: success
impact_score:
  score: 4.5
  reason: 评分依据：该论文是 arXiv 预印本，未经同行评审，且从内容看未见配套开源代码或产品化信息；方法本质是改进在线蒸馏的监督信号（RoCo 的 token
    级权重重分配 + ACE 的稀疏锚定修正），属于知识注入这一细分方向的增量学术优化，而非范式级突破。短期对行业竞争格局无直接影响，但为多模态大模型持续更新（避免灾难性漂移）提供了更细粒度的监督思路，对做模型迭代的研究团队有一定参考价值。综合判断为中等偏低冲击，评分
    4.5。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 在线蒸馏做知识注入时，注入准确率与原有能力保留之间的权衡能否在真实业务场景中复现
hype_assessment:
  level: low
  reason: 判定依据：论文全文使用克制的学术表述，未出现'颠覆''革命性''突破'等 PR 滥用词汇；实验设置系统完整（三种注入设置、六个保留基准、多个基线模型与基础模型），结论有实证支撑；作为
    arXiv 预印本无营销包装成分，故炒作指数低。
information_entropy: high
domain_disruption:
  technical_innovation: 提出 RoCo-ACE 在线蒸馏目标：RoCo 通过同 rollout 内参考无关与参考条件似然对比，动态为受参考支持的
    token 重新分配额外蒸馏权重，解决统一参考条件监督低估关键 token 的问题；ACE 以稀疏的参考侧锚定修正补足 rollout 中遗漏的权威锚点，在不做完整答案模仿的前提下强化事实锚定，为知识注入中'该学的新知识'与'该保留的既有行为'之间提供了更细粒度的监督信号。
  business_model: 潜在价值在于降低多模态大模型的持续知识更新成本——企业可借助在线蒸馏为预训练模型注入私有领域知识，而无需全量重训或大规模微调，对模型即服务（MaaS）的迭代节奏和私有化部署的更新模式有间接商业意义；但论文本身未涉及商业模式设计。
engineering_complexity: prototype
compound_value:
  score: 4.5
  reason: 知识注入（retention-aware knowledge injection）解决的是模型生命周期刚需——在不遗忘既有能力的前提下持续吸收新事实与领域知识，这是所有模型厂商长期都要面对的基础问题，因此赛道本身具备持续价值。但
    RoCo-ACE 属于学术增量贡献：无代码、无数据、无产品落地，仅是一个训练目标层面的改进；该赛道已有 RAG、LoRA、模型编辑（ROME/MEMIT）等多条相互竞争的成熟路径，蒸馏式注入未必能成为行业标准，实际商业转化高度依赖被主流模型厂商采纳的验证周期。短期看难以形成复利积累，长期若被纳入头部实验室的训练管线则具备基础设施潜力，故给予中低分，需持续跟踪落地信号。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- OpenAI
- Google DeepMind
- 开源多模态模型生态（Llama/Qwen）
competitive_casualty:
- 纯 RAG 知识更新方案
- 模型编辑类工具（ROME/MEMIT）
- 传统微调服务商
market_opportunities:
- 基于该蒸馏目标可开发企业级'低遗忘'领域知识更新工具，服务法律、医疗、金融等需高频知识注入且不容许旧能力退化的垂直场景
- 该方法的保留能力评估框架（六项基准、多基础模型）可复用为 MLLM 持续学习/知识更新产品的评测基准，形成差异化评测服务
- 待方法开源后存在工程化封装机会，可落地为 MLOps 平台中的模型增量更新模块，降低领域微调导致的灾难性遗忘成本
risk_matrix:
  regulatory: 知识注入若采用受版权保护的权威答案或专有语料，可能引发数据许可与著作权争议；在医疗、金融等受监管领域使用注入后模型需承担内容合规责任
  technological: 论文属理论主张且当前未公开代码与数据，可复现性存疑；在线蒸馏计算开销较高，可能被 LoRA、DPO 等更轻量、生态更成熟的方法替代
  competitive: 主流模型厂商与开源社区均在持续投入持续学习/知识编辑方向，该学术提案尚未形成工程生态，存在被巨头方案与开源替代挤压的风险
  ethical: 注入的权威语料可能隐含偏见并被放大；保留评估若未覆盖安全对齐维度，蒸馏过程可能无意保留或强化有害行为
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection

View PDF HTML (experimental)Abstract:Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior. Online distillation mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned distillation provides coarse supervision: it can under-emphasize reference-supported rollout tokens and supervise omitted facts only indirectly. We introduce RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection. RoCo uses same-rollout reference-free/reference-conditioned likelihood contrast to reallocate additional distillation weight to reference-supported rollout tokens, while ACE adds sparse reference-side anchored correction for authoritative anchors omitted from the rollout without full-answer imitation. Across three knowledge-injection settings, six retention benchmarks, multiple baselines, and multiple base models, RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while keeping evaluated retention close to the base model.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.