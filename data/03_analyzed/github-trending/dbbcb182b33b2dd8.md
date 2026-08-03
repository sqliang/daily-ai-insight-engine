---
title: citrolabs/ego-lite
source: https://github.com/citrolabs/ego-lite
author: []
published: ''
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
- '2026-07-25'
- '2026-07-26'
- '2026-07-27'
description: 'The best browser for both you and your AI agents work in parallel. The
  best browser for both you and your AI agents work in parallel. ego (lite) is a browser
  where you and your AI agents work in parallel. Your agents run multiple browser
  tasks in their own Spaces while your tabs stay yours, and tasks complete faster
  on fewer tokens. Existing tools like browser-use and agent-browser are browser automation
  frameworks: they need a separate browser to drive, logins never carry cleanly, and
  you and the agent end up fighting for the same tabs. ego lite is one browser designed
  from the start for the two of you to share. No extra setup, and the agent can always
  reach your real logins and tabs through ego-browser. Demo https://github.com/user-attachments/assets/ffe7954b-58ee-411e-b35d-ec30c58a08bc
  Quick Start ego lite runs on macOS today. Windows and Linux are on the roadmap.
  1. Install Pick whichever fits your flow. 1.1 Download the macOS app Click to download,
  then open it to install. Either way, ego lite adds the ego-browser skill to every
  agent''s skills directory on your machine. 1.2 Add the skill with npx Install just
  the ego-browser skill: npx skills add citrolabs/ego-lite The first time your agent
  runs a browser task, it walks you through installing the ego lite app. 1.3 Let your
  agent set it up Paste this into your agent: Set up ego lite for me: https://github.com/citrolabs/ego-lite
  Read `skills/ego-browser/references/install.md` and follow the steps to install
  ego lite. On first launch, ego lite asks one question, whether to migrate your Chrome
  data. Say yes and your agent inherits your existing logins, cookies, extensions,
  and bookmarks. 2. Run your first task In your agent CLI, type /ego-browser followed
  by a space, then describe what you want in plain language: ego-browser follow @ego_agent
  on x.com for me The agent picks up the ego-browser skill, opens the page in its
  own Space, reads a Snapshot, acts on the page, and reports back, all while your
  own tabs stay untouched. Your browsing data stays on your device. ego lite only
  records whether you opted into Chrome migration during setup. Highlight of ego lite
  Feature What it does Code base, not CLI base, for faster runs with fewer tokens
  on complex tasks The capabilities ego lite exposes to the agent are wrapped as JavaScript
  functions the agent calls directly. The agent gets to do what it does best: write
  code, composing a multi-step task into a single output instead of getting stuck
  in a "call two commands, look at the result, call two more commands" loop. Compared
  to the conventional CLI approach, complex workflows finish up to 2.5× faster with
  higher task success rates and far fewer tool calls per task. A dedicated Space for
  every agent ego lite gives each agent its own fully isolated Space. You browse up
  front, your agent works in the background, and they don''t get in each other''s
  way. You can see which Space has an agent running at any moment, and take it over
  or stop it whenever you want. Your agents multitask in Spaces, parallel workspaces
  inside the same browser Each Space gets its own AI agent or its own task, all running
  at the same time. Claude Code enriching 10 leads in 10 parallel Spaces. Codex scraping
  5 competitor sites in 5 more. They don''t collide or steal your tabs. Your mouse
  stays where you left it. The strongest page Snapshot on the market Thanks to kernel-level
  customization, ego lite produces the highest-quality page snapshots, the view text
  models rely on to "see" and act on a webpage. It reliably handles tough cases like
  deeply nested iframes, exactly where other approaches consistently break down. Any
  agent can drive it through ego-browser ego-browser is the connection layer between
  any agent CLI (Claude Code, Codex, Cursor, or a custom one) and ego lite. It exposes
  the browser as a set of in-page JavaScript tools: snapshot, fill, click, wait, navigate,
  capture. The agent writes a JavaScript snippet calling those tools, and ego-browser
  runs it on the page in one pass. Experience accumulation that makes your agent faster
  the more you use it (coming soon) Most of an agent''s time on browser tasks goes
  to trial and error. ego lite''s official Skill distills every successful action
  into reusable tools and workflows, so similar tasks down the line run up to 5x faster.
  ego lite vs existing products Most tools can automate a browser. The real questions
  are what browser the agent gets, whether you can keep working at the same time,
  and whether the tool is built for the agent you already use or a built-in one. Capability
  ego lite Browser-Use agent-browser (Vercel) ChatGPT Atlas Perplexity Comet Multitask
  in parallel ✓ — — — — Reusable skills ✓ — — — — Inherits Chrome''s data ✓ — — ✓
  ✓ Same browser, separate workspace ✓ — — — — Compressed semantic input ✓ — ✓ — —
  Controllable by external agents ✓ ✓ ✓ — — Data stored locally ✓ ✓ ✓ — — No login
  friction ✓ — — ✓ ✓ Daily-use browser ✓ — — ✓ ✓ Free ✓ ✓ ✓ — — Two other categories
  try to solve the same problem. Browser automation frameworks like Browser-Use and
  Vercel''s agent-browser are libraries the agent calls; they ship no browser of their
  own, so they need a separate one to drive and your logins rarely carry cleanly.
  AI browsers like ChatGPT Atlas and Perplexity Comet ship a built-in agent, and only
  that agent can drive the browser. ego lite is one browser, designed from the start
  for you and any agent you bring to share. Benchmarks We benchmarked ego lite against
  Vercel''s agent-browser on four complex browser automation tasks. ego lite finished
  each task up to 2.5× faster, with substantially fewer tokens. The harder the task,
  the bigger the gap. Check the comparison. Docs Tutorials, the full tool reference,
  and integration guides live at lite.ego.app/document/. Community Discord, questions,
  setup help, and skill sharing GitHub Discussions, ideas and longer threads X/Twitter,
  updates and releases Star History License The contents of this repository are released
  under the MIT License. The ego lite browser is a separate, free download.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dbbcb182b33b2dd8
source_type: community_discussion
tldr: citrolabs 发布 ego-lite，一款为人类与 AI 代理并行使用而设计的浏览器。每个代理拥有独立的工作空间（Space），支持多任务并行、继承
  Chrome 登录态和书签、通过代码而非 CLI 驱动的交互方式，并声称在复杂任务上比 Vercel agent-browser 快 2.5 倍。
objective_summary: citrolabs 于 2026 年 7 月发布了 ego-lite，这是一款面向 AI 代理与人类用户并行工作的浏览器产品。它允许用户在常规标签页浏览的同时，让多个
  AI 代理在隔离的 Space 中独立执行浏览器任务。ego-lite 通过 JavaScript 函数封装浏览器能力，代理以编写代码而非调用 CLI 命令的方式控制浏览器，据称复杂工作流执行速度比
  Vercel 的 agent-browser 快 2.5 倍，且消耗更少 token。产品当前仅支持 macOS，Windows 和 Linux 版本正在规划中，免费使用并以
  MIT 许可证开源。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - citrolabs
  - Vercel
  - OpenAI
  - Perplexity
  technologies:
  - ego-browser
  - Browser-Use
  - agent-browser
  key_people: []
key_logic_flow:
- ego-lite 是一款专为人类和 AI 代理并行使用设计的浏览器，代理在独立的 Space 中运行任务，不干扰用户标签页。
- ego-lite 通过 JavaScript 函数而非 CLI 命令暴露浏览器能力，代理直接编写代码组合多步操作，复杂任务速度提升最高 2.5 倍。
- 首次启动时可迁移 Chrome 数据，代理自动继承用户的登录态、Cookie、扩展和书签。
- ego-lite 通过 ego-browser 技能层与任意代理 CLI（Claude Code、Codex、Cursor 等）对接。
- ego-lite 当前仅支持 macOS，Windows 和 Linux 版本在规划中，产品免费且以 MIT 许可证开源。
- ego-lite 自述在页面 Snapshot 质量上领先，通过内核级定制处理深层嵌套 iframe 等复杂场景。
object_mentions:
- object_type: product
  name: ego-lite
  canonical_name: citrolabs/ego-lite
  url: https://github.com/citrolabs/ego-lite
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ego-lite 是一款为人类与 AI 代理并行使用而设计的浏览器，代理在独立的 Space 中运行任务。
  - ego-lite 当前仅支持 macOS，Windows 和 Linux 版本在规划中，产品免费且以 MIT 许可证开源。
  article_id: dbbcb182b33b2dd8
- object_type: project
  name: ego-browser
  canonical_name: ego-browser
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ego-browser 是连接任意代理 CLI 与 ego-lite 浏览器的技能层，通过 JavaScript 工具暴露浏览器能力。
  - ego-browser 将浏览器能力封装为 in-page JavaScript 工具：snapshot、fill、click、wait、navigate、capture。
  article_id: dbbcb182b33b2dd8
- object_type: product
  name: agent-browser
  canonical_name: Vercel agent-browser
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - ego-lite 在基准测试中对比 Vercel 的 agent-browser，声称在复杂任务上快 2.5 倍且消耗更少 token。
  - 文章将 Browser-Use 和 Vercel agent-browser 归类为浏览器自动化框架，需要独立浏览器驱动且登录态不易继承。
  article_id: dbbcb182b33b2dd8
- object_type: product
  name: Browser-Use
  canonical_name: Browser-Use
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将 Browser-Use 归类为浏览器自动化框架，需要独立浏览器驱动且登录态不易继承。
  article_id: dbbcb182b33b2dd8
- object_type: product
  name: ChatGPT Atlas
  canonical_name: ChatGPT Atlas
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将 ChatGPT Atlas 归类为 AI 浏览器，内置固定代理且仅该代理能驱动浏览器。
  article_id: dbbcb182b33b2dd8
- object_type: product
  name: Perplexity Comet
  canonical_name: Perplexity Comet
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章将 Perplexity Comet 归类为 AI 浏览器，内置固定代理且仅该代理能驱动浏览器。
  article_id: dbbcb182b33b2dd8
extract_result: success
impact_score:
  score: 6.0
  reason: ego-lite 的发布填补了一个真实空白——现有方案要么是自动化框架（Browser-Use、agent-browser）需要额外启动浏览器且登录态难以传递，要么是封闭
    AI 浏览器（Atlas、Comet）只能使用内置代理。ego-lite 从架构层面重新设计了共享浏览器：隔离的 Space 实现人/代理并行、以 JS 函数而非
    CLI 命令暴露浏览器能力、继承 Chrome 登录态和 Cookie。这些差异化是实在的工程创新而非 PR 话术。但它仍处于早期阶段：仅支持 macOS、用户基数小、2.5x
    性能提升需要独立复现验证。评分 6.0：足以改变 agent 浏览器赛道的竞争格局和开发者预期，但尚未达到范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 代码直接操控浏览器而非 CLI 命令循环的并行 Space 架构，以及免费 MIT 开源
hype_assessment:
  level: medium
  reason: 文章提供了详细的技术对比表（ego-lite vs Browser-Use vs agent-browser vs Atlas vs Comet）和基准测试数据（复杂任务快
    2.5 倍、更少 token），这些是可验证的具体声明。但 'strongest page Snapshot on the market'、'Experience
    accumulation that makes your agent faster the more you use it' 等表述带有典型 PR 包装色彩，且
    2.5x 的性能提升仅在自选 benchmark 上验证，缺乏第三方复现。综合判定 medium 级别——有干货但存在一定包装。
information_entropy: high
domain_disruption:
  technical_innovation: 提出了一种新的浏览器架构：1）隔离的 Space 机制让多个代理和人类在同一浏览器实例中并行工作而不互相干扰，这不同于现有的单进程浏览器自动化方案；2）以
    JavaScript 函数而非 CLI 命令作为代理操控浏览器的原语，将多步操作编译为单段代码执行，从工程上消除了 CLI 循环的往返开销；3）内核级 Snapshot
    定制支持深层嵌套 iframe 等复杂 DOM 场景的可靠序列化。这三项创新共同构成了一个更高效的 agent 浏览器控制范式。
  business_model: MIT 开源+免费+生态驱动——以开源社区吸引开发者采用，通过 'ego-browser' 技能层和即将推出的 Experience
    Accumulation（复用成功操作流）构建网络效应，潜在商业变现路径包括企业版、技能市场或高级 Snapshot API。对现有商业 AI 浏览器（Atlas、Comet）构成定价压力，对
    Vercel agent-browser 等开源方案则形成架构层面的竞争。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 'ego-lite 切入的是 AI Agent 基础设施中尚未被占领的浏览器层。长期复利逻辑来自三个方面：


    (1) **架构级差异化**：平行 Space + 代码驱动范式不是 feature 层面的微创新，而是对''浏览器如何与 AI 代理交互''的根本性重构。代码组合而非
    CLI 调用的方式，在复杂多步任务上展示的 2.5x 性能优势不仅是速度指标，更意味着 agent 的可用 token 预算被更高效利用——这会随着任务复杂度提升而放大。即将推出的
    Experience Accumulation 功能若兑现，将形成''使用越多、速度越快''的数据飞轮，这是真正的护城河基础。


    (2) **生态位卡位**：与所有主流 Agent CLI（Claude Code、Codex、Cursor）兼容 + MIT 开源策略，使其有机会成为 Agent
    浏览器领域的''默认选择''。浏览器作为入口级产品具有极强的锁定效应——一旦开发者工作流和 agent skill 生态围绕 ego-browser 构建，迁移成本极高。对标价值：如果
    Playwright/Selenium 是 Web 2.0 时代的浏览器自动化标准，ego-lite 有机会成为 Web + Agent 时代的对应层。


    (3) **数据继承优势**：首次启动无缝继承 Chrome 登录态、Cookie、扩展和书签，极大降低了用户和 agent 的迁移摩擦。这一点看似简单，实则是
    adoption 的关键门槛——历史上有大量浏览器挑战者失败正是因为用户不愿重新配置。


    **风险项**：浏览器赛道历史成功率极低（Chrome/WebKit 双寡头统治十余年），macOS 独占限制早期 TAM，开源授权在加速 adoption
    的同时削弱了商业价值捕获能力。此外，Vercel（agent-browser）和 OpenAI（Atlas）均有资源在自家产品中快速跟进类似能力。若 citrolabs
    未能在跨平台发布后的 6-12 个月内建立足够深的开发者生态或找到商业模式（企业版 / 云托管 / premium skill market），复利效应可能被竞争对手稀释。


    综合判断：这是一个高 Beta 的早期押注——若 AI Agent adoption 按当前预期增长，ego-lite 有机会成为 AI 时代的浏览器基础设施；若
    agent 热潮降温或巨头快速复制，则可能沦为小众工具。7 分反映的是其''正确赛道 + 正确架构 + 早期先发''的潜力溢价。'
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- citrolabs
- Claude Code (Anthropic)
- Codex (OpenAI)
- Cursor (Anysphere)
- AI Agent 开发者社区
competitive_casualty:
- Vercel (agent-browser)
- Browser-Use
- ChatGPT Atlas (OpenAI)
- Perplexity Comet
- 传统浏览器自动化框架 (Playwright/Selenium)
market_opportunities:
- 企业可基于 ego-lite 的并行 Space 架构，构建多代理浏览器自动化平台，实现批量数据采集、竞品监控和销售线索挖掘等高频任务的并行执行，显著提升人机协作效率
- 围绕 ego-browser 技能层生态，开发者可构建垂直领域的浏览器代理技能包（如电商比价、表单自动填充、SaaS 流程编排），形成可复用的技能市场
- ego-lite 的"代码而非 CLI"驱动范式为 AI 浏览器交互提供了新思路，开发者可借鉴其 JavaScript 函数封装方式，优化现有 Web 自动化工具的代理交互架构
risk_matrix:
  regulatory: 代理自动继承 Chrome 登录态和 Cookie 存在数据隐私合规风险，尤其在欧洲 GDPR 和中国《个人信息保护法》框架下，用户对代理访问个人账户的知情同意边界不清晰，且
    MIT 许可证下责任归属不明
  technological: 当前仅支持 macOS 严重限制用户群体；浏览器自动化赛道技术迭代极快，若主流框架（如 Browser-Use、agent-browser）快速跟进多空间和代码驱动范式，ego-lite
    的技术差异化将被削弱
  competitive: 面临三方竞争夹击：开源社区活跃的 Browser-Use、生态整合能力强的 Vercel agent-browser、自带代理一体化体验的
    ChatGPT Atlas 和 Perplexity Comet，新兴项目获客成本高且用户迁移壁垒低
  ethical: 代理在用户浏览器操作时可能无意访问或泄露敏感个人信息（如邮箱内容、银行页面），多个代理并行时的行为审计和问责机制尚不明确，存在用户数据滥用隐患
  additional: []
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: speculative_watch
object_insights:
- object_type: product
  name: ego-lite
  canonical_name: citrolabs/ego-lite
  url: https://github.com/citrolabs/ego-lite
  positioning: 一款专为人类与AI代理并行使用而设计的浏览器，代理在独立Space中运行任务，同时人类可以正常浏览网页。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要并行执行浏览器自动化任务的AI代理用户
  - 使用Claude Code、Codex、Cursor等代理CLI的开发者
  - 需要代理继承Chrome登录态完成复杂操作的技术用户
  product_signal: 通过JavaScript函数而非CLI命令暴露浏览器能力，代理直接编写代码组合多步操作，复杂任务速度提升最高2.5倍且消耗更少token。
  market_signal: 声称在复杂浏览器自动化任务上比Vercel agent-browser快2.5倍，与Browser-Use、ChatGPT Atlas等竞品形成差异化竞争定位。
  differentiation: 唯一支持代理并行多任务、可继承Chrome登录态和书签、且允许人类与多代理在同一浏览器中独立工作的产品，兼具浏览器和自动化框架双重属性。
  watch_reason: ego-lite代表了浏览器与AI代理协作的新范式，将浏览器从自动化框架升级为人类与多代理并行工作的基础设施，其以代码而非CLI驱动的交互模式有望重塑AI代理操作浏览器的标准方式，值得持续跟踪其采用速度和生态扩展。
  risk_notes:
  - 当前仅支持macOS，Windows和Linux版本仍在规划中，跨平台兼容性限制可能延缓早期用户采用。
  - 作为新生浏览器产品，需与Browser-Use等成熟自动化框架及ChatGPT Atlas等AI浏览器竞争，市场不确定性较高。
  score: 8.0
  article_ids:
  - dbbcb182b33b2dd8
  evidence_snippets:
  - ego-lite 是一款为人类与 AI 代理并行使用而设计的浏览器，代理在独立的 Space 中运行任务。
  - ego-lite 当前仅支持 macOS，Windows 和 Linux 版本在规划中，产品免费且以 MIT 许可证开源。
- object_type: project
  name: ego-browser
  canonical_name: ego-browser
  url: null
  positioning: 连接任意AI代理CLI与ego-lite浏览器的技能层，通过in-page JavaScript工具暴露浏览器能力，是代理控制浏览器的标准化接口。
  technical_signal: 将浏览器能力封装为snapshot、fill、click、wait、navigate、capture等JavaScript工具，代理通过编写代码单次传递完成多步操作，无需反复调用CLI命令。
  adoption_signal: null
  ecosystem_relevance: 可对接Claude Code、Codex、Cursor等多种主流代理CLI，作为桥梁定义了AI代理操作Web浏览器的标准化接口模式，具有生态杠杆价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ego-browser提出的'代码而非CLI'的代理浏览器交互范式，有别于传统自动化框架的命令行循环模式，有望成为AI代理操作Web浏览器的行业标准接口，值得持续跟踪其采用范围和生态扩展情况。
  risk_notes:
  - 作为ego-lite的附属技能层，其发展前景高度依赖ego-lite浏览器的市场采用和用户基础。
  - 目前仅与有限的代理CLI兼容，生态覆盖广度有待验证。
  score: 7.0
  article_ids:
  - dbbcb182b33b2dd8
  evidence_snippets:
  - ego-browser 是连接任意代理 CLI 与 ego-lite 浏览器的技能层，通过 JavaScript 工具暴露浏览器能力。
  - ego-browser 将浏览器能力封装为 in-page JavaScript 工具：snapshot、fill、click、wait、navigate、capture。
- object_type: product
  name: agent-browser
  canonical_name: Vercel agent-browser
  url: null
  positioning: Vercel推出的浏览器自动化框架，代理通过CLI命令驱动独立浏览器执行操作，需额外配置浏览器驱动环境。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为被ego-lite对标的主流浏览器自动化框架，其与新兴方案的性能和架构差异反映了浏览器代理技术的演进方向，值得关注后续迭代和竞争回应。
  risk_notes: []
  score: 2.0
  article_ids:
  - dbbcb182b33b2dd8
  evidence_snippets:
  - ego-lite 在基准测试中对比 Vercel 的 agent-browser，声称在复杂任务上快 2.5 倍且消耗更少 token。
  - 文章将 Browser-Use 和 Vercel agent-browser 归类为浏览器自动化框架，需要独立浏览器驱动且登录态不易继承。
- object_type: product
  name: Browser-Use
  canonical_name: Browser-Use
  url: null
  positioning: 开源浏览器自动化框架，代理通过库调用方式控制浏览器操作，需依赖独立浏览器驱动完成页面交互。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为开源浏览器自动化框架的代表，其技术路线与专用浏览器方案形成对比，反映了行业对Agent浏览器控制方式的不同探索方向。
  risk_notes: []
  score: 2.0
  article_ids:
  - dbbcb182b33b2dd8
  evidence_snippets:
  - 文章将 Browser-Use 归类为浏览器自动化框架，需要独立浏览器驱动且登录态不易继承。
---

ego (lite) is a browser where you and your AI agents work in parallel. Your agents run multiple browser tasks in their own Spaces while your tabs stay yours, and tasks complete faster on fewer tokens.

Existing tools like browser-use and agent-browser are browser automation frameworks: they need a separate browser to drive, logins never carry cleanly, and you and the agent end up fighting for the same tabs. ego lite is one browser designed from the start for the two of you to share. No extra setup, and the agent can always reach your real logins and tabs through `ego-browser`

.

## 01_codex_x_scape_1080p_265.mp4

ego lite runs on macOS today. Windows and Linux are on the roadmap.

Pick whichever fits your flow.

**1.1 Download the macOS app**

Click to download, then open it to install. Either way, ego lite adds the `ego-browser`

skill to every agent's skills directory on your machine.

**1.2 Add the skill with npx**

Install just the `ego-browser`

skill:

`npx skills add citrolabs/ego-lite`

The first time your agent runs a browser task, it walks you through installing the ego lite app.

**1.3 Let your agent set it up**

Paste this into your agent:

```
Set up ego lite for me: https://github.com/citrolabs/ego-lite
Read `skills/ego-browser/references/install.md` and follow the steps to install ego lite.
```


On first launch, ego lite asks one question, whether to migrate your Chrome data. Say yes and your agent inherits your existing logins, cookies, extensions, and bookmarks.

In your agent CLI, type `/ego-browser`

followed by a space, then describe what you want in plain language:

```
ego-browser follow @ego_agent on x.com for me
```


The agent picks up the `ego-browser`

skill, opens the page in its own Space, reads a Snapshot, acts on the page, and reports back, all while your own tabs stay untouched.

Your browsing data stays on your device. ego lite only records whether you opted into Chrome migration during setup.

| Feature | What it does |
|---|---|
Code base, not CLI base, for faster runs with fewer tokens on complex tasks |
The capabilities ego lite exposes to the agent are wrapped as JavaScript functions the agent calls directly. The agent gets to do what it does best: write code, composing a multi-step task into a single output instead of getting stuck in a "call two commands, look at the result, call two more commands" loop. Compared to the conventional CLI approach, complex workflows finish up to 2.5× faster with higher task success rates and far fewer tool calls per task. |
A dedicated Space for every agent |
ego lite gives each agent its own fully isolated Space. You browse up front, your agent works in the background, and they don't get in each other's way. You can see which Space has an agent running at any moment, and take it over or stop it whenever you want. |
Your agents multitask in Spaces, parallel workspaces inside the same browser |
Each Space gets its own AI agent or its own task, all running at the same time. Claude Code enriching 10 leads in 10 parallel Spaces. Codex scraping 5 competitor sites in 5 more. They don't collide or steal your tabs. Your mouse stays where you left it. |
The strongest page Snapshot on the market |
Thanks to kernel-level customization, ego lite produces the highest-quality page snapshots, the view text models rely on to "see" and act on a webpage. It reliably handles tough cases like deeply nested iframes, exactly where other approaches consistently break down. |
Any agent can drive it through `ego-browser` |
`ego-browser` is the connection layer between any agent CLI (Claude Code, Codex, Cursor, or a custom one) and ego lite. It exposes the browser as a set of in-page JavaScript tools: snapshot, fill, click, wait, navigate, capture. The agent writes a JavaScript snippet calling those tools, and `ego-browser` runs it on the page in one pass. |
Experience accumulation that makes your agent faster the more you use it (coming soon) |
Most of an agent's time on browser tasks goes to trial and error. ego lite's official Skill distills every successful action into reusable tools and workflows, so similar tasks down the line run up to 5x faster. |

Most tools can automate a browser. The real questions are what browser the agent gets, whether you can keep working at the same time, and whether the tool is built for the agent you already use or a built-in one.

| Capability | ego lite | Browser-Use | agent-browser (Vercel) | ChatGPT Atlas | Perplexity Comet |
|---|---|---|---|---|---|
| Multitask in parallel | ✓ | — | — | — | — |
| Reusable skills | ✓ | — | — | — | — |
| Inherits Chrome's data | ✓ | — | — | ✓ | ✓ |
| Same browser, separate workspace | ✓ | — | — | — | — |
| Compressed semantic input | ✓ | — | ✓ | — | — |
| Controllable by external agents | ✓ | ✓ | ✓ | — | — |
| Data stored locally | ✓ | ✓ | ✓ | — | — |
| No login friction | ✓ | — | — | ✓ | ✓ |
| Daily-use browser | ✓ | — | — | ✓ | ✓ |
| Free | ✓ | ✓ | ✓ | — | — |

Two other categories try to solve the same problem. Browser automation frameworks like Browser-Use and Vercel's agent-browser are libraries the agent calls; they ship no browser of their own, so they need a separate one to drive and your logins rarely carry cleanly. AI browsers like ChatGPT Atlas and Perplexity Comet ship a built-in agent, and only that agent can drive the browser. ego lite is one browser, designed from the start for you and any agent you bring to share.

We benchmarked ego lite against Vercel's agent-browser on four complex browser automation tasks. ego lite finished each task up to 2.5× faster, with substantially fewer tokens. The harder the task, the bigger the gap. Check the comparison.

Tutorials, the full tool reference, and integration guides live at lite.ego.app/document/.

- Discord, questions, setup help, and skill sharing
- GitHub Discussions, ideas and longer threads
- X/Twitter, updates and releases

The contents of this repository are released under the MIT License. The ego lite browser is a separate, free download.