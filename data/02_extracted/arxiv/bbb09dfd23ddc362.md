---
title: RLDX-1 Technical Report
source: https://arxiv.org/abs/2605.03269
author:
- '[[Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun
  Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung
  Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won,
  Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung
  Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku
  Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Heecheol
  Kim, Heewon Lee, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung,
  Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park,
  Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe,
  Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim,
  Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee,
  Yeonwoo Bae, Jinwoo Shin]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.03269v2 Announce Type: replace-cross Abstract: While Vision-Language-Action
  models (VLAs) have shown remarkable progress toward human-like generalist robotic
  policies through the versatile intelligence (i.e. broad scene understanding and
  language-conditioned generalization) inherited from pre-trained Vision-Language
  Models, they still struggle with complex real-world tasks requiring broader functional
  capabilities (e.g. motion awareness, long-term memory, and physical sensing). To
  address this, we introduce RLDX-1, a general-purpose robotic policy for dexterous
  manipulation built on the Multi-Stream Action Transformer (MSAT), an architecture
  that unifies these capabilities by integrating heterogeneous modalities through
  modality-specific streams with cross-modal joint self-attention. RLDX-1 further
  combines this architecture with system-level design choices, including data synthesis
  for rare manipulation scenarios, learning procedures specialized for human-like
  manipulation, and inference optimizations for real-time deployment. Through empirical
  evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g.
  $\pi_{0.5}$ and GR00T N1.6) across both simulation benchmarks and real-world tasks
  that require broad functional capabilities beyond general versatility. In particular,
  RLDX-1 shows superiority in ALLEX humanoid tasks by achieving success rates of 86.8%
  while $\pi_{0.5}$ and GR00T N1.6 achieve around 40%, highlighting the ability of
  RLDX-1 to control a high-DoF humanoid robot under diverse functional demands. Together,
  these results position RLDX-1 as a promising step toward reliable VLAs for complex,
  contact-rich, and dynamic real-world dexterous manipulation.'
tags:
- clippings
id: bbb09dfd23ddc362
source_type: academic_paper
tldr: RLDX-1 是一种基于多流动作Transformer的通用灵巧操作机器人策略
objective_summary: RLDX-1 采用多流动作Transformer架构，通过模态专用流和跨模态联合自注意力整合异构模态，在ALLEX人形机器人任务中达86.8%成功率，显著优于π_{0.5}和GR00T
  N1.6约40%的水平。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - VLA
  - MSAT
  - Multi-Stream Action Transformer
  - ALLEX
  - GR00T N1.6
  - π_{0.5}
  key_people: []
key_logic_flow:
- 现有VLA模型在视觉理解和语言条件泛化方面有进展，但在需要运动感知、长期记忆和物理感知等广泛功能能力的复杂现实任务中仍存在困难
- RLDX-1 提出了多流动作Transformer架构，通过模态专用流与跨模态联合自注意力机制统一整合异构模态能力
- RLDX-1 结合了针对稀有操控场景的数据合成、类人操控学习程序和实时部署推理优化等系统级设计
- 在模拟基准测试和真实世界任务中，RLDX-1 始终优于 π_{0.5} 和 GR00T N1.6 等前沿VLA模型
- 在ALLEX人形机器人任务中，RLDX-1 达到86.8%的成功率，而 π_{0.5} 和 GR00T N1.6 仅约40%
- RLDX-1 展示了在高自由度人形机器人上应对多样化功能需求的能力，被视为迈向可靠VLA用于复杂、高接触动态灵巧操作的重要一步
---

# Computer Science > Robotics

# Title:RLDX-1 Technical Report

View PDF HTML (experimental)Abstract:While Vision-Language-Action models (VLAs) have shown remarkable progress toward human-like generalist robotic policies through the versatile intelligence (i.e. broad scene understanding and language-conditioned generalization) inherited from pre-trained Vision-Language Models, they still struggle with complex real-world tasks requiring broader functional capabilities (e.g. motion awareness, long-term memory, and physical sensing). To address this, we introduce RLDX-1, a general-purpose robotic policy for dexterous manipulation built on the Multi-Stream Action Transformer (MSAT), an architecture that unifies these capabilities by integrating heterogeneous modalities through modality-specific streams with cross-modal joint self-attention. RLDX-1 further combines this architecture with system-level design choices, including data synthesis for rare manipulation scenarios, learning procedures specialized for human-like manipulation, and inference optimizations for real-time deployment. Through empirical evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g. $\pi_{0.5}$ and GR00T N1.6) across both simulation benchmarks and real-world tasks that require broad functional capabilities beyond general versatility. In particular, RLDX-1 shows superiority in ALLEX humanoid tasks by achieving success rates of 86.8% while $\pi_{0.5}$ and GR00T N1.6 achieve around 40%, highlighting the ability of RLDX-1 to control a high-DoF humanoid robot under diverse functional demands. Together, these results position RLDX-1 as a promising step toward reliable VLAs for complex, contact-rich, and dynamic real-world dexterous manipulation.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.