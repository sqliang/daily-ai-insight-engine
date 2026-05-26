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