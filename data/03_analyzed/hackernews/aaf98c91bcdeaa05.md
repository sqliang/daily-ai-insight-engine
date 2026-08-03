---
title: Back to Kagi
source: https://blog.melashri.net/micro/back-to-kagi/
author:
- '[[speckx]]'
published: '2026-07-22'
created: '2026-07-23'
manifest_dates:
- '2026-07-23'
description: 'Article URL: https://blog.melashri.net/micro/back-to-kagi/ Comments
  URL: https://news.ycombinator.com/item?id=49006195 Points: 266 # Comments: 197'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: aaf98c91bcdeaa05
source_type: community_discussion
tldr: 作者在尝试 Google、DuckDuckGo、SearxNG、Brave Search 和 Qwant 数月后，因搜索质量和隐私问题重新订阅了 Kagi。
objective_summary: 博客作者 Mel Ashri 在 2026 年 7 月重新订阅了 Kagi 搜索引擎，此前他已使用 Kagi 多年并于数月前离开尝试其他替代品。作者测试了
  Google（结果质量糟糕且过度强调 AI/视频/图片）、自建 SearxNG 实例（速率限制和结果质量不佳）、DuckDuckGo、Brave Search
  和 Qwant，均未达到 Kagi 的搜索质量。Kagi 的隐私保护、搜索结果质量、摘要/翻译功能和 CSS 自定义是吸引作者回归的主要原因。
event_type: application_landing
epistemic_status: theoretical_claim
entities:
  companies:
  - Kagi
  - Google
  - DuckDuckGo
  - Brave Search
  - Qwant
  technologies:
  - SearxNG
  key_people: []
key_logic_flow:
- 作者在离开 Kagi 数月后重新订阅了该搜索引擎，此前自 2021 年起就是 Kagi 用户。
- 作者尝试了 Google 但认为结果质量糟糕，且 Google 过度聚焦 AI、视频和图片而非文本内容。
- 作者使用自建 SearxNG 实例作为主要替代方案，但受到速率限制和搜索结果质量不稳定的困扰。
- 作者还测试了 DuckDuckGo、Brave Search 和 Qwant，认为这些引擎均无法匹配 Kagi 的搜索结果质量和相关性。
- Kagi 的隐私保护承诺、搜索结果质量、摘要功能和翻译功能以及 CSS 自定义能力是作者回归的关键因素。
object_mentions:
- object_type: product
  name: Kagi
  canonical_name: Kagi
  url: https://kagi.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 作者重新订阅了 Kagi，并自 2021 年起就是其用户，一直赞赏其隐私保护理念和搜索质量。
  - 作者认为 Kagi 的搜索结果质量和相关性优于 Google、DuckDuckGo、Brave Search 和 Qwant。
  - Kagi 的摘要功能、翻译功能以及 CSS 自定义是作者在其他搜索引擎上无法复现的独特特性。
  article_id: aaf98c91bcdeaa05
- object_type: project
  name: SearxNG
  canonical_name: searxng/searxng
  url: https://github.com/searxng/searxng
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者大部分时间使用自己配置的 SearxNG 实例，移除了导致返回结果过慢的搜索引擎。
  - 作者认为 SearxNG 的搜索结果质量和持续的速率限制问题使其使用体验令人沮丧。
  article_id: aaf98c91bcdeaa05
- object_type: product
  name: DuckDuckGo
  canonical_name: DuckDuckGo
  url: https://duckduckgo.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者尝试了 DuckDuckGo 作为 Kagi 的替代品，但认为其无法匹配 Kagi 的结果质量和相关性。
  article_id: aaf98c91bcdeaa05
- object_type: product
  name: Brave Search
  canonical_name: Brave Search
  url: https://search.brave.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者尝试了 Brave Search 作为替代搜索引擎，但认为其无法达到 Kagi 的搜索质量水平。
  article_id: aaf98c91bcdeaa05
- object_type: product
  name: Qwant
  canonical_name: Qwant
  url: https://www.qwant.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者尝试了 Qwant 作为替代搜索引擎，但认为其无法匹配 Kagi 的搜索结果质量和相关性。
  article_id: aaf98c91bcdeaa05
extract_result: success
impact_score:
  score: 1.5
  reason: 这是一篇个人博客，记录了一位用户尝试多个搜索引擎后回归 Kagi 的主观体验。事件本身不涉及任何新技术发布、融资、产品更新或行业范式转变。虽然
    Kagi 作为隐私优先的搜索引擎在技术社区有一定口碑，但单一个体的使用体验不足以对搜索行业格局产生可衡量的冲击力。评分依据：纯个人叙事，无结构性行业影响。
sentiment: positive
developer_sentiment:
  tone: neutral
  primary_focus: Kagi 搜索结果质量与隐私保护能否支撑付费订阅模式
hype_assessment:
  level: low
  reason: 文章是作者个人的搜索引擎使用日记，没有任何 PR 话术或夸张宣传。作者诚实描述了尝试多个替代方案的过程和各自的缺点，没有使用'颠覆'、'革命性'等概念炒作词汇。判定依据：真实用户反馈，非商业推广，无包装痕迹。
information_entropy: low
domain_disruption:
  technical_innovation: 无。文章未提及任何技术架构或算法突破，只是用户体验层面的对比。
  business_model: 无。文章未涉及 Kagi 的商业模式分析或行业生态影响。
engineering_complexity: conceptual
compound_value:
  score: 4.5
  reason: 该事件虽仅为一个用户的个人体验反馈，但折射出三个具有长期投资价值的信号：1) 付费搜索引擎订阅模式（Kagi 模式）已形成产品-市场契合验证，用户愿意为高质量文本搜索结果持续付费，订阅制带来的复购率和高
    LTV 构成复利基础；2) 用户'无法回到 Google'的心态表明，Google 在 AI 转型中过度侧重图片/视频/AI概览而牺牲核心文本搜索体验，这正在打开一个高端付费搜索的细分市场缝隙；3)
    Kagi 的差异化能力（隐私、摘要/翻译、CSS 自定义）形成了用户粘性壁垒，离开后又回归的路径验证了其不可替代性。然而，该市场仍极为小众，Kagi 年营收估计在千万美元级别，相比
    Google 搜索广告数千亿美元规模微不足道；且 Perplexity/ChatGPT Search 等 AI 原生搜索正在从另一维度颠覆搜索范式，对 Kagi
    构成长期结构性威胁。综合评估：细分赛道有复利潜力，但需持续验证付费搜索的 TAM 扩张能力和面对 AI 搜索的防御力。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Kagi
competitive_casualty:
- Google
- DuckDuckGo
- Brave Search
market_opportunities:
- 针对注重搜索质量和隐私保护的技术用户群体，推出付费制、无广告且文本优先的搜索引擎可作为差异化的细分赛道切入
- 搜索引擎提供深度自定义能力（如CSS界面定制、摘要/翻译等增值功能）可成为付费用户的留存利器与溢价卖点
- Google过度推送AI摘要和视频/图片内容引发的用户疲劳，为强调简洁文本结果和用户控制权的搜索产品创造市场空白
risk_matrix:
  regulatory: 无
  technological: 小型付费搜索引擎的核心算法依赖有限的数据规模，在搜索结果质量和相关性上难以与Google等巨头的长期技术投入和用户数据积累相抗衡
  competitive: Google、DuckDuckGo、Brave等免费搜索引擎构成巨大的竞争压力；Kagi的付费订阅模式限制了用户规模天花板，在巨头免费策略挤压下市场份额难以突破
  ethical: 无直接伦理风险；Kagi的隐私保护定位反而符合伦理正向趋势，但需警惕付费搜索模式可能引发的数字公平性质疑
  additional: []
confidence:
  impact: low
  compound: low
  hype: low
actionable_insight: speculative_watch
object_insights:
- object_type: product
  name: Kagi
  canonical_name: Kagi
  url: https://kagi.com
  positioning: 付费隐私搜索引擎，以无广告追踪、高质量文本搜索结果以及摘要翻译和 CSS 自定义等独特功能为核心竞争力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 注重隐私保护的技术用户
  - 对搜索质量有高要求的深度搜索者
  - 厌倦主流搜索引擎过度推广 AI 和多媒体内容的用户
  product_signal: Kagi 的搜索结果质量和相关性获得用户高度评价，摘要翻译和 CSS 自定义功能在竞品中不可简单复现。
  market_signal: 用户经历 Google、DuckDuckGo、Brave Search 和 Qwant 等多轮尝试后仍回归 Kagi，体现其用户黏性和产品壁垒。
  differentiation: 以付费模式消除广告干扰，通过摘要翻译和 CSS 自定义等特色功能构建差异化体验，区别于主流免费搜索引擎。
  watch_reason: Kagi 在付费搜索引擎赛道中以搜索质量和隐私保护建立差异化壁垒，用户跨竞品尝试后仍回归，反映其产品不可替代性，值得持续跟踪用户增长和商业模式可持续性。
  risk_notes:
  - Kagi 为付费订阅模式，在免费搜索引擎主导的市场中面临用户获取和留存压力。
  - 作为独立搜索引擎，其索引覆盖范围和算法迭代速度可能落后于 Google 等巨头。
  score: 5.0
  article_ids:
  - aaf98c91bcdeaa05
  evidence_snippets:
  - 作者重新订阅了 Kagi，并自 2021 年起就是其用户，一直赞赏其隐私保护理念和搜索质量。
  - 作者认为 Kagi 的搜索结果质量和相关性优于 Google、DuckDuckGo、Brave Search 和 Qwant。
  - Kagi 的摘要功能、翻译功能以及 CSS 自定义是作者在其他搜索引擎上无法复现的独特特性。
- object_type: project
  name: SearxNG
  canonical_name: searxng/searxng
  url: https://github.com/searxng/searxng
  positioning: 开源元搜索引擎，允许用户自建搜索实例并从多个搜索引擎聚合结果，以隐私保护和去中心化为核心理念。
  technical_signal: SearxNG 的技术架构依赖上游搜索引擎 API，导致结果质量不稳定并受到速率限制问题的严重困扰。
  adoption_signal: 技术用户选择自建 SearxNG 实例作为主要搜索引擎，反映其在隐私意识和自主可控需求群体中的实际采用。
  ecosystem_relevance: 作为开源搜索生态的重要组成部分，SearxNG 提供去中心化搜索替代方案，但对上游 API 的依赖构成生态脆弱性。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: SearxNG 在开源搜索领域占据重要生态位，为注重隐私和自主控制的用户提供去中心化搜索方案，但搜索结果质量和速率限制问题持续存在，值得关注社区改进方向。
  risk_notes:
  - SearxNG 高度依赖上游搜索引擎 API，速率限制问题难以从项目层面根本解决。
  - 搜索结果质量参差不齐，在相关性和覆盖面方面与传统搜索引擎存在显著差距。
  score: 3.0
  article_ids:
  - aaf98c91bcdeaa05
  evidence_snippets:
  - 作者大部分时间使用自己配置的 SearxNG 实例，移除了导致返回结果过慢的搜索引擎。
  - 作者认为 SearxNG 的搜索结果质量不佳且持续的速率限制问题使其使用体验令人沮丧。
- object_type: product
  name: DuckDuckGo
  canonical_name: DuckDuckGo
  url: https://duckduckgo.com
  positioning: 注重隐私保护的通用搜索引擎，以无追踪浏览体验为主要卖点，服务对基础隐私保护有需求的广泛用户。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 注重基础隐私保护的搜索引擎用户
  - 不愿为搜索付费但反感广告追踪的普通网民
  product_signal: DuckDuckGo 的搜索结果质量和相关性被用户认为不及 Kagi，且缺乏摘要翻译等高级搜索功能。
  market_signal: null
  differentiation: 以隐私保护和简洁无追踪体验为核心差异化优势，但搜索质量和功能丰富度与付费竞品相比存在差距。
  watch_reason: DuckDuckGo 是隐私搜索领域用户量最大的产品之一，但本文用户反馈其在搜索质量和高级功能方面不及 Kagi，反映出隐私搜索引擎在核心搜索能力上的分化趋势。
  risk_notes:
  - DuckDuckGo 搜索深度和质量在技术用户场景下不足，可能影响高价值用户的留存。
  score: 2.0
  article_ids:
  - aaf98c91bcdeaa05
  evidence_snippets:
  - 作者尝试了 DuckDuckGo 作为 Kagi 的替代品，但认为其无法匹配 Kagi 的结果质量和相关性。
- object_type: product
  name: Brave Search
  canonical_name: Brave Search
  url: https://search.brave.com
  positioning: 拥有独立搜索引擎索引的隐私搜索产品，以搜索独立性区别于依赖第三方索引的同类竞品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 追求搜索独立性和隐私保护的技术用户
  - Brave 浏览器的生态用户
  product_signal: Brave Search 的搜索结果质量和相关性被用户认为无法达到 Kagi 的水平，在文本搜索场景下表现不足。
  market_signal: null
  differentiation: Brave Search 拥有独立搜索索引，区别于依赖 Bing 等第三方索引的隐私搜索产品，但搜索质量仍有待提升。
  watch_reason: Brave Search 凭借独立搜索引擎索引在隐私搜索领域构建了独特的技术壁垒，但本文用户反馈其搜索质量仍不及 Kagi，值得关注其索引规模和搜索能力的持续改进。
  risk_notes:
  - Brave Search 的独立索引覆盖范围有限，搜索结果的相关性和全面性尚待加强。
  score: 2.0
  article_ids:
  - aaf98c91bcdeaa05
  evidence_snippets:
  - 作者尝试了 Brave Search 作为替代搜索引擎，但认为其无法达到 Kagi 的搜索质量水平。
- object_type: product
  name: Qwant
  canonical_name: Qwant
  url: https://www.qwant.com
  positioning: 法国隐私搜索引擎，以数据本地化和遵守欧洲隐私法规为核心定位，面向欧洲市场的隐私意识用户。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 欧洲市场注重数据本地化的隐私意识用户
  - 偏好欧洲本土互联网服务的用户
  product_signal: Qwant 的搜索质量和相关性在用户对比中未能达到 Kagi 的标准，搜索能力有待进一步提升。
  market_signal: null
  differentiation: 以数据本地化和欧洲隐私合规为独特卖点，但搜索质量的不足制约了其市场竞争力。
  watch_reason: Qwant 作为欧洲隐私搜索引擎的代表，以数据本地化为差异化定位，但用户反馈其搜索质量尚无法与 Kagi 竞争，后续产品改进和市场份额变化值得关注。
  risk_notes:
  - Qwant 搜索结果质量难以满足技术用户的深度搜索需求，市场竞争力受限。
  - 用户基数较小可能影响其索引扩展和搜索算法的持续优化投入。
  score: 2.0
  article_ids:
  - aaf98c91bcdeaa05
  evidence_snippets:
  - 作者尝试了 Qwant 作为替代搜索引擎，但认为其无法匹配 Kagi 的搜索结果质量和相关性。
---

Yesterday I re-subscribed to Kagi after a couple of months of trying out other search engines. Before that, I was alternating between Google and DuckDuckGo. And then have been Kagi user since 2021. And I have always appreciated its privacy-focused approach and the quality of its search results. However as I said in previous post, I left it and then I needed to find an alternative. I tried a few, but none of them were as good as Kagi.

I even tried Google again, but it was a disaster. The results were terrible and the focus on things like AI, Videos and Images instead of the focusing on the text which is what I need in 99% of the cases.

Most of time I used my custom configured SearxNG instance which I removed most of the engines that would make it take too long to return results. But the quality of both the results and the constant problems with rate-limiting made it a frustrating experience.

I did try different search engines like DuckDuckGo, Brave Search, and Qwant, but none of them were able to match the quality and relevance of Kagi's results. I also missed Kagi summerize and translate features. And above all, my css custimization for Kagi was something I really liked and I missed it a lot and couldn't reproduce even with userscripts/userstyles on other search engines.

Now as I'm back to Kagi, I feel relieved and happy to have found my way back to a search engine that truly meets my needs. The experience of trying out other search engines has reinforced my appreciation for Kagi's unique features and its commitment to user privacy. I also came back because the quality of the results is much better than any other search engine I tried.

The well is aleady poisoned for me and I can't go back to Google or any other search engine that doesn't prioritize user privacy and quality results. And above all, doesn't try to shove AI, videos and images down my throat when I just want to look up some text.