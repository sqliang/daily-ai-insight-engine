---
title: Right-Sizing Communication and Recommendation Set Size in AI-Assisted Search
source: https://arxiv.org/abs/2605.23944
author:
- '[[Jing Dong, Prakirt Raj Jhunjhunwala, Yash Kanoria]]'
published: '2026-05-26'
created: '2026-05-26'
description: 'arXiv:2605.23944v1 Announce Type: new Abstract: We model the interaction
  between a user and an AI driven recommendation system. The user initiates the process
  by conveying preference information through a costly and noisy message. The AI assistant,
  acting as a Bayesian agent, interprets the user''s message to form a posterior belief
  about their true preferences and make product recommendations. In particular, it
  determines how many recommendations to present so as to maximize the user''s expected
  utility from their final choice, while accounting for the search cost induced by
  the size of the recommendation set. We use mutual information based cost functions
  to model the two distinct costs incurred by the user during the interaction: (i)
  a communication cost, which increases with the precision of their preference message,
  and (ii) a search cost, which increases with the size of the recommendation set
  provided by the AI assistant. We study products and preferences which live in d
  dimensional space, and ask how the user''s expected payoff can be maximized. For
  large d, we characterize how optimal message precision and recommendation set size
  depend on the cost parameters, under two distinct distributions from which recommendations
  can be sampled from the product universe: (i) Bayes'' posterior belief, and (ii)
  an optimized tilted distribution. Under the posterior sampling scheme (i), we identify
  a hybrid regime, in which an efficient interaction policy requires jointly optimizing
  the amount of information (in bits) conveyed by the user and the number of recommendations
  provided by the AI assistant. In the tilted sampling scheme (ii), our results show
  that the optimal interaction policy uses only one of communication and search, favoring
  whichever of them is less costly.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 67aaecd6df615a1e
source_type: academic_paper
tldr: 研究AI推荐系统中用户通信精度与推荐集合大小的最优权衡，发现最优策略取决于采样方案和成本参数。
objective_summary: 该论文从理论上建模AI辅助搜索中用户与推荐系统的交互过程。用户以有成本且含噪声的消息传达偏好，AI作为贝叶斯智能体据此形成后验信念并决定推荐数量。研究在d维偏好空间中，分别分析后验采样和倾斜分布采样两种方案下的最优交互策略。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Bayesian inference
  - mutual information
  - recommendation systems
  - posterior sampling
  - tilted distribution
  key_people: []
key_logic_flow:
- 论文建模了用户与AI驱动推荐系统之间的交互过程，用户通过有成本且含噪声的消息传达偏好信息，AI助手据此进行贝叶斯推断。
- 使用基于互信息的成本函数量化两类用户成本：通信成本随偏好消息精度增加而上升，搜索成本随推荐集合大小增加而上升。
- 在d维偏好空间的高维情形下，分析了两种推荐采样方案：基于贝叶斯后验信念的采样，以及经过优化的倾斜分布采样。
- 在后验采样方案下，存在一个混合策略区间，高效交互需联合优化用户传达的信息量（以比特计）和AI提供的推荐数量。
- 在倾斜采样方案下，最优交互策略仅使用通信或搜索其中之一，优先选择成本更低的那一方。
impact_score:
  score: 3.5
  reason: 该论文从信息论角度对AI推荐系统中通信精度与推荐集合大小的最优权衡进行了严格的数学建模，揭示了两种采样方案下截然不同的最优策略（后验采样存在混合区间、倾斜采样则二者择一），这一反直觉结论对AI搜索产品的交互设计具有理论指导意义。但作为纯理论论文，无实证验证、无产品落地、无行业参与者背书，短期内难以产生实际冲击力，属于学术圈内的有价值增量研究。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 倾斜采样方案下'通信与搜索择一而用'的反直觉结论是否能在真实推荐场景中复现
hype_assessment:
  level: low
  reason: 论文采用严格的数学建模语言（贝叶斯推断、互信息成本函数、d维偏好空间渐进分析），全文未出现'颠覆''革命性'等PR词汇，篇幅聚焦于定理推导与方案对比，属于实打实的理论工作。
information_entropy: high
domain_disruption:
  technical_innovation: 首次将用户通信成本（以互信息比特数度量）与AI推荐集合大小纳入统一优化框架，并在高维偏好空间下对后验采样与倾斜分布采样两种方案给出了渐进最优策略的完整刻画，尤其是揭示了倾斜采样下最优策略的'二择一'相变现象。
  business_model: 若该理论框架被验证并工程化，可能重塑AI搜索与推荐产品的交互范式——例如在低成本通信场景下让用户用简短自然语言描述偏好后AI返回大量结果，而在高噪声场景下则减少交互轮次、依赖AI主动推断，从而优化用户决策效率与平台算力分配。
engineering_complexity: conceptual
compound_value:
  score: 4.0
  reason: 该论文提出了一个具有理论价值的框架——用互信息成本函数建模AI推荐系统中'用户通信精度'与'推荐集合大小'之间的最优权衡，并揭示了后验采样下的混合策略区间与倾斜采样下的单边最优策略。然而，这是一篇纯理论论文，无公司背书、无产品化路径、无实验验证，从VC视角看，从理论到商业落地的距离极长（3-5年以上）。若未来有团队将此框架工程化并嵌入AI搜索/推荐产品中，可能成为差异化竞争力来源，但当前阶段仅具备学术参考价值，不具备复利积累特征。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- Google
- Microsoft
- Perplexity
- OpenAI
- Anthropic
- Amazon
- Netflix
competitive_casualty:
- 传统固定规则推荐引擎
- 过度依赖单一维度优化的推荐系统厂商
market_opportunities:
- 推荐系统团队可将该理论框架融入产品设计，通过量化用户通信成本与搜索成本的最优权衡点，动态调整推荐列表长度（如电商搜索结果显示数量、视频平台首页推荐密度），在不过度消耗用户注意力的前提下最大化转化率。
- 基于倾斜分布采样方案的结论（仅使用通信或搜索中成本更低的一方），AI助手产品可设计两种差异化交互模式：一是"少问多推"模式（适合低偏好确定性的泛化搜索场景），二是"多问精推"模式（适合高偏好精确性的决策场景，如医疗、理财咨询），形成产品壁垒。
- 从事AI产品设计或人机交互研究的从业者，可深入学习该论文的互信息成本建模方法，将其作为量化评估用户认知负荷与AI输出信息量之间关系的分析工具，提升自身在AI交互体验优化领域的专业竞争力。
risk_matrix:
  regulatory: 无
  technological: 该理论框架基于贝叶斯推断和互信息成本函数，属于基础理论建模，短期内不存在被替代的直接风险；但若未来出现更优的偏好建模范式（如基于大语言模型的隐式偏好推断），可能使该框架的实用性受限。
  competitive: 若头部AI公司（如Google搜索、TikTok推荐、Amazon电商）将论文中的最优交互策略工程化落地，可能拉大与中小企业在推荐效率上的差距，形成"数据+算法+交互范式"的三重竞争壁垒。
  ethical: 倾斜分布采样方案下，AI助手自主决定推荐策略（仅通信或仅搜索），可能系统性减少用户的选择多样性——当AI判定搜索成本更低时，用户将失去表达细粒度偏好的机会，长期可能导致"偏好窄化"和推荐同质化，侵蚀用户自主决策权。
  additional:
  - 高维偏好空间（d维）的理论结论在小规模实际场景中可能不成立，企业在未充分验证的情况下直接应用可能存在模型误用风险。
confidence:
  impact: low
  compound: medium
  hype: low
actionable_insight: speculative_watch
---

# Computer Science > Artificial Intelligence

# Title:Right-Sizing Communication and Recommendation Set Size in AI-Assisted Search

View PDF HTML (experimental)Abstract:We model the interaction between a user and an AI driven recommendation system. The user initiates the process by conveying preference information through a costly and noisy message. The AI assistant, acting as a Bayesian agent, interprets the user's message to form a posterior belief about their true preferences and make product recommendations. In particular, it determines how many recommendations to present so as to maximize the user's expected utility from their final choice, while accounting for the search cost induced by the size of the recommendation set. We use mutual information based cost functions to model the two distinct costs incurred by the user during the interaction: (i) a communication cost, which increases with the precision of their preference message, and (ii) a search cost, which increases with the size of the recommendation set provided by the AI assistant.

We study products and preferences which live in d dimensional space, and ask how the user's expected payoff can be maximized. For large d, we characterize how optimal message precision and recommendation set size depend on the cost parameters, under two distinct distributions from which recommendations can be sampled from the product universe: (i) Bayes' posterior belief, and (ii) an optimized tilted distribution. Under the posterior sampling scheme (i), we identify a hybrid regime, in which an efficient interaction policy requires jointly optimizing the amount of information (in bits) conveyed by the user and the number of recommendations provided by the AI assistant. In the tilted sampling scheme (ii), our results show that the optimal interaction policy uses only one of communication and search, favoring whichever of them is less costly.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.