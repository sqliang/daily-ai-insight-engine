---
title: OpenAI launches a safer ChatGPT for teens — years after teens started using
  it
source: https://techcrunch.com/2026/08/18/openai-launches-a-safer-chatgpt-for-teens-years-after-teens-started-using-it/
author:
- '[[Sarah Perez]]'
published: '2026-08-18'
created: '2026-08-19'
manifest_dates:
- '2026-08-19'
description: ChatGPT for Teens adds age-appropriate safety measures, parental controls,
  and learning tools designed to steer teens away from harmful content — and from
  using AI to cheat on their homework.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 667df1e38fed1adf
source_type: news_media
tldr: OpenAI 于 2026 年 8 月 18 日发布面向青少年的 ChatGPT for Teens，新增 Study Mode 与默认安全防护，并宣布与
  CodeAI 合作开展 AI 教育，以回应多起青少年安全诉讼。
objective_summary: 2026 年 8 月 18 日，OpenAI 发布面向青少年的 ChatGPT for Teens，该产品新增 Study Mode、作弊检测提醒、测验与家长控制等教育功能，并默认开启基于
  Under-18 Principles 的年龄适配保护。OpenAI 同时宣布与 CodeAI 合作帮助青少年学习 AI，并继续为学校提供 ChatGPT for
  Teachers。文章指出这些安全措施的实际绕开难度尚未经过严格测试，并质疑此类保护为何未在 ChatGPT 上线之初内置。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - OpenAI
  - CodeAI
  technologies:
  - ChatGPT
  - Study Mode
  - Model Spec
  key_people: []
key_logic_flow:
- OpenAI 于周一发布面向青少年的 ChatGPT for Teens，背景是多起关于 AI 聊天机器人缺乏安全措施、导致青少年自杀等心理健康问题的诉讼。
- 新产品默认开启年龄适配保护，这些保护基于 OpenAI 的 Under-18 Principles，旨在减少青少年接触有害或不适合成长的内容。
- 教育层面新增 Study Mode，通过引导性问题和逐步支持帮助青少年理解学习材料，而非直接给出答案。
- 当系统检测到青少年试图作弊时，AI 会弹出作业提醒并引导其改用 Study Mode，同时支持测验、学习可视化与家长控制功能。
- 家长可通过先前推出的家庭工具和家长控制来管理设置、接收安全通知并设定 Quiet Hours。
- OpenAI 宣布与 CodeAI 合作教授青少年 AI 知识，并已在课堂提供 ChatGPT for Teachers，但文章质疑安全措施的实际有效性且追问为何保护未从一开始内置。
object_mentions:
- object_type: product
  name: ChatGPT for Teens
  canonical_name: ChatGPT for Teens
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 于周一发布面向青少年的 ChatGPT for Teens，承诺加入额外安全措施，以回应多起 AI 聊天机器人导致青少年自杀等心理健康问题的诉讼。
  - ChatGPT for Teens 将默认开启年龄适配保护，并新增 Study Mode、作弊检测提醒、测验与家长控制等教育功能。
  article_id: 667df1e38fed1adf
- object_type: product
  name: Study Mode
  canonical_name: Study Mode
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Study Mode 会向青少年提供引导性问题与逐步支持，帮助他们理解学习材料，而不是直接给出答案。
  - 当系统检测到青少年试图作弊时，会弹出作业提醒并引导其改用 Study Mode 来完成学习。
  article_id: 667df1e38fed1adf
- object_type: company
  name: CodeAI
  canonical_name: CodeAI
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 宣布与 CodeAI 建立合作，帮助青少年学习 AI 的工作原理、如何指导或质疑 AI 以及如何使用 AI。
  article_id: 667df1e38fed1adf
- object_type: product
  name: ChatGPT for Teachers
  canonical_name: ChatGPT for Teachers
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在课堂场景中，OpenAI 已提供 ChatGPT for Teachers，帮助学校以机构托管方式管理 AI 访问并提供教学支持。
  article_id: 667df1e38fed1adf
- object_type: product
  name: ChatGPT
  canonical_name: ChatGPT
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - ChatGPT 于 2022 年底推出，用户规模增长至每周 9 亿人之后，才加入专门针对青少年用户的防护措施。
  article_id: 667df1e38fed1adf
extract_result: success
impact_score:
  score: 4.5
  reason: 评分依据：这是 OpenAI 在青少年细分市场的一次「合规回应 + 教育功能扩展」型产品发布，而非技术范式转移。其行业话题性主要来自多起青少年安全诉讼带来的舆论压力，属于被动补课而非主动引领；功能本质是在现有
    ChatGPT 之上叠加年龄适配过滤、Study Mode 引导式问答与作弊检测，未改变大模型底层竞争格局。对照评估标准，它落在「重要产品发布、改变局部竞争格局」的范畴内，且考虑到谷歌等竞品早已推出针对未成年人的版本，OpenAI
    此举更多是补齐竞争短板，冲击力有限，故评 4.5 分。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 安全/反作弊机制的真实效力——青少年绕开防护的难度、作弊检测的误判率，以及为何这些保护未在 2022 年上线之初内置
hype_assessment:
  level: medium
  reason: 判定依据：本文认知论状态即为 pr_statement，OpenAI 以『developmental science and guidance
    from experts』等专家背书话术包装产品，但未提供任何可复现的测试数据或评测基准；TechCrunch 原文也明确质疑安全措施未经严格压力测试。虽未滥用『颠覆』『革命性』等词汇，但『safer』定位存在
    PR 包装成分——把本应默认具备的基础安全能力包装成新卖点。不过功能确有真实落地（Study Mode、家长控制、作弊提醒），并非纯概念炒作，故定为 medium。
information_entropy: medium
domain_disruption:
  technical_innovation: 在应用层落地了基于 Model Spec 中 Under-18 Principles 的年龄适配内容过滤，并通过「Study
    Mode 引导式提问替代直接给答案」的交互范式转变，配合作弊行为检测（意图分类器触发作业提醒）来约束模型输出行为。这是安全工程与产品交互设计的应用创新，属于意图分类与输出策略控制的产品化，不涉及模型架构、训练范式或推理效率的本质突破。
  business_model: 以『合规安全』为差异化卖点切入青少年教育 AI 市场，将家长/监护人（家长控制、安全通知、Quiet Hours）与学校（ChatGPT
    for Teachers 机构托管）双端转化为付费决策者，并通过 CodeAI 合作锁定 AI 通识教育入口，强化 OpenAI 在教育场景的订阅制生态壁垒。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 从资本视角看，这是一次防御性合规驱动的产品扩展，而非进攻性技术创新，故不给予高分。正面逻辑：K-12 AI 教育是长期确定性赛道，OpenAI
    凭借 900M 周活用户基盘、品牌信任与模型能力先发卡位，一旦家校生态（家长控制、学校托管管理、Study Mode 使用习惯）形成惯性，切换成本与教育场景数据飞轮将带来中等偏上的复利效应。反面逻辑：该产品本质是应对青少年安全诉讼的合规补丁，Study
    Mode/家长控制的技术壁垒不高，青少年绕过安全措施的顽疾未经验证，且教育市场强敌环伺（Google Gemini、可汗学院 Khanmigo 等），教育赛道商业化路径长、利润率偏低。综合判断，它有潜力成为
    K-12 AI 教育细分赛道的基础设施，但需持续验证安全有效性与商业化落地，故给 6 分而非更高。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- OpenAI
- CodeAI
competitive_casualty:
- Chegg
- 小型 AI 聊天机器人创业公司
- 传统课后辅导平台
market_opportunities:
- 面向 K-12 的 AI 素养教育存在明确空白，创业者可与学校及机构合作开发基于安全框架（如 Under-18 Principles）的 AI 教学课程、认证与评测工具，类比
  OpenAI 与 CodeAI 的合作模式
- 青少年 AI 安全与合规服务将成刚需，可切入 AI 产品的未成年人保护审计、年龄验证、家长控制 SaaS 以及'安全护栏有效性压力测试'这一细分赛道
- Study Mode 所代表的'引导式学习'交互范式（引导性问题、逐步提示、反作弊提醒、学习可视化）值得复刻到教育类 AI 产品中，作为区别于'直接给答案'的差异化功能
risk_matrix:
  regulatory: OpenAI 正因青少年心理健康诉讼承压，且各国监管同步收紧（美国 COPPA/FTC、欧盟 AI Act 对未成年人的特殊保护），任何面向青少年的
    AI 产品都可能触发年龄验证、未成年人数据保护与内容分级方面的合规审查，行业整体合规成本上升
  technological: 文章明确指出安全防护的实际有效性尚未经过严格压力测试，青少年普遍擅长绕过家长控制与内容限制，存在越狱（jailbreak）与提示注入绕过风险；年龄验证在技术上也难以可靠实现，防护体系可能形同虚设
  competitive: Google Gemini、Snapchat My AI、Character.AI 等对手已布局青少年与教育场景，Character.AI
    同样因青少年安全遭诉讼，合规压力与竞争并存；教育场景还面临 Khanmigo 等专用 EdTech 产品的直接竞争
  ethical: 核心伦理争议在于安全保护为何迟到多年——青少年已在无防护状态下使用 ChatGPT 数年；防作弊检测与家长控制可能引发隐私和监控担忧，与未成年人自主权存在张力；AI
    对青少年心理健康的潜在负面影响仍是诉讼与社会舆论的焦点
  additional:
  - 声誉风险：'为何不一开始内置保护'的质疑将长期伴随该产品，OpenAI 的信任修复比技术实现更难
  - 教育公平风险：依赖 AI 的引导式学习可能加剧有/无优质教育资源学生之间的数字鸿沟
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: ChatGPT for Teens
  canonical_name: ChatGPT for Teens
  url: null
  positioning: OpenAI 面向青少年用户推出的 ChatGPT 专用版本，默认开启年龄适配安全保护，并通过 Study Mode 等教育功能引导青少年以正确方式使用
    AI 学习。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 青少年学生
  - 家长与监护人
  - 学校与教育机构
  product_signal: 新增 Study Mode、作弊检测提醒、测验与学习可视化及家长控制，通过引导性问题帮助青少年理解学习材料而非直接给出答案。
  market_signal: 发布于多起针对 AI 聊天机器人导致青少年心理健康问题的诉讼背景之下，OpenAI 借此回应社会关切并拓展教育市场。
  differentiation: 与通用版 ChatGPT 相比，默认开启基于 Under-18 Principles 的年龄适配保护，并内置教育场景功能与家长控制，针对性更强。
  watch_reason: ChatGPT for Teens 是 OpenAI 在青少年安全诉讼压力下推出的年龄定向产品，其安全措施的实际有效性、学校采用率以及监管回应将直接影响
    AI 教育市场格局与行业安全标准走向。
  risk_notes:
  - 文章指出青少年擅长绕过家长控制等限制，新安全系统尚未经过严格压力测试，实际绕开难度未知。
  - 安全保护在 ChatGPT 上线多年后才默认内置，公众与监管可能质疑 OpenAI 的诚意并带来合规风险。
  score: 8.0
  article_ids:
  - 667df1e38fed1adf
  evidence_snippets:
  - OpenAI 于周一发布面向青少年的 ChatGPT for Teens，承诺加入额外安全措施，以回应多起 AI 聊天机器人导致青少年自杀等心理健康问题的诉讼。
  - ChatGPT for Teens 将默认开启年龄适配保护，并新增 Study Mode、作弊检测提醒、测验与家长控制等教育功能。
- object_type: product
  name: Study Mode
  canonical_name: Study Mode
  url: null
  positioning: ChatGPT for Teens 内置的教育学习模式，通过引导性问题与逐步支持帮助青少年理解学习材料，替代直接给出答案的学习方式。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 青少年学生
  - 家长与监护人
  product_signal: 当系统检测到青少年试图作弊时自动弹出作业提醒并引导切换至 Study Mode，同时支持测验与学习可视化，并可由家长控制默认启用状态。
  market_signal: 针对校园 AI 作弊这一教育危机设计，是 OpenAI 进入并巩固 AI 教育市场的关键差异化功能。
  differentiation: 与直接生成答案的通用 AI 助手不同，Study Mode 强调引导式提问与逐步支持，聚焦理解过程而非结果，旨在改变学生的 AI
    使用习惯。
  watch_reason: Study Mode 是 OpenAI 应对校园 AI 作弊问题、重塑学生 AI 使用习惯的核心功能，其教育效果与青少年实际接受度将决定
    ChatGPT 在教育场景的长期价值。
  risk_notes:
  - 文章指出青少年极擅长绕过此类系统，Study Mode 实际能否有效阻止作弊仍未经过严格验证。
  score: 7.0
  article_ids:
  - 667df1e38fed1adf
  evidence_snippets:
  - Study Mode 会向青少年提供引导性问题与逐步支持，帮助他们理解学习材料，而不是直接给出答案。
  - 当系统检测到青少年试图作弊时，会弹出作业提醒并引导其改用 Study Mode 来完成学习。
- object_type: product
  name: ChatGPT for Teachers
  canonical_name: ChatGPT for Teachers
  url: null
  positioning: OpenAI 面向学校课堂场景推出的教育产品，以机构托管方式管理 AI 访问，为学校提供受控的 AI 使用环境与教学支持。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 学校
  - 教师
  - 教育机构
  product_signal: 为学校提供机构托管的 AI 访问管理能力，与 ChatGPT for Teens 及 CodeAI 合作共同构成 OpenAI
    的教育产品矩阵。
  market_signal: 作为 OpenAI 教育产品线的一环，面向课堂与学校机构提供托管式访问，反映其持续拓展教育市场的布局。
  differentiation: 与面向个人用户的 ChatGPT 版本不同，ChatGPT for Teachers 侧重机构托管与集中管理，便于学校统一管控
    AI 在课堂中的使用。
  watch_reason: ChatGPT for Teachers 是 OpenAI 教育布局的机构侧入口，与 ChatGPT for Teens 形成互补，其在学校中的实际采用情况将反映
    AI 教育商业化落地的进程。
  risk_notes:
  - 该产品在文章中仅被顺带提及，详细功能与独立市场表现尚缺乏公开数据支撑。
  score: 5.0
  article_ids:
  - 667df1e38fed1adf
  evidence_snippets:
  - 在课堂场景中，OpenAI 已提供 ChatGPT for Teachers，帮助学校以机构托管方式管理 AI 访问并提供教学支持。
---

After numerous lawsuits over AI chatbots’ lack of safety measures, leading to teens’ suicides and other mental health concerns, OpenAI on Monday announced the launch of ChatGPT for Teens. The new product promises to include additional safety measures, as well as address the educational crisis of ChatGPT-assisted cheating in schools.

On the educational side, ChatGPT for Teens introduces a new Study Mode feature and other tools designed to encourage teen users to engage their curiosity and work through problems, not just get quick answers.

As OpenAI explains in a blog post, the Study Mode option will give teens guiding questions and step-by-step support to help them understand the material. Meanwhile, the teen experience will also include homework reminders that appear when a teen appears to be trying to cheat, instead of understanding the material. The AI chatbot will then push the teen to use Study Mode instead.

The app will also support quizzes and learning visualizations, and controls that allow parents or guardians to decide when Study Mode is enabled by default, the company says.

Still, it’s not clear how difficult it will be for teens to escape these new systems if they decide not to cooperate. Teens are incredibly adept at working around parental controls and other attempts to lock down digital experiences. Until ChatGPT’s teen mode can be put to more strenuous tests, it’s unclear how difficult it will be to work around these safety measures in reality.

There’s also the question as to why these protections weren’t part of ChatGPT from the beginning. The AI chatbot first arrived in late 2022 and scaled to 900 million weekly users before meaningful safeguards designed specifically for teenage users were added.

OpenAI says the age-appropriate protections will now be on by default in ChatGPT for Teens, which are designed to reduce exposure to harmful or developmentally inappropriate content. These measures are based on OpenAI’s Under-18 Principles in our Model Spec, which the company claims to be informed by “developmental science and guidance from experts.”

Parents will also be able to use the family tools and parental controls previously introduced to manage settings, receive safety notifications, and set Quiet Hours, among other things.

OpenAI announced a partnership with CodeAI to help teens learn more about AI, including how it works, how to direct it or question it, and how to use it. In the classroom, OpenAI already offers ChatGPT for Teachers to help provide schools with institution-managed access to AI and support.