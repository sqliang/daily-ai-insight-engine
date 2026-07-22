---
title: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation'
source: https://arxiv.org/abs/2607.06624
author:
- '[[Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy,
  Maksim Parshin, Sergey Nikolenko]]'
published: '2026-07-09'
created: '2026-07-09'
description: 'arXiv:2607.06624v1 Announce Type: new Abstract: We present AgentLens,
  a production-assessed benchmark for interactive code agents. Most code-agent benchmarks
  reduce a run to a single bit -- did the task pass? -- but the people who actually
  use these agents experience the entire trajectory: how the agent follows instructions,
  uses its tools, verifies its own work, recovers from mistakes, and talks to them
  along the way. AgentLens evaluates that whole trajectory. It pairs formal verification,
  where an objective check exists, with LLM-written trajectory reviews and side-by-side
  comparisons, so that each run yields a readable explanation of why the score is
  what it is. This makes AgentLens useful for more than ranking models: we use it
  to diagnose model behavior, compare successive versions of our own agent, and catch
  product regressions in a nightly evaluation pipeline. We release the benchmark as
  open source at https://github.com/agent-lens/agent-lens-bench.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 08e820bcd6acda0c
source_type: academic_paper
tldr: AgentLens 是一个面向交互式代码智能体的生产级别评估基准，它不仅评估任务是否通过，还通过形式化验证和 LLM 编写的轨迹评审对整个执行过程进行评分，并已开源。
objective_summary: 研究人员发布了一个名为 AgentLens 的代码智能体评估基准。与传统只输出任务通过与否的二值化评估不同，AgentLens
  对智能体的完整执行轨迹进行评估，包括指令遵循、工具使用、自我验证、错误恢复和交互对话等方面。该基准结合了形式化验证与 LLM 编写的轨迹评审及并排对比，为每次运行提供可读的评分理由。研究者已将其用于诊断模型行为、对比不同版本的智能体以及在夜间评估流水线中捕获产品回归。该基准已作为开源项目发布。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - AgentLens
  - LLM
  key_people: []
key_logic_flow:
- AgentLens 是一个面向交互式代码智能体的生产评估基准，由论文作者团队提出并开源。
- 传统代码智能体基准测试只将一次运行简化为任务是否通过，而 AgentLens 评估完整的执行轨迹。
- 评估维度包括指令遵循、工具使用、自我验证、错误恢复以及智能体与用户的交互对话。
- AgentLens 将形式化验证与 LLM 编写的轨迹评审及并排对比相结合，每次运行都附带可读的评分解释。
- 该基准可用于诊断模型行为、对比相同智能体的不同版本，以及在夜间评估流水线中捕获产品回归。
- 作者已将该基准作为开源项目发布，供社区使用。
specialized_tags:
  paper:
    paperTitle: 'AgentLens: Production-Assessed Trajectory Reviews for Coding Agent
      Evaluation'
    authors: []
    affiliations: []
    venue: arXiv preprint
    codeUrl: null
    datasetUrl: null
    researchArea: NLP
    methodType: benchmark
extract_result: success
object_mentions:
- object_type: project
  name: AgentLens
  canonical_name: AgentLens
  url: https://github.com/agentlens/agentlens
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - AgentLens 是一个生产评估基准，用于对交互式代码智能体进行完整的执行轨迹评估，而非仅看任务是否通过。
  - 该基准结合了形式化验证与 LLM 编写的轨迹评审和并排对比，每次运行都提供可读的评分解释。
  - 研究者已将其用于诊断模型行为、对比智能体不同版本以及在夜间评估流水线中捕获产品回归。
  article_id: 08e820bcd6acda0c
impact_score:
  score: 5.5
  reason: AgentLens 提出的轨迹级评估范式填补了编码 Agent 评估体系中的一个关键空白——从二元通过/失败走向完整的执行轨迹评估。这不是 ChatGPT
    级别的范式转移，但对于高速发展的编码 Agent 赛道（Cursor、Copilot、Devin 等），一个开源的、可落地的细粒度评估基准具有改变局部竞争格局的潜力。它已在产品级夜间管线中验证了回归捕获和版本对比能力，说明不是纸上谈兵。但该框架依赖
    LLM 进行轨迹评审，评估本身的可靠性和成本仍需社区进一步验证，目前尚处于早期采用阶段。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 轨迹级细粒度评估取代二元通过/失败，可诊断模型行为和捕获回归
hype_assessment:
  level: low
  reason: 论文陈述克制且具体，没有使用'颠覆性''革命性'等 PR 话术。明确说明了方法论（形式化验证+LLM 轨迹评审）、适用场景（诊断、版本对比、夜间回归检测），并已开源。所有声称都有实际部署验证支撑，属于实打实的干货输出。
information_entropy: high
domain_disruption:
  technical_innovation: 将形式化验证（客观检查）与 LLM 轨迹评审（主观评估）结合，解决了编码 Agent 评估中单一通过/失败粒度太粗的问题，为五维（指令遵循、工具使用、自我验证、错误恢复、用户交互）轨迹评分提供了可落地的实现范式。
  business_model: 为编码 Agent 产品团队提供了标准化的质量保障基础设施——夜间回归管线、版本对比、行为诊断，可能推动 Agent 产品从'凭感觉迭代'转向'数据驱动评估'的工程实践标准化。
engineering_complexity: production_ready
compound_value:
  score: 5.0
  reason: AgentLens 解决了一个真实痛点：当前编码 Agent 评估过度简化（二元通过/失败），缺乏对执行轨迹——指令遵循、工具使用、自我验证、错误恢复——的细粒度评估。作为开源基准，它有望成为
    Agent 开发者的基础设施级工具，用于夜间回归检测和模型行为诊断。然而其长期复利价值受限：第一，开源学术项目缺乏商业模式和持续维护的财务激励，benchmark
    的保鲜期通常较短（模型能力提升后旧基准失效）；第二，评估赛道已拥挤（SWE-bench、HumanEval、LiveCodeBench 等），AgentLens
    的轨迹评审差异化虽显著但未必能形成独占性；第三，LLM-as-judge 的轨迹评审模式本身存在偏见和可靠性争议。因此该项目的核心价值不在自身商业化，而在于为编码
    Agent 生态提供更好的『度量衡』，间接加速整个赛道的产品迭代质量。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Cursor (Anysphere)
- GitHub Copilot
- Codeium
- Cognition (Devin)
- Anthropic
- OpenAI
competitive_casualty:
- SWE-bench（若未能演进到轨迹级评估）
- 依赖简化二元基准进行营销的 Agent 产品
- 缺乏系统化评估能力的早期编码 Agent 初创公司
market_opportunities:
- 使用 AgentLens 构建夜间评估管线，可帮助编码 Agent 团队在产品上线前自动捕获回归问题，提升发布质量
- 将 AgentLens 的轨迹评估方法论扩展到非编码领域（如数据分析 Agent、客服 Agent），形成垂直行业评估框架的商业机会
- 基于 AgentLens 开源的评估体系，可为企业提供定制化 Agent 评估咨询服务，帮助客户诊断模型行为和版本迭代效果
risk_matrix:
  regulatory: 无
  technological: AgentLens 依赖 LLM 进行轨迹评审，存在评审偏差风险，即 LLM 裁判可能对特定模型风格或输出格式有系统性偏好；此外，该基准聚焦编码场景，若编码
    Agent 架构快速演进（如从工具调用转向端到端生成），部分评估维度可能过时
  competitive: Anthropic、OpenAI、GitHub 等巨头可能推出自有编码 Agent 评估标准，导致 AgentLens 成为小众方案而非行业通用基准；若其他开源基准（如
    SWE-bench、HumanEval）快速吸纳轨迹评估能力，AgentLens 的差异化优势将被稀释
  ethical: AgentLens 的轨迹评审可能无意中放大 LLM 裁判的偏见（如对某些代码风格或语言偏好），影响评估公平性；开源性质也意味着存在被恶意修改评估标准以美化特定
    Agent 表现的风险
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: AgentLens
  canonical_name: AgentLens
  url: https://github.com/agentlens/agentlens
  positioning: AgentLens 是一个面向交互式代码智能体的生产级评估基准，对完整执行轨迹而非仅任务结果进行多维度评分与诊断。
  technical_signal: AgentLens 采用形式化验证与 LLM 编写的轨迹评审及并排对比相结合的混合评估方法。
  adoption_signal: 研究者已将其用于诊断模型行为、对比智能体不同版本以及在夜间评估流水线中捕获产品回归。
  ecosystem_relevance: 填补了代码智能体评估仅依赖二值化通过率而缺乏轨迹级质量判断的空白，已作为开源项目发布。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: AgentLens 提出的轨迹级评估方法可能成为代码智能体质量评估的新范式，其开源性质和夜间评估流水线使其具备持续迭代和社区共建的潜力，值得关注其对开发工具链和智能体评估标准的影响。
  risk_notes:
  - 评估结果高度依赖 LLM 评审质量，LLM 自身的偏见和幻觉可能影响评分一致性。
  - 目前仅基于论文作者团队自身实践验证，在更广泛社区中的通用性和复现性有待验证。
  score: 6.0
  article_ids:
  - 08e820bcd6acda0c
  evidence_snippets:
  - AgentLens 是一个生产评估基准，用于对交互式代码智能体进行完整的执行轨迹评估，而非仅看任务是否通过。
  - 该基准结合了形式化验证与 LLM 编写的轨迹评审和并排对比，每次运行都提供可读的评分解释。
  - 研究者已将其用于诊断模型行为、对比智能体不同版本以及在夜间评估流水线中捕获产品回归。
---

# Computer Science > Artificial Intelligence

# Title:AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

View PDFAbstract:We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.