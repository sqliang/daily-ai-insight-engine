---
title: Patreon stops asking AI bots not to scrape — and starts blocking them
source: https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/
author:
- '[[Sarah Perez]]'
published: '2026-07-17'
created: '2026-07-18'
manifest_dates:
- '2026-07-18'
- '2026-07-19'
description: Patreon is strengthening its defenses against AI scraping by working
  with Cloudflare to block bots that train AI models on creators’ content without
  permission. The move marks a shift away from relying on websites using robots.txt
  alone to actively block unauthorized AI training.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f4b489ce2fdadba0
source_type: news_media
tldr: Patreon 联合 Cloudflare 使用 AI Crawl Control 技术，从 robots.txt 劝阻转向主动拦截 AI 训练爬虫，测试显示拦截后AI爬虫的周访问量从数千次降至零。
objective_summary: Patreon 于 2026 年 7 月宣布与 Cloudflare 合作，升级其 AI 爬虫管控策略。此前 Patreon
  仅通过 robots.txt 文件请求 AI 爬虫不要抓取内容，但部分爬虫无视该请求。新方案采用 Cloudflare 的 AI Crawl Control 技术，主动拦截用于训练
  AI 模型的爬虫，而非仅靠请求约束。测试期间，个别 AI 训练爬虫的周访问尝试从数千次降为零。Patreon 表示仍允许索引类爬虫将用户引导回平台。Patreon
  产品负责人 Drew Rowny 在公告中强调创作者应有权决定其作品如何被 AI 使用。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Patreon
  - Cloudflare
  technologies:
  - AI Crawl Control
  - robots.txt
  - Pay Per Crawl
  key_people:
  - Drew Rowny
key_logic_flow:
- Patreon 于 2023 年首次部署措施劝阻 AI 爬虫抓取创作者内容，但 AI 爬虫技术日趋复杂，部分爬虫无视 robots.txt 的请求。
- Patreon 推出的新版发现工具（改版 Home Feed 和 Quips）可能将更多内容暴露给爬虫，促使公司采取更强的防护措施。
- Patreon 与 Cloudflare 合作，使用 AI Crawl Control 技术从被动劝阻转为主动拦截 AI 训练爬虫。
- 测试结果显示，拦截后个别 AI 训练爬虫的周访问尝试从数千次降至零。
- Patreon 明确允许索引类爬虫继续访问，前提是其目的是将用户引导回 Patreon 平台。
- Cloudflare 近期还推出了 Pay Per Crawl 市场，允许网站向 AI 爬虫收费，并更改策略默认拦截混合用途爬虫。
object_mentions:
- object_type: product
  name: AI Crawl Control
  canonical_name: Cloudflare AI Crawl Control
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Patreon 表示正在扩展与 Cloudflare 的现有合作，使用其 AI Crawl Control 技术来更新 AI 策略和执行工具。
  - 与之前仅通过 robots.txt 请求爬虫不要抓取不同，Patreon 现在主动拦截 AI 训练爬虫。
  article_id: f4b489ce2fdadba0
- object_type: product
  name: Pay Per Crawl
  canonical_name: Cloudflare Pay Per Crawl
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Cloudflare 提供了一个市场，允许网站向 AI 爬虫收费，名为 Pay Per Crawl。
  article_id: f4b489ce2fdadba0
- object_type: product
  name: Quips
  canonical_name: Patreon Quips
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Patreon 新推出了类似推文的 Quips 功能，可能将更多创作者内容暴露给爬虫。
  article_id: f4b489ce2fdadba0
extract_result: success
impact_score:
  score: 5.5
  reason: 该事件代表了 AI 训练数据获取从'君子协议'（robots.txt）向'强制执行'（主动拦截）的关键转变。Patreon 作为创作者经济的重要平台，其采用
    Cloudflare AI Crawl Control 为其他 UGC 平台提供了可参照的范本。测试数据（周访问量从数千降至零）证实了技术可行性。但该技术本身并非突破性创新（Cloudflare
    已有相关产品），且整体上属于行业防御性升级而非颠覆性变革。评分 5-6 分区间：改变了局部竞争格局（平台与 AI 爬虫的攻防态势从道德劝导升级为技术对抗），但远未达到范式转移级别。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: 主动拦截 AI 爬虫的技术有效性以及猫鼠游戏中的长期可持续性
hype_assessment:
  level: low
  reason: Patreon 和 Cloudflare 的公告没有使用'颠覆性''革命性'等 PR 套话。文章提供了具体的测试数据（周访问量从数千降至零），技术方案（AI
    Crawl Control）有清晰的技术实现路径。Cloudflare Pay Per Crawl 市场属于渐进式产品创新而非概念炒作。整体属于事实性产品更新报道，炒作成分低。
information_entropy: medium
domain_disruption:
  technical_innovation: Cloudflare AI Crawl Control 实现了从被动请求（robots.txt）到主动网络层拦截的架构升级，通过爬虫行为特征实时检测和分类，在不依赖爬虫自觉遵守的前提下阻断无视
    robots.txt 的 AI 训练爬虫。
  business_model: Pay Per Crawl 市场为内容平台提供了'完全禁止 vs 完全开放'之外的第三种商业化选择——向 AI 训练数据索取者收费，可能重塑
    AI 训练数据的获取成本结构和定价范式。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 该事件标志着 AI 训练数据获取从软约束（robots.txt）向基础设施层硬拦截的范式转变，具有长远复利潜力。Cloudflare 通过 AI
    Crawl Control 和 Pay Per Crawl 市场，正在构建'数据权利经济'的核心基础设施层——它不只是一个安全工具，而是 AI 公司与内容创作者之间的强制性收费站。核心投资逻辑：Patreon
    的采纳验证了 PMF，证明内容平台愿意为保护创作者数据付费；随着更多平台跟进，Cloudflare 的网络效应将指数级增强（每多一个采用方，AI 公司获取数据的摩擦就越大，Cloudflare
    的议价权就越强）。如果 Pay Per Crawl 成为行业标准定价模式，Cloudflare 将从边缘 CDN 服务商进化为 AI 产业链中不可或缺的数据准入层，类似
    AWS 在云计算中的角色。3-5 年后，控制高质量人类创作数据的访问权，将是 AI 军备竞赛中最稀缺的资源之一。
value_capture_layer: cloud_platform
moat_impact: creates_new_moat
key_beneficiaries:
- Cloudflare
- Patreon
- Substack
- Medium
- WordPress.com
competitive_casualty:
- 小型 AI 初创公司（无力支付数据授权费）
- 网页数据中间商（如 Common Crawl 依赖方）
- Akamai
- Fastly
market_opportunities:
- 内容创作者平台可将AI爬虫主动拦截（如Patreon与Cloudflare的合作模式）包装为差异化卖点，作为创作者权益保护功能吸引和留存优质创作者
- Cloudflare推出的Pay Per Crawl模式开创了内容授权交易新赛道，创业者可构建AI训练数据授权中介平台，帮助内容所有者与AI公司建立合规的定价和交易机制
- 针对AI公司的合规数据采集工具和服务存在机会，协助AI企业建立符合版权和道德标准的训练数据管道，规避日益增长的诉讼风险
risk_matrix:
  regulatory: AI训练数据使用的版权诉讼正在全球范围内升温（如纽约时报诉OpenAI案），Patreon主动拦截策略虽受CFAA保护，但可能面临爬虫方的反制法律挑战，且欧盟AI
    Act对训练数据处理提出了更严格的合规要求
  technological: AI爬虫技术正快速进化，部分高级爬虫已能模拟人类浏览行为绕过简单检测机制，Patreon和Cloudflare需要持续迭代AI Crawl
    Control算法以应对猫鼠博弈
  competitive: 如果主要UGC平台（如Medium、Substack、YouTube）纷纷效仿Patreon采用主动拦截策略，AI公司可能转向与平台达成独家数据付费协议形成新的竞争壁垒，中小平台若不跟进可能成为爬虫重灾区
  ethical: 该举措在保护创作者权益方面具有正面伦理意义，但可能导致AI训练数据进一步向已授权/付费的高质量数据源集中，加剧AI模型的知识代表偏差和可及性不平等
  additional:
  - 小型AI创业公司和学术研究机构获取训练数据的成本将进一步上升，可能加剧AI行业马太效应，巨头与初创之间的数据鸿沟持续扩大
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: AI Crawl Control
  canonical_name: Cloudflare AI Crawl Control
  url: null
  positioning: Cloudflare 提供的 AI 爬虫主动管控技术，从网络层面替代传统的 robots.txt 被动约束，帮助网站直接拦截 AI 训练爬虫，属于网站内容保护领域的重要技术产品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要保护创作者内容不被 AI 爬虫未经授权抓取的平台和网站
  product_signal: 该技术从网络层面主动拦截 AI 训练爬虫，不依赖爬虫自愿遵守 robots.txt，测试期间将个别爬虫的周访问尝试从数千次直接降为零。
  market_signal: Patreon 作为主流创作者平台率先采用该技术，体现了内容平台对 robots.txt 失效后主动式防护方案的强烈市场需求。
  differentiation: 与传统的 robots.txt 依赖爬虫自律截然不同，该技术通过 Cloudflare 网络层直接强制执行拦截策略，不依赖爬虫的合作意愿。
  watch_reason: AI Crawl Control 代表了内容平台应对 AI 爬虫从消极防御到主动拦截的关键技术演进；随着更多平台意识到 robots.txt
    的局限性，该技术可能成为行业标准防护方案，其市场拓展和技术迭代方向值得持续跟踪。
  risk_notes:
  - AI 公司可能开发出更复杂的爬虫技术以绕过 Cloudflare 的拦截机制，形成新的攻防对抗。
  - 该方案目前仅对使用 Cloudflare 网络的网站有效，覆盖范围受限于 Cloudflare 自身的市场渗透率，无法保护未使用其服务的平台。
  score: 8.0
  article_ids:
  - f4b489ce2fdadba0
  evidence_snippets:
  - Patreon 宣布扩展与 Cloudflare 的现有合作，使用其 AI Crawl Control 技术来更新 AI 爬虫管控策略，从仅靠 robots.txt
    文件被动劝阻转向在网络层面主动拦截 AI 训练爬虫。
  - 与之前仅通过 robots.txt 请求 AI 爬虫不要抓取不同，Patreon 现在使用 Cloudflare 技术主动拦截 AI 训练爬虫，测试期间个别爬虫的访问量从数千次降为零。
- object_type: product
  name: Pay Per Crawl
  canonical_name: Cloudflare Pay Per Crawl
  url: null
  positioning: Cloudflare 推出的允许网站向 AI 爬虫收费的市场化服务平台，将数据抓取从零和博弈转化为可商业化的交易机制，属于 AI 数据定价领域的新兴产品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 希望从 AI 数据抓取中获得收入补偿的内容平台和创作者
  product_signal: 该市场为 AI 公司提供合法获取训练数据的付费通道，将内容方在数据抓取中的被动损失转化为主动收入来源。
  market_signal: 在 AI 训练数据需求激增与版权争议加剧的行业背景下，该市场为数据所有权定价提供了新的商业化参考模式。
  differentiation: 与 AI Crawl Control 的拦截策略形成互补，Pay Per Crawl 采用商业化收费模式，为 AI 公司获取训练数据提供了合法合规的付费通道。
  watch_reason: Pay Per Crawl 探索了 AI 数据抓取问题的商业化解决方案，若成功可重构 AI 公司与内容平台之间的关系，将对抗转为交易机制，其定价模型与市场接受度值得持续跟踪观察。
  risk_notes:
  - AI 公司可能不愿为已可免费抓取的数据额外付费，该商业化模式的真实市场需求仍有待验证。
  - 该模式可能面临法律层面的挑战，数据所有权归属和定价权的法律界定目前尚不明确。
  score: 6.0
  article_ids:
  - f4b489ce2fdadba0
  evidence_snippets:
  - Cloudflare 推出了一个名为 Pay Per Crawl 的市场化平台，允许网站向 AI 训练爬虫收费，这为内容创作者提供了一种将数据抓取转化为收入来源的新选择。
- object_type: product
  name: Quips
  canonical_name: Patreon Quips
  url: null
  positioning: Patreon 平台推出的类推文短内容功能，让创作者发布碎片化短文并与受众互动，拓展了平台从纯付费墙向混合内容发现生态的战略转型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Patreon 平台创作者群体
  - 希望通过轻量短内容吸引新受众的内容创作者
  product_signal: Quips 作为 Patreon 内容发现策略的新组件，增加了创作者内容的曝光面和互动频次，但也因此带来了内容被 AI 爬虫抓取的附加风险。
  market_signal: Quips 反映了 Patreon 从纯付费墙模式走向混合内容发现模式的战略转型，以应对创作者平台日益激烈的竞争压力。
  differentiation: 与 Twitter/X 等完全公开的社交平台不同，Quips 在 Patreon 的付费围墙内运营，为创作者提供了半封闭式的短内容分发和粉丝互动渠道。
  watch_reason: Quips 作为 Patreon 内容发现转型的核心组件，其与付费墙的平衡策略以及由此引发的 AI 爬虫防护需求演变，反映了创作者平台在内容开放与数据安全之间的深层矛盾，值得持续关注。
  risk_notes:
  - 短内容模式可能稀释 Patreon 原本的深度内容社区定位，引发核心创作者的认同分歧和平台调性变化。
  - 内容曝光面的增加直接放大了 AI 爬虫抓取风险，Patreon 在内容发现增长与数据安全之间的平衡难度较大。
  score: 4.0
  article_ids:
  - f4b489ce2fdadba0
  evidence_snippets:
  - Patreon 新推出的类似推文的 Quips 功能，让创作者可以发布碎片化短文与受众互动，但也可能将更多创作者内容暴露给 AI 训练爬虫。
---

Patreon, the membership platform for creators, is cracking down on AI scraping its content for training purposes. On Thursday, the company shared that it’s working with internet infrastructure provider Cloudflare to directly block access to AI bots designed to train their AI models on creators’ work without permission.

The strengthened measures were necessary because AI scraping has become more sophisticated since it first put measures in place to deter AI crawlers in 2023, the company says. In addition, Patreon’s paywall has long locked much of creators’ content out of reach of crawlers. But more recently, the company introduced new discovery tools like a redesigned Home Feed and its tweet-like Quips, which could expose more content to crawlers.

The changes come about as more online publishers and content creators are coming to grips with how AI is ingesting their work for the purpose of making their AI models smarter. To combat this, Cloudflare now offers tools that allow website publishers to restrict AI bots, including a marketplace that lets websites charge AI bots for scraping, dubbed Pay Per Crawl. Earlier this month, it changed its policies so that “mixed-use” crawlers, meaning those that both index and train on a website’s content, are blocked by default on any pages that host ads.

Patreon says that it’s extending its existing work with Cloudflare to use the company’s AI Crawl Control technology to update its AI policies and enforcement tools. The difference here is that instead of simply asking AI crawlers not to scrape content using the robots.txt files — a standard way to provide bots with instructions on how they can use its site — Patreon is now actively blocking AI training bots.

“Consent shouldn’t depend on whether a scraper chooses to behave,” a Patreon blog post explains, referencing the stricter measures.

When testing the features, individual AI training crawlers’ weekly attempts to access Patreon went from “thousands of attempts to zero,” the post noted. That indicates that the AI scrapers were ignoring Patreon’s robots.txt file and scraping the site anyway, despite its requests.

However, the company said that it will allow bots that index pages and organize information that can be used to send users back to Patreon.

“As AI agents become increasingly powerful and popular, creators deserve a meaningful say in how their work is used by AI companies,” remarked Patreon’s product chief Drew Rowny in the announcement. “On most of the Internet, creators have to accept AI training on their work just to reach and grow an audience. Patreon has a different vision: creators should be able to grow their audience and control how their work is used.”