---
title: PR spam today looks like email spam in the early 2000s
source: https://www.greptile.com/blog/prs-on-openclaw
author:
- '[[dakshgupta]]'
published: '2026-06-24'
created: '2026-06-25'
description: 'Article URL: https://www.greptile.com/blog/prs-on-openclaw Comments
  URL: https://news.ycombinator.com/item?id=48660579 Points: 220 # Comments: 129'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 61cebb5cfcee9b53
source_type: community_discussion
tldr: Greptile 基于为 OpenClaw 审查 PR 的数据发现，AI 编码代理正导致开源 PR 垃圾信息泛滥：OpenClaw 的 PR 从每周 2
  个飙升至 3400 个，合并率从 48% 跌至 9.3%。文章认为需要发件人声誉系统和信任基础设施来应对这一趋势。
objective_summary: Greptile 员工 Rahul 基于该公司为 OpenClaw 审查 PR 的实际数据，分析了 AI 编码代理对开源贡献的影响。OpenClaw
  的 PR 提交量从每周 2 个暴增至 3400 个，合并率从 48% 降至 9.3%，大量低质量 PR 由 AI 代理自动生成。文章将 PR 垃圾信息类比为 2000
  年代初的电子邮件垃圾信息，指出需要声誉系统和信任管理工具来应对。Mitchell Hashimoto 因 Ghostty 项目遭遇 AI 生成的 PR 泛滥，已发布
  Vouch 信任管理系统。在 OpenClaw 中，重构类 PR 的合并率（35%）远高于功能类 PR（9%），表明需深入理解代码库的贡献更受青睐。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Greptile
  - OpenClaw
  technologies:
  - AI coding agents
  key_people:
  - Rahul
  - Mitchell Hashimoto
  - Linus Torvalds
key_logic_flow:
- OpenClaw 的 PR 提交量从每周约 2 个暴增至 3400 个，合并率从约 48% 降至不到 9.3%，大量低质量 PR 由 AI 编码代理自动生成。
- PR 垃圾信息与 2000 年代初的电子邮件垃圾信息模式相似，需要通过发件人声誉系统和信任基础设施来应对。
- Mitchell Hashimoto 因 Ghostty 项目遭遇 AI 生成 PR 泛滥，发布了 Vouch 信任管理系统来管理开源贡献者的可信度。
- 当大多数贡献者使用相同的 AI 编码代理时，观点多样性丧失，Linus 定律（足够多的眼球使所有漏洞变浅显）可能不再成立。
- 在 OpenClaw 中，需要深入理解代码库的重构类 PR 合并率（35%）远高于功能类 PR（9%），表明深度思考比大量编写更重要。
- 开源社区需要更好的身份认证、声誉系统和贡献验证基础设施来应对 AI 带来的新挑战。
extract_result: success
object_mentions:
- object_type: project
  name: openclaw/openclaw
  canonical_name: openclaw/openclaw
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenClaw 成为 GitHub 历史上增长最快的仓库，PR 提交量从每周约 2 个暴增至 3400 个，合并率从 48% 降至不到 9.3%。
  - 大量 PR 是由 AI 编码代理生成的低质量贡献，有贡献者在一天内提交了 106 个 PR，中位提交间隔仅 3 秒。
  - 在 OpenClaw 中，重构类 PR 的合并率为 35%，远高于功能类 PR 的 9%，表明需深入理解代码库的贡献更受青睐。
  article_id: 61cebb5cfcee9b53
- object_type: project
  name: Vouch
  canonical_name: Vouch
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Mitchell Hashimoto 发布了 Vouch，一个为开源贡献者设计的信任管理系统，未经过担保的用户无法贡献。
  - Vouch 的愿景是让信任决策最终在不同项目之间传播，类似开源版的发件人声誉评分系统。
  article_id: 61cebb5cfcee9b53
- object_type: project
  name: Ghostty
  canonical_name: Ghostty
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Mitchell Hashimoto 创建并维护了 Ghostty，这是最受欢迎的开源终端模拟器之一。
  - 由于 AI 生成的 PR 垃圾流量过大，Mitchell 需要限制 AI 生成的贡献，随后发布了 Vouch 来解决这个问题。
  article_id: 61cebb5cfcee9b53
- object_type: company
  name: Greptile
  canonical_name: Greptile
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Greptile 是一家构建 AI 代理来审查拉取请求的公司，为 OpenClaw 提供 PR 审查服务。
  - 该文章基于 Greptile 在审查 OpenClaw PR 过程中直接观察到的数据和经验撰写。
  article_id: 61cebb5cfcee9b53
impact_score:
  score: 6.5
  reason: AI编程代理导致的开源PR垃圾信息泛滥是一个正在加速蔓延的趋势。OpenClaw仓库PR量从每周2个飙升至3400个，合并率从48%骤降至9.3%，这些硬数据表明AI代理正在系统性冲击开源协作模式。Mitchell
    Hashimoto因垃圾PR被迫限制Ghostty贡献并发布Vouch信任系统，验证了问题的严重性。短期影响集中在开源维护者负担加剧和贡献质量管控上，虽未达到范式转移级别，但将催生开源身份验证、发件人信誉等基础设施需求，改变开源贡献的游戏规则。评分：6.5
sentiment: neutral
developer_sentiment:
  tone: frustrated
  primary_focus: AI代理生成的低质量PR垃圾信息正在严重浪费维护者时间、降低仓库质量，需要建立发件人信誉和身份验证机制
hype_assessment:
  level: low
  reason: 文章基于Greptile实际观察到的PR审查数据，提供了具体的量化指标（合并率48%→9.3%、单日106个PR、中位间隔3秒、多位贡献者提交相同功能PR等），没有使用'颠覆性''革命性'等空洞PR词汇，而是通过数据驱动的方式描述问题并提出基于发件人信誉的解决方案思路，属于实打实的现象分析。
information_entropy: high
domain_disruption:
  technical_innovation: 文章揭示了AI编程代理导致的开源贡献同质化问题——多位贡献者使用相同AI工具独立提交了内容完全相同的PR（如4人提交相同标题的SearXNG搜索功能PR、6人修复同一Brave
    Search语言环境bug），表明AI工具正在收敛而非多元化开源贡献的思维多样性。重构类PR合并率（35%）远高于功能类PR（9%）的发现，量化了深度代码理解比纯代码生成更有价值的技术洞见。
  business_model: Mitchell Hashimoto发布的Vouch信任管理系统代表了开源贡献验证从隐性社交信用向显式基础设施的演化方向。若Vouch的信任评分能在跨项目传播，将催生开源领域的'发件人信誉'市场，可能形成基于贡献者身份验证和信誉评分的平台化服务商业模式，影响GitHub等代码托管平台的贡献管理策略。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: AI编程代理的爆发式增长必然导致开源仓库PR垃圾信息持续泛滥，这是一个结构性且不可逆的趋势——更多AI代理意味着更多低成本、同质化的自动PR提交。类比2000年代电子邮件垃圾催生了SPF/DKIM/DMARC等整个反垃圾邮件产业（如今已是数十亿美元规模的基础设施），开源贡献的信誉/身份/验证基础设施也将成为长期刚需。Vouch等信任管理系统有潜力形成'开源贡献者身份层'的协议级标准，具备网络效应：越多项目采用→越多人建立信誉→越难被替代。Greptile作为PR审查工具的数据积累也构成数据壁垒。但核心风险在于：GitHub可能将信誉过滤内建为核心平台功能，压缩第三方独立项目的生存空间，且去中心化信任方案的跨项目协调成本极高。该赛道尚处于Day
    0阶段，价值捕获路径需持续验证。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Greptile
- Vouch
- GitHub
competitive_casualty:
- 低质量AI编程代理工具
- 无信誉体系的匿名开源贡献者
- 治理薄弱的大型开源项目
market_opportunities:
- 创业者可围绕开源贡献者信誉系统构建产品，类似 Vouch 的跨项目信任网络存在巨大空白，可作为 GitHub/GitLab 的生态插件商业化
- PR 审查工具（如 Greptile）可集成发件人信誉评分与 AI 生成内容检测功能，为大型开源项目提供垃圾 PR 过滤的 SaaS 服务
- AI 编程代理差异化方向明确：能深度理解代码库并进行重构的代理（合并率 35%）比简单生成功能的代理（合并率 9%）价值高 4 倍，产品应强调深度代码理解而非代码生成量
risk_matrix:
  regulatory: 开源项目引入贡献者信誉过滤机制可能面临歧视性准入争议，若 Vouch 类系统成为事实标准，可能引发平台责任和反垄断审查
  technological: 主流 AI 编程代理的思维同质化导致开源贡献多样性下降，Linus 定律失效风险上升；若代理趋向于生成相似解决方案，开源的去中心化优势将被削弱
  competitive: GitHub/GitLab 可能内置 AI 垃圾 PR 检测能力，挤压独立第三方工具的生存空间；Vouch 若被广泛采用可能形成新的信任垄断格局
  ethical: AI 生成的垃圾 PR 挤占维护者精力，降低开源社区健康度；信誉系统可能将新贡献者拒之门外，加剧开源贡献的精英化与门槛；AI 代理的思维同质化削弱了开源最核心的多元视角优势
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: openclaw/openclaw
  canonical_name: openclaw/openclaw
  url: null
  positioning: 因AI编码代理贡献泛滥而成为开源PR垃圾信息典型案例的GitHub快速增长仓库，是观察AI代理时代开源生态演变的核心样本。
  technical_signal: PR提交量从每周约2个飙升至3400个，合并率从48%跌至9.3%，贡献者在一天内提交106个PR，中位提交间隔仅3秒。
  adoption_signal: 成为GitHub历史上增长最快的仓库，大量AI代理贡献者涌入，但PR合并率从48%急剧下降至9.3%。
  ecosystem_relevance: 作为AI编码代理冲击开源生态的典型样本，揭示了建立声誉系统和信任基础设施的迫切需求，推动了Vouch等解决方案的诞生。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: OpenClaw展示了AI编码代理时代开源贡献的核心矛盾——数量暴增但质量急剧下降，正在催生新的信任基础设施需求，对理解开源生态演变具有风向标意义。
  risk_notes:
  - 大量低质量AI生成PR可能淹没有深度、有思考的贡献，降低开源项目的整体质量。
  - 贡献者观点因集中使用Claude/Codex等相同AI工具而趋同，Linus定律的有效性面临挑战。
  - PR合并率从48%降至9.3%，项目维护者的审查负担急剧加重。
  score: 8.0
  article_ids:
  - 61cebb5cfcee9b53
  evidence_snippets:
  - OpenClaw 成为 GitHub 历史上增长最快的仓库，PR 提交量从每周约 2 个暴增至 3400 个，合并率从 48% 降至不到 9.3%。
  - 大量 PR 是由 AI 编码代理生成的低质量贡献，有贡献者在一天内提交了 106 个 PR，中位提交间隔仅 3 秒。
  - 在 OpenClaw 中，重构类 PR 的合并率为 35%，远高于功能类 PR 的 9%，表明需深入理解代码库的贡献更受青睐。
- object_type: project
  name: Vouch
  canonical_name: Vouch
  url: null
  positioning: 面向开源贡献者的信任管理系统，通过担保人机制过滤AI生成的垃圾PR贡献，规划跨项目信任评分传播。
  technical_signal: 采用担保人机制过滤未经验证的贡献者，规划跨项目信任评分传播体系，类似开源版发件人声誉系统。
  adoption_signal: 由Mitchell Hashimoto为Ghostty项目创建并投入使用，目前为项目级信任管理，尚未实现跨项目传播。
  ecosystem_relevance: 作为应对AI编码代理贡献泛滥的首个系统化信任管理方案，Vouch代表了开源社区在贡献验证基础设施建设上的关键探索方向。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Vouch是应对AI编码代理时代开源贡献信任危机的首个系统方案，其跨项目信任传播愿景若能实现有望成为开源基础设施关键组件，代表了开源社区在信任管理领域的前沿探索。
  risk_notes:
  - 目前仅限单个项目使用，跨项目信任传播仍为愿景，尚未实际落地。
  - 担保人机制可能增加新贡献者的参与门槛，与开源社区的低门槛参与理念存在潜在矛盾。
  score: 7.0
  article_ids:
  - 61cebb5cfcee9b53
  evidence_snippets:
  - Mitchell Hashimoto 发布了 Vouch，一个为开源贡献者设计的信任管理系统，未经过担保的用户无法贡献。
  - Vouch 的愿景是让信任决策最终在不同项目之间传播，类似开源版的发件人声誉评分系统。
---

I'm Rahul, and I work at Greptile, where we build AI agents that review pull requests. Greptile reviews PRs for OpenClaw which became the fastest-growing repo in GitHub history almost overnight. That gave us a front row seat to something strange.

Last December, OpenClaw was getting two pull requests a week. By February, that number jumped to 3,400/week. Before the spike, ~48% of PRs got merged; after, fewer than 9.3% of PRs got merged.

Many of those PRs were low-effort slop which were often generated by people's AI coding agents. For example, one contributor submitted 106 PRs in a single day, with the median time between submissions being *three seconds*.

In many ways, openclaw/openclaw offers us a preview of what the future of open source contribution may look like. Here are three observations:

### PRs will require sender reputation

PR spam today looks like email spam in the early 2000s.

When I first looked at the OpenClaw data, the pattern reminded me of email. In 2000, the ILOVEYOU worm infected 45 million computers in 24 hours because the cost of sending email approached zero and people trusted the platform. As a result, people were receiving a much higher volume of emails, and some of them were malicious. Those same parameters apply to PRs today.

The first fixes are similar: blocklists to manage volume, and confidence-based filters and reputation infrastructure to catch bad actors. Today, whether your email reaches its recipient's inbox comes down to two things: who you are, and your sending history.

Contributors on OpenClaw are already being filtered by their reputation: 8.2% merge rate for first-timers, 10.3% for contributors with 2-5 PRs, 18.6% for 5+.

Mitchell Hashimoto created and maintains Ghostty, one of the most popular open source terminal emulators. As the project gained momentum, people submitted such a high volume of AI-generated PR slop that he needed to limit AI-generated contributions.

A week later, he released a solution: Vouch, a trust management system for open source contributors. Unvouched users can't contribute, and bad actors get explicitly flagged. While Vouch is project-specific for now, Mitchell's vision is for trust decisions to eventually ripple across projects that share similar values. Vouch is the open source equivalent of a sender reputation score. (Worth noting: while Vouch was working well for Ghostty, Mitchell decided to take Ghostty off GitHub.)

### More contributors won't help if they all think the same way

Linus Torvalds has a famous line: "Given enough eyeballs, all bugs are shallow."

Having more eyes on the same problem brings diverse perspectives. Different people use software differently, encounter different bugs, and approach fixes in novel ways.

That rule might not hold when everyone converges on Claude / Codex / Cursor / Devin etc. In OpenClaw:

- 4 contributors submitted PRs with the exact title "feat(web-search): add SearXNG as a search provider." They were 4 of 10+ people who independently tried to add the same feature.
- 6 people independently fixed the same Brave Search locale bug. 2 submitted PRs with identical titles 94 minutes apart.
- 5 people independently found the same timeout deadlock in the agent runner.

There are more eyes on OpenClaw than ever, but their perspectives are also being filtered by AI coding agents. If most contributors use the same AI coding agents with the same prompts, then their contributions will resemble each other as well.

The promise and advantage of open source has been diversity of thought. Linus's law only holds if the underlying thinking remains diverse too. A contributor who really studies a codebase will prompt differently than one who doesn't.

### What's actually getting merged

In the OpenClaw PR data, features have a 9% merge rate, while refactors merge at 35%.

The contributions requiring a deep understanding of the existing codebase outperform novel feature contributions by nearly 4x. It's the common adage these days; the thinking matters a lot more than the typing. The data backs it up.

For example, the way claude-mem maps Claude Code's hook-captured tool stream into its own resumable Agent SDK observer session is a non-obvious architectural choice that requires a deep understanding of both systems. A software developer who understood this decision would be able to distill it into a checklist, which would become the prompt that makes the agent's output significantly better. An agent prompted to "build a memory system" wouldn't be able to achieve that on its own.

Until 200 years ago, the people who designed buildings also constructed them. They were known as master builders. As construction advanced, that role split into two crafts: architecture and construction. The analogy to software isn't clean. Architects still need to know how buildings stand up. But it points at something real: the contributions that survive review are increasingly the ones an agent can't do alone, the calls that require deep understanding of an existing system, not novel construction.

### So, what's next?

OpenClaw went from nothing to a real world Jarvis in a few short months. One person, along with a strong community, was able to build at a pace that wasn't possible a year ago. That's pretty special.

The open source community can build faster than ever. The problems introduced by this speed will need better primitives in identity, reputation, and how we validate contributions, which will all be built. Open source has solved harder problems before.