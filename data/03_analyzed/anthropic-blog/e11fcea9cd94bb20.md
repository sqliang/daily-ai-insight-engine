---
title: Claude Fable 5 Mythos 5
source: https://www.anthropic.com/news/claude-fable-5-mythos-5
author: []
published: '2026-06-09'
created: '2026-06-10'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e11fcea9cd94bb20
source_type: tech_blog
tldr: Anthropic 发布 Claude Fable 5（面向通用用户的旗舰模型）和 Claude Mythos 5（面向网络安全防御者的增强版本），定价为输入每百万
  token 10 美元、输出每百万 token 50 美元，不到 Mythos Preview 的一半。
objective_summary: 2026 年 7 月 21 日，Anthropic 正式发布 Claude Fable 5 和 Claude Mythos 5
  两款模型。Fable 5 是面向公众开放的 Mythos 级模型，在软件工程、知识工作、视觉、科学研究等基准测试中达到最先进水平。为控制风险，Anthropic
  对 Fable 5 加入了安全护栏，对部分敏感查询会降级到 Claude Opus 4.8 回复，该机制在不到 5% 的会话中触发。Mythos 5 与 Fable
  5 使用相同底层模型，但移除了部分安全限制，通过 Project Glasswing 与美国政府合作部署，拥有全球最强的网络安全能力。两款模型定价均为输入每百万
  token 10 美元、输出每百万 token 50 美元，不到 Claude Mythos Preview 的一半。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Anthropic
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 发布了两款新模型：Claude Fable 5（面向公众的通用版本）和 Claude Mythos 5（面向网络安全防御者的增强版本）。
- Fable 5 在软件工程、知识工作、视觉和科学研究等几乎所有基准测试中均达到最先进水平，任务越长越复杂其领先优势越大。
- 为了安全发布，Anthropic 为 Fable 5 加入了安全护栏，对敏感查询会切换到 Claude Opus 4.8 回复，该机制平均在不到 5% 的会话中触发。
- Mythos 5 基于与 Fable 5 相同的底层模型，但移除了部分安全限制，通过 Project Glasswing 与美国政府合作部署。
- 两款模型的定价均为输入每百万 token 10 美元、输出每百万 token 50 美元，不到 Claude Mythos Preview 价格的一半。
- Anthropic 表示这些模型在网络安全防御和生命科学研究领域已展现出巨大潜力，包括保障关键软件安全和提出新科学假设。
extract_result: success
object_mentions:
- object_type: product
  name: Claude Fable 5
  canonical_name: Claude Fable 5
  url: https://www.anthropic.com/news/claude-fable-5-mythos-5
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布 Claude Fable 5，这是一款面向公众开放的 Mythos 级模型，在所有已测试的 AI 能力基准上均达到最先进水平。
  - Fable 5 在软件工程、知识工作、视觉和科学研究等多个领域表现卓越，任务越复杂其领先优势越大。
  - Fable 5 定价为输入每百万 token 10 美元、输出每百万 token 50 美元，不到 Claude Mythos Preview 价格的一半。
  article_id: e11fcea9cd94bb20
- object_type: product
  name: Claude Mythos 5
  canonical_name: Claude Mythos 5
  url: https://www.anthropic.com/news/claude-fable-5-mythos-5
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Claude Mythos 5 与 Fable 5 使用相同底层模型，但移除了部分安全限制，拥有全球最强的网络安全能力。
  - Mythos 5 通过 Project Glasswing 与美国政府合作部署，作为 Claude Mythos Preview 的升级版本。
  - Mythos 5 的定价与 Fable 5 相同，均为输入每百万 token 10 美元、输出每百万 token 50 美元。
  article_id: e11fcea9cd94bb20
- object_type: project
  name: Project Glasswing
  canonical_name: Project Glasswing
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Claude Mythos 5 通过 Project Glasswing 与美国政府合作部署，作为 Claude Mythos Preview 的升级版本。
  - Project Glasswing 中已使用模型帮助网络防御者保护关键软件，并在生命科学研究中提出新假设和加速新疗法开发。
  article_id: e11fcea9cd94bb20
impact_score:
  score: 7.0
  reason: Anthropic 发布的 Claude Fable 5 和 Mythos 5 是前沿模型领域的重要产品落地。Fable 5 在多项基准测试中达到
    SOTA，覆盖软件工程、知识工作、视觉、生命科学等关键领域，同时定价仅为 Mythos Preview 的一半（$10/$50 每百万 token），兼具能力跃升和价格下探的双重冲击力。Mythos
    5 通过 Project Glasswing 与美国政府合作部署，开创了 '安全版公开发售 + 无限制版政府专用' 的双轨发布模式，可能重塑 AI 公司与政府合作的标准范式。评分
    7.0：属于重要产品发布，显著改变局部竞争格局，但尚未达到 ChatGPT 发布或 Transformer 论文级别的范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: SOTA 能力叠加半价 API 定价，软件工程领域表现突出，但安全路由机制可能带来 <5% 的查询降级到 Opus 4.8 的体验不一致
hype_assessment:
  level: medium
  reason: 文章使用了 'state-of-the-art on nearly all tested benchmarks'、'strongest cybersecurity
    capabilities of any model' 等强力措辞，存在一定的产品发布包装。但 Anthropic 提供了具体的基准对比表、明确的定价数据和实际部署案例（Project
    Glasswing），核心 claims 有实质支撑。'革命性' 等过度词汇未出现，整体属于合理的产品发布宣传范畴，非空洞炒作。
information_entropy: high
domain_disruption:
  technical_innovation: Fable 5 和 Mythos 5 共享同一个基础模型，通过安全路由层（敏感查询转至 Opus 4.8）实现了同一架构下的能力分级释放。这种
    '模型级安全门控' 设计替代了传统的 prompt-level 过滤，是 AI 安全架构的重要演进。模型在超长上下文和复杂自主任务完成上展现出代际提升，工程实现上属于可靠的前沿迭代。
  business_model: 开创了 '安全版（Fable）公开发售 + 无限制版（Mythos）政府专用' 的双轨商业模式。通过 Project Glasswing
    建立美国政府合作渠道，将模型能力直接嵌入国家级网络防御体系。同时以高出行业主流（GPT-4o/Claude 4）50-100% 的定价锚定高端市场，再用 '半价于上一代旗舰'
    的策略制造强烈性价比感知，形成清晰的价格阶梯。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Anthropic 此次发布的 Fable 5 和 Mythos 5 是典型的能力跃迁+价格下降的复利组合。一方面，Fable 5 在几乎所有基准测试中达
    SOTA，软件工程、生命科学等场景的能力积累具有强飞轮效应——用户越多、用例越复杂，模型优势越明显；另一方面，定价仅为 Mythos Preview 的一半（$10/$50
    per million tokens），说明推理成本正在快速下降，这进一步扩大了可寻址市场。Mythos 5 通过 Project Glasswing 与美国政府深度绑定网络防御场景，形成了一条不易复制的政府收入护城河。但需注意：目前安全护栏仍偏保守（<5%
    会话触发回退），若误报率未能快速降低可能影响企业采用率；此外，这是继 4.x 系列的增量跃迁而非范式革命，竞争格局仍可能被下一代架构（如推理时计算、MoE
    优化）重新洗牌。长期看，Anthropic 在安全对齐+政府合作上的差异化投入具有 3-5 年持续性，但评分不追顶分是因为价格战可能压缩利润率，且 OpenAI/Google
    的跟进速度不可忽视。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- US Cyber Command / 政府网络防御机构
- Project Glasswing 合作企业
- 生命科学研究机构（加速新药研发）
competitive_casualty:
- OpenAI（直接竞争 SOTA 基准 + 定价下压）
- Google DeepMind（Gemini 系列面临能力与价格双重对标）
- 中小型基础模型创业公司（能力差距拉大且价格战加剧）
- 传统网络安全 SaaS 厂商（AI 驱动的网络防御能力可能替代部分人力密集型业务）
market_opportunities:
- 软件工程自动化是当前最直接的落地场景——Fable 5 在 SWE-bench 等基准上领先，且定价降至 Mythos Preview 的一半，可大幅降低 AI
  辅助编码、自动化代码审查和测试生成的成本门槛，建议 SaaS 工具团队快速集成 Fable 5 API 推出增值服务
- 生命科学研究加速赛道存在结构性机会——Anthropic 明确指出模型在新假设提出和治疗开发方面有加速作用，AI 制药和科研辅助平台可基于 Fable 5 构建分子设计、文献挖掘和实验方案建议等垂直功能
- 网络防御即服务(NaaS)的政府/军工市场值得关注——Mythos 5 通过 Project Glasswing 与美国政府合作的模式可能扩展为可信访问计划，安全厂商可提前布局与此类政府合作项目的技术对接和合规认证
risk_matrix:
  regulatory: Mythos 5 移除安全限制用于网络防御，面临出口管制（ITAR/EAR）和 AI Act 高风险分类的合规压力；Fable 5 的保守安全审查机制（低于
    5% 误转 Opus 4.8）可能触发欧盟和英国监管机构对'安全审查透明度'的调查
  technological: Fable 5 的安全审查机制采用保守阈值，虽宣称平均触发率低于 5%，但在复杂长任务场景中误转概率可能更高，影响关键业务的连贯性；若竞争方（如
    OpenAI、Google）在同等价位推出能力相近的模型，Fable 5 的技术领先窗口期可能缩短至 3-6 个月
  competitive: Anthropic 将旗舰模型定价腰斩至 $10/$50 每百万 token，直接加剧了与 GPT-5、Gemini Ultra 等竞品的价格战；开源社区（如
    Llama、DeepSeek）若在类似能力上突破，将对闭源定价体系形成更大挤压
  ethical: 双轨模型策略（Fable 5 受限制 vs Mythos 5 无限制）引发 AI 安全治理的深层伦理争议——同一基础能力仅因部署方身份不同而施加不同安全约束，可能导致'安全歧视'争议；Mythos
    5 的网络防御能力若被滥用或泄露，可能造成大规模网络攻击工具平民化风险
  additional:
  - Anthropic 对 Fable 5 安全机制的'保守调优'表述模糊，未公开具体触发条件清单，存在信息不对称风险
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Claude Fable 5
  canonical_name: Claude Fable 5
  url: https://www.anthropic.com/news/claude-fable-5-mythos-5
  positioning: 面向公众开放的 Mythos 级旗舰模型，在软件工程、知识工作、视觉和科学研究等领域全面达到最先进水平。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 开发者与软件工程师
  - 知识工作者与研究人员
  - 科学研究者
  - 需要高级 AI 辅助的普通用户
  product_signal: 在所有已测试的 AI 能力基准上均达到最先进水平，任务越长越复杂其领先优势越大。
  market_signal: 定价为输入每百万 token 10 美元、输出每百万 token 50 美元，不到 Claude Mythos Preview 价格的一半。
  differentiation: 采用安全护栏机制对敏感查询自动降级到 Opus 4.8，在不到 5% 的会话中触发以平衡能力与安全。
  watch_reason: 作为 Anthropic 目前面向公众开放的最强模型，Fable 5 代表了可安全部署的顶级 AI 能力新标杆，其选择性降级安全策略和激进定价将深刻影响行业竞争格局。
  risk_notes:
  - 安全护栏存在误伤可能，无害请求也可能被拦截，平均低于 5% 的会话会触发降级。
  - 强网络安全能力在公开部署中仍存在被滥用的潜在风险，需持续观察实际使用情况。
  score: 9.0
  article_ids:
  - e11fcea9cd94bb20
  evidence_snippets:
  - Anthropic 发布 Claude Fable 5，这是一款面向公众开放的 Mythos 级模型，在所有已测试的 AI 能力基准上均达到最先进水平。
  - Fable 5 在软件工程、知识工作、视觉和科学研究等多个领域表现卓越，任务越复杂其领先优势越大。
  - Fable 5 定价为输入每百万 token 10 美元、输出每百万 token 50 美元，不到 Claude Mythos Preview 价格的一半。
- object_type: product
  name: Claude Mythos 5
  canonical_name: Claude Mythos 5
  url: https://www.anthropic.com/news/claude-fable-5-mythos-5
  positioning: 面向网络安全防御者的增强版本，与 Fable 5 共享底层模型但移除部分安全限制，通过 Project Glasswing 与美国政府合作部署。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 网络安全防御者
  - 关键基础设施提供商
  - 美国政府网络安全部门
  product_signal: 与 Fable 5 使用相同底层模型，移除部分安全限制，拥有全球最强的网络安全能力。
  market_signal: 定价与 Fable 5 相同，均为输入每百万 token 10 美元、输出每百万 token 50 美元，作为 Claude Mythos
    Preview 的升级版本。
  differentiation: 通过 Project Glasswing 与美国政府独家合作部署，同一模型不同安全策略服务于完全不同的使用场景。
  watch_reason: Mythos 5 代表了 AI 模型能力分层的典型实践，其 Trusted Access 扩展计划将影响行业关于 AI 安全与能力平衡的讨论方向。
  risk_notes:
  - 移除安全限制后若访问控制出现漏洞，可能带来严重的网络安全滥用风险。
  - 初期仅通过美国政府合作部署，公平性和广泛可用性存在不确定性。
  score: 8.0
  article_ids:
  - e11fcea9cd94bb20
  evidence_snippets:
  - Claude Mythos 5 与 Fable 5 使用相同底层模型，但移除了部分安全限制，拥有全球最强的网络安全能力。
  - Mythos 5 通过 Project Glasswing 与美国政府合作部署，作为 Claude Mythos Preview 的升级版本。
  - Mythos 5 的定价与 Fable 5 相同，均为输入每百万 token 10 美元、输出每百万 token 50 美元。
---

# Claude Fable 5 and Claude Mythos 5

Today we’re launching **Claude Fable 5**: a Mythos-class1 model that we’ve made safe for general use.

Fable 5’s capabilities exceed those of any model we’ve ever made generally available. It is state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, vision, scientific research, and many other areas. The longer and more complex the task, the larger Fable 5’s lead over our other models.

Releasing a model this capable comes with risks. Without safeguards, Fable 5’s capabilities in areas like cybersecurity could be misused to cause serious damage. We’ve therefore launched the model with safeguards that mean queries on some topics will instead receive a response from our next-most-capable model, Claude Opus 4.8. To release the model both safely and quickly, we’ve tuned these safeguards conservatively—they’ll sometimes catch harmless requests, though they trigger, on average, in less than 5% of sessions. With more capable models arriving in the coming months, we’re working to improve our safeguards and reduce false positives as quickly as we can.

For a small group of cyberdefenders and infrastructure providers, we’re also launching **Claude Mythos 5**. It’s the same underlying model as Fable 5, but with the safeguards lifted in some areas.2 Mythos 5 will initially be deployed through Project Glasswing, in collaboration with the US government, as an upgrade to Claude Mythos Preview. It has the strongest cybersecurity capabilities of any model in the world. Soon, we intend to expand access to Mythos 5 through a broader trusted access program.

The capabilities of models like Fable 5 and Mythos 5 have the potential to do profound good for the world. We’ve seen the beginnings of this in Project Glasswing, where the models have helped cyber defenders secure critically important software. We’ve also seen it in life sciences research, where the models are positing novel hypotheses and speeding up the development of new therapeutics.

Fable 5 and Mythos 5 are being offered at $10 per million input tokens and $50 per million output tokens—less than half the price of Claude Mythos Preview. Today’s joint launch is another step towards our goal of bringing advanced AI capabilities to as many users as possible, as quickly and as safely as we can.

## Evaluating Claude Fable 5 and Claude Mythos 5

The table below compares the capabilities of Fable 5 and Mythos 5 to other leading models.


Fable 5 and Mythos 5 can work autonomously for longer than any previous Claude models. Below we discuss how these skills apply to software engineering, and cover the model’s improved capabilities in knowledge work, vision, memory, and life sciences research.