---
title: 'Representation Affects Retrieval: A Case Study of Skill Discovery and Routing
  in a Multimodal Agent Harness'
source: https://arxiv.org/abs/2608.20389
author:
- '[[Kevin Dela Rosa]]'
published: '2026-08-24'
created: '2026-08-24'
manifest_dates:
- '2026-08-24'
description: 'arXiv:2608.20389v1 Announce Type: new Abstract: A production agent harness
  must discover and rank, from a growing library of skills, the one most appropriate
  for a user''s task. At small scale this selection happens in context: the LLM planner
  chooses among skill representations exposed in its system prompt, without an explicit
  embedding-based retrieval step. We treat this in-context selection as the small-N
  counterpart to embedding-based skill retrieval at scale, and present a case study
  of how Tinycloud, a production multimodal video agent harness, represents its skills
  for the planner. The harness ships skills under two recurring representations: tool-skills
  that wrap a single external API or system tool and serve as primitive vocabulary,
  and workflow-skills that orchestrate tool-skill calls plus a template render to
  produce one named deliverable. The harness exposes them via two surfaces in the
  system prompt: an inlined-body surface (full instructions, scripts, templates) for
  autoloaded skills, and a one-line listing for on-demand skills. A six-task selection
  ablation across three exposure regimes (all-on, default, all-off) shows that full
  autoload selects the gold skill on every task; all-off slows execution and produces
  hard discovery failures; and the production default misroutes one task because its
  lexical signal collides with an autoloaded tool-skill that pulls planner attention
  away from a listed workflow-skill. The headline finding is that in-prompt exposure
  of skills is not monotonically helpful: partial exposure can create lexical competition
  that suppresses correct selection. We connect this small-N observation to recent
  retrieval-based skill-routing work at large scale, and frame this contribution as
  a case study rather than a benchmark.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 5e7a1c6cfddad775
source_type: academic_paper
tldr: 论文以生产级多模态视频智能体 harness Tinycloud 为案例，研究技能表示如何影响 LLM 规划器的上下文内选择。六任务消融实验显示，提示词内技能暴露并非单调有益，部分暴露会造成词汇竞争并抑制正确路由选择。
objective_summary: 这篇 arXiv 论文以 Tinycloud 生产级多模态视频智能体 harness 为案例，研究技能表示对 LLM 规划器上下文内选择的影响。Tinycloud
  将技能分为封装单一外部 API 的工具技能与编排调用并生成命名交付物的流程技能，并通过内联正文与单行列表两种表面暴露给规划器。六任务消融实验对比全开、默认、全关三种暴露模式，结果显示全自动加载在每项任务上选中黄金技能，全关闭拖慢执行并产生硬性发现失败，而生产默认配置在一个任务上因词汇信号冲突而错误路由。论文的核心结论是技能暴露并非越多越好，并将这一小规模观察与大规模嵌入检索式技能路由研究联系起来。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - multimodal agent harness
  - tool-skills
  - workflow-skills
  - skill routing
  - embedding-based retrieval
  - LLM planner
  - in-context selection
  key_people: []
key_logic_flow:
- 论文以生产级多模态视频智能体 harness Tinycloud 为例，研究其技能在系统提示词中的表示方式如何影响 LLM 规划器的上下文内选择。
- Tinycloud 的技能分为两类：封装单一外部 API 或系统工具的工具技能，以及编排工具技能调用并渲染模板以产生命名交付物的流程技能。
- 系统提示词通过两种表面暴露技能：内联正文表面承载完整指令、脚本与模板用于自动加载技能，单行列表则用于按需技能。
- 六任务消融实验对比全开、默认、全关三种暴露模式，结果显示全自动加载在每项任务上都选中黄金技能，全关闭则拖慢执行并产生硬性发现失败。
- 生产默认配置在一个任务上发生错误路由，因为其词汇信号与自动加载的工具技能冲突，把规划器注意力从列出的流程技能上引开。
- 核心结论是提示词内技能暴露并非单调有益，部分暴露可能产生词汇竞争从而抑制正确选择，论文将其定位为案例研究而非基准评测。
object_mentions:
- object_type: project
  name: Tinycloud
  canonical_name: Tinycloud
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Tinycloud 是一个生产级多模态视频智能体 harness，论文以它为例研究技能表示对规划器选择的影响。
  - Tinycloud 将技能组织为工具技能与流程技能两类，并通过系统提示词中的内联正文与单行列表两种表面暴露给 LLM 规划器。
  - 针对 Tinycloud 的六任务消融实验表明，全自动加载在每项任务上都选中黄金技能，而生产默认配置会因词汇竞争错误路由一个任务。
  article_id: 5e7a1c6cfddad775
extract_result: success
compound_value:
  score: 5.5
  reason: 论文揭示'提示词内技能暴露并非单调有益'这一反直觉结论，并用生产级 harness（Tinycloud）的实际错误路由案例说明：当技能库扩大，词汇竞争会使上下文内选择失效，大规模场景必须转向
    embedding 检索式路由。该设计原则会沉淀为 agent 中间件层的通用实践，具备知识复利——任何构建 agent harness 的团队（Anthropic/OpenAI/LangChain
    等）都会遇到并复用这一洞见，后续检索式路由的实证工作大概率会引用并扩展它。但作为单一产品案例研究而非基准评测，缺乏跨平台定量验证，短期直接转化为产品与收入的路径尚不清晰；技能路由层的标准化（如
    MCP 生态演化）仍处早期，3-5 年后能否成为独立行业基石取决于路由层能否从模型能力中剥离为可投资的独立基础设施，故给予 5.5 分，处于'细分赛道基础设施待验证'区间。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- OpenAI
- LangChain
- Pinecone
competitive_casualty:
- 依赖全量技能内联的 Agent 平台
- 未引入检索式路由的闭源 Agent harness
- 传统 RPA 厂商
market_opportunities:
- 面向 Agent 平台可开发技能暴露配置的自动化消融测试与调优工具，帮助团队在生产部署前验证技能库表示方式，规避词汇竞争导致的错误路由
- 多模态视频等垂直场景的 Agent 技能库管理存在服务缺口，可提供技能元数据规范化、词汇冲突检测与路由审计等咨询或 SaaS 能力
- 随着技能路由从上下文内选择走向嵌入检索，可提前布局'上下文+检索'混合路由中间件方案，服务拥有中大规模技能库的 Agent 团队
risk_matrix:
  regulatory: 无
  technological: 该结论基于单一 harness 与六任务的小样本案例研究，泛化性有限；技能库规模扩大后路由范式可能整体转向嵌入检索，上下文内暴露相关结论的适用窗口较短
  competitive: 主流 Agent 框架与模型厂商正快速内化技能路由最佳实践，该发现若被写入平台级默认配置，独立团队的差异化窗口将非常短暂
  ethical: 技能误路由可能使多模态智能体在真实业务中执行错误动作，带来可靠性信任风险；技能库持续扩增后，误导性或恶意技能描述可能污染路由决策，形成数据投毒类安全隐忧
  additional:
  - Tinycloud 为生产系统案例，其实现细节与评测数据可能不公开，可复现性存疑
  - 论文定位为案例研究而非基准评测，未经同行评审，结论强度有限
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Tinycloud
  canonical_name: Tinycloud
  url: null
  positioning: Tinycloud 是一个生产级多模态视频智能体 harness，将技能组织为工具技能与流程技能两类，并通过系统提示词暴露给 LLM
    规划器进行上下文内选择。
  technical_signal: 论文核心发现是提示词内技能暴露并非单调有益，部分暴露会因词汇竞争抑制正确路由选择。
  adoption_signal: 作为生产级 harness，Tinycloud 已在实际生产环境运行，其六任务消融实验直接基于生产默认配置展开。
  ecosystem_relevance: 论文将小规模上下文内技能选择与大尺度嵌入检索式技能路由研究相关联，对多模态智能体技能编排生态有参考意义。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该论文揭示了“技能暴露越多越好”的反直觉结论，即部分暴露会因词汇竞争抑制正确路由，这对生产级多模态智能体的技能编排与提示词设计具有直接指导意义，值得持续跟踪其后续研究与方法论演进。
  risk_notes:
  - 论文明确将其定位为案例研究而非基准评测，六任务样本量较小，结论的普适性有待更大规模验证。
  - Tinycloud 的具体实现细节未在论文中充分披露，外部难以独立复现其词汇竞争与错误路由结论。
  score: 6.0
  article_ids:
  - 5e7a1c6cfddad775
  evidence_snippets:
  - Tinycloud 是一个生产级多模态视频智能体 harness，论文以它为例研究技能表示对规划器选择的影响。
  - Tinycloud 将技能组织为工具技能与流程技能两类，并通过系统提示词中的内联正文与单行列表两种表面暴露给 LLM 规划器。
  - 针对 Tinycloud 的六任务消融实验表明，全自动加载在每项任务上都选中黄金技能，而生产默认配置会因词汇竞争错误路由一个任务。
impact_score:
  score: 2.8
  reason: 评分依据：这是一篇自我定位为 case study 的 arXiv 论文，六任务消融实验验证了'提示词内技能暴露并非单调有益'这一反直觉结论，对
    agent 系统提示词工程与技能路由实践有一定启发。但样本规模极小（单一私有 harness、6 个任务），无新算法、无开源代码、无产品发布，属于技术社区内的小范围观察性贡献，短期不改变任何竞争格局，因此给予
    2.8 分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 技能在系统提示词中的暴露方式（自动加载 vs 按需列出）如何影响 LLM 规划器的路由准确性，尤其是词汇竞争导致的错误路由问题
hype_assessment:
  level: low
  reason: 判定依据：论文明确自我限定为 case study 而非 benchmark，完整披露了失败案例（生产默认配置因词汇信号冲突在一个任务上错误路由），结论附带边界条件，全文无'颠覆''革命性'等
    PR 滥用词汇，属于诚实的小规模实证观察，炒作水分极低。
information_entropy: medium
domain_disruption:
  technical_innovation: 论文未提出新算法或架构，核心贡献是识别出上下文内技能路由的'词汇竞争'失败模式——自动加载的工具技能与按需列出的流程技能之间词汇信号冲突会抑制正确选择，并将提示词内技能选择视为大规模嵌入检索式路由的小样本对应物，为
    agent 系统提示词工程提供了可复验的实证结论。
  business_model: 对生产级 agent harness（如 Tinycloud 及同类多模态智能体平台）的产品设计有直接指导意义：技能库的暴露策略直接影响路由准确性与执行效率，过度暴露反而降低性能，将影响
    agent 平台的上下文预算分配与技能库组织方式。但属于工程实践层面的优化建议，不构成商业模式重塑。
engineering_complexity: production_ready
---

# Computer Science > Artificial Intelligence

# Title:Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness

View PDF HTML (experimental)Abstract:A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.