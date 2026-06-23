---
title: In the Weights is your new AI-centric vanity search
source: https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/
author:
- '[[Anthony Ha]]'
published: '2026-06-20'
created: '2026-06-21'
description: So ... what's your In the Weights score?
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: abec0710ffac301a
source_type: news_media
tldr: In the Weights 推出AI虚荣搜索，衡量个人在LLM参数中的被记忆程度
objective_summary: 前OpenAI员工Thomas Dimson和Joey Flynn创建了In the Weights网站，通过向Grok、Gemini、GPT、Claude、Llama等多个AI模型提问来评估模型对个人的"记忆"强度，并给出分数和排行榜。该工具旨在反映LLM时代信息检索方式的变化。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - Global Illumination
  - TechCrunch
  technologies:
  - Grok
  - Gemini
  - GPT-5.4 Mini
  - Claude
  - Llama
  key_people:
  - Thomas Dimson
  - Joey Flynn
  - Macaulay Culkin
  - Luciano Pavarotti
  - Anthony Ha
key_logic_flow:
- Thomas Dimson和Joey Flynn创建了In the Weights网站，用于衡量个人是否被AI模型的训练参数所"记住"。
- 该工具同时查询Grok、Gemini、GPT-5.4 Mini、Claude、Llama等多个AI模型，通过聚类相似描述并分配强度分数来评估记忆程度。
- 结果显示哪些模型返回了哪些答案，并高亮显示模型可能产生的幻觉内容。
- Dimson表示，2026年Google虚荣搜索已不再合适，因为越来越多流量转向了LLM。
- Dimson和Flynn此前通过其设计公司Global Illumination被收购而加入OpenAI，离职后创建了这一项目。
impact_score:
  score: 3.5
  reason: 该项目是一个趣味性产品，通过同时查询多个LLM并聚类返回结果来评估个人在模型参数中的'记忆程度'。它敏锐地捕捉了AI时代信息检索从搜索引擎向LLM迁移的文化现象，也因前OpenAI员工的身份获得了媒体关注。但从行业冲击力来看，它只是一个技术Demo级别的创意项目——没有提出新的技术范式、没有改变模型训练或推理方式、也没有商业模式的创新。其影响力更多体现在文化/社会层面（引发公众对'AI如何记忆我们'的好奇），而非技术或商业层面的行业变革。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 评估方法的严谨性——'被模型记住'的量化定义和强度打分机制缺乏透明度，结果的可重复性存疑
hype_assessment:
  level: medium
  reason: 项目使用了'superhuman artificial intelligence'、'live forever in the super intelligence'等夸张表述，但创始人明确表示这是一个半开玩笑的创意项目（'a
    mild curiosity'），并非严肃的产品发布。存在一定程度的叙事包装，但属于有意识的自我调侃而非恶意炒作。文章本身也如实报道，没有过度渲染。
information_entropy: low
domain_disruption:
  technical_innovation: 无——本质上是多模型API调用的聚合展示加上文本聚类，没有技术突破或工程创新
  business_model: 无——目前是免费趣味工具，没有展示任何商业模式或收入路径
engineering_complexity: prototype
compound_value:
  score: 2.5
  reason: In the Weights 本质上是一个趣味性 vanity search 工具，缺乏网络效应、数据飞轮和明确的变现路径。创始团队（前 OpenAI
    员工 Thomas Dimson 和 Joey Flynn）有技术信用背书，但产品本身技术门槛极低——本质是对多个 LLM API 的封装调用，极易被复制。'被权重记住'这一概念虽有文化传播价值，但作为独立产品难以形成可持续的竞争壁垒和复利效应。其最大价值在于作为'LLM
    取代传统搜索成为信息入口'这一宏观趋势的具象化信号，而非自身能捕获显著的长期商业价值。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- OpenAI
- Anthropic
- Google DeepMind
- xAI
competitive_casualty:
- Google Search
- 传统搜索引擎
- Google Alerts
market_opportunities:
- 企业和个人可布局'AI品牌声誉管理'服务，帮助客户确保其在主流LLM中被准确、正面地提及，类似于SEO但针对LLM参数空间的全新赛道
- 创业者可基于类似方法开发LLM输出一致性审计工具，帮助企业批量检测模型对其品牌、产品和关键人物的输出是否存在幻觉或负面偏差
- 个人数字身份管理可延伸至AI领域，随着LLM成为信息检索入口，'AI可见度评分'可能成为个人品牌建设和职场竞争力的新KPI
risk_matrix:
  regulatory: 该工具批量查询多模型评估个人被'记住'的程度，涉及个人数据的自动化画像与评分，在GDPR和CCPA框架下可能构成未经同意的数据合规风险；若工具开放第三方查询（非本人），将触发更严重的数据主体权利争议
  technological: 评分方法缺乏学术验证和跨模型一致性保障，模型版本更新后结果可能剧烈变动；幻觉高亮功能本身基于不可靠的模型自判，可能产生二次误导
  competitive: Google等搜索引擎可能快速推出类似的'AI搜索结果可见度'原生功能；LinkedIn、Wikipedia等已验证身份平台可能推出'AI知识面认证'服务，挤压独立工具的生存空间
  ethical: 核心机制是对个人在AI参数空间中的'被记忆程度'进行量化评分，可能引发广泛的隐私焦虑和'被AI遗忘'的社会伦理争议；评分体系客观上加剧名人/公众人物与普通人的数字不平等
  additional: []
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
---

Anyone who’s Googled themselves recently knows that it doesn’t quite hit the way it used to. Sure, there’s everything going on with Google search itself, but there’s also an inescapable feeling that web search isn’t the canonical source of information that it used to be, with just as many people learning about who you and I might be from chatbots.

Thomas Dimson and Joey Flynn had a similar feeling, leading them to create In the Weights. The “weights” in question are the numerical parameters that shape an AI model’s training and output, so the website purports to measure how well “a model is able to recall someone without using tools like web search.”

“Being in the weights means your existence was deemed important in the process of creating superhuman artificial intelligence,” the website says.

To achieve this, In the Weights supposedly queries different models (including Grok, Gemini, multiple versions of GPT, Claude, and Llama, plus lesser known models) with a question similar to, “Who is <name>? Give up to 10 results, each with a short description and confidence.” It then “cluster[s] similar descriptions together and assign[s] a strength score.”

For example, this humble tech blogger received a strength score of 641, placing me in the top 6% of names. I was feeling pretty good until I saw that multiple TechCrunch colleagues scored even higher. And the leaderboard has been shifting as I write this post, with “Home Alone” star Macaulay Culkin currently in the top slot with a strength score of 988, neck-and-neck with opera singer Luciano Pavarotti.

The results also show which models returned which answers for a given name, and they highlight potential hallucinations — apparently GPT-5.4 Mini says that Anthony Ha is an “ambiguous name form that could refer to multiple people with the initials A.H.A.”

Asked why he built In the Weights, Dimson told TechCrunch via email that he and Flynn were looking to “get the creative juices flowing again” after leaving OpenAI (which they both joined through the acquisition of their design startup Global Illumination).

Dimson said he was thinking about how “Google vanity searches are the wrong objective in 2026 as more traffic moves to LLMs” and about the fact that “so many lives are encoded somehow in a bunch of floating point numbers inside the AI brain.” He also said the direction of the site was “sealed” by a tongue-in-cheek blog post riffing on AI weights and Terry Bisson’s classic short story “They’re Made Out of Meat.”

“Reception has been insane so far, we thought this would be a mild curiosity but it seems like it has struck a nerve of wanting to see if you live forever in the super intelligence (the comparison factor doesn’t hurt either!)” Dimson added.