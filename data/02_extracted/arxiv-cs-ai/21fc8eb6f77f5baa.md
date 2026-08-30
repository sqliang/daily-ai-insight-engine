---
title: 'Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation'
source: https://arxiv.org/abs/2608.06632
author:
- '[[Ziyun Xu, Bosen Ding, Yue Zhang, Ji Qi, Qingyuan Song, Jizhou Huang, Liwei Wang,
  Jefferey Santelli, Yue Weng, Qichao Que, Zhenheng Yang, Junfeng Pan, Linhong Zhu]]'
published: '2026-08-10'
created: '2026-08-10'
manifest_dates:
- '2026-08-10'
description: 'arXiv:2608.06632v1 Announce Type: new Abstract: Industrial recommendation
  systems predominantly adopt a passive ranking paradigm that infers user preferences
  from implicit behavioral signals (e.g., clicks, dwell time) rather than explicit,
  natural language inputs. As a result, users experience a persistent discrepancy
  between their explicit interests and what passive behavioral algorithms deliver,
  limiting their ability to express nuanced preferences or steer their feed in real
  time. To address this growing gap between how recommendations are optimized and
  how users wish to articulate their interests, we present Shape Your Feed (SYF),
  an LLM-based agentic recommendation framework that enables real-time, multimodal
  co-curation of content. SYF employs a three-tier architecture: (i) a Perception
  Flow that captures fine-grained user intent from text prompts, voice commands, and
  UI interactions; (ii) a Serving Flow that performs real-time agentic re-ranking
  and pruning of candidate items, grounded in a persistent Semantic Profile encoding
  evolving user preferences; and (iii) a Self-Evolution Flow that aligns system behavior
  with human judgments via Direct Preference Optimization (DPO) and an LLM-as-a-Judge
  ensemble. Offline evaluations show that SYF''s alignment scoring module achieves
  98.85% accuracy, substantially improving over strong few-shot baselines. Large-scale
  online A/B experiments on production traffic further demonstrate that SYF improves
  feed relevance and user sentiment, indicating a practical and scalable path toward
  interactive, user-steerable recommendation in industrial settings.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 21fc8eb6f77f5baa
source_type: academic_paper
tldr: arXiv 论文提出 Shape Your Feed（SYF），一个基于 LLM 的智能体推荐框架，通过感知流、服务流与自进化流三层架构实现实时多模态信息流共同策展。离线评测对齐评分模块达
  98.85% 准确率，在线 A/B 实验改善了信息流相关性与用户情感。
objective_summary: 工业推荐系统通常采用被动排序范式，仅从点击和停留时长等隐式行为推断用户偏好，与用户显式兴趣存在偏差。为此，arXiv 论文提出
  Shape Your Feed（SYF），一个基于 LLM 的智能体推荐框架，其三层架构分别负责捕获用户意图、执行实时重排剪枝以及通过 DPO 和 LLM-as-a-Judge
  对齐人类判断。离线评测显示对齐评分模块准确率达 98.85%，显著优于少样本基线；大规模在线 A/B 实验表明该框架提升了生产信息流的相关性和用户情感体验。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - DPO
  - LLM-as-a-Judge
  key_people: []
key_logic_flow:
- 工业推荐系统普遍采用被动排序范式，仅从点击、停留时长等隐式行为信号推断用户偏好，导致用户显式兴趣与算法交付内容之间存在持续偏差。
- 论文提出基于 LLM 的智能体推荐框架 Shape Your Feed（SYF），支持用户通过文本提示、语音指令和界面交互进行实时、多模态的信息流共同策展。
- SYF 采用三层架构：感知流捕获细粒度用户意图，服务流基于持久化语义画像执行实时智能体重排与候选剪枝，自进化流通过直接偏好优化（DPO）和 LLM-as-a-Judge
  集成使系统与人类判断对齐。
- 离线评估表明 SYF 的对齐评分模块达到 98.85% 准确率，显著超过强少样本基线。
- 在真实生产流量上的大规模在线 A/B 实验中，SYF 改善了信息流相关性和用户情感，展示了工业场景下交互式、用户可操控推荐的实际可行路径。
object_mentions:
- object_type: project
  name: Shape Your Feed (SYF)
  canonical_name: Shape Your Feed (SYF)
  url: https://arxiv.org/abs/2608.06632
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - SYF 是一个基于 LLM 的智能体推荐框架，采用感知流、服务流与自进化流三层架构，支持用户实时、多模态地共同策展信息流。
  - 离线评测显示 SYF 的对齐评分模块达到 98.85% 准确率，显著优于强少样本基线。
  - 大规模在线 A/B 实验表明 SYF 改善了生产信息流的相关性和用户情感体验。
  article_id: 21fc8eb6f77f5baa
- object_type: paper
  name: 'Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation'
  canonical_name: Shape Your Feed (arXiv 2608.06632)
  url: https://arxiv.org/abs/2608.06632
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该 arXiv 论文提出 Shape Your Feed（SYF），一个基于 LLM 的智能体推荐框架，以解决工业推荐系统被动排序与用户显式兴趣表达之间的偏差。
  - 论文报告离线评测中对齐评分模块达到 98.85% 准确率，并在生产流量上通过在线 A/B 实验验证了信息流相关性和用户情感的改善。
  article_id: 21fc8eb6f77f5baa
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:Shape Your Feed: An LLM-based Agentic System for Conversational Recommendation

View PDF HTML (experimental)Abstract:Industrial recommendation systems predominantly adopt a passive ranking paradigm that infers user preferences from implicit behavioral signals (e.g., clicks, dwell time) rather than explicit, natural language inputs. As a result, users experience a persistent discrepancy between their explicit interests and what passive behavioral algorithms deliver, limiting their ability to express nuanced preferences or steer their feed in real time. To address this growing gap between how recommendations are optimized and how users wish to articulate their interests, we present Shape Your Feed (SYF), an LLM-based agentic recommendation framework that enables real-time, multimodal co-curation of content. SYF employs a three-tier architecture: (i) a Perception Flow that captures fine-grained user intent from text prompts, voice commands, and UI interactions; (ii) a Serving Flow that performs real-time agentic re-ranking and pruning of candidate items, grounded in a persistent Semantic Profile encoding evolving user preferences; and (iii) a Self-Evolution Flow that aligns system behavior with human judgments via Direct Preference Optimization (DPO) and an LLM-as-a-Judge ensemble. Offline evaluations show that SYF's alignment scoring module achieves 98.85% accuracy, substantially improving over strong few-shot baselines. Large-scale online A/B experiments on production traffic further demonstrate that SYF improves feed relevance and user sentiment, indicating a practical and scalable path toward interactive, user-steerable recommendation in industrial settings.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.