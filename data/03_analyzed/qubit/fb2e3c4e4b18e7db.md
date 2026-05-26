---
title: OpenAI大神教你如何榨干Codex
source: https://www.qbitai.com/2026/05/423179.html
author:
- '[[听雨]]'
published: '2026-05-23'
created: '2026-05-24'
description: 13k星开源库作者解锁Codex-maxxing！
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: fb2e3c4e4b18e7db
source_type: news_media
tldr: OpenAI Codex 团队成员 Jason Liu 公开分享将 Codex 打造为长期运行自主工作系统的完整方法论
objective_summary: 2026年5月，OpenAI Codex 团队新成员 Jason Liu（开源库 Instructor 作者）在社交平台发布
  Codex-maxxing 使用心法，展示如何通过跨月存活线程、Heartbeats 定时调度、Obsidian 本地记忆管理等手段将 Codex
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - Amazon
  - Slack
  - GitHub
  technologies:
  - Codex
  - Heartbeats
  - Goal
  - Appshots
  - Chronicle
  - Connectors
  - Skills
  - Steering
  - MCP
  - Instructor
  - Obsidian
  key_people:
  - Jason Liu
key_logic_flow:
- Jason Liu 的核心方法论是将 Codex 会话改造为跨月存活的巨型线程，通过积累对话历史和决策实现 Agent 的连续性工作能力
- Heartbeats 定时调度机制让 Codex 可每 30 分钟自动扫描 Slack/Gmail 并起草回复，或每 15 分钟检查审阅线程反馈并自动推进任务
- Jason 强调任务必须建立可验证的反馈闭环（如通过单元测试作为完成标准），否则自动化仅为愿望而非可交付成果
- Codex Goal 模式已从实验版转正，用户设定最终目标和验收标准后 Agent 可自主持续数小时至数天推进
- Jason 放弃 Codex 内置记忆系统，将核心记忆数据存放在本地 Obsidian vault 中，通过 AGENTS.md 规则同步更新，实现工具无关的知识库可迁移性
- Codex 近期更新包括 Appshots 截图直喂、锁屏后远程工作、侧边栏支持 Markdown/PDF/PPT 渲染及内置浏览器 JavaScript 操控能力，周活用户已破
  400 万
impact_score:
  score: 6.5
  reason: 这是一次高质量的产品使用方法论公开分享，而非新品发布或技术突破。核心价值在于：1）揭示了 Codex 从单次问答工具向长期自主工作系统的演进方向，Heartbeats
    定时调度 + Goal 模式组合代表了 AI Agent 产品化的关键范式；2）Codex 周活破 400 万的里程碑具有行业信号意义；3）Jason Liu
    提出的'本地文件系统作为记忆基础设施'理念对 AI 工具生态的锁定问题有反思价值。但本质仍属于 power user 经验分享，不构成行业范式转移，故评分
    6.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Heartbeats 定时调度机制与跨月存活巨型线程的工程可行性，以及本地 Obsidian vault 替代平台内置记忆的架构选择
hype_assessment:
  level: medium
  reason: 文章标题使用'大神''榨干'等自媒体流量话术，且 QuantumBit 作为科技媒体天然有包装倾向。但正文内容以 Jason Liu 的实操方法论为主，包含了
    Heartbeats 调度间隔、Obsidian 目录结构、验证闭环设计等具体细节，干货占比较高。PR 水分主要体现在标题渲染和部分场景描述（如'洗澡时自动退款'）的戏剧化处理，核心方法论本身有实质内容支撑，故判定为中等炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 核心技术突破在于 Agent 运行时架构的三个设计模式：1）Heartbeats 定时轮询机制将 Agent 从被动响应转变为主动巡检，配合
    MCP 协议实现跨平台（Slack/Gmail/GitHub）事件驱动自动化；2）跨月存活巨型线程通过累积对话历史实现 Agent 的长期上下文连续性，解决了当前大模型会话无状态的工程痛点；3）以本地文件系统（Obsidian
    vault + AGENTS.md）替代平台内置记忆的方案，实现了记忆数据的工具无关性和可迁移性。这些并非算法层面的突破，而是 Agent 产品工程的最佳实践凝练。
  business_model: 对商业模式的影响体现在三个层面：1）AI 编码助手从按会话计费的工具型产品向按持续运行时间计费的'数字员工'平台演进，Codex
    的 Heartbeats + Goal 模式正在模糊 SaaS 工具与劳动力外包的边界；2）Jason 强调的本地记忆策略暗示用户对平台数据锁定的警惕，可能催生以可迁移性为卖点的第三方记忆管理工具生态；3）Connectors
    + Skills 的可复用工作流模版机制，预示着 AI Agent 应用商店/技能市场的商业化路径，类似 Slack App Directory 或 GitHub
    Actions Marketplace。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: 该事件标志着 AI Agent 从「单次问答工具」向「持久自主劳动力」的范式迁移，具有极强的长期复利效应。核心逻辑有三层：(1) 跨月存活线程积累的对话历史、偏好与决策形成天然切换成本——使用越久，替代成本越高，这是典型的复利护城河；(2)
    Heartbeats 定时调度 + 可验证反馈闭环（单元测试、人工审批节点）使 Agent 从「辅助」升级为「替代」，直接切入 RPA 和初级白领工作的 TAM，市场空间十倍于纯开发者工具；(3)
    Codex 周活 400 万 + Goal 模式转正，说明该范式已跨过实验阶段进入规模化。3-5 年后，具备持久运行能力的 Agent 大概率成为知识工作者的标配基础设施，而非昙花一现的功能。风险在于开源竞品（如
    Claude Code）正在追赶，OpenAI 能否在产品体验和生态锁定上持续领先尚需验证。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Obsidian
- Slack
- GitHub
competitive_casualty:
- Anthropic (Claude Code)
- Cursor
- 传统 RPA 厂商 (UiPath, Automation Anywhere)
- 单次对话式 AI 编码助手 (Codeium, Tabnine)
- 独立 AI Agent 框架 (CrewAI, AutoGPT)
market_opportunities:
- 基于「本地文件系统 + AGENTS.md 规则」的记忆管理范式，可开发跨 AI Agent 平台的知识库同步工具，帮助用户将个人工作记忆从单一平台解耦，实现
  Claude Code、Codex、Cursor 等工具间的知识无缝迁移
- Heartbeats 定时调度 + 可验证反馈闭环的 Agent 工作流模式具备产品化潜力，创业者可构建面向开发者的「Agent CI/CD」平台，将单元测试、PR
  Review、Slack 反馈等事件作为 Agent 任务的触发器和完成标准
- Jason 强调的「可复用工作流模版」（Connectors/Skills）揭示了 AI Agent 时代的协作新需求——个人和小团队可将已验证成功的 Agent
  工作流打包为可交易或共享的模版，类似 GitHub Actions 的 Agent Skills 市场机会已经出现
risk_matrix:
  regulatory: AI Agent 自主访问电子邮件、Slack 消息、电商账户并执行退款/回复等操作，涉及多国数据隐私法规（GDPR、CCPA）的同意授权边界问题，且
    Agent 冒充用户进行金融操作可能触发消费者保护法合规风险
  technological: 方法论高度依赖 Codex CLI 的特定功能（Heartbeats、Goal、Appshots），尽管 Jason 通过 Obsidian
    做记忆解耦，但任务执行层仍存在明显的平台锁定风险；此外 Agent 长期线程的上下文膨胀可能导致推理质量衰减和 token 成本失控
  competitive: Anthropic 的 Claude Code、Google 的 Gemini CLI、Cursor 等竞品正在快速补齐 Agent
    自主工作能力，Codex 的先发优势窗口正在收窄；各平台 Agent 协议互不兼容将导致用户被迫选边站队，生态碎片化加剧
  ethical: AI Agent 在用户洗澡、锁屏期间自主完成亚马逊退款、起草并发送消息等操作，存在越权决策风险（Agent 可能误判退款条件或发送不当回复）；长期无人监督的自主运行模式模糊了人类与
    AI 的责任归属边界，一旦出现错误操作，问责链难以追溯
  additional:
  - 400 万周活用户规模下，若 Heartbeats/Goal 模式被广泛采用，Codex 后台算力消耗将呈指数级增长，OpenAI 可能在短期内调整定价策略或施加并发限制，影响重度用户的投资回报预期
  - Agent 跨月线程积累的对话历史和决策偏好构成高价值个人数据资产，若 Codex 云端存储被攻击或内部泄露，用户的沟通习惯、项目规划、商业决策等敏感信息将大面积暴露
confidence:
  impact: medium
  compound: high
  hype: high
actionable_insight: strategic_invest
---

# OpenAI大神教你如何榨干Codex

13k星开源库作者解锁Codex-maxxing！

### 闻乐 发自 凹非寺

量子位 | 公众号 QbitAI

新晋员工确实毫无保留。

**Jason Liu**，13k星开源库Instructor的作者，刚被OpenAI招进Codex团队没多久，不仅在社交平台大方发API额度；

还写了篇**Codex-maxxing**，把自己的Codex玩法全抖出来了。

而且是让Codex自动跟进亚马逊退款、定时扫Slack接需求、开着Heartbeats在你洗澡的时候帮你干活的那种。

Codex周活用户4月底已经破了400万，终于来了份“官方使用指南”。

正好，这两天Codex又更新了一波：**Appshots截图直喂、Goal模式正式转正、锁屏后也能远程干活**。

跟Jason的使用心法叠在一起看会发现，现在大家比拼的，是谁能持续工作更久，谁能真正上岗了……

**让它自己跑起来**

Jason整套玩法的核心，是把Codex改造成了一个能长期运行、持续接管任务的工作系统。

多数人习惯单次问答结束就关闭会话，但Jason是开着一堆**跨月存活的巨型线程**，不会随意终止。

他给每个工作流一个置顶线程：管日程的一个、管开源项目的一个、监控社交平台的一个……通过Command-1到Command-9一键跳转。

线程里积累了几个月的对话历史、偏好和决策，再次使用时不用重新交代背景，Agent就能自动承接进度。

当线程生命周期被拉长后，项目背景、沟通习惯和历史决策都会自然沉淀进去，Agent开始具备连续性。

而且Jason下任务不打字，主要靠说。

在他看来，口述能完整保留原始思路，不需要刻意优化Prompt，可以直接把模糊、跳跃、带溯源需求的想法原样丢给Agent。

再配合Codex的Steering功能，还能在Agent执行任务时插队追加指令，说完就走，不用干等。

不过，真正让Codex从工具变员工的，是**Heartbeats+@computer**这套组合拳。

Heartbeats本质上相当于给Agent加了一层定时任务调度。

Jason有个Chief of Staff线程，每30分钟跑一次——

扫一遍Slack和Gmail，看看有没有需要回复的消息，判断优先级，需要回复的先起草一份草稿，但不发送，最终由人来决定是否发出。

他还举了一个更复杂的例子是，做动画项目时，他会先把视频发到Slack审阅线程，然后让Codex每15分钟检查一次线程。

如果同事提了反馈，Codex就重新渲染一个新版本并回复到线程里。

因为Slack MCP服务器还不支持文件上传，Agent甚至会自己调用@computer去点“Add file”按钮，把渲染好的文件传上去。

还有一次，Jason在洗澡前让Codex盯着亚马逊客服排队状态，结果等他洗完澡出来，退款已经到账了。

类似的流程，现在已经能扩展到Google Docs评论、GitHub PR Review等场景，只要有反馈就自动推进下一步。

Jason最强调的一点，是**验证机制**，可以判断任务什么时候终止。

他试过让Codex把Python的Rich库完整迁移到Rust，硬性要求是必须通过原Python库的所有单元测试。

测试能不能通过，决定了任务是否完成；失败了，Agent就继续修。

用他的话说：

没有验证机制的野心，顶多算个愿望而已。


而在最新的这次更新中，OpenAI已经把**Goal模式从实验版本转正了**。

你只要明确一个最终目标和验收标准，Codex会自主持续推进，短则几小时长则数天，中途可以查进度、调方向，也可以直接暂停。

但前提是任务本身必须存在清晰、可验证的反馈闭环。

**记忆放在自己手里**

Jason这套用法的另一大核心思路，是**个人工作记忆不应该托管在平台内部**。

他所有的长期线程都从一个Obsidian vault起步，目录划分为TODO、people、projects、agent、notes等板块。

在顶层AGENTS.md里写明规则：人员信息更新、项目推进、待办办结等变动，都要同步更新知识库对应内容。

也就是说，他几乎放弃了Codex的内置记忆系统，把核心记忆数据存放在本地可控文件中，既能随时查阅手动修改，也能通过版本对比查看变动，出现问题还能一键roll back。

原因是AI承载的记忆体量越大，就越不该把数据锁死在单一平台。

而文件是完全属于用户自己的，后续想换工具、迁平台，拎着知识库就能走，毫无顾虑。

他也提到了Codex自带的记忆功能**Chronicle**，通过截取屏幕内容来构建上下文。

但这是需要手动开启的实验预览功能，在权限、速率和隐私方面存仍在短板，整体方向可行但还不够成熟。

所以，在他看来，文件系统仍然是最可靠的记忆基础设施。

而且Codex工作台本身也在升级。

Codex的侧边栏不再局限聊天交互，可直接渲染Markdown、筛选表格、阅览PDF与PPT。

Agent还能通过内置浏览器用JavaScript控制网页，用户可以边看边标注，不用来回切窗口。

Jason说他经常在侧边面板里同时打开Storybook审阅UI组件、用Remotion Studio做动画、用Slidev做演示文稿。

而他最喜欢的交付形式，就是一个带JS和CSS的单文件index.html，不用部署，不用服务器，打开就能跑。

另外，他还把Connectors和Skills作为可复用工作流模版。

只要成功做完一件有用的事，就把流程打包起来，下次Codex不用重新学，直接调用就行。

最近Codex还补了一手远程能力，电脑锁屏后Codex可以继续工作，手机端也能实时查看、审批甚至接管任务。

现在好了，你下班它加班，你锁屏它干活，超额KPI这不就来了……

不过，当AI可以持续接管工作，人自己倒是越来越轻松了（doge）。

*参考链接：https://x.com/jxnlco/status/2057153744630890620*

*版权所有，未经授权不得以任何形式转载及使用，违者必究。*