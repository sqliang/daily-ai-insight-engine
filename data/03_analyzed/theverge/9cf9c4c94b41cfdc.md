---
title: OpenAI rolls out GPT-5.6 after government greenlight — and announces ‘ChatGPT
  Work’
source: https://www.theverge.com/ai-artificial-intelligence/963464/openai-gpt-5-6-codex-chatgpt-work
author:
- '[[Hayden Field]]'
published: '2026-07-09'
created: '2026-07-10'
description: About two weeks after OpenAI's GPT-5.6 was caught up in regulatory drama
  - rolled out only to government-approved organizations during a "limited preview"
  period - the company has received the Trump administration's greenlight for a public
  rollout of the model. OpenAI CEO Sam Altman called it "the best model we have ever
  produced." To celebrate, [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 9cf9c4c94b41cfdc
source_type: news_media
tldr: OpenAI 获政府批准公开发布 GPT-5.6 并推出 ChatGPT Work 智能体
objective_summary: OpenAI 在获得特朗普政府批准后，公开发布 GPT-5.6 模型套件（Sol、Terra、Luna），同时推出结合 ChatGPT
  与 Codex 的 AI 智能体产品 ChatGPT Work，支持连接 Slack、Gmail 等工具并生成文档、表格等材料。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Anthropic
  - Google
  - Apple
  technologies:
  - GPT-5.6
  - Codex
  - ChatGPT Work
  - Claude Cowork
  - OpenClaw
  - Sol
  - Terra
  - Luna
  key_people:
  - Sam Altman
key_logic_flow:
- GPT-5.6 之前仅限政府批准机构使用，现获特朗普政府批准向公众公开发布
- OpenAI CEO Sam Altman 称 GPT-5.6 是公司迄今最好的模型
- OpenAI 发布新 AI 智能体 ChatGPT Work，将 ChatGPT 与 Codex 结合，面向非技术用户完成文档、表格、演示文稿和网页应用等任务
- ChatGPT Work 由 GPT-5.6 模型套件（Sol、Terra、Luna）驱动，配备统一的插件目录，可连接 Slack、Gmail、Google Drive、日历和
  CRM 等工具
- Mac/Windows 桌面端所有用户（含免费用户）立即可用，移动端和网页端 Pro/Enterprise/Edu 用户优先，Plus/Business 用户随后逐步开放
- ChatGPT Work 直接对标 Anthropic 的 Claude Cowork，Sol 模型主打编程、网络安全和科学领域的高性能低成本路线
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：GPT-5.6 从政府专用走向公众开放，本身是预期之内的节点性事件，影响有限；但同日发布的 ChatGPT Work 是更关键的产品信号——将
    Codex 的编程能力封装为非技术用户可用的通用智能体（对标 Claude Cowork），配合统一插件目录打通 Slack/Gmail/Google Drive
    等企业工具链，标志着 AI 智能体从开发者工具向大众生产力工具的实质跨越。Sol 模型主打编程/安全/科学领域的低成本高性能路线，直接回应行业对 AI 成本转嫁的不满。整体来看是
    OpenAI 在智能体战场的重要落子，但不是范式转移级的冲击。评分：7.5
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Sol 模型的定价策略和实际性能是否能兑现低成本高智能的承诺
hype_assessment:
  level: medium
  reason: 判定依据：文章存在一定 PR 包装——Altman 称‘史上最好模型’是常规 CEO 话术，‘新智能和效率标准’也是常见夸大表述。但产品确实已公开发布、有明确功能和定价策略、有可验证的桌面端体验，并非空头支票。ChatGPT
    Work 的插件目录和 Codex 融合有实质技术内容支撑。综合判断存在适度水分，未到严重概念炒作程度。
information_entropy: medium
domain_disruption:
  technical_innovation: ChatGPT Work 将 Codex 的原型性编程能力通过智能体框架封装为非技术用户可用的文档/表格/演示/网页应用生成工具，配合统一插件目录（Slack、Gmail、Google
    Drive、CRM）实现跨应用上下文感知。Sol 模型在编程、网络安全和科学领域追求高性能低成本的工程权衡，可能改变模型选型的性价比基准线。
  business_model: ChatGPT Work 直接对标 Anthropic Claude Cowork，标志智能体从开发者专属（Codex/Claude
    Code）走向大众 SaaS 产品形态。结合插件生态的目录化分发，OpenAI 正在构建智能体时代的平台绑定层——用户通过 Work 接入的第三方工具越多，切换成本越高。Sol
    的低价策略则可能引发新一轮模型定价战，压缩中小 AI 厂商的利润空间。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: ChatGPT Work 的发布标志着 OpenAI 从模型提供商向 AI Agent 平台商的战略跃迁，其长期复利价值体现在三个层面：第一，统一的插件目录（Slack、Gmail、Google
    Drive、CRM 等）创造了生态网络效应——更多集成吸引更多用户，更多用户吸引更多第三方开发者，形成平台级锁定；第二，桌面端免费+全用户覆盖的 Distribution
    策略极低摩擦，一旦嵌入用户日常工作流，替换成本极高（习惯+集成依赖）；第三，Sol 模型主打高性能低成本路线，直接回应行业对推理成本膨胀的担忧，这意味着 ChatGPT
    Work 的单位经济模型可能优于竞品，能支撑更激进的定价和更广的渗透。主要风险在于：消费者级 AI Agent 市场仍处早期（文章直言'触手可及但尚未实现'），Anthropic
    Claude Cowork 形成正面竞争，且开源项目 OpenClaw 可能加速 Agent 能力的商品化。综合来看，这是一次有明确平台化意图的产品发布，若执行到位，3-5
    年后 ChatGPT Work 有望成为知识工作者的核心操作系统层。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- OpenAI
- Microsoft
- Slack/Salesforce
- Google
- Anthropic
competitive_casualty:
- 通用型 AI Agent 初创公司
- 传统 RPA 厂商（UiPath, Automation Anywhere）
- 低代码/无代码自动化平台（Zapier）
market_opportunities:
- 企业级 AI 智能体集成服务商可基于 ChatGPT Work 和 Claude Cowork 的插件生态，开发面向特定行业（如法律、医疗、金融）的定制化工作流模板与合规插件
- Sol 模型主打的编程、网络安全和科学领域高性能低成本路线，为创业公司在这些垂直领域开发生成式 AI 工具（如自动化安全审计、科学文献分析）提供了明确的商业化切入点
- AI 智能体的桌面端优先策略暗示桌面自动化场景存在蓝海机会，可围绕文档生成、跨应用数据编排等非技术用户痛点开发轻量级 SaaS 产品
risk_matrix:
  regulatory: GPT-5.6 从仅限政府批准机构使用到获政府批准才公开发布的过程，表明美国对前沿 AI 模型的出口管制和审批制度正在收紧，未来类似产品可能面临更长的审查周期和合规成本
  technological: 开源智能体 OpenClaw 的病毒式传播与 Anthropic、Google、Apple 的同步发力，形成多路线竞争，GPT-5.6
    的技术领先窗口可能因开源社区的快速追赶而缩短
  competitive: Anthropic Claude Cowork 已先行占据智能体赛道心智，Google 和 Apple 也在积极布局，叠加行业价格战压力和
    AI 成本转嫁客户趋势，OpenAI 面临激烈的市场份额争夺
  ethical: ChatGPT Work 连接 Slack、Gmail、Google Drive 和 CRM 等个人及企业工具，智能体自主操作带来的数据隐私泄露、权限越界访问和用户误操作风险显著上升
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

About two weeks after OpenAI’s GPT-5.6 was caught up in regulatory drama — rolled out only to government-approved organizations during a “limited preview” period — the company has received the Trump administration’s greenlight for a public rollout of the model. OpenAI CEO Sam Altman called it “the best model we have ever produced.”

# OpenAI rolls out GPT-5.6 after government greenlight — and announces ‘ChatGPT Work’

The limited preview period is officially over.

The limited preview period is officially over.

To celebrate, OpenAI also unveiled a new AI agent on the same day: ChatGPT Work. It’s billed as a combination of ChatGPT and Codex, allowing the everyday non-technical user to take advantage of Codex’s capabilities for non-coding tasks, and it’s powered by the GPT-5.6 model suite (Sol, Terra, and Luna). “It can gather context from the apps, files, and workflows you choose and create finished materials such as documents, spreadsheets, presentations, and web apps,” OpenAI wrote in a blog post, adding that a “unified plugins directory” allows ChatGPT to connect to tools like Slack, Gmail, Google Drive, calendars, and CRMs.

Mac and Windows users worldwide, including free ChatGPT users, should have immediate access to ChatGPT Work and GPT-5.6 via the ChatGPT desktop app. On mobile and the web, Pro, Enterprise, and Edu users will first get access, while Plus and Business users will receive access “over the next few days,” OpenAI wrote, adding that the “rollout is starting globally and will continue gradually toward full availability over the next 24 hours.”

Companies like OpenAI and Anthropic, as well as tech giants like Google (and even, recently, Apple), have been vying to clear new ground in the race to make AI agents actually useful for the average person, especially in the wake of the viral open-source AI agent OpenClaw. They’ve had varying results, and for now, the theoretical right-hand AI agent for the everyday consumer remains out of reach.

OpenAI is hoping that its new product, which is a direct competitor to Anthropic’s Claude Cowork (combining its own Claude and Claude Code), will push it ahead in the race.

OpenAI is especially banking on Sol, the most powerful of the GPT-5.6 model suite, to set “a new standard for intelligence and efficiency,” particularly when it comes to coding, cybersecurity, and science, as well as computer use capabilities. The company is also marketing the model as a lower-cost alternative to competitors’ most powerful models, amid complaints of an industry-wide money squeeze and AI lab costs being passed onto customers.

**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.