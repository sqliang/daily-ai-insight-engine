---
title: 'GrocLM: Grocery Category Recommendation in E-Commerce with Large Language
  Models'
source: https://arxiv.org/abs/2607.24764
author:
- '[[Yuan Zhong, Chuanwei Ruan, Moein Hasani, Tejaswi Tenneti, Haixun Wang, Fenglong
  Ma]]'
published: '2026-07-29'
created: '2026-07-29'
manifest_dates:
- '2026-07-29'
description: 'arXiv:2607.24764v1 Announce Type: new Abstract: The rapid growth of
  online grocery shopping requires recommendation systems that capture cyclical purchasing
  behavior and diverse user intents. Traditional item-level methods face scalability
  and accuracy challenges, motivating category-level recommendation as a more structured
  and practical alternative. We present GROCLM, a fine-tuned language model for grocery
  category recommendation in a real-world production environment. GROCLM employs a
  two-stage LoRA-based training strategy to encode cyclical purchasing patterns directly
  into model parameters, enabling more effective utilization of rebuying signals compared
  to prompt-based conditioning. To ensure valid and controllable outputs, we further
  introduce a trie-based constrained decoding mechanism over a predefined category
  space. Experiments on both proprietary production data and a public benchmark demonstrate
  that GROCLM consistently outperforms strong baselines. In a live production restocking
  task, GROCLM achieves a 7.5% relative improvement in cart-adds per impression, while
  maintaining efficient inference by generating all categories jointly. These results
  highlight the effectiveness and practicality of integrating large language models
  into structured recommendation systems.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2ee3d57a9a4ce9cd
source_type: academic_paper
tldr: 论文提出 GROCLM，一个针对线上杂货电商品类推荐微调的语言模型。它采用两阶段 LoRA 训练将周期性购买模式编码进模型参数，并用前缀树约束解码保证输出可控；在线上补货任务中每展示加购数相对提升
  7.5%，优于强基线模型。
objective_summary: GROCLM 是 arXiv 上发布的一篇论文，提出用于电商杂货品类推荐的微调语言模型，其研究背景是线上杂货购物的快速增长对推荐系统提出可扩展性与准确性挑战。研究团队采用两阶段
  LoRA 训练策略，把周期性购买模式直接编码进模型参数，并设计基于前缀树的约束解码机制限定在预定义品类空间内输出。实验基于专有生产数据与公开基准，结果显示 GROCLM
  一致优于强基线；在线上补货任务中每展示加购数取得 7.5% 的相对提升，并通过联合生成全部品类实现高效推理。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LoRA
  - LLM
  - trie-based constrained decoding
  - grocery category recommendation
  - fine-tuned language model
  key_people: []
key_logic_flow:
- GROCLM 是一个针对电商杂货场景微调的语言模型，用于品类级推荐，以应对传统单品级方法在扩展性和准确性上的挑战。
- 模型采用两阶段 LoRA 微调训练策略，将周期性购买行为直接编码进模型参数，比基于提示的条件化方式更有效地利用复购信号。
- 为保障输出有效且可控，论文引入基于前缀树的约束解码机制，将生成范围限制在预定义品类空间内。
- 实验在专有生产数据和公开基准上展开，结果显示 GROCLM 一致优于强基线模型。
- 在线上补货任务中，GROCLM 取得每展示加购数 7.5% 的相对提升，并通过联合生成全部分类保持高效推理。
object_mentions:
- object_type: model
  name: GrocLM
  canonical_name: GrocLM
  url: https://arxiv.org/abs/2607.24764
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 GROCLM，一个在真实生产环境中面向杂货品类推荐微调的语言模型，通过两阶段 LoRA 训练将周期性购买模式编码进模型参数。
  - GROCLM 在预定义品类空间上引入基于前缀树的约束解码机制，以保证输出有效且可控，并联合生成所有品类以维持高效推理。
  - 在线上补货任务中，GROCLM 相比强基线实现每展示加购数 7.5% 的相对提升，并在专有生产数据和公开基准上均表现更优。
  article_id: 2ee3d57a9a4ce9cd
extract_result: success
impact_score:
  score: 4.0
  reason: 该论文属于 LLM4Rec 方向的垂直落地应用，技术方案（两阶段 LoRA + 前缀树约束解码）扎实且有真实线上数据支撑（每展示加购数相对提升
    7.5%），能为电商推荐团队提供可借鉴的工程范式。但应用域窄（杂货品类推荐），且实验依赖专有生产数据、缺乏开源代码，短期难以引发行业级范式变化，更接近局部竞争格局内的工程方法验证，故评分落在中低位区间。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 约束解码与 LoRA 在真实推荐系统中的增益能否复现，以及专有数据下的结论是否具有普适性
hype_assessment:
  level: low
  reason: 论文措辞克制，未使用“颠覆/革命性”等 PR 语言，给出了明确的线上业务指标（7.5% 相对提升）、具体技术细节（两阶段 LoRA、trie 约束解码、联合生成）及与强基线的对比，属于有实验支撑的工程贡献，无明显概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 将周期性复购模式以两阶段 LoRA 直接编码进模型参数，替代提示条件化方式利用复购信号；并设计基于前缀树的约束解码，将生成限制在预定义品类空间内，同时以联合生成全部品类的方式压缩推理成本，为
    LLM 接入结构化推荐输出提供了可落地的工程路径。
  business_model: 以品类级推荐替代传统单品级推荐，可能重构电商/生鲜零售推荐系统的建模粒度和算力成本结构，对补货、复购提醒等高价值业务场景有直接商业增益，或推动零售平台将
    LLM 作为结构化推荐管道的核心组件。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: 从资本复利视角审视：该事件的核心价值在于验证了'LLM 进入结构化推荐系统'这一方向的真实生产力——7.5% 加购相对提升是生产环境中的硬指标，说明
    LLM 不仅能做对话式交互，还能嵌入电商核心转化链路。但需冷静拆解其技术构成：两阶段 LoRA 微调 + 前缀树约束解码均为成熟方法的工程组合，无突破性技术代差，真正的竞争壁垒落在专有购买数据与复购信号上，而非模型架构。这意味着可复制性较高（论文公开、LoRA
    成本低），短期不会形成单一公司的独占性护城河，但'品类级推荐 + 周期性购买编码'这一范式若被头部电商采纳并跑通数据-模型-体验的正循环飞轮，有潜力沉淀为品类推荐的基础设施。当前状态属于细分赛道早期验证信号，距行业基石仍有产品化与规模化距离，故评分落在
    4-7 区间下沿，需持续观察落地案例与数据飞轮是否成立。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Instacart
- Amazon Fresh
- Walmart
- Kroger
- Alibaba
- JD.com
competitive_casualty:
- 传统单品级推荐系统服务商
- 依赖人工特征工程的推荐引擎团队
- 纯推荐算法初创公司
market_opportunities:
- 电商推荐团队可借鉴 GROCLM 的品类级 LLM 推荐范式，将复购/补货场景从传统单品级模型升级为微调语言模型，以获得可量化的加购转化增益
- 基于前缀树的约束解码机制可产品化为通用的结构化输出控制工具，泛化到商品分类、税务编码、医疗编码等强约束生成场景，形成可复用的中间件或开源库
- 两阶段 LoRA 编码周期性购买模式的方法对订阅制电商、日用消费品补货等强复购型业务有直接落地价值，可作为垂直行业 LLM 微调咨询与解决方案的卖点
risk_matrix:
  regulatory: 推荐系统处理购物记录、复购偏好等个人信息，需关注《个人信息保护法》与 GDPR 的数据合规要求；若结合个性化定价可能触发消费者权益保护审查，欧盟
    AI Act 对推荐系统透明性义务也需纳入评估
  technological: 论文属理论性主张（theoretical_claim），基于专有生产数据且未披露可复现细节，公开验证成本高；LoRA 微调方案可能被更高效的序列/图模型或新一代架构快速替代，7.5%
    的边际优势存在时效性
  competitive: 亚马逊、沃尔玛、阿里、京东等巨头在电商推荐领域拥有深厚积累与独占数据，可快速复制同类方案；通用 LLM API 提供商及推荐即服务创业公司也可能挤压该差异化空间
  ethical: 强化复购引导可能诱发过度消费，存在消费伦理争议；基于购物行为的个性化建模有隐私滥用风险；品类级推荐可能固化品牌与品类偏差，影响中小商家的曝光公平性
  additional:
  - 结果依赖专有生产数据，未见公开代码与数据集，外部独立验证与复现难度大
  - 生产环境 LLM 推理成本与延迟可能限制中小商家规模化采用该方案
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:GrocLM: Grocery Category Recommendation in E-Commerce with Large Language Models

View PDF HTML (experimental)Abstract:The rapid growth of online grocery shopping requires recommendation systems that capture cyclical purchasing behavior and diverse user intents. Traditional item-level methods face scalability and accuracy challenges, motivating category-level recommendation as a more structured and practical alternative. We present GROCLM, a fine-tuned language model for grocery category recommendation in a real-world production environment. GROCLM employs a two-stage LoRA-based training strategy to encode cyclical purchasing patterns directly into model parameters, enabling more effective utilization of rebuying signals compared to prompt-based conditioning. To ensure valid and controllable outputs, we further introduce a trie-based constrained decoding mechanism over a predefined category space. Experiments on both proprietary production data and a public benchmark demonstrate that GROCLM consistently outperforms strong baselines. In a live production restocking task, GROCLM achieves a 7.5% relative improvement in cart-adds per impression, while maintaining efficient inference by generating all categories jointly. These results highlight the effectiveness and practicality of integrating large language models into structured recommendation systems.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.