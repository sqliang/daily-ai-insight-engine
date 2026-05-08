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
impact_score:
  score: 7.5
  reason: RLDX-1 提出的多流动作Transformer (MSAT) 架构在灵巧操作任务上取得了显著突破——在ALLEX人形机器人任务中达到86.8%成功率，比当前前沿VLA模型(π_{0.5}和GR00T
    N1.6约40%)提升超一倍。这是对现有VLA架构范式的实质性改进，但尚未达到ChatGPT发布级别的行业范式转移。该工作解决了一个关键痛点：现有VLA在需要运动感知、长期记忆和物理感知等广泛功能能力的复杂现实任务中表现不佳，MSAT通过模态专用流+跨模态联合自注意力的设计直接回应了这一缺口。综合评分7.5分，属于重要的局部竞争格局改变。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: MSAT多流架构在灵巧操作任务上相比π_{0.5}和GR00T N1.6取得压倒性优势
hype_assessment:
  level: low
  reason: 论文使用客观学术语言，未出现'颠覆'、'革命性'等PR滥用词汇。表述克制（'a promising step toward'），提供了充分的模拟基准测试和真实世界任务对比数据，消融研究扎实，性能数据透明。arXiv上的技术报告格式，非商业化PR稿。
information_entropy: high
domain_disruption:
  technical_innovation: 提出多流动作Transformer（MSAT）架构，通过模态专用流分别处理视觉、运动学、触觉等异构模态，再通过跨模态联合自注意力机制实现统一融合——这一设计突破了现有VLA模型依赖单一自注意力混杂处理多模态信息的瓶颈，在高自由度人形机器人控制中展现出显著优越性。
  business_model: 无直接商业模式影响。若技术成熟经产品化，可赋能人形机器人在精密装配、手术辅助、家庭服务等高接触动态场景的商业落地，降低灵巧操作任务的编程门槛和部署成本。
engineering_complexity: prototype
compound_value:
  score: 6.8
  reason: RLDX-1 提出的多流动作Transformer（MSAT）架构在灵巧操作任务上实现了对 π₀.5 和 GR00T N1.6 约 2 倍的性能提升（86.8%
    vs ~40%），这是一个非常显著的边际改进，直接证明了现有 VLA 架构在处理运动感知、长期记忆和物理感知等广泛功能能力方面的根本性缺陷可以被新的架构设计解决。从复利效应来看，灵巧操作是通向通用人形机器人商业化的关键瓶颈，一旦突破将打开万亿级市场（制造、物流、家政、护理等），因此该技术路径具备极强的长期价值积累潜力。但扣分点在于：这是一篇学术技术报告，没有披露商业实体、公司关联或明确的商业化路线图；代码和模型权重是否开源不明确；验证场景局限于
    ALLEX 平台，泛化性尚需更多证据。综合来看，MSAT 架构有潜力成为灵巧操作领域的标准范式，但目前处于技术验证阶段，需要关注是否有团队以此为基础创立公司或头部机器人企业将其内部化。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- ALLEX
- Humanoid机器人初创公司
- NVIDIA
- Figure AI
- Tesla Optimus
competitive_casualty:
- Physical Intelligence (π₀.5)
- NVIDIA GR00T
- 传统基于模仿学习的机器人策略
market_opportunities:
- 机器人灵巧操作中间件商业化——RLDX-1的MSAT多流架构可封装为标准化软件栈，向人形机器人硬件厂商授权或提供定制集成服务，市场空间广阔
- 稀缺操控场景的合成数据服务——利用RLDX-1的数据合成方案，为工业精密装配、医疗手术辅助等低频率高价值场景生成高质量训练数据，形成数据即服务（DaaS）模式
- 人形机器人实时推理加速工具链——RLDX-1的推理优化技术可独立提取为边缘端部署工具（模型量化、算子融合），服务于机器人公司的端侧推理需求
risk_matrix:
  regulatory: 高性能灵巧操作算法可能被纳入AI出口管制清单（类似EDA/芯片管制逻辑），同时各主要经济体可能加速出台人形机器人安全认证与功能限制法规
  technological: MSAT架构的有效性尚需在更多机器人平台和操作场景中验证；扩散策略、世界模型等并行路线可能更快突破，导致该技术路径被边缘化
  competitive: NVIDIA GR00T、Physical Intelligence（π系列）、Tesla Optimus等拥有更强资金、数据和硬件整合能力的巨头可能快速迭代反超，压缩RLDX-1生态空间
  ethical: 高自由度人形机器人的灵活操作能力显著加速制造业和服务业岗位替代，同时该技术若被恶意利用可能用于自主武器系统的灵巧操控
  additional:
  - 论文为arXiv预印本，未经同行评审，实验复现性和结果稳健性尚待独立验证
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
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