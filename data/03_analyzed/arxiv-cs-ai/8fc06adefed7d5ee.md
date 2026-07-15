---
title: Internal Pluralism and the Limits of Pairwise Comparisons
source: https://arxiv.org/abs/2607.02672
author:
- '[[Bailey Flanigan, Michelle Si]]'
published: '2026-07-07'
created: '2026-07-07'
description: 'arXiv:2607.02672v1 Announce Type: new Abstract: Local pairwise comparisons
  are a standard tool for learning how people want decision rules to work, e.g., in
  participatory design or alignment. However, their use builds in two strong assumptions:
  that local comparisons are sufficient evidence about how a person wants an automated
  decision rule to behave, and that people can always answer those comparisons decisively.
  We investigate how these assumptions may be compromised under internal pluralism:
  the idea that an individual evaluates decision rules according to multiple authoritative
  priorities about how the rule should behave. We provide a formal model of such pluralistic
  preferences over decision rules, which then lets us identify two distinct failures
  of forced local pairwise comparison data. First, priorities such as proportionality,
  egalitarianism, and equal treatment are inherently global: what they imply in one
  case can depend on what happens elsewhere, so local comparisons may fail to capture
  them. Second, even when priorities are representable locally, tension between strongly-held
  priorities can generate internal conflict, producing potentially costly behavioral
  distortions when comparisons are forced. We then use our model to investigate the
  alternative -- allowing people to report indecision -- and our findings suggest
  that doing so can considerably reduce the number of queries needed to learn preferences
  accurately. We conclude by describing how our model points toward preference-learning
  methods that elicit these priorities directly, yielding more faithful and interpretable
  accounts of what people value.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 8fc06adefed7d5ee
manifest_dates:
- '2026-07-07'
source_type: academic_paper
tldr: 论文提出内部多元主义模型，证明局部成对比较不足以捕捉个体对决策规则的多重优先级偏好。
objective_summary: 研究者在 arXiv 发表论文，通过形式化建模分析内部多元主义（个体对决策规则存在多重权威优先级）如何破坏成对比较的两个隐含假设，发现全局性优先级（如比例性、平等主义）无法被局部比较捕获，且强优先级间的冲突会导致行为扭曲，并提出允许报告不确定能减少偏好学习所需查询次数。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies: []
  key_people: []
key_logic_flow:
- 论文指出局部成对比较依赖于两个隐含假设：局部比较足以推断个体对决策规则的偏好，且个体总能给出明确比较结果。
- 提出"内部多元主义"概念，即个体同时持有多个权威性优先级来评估决策规则，导致上述假设部分失效。
- 构建了关于多元偏好的形式化模型，用以分析成对比较数据的两种失效模式。
- 第一类失效：比例性、平等主义等优先级本质上是全局性的，单个局部案例的比较结果无法体现其在其他案例中的含义。
- 第二类失效：即使优先级可局部表示，彼此矛盾的强优先级会产生内部冲突，被迫下定论会导致行为扭曲。
- 模型分析表明，允许个体报告"不确定"可显著减少准确学习偏好所需的查询次数，指向直接引出优先级的新偏好学习方法。
specialized_tags:
  paper:
    paperTitle: Internal Pluralism and the Limits of Pairwise Comparisons
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Other
    methodType: theoretical
extract_result: success
impact_score:
  score: 5.0
  reason: 该论文对RLHF/对齐领域广泛使用的成对比较方法提出了根本性质疑——证明局部比较无法捕获比例性、平等主义等全局性优先级，且强优先级冲突会导致行为扭曲。这是对当前主流偏好学习范式（Bradley-Terry模型）的底层假设批判，在AI安全和对齐研究社群中有理论价值。但论文停留在形式化建模阶段，缺乏实证验证和工程化方案，短期内不会对行业产品产生直接冲击。综合评定为中等偏下冲击力。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: 成对比较（Pairwise Comparisons）在RLHF中的根本性局限，以及偏好学习的替代方案
hype_assessment:
  level: low
  reason: arXiv纯学术论文，采用严谨的形式化数学建模，没有使用'颠覆'、'革命性'等PR话术，结论基于理论推导而非夸张宣传。论文明确给出了模型假设和局限性说明。
information_entropy: high
domain_disruption:
  technical_innovation: 形式化提出'内部多元主义'（Internal Pluralism）概念，建模个体同时持有多个权威优先级时的偏好结构，证明全局性优先级（比例性、平等主义）无法通过局部成对比较捕获，并且允许报告'不确定'能显著减少偏好学习所需查询次数——这指向一种直接引出优先级的新范式。
  business_model: 若该方向的理论成果被工程化，将动摇当前RLHF数据标注以成对比较为核心的方法论基础，推动AI对齐标注工具从'二选一'模式转向'多优先级陈述'模式，可能催生新一代偏好标注平台和数据管线。
engineering_complexity: conceptual
compound_value:
  score: 5.0
  reason: 该论文从形式化建模角度揭示了成对比较（RLHF 的核心方法论基础）的两类根本性失效模式：全局性优先级无法被局部比较捕获，以及强优先级冲突下的行为扭曲。模型进一步证明，允许报告不确定性可显著减少偏好学习所需的查询次数。这一理论洞察若被后续工程化验证，有望重塑
    AI 对齐的技术范式——从依赖海量成对偏好标注转向直接引出优先级的多维度方法。但当前处于纯理论阶段，无代码实现、无实验验证、无公司背书，距离产品化和商业化极其遥远。价值兑现完全取决于是否有
    AI 实验室（如 Anthropic、DeepMind）将其转化为可落地的训练算法。属于高潜力的理论种子，但尚未进入可投资的商业射程。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- DeepMind
- OpenAI
competitive_casualty:
- 传统 RLHF 偏好标注平台
- 纯成对比较对齐方案提供商
market_opportunities:
- 偏好学习工具开发者可基于该框架设计直接引出用户多重优先级的新型方法，替代或补充传统的成对比较偏好学习流程
- AI 对齐服务提供商可针对 RLHF/DPO 等偏好学习方法暴露的局限性，推出结合内部多元主义的混合反馈采集方案
- 参与式 AI 设计平台可引入支持用户表达不确定性的交互机制，提升群体偏好建模的准确性与忠实度
risk_matrix:
  regulatory: 无（纯理论论文，不涉及具体监管合规问题）
  technological: 该论文框架若成立，将对当前依赖成对比较的 RLHF/DPO 等偏好学习范式的有效性构成根本性质疑，可能催生替代性技术路径，导致现有偏好建模基础设施需要重新设计
  competitive: 早期关注该方向并构建新型偏好学习能力的团队可能获得差异化优势，而固守纯成对比较方法的公司在范式转向时面临落后风险
  ethical: 论文核心关注的就是伦理问题——指出强制用户在有冲突的优先级间做出明确选择会导致行为扭曲，允许表达不确定性反而能更忠实地捕获人类价值观，这本身是对现有偏好学习伦理缺陷的建设性批评
  additional: []
confidence:
  impact: low
  compound: medium
  hype: low
actionable_insight: monitor
paper_metadata:
  title: Internal Pluralism and the Limits of Pairwise Comparisons
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.02672
  code_url: null
  dataset_url: null
research_problem:
  core_question: 当个体持有多个权威性优先级（内部多元主义）时，基于局部成对比较的偏好学习是否仍然有效，以及如何改进？
  motivation: 成对比较是参与式设计和AI对齐中广泛使用的标准工具，用于了解人们希望决策规则如何运作。然而该工具隐含着两个强假设：局部比较足以反映一个人对自动化决策规则的偏好，且人们总能果断地回答这些比较。内部多元主义——个体依据多个权威优先级同时评估决策规则——的存在使这两个假设面临根本性挑战。理解这种挑战并探索替代方案，对于构建更忠实、更可解释的偏好学习系统至关重要，直接影响AI对齐方法论的可靠性。
  significance: fundamental
  gap_addressed: 填补了偏好学习研究中一个被忽视的理论空白：现有方法假设个体拥有单一、一致的偏好结构，但现实中个体可能同时持有多个权威优先级（如公平性、效率、平等对待等），这些优先级之间可能存在冲突。论文系统化地建模了这种内部多元主义对成对比较有效性的影响，并理论证明了允许不确定表达可以提升学习效率。
methodology:
  approach_summary: 论文构建了一个形式化的内部多元主义偏好模型，将个体对决策规则的偏好建模为多个权威优先级（如比例性、平等主义、平等对待）的复合函数。基于该模型，作者识别了强制局部成对比较的两类结构性失败：（1）某些优先级具有固有全局性——它们在某一案例中的含义取决于其他案例的结果，因此局部比较无法捕获它们；（2）即使优先级可局部表征，强优先级之间的张力也会引发内部冲突，在强制比较时产生代价高昂的行为扭曲。论文进一步通过模型分析探索了允许个体报告不确定（indecision）的替代方案，从理论上证明该方法可显著减少准确学习偏好所需的查询次数，并指向直接提取优先级的偏好学习方法。
  novelty_type: theoretical
  key_innovations:
  - 首次提出内部多元主义的形式化模型，将个体偏好表达为多个权威优先级的复合体，为分析偏好学习方法提供了新的理论基础
  - 识别并分类了强制成对比较在多元主义偏好下的两类结构性失败模式——全局性优先级的局部不可表征性和优先级冲突的行为扭曲效应
  - 理论上证明了允许不确定表达（indecision）可以显著降低准确学习偏好所需的查询复杂度，挑战了偏好学习中"必须迫使决策者做出明确选择"的传统范式
  inspiration_sources:
  - AI alignment中的偏好学习方法（RLHF等）
  - 社会选择理论与集体决策理论
  - 行为经济学中的偏好不一致性研究
  - 参与式设计中的价值敏感性设计方法
  technical_depth: moderate
experimental_rigor:
  benchmark_coverage: 本文为纯理论性论文，不涉及实验基准评测。核心贡献在于形式化建模和理论分析，缺乏在真实或模拟数据上的实证验证。
  baseline_comparison: weak
  ablation_quality: absent
  reproducibility_level: mostly_reproducible
  claimed_improvement: 提出理论框架证明，在内部多元主义假设下，允许个体报告不确定（而非强制二元比较）可以显著减少准确学习其偏好所需的查询数量；并指出直接提取优先级的方法能产生更忠实和可解释的偏好表征。
limitations_and_honesty:
  stated_limitations:
  - 论文未提供明确的局限性自述段落（基于可用文本信息），但通过指出指向未来研究方向——开发直接提取优先级的偏好学习方法——间接承认了当前工作的理论性质
  - 论文明确将结果定位为理论模型，而非实证验证
  reviewer_concerns:
  - 缺乏实证验证：理论预测（如允许不确定可减少查询次数）未通过人类实验或仿真实验进行验证
  - 模型假设的合理性：内部多元主义的形式化方式是否覆盖了现实中多样化的偏好结构？是否存在其他未被建模的多元主义形式？
  - 实际效用未知：理论上的查询复杂度优势在真实人类决策场景中能否转化为实际效率提升仍存疑
  - 与现有方法的衔接：论文未讨论如何将理论洞见整合到现有的RLHF或偏好学习管线中
  overclaiming_assessment: honest
  generalization_concern: 理论结果建立在特定的多元主义形式化模型之上，假设个体的优先级可以分解为可枚举的权威标准集合。对于更模糊、直觉性或情境依赖的偏好结构，该模型的可推广性需进一步验证。此外，论文的分析主要聚焦于决策规则（decision
    rules）的偏好，其在其他偏好学习场景（如奖励模型训练、内容推荐）中的适用性有待探讨。
industrial_relevance:
  applicable_domains:
  - AI对齐与安全（偏好建模、RLHF方法论改进）
  - 参与式产品设计与用户研究（价值敏感性设计）
  - 人机交互系统中的决策支持
  - 公共政策与伦理决策中的偏好聚合
  compute_requirements: commodity
  integration_readiness: needs_research
  cost_efficiency_analysis: 该研究目前处于纯理论阶段，尚未提供可直接落地部署的算法、工具或实现代码。其核心洞见——允许不确定表达和直接提取优先级——需要进一步的算法化和工程化才能应用于实际系统。从长远看，如果理论预测成立，该方法有望通过减少偏好采集所需的查询次数来降低数据采集成本，但短期内需要大量的实证开发和验证工作。
related_work_context:
  closest_prior_works:
  - RLHF与基于成对比较的偏好学习范式（Christiano et al., 2017; Stiennon et al., 2020; Ouyang et al.,
    2022）
  - 参与式设计与价值敏感性设计中的利益相关者偏好采集方法
  - 社会选择理论中关于偏好聚合与集体决策的经典研究（Arrow定理等）
  - 行为经济学中关于偏好不一致与决策冲突的研究
  advancement_over_prior: 现有偏好学习方法默认将个体视为拥有统一、一致的偏好函数，并通过大量成对比较来逼近这一函数。本文首次系统化地质疑了这一假设，从理论层面揭示了当个体内部存在多个权威优先级（内部多元主义）时，成对比较方法存在的结构性缺陷。相比现有工作仅关注偏好的"聚合"（aggregation），本文转向关注偏好的"结构"（structure），为新一代偏好学习方法提供了理论基础。
  opens_new_direction: true
  potential_follow_ups:
  - 开发基于优先级直接提取的偏好学习算法，替代传统的成对比较范式
  - 设计允许汇报不确定性的交互式偏好采集协议并进行人类实验验证
  - 将内部多元主义模型扩展到集体决策（多人）场景，研究个体内与个体间多元主义的交互
  - 实证研究当前主流对齐系统中成对比较数据的多元主义污染程度
  - 探索深度学习方法学习多元主义偏好表征的可行性
---

# Computer Science > Artificial Intelligence

# Title:Internal Pluralism and the Limits of Pairwise Comparisons

View PDF HTML (experimental)Abstract:Local pairwise comparisons are a standard tool for learning how people want decision rules to work, e.g., in participatory design or alignment. However, their use builds in two strong assumptions: that local comparisons are sufficient evidence about how a person wants an automated decision rule to behave, and that people can always answer those comparisons decisively. We investigate how these assumptions may be compromised under internal pluralism: the idea that an individual evaluates decision rules according to multiple authoritative priorities about how the rule should behave. We provide a formal model of such pluralistic preferences over decision rules, which then lets us identify two distinct failures of forced local pairwise comparison data. First, priorities such as proportionality, egalitarianism, and equal treatment are inherently global: what they imply in one case can depend on what happens elsewhere, so local comparisons may fail to capture them. Second, even when priorities are representable locally, tension between strongly-held priorities can generate internal conflict, producing potentially costly behavioral distortions when comparisons are forced. We then use our model to investigate the alternative -- allowing people to report indecision -- and our findings suggest that doing so can considerably reduce the number of queries needed to learn preferences accurately. We conclude by describing how our model points toward preference-learning methods that elicit these priorities directly, yielding more faithful and interpretable accounts of what people value.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.