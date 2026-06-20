---
title: 'Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs'
source: https://arxiv.org/abs/2606.13815
author:
- '[[Pratham Singla, Shivank Garg, Vihan Singh]]'
published: '2026-06-15'
created: '2026-06-15'
description: 'arXiv:2606.13815v1 Announce Type: new Abstract: Strategic reasoning
  under uncertainty underpins consequential decisions in negotiation, finance, and
  policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions
  into a single scalar, leaving the capability structure of frontier LLMs unexamined.
  We introduce Poker Arena, a no-limit Texas Hold''em tournament platform that couples
  a three-layer memory architecture (within-hand, session, and cross-session) with
  a nine-axis cognitive profile decomposing strategic reasoning into interpretable
  dimensions such as bet-sizing calibration and positional awareness. We evaluate
  seven frontier models across 50 sessions of 1,000 hands and a controlled memory
  ablation; tournament chips and aggregate axis score order the field differently:
  Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only
  fifth of seven on mean axis score, while persistent memory helps some models and
  hurts others. These findings show that multi-axis evaluation surfaces capability
  structure that scalar leaderboards systematically misrank, with cross-dimensional
  consistency outweighing peak performance on any single axis.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 6abedda39a36d5e2
source_type: academic_paper
tldr: Poker Arena：基于德州扑克的多轴评估框架，揭示LLM战略推理能力结构，发现Claude Opus 4.6筹码最高但综合轴得分仅排第五。
objective_summary: 该论文提出Poker Arena，一个无限制德州扑克比赛平台，采用三层记忆架构和九轴认知画像评估LLM战略推理。实验对7个前沿模型进行了50轮各1000手牌测试，发现传统标量排行榜会系统性误排模型真实能力。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Anthropic
  technologies:
  - Poker Arena
  - Texas Hold'em
  - LLMs
  key_people: []
key_logic_flow:
- 该论文提出了Poker Arena，一个基于无限制德州扑克的比赛平台，用于评估大语言模型的战略推理和记忆能力。
- Poker Arena采用三层记忆架构（局内记忆、会话记忆和跨会话记忆）和九轴认知画像，将战略推理分解为可解释的维度（如下注规模校准和位置意识）。
- 论文评估了7个前沿模型，进行了50轮各1000手牌的比赛，并实施了受控记忆消融实验。
- 实验发现Claude Opus 4.6赢得+15,730筹码和14次第一名，但在平均轴得分上仅排名第五（共七个模型）。
- 持久性记忆对某些模型有帮助，但对另一些模型反而有害。
- 多轴评估揭示了标量排行榜系统性误排的能力结构，跨维度一致性比单轴峰值表现更重要。
impact_score:
  score: 4.0
  reason: 该论文提出了一个新颖的多轴评估框架(Poker Arena)，通过德州扑克场景将LLM战略推理分解为9个可解释维度进行评测，并发现了标量排行榜系统性误排模型真实能力的问题。虽然方法论扎实、实验设计严谨，但本质属于学术研究贡献，短期内不会直接改变行业格局或产品形态。对AI评测社区有一定参考价值，但影响力局限于学术圈和模型开发团队，尚未形成广泛的行业冲击力。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 多轴画像方法能否替代或补充现有的单标量排行榜评测体系
hype_assessment:
  level: low
  reason: 论文语气克制、学术化，未使用'颠覆'、'革命性'等PR词汇。实验数据详实（7个模型×50轮×每轮1000手牌），并开展了受控消融实验，统计方法严谨。结论也保持了学术审慎——承认持久记忆对部分模型有益但对其他有害，属于典型的负责任学术写作。
information_entropy: high
domain_disruption:
  technical_innovation: 提出三层记忆架构（局内记忆、会话记忆、跨会话记忆）和九轴认知画像框架（如下注规模校准、位置意识等），将LLM的战略推理能力分解为可解释的独立维度进行量化评估，突破了传统标量排行榜的单一维度局限。
  business_model: 无直接商业模式影响，但可能推动AI评测服务从单标量排名向多维度能力画像转型，对模型评测SaaS和模型选型咨询类业务产生间接参考价值。
engineering_complexity: prototype
compound_value:
  score: 5.0
  reason: Poker Arena 作为一个多轴认知画像评估框架，价值在于为行业提供了超越传统标量排行榜的模型能力评估方法论。其三层记忆架构和九轴维度设计具有方法论创新性，如果被广泛采纳，可能影响未来模型训练的投资方向和采购决策。但其作为纯学术基准论文，无直接商业变现路径，也不构成可复用的基础设施或平台。长期价值取决于能否被社区采纳为行业标准评估框架——这一过程中面临来自现有基准（如
    SWE-bench、MMLU）和商业评估平台的竞争。3-5 年后大概率仅作为评估方法论的参考案例存在，而非行业基石。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
competitive_casualty:
- 依赖单一标量基准营销的模型厂商
market_opportunities:
- 创业者可将 Poker Arena 的多轴评估框架产品化为 AI agent 战略推理能力的 SaaS 评估服务，服务于金融交易、自动谈判、供应链博弈等需要复杂决策的商业场景
- 游戏公司可借鉴其三层次记忆架构设计更智能的 NPC 或游戏 AI，提升开放世界游戏中角色的策略性和沉浸感
- 该论文揭示的标量排行榜系统性误排问题，可转化为企业引入 AI 模型时的多维度能力画像选型工具，替代单一指标驱动的评估模式
risk_matrix:
  regulatory: 基于扑克的推理评估间接涉及博弈行为，若评估平台或评估能力被用于开发自动化赌博系统，可能触发相关司法辖区的赌博监管法规
  technological: Poker Arena 的评估结论建立在德州扑克这一特定不完全信息博弈上，迁移到金融、谈判等真实商业场景的通用性尚未验证，存在评估生态位过窄的局限
  competitive: LLM 评估基准赛道竞争激烈（SWE-bench、GAIA、HumanEval 等均已形成社区认知），Poker Arena 需持续运营与社区建设才能在评估体系中建立影响力
  ethical: 研究揭示的多轴能力画像技术若被恶意使用，可能被用于开发更难以检测的高水平 AI 赌博代理，带来潜在的成瘾性和金融欺诈风险
  additional:
  - 该论文发现持久性记忆对某些模型有帮助、对另一些反而有害，这一反直觉结论可能被断章取义用于营销，误导行业对记忆架构作用的认知
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
---

# Computer Science > Artificial Intelligence

# Title:Poker Arena: Multi-Axis Profiling of Strategic Reasoning and Memory in LLMs

View PDF HTML (experimental)Abstract:Strategic reasoning under uncertainty underpins consequential decisions in negotiation, finance, and policy, but prevailing game-play benchmarks collapse heterogeneous reasoning dimensions into a single scalar, leaving the capability structure of frontier LLMs unexamined. We introduce Poker Arena, a no-limit Texas Hold'em tournament platform that couples a three-layer memory architecture (within-hand, session, and cross-session) with a nine-axis cognitive profile decomposing strategic reasoning into interpretable dimensions such as bet-sizing calibration and positional awareness. We evaluate seven frontier models across 50 sessions of 1,000 hands and a controlled memory ablation; tournament chips and aggregate axis score order the field differently: Claude Opus 4.6 wins +$15,730 chips with 14 first-place finishes, yet ranks only fifth of seven on mean axis score, while persistent memory helps some models and hurts others. These findings show that multi-axis evaluation surfaces capability structure that scalar leaderboards systematically misrank, with cross-dimensional consistency outweighing peak performance on any single axis.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.