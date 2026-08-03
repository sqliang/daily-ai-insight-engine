---
title: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents'
source: https://arxiv.org/abs/2607.05682
author:
- '[[Yufeng Wang]]'
published: '2026-07-08'
created: '2026-07-08'
description: 'arXiv:2607.05682v1 Announce Type: new Abstract: LLM systems for scientific
  discovery increasingly assist with ideation, literature synthesis, experiment planning,
  and report generation, but the first research question they propose can remain difficult
  to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption
  that a scientist should inspect. We introduce FirstResearch, a first-principles
  research-question formation framework for scientific LLM agents whose core artifact
  is a structured Research Question Certificate. The certificate records primitive
  definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable
  hypothesis, a minimal decisive test, and a failure update rule, making the proposed
  question inspectable before downstream execution. On ten LLM-agent research topics,
  FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist,
  Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol.
  A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves
  the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the
  strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat
  ablation checkpoint further suggests that the certificate-centered core is the strongest
  component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under
  Gemini, while removing certificates drops below 1/5 under both judges. These results
  are preliminary and use LLM judges rather than human domain experts, but they support
  a narrow scientific-discovery claim: explicit derivation constraints are a promising
  mechanism for making LLM-generated scientific questions more auditable. Code, prompts,
  saved outputs, and reproduction scripts are available at https://github.com/louiswang524/FirstResearch.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: feed0d40c9ddb3b9
manifest_dates:
- '2026-07-08'
source_type: academic_paper
tldr: FirstResearch 是一个面向科学发现 LLM 代理的研究问题形成框架，通过结构化"研究问题证书"记录原始定义、假设、机制模型和可证伪假设，使问题在下游执行前可被审计。在十个主题上的实验显示其得分（4.86/5）优于
  AI co-scientist 等基线方法。
objective_summary: 研究人员提出了 FirstResearch，一个基于一阶原理的科学问题生成框架，专为 LLM 驱动的科学发现代理设计。该框架的核心产出是"研究问题证书"，包含原始定义、假设、机制模型、张力矛盾、可证伪假设、最小决定性测试和失败更新规则七项结构化内容。在十个
  LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory 和
  AI Scientist-v2 等基线方法，Gemini-2.5-Flash 独立重评也确认了该排名（4.86/5 vs 最强基线 4.38/5，Pearson
  一致性 0.865）。消融实验显示证书机制是最强组件，去除证书后得分降至 1/5 以下。结果尚属初步且使用 LLM 评审而非人类专家。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - DeepSeek
  - Google
  technologies:
  - LLM
  - FirstResearch
  - AI co-scientist
  - Agent Laboratory
  - AI Scientist-v2
  - Gemini-2.5-Flash
  key_people: []
key_logic_flow:
- FirstResearch 是一个面向科学发现 LLM 代理的一阶研究问题形成框架，其核心产出是结构化的"研究问题证书"。
- 该证书记录了原始定义、假设、机制模型、张力或矛盾、可证伪假设、最小决定性测试和失败更新规则七项内容，使提出的问题在下游执行前可被科学家检查。
- 在十个 LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory
  和 AI Scientist-v2 等基线方法。
- Gemini-2.5-Flash 独立评审对相同 40 个基线包的重新评分保持了系统级排名，FirstResearch 得分为 4.86/5，最强基线得分为 4.38/5，Pearson
  一致性达 0.865。
- 消融实验表明仅使用证书核心即可达到 4.90/5（DeepSeek）和 4.88/5（Gemini），而去除证书后得分降至 1/5 以下。
- 这些结果尚属初步阶段且使用 LLM 评审而非人类领域专家，但表明显式推导约束是让 LLM 生成科学问题更具可审计性的有前景机制。
specialized_tags:
  paper:
    paperTitle: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery
      Agents'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: Other
    methodType: LLM-based
extract_result: success
object_mentions:
- object_type: paper
  name: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery
    Agents'
  canonical_name: FirstResearch
  url: https://arxiv.org/abs/2607.05682
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - FirstResearch 是一个面向科学发现 LLM 代理的一阶研究问题形成框架，其核心产出是结构化的研究问题证书。
  - 在十个 LLM 代理研究主题上，FirstResearch 在 DeepSeek 盲评审协议下优于 AI co-scientist、Agent Laboratory
    和 AI Scientist-v2 等基线方法。
  - 消融实验表明仅使用证书核心即可达到 4.90/5（DeepSeek）和 4.88/5（Gemini），而去除证书后得分降至 1/5 以下。
  article_id: feed0d40c9ddb3b9
- object_type: project
  name: Research Question Certificate
  canonical_name: Research Question Certificate
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究问题证书记录了原始定义、假设、机制模型、张力或矛盾、可证伪假设、最小决定性测试和失败更新规则七项内容。
  - 消融实验表明证书机制是 FirstResearch 的最强组件，仅使用证书即可保持最高评分。
  article_id: feed0d40c9ddb3b9
impact_score:
  score: 4.5
  reason: 该论文提出研究问题证书框架，在LLM科学发现Agent的子领域内有增量贡献，但局限性明显：评估仅依赖LLM自评（非人类专家评审），样本量仅为10个科研主题，且结果尚未被独立复现。该工作有助于推动科研Agent的可审计性讨论，但远未达到改变局部竞争格局的程度。评分4.5分，属于学术圈内有一定关注度的方法论文献。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: LLM自评而非人类专家评审的评估方法是否可靠
hype_assessment:
  level: low
  reason: 论文措辞克制，明确标注'preliminary'（初步性）、'use LLM judges rather than human domain experts'等限定语。未使用'颠覆'、'革命性'等PR词汇。消融实验设计严谨，代码和复现脚本全部开源，无明显概念炒作成分。
information_entropy: medium
domain_disruption:
  technical_innovation: 提出研究问题证书（Research Question Certificate）框架，以原始定义、假设、机制模型、矛盾/张力、可证伪假设、最小决定性测试和失败更新规则七要素结构化LLM科研问题生成过程，使问题推导链可审计、可审查。
  business_model: 无
engineering_complexity: prototype
compound_value:
  score: 7.0
  reason: FirstResearch 的核心价值在于提出了'研究问题证书(RQC)'这一结构化审计机制，本质上是 AI 科学发现领域的可信中间件。从 VC
    视角看，这解决了 LLM 科研 Agent 的核心痛点：黑箱式问题生成让研究人员无法信任输出。RQC 的七要素（定义、假设、机制、矛盾、可证伪假设、最小决定性测试、失败更新规则）构建了完整的可审计链路，消融实验显示移除证书后评分从
    4.90/5 骤降至 1/5 以下，说明该机制是关键差异化组件。长期复利逻辑在于：若 AI for Science 从'炫技'走向'可信生产力工具'，可审计的问题生成将成为强制性要求，RQC
    或其衍生标准可成为该赛道的审核基础设施层，具备类似 MCP 在 Agent 工具调用中的中间件粘性。但风险不可忽视：(1) 评估基于 LLM Judge 而非人类领域专家，存在
    Self-reinforcing 偏差风险；(2) 仅覆盖 10 个 LLM Agent 主题，泛化能力存疑；(3) 学术开源项目面临大厂快速复制的竞争——一旦
    OpenAI/Google 将类似机制内嵌到产品中，独立框架的生态位会被挤压。综合评分 7.0，这是 AI for Science 中间件方向的优质早期标的，具备细分标准潜力，但需看到人类专家验证和跨领域泛化证据才能上调至基石级评分。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- DeepSeek
- Google DeepMind
- AI for Science 开源社区
- 学术研究实验室
competitive_casualty:
- 闭源 AI Scientist 系统
- 缺乏审计机制的科研 Agent 平台
- 传统科研辅助工具
market_opportunities:
- 科研管理平台可集成该证书框架作为AI生成研究问题的质量审计模块，服务于药企、学术机构和R&D团队的科研流程合规化需求
- 开发者可基于开源的证书机制构建科研Agent的审计插件/中间件，赋予现有科学发现Agent（如AI Scientist系列）可审计的研究问题生成能力
- 该框架可拓展至商业场景中的AI提案与假设生成审计，用于战略咨询、产品创新和研发管线的可追溯性管理
risk_matrix:
  regulatory: 目前无直接监管风险，但若未来AI辅助科研被纳入研究诚信审查框架，此类审计工具可能成为合规要求，反而带来正向合规价值
  technological: 当前评估仅基于LLM评审而非人类领域专家，结果可能无法完全泛化到真实科研场景；若后续人类专家验证不通过或发现评估偏差，框架核心主张将大幅削弱
  competitive: Google（AI co-scientist）和DeepSeek等已有相近研究或产品线，若它们将类似审计机制直接内置于自有平台，将挤压独立框架的采用空间
  ethical: 证书机制可能造成'审计幻觉'——结构化证书不等于科学质量过关，过度依赖形式化审计可能掩盖深层假设缺陷，反而降低科研人员的批判性审查意识
  additional: []
confidence:
  impact: medium
  compound: low
  hype: low
actionable_insight: monitor
paper_metadata:
  title: 'FirstResearch: Auditable Question Formation for LLM Scientific Discovery
    Agents'
  authors: []
  affiliations: []
  venue: arXiv preprint
  paper_url: https://arxiv.org/abs/2607.05682
  code_url: null
  dataset_url: null
research_problem:
  core_question: 如何让LLM科学发现智能体生成的研究问题变得可审计、可检验，使科学家能够在执行下游实验前审查问题质量？
  motivation: LLM科学发现系统在提出研究问题时往往缺乏透明度，问题听起来合理但隐藏了底层假设、作用机制和可证伪条件，科学家难以评估这些问题的有效性和可靠性。现有系统（如AI
    co-scientist、Agent Laboratory、AI Scientist-v2）直接输出研究问题，缺乏结构化、可审计的中间表示，导致科学家只能依赖直觉判断问题质量。
  significance: practical
  gap_addressed: 现有LLM科学发现系统在生成研究问题时缺乏结构化的可审计性机制，无法显式暴露问题的原始定义、假设、机制模型、矛盾张力、可证伪假设、最小决定性测试和失败更新规则，科学家难以在投入资源前系统性地审查问题质量。
methodology:
  approach_summary: FirstResearch提出了一个基于第一性原理的研究问题形成框架，其核心创新是结构化的'研究问题证书'（Research
    Question Certificate），包含七个要素：原始定义（primitive definitions）、假设（assumptions）、机制模型（mechanism
    model）、矛盾张力（tension/contradiction）、可证伪假设（falsifiable hypothesis）、最小决定性测试（minimal
    decisive test）和失败更新规则（failure update rule）。该框架通过显式的推导约束迫使LLM暴露每个要素，使研究问题在下游执行前就可供科学家逐项审查。在10个LLM智能体研究主题上，与AI
    co-scientist、Agent Laboratory和AI Scientist-v2三个基线进行了对比评估。
  novelty_type: algorithmic
  key_innovations:
  - 研究问题证书（Research Question Certificate）—— 七要素结构化表示，使LLM生成的研究问题从黑盒输出变为可逐项审计的透明构件
  - 明确的推导约束机制，迫使LLM显式暴露原始假设、机制建模和可证伪条件，而非隐式生成语义流畅但不可检验的问题
  - 失败更新规则（failure update rule）—— 当假设被证伪时系统如何更新推理的闭环机制，增强了科学推理的完整性
  - 将波普尔可证伪性原则系统性地嵌入LLM提示框架，弥合了科学哲学与LLM代理之间的方法论鸿沟
  inspiration_sources:
  - 波普尔的可证伪性科学哲学
  - AI co-scientist
  - Agent Laboratory
  - AI Scientist-v2
  - 结构化论证框架
  technical_depth: moderate
experimental_rigor:
  benchmark_coverage: 在10个LLM智能体研究主题上评估，涵盖该领域内多个研究方向，但具体主题领域未详细列出，评估范围的广度不够明确
  baseline_comparison: adequate
  ablation_quality: thorough
  reproducibility_level: mostly_reproducible
  claimed_improvement: 在DeepSeek盲评协议下FirstResearch得分为4.86/5，最强基线（AI co-scientist/Agent
    Laboratory/AI Scientist-v2之一）为4.38/5；Gemini-2.5-Flash独立重评保持系统级排名，Pearson相关系数为0.865；消融实验显示证书核心是最强组件，移除证书后评分降至1/5以下
limitations_and_honesty:
  stated_limitations:
  - 结果为初步性质（preliminary results）
  - 使用LLM作为评判者而非人类领域专家
  - 评估规模有限（10个主题）
  - 结果需要进一步验证
  reviewer_concerns:
  - LLM自我评估的可信度问题——DeepSeek评判FirstResearch本身可能存在偏差，尽管采用了盲评协议
  - 仅与3个基线对比，覆盖不够全面，缺少与更多无证书方法的系统比较
  - 10个评估主题规模有限，统计显著性存疑
  - 缺少与人类专家评估的相关性分析，无法判断证书是否真正帮助科学家做出更好的判断
  - 研究问题'质量'的度量标准不够明确，评分标准可能偏向结构化输出的形式而非科学实质
  - 缺乏对下游任务（如实际实验设计）中证书实用性的端到端验证
  - 证书框架的通用性未验证——是否适用于非LLM相关的自然科学领域
  overclaiming_assessment: honest
  generalization_concern: 论文仅在LLM智能体研究主题上评估，未涉足更广泛的自然科学领域（如生物学、化学、物理学），证书框架的结构化要素在不同科学范式中的适配性未经检验。此外，10个主题的评估规模不足以支撑强泛化性声明。
industrial_relevance:
  applicable_domains:
  - 科学发现自动化
  - AI研究辅助工具
  - 学术同行评审辅助
  - 科研项目立项评估
  - 研发质量管理与审计
  compute_requirements: commodity
  integration_readiness: needs_research
  cost_efficiency_analysis: 基于LLM API调用的架构，算力需求较低（commodity级别），但证书框架需要多轮结构化生成，相比直接输出研究问题的方法增加了推理成本（约7个结构化要素的额外产出）。当前阶段主要价值在于研究验证和概念证明，距离工业级产品部署尚缺人类专家验证、跨领域泛化测试以及与下游实验工具链的集成。若后续验证有效，该框架可作为AI科学发现平台的质量保障模块，边际成本较低但能显著提升结果的可审计性和可信度。
related_work_context:
  closest_prior_works:
  - AI co-scientist
  - Agent Laboratory
  - AI Scientist-v2
  advancement_over_prior: 现有LLM科学发现系统（AI co-scientist、Agent Laboratory、AI Scientist-v2）直接生成研究问题，输出语义流畅但缺乏可审查的中间结构，科学家无法追溯问题背后的假设和推理链路。FirstResearch通过研究问题证书框架，将问题生成过程分解为7个可独立审查的结构化要素，使每个假设、机制和可证伪条件都显式呈现，实现了从'黑盒输出'到'透明可审计'的跃迁。论文实验数据也支持了这一进步：在DeepSeek和Gemini双评判协议下，FirstResearch显著优于所有基线。
  opens_new_direction: true
  potential_follow_ups:
  - 引入人类领域专家评估系统，验证研究问题证书在实际科研场景中的效用
  - 将证书框架扩展到更广泛的自然科学领域（生物学、化学、物理学等），检验跨领域通用性
  - 自动化证书质量评分与验证机制，减少对LLM评判者的依赖
  - 将研究问题证书与下游实验执行（实验设计、数据分析）进行端到端集成
  - 多轮迭代式证书优化——基于失败更新规则的多轮改进机制
  - 开发可视化工具帮助科学家直观审查和理解证书结构
object_insights:
- object_type: project
  name: Research Question Certificate
  canonical_name: Research Question Certificate
  url: null
  positioning: FirstResearch 框架的核心结构化产出，通过记录原始定义、假设、机制模型等七项内容使 LLM 生成的研究问题在下游执行前可被科学家审计检查。
  technical_signal: 证书机制通过显式推导约束使 LLM 科学问题生成更具可审计性，消融实验中仅使用证书即可达到 4.90/5（DeepSeek）和
    4.88/5（Gemini）的最高评分。
  adoption_signal: 在十个 LLM 代理研究主题上验证，Gemini-2.5-Flash 独立重评确认系统级排名，Pearson 一致性达 0.865。
  ecosystem_relevance: 与 AI co-scientist、Agent Laboratory、AI Scientist-v2 等主流科学发现代理框架的方法进行系统比较并显著优于它们。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Research Question Certificate 为 LLM 科学发现代理提供了首个结构化可审计问题形成机制，解决了黑箱问题生成的关键痛点，实验结果显著优于现有基线且消融研究证明证书组件贡献最大，具有推动科学
    AI 透明化的潜力。
  risk_notes:
  - 实验结果尚属初步阶段，仅使用 LLM 评审而非人类领域专家验证。
  - 证书机制的有效性可能受限于底层 LLM 自身的推理能力和知识边界。
  score: 7.0
  article_ids:
  - feed0d40c9ddb3b9
  evidence_snippets:
  - 研究问题证书记录了原始定义、假设、机制模型、张力或矛盾、可证伪假设、最小决定性测试和失败更新规则七项内容。
  - 消融实验表明证书机制是 FirstResearch 的最强组件，仅使用证书即可达到接近满分（4.90/5）的评分，去除证书后得分降至 1/5 以下。
  - FirstResearch 在十个 LLM 代理研究主题上以 4.86/5 平均得分优于 AI co-scientist 等基线方法（最强基线 4.38/5），Gemini
    独立重评确认排名且 Pearson 一致性达 0.865。
---

# Computer Science > Artificial Intelligence

# Title:FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents

View PDF HTML (experimental)Abstract:LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption that a scientist should inspect. We introduce FirstResearch, a first-principles research-question formation framework for scientific LLM agents whose core artifact is a structured Research Question Certificate. The certificate records primitive definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable hypothesis, a minimal decisive test, and a failure update rule, making the proposed question inspectable before downstream execution. On ten LLM-agent research topics, FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist, Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol. A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat ablation checkpoint further suggests that the certificate-centered core is the strongest component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under Gemini, while removing certificates drops below 1/5 under both judges. These results are preliminary and use LLM judges rather than human domain experts, but they support a narrow scientific-discovery claim: explicit derivation constraints are a promising mechanism for making LLM-generated scientific questions more auditable. Code, prompts, saved outputs, and reproduction scripts are available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.