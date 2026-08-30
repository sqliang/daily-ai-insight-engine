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
impact_score:
  score: 3.5
  reason: 该论文提出了一套完整的三层代理式推荐框架（感知流/服务流/自进化流），将 LLM 智能体、DPO 与 LLM-as-a-Judge 引入工业推荐场景，方向契合当下'代理式
    AI 落地'的主线叙事，属于值得关注的架构级方案。但作为 arXiv 预印本，未公开代码与数据集，'大规模生产 A/B 实验'与 98.85% 准确率均无法独立核实；其技术组合本质是已知方法的架构级集成，而非范式级突破，短期内难以改变行业竞争格局。综合评定
    3.5 分。
sentiment: positive
developer_sentiment:
  tone: skeptical
  primary_focus: 生产 A/B 声明与 98.85% 准确率的可复现性，以及三层 LLM 代理流水线在推荐服务中的推理成本与延迟开销
hype_assessment:
  level: medium
  reason: 论文行文未使用'颠覆性/革命性'等极端措辞，框架也明确构建在 DPO、LLM-as-a-Judge 等已知技术之上；但存在两点包装嫌疑：一是'98.85%
    准确率'仅针对对齐评分模块而非端到端推荐效果，属选择性指标展示；二是未署名公司/平台的'大规模生产 A/B'声明无法核实，且未提供代码与数据，存在结果不可复现的隐患。
information_entropy: medium
domain_disruption:
  technical_innovation: 核心突破在于将工业推荐从'被动行为排序'范式重构为'用户可实时操控的多模态共策展'代理架构——三层流把细粒度意图捕获、基于持久化语义画像的实时智能体重排剪枝、以及
    DPO+LLM-as-a-Judge 的自进化对齐集成到统一流水线中。这属于系统架构层面的集成创新，而非底层算法突破，其工程意义大于理论意义。
  business_model: 若验证成立，可能推动推荐产品从'黑盒算法分发'转向'用户可对话操控的智能体式策展'，为信息流产品带来新的交互式变现与用户留存模式；对推荐
    SaaS 生态而言，'用户可操控/可解释推荐'有望成为差异化卖点，也可能催生围绕交互式推荐的新中间层服务。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 投资逻辑链条：1) 方向验证真实——在线 A/B 实验在生产流量上同时改善信息流相关性与用户情感，说明'用户可操控/会话式推荐'不是纯学术概念，而是有真实需求与落地路径的赛道；2)
    复利潜力在于范式——'感知流-服务流-自进化流'三流架构 + DPO/LLM-as-a-Judge 对齐循环，若被行业采纳为交互式推荐的通用模板，将具备细分赛道基础设施的复利价值；3)
    但当前仅是单篇论文，无公司主体、无代码/产品落地，知识形态仍属 theoretical_claim，工业推荐系统的数据基础设施切换成本极高、组织惯性大，采用周期长，范式能否胜出需多团队复现验证；4)
    扣分项是'论文≠标准'，历史上多数推荐框架论文不会成为行业标准。综合判断处于'方向正确、待验证'的早期阶段，给 5.5 分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- ByteDance
- Meta
- Google
- OpenAI
- Anthropic
competitive_casualty:
- 传统推荐系统厂商（依赖 CTR/隐式行为信号）
- 纯排序算法 AdTech 服务商
- 无交互式能力的个性化推荐初创公司
market_opportunities:
- 内容平台可将 SYF 的'用户可操控信息流'思路作为差异化卖点，在现有被动排序之上叠加 LLM 智能体重排层，打造'可控性+个性化'兼顾的产品形态
- 围绕 DPO + LLM-as-a-Judge 的对齐链路，可开发面向推荐系统的可解释评测与偏好自进化工具，服务中小内容平台的个性化升级需求
- 多模态意图捕捉（文本/语音/UI 交互）为社区产品与信息流 App 提供了新的交互范式切入机会，可探索'对话式策展'增值功能以提升用户参与度
risk_matrix:
  regulatory: 个性化推荐与用户语义画像的持久化存储涉及《个人信息保护法》与《互联网信息服务算法推荐管理规定》，在中国运营需完成算法备案并保障用户对个性化推荐的可解释、可关闭权利
  technological: 论文为 arXiv 预印本且未公开代码与数据，98.85% 准确率等指标难以独立复现；LLM 实时重排在超大规模流量下的延迟与成本瓶颈尚未解决，可能被更廉价的轻量方案替代
  competitive: 字节跳动、Meta、Google 等头部平台在推荐基建上积累深厚，若 SYF 的增量收益不够显著则难以撼动现有排序体系；开源社区快速跟进也可能抹平先发优势
  ethical: 持久化语义画像与实时偏好建模可能加剧信息茧房与过滤气泡；LLM-as-a-Judge 的对齐过程可能编码标注者偏见，对用户交互行为的精细建模还伴随隐私泄露与数据投毒风险
  additional: []
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: Shape Your Feed (SYF)
  canonical_name: Shape Your Feed (SYF)
  url: https://arxiv.org/abs/2608.06632
  positioning: SYF 是一个基于 LLM 的智能体推荐框架，通过感知流、服务流与自进化流三层架构实现实时、多模态的信息流共同策展，让用户以自然语言主动参与并操控推荐结果。
  technical_signal: SYF 三层架构分别处理意图捕获、实时重排与自我进化，感知流融合文本、语音与界面交互信号，服务流结合持久化语义画像进行智能体重排，自进化流以
    DPO 和 LLM-as-a-Judge 对齐人类判断。
  adoption_signal: 论文在真实生产流量上开展了大规模在线 A/B 实验，结果表明 SYF 改善了信息流相关性与用户情感，验证了其工业场景下的可落地性。
  ecosystem_relevance: SYF 代表了推荐系统与 LLM 智能体融合的前沿方向，其交互式、用户可操控范式可能推动工业推荐生态从被动排序走向对话式协同策展。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: SYF 为 LLM 智能体在工业推荐系统中的应用提供了含在线验证的完整技术路径，三层架构与 DPO 对齐的组合设计具有借鉴价值；若后续开源代码或披露更多生产实验数据，将进一步提升该范式的可信度与可复制性，值得持续跟踪。
  risk_notes:
  - 该研究为 arXiv 预印本，尚未开源代码与数据，离线评测和在线实验的细节有待同行评审进一步验证。
  - 摘要未量化在线 A/B 实验的改进幅度，相关性与用户情感的具体提升程度需查阅完整论文核实。
  score: 7.0
  article_ids:
  - 21fc8eb6f77f5baa
  evidence_snippets:
  - SYF 是一个基于 LLM 的智能体推荐框架，采用感知流、服务流与自进化流三层架构，支持用户实时、多模态地共同策展信息流。
  - 离线评测显示 SYF 的对齐评分模块达到 98.85% 准确率，显著优于强少样本基线。
  - 大规模在线 A/B 实验表明 SYF 改善了生产信息流的相关性和用户情感体验。
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