---
title: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
source: https://arxiv.org/abs/2605.19192
author:
- '[[Guijia Zhang, Hao Zheng, Harry Yang]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'arXiv:2605.19192v1 Announce Type: new Abstract: Multimodal agents use
  screenshots, documents, and webpages to choose tool calls. When a false visual claim
  triggers a click, email, extraction, or transfer, hallucination becomes an authorization
  failure rather than an answer-quality error. We formalize this failure mode as hallucination-to-action
  conversion: an unsupported perceptual claim supplies the precondition that makes
  a privileged action appear permitted. We propose evidence-carrying multimodal agents
  (ECA), which treat free-form model text as inadmissible evidence. ECA decomposes
  each tool call into action-critical predicates, obtains typed certificates from
  constrained DOM/OCR/AX verifiers, and lets a deterministic gate grant only the privileges
  those certificates support. The architecture does not hide perception error; it
  converts opaque model belief into named verifier, schema, and implementation residuals.
  Verifier red-teaming over 1,900 attacks exposes this residual directly: four targeted
  hardening steps reduce gate bypass from 15% to 1.3%. With content-derived certificates,
  ECA obtains 0% unsafe-action rate on a 200-task end-to-end pipeline (Wilson 95%
  upper bound 2.67%) and a 120-task browser proof-of-concept (upper bound 4.3%). A
  direct HACR audit on 500 stratified task keys shows that unsupported action-critical
  claims reach unsafe execution for naive agents (100.0%) and prompt-only defense
  (49.6%), but not for ECA. Oracle-certificate replay on 7,488 GPT-5.4 benchmark traces
  serves as a gate-correctness sanity check, and neural judge baselines remain bypassable
  under the same threat model. The resulting principle is simple: model language may
  propose actions, but external evidence must authorize them.'
tags:
- clippings
extraction_status: success
id: ed0d77dab9cf497a
source_type: academic_paper
tldr: 该论文将多模态智能体的幻觉问题重新定义为授权失败，并提出证据携带型多模态智能体（ECA）架构。ECA通过受约束的验证器提供类型化证书，由确定性门控决定授权，在1,900次红队攻击中将门控绕过率从15%降至1.3%，并在200项任务上实现0%的不安全动作率。
objective_summary: 该arXiv论文于2026年5月提交，作者形式化定义了多模态智能体因视觉幻觉触发危险工具调用的"幻觉到行动转换"模式。他们提出证据携带型多模态智能体（ECA）架构，将模型自由文本视为不可采纳证据，通过DOM/OCR/AX验证器提供类型化证书，由确定性门控仅授予证书支持的权限。在1,900次验证器红队攻击中，经四轮定向加固将门控绕过率从15%降至1.3%；ECA在200项任务端到端流水线上实现0%不安全动作率（Wilson
  95%上限2.67%），在500项任务HACR审计中朴素智能体不安全执行率为100.0%，仅提示词防御为49.6%，ECA为0%。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - ECA
  - DOM/OCR/AX
  - HACR
  - GPT-5.4
  key_people: []
key_logic_flow:
- 论文将多模态智能体的幻觉问题重新定义为授权失败而非回答质量错误，并提出"幻觉到行动转换"的形式化框架：不支持的感知主张为特权动作提供了看似允许的前提条件。
- 作者提出证据携带型多模态智能体（ECA）架构，将模型自由文本视为不可采纳证据，通过受约束的DOM/OCR/AX验证器获取类型化证书，由确定性门控仅授予证书支持的权限。
- 在1,900次攻击的验证器红队测试中，经过四轮定向加固步骤，门控绕过率从15%降至1.3%，证明该残差可直接暴露并修复。
- ECA在200项任务的端到端流水线上实现了0%的不安全动作率（Wilson 95%置信区间上限2.67%），在120项任务的浏览器概念验证中同样实现0%（上限4.3%）。
- 在500个分层任务键上的直接HACR审计显示，朴素智能体的不安全执行率为100.0%，仅靠提示词防御为49.6%，而ECA为0%。
- 在7,488条GPT-5.4基准轨迹上的预言机证书重放验证了门控正确性，同时神经判别器基线在相同威胁模型下仍可被绕过。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: paper
  name: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
  canonical_name: 'Hallucination as Exploit: Evidence-Carrying Multimodal Agents'
  url: https://arxiv.org/abs/2605.19192
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该论文形式化定义了多模态智能体中幻觉成为授权失败而非回答质量错误的故障模式，并命名为'幻觉到行动转换'。
  - 论文在1,900次红队攻击上验证了ECA门控机制，经四轮定向加固将绕过率从15%降至1.3%。
  - ECA架构在200项任务端到端流水线上实现0%不安全动作率，Wilson 95%置信区间上限为2.67%。
  article_id: ed0d77dab9cf497a
- object_type: project
  name: Evidence-Carrying Multimodal Agents (ECA)
  canonical_name: Evidence-Carrying Multimodal Agents (ECA)
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ECA将每个工具调用分解为行动关键谓词，从受约束的DOM/OCR/AX验证器获取类型化证书，并由确定性门控仅授权证书支持的操作。
  - ECA的核心原则是：模型语言可以提议行动，但外部证据必须授权它们。
  - 在500项任务的HACR审计中，ECA实现了0%的不安全执行率，而朴素智能体为100.0%，仅提示词防御为49.6%。
  article_id: ed0d77dab9cf497a
impact_score:
  score: 6.8
  reason: 该论文在智能体安全领域提出了一个重要的范式转换——将多模态幻觉从'回答质量问题'重新定义为'授权失败问题'，并给出了可量化的工程解决方案（ECA架构+确定性门控）。论文的1900+红队测试、200任务端到端管道0%不安全操作率等实验数据扎实。短期看，它直接触及当前Agent产品化最大的安全痛点（Claude
    Code、Computer Use等均面临此问题），对工业界Agent安全架构设计有直接指导意义。但作为学术论文，尚未产品化，影响力限于架构思想层面，不构成行业范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 确定性门控机制替代模型置信度阈值的工程可行性，以及DOM/OCR/AX验证器在真实Web环境中的覆盖率与延迟开销
hype_assessment:
  level: low
  reason: 论文语言严谨，无'颠覆''革命性'等PR词汇。核心主张（幻觉→授权失败）有形式化定义（HACR），实验设计包含Wilson置信区间、消融对比（朴素智能体100%不安全率
    vs 纯提示防御49.6% vs ECA 0%）、预言机证书回放验证等统计严谨性措施。结论克制——明确给出了置信上界而非绝对零风险声称。
information_entropy: high
domain_disruption:
  technical_innovation: 将智能体工具调用的安全授权从'信任模型自由文本'转变为'外部证据携带'范式：每个工具调用被分解为动作关键谓词，通过受限的DOM/OCR/AX验证器获取类型化证书，由确定性门控裁决授权。这本质上是在不可靠的感知层与特权操作层之间插入了一个可审计、可加固的验证中间件，将不透明的模型信念转化为命名的验证器、模式和实现残差。
  business_model: 若该架构被工业界采纳，将催生'验证器即服务'生态——针对不同应用场景（邮件、支付、浏览器操作）的标准化证书颁发器可能成为Agent安全中间件赛道。同时，企业级Agent产品的合规审计将获得可追溯的授权链路，降低部署Agent的安全审查阻力。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 该架构将多模态智能体的幻觉问题从'回答质量缺陷'重新定义为'授权安全失败'，这一认知框架的转变具有长期价值。核心理念——'模型语言可提议行动，但外部证据必须授权'——简洁且可泛化，随着AI
    Agent获得更多自主权（邮件发送、支付、数据操作），授权层的必要性将呈指数增长。然而，当前仅为学术论文+概念验证（200任务管道），无商业实体、无产品、无生态
    adopt，从论文到基础设施的路径漫长且不确定。3-5年内该原则大概率被主流Agent框架吸收，但ECA作为特定架构品牌能否独立存续存疑。评分6.5：强学术基础+清晰基础设施潜力，但商业化成熟度为零，需持续验证。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Anthropic
- LangChain
- CrewAI
- Cloud agent platform providers (AWS, GCP, Azure)
competitive_casualty:
- Prompt-only safety/guardrail approaches
- Neural judge based safety systems
- Unverified autonomous agent deployment platforms
market_opportunities:
- AI Agent 安全中间件创业机会：基于 ECA 架构中「验证器 + 确定性门控」的模式，可开发面向企业级 AI Agent 平台的授权网关中间件，在模型自由文本输出与工具执行之间插入可审计的验证层，将幻觉从质量问题转化为可量化的安全边界，目标客户包括金融、医疗、法律等对操作合规性要求极高的行业。
- Agentic AI 安全审计与红队测试服务：论文中 HACR 审计方法论（分层任务键 + 不安全执行率量化）可直接产品化为 AI Agent 安全评估框架，为企业提供「幻觉到行动转化」专项渗透测试服务，帮助客户识别其
  Agent 在生产环境中的实际风险敞口，并给出基于证据门控的加固路线图。
- 多模态 Agent 开发者工具链升级：建议从事 Agent 框架开发的团队关注 ECA 架构并将其验证器模式（DOM/OCR/AX 类型化证书）内建到框架的权限系统中，提供开箱即用的「模型提议
  + 外部证据授权」原语，这将成为下一代 Agent 框架的安全差异化竞争力。
risk_matrix:
  regulatory: 欧盟 AI Act 对高风险 AI 系统的「人类监督」要求可能因 ECA 这类证据门控架构的出现而升级为「可验证的自动化监督」标准，合规成本上升；同时，论文暴露的
    100% 不安全执行率（朴素 Agent）可能成为监管机构收紧 Agent 自主权限的依据，推动「AI Agent 操作需持证执行」的立法方向。
  technological: ECA 架构依赖的 DOM/OCR/AX 验证器本身并非完美——论文承认验证器红队测试中门控绕过率仍有 1.3%，这意味着攻击者可能转向直接攻击验证器（如对抗性
    UI 设计、OCR 混淆）；此外，GPT-5.4 等更强模型可能使神经法官基线的防御能力提升，改变「纯提示防御 vs 证据门控」的相对收益计算。
  competitive: OpenAI（GPT-5.4 已在论文中被用于基准测试）、Anthropic（Computer Use）和 Google（Project
    Mariner）等巨头极有可能将类似验证机制内化到其 Agent 平台中，形成平台级安全默认项，对独立安全中间件创业公司构成生态挤压风险；论文开源架构可能被快速吸收并标准化，先发优势窗口有限。
  ethical: 论文通过红队测试证明了当前多模态 Agent 在无防护状态下 100% 会执行危险操作（点击、转账、邮件发送等），这一发现若被恶意利用，可能加速针对未加固
    Agent 的攻击工具开发；同时，「证据门控」若设计不当，验证器的偏见（如 OCR 对特定语言/字体的识别差异）可能导致对某些用户群体的系统性拒绝服务。
  additional:
  - 供应链传导风险：ECA 架构将安全责任从模型能力转移到验证器实现（DOM/OCR/AX），验证器本身的供应链安全（如使用的 OCR 库、浏览器引擎）成为新的攻击面，单点失败可能导致整个门控体系被绕过。
  - 过度依赖确定性门控的刚性风险：在模糊场景（如 CAPTCHA、非标准 UI 控件）下，严格的门控策略可能导致 Agent 完全无法操作，产生可用性与安全性的紧张关系，需要在架构设计中加入降级路径。
confidence:
  impact: high
  compound: high
  hype: medium
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: Evidence-Carrying Multimodal Agents (ECA)
  canonical_name: Evidence-Carrying Multimodal Agents (ECA)
  url: https://arxiv.org/abs/2605.19192
  positioning: 证据携带型多模态智能体架构，将模型视觉幻觉重新定义为授权失败问题，通过确定性门控和类型化证书机制实现安全工具调用。
  technical_signal: 提出ECA架构，将模型自由文本视为不可采纳证据，通过受约束的DOM/OCR/AX验证器获取类型化证书，由确定性门控仅授权证书支持的操作。
  adoption_signal: 在200项任务端到端流水线和120项任务浏览器概念验证中均实现0%不安全动作率，验证了该架构在不同任务域中的有效性。
  ecosystem_relevance: 针对多模态智能体因视觉幻觉触发危险工具调用的关键安全问题，为AI安全社区提供了可验证、可修复的新型防御范式。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ECA将多模态智能体幻觉从回答质量问题重新定义为授权失败，通过验证器红队测试证明残差可定向修复，为构建安全可靠的AI智能体提供了全新范式，值得持续跟踪其在真实部署中的表现。
  risk_notes:
  - 验证器红队测试在1,900次攻击后门控绕过率降至1.3%，但仍存在残差被利用的风险。
  - 架构依赖受约束验证器的覆盖范围，在验证器未定义的操作类别上可能存在安全盲区。
  - 目前仅在研究环境和基准轨迹上验证，真实世界对抗样本的复杂性和强度尚未充分检验。
  score: 8.0
  article_ids:
  - ed0d77dab9cf497a
  evidence_snippets:
  - ECA将每个工具调用分解为行动关键谓词，从受约束的DOM/OCR/AX验证器获取类型化证书，并由确定性门控仅授权证书支持的操作。
  - 在1,900次攻击的验证器红队测试中，经过四轮定向加固步骤，门控绕过率从15%降至1.3%，证明该残差可直接暴露并修复。
  - 在500项任务的HACR审计中，ECA实现了0%的不安全执行率，而朴素智能体为100.0%，仅提示词防御为49.6%。
---

# Computer Science > Artificial Intelligence

# Title:Hallucination as Exploit: Evidence-Carrying Multimodal Agents

View PDF HTML (experimental)Abstract:Multimodal agents use screenshots, documents, and webpages to choose tool calls. When a false visual claim triggers a click, email, extraction, or transfer, hallucination becomes an authorization failure rather than an answer-quality error. We formalize this failure mode as hallucination-to-action conversion: an unsupported perceptual claim supplies the precondition that makes a privileged action appear permitted. We propose evidence-carrying multimodal agents (ECA), which treat free-form model text as inadmissible evidence. ECA decomposes each tool call into action-critical predicates, obtains typed certificates from constrained DOM/OCR/AX verifiers, and lets a deterministic gate grant only the privileges those certificates support. The architecture does not hide perception error; it converts opaque model belief into named verifier, schema, and implementation residuals. Verifier red-teaming over 1,900 attacks exposes this residual directly: four targeted hardening steps reduce gate bypass from 15% to 1.3%. With content-derived certificates, ECA obtains 0% unsafe-action rate on a 200-task end-to-end pipeline (Wilson 95% upper bound 2.67%) and a 120-task browser proof-of-concept (upper bound 4.3%). A direct HACR audit on 500 stratified task keys shows that unsupported action-critical claims reach unsafe execution for naive agents (100.0%) and prompt-only defense (49.6%), but not for ECA. Oracle-certificate replay on 7,488 GPT-5.4 benchmark traces serves as a gate-correctness sanity check, and neural judge baselines remain bypassable under the same threat model. The resulting principle is simple: model language may propose actions, but external evidence must authorize them.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.