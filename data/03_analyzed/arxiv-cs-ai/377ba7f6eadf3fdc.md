---
title: 'Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment
  of Financial Literacy in Serious Games'
source: https://arxiv.org/abs/2606.25358
author:
- '[[Gabriel Santos, Rita Julia, Marcelo Nascimento]]'
published: '2026-06-25'
created: '2026-06-25'
description: 'arXiv:2606.25358v1 Announce Type: new Abstract: Assessing financial
  literacy during gameplay without disrupting the learning experience remains a key
  challenge in serious games for education. We present the Agentic BKT pipeline, a
  multi-agent large language model architecture for stealth assessment of financial
  competencies from open-ended gameplay events. The pipeline processes events from
  a 2D platformer serious game aligned with the OECD/INFE financial literacy framework
  through four phases: (1) the game captures every player decision as a structured
  event log; (2) an LLM event classifier labels each action on a four-point rubric
  validated against three domain experts (Fleiss kappa = 0.624, substantial agreement);
  (3) four domain-specific agents specializing in risk mitigation, investing, spending,
  and credit management perform session-level reasoning over behavioral trajectories,
  feeding per-competency Bayesian Knowledge Tracing that estimates mastery within
  each domain; and (4) an expert judge agent synthesizes the domain-level estimates
  into an overall mastery score. Evaluated with 193 K-12 participants across 264 game
  sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated
  with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p <
  0.0001) while showing no correlation with pre-test scores, providing both convergent
  and discriminant validity. The multi-agent approach approximately triples the predictive
  validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating
  that domain decomposition and session-level reasoning play a central role in capturing
  the multidimensional nature of financial literacy from gameplay'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 377ba7f6eadf3fdc
source_type: academic_paper
tldr: 多智能体LLM架构Agentic BKT通过游戏行为隐式评估金融素养，预测效度是单LLM基线的3倍
objective_summary: 研究者提出Agentic BKT管道，基于多智能体LLM架构从严肃游戏行为中隐式评估金融能力。系统通过4阶段流程处理游戏日志：事件捕获、LLM分类、4个领域智能体推理（风险/投资/支出/信用）及专家综合。193名K-12学生实验显示掌握度估计与学习增益显著相关(r=0.276,
  p=0.
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - LLM
  - Bayesian Knowledge Tracing
  - BKT
  - Agentic BKT
  - Multi-Agent System
  key_people: []
key_logic_flow:
- 论文提出Agentic BKT管道，一种基于多智能体LLM的架构，用于从严肃游戏行为中隐式评估金融素养，与OECD/INFE金融素养框架对齐。
- 系统包含4个阶段：游戏事件日志捕获、LLM事件分类（基于四点评分表，与三位专家一致性达Fleiss kappa=0.624）、4个领域智能体（风险缓解、投资、支出、信用管理）进行会话级推理并执行贝叶斯知识追踪、专家评审智能体综合得出总体掌握度分数。
- 评估基于193名K-12学生在264场游戏会话中的数据，掌握度估计与学习增益显著相关（r=0.276, p=0.0001），与后测成绩显著相关（r=0.333,
  p<0.0001），且与前测成绩无相关性，验证了收敛效度和判别效度。
- 多智能体方法的预测效度（r=0.276，显著）约为单LLM基线（r=0.095，不显著）的3倍，表明领域分解和会话级推理在捕捉金融素养多维特性中发挥核心作用。
extract_result: success
impact_score:
  score: 3.5
  reason: 该论文提出了一种多智能体LLM与贝叶斯知识追踪（BKT）结合的架构Agentic BKT，用于严肃游戏中金融素养的隐式评估。虽然实验结果显示多智能体方法的预测效度约为单LLM基线的3倍（r=0.276
    vs r=0.095），且具备收敛效度和判别效度，但该研究属于高度垂直的学术场景（K-12金融素养教育游戏），样本量仅193人，属于小规模实验验证。对AI行业整体格局无实质冲击，属于特定学术子领域（AI教育评估）的一次有益探索，而非行业级事件。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: BKT与LLM多智能体结合的架构设计是否真的比纯数据驱动方法有实质优势，以及该架构能否泛化到其他学科领域
hype_assessment:
  level: low
  reason: 论文本身是arXiv预印本，属于正常学术发表，没有使用'颠覆'、'革命性'等PR话术。标题中的'Agentic'是对当前多智能体研究趋势的合理引用，而非炒作。论文提供了完整的实验设计、统计分析（含p值、Fleiss
    kappa、相关系数）和消融对比基线，学术诚信度较高。
information_entropy: high
domain_disruption:
  technical_innovation: 将贝叶斯知识追踪（BKT）与多智能体LLM架构结合，通过领域分解（风险/投资/支出/信用4个专业智能体）实现会话级行为推理，解决了单LLM无法捕捉金融素养多维特性的问题。这种'LLM语义理解+BKT概率追踪'的混合范式在AI教育评估领域具有一定创新性。
  business_model: 无。该研究属于纯学术探索，尚处于小样本概念验证阶段，距离商业化教育评估产品或SaaS服务还有显著距离。
engineering_complexity: prototype
compound_value:
  score: 3.5
  reason: 该论文展示了多智能体LLM架构在严肃游戏隐式评估中的有效性（预测效度3倍于单LLM基线），但这是一项纯粹的学术研究，而非商业化产品。从VC视角看：（1）样本量仅193名K-12学生，统计效力有限，尚需更大规模验证；（2）仅覆盖金融素养一个领域，跨领域通用性未经检验；（3）评估发生在严肃游戏场景中，该细分市场规模本身有限；（4）论文未提及任何公司、产品、开源项目或商业模式，纯属学术界的一次方法探索。该研究对多智能体评估范式的积累有一定学术价值，但转化为商业价值的路径不清晰，难以形成长期复利效应。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- Google DeepMind
competitive_casualty:
- 传统教育评估公司
- 标准化考试服务商
- 非LLM的知识追踪系统
market_opportunities:
- 教育科技公司可将该多智能体架构产品化为「游戏化隐式评估即服务」，为第三方严肃游戏开发者提供即插即用的学生能力评估SDK，按游戏会话或学生数量收费
- 金融素养之外，该领域分解+会话级推理的评估范式可直接迁移至STEM教育（如数学推理、科学素养）、数字素养、健康素养等其他多维能力领域，创业者可优先切入监管较宽松的企业培训场景
- 传统教育评估机构（如测评公司、考试服务商）可基于该思路开发新一代形成性评估工具，将隐式评估嵌入现有数字教材和教学游戏，替代周期性纸笔测试
risk_matrix:
  regulatory: K-12 学生数据受 COPPA/FERPA/GDPR-K 等法规严格保护，LLM 处理学生游戏行为数据用于评估需明确获得家长同意并保证数据不出境；若用于正式学业评分，各国教育评估法规（如中国教育评价改革政策、EU
    AI Act 高风险类别）可能要求算法审计和透明性披露
  technological: 当前单 LLM 基线几乎无效（r=0.095, 不显著），说明架构严重依赖领域分解和会话推理的设计，若 LLM 能力持续提升（GPT-5,
    Claude 4），单模型可能逐步追赶，削弱多智能体架构的差异化优势；此外 Fleiss kappa=0.624 为「基本一致」而非「完全一致」，LLM 分类与专家间仍有约
    38% 的不一致空间
  competitive: Khan Academy、Duolingo、Coursera 等拥有海量学习者行为数据的平台可快速复现类似方案，且数据规模远超百人级学术实验，可能形成数据飞轮效应碾压初创团队；Pearson、ETS
    等传统测评机构也可能通过收购或自研进入该赛道
  ethical: 「隐式评估」（stealth assessment）本质是学生在不知情下被评估，存在知情同意缺失和透明度问题；多智能体系统可能对特定文化背景或经济水平的学生产生系统性评估偏差（如金融素养评估天然偏向中产家庭认知框架）；若评估结果影响升学或分班决策，算法公平性风险将进一步放大
  additional:
  - 评估架构与特定游戏机制高度耦合，迁移到其他游戏或平台时需要大量定制化适配工作，限制了通用性
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
---

# Computer Science > Artificial Intelligence

# Title:Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games

View PDF HTML (experimental)Abstract:Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.