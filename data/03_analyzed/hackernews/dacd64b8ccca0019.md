---
title: Our decision on Cursor following its acquisition by SpaceX
source: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
author:
- '[[meetpateltech]]'
published: '2026-08-29'
created: '2026-08-29'
manifest_dates:
- '2026-08-29'
description: 'Article URL: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
  Comments URL: https://news.ycombinator.com/item?id=49486172 Points: 504 # Comments:
  266'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dacd64b8ccca0019
source_type: community_discussion
tldr: OpenAI 官方宣布终止向被 SpaceX 收购的 Cursor 提供其模型，理由是马斯克旗下公司有违反合同与服务条款的前科；拟定 2026 年 11
  月 12 日关闭，期间不再提供包括 Astra 在内的未来模型，并为受影响开发者提供支持。
objective_summary: OpenAI 发布官方公告，宣布已通知 SpaceX 终止向其旗下 Cursor 提供 OpenAI 模型的合同，拟定关闭日期为
  2026 年 11 月 12 日。终止原因是 OpenAI 基于马斯克旗下公司（Twitter、xAI）先前违反合同与服务条款的历史，无法确信 SpaceX 会合规使用其技术。OpenAI
  选择在合同允许的最晚日期取消合作，此后不再向 Cursor 提供包括 Astra 在内的未来新模型，并承诺为受影响的开发者提供支持。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - SpaceX
  - Cursor
  - xAI
  - Twitter
  technologies:
  - Astra
  key_people:
  - Elon Musk
key_logic_flow:
- OpenAI 于今日通知 SpaceX，计划终止向 Cursor 提供 OpenAI 模型的合同，拟定关闭日期为 2026 年 11 月 12 日，并给出合同允许的最长通知期。
- 终止合作的直接原因是 OpenAI 无法确信 SpaceX 会遵守其服务条款，依据是马斯克旗下公司此前多次违反合同的历史。
- 马斯克在收购 Twitter（现已并入 SpaceX）后曾违反合同条款，并于今年早些时候在宣誓下承认 xAI（同样已并入 SpaceX）违反过 OpenAI 服务条款。
- OpenAI 与 Cursor 的定制协议允许在控制权变更后的有限时间窗口内取消合同，OpenAI 决定将取消日期推迟到合同允许的最晚时点。
- 随着 AI 能力增强，OpenAI 对其即将推出的模型 Astra 提出更高问责要求，决定在取消合同后不再向 Cursor 提供未来的新模型。
- OpenAI 与 Cursor 已合作近四年，表示尊重其团队与产品，并愿意为受影响的开发者提供支持。
object_mentions:
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 已通知 SpaceX，计划在 2026 年 11 月 12 日终止向 Cursor 提供 OpenAI 模型的合同，并给出合同允许的最长通知期。
  - OpenAI 表示与 Cursor 合作近四年，尊重其团队与产品，深知最受影响的是依赖 Cursor 中 OpenAI 模型的开发者，并愿提供额外支持。
  article_id: dacd64b8ccca0019
- object_type: model
  name: Astra
  canonical_name: Astra
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 指出随着 AI 能力进步，其即将推出的新模型 Astra 的使用必须符合自身服务条款，这也是决定不再向 Cursor 提供未来模型的原因之一。
  article_id: dacd64b8ccca0019
extract_result: success
impact_score:
  score: 7.5
  reason: 评分依据：这是主流模型厂商首次对头部 AI 编程工具实施模型停供，直接波及 Cursor 数百万开发者用户，并在'模型 API 合同 + 控制权变更'场景下确立可被援引的行业先例；短期将打开
    AI 编程工具竞争格局的重排窗口（Cursor 被迫向 Claude/自研模型路线倾斜，竞品获得获客机会），同时放大开发者对模型供应商集中化风险的担忧。但该事件不构成技术范式转移，且公告给出至
    2026 年 11 月的较长缓冲期，实际冲击被推迟，属于重要生态事件而非颠覆性事件，故落在 7 分区。评分：7.5
sentiment: mixed
developer_sentiment:
  tone: frustrated
  primary_focus: Cursor 用户被卷入商业冲突被迫迁移模型栈，暴露对单一模型供应商的深度依赖风险
hype_assessment:
  level: low
  reason: 全文为 OpenAI 官方事实性公告，未出现'颠覆/革命性'等 PR 滥用词汇；给出了具体的关停日期（2026-11-12）、合同条款依据（控制权变更后的取消窗口）、以及可核查的历史违约事实（Twitter
    违反合同、xAI 宣誓承认违反服务条款），声明具备可验证性，包装成分极低，故判定为低水分
information_entropy: high
domain_disruption:
  technical_innovation: 无直接技术突破。事件本质是模型分发治理层的商业决策，其背后的技术驱动力在于：前沿模型（Astra）能力增强后 OpenAI
    对使用合规问责的要求上升，以及对模型 API 接入渠道控制权的强化
  business_model: 重塑 AI 编程工具与模型供应商之间的议价结构：Cursor 在控制权变更后失去 OpenAI 模型供给，暴露下游工具对上游模型厂商的深度依赖；将倒逼
    Cursor 加速多模型化与自研模型布局，并为模型 API 合同中的'控制权变更取消条款'确立行业先例
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 第一步，事件本质是模型供应商首次以服务条款为由单方面切断头部应用的分发通道，确立了'模型访问权=战略武器'的新规则，属于结构性事件而非一次性新闻。第二步，从复利视角看，最持久的效应不在
    OpenAI 与 Cursor 的个案纠纷，而在于它向整个开发者生态发出'单一模型依赖即致命风险'的强信号——这会系统性加速多模型架构、开源模型与中立网关的采用，此类需求一旦形成便持续累积，且随
    AI 能力增强（如 Astra）而不断强化，具备复利特征。第三步，编码助手是当前 AI 应用端变现最快的赛道，Cursor 被迫迁移模型栈将重排该赛道的价值分布，替代模型商（Anthropic、xAI、Google）获得确定性增量需求，这一重排效应至少以季度计并伴随开发者迁徙而放大。第四步，扣分项：事件直接冲击面局限于特定公司与
    Musk-Altman 的个人对抗，OpenAI 自身短期损失分发渠道与 API 收入，复利主要靠'风险认知扩散'这一间接渠道实现，而非直接创造新的基础设施层。综合评分落在细分赛道结构性催化区间，给予
    7.0。
value_capture_layer: foundation_model
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- xAI
- Google DeepMind
- OpenRouter
- DeepSeek
competitive_casualty:
- Cursor
- OpenAI
- 单一模型绑定的 AI 编码工具
market_opportunities:
- AI 编程工具的多模型解耦与模型路由编排将成为刚需，可开发支持 Anthropic、Google、开源模型自由切换的中间层产品，帮助 Cursor 用户与 B
  端企业对冲单一模型依赖风险
- Cursor 用户迁移潮将利好替代编辑器生态（Windsurf、GitHub Copilot、开源 Fork 等），可围绕工作流导入、插件适配、提示词与规则迁移开发配套迁移工具与服务
- AI 模型供应合同的变更控制权尽调与供应商风险管理将催生企业级服务新赛道，可面向 CTO 与法务团队提供 AI 供应链风险评估、合同条款设计与合规咨询
risk_matrix:
  regulatory: 该事件可能引发反垄断审查：OpenAI 以合规为由切断对马斯克系渠道的模型供应，存在被质疑滥用市场支配地位的风险，可能成为美国 FTC/DOJ
    关注对象，并牵涉合同控制权变更条款的司法边界争议。
  technological: Cursor 断供后失去 OpenAI 前沿模型（含 Astra）使用权，存在能力代差风险，若替代模型在代码生成质量上无法对齐，其产品竞争力将下滑；OpenAI
    亦面临编程分发渠道收缩、生态渗透率下降的技术生态风险。
  competitive: AI 编程赛道格局将被改写：Anthropic 有望进一步巩固在 Cursor 中的主导地位，GitHub Copilot、Windsurf、Trae
    等将争夺迁移用户，xAI 也可能借机将自有模型导入 Cursor，形成对 OpenAI 的直接对抗与价格、能力竞争。
  ethical: 大量依赖 Cursor 的开发者与企业将被迫非自愿迁移，暴露 AI 供应链受企业高层个人争端影响的脆弱性；模型供应决策与治理问责绑定，可能加深公众对
    AI 技术武器化的担忧，并造成开发者社区信任损耗。
  additional:
  - AI 供应链集中度风险凸显：模型供应商在并购后行使取消权将越来越常见，企业技术栈选型需将供应商控制权变更条款纳入评估。
  - 马斯克与 OpenAI 之间的对抗可能进一步升级，引发 xAI 报复性措施或更广泛的技术生态分裂，放大行业不确定性。
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  positioning: Cursor 是 AI 原生代码编辑器，通过深度集成 OpenAI 等前沿模型提供智能编程辅助，是 AI 编程工具赛道的代表性产品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 开发者
  - 软件工程师
  - AI 编程工具使用者
  product_signal: Cursor 长期集成 OpenAI 模型作为核心能力，与 OpenAI 合作近四年，体现其产品对前沿大模型的高度依赖与深度耦合。
  market_signal: OpenAI 因 SpaceX 收购 Cursor 后终止合同并停止提供未来模型，反映模型供应方的合规约束正成为产品可用性的关键变量。
  differentiation: Cursor 以 AI 原生编辑体验见长，但模型供应高度集中于 OpenAI，面临供应商依赖风险，与多模型接入的竞品形成差异化。
  watch_reason: Cursor 被 SpaceX 收购后遭遇核心模型供应商 OpenAI 断供，其应对策略、替代模型接入方案以及开发者迁移情况，将直接影响
    AI 编程工具市场格局与商业模式演进。
  risk_notes:
  - 依赖 Cursor 中 OpenAI 模型的开发者可能在 2026 年 11 月后失去模型接入，面临服务中断与迁移成本。
  - 模型供应集中于单一供应商，供应链中断风险放大产品交付与体验的不确定性。
  - SpaceX 与 OpenAI 之间的合同纠纷可能持续发酵，未来双方合作与合规走向仍不明朗。
  score: 8.0
  article_ids:
  - dacd64b8ccca0019
  evidence_snippets:
  - OpenAI 已通知 SpaceX，计划在 2026 年 11 月 12 日终止向 Cursor 提供 OpenAI 模型的合同，并给出合同允许的最长通知期。
  - OpenAI 表示与 Cursor 合作近四年，尊重其团队与产品，深知最受影响的是依赖 Cursor 中 OpenAI 模型的开发者，并愿提供额外支持。
---

Today, we notified SpaceX that we intend to wind down our contract providing OpenAI models to Cursor, with a proposed shutoff date of November 12, 2026. To maximize the time that developers can retain access to our models through Cursor, we are giving the maximum notice provided by our contract. This decision was incredibly tough, as we care deeply about our models being broadly available for developers. We are making this choice because we cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts.

To work with a large partner like SpaceX, we typically rely on custom contracts to ensure compliance with our terms of service and that the integration provides for safety at scale. After Musk acquired Twitter, now part of SpaceX, the company __broke__(opens in a new window) the terms of our contract (alongside many others). Under oath earlier this year, Musk __admitted__(opens in a new window) that xAI, now also part of SpaceX, had violated OpenAI’s terms of service (terms which are similar to xAI’s own).

Our custom agreement with Cursor gives us a limited time window to cancel it after a change of control. As AI capabilities advance, we also have a new level of accountability to ensure our upcoming model, __Astra__, is being used in accordance with our terms. Given all of this, we’ve decided to hold the contract cancellation to the latest date we can while not providing future models to Cursor.

We’ve worked with Cursor for nearly four years and have enormous respect for their team, their product, and what they’ve built for the developer community. We know that the people most affected by this decision are the developers who rely on OpenAI models in Cursor. We care about their experience in this transition and we’re ready to go above and beyond to support them.