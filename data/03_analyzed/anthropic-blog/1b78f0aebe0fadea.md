---
title: Usage Policy Update
source: https://www.anthropic.com/news/usage-policy-update
author: []
published: '2026-08-26'
created: '2026-08-27'
manifest_dates:
- '2026-08-27'
- '2026-08-28'
- '2026-08-29'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 1b78f0aebe0fadea
source_type: tech_blog
tldr: Anthropic 更新了使用政策（Usage Policy），新增针对恶意网络与基础设施入侵的禁止条款，收窄对政治内容的全面限制范围，并修订执法用途的表述。新政策于
  2025 年 9 月 15 日生效。
objective_summary: Anthropic 基于用户反馈、产品变化、监管进展与执法优先事项更新了使用政策，为 Claude 的使用方式提供更清晰的框架，新政策于
  2025 年 9 月 15 日生效。更新新增了禁止恶意计算机、网络与基础设施入侵行为的章节，并发布了面向代理式（agentic）使用的补充指引。政策取消了历史上对游说与竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程、涉及选民和竞选定向的用途。政策还修订了执法用途相关表述，移除了此前针对后台工具和分析应用的各类例外条款。
event_type: policy_and_safety
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies:
  - Claude
  - Claude Code
  - Computer Use
  - Agentic AI
  key_people: []
key_logic_flow:
- Anthropic 基于用户反馈、产品变化、监管进展和执法优先事项更新了使用政策，所有变更将于 2025 年 9 月 15 日生效。
- 针对代理式 AI 能力带来的规模化滥用、恶意软件生成和网络攻击风险，政策新增了禁止恶意计算机、网络与基础设施入侵活动的章节。
- 公司发布了关于使用政策如何适用于代理式用途的补充指南，提供代理场景下禁止活动的具体示例，但不替代使用政策本身。
- 政策取消了历史上对游说和竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程、以及涉及选民和竞选定向的用途，以支持合法的政策研究与政治写作。
- 政策修订了执法用途相关表述，移除了此前针对后台办公工具和分析应用的各类例外，使允许的用途更易于理解。
object_mentions:
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://www.anthropic.com/claude
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 表示此次使用政策更新为 Claude 的使用方式提供清晰框架，相关变更将于 2025 年 9 月 15 日生效。
  - 政策取消了历史上对游说与竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程的用途，从而支持合法的政策研究与政治写作。
  article_id: 1b78f0aebe0fadea
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: https://www.anthropic.com/claude-code
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 指出其已发布包括 Claude Code 和 Computer Use 在内的代理式工具，这些工具也带来规模化滥用与网络攻击的新风险。
  article_id: 1b78f0aebe0fadea
- object_type: product
  name: Computer Use
  canonical_name: Computer Use
  url: https://www.anthropic.com/news/computer-use
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Anthropic 在文章中提及已发布 Computer Use 等代理式工具，并据此更新使用政策以约束相关的恶意用途。
  article_id: 1b78f0aebe0fadea
- object_type: paper
  name: 'Detecting and Countering Malicious Uses of Claude: March 2025'
  canonical_name: 'Detecting and Countering Malicious Uses of Claude: March 2025'
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - '文章引用其首份威胁情报报告《Detecting and Countering Malicious Uses of Claude: March 2025》，指出代理能力带来规模化滥用、恶意软件生成与网络攻击等风险。'
  article_id: 1b78f0aebe0fadea
extract_result: success
impact_score:
  score: 4.0
  reason: 这是前沿实验室的使用政策调整，不改变模型技术能力或竞争格局，冲击力中等偏低。但两点值得关注：其一，取消对游说与竞选内容的全面禁令，为政策研究、公民教育等此前被拒的应用场景打开合法空间，对相关垂直开发者有实质影响；其二，针对
    agentic 使用新增网络安全禁止条款并发布配套指引，为快速扩张的代理式 AI 生态（Claude Code、Computer Use）划定了合规边界，释放出行业安全规范化的信号。综合判断为重要但非范式转移级别的政策事件，故给
    4 分。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: 代理式应用（Claude Code/Computer Use）的合规边界是否清晰可执行，以及政治内容类应用是否真正获得放开而非仅停留在措辞层面
hype_assessment:
  level: low
  reason: 公告语言克制务实，未使用'颠覆'、'革命性'等 PR 滥用词汇；内容具体可执行——明确了生效日期（2025年9月15日），逐条列出三项政策变更（新增网络安全禁令、政治内容松绑、执法用途措辞修订），并引用配套帮助中心文章与威胁情报报告作为依据。整体是透明的合规沟通而非概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 无直接技术突破。政策更新本质上是 agentic AI 技术能力快速演进的反射——Claude Code、Computer
    Use 等代理式工具带来的规模化滥用、恶意软件生成与网络攻击风险，促使 Anthropic 将安全边界形式化写入政策条款，属于对既有技术趋势的合规响应而非新技术供给。
  business_model: 放宽政治内容全面禁令，为政策研究、公民教育、政治写作等此前被拒之门外的商业场景打开了合法空间，可能催生新的垂直 SaaS 需求；同时发布
    agentic 使用指引，为企业客户提供合规确定性，降低 Claude Code 等代理式产品的采购与部署顾虑。合规透明度正成为平台型 AI 公司的差异化竞争要素。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 本次政策更新本身是渐进式修订，但站在资本视角有三层长期价值：其一，Anthropic 率先针对代理式 AI 的规模化滥用、恶意软件与网络攻击风险建立明确合规框架。随着
    Agent 进入企业生产环境，安全治理正从成本项转化为政企采购决策的关键权重，Anthropic 借此积累的信任资产会随 Agent 渗透率提升而复利累积，成为其在
    Claude Code/Computer Use 生态扩张中的差异化壁垒。其二，收窄政治内容全面禁令，实质扩大了 Claude 在政策研究、公民教育、政治写作等合规场景的可服务市场（TAM），为下游开发者打开增量空间，属于'监管松绑→需求释放'的边际利好。其三，配套发布的
    agentic 使用补充指引有望成为行业参照标准，强化 Anthropic 在 AI 治理话语权上的先发地位。制约因素：单一政策变更不构成独立技术护城河，且执行口径仍需市场验证，因此未达
    8 分以上；但作为 Anthropic 信任资产与治理标准积累的关键一环，具备中等偏强的长期复利效应。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- Claude Code
- Cursor
- 政策研究与公民教育机构
competitive_casualty:
- AI 选举/选民定向操纵服务商
- 未授权网络攻击工具开发商
- Agent 治理框架落后的 AI 平台
market_opportunities:
- 面向企业级代理式 AI 的合规与安全审计工具：Anthropic 新增对恶意网络入侵、恶意软件生成的禁止条款，意味着企业在部署 Claude Code、Computer
  Use 等代理时，需要配套的权限管控、行为审计与合规检测方案，创业者可围绕“代理式 AI 治理”打造差异化产品
- 合规漏洞挖掘与红队服务：政策明确支持经系统所有者同意的漏洞发现，可基于 Claude 构建自动化渗透测试、漏洞扫描与红队评估产品，服务企业网络安全与合规需求
- 政策研究与公民教育类 AI 应用：政策取消对游说与竞选内容的全面禁止，仅禁止欺骗性或破坏民主进程的用途，为面向政策分析、公民教育、政治写作的合法 AI 工具打开市场空间，可开发带来源核验与合规过滤的垂直应用
risk_matrix:
  regulatory: 新政策与欧盟 AI Act、网络犯罪相关立法方向呼应，但政治内容限制的收窄可能引发监管与公众关注；不同司法辖区（如欧盟、美国各州）对选举操纵与深度伪造的监管尺度差异，可能使
    Anthropic 的“仅禁止欺骗性用途”边界在部分地区面临合规张力。此外，执法用途表述的修订可能招致隐私与公民自由团体的审查
  technological: 政策本质是对代理式 AI 能力扩张的风险回应，但仅靠使用政策难以根治技术滥用——Claude Code、Computer Use
    等代理工具的规模化滥用与恶意软件生成风险仍存在对抗压力；同时，开源模型与自托管部署不受 Anthropic 政策约束，可能形成监管套利与技术外溢
  competitive: Anthropic 在网络安全与代理式用途上的限制若比 OpenAI、Google 等竞争者更严格，可能推动部分开发者转向政策更宽松的替代模型；反之，若
    Anthropic 借此强化安全品牌，也可能挤压中小安全厂商的生存空间
  ethical: 政治内容限制的收窄虽支持合法研究与公民教育，但若无强效的内容检测与溯源机制，可能被用于大规模选民定向、欺骗性政治宣传和深度伪造传播，对民主进程构成威胁；代理式
    AI 的滥用（网络入侵、恶意软件）若未有效阻断，会放大整体网络空间安全风险
  additional:
  - 政策执行的一致性与可解释性风险：如何在实际执法中区分“经同意的漏洞发现”与“未经授权的入侵”、以及执法用途例外条款的具体边界，可能引发开发者社区的分歧与不确定性
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Claude
  canonical_name: Claude
  url: https://www.anthropic.com/claude
  positioning: Anthropic 的旗舰大语言模型与 AI 助手，以使用政策明确合规边界，覆盖编码、研究、内容创作与日常对话等场景，强调安全与负责任使用。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 开发者与企业客户
  - 政策研究与政治写作者
  - 一般 AI 助手用户
  product_signal: 使用政策为 Claude 的使用方式提供清晰框架，新增禁止恶意网络入侵条款，并取消对政治内容的全面禁止以支持合法研究与写作。
  market_signal: Anthropic 依据用户反馈与监管进展更新政策，显示其在合规治理上的主动姿态，新政策将于 2025 年 9 月 15 日生效。
  differentiation: 相比全面禁止政治内容的旧政策，Claude 转向仅禁止欺骗性或破坏民主进程的用途，在支持合法政治话语与防范滥用之间取得平衡。
  watch_reason: Anthropic 对使用政策的调整直接定义 Claude 的可用边界，尤其是针对代理式能力新增的网络安全禁止条款与政治内容限制的放宽，反映主流
    AI 厂商在安全合规与开放可用性之间的权衡走向，值得持续跟踪其执行效果与对用户的影响。
  risk_notes:
  - 新增的恶意网络入侵禁止条款依赖执行落地，违规检测与处置效果仍待验证。
  - 放宽政治内容限制可能引发关于选举操纵与深度伪造的担忧，监管压力或上升。
  - 政策变更主要涉及使用指引，未涉及模型能力层面的具体安全措施。
  score: 7.0
  article_ids:
  - 1b78f0aebe0fadea
  evidence_snippets:
  - Anthropic 表示此次使用政策更新为 Claude 的使用方式提供清晰框架，相关变更将于 2025 年 9 月 15 日生效。
  - 政策取消了历史上对游说与竞选内容的全面禁止，改为仅禁止欺骗性或破坏民主进程的用途，从而支持合法的政策研究与政治写作。
- object_type: product
  name: Claude Code
  canonical_name: Claude Code
  url: https://www.anthropic.com/claude-code
  positioning: Anthropic 推出的代理式编码工具，能够自主完成软件工程任务，是 Claude 在开发者生态中的核心产品形态，受新使用政策中网络安全条款的直接约束。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 软件开发与工程团队
  - 智能体编码与自动化工作流用户
  product_signal: 作为代理式工具代表，Claude Code 带来规模化滥用与网络攻击的新风险，促使 Anthropic 新增禁止恶意计算机与网络入侵的使用政策章节。
  market_signal: Anthropic 将 Claude Code 与 Computer Use 并列作为代理式能力的代表，显示其在智能体编码工具赛道上的重点投入。
  differentiation: 作为 Anthropic 官方代理式编码工具，其使用边界由厂商政策直接定义，与第三方编码智能体相比在安全治理上更受厂商管控。
  watch_reason: Claude Code 是 Anthropic 代理式能力的旗舰产品，新使用政策专门针对代理式滥用新增禁止条款，直接约束其应用边界；其安全治理与合规执行如何平衡开发者生产力与网络风险，值得持续观察。
  risk_notes:
  - 代理式工具带来的恶意软件生成与网络攻击风险，使其面临更高的安全审查与监管关注。
  - 使用政策的禁止条款可能限制部分合法但敏感的自动化安全测试等场景。
  score: 6.0
  article_ids:
  - 1b78f0aebe0fadea
  evidence_snippets:
  - Anthropic 指出其已发布包括 Claude Code 和 Computer Use 在内的代理式工具，这些工具也带来规模化滥用与网络攻击的新风险。
- object_type: product
  name: Computer Use
  canonical_name: Computer Use
  url: https://www.anthropic.com/news/computer-use
  positioning: Anthropic 推出的代理式功能，让 Claude 能够像人一样操作计算机界面完成多步任务，是其在代理式 AI 应用上的关键能力之一。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 桌面自动化与多步任务执行用户
  - 企业流程自动化团队
  product_signal: Computer Use 被列为 Anthropic 已发布的代理式工具之一，其规模化滥用风险促成了使用政策中新增的网络安全禁止条款。
  market_signal: Anthropic 将 Computer Use 与 Claude Code 并列提及，显示代理式交互能力已成为其产品战略的重要方向。
  differentiation: 相比传统 RPA 与脚本自动化，Computer Use 以视觉与自然语言驱动计算机操作，但其能力边界受使用政策严格约束。
  watch_reason: Computer Use 代表代理式 AI 与真实计算机环境交互的方向，其潜在滥用风险直接推动 Anthropic 政策更新；该功能的实际能力边界、安全约束与落地场景值得持续跟踪。
  risk_notes:
  - 计算机操作类代理能力被滥用时可能构成恶意网络入侵，安全治理难度较高。
  - 目前证据主要来自政策表述，Computer Use 的实际产品进展与市场反馈有限。
  score: 5.0
  article_ids:
  - 1b78f0aebe0fadea
  evidence_snippets:
  - Anthropic 在文章中提及已发布 Computer Use 等代理式工具，并据此更新使用政策以约束相关的恶意用途。
---

# Usage policy update

Today, we’re sharing some updates to our Usage Policy that reflect the growing capabilities and evolving usage of our products. Our Usage Policy serves as a framework for how Claude should and shouldn’t be used, providing clear guidance for everyone who uses Anthropic’s products.

In this update, our goal is to provide greater clarity and detail on our Policy based on user feedback, product changes, regulatory developments, and our enforcement priorities. These changes will take effect on September 15, 2025.

Below is a summary of some of the changes, and you can view the new Usage Policy here.

**Addressing cybersecurity and agentic use**

Over the past year, we’ve seen rapid advances in agentic capabilities. We've released our own agentic tools like Claude Code and Computer Use, and our models power many of the world's leading coding agents.

These powerful capabilities introduce new risks, including potential for scaled abuse, malware creation, and cyber attacks, as shared in our first threat intelligence report, *Detecting and Countering Malicious Uses of Claude: March 2025*.

To address these risks, we've added a section to our Usage Policy outlining the malicious computer, network, and infrastructure compromise activities that are prohibited by Anthropic. We continue to support use cases that strengthen cybersecurity, such as discovering vulnerabilities with the system owner's consent.

We’ve also published a new article to our Help Center on how our Usage Policy applies to agentic use more broadly. This supplementary guidance provides concrete examples of prohibited activities in agentic contexts, and is not meant to replace or supersede our Usage Policy.

**Revisiting broad restrictions on political content**

Our Usage Policy has historically contained broad prohibitions on all types of lobbying or campaign content. We believed this stance was appropriate given the unknown risks of AI-generated content on influencing democratic processes, and these are still prominent risks we take seriously.

We’ve heard from users that this blanket approach also limited legitimate use of Claude for policy research, civic education, and political writing. We're now tailoring our restrictions to specifically prohibit use cases that are deceptive or disruptive to democratic processes, or involve voter and campaign targeting. This approach enables legitimate political discourse and research while prohibiting activity that is misleading or invasive.

**Updating our language on law enforcement use**

Our previous Usage Policy language on law enforcement included various exceptions for back-office tools and analytical applications, which occasionally made it difficult to understand which use cases were permitted.