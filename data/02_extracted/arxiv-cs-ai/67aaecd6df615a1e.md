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
tldr: 这篇论文构建了用户与AI推荐系统的交互模型，研究如何优化用户的通信成本（偏好信息精度）和AI的搜索成本（推荐集大小）。在高维空间中，论文刻画了两种采样方案下的最优交互策略：后验采样方案需要联合优化信息比特数和推荐数量，倾斜采样方案则倾向于只使用成本较低的那一种。
objective_summary: arXiv 发表了一篇编号为 2605.23944 的理论论文，研究 AI 辅助搜索中通信与推荐集大小的最优化问题。作者将用户与
  AI 推荐系统的交互建模为贝叶斯博弈：用户发送有成本且带有噪声的偏好信息，AI 作为贝叶斯智能体形成后验信念并做出推荐决策。论文使用基于互信息的成本函数刻画两类成本——通信成本随消息精度增加而上升，搜索成本随推荐集规模增加而上升——并在两种推荐采样方案（后验采样与倾斜采样）下分析了高维空间中最大化用户期望收益的最优策略。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - Recommendation Systems
  - Bayesian Inference
  - Mutual Information
  key_people: []
key_logic_flow:
- 论文建模了用户与AI推荐系统之间的交互过程：用户通过有成本且带有噪声的消息传达偏好信息，AI作为贝叶斯智能体解释消息并形成关于用户真实偏好的后验信念。
- AI智能体决定向用户展示多少个推荐项，以最大化用户从最终选择中获得的期望效用，同时考虑推荐集大小带来的搜索成本。
- 论文使用基于互信息的成本函数来建模两类成本：通信成本随用户偏好消息的精度增加而增加，搜索成本随AI推荐集的大小增加而增加。
- 研究假设产品和偏好位于d维空间中，考察在高维极限下如何最大化用户的期望收益。
- 在后验采样方案下，论文识别出一个混合机制，要求联合优化用户传达的信息比特数和AI提供的推荐数量。
- 在倾斜采样方案下，最优交互策略只使用通信或搜索中的一种，倾向于选择成本较低的那个维度。
extract_result: success
object_mentions:
- object_type: paper
  name: Right-Sizing Communication and Recommendation Set Size in AI-Assisted Search
  canonical_name: '2605.23944'
  url: https://arxiv.org/abs/2605.23944
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文建模了用户与AI推荐系统的交互，用户通过有成本且带有噪声的消息传达偏好信息，AI作为贝叶斯智能体解释消息并形成关于用户真实偏好的后验信念。
  - 论文使用基于互信息的成本函数建模两类成本：通信成本随偏好消息精度上升，搜索成本随推荐集规模上升。
  - 在后验采样方案下论文识别出混合机制，要求联合优化用户传达的信息比特数和AI提供的推荐数量；在倾斜采样方案下最优策略只使用其中一种。
  article_id: 67aaecd6df615a1e
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