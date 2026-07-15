---
title: LLM-powered reasoning in agent-based modeling
source: https://arxiv.org/abs/2607.06757
author:
- '[[Sifat Afroj Moon, Dakotah Maguire, Adam Spannaus, Joe Tuccillo, Maksudul Alam,
  Sudip K. Seal, John Gounley, Heidi Hanson]]'
published: '2026-07-09'
created: '2026-07-09'
description: 'arXiv:2607.06757v1 Announce Type: new Abstract: Agent-based modeling
  (ABM) has the capability to model millions of individuals and their interactions,
  which is useful for policy making. However, ABMs have traditionally relied on static
  prior, which prevents the models from adapting to real-time changes. Our research
  provides a novel approach to addressing this information gap. Large language models
  (LLMs) offer new opportunities to predict human decision-making. Here, we introduce
  a scalable Hybrid Agent-based and Language-driven Epidemic (HALE) modeling framework
  that leverages LLMs to predict human decision-making in an ABM simulation. As a
  proof-of-concept, we use HALE to simulate COVID-19 and its effects in Salt Lake
  County, UT.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: bbc17e01a6cb04cf
source_type: academic_paper
tldr: 提出 HALE 框架，将 LLM 用于基于智能体的建模以模拟人类决策
objective_summary: 作者针对传统 ABM 依赖静态先验无法实时适应的问题，提出了 HALE 框架，利用大语言模型预测 ABM 模拟中的人类决策，并以
  COVID-19 在盐湖县的模拟作为概念验证。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - ABM
  - LLM
  - HALE
  key_people: []
key_logic_flow:
- 传统基于智能体的建模（ABM）依赖静态先验假设，无法适应实时变化。
- 大语言模型（LLM）为预测人类决策提供了新的可能性。
- 作者提出 HALE（混合智能体与语言驱动流行病模型）框架，将 LLM 集成到 ABM 模拟中。
- HALE 框架使用 LLM 推理来驱动模拟中智能体的人类决策行为。
- 以 COVID-19 在犹他州盐湖县的模拟作为概念验证案例。
specialized_tags:
  paper:
    paperTitle: LLM-powered reasoning in agent-based modeling
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Other
    methodType: LLM-based
extract_result: success
impact_score:
  score: 3.5
  reason: 该论文提出了将LLM推理能力集成到基于智能体建模（ABM）中的HALE框架，属于学术探索性质的新思路。但仅以COVID-19在盐湖县的模拟作为概念验证，缺乏大规模实验数据支撑及可推广的工程实践。短期内在AI行业中的冲击力有限，不属于改变局部竞争格局或范式转移级别的事件，更多是特定交叉领域（AI+计算社会科学/流行病学）的渐进式创新。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: LLM驱动ABM模拟的推理可靠性与可扩展性
hype_assessment:
  level: low
  reason: 论文陈述风格务实，明确指出是概念验证（proof-of-concept），未使用'颠覆'、'革命性'等PR化词汇。方法学创新有限——本质是将现有LLM作为ABM中决策模块的替代，而非底层技术突破。arXiv预印本且应用场景局限（流行病模拟），不存在概念炒作嫌疑。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出HALE框架，用LLM的语义推理能力替代传统ABM中基于静态先验假设的决策模型，使智能体行为能够根据实时语境动态调整，突破了传统ABM无法适应环境变化的根本局限
  business_model: 无
engineering_complexity: conceptual
compound_value:
  score: 4.5
  reason: HALE 框架将 LLM 作为 ABM 中智能体的推理引擎，理论上可替代传统静态先验规则，使仿真能实时响应环境变化。从长期复利视角看，如果 LLM
    驱动的 ABM 被证明可扩展（目前尚未解决大规模并发调用 LLM 的成本与延迟问题），它可能成为政策模拟、城市规划、流行病预测等数字孪生场景的基础设施层——这类场景一旦跑通，用户迁移成本高、网络效应强，具备
    5 年以上的复利潜力。但当前风险极高：① 仅以盐湖县 COVID-19 为单一概念验证，未涉及不同规模、不同场景的泛化验证；② 认知论状态为 theoretical_claim，无任何商业化信号或行业采用数据；③
    LLM token 成本在百万级智能体模拟中呈超线性爆炸，经济可行性存疑。因此现阶段更像学术探索，吸引力远低于已进入产品化阶段的 AI Agent 基建方向。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- 微软（Azure 算力）
competitive_casualty:
- 传统 ABM 仿真平台（AnyLogic, NetLogo）
- 基于静态规则的流行病建模工具
market_opportunities:
- 公共卫生与流行病防控部门可基于 HALE 框架构建动态策略模拟器，在政策出台前用 LLM 驱动的人群行为模拟预判干预措施的居民响应，辅助制定更精准的防控政策
- 城市应急管理、交通规划和社会治理场景可借鉴该思路，将 LLM+ABM 结合用于模拟居民在极端天气、灾害疏散或大型活动中的行为，提升应急预案的实效性
- 商业仿真软件厂商可探索将 LLM 嵌入现有 ABM 平台（如 AnyLogic、NetLogo）的插件化方案，为客户提供"智能体行为智能化"的增值功能
risk_matrix:
  regulatory: LLM 驱动的模拟结果若被用于公共政策制定，可能面临模型可解释性不足导致的监管质疑（如欧盟 AI Act 高风险分类要求可审计的决策依据）；模拟数据涉及人群行为偏好可能触发数据隐私法规
  technological: LLM 的幻觉和推理不稳定性在 ABM 场景中被放大——错误推理的单智能体行为通过交互传播可能导致模拟结果系统性偏差；当前仅以 COVID-19
    为概念验证，泛化到其他领域（交通、经济、社会冲突）的迁移能力尚未验证
  competitive: 该方向尚处早期，但 Google DeepMind、Anthropic 等大模型厂商及传统 ABM 建模公司（如 Simudyne）均有能力快速跟进，独立学术团队的技术壁垒较低
  ethical: LLM 驱动的智能体行为模拟可能隐含训练数据中的社会偏见（如种族、经济地位），导致政策建议对不同群体产生不公平影响；模拟结果被误用为"预测"而非"推演"时存在误导决策者的风险
  additional:
  - LLM 推理延迟和 token 成本在大规模 ABM（百万级智能体）场景下的可扩展性存疑，算力消耗可能远超传统 ABM 的数值模拟
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: speculative_watch
---

# Computer Science > Artificial Intelligence

# Title:LLM-powered reasoning in agent-based modeling

View PDF HTML (experimental)Abstract:Agent-based modeling (ABM) has the capability to model millions of individuals and their interactions, which is useful for policy making. However, ABMs have traditionally relied on static prior, which prevents the models from adapting to real-time changes. Our research provides a novel approach to addressing this information gap. Large language models (LLMs) offer new opportunities to predict human decision-making. Here, we introduce a scalable Hybrid Agent-based and Language-driven Epidemic (HALE) modeling framework that leverages LLMs to predict human decision-making in an ABM simulation. As a proof-of-concept, we use HALE to simulate COVID-19 and its effects in Salt Lake County, UT.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.