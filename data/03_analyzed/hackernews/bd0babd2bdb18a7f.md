---
title: Google Declaring War on the Web
source: https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/
author:
- '[[cdrnsf]]'
published: '2026-05-20'
created: '2026-05-21'
description: 'Article URL: https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/
  Comments URL: https://news.ycombinator.com/item?id=48214449 Points: 392 # Comments:
  265'
tags:
- clippings
extraction_status: success
id: bd0babd2bdb18a7f
source_type: community_discussion
tldr: 谷歌在IO主题演讲中宣布将搜索进一步推向AI直接生成答案的方向，减少对原始网页链接的依赖。批评者认为这本质上是在网络之上建立谷歌控制的抽象层，将创作者的作品降级为AI的免费原料，损害了参与式网络的根基。
objective_summary: 2026年5月20日，谷歌在IO主题演讲中宣布搜索将更加侧重AI直接生成答案（即AI Overviews模式），而非提供指向信息来源的链接。批评文章指出，这一做法将网站和创作者的作品视为LLM的免费训练原料，用谷歌控制的抽象层遮蔽了开放网络。作者认为这是一场针对参与式网络的革命，谷歌意图垄断信息访问渠道，并预测下一步将使用贬义标签（类似'暗网'）来污名化开放网络。
event_type: application_landing
epistemic_status: theoretical_claim
entities:
  companies:
  - Google
  technologies:
  - AI Overviews
  - LLM
  key_people:
  - Zuckerberg
key_logic_flow:
- 谷歌在IO主题演讲中宣布搜索将更倾向于AI直接生成答案，而非提供信息链接，延续了AI Overviews的范式。
- 批评者认为这本质是在网络之上建立谷歌控制的抽象层，将网站和创作者的作品降级为AI的免费原料。
- 作者将此举与扎克伯格失败的Metaverse类比，认为谷歌正在发起对参与式网络的新一轮攻击。
- 作者预测谷歌下一步将开发贬义标签来污名化开放网络，类似'暗网'一词的使用方式。
- 文章呼吁用户去谷歌化，寻找替代搜索引擎并停止使用Chrome浏览器。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: product
  name: AI Overviews
  canonical_name: Google AI Overviews
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌正在将搜索推向'直接给出答案'的方向，延续了AI Overviews（AI摘要）的范式，这些AI摘要在当前搜索中大约有10%的错误率。
  - 谷歌正在放弃提供信息链接的范式，转而通过LLM生成回复，将网页信息去语境化并隐藏在其控制的抽象层之下。
  article_id: bd0babd2bdb18a7f
- object_type: product
  name: Chrome
  canonical_name: Google Chrome
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 作者批评谷歌不仅通过搜索改变信息获取方式，还拥有浏览器垄断地位，加剧了对网络流量的控制。
  - 作者呼吁用户停止使用Chrome浏览器，作为去谷歌化行动的一部分。
  article_id: bd0babd2bdb18a7f
- object_type: product
  name: Google Search
  canonical_name: Google Search
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌在IO主题演讲中宣布搜索将更侧重于AI直接生成答案，这是对现有信息链接范式的重大转变。
  - 作者认为谷歌的目标是让信息访问完全由其合成文本挤出机控制，用户只能获得谷歌认为相关的内容。
  article_id: bd0babd2bdb18a7f
impact_score:
  score: 7.5
  reason: Google 搜索从「链接索引」范式向「AI 生成答案」的全面转型，影响全球数十亿用户的信息获取方式。这并非一次性的技术突破，而是对已有 AI
    Overviews 路线的激进深化——减少甚至取消来源链接，意味着搜索引擎的角色从「信息导航者」变为「信息替代者」。对于依赖搜索流量的内容创作者、新闻媒体、独立网站而言，这是生存威胁级别的战略冲击。同时，Chrome
    浏览器垄断 + 搜索垄断的双重锁定效应放大了这一事件的短期行业冲击力。扣分原因在于：AI Overviews 已存在一年多，此次 IO 更多是路线宣告而非全新产品发布，实际落地效果和用户接受度仍存变数。
sentiment: mixed
developer_sentiment:
  tone: skeptical
  primary_focus: Google 以 AI 生成答案替代来源链接后，内容创作者和独立网站的流量将被系统性截流，开放 Web 的参与式生态面临生存危机
hype_assessment:
  level: medium
  reason: Google 在 IO 大会上使用 'agentic'、'AI-native search' 等话术包装这一战略转型，将其塑造为技术进步而非商业模式重构。实际上核心动作是：用
    LLM 合成文本取代外部链接，将 Web 内容降格为免费训练数据。文章作者使用的 'war on the Web'、'revolution' 虽是批判性修辞，但指出了被
    PR 叙事掩盖的本质——这是一场由广告收入驱动的信息渠道垄断。存在包装成分，但并非空洞的概念炒作，因为 Google 确实已在生产环境中大规模部署 AI Overviews。
information_entropy: medium
domain_disruption:
  technical_innovation: Google 在开放 Web 之上构建一个由其完全控制的 LLM 驱动的信息抽象层——搜索不再返回链接引导用户访问原始内容，而是直接在搜索结果页合成答案。技术上涉及大规模
    RAG 管道、多源信息融合与去上下文化摘要生成，核心挑战在于归因机制缺失导致的事实准确性问题（当前 AI Overviews 约 10% 错误率）以及内容创作者无法获得流量回报的生态负反馈循环。
  business_model: 此举直接颠覆了以搜索流量为核心的 Web 内容经济模式。新闻媒体、博客、Wiki 等内容网站依赖 Google 搜索导流获取广告收入或订阅转化；当
    Google 将答案直接呈现在搜索结果中而不提供来源链接时，内容生产者的经济基础被抽空。长期看，这可能加速 Web 内容质量的下降（内容生产者失去激励），同时强化
    Google 的广告垄断地位——用户停留在 Google 控制的界面内，广告展示机会进一步集中。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: Google此举本质上是将搜索从「索引-分发」模式升级为「合成-垄断」模式，试图在开放Web之上建立由其完全控制的信息抽象层。从复利视角看：（1）用户锁定效应极强——一旦用户习惯AI直接答案而非点击链接，迁移成本急剧上升，形成「用越多越难离开」的正向飞轮；（2）数据飞轮加速——每一次用户交互都反过来训练和优化Gemini模型，模型越强用户越多，形成闭环；（3）商业变现升级——AI答案页面可以嵌入更精准的广告和交易闭环，ARPU有望数倍于传统搜索广告。但扣分因素同样明显：（a）监管风险——EU
    DMA和US反垄断诉讼可能强制要求开放接口或拆分业务；（b）准确性质疑——AI Overviews约10%的错误率在医疗、法律等关键领域可能引发信任危机和诉讼；（c）出版商集体反抗——News
    Corp、Axel Springer等内容巨头可能联合抵制Google爬取，切断免费训练数据。综上，这是一场高赔率但对执行和监管环境极度敏感的赌注，3-5年后大概率成为行业基石，但路径上布满地雷，因此给予7.5分而非8+。
value_capture_layer: end_application
moat_impact: strengthens_monopoly
key_beneficiaries:
- Google
- NVIDIA
- Microsoft
- OpenAI
competitive_casualty:
- 独立内容创作者与博客作者
- 中小型新闻出版商
- 传统SEO工具与服务商
- DuckDuckGo
- Mozilla Firefox
- 广告技术中间商
market_opportunities:
- 独立搜索引擎与AI溯源工具迎来结构性机会：创业者可开发保留来源链接、强调内容归属的AI搜索产品（如付费订阅制的Kagi模式），差异化竞争Google的封闭式答案引擎
- 内容创作者应加速构建脱离搜索引擎依赖的自有分发渠道：强化Newsletter订阅、RSS复兴、播客/视频等多模态直达受众策略，降低对Google搜索引流的单一依赖
- 企业级AI合规与内容版权追踪工具需求将显著增长：可围绕网站内容被AI模型「无偿吸收」问题，开发内容水印、爬虫声明检测、AI引用溯源审计等SaaS产品
risk_matrix:
  regulatory: 高度风险：欧盟《数字市场法案》(DMA) 已将Google搜索列为守门人服务，此次战略转向可能触发反垄断调查；AI Overviews生成内容涉及数据来源与AI
    Act透明度条款的合规争议；美国FTC在新一届政府下的反垄断态度亦值得关注
  technological: 中等风险：若Google全面减少来源链接，可能催生去中心化Web替代方案（如ActivityPub协议、分布式搜索索引）的加速发展；同时「大模型幻觉率约10%」的问题若未显著改善，AI搜索质量天花板将限制其替代传统搜索的速度
  competitive: 高度风险：Google此举可能引发Meta、Microsoft（Bing/Copilot）等追随式跟进，形成「封闭AI答案层」行业趋势；但同时也为Perplexity、You.com、DuckDuckGo等强调透明度的替代品创造差异化空间；Chrome浏览器垄断与搜索垄断的双重绑定效应进一步强化进入壁垒
  ethical: 高度风险：将全球Web内容降格为LLM训练的「无偿原材料」，本质上是对内容创作者的系统性剥削；AI Overviews约10%的错误率在医疗、法律等高利害领域可能造成实质性伤害；信息获取渠道垄断将加深数字威权与信息茧房效应；公众知情权与参与式Web文化遭受根本性侵蚀
  additional:
  - Web标准俘获风险：Google通过Chrome和搜索双重垄断持续主导W3C等标准组织，可能将封闭式AI搜索的技术范式嵌入下一代Web标准，使得开放Web在技术层面被边缘化
  - 话语权操控风险：作者预测Google等行业巨头将系统性地贬低传统Web（类比「暗网」污名化策略），塑造「AI中介层=安全Web」的公众认知，为封闭生态争取社会合法性
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: product
  name: AI Overviews
  canonical_name: Google AI Overviews
  url: null
  positioning: 谷歌AI Overviews是集成在谷歌搜索中的AI摘要功能，直接通过LLM生成答案而非提供网页链接，旨在建立谷歌控制的信息抽象层。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 谷歌搜索用户
  - 信息检索者
  product_signal: AI Overviews延续AI摘要范式，直接将网页信息去语境化后通过LLM生成合成回复，目前约有10%的错误率。
  market_signal: 谷歌在IO主题演讲中正式宣布搜索转向AI生成答案，标志着搜索引擎从信息索引向AI合成范式的重大转变。
  differentiation: 与提供信息链接的传统搜索不同，AI Overviews在用户和网页之间建立了谷歌完全控制的抽象层，用户无法直接访问原始信息来源。
  watch_reason: AI Overviews代表了谷歌搜索从信息索引向AI合成答案的根本转变，将深刻影响开放网络的流量生态、内容创作者的可见性以及用户的信息获取方式，值得持续跟踪其对整个网络生态的冲击与反制措施。
  risk_notes:
  - 目前AI Overviews约有10%的错误率，可能向用户系统性传播不准确信息，影响信息获取质量。
  - 该模式将内容创作者的作品降级为LLM的免费训练原料，损害了参与式网络的生态根基。
  score: 8.0
  article_ids:
  - bd0babd2bdb18a7f
  evidence_snippets:
  - 谷歌正在将搜索推向'直接给出答案'的方向，延续了AI Overviews（AI摘要）的范式，这些AI摘要在当前搜索中大约有10%的错误率。
  - 谷歌正在放弃提供信息链接的范式，转而通过LLM生成回复，将网页信息去语境化并隐藏在其控制的抽象层之下。
- object_type: product
  name: Chrome
  canonical_name: Google Chrome
  url: null
  positioning: 谷歌Chrome是Google推出的主流网页浏览器，拥有显著的市场垄断地位，是谷歌控制网络流量的重要入口。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 网络浏览器用户
  - 谷歌生态用户
  product_signal: Chrome作为浏览器拥有市场垄断地位，与Google Search协同强化了谷歌对网络流量的控制能力。
  market_signal: 文章作者呼吁用户停止使用Chrome浏览器作为去谷歌化行动的一部分，反映了市场对浏览器垄断的担忧。
  differentiation: null
  watch_reason: Chrome作为谷歌控制网络流量的核心入口，其市场垄断地位与Google Search的AI化转型形成协同效应，值得关注其对浏览器市场竞争格局和用户选择权的影响。
  risk_notes:
  - Chrome与Google Search的深度绑定可能使用户更难脱离谷歌生态系统，加剧信息访问的集中化。
  - 浏览器市场份额集中度使单一公司对网络标准的影响力过大，可能影响开放网络的技术走向。
  score: 5.0
  article_ids:
  - bd0babd2bdb18a7f
  evidence_snippets:
  - 作者批评谷歌不仅通过搜索改变信息获取方式，还拥有浏览器垄断地位，加剧了对网络流量的控制。
  - 作者呼吁用户停止使用Chrome浏览器，作为去谷歌化行动的一部分，以打破对搜索和浏览的双重垄断。
- object_type: product
  name: Google Search
  canonical_name: Google Search
  url: null
  positioning: 谷歌搜索是全球最大的搜索引擎，目前正从提供信息链接的范式转向AI直接生成答案，意图建立谷歌控制的网络信息访问抽象层。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 全球互联网用户
  - 信息搜索者
  product_signal: 谷歌搜索在IO主题演讲中宣布将更侧重于AI直接生成答案，这是对传统信息链接范式的重大转变。
  market_signal: 谷歌搜索的AI化转型标志着搜索引擎行业从信息索引到AI合成答案的范式切换，将重塑整个网络信息获取生态。
  differentiation: 与传统搜索返回链接列表不同，谷歌搜索的新方向通过LLM合成回复，在用户和网页之间建立完全由谷歌控制的抽象层。
  watch_reason: Google Search作为全球最大流量入口转向AI合成答案模式，将从根本上改变内容创作者的可见性、用户的信息获取方式以及开放网络的生存环境，这一转变的影响远超单一产品迭代，值得持续跟踪其对网络生态的深远冲击。
  risk_notes:
  - AI生成答案约有10%的错误率，可能系统性传播不准确信息，影响信息获取的可信度。
  - 该模式将网站和创作者的作品降级为LLM的免费训练原料，损害开放网络的内容创作生态。
  - 谷歌对信息访问的垄断控制可能导致网络标准的变形和开放性的丧失，形成封闭信息孤岛。
  score: 9.0
  article_ids:
  - bd0babd2bdb18a7f
  evidence_snippets:
  - 谷歌在IO主题演讲中宣布搜索将更侧重于AI直接生成答案，这是对现有信息链接范式的重大转变。
  - 作者认为谷歌的目标是让信息访问完全由其合成文本挤出机控制，用户只能获得谷歌认为相关的内容。
---

In Yesterday’s IO Keynote Google declared war on the remnants of the Web. (See longer description on their website.) TL;DR: They are pushing Search more into the “here’s your processed answer” direction that “AI Overviews” have established (you know, those AI snippets in current Search that are wrong about 10% of the time). So they are mostly giving up on the paradigm of providing links to information.

While they packaged it as a lot of “AI” talk and “agentic” and whatnot, what their whole approach of decontextualizing information, of taking away links to sources and instead producing some LLM generated response means is that they want to establish a new abstraction layer on the web. Where Zuckerberg with his Metaverse failed Google is starting the next attack: Your website, your work no longer matters. The web is being fully hidden behind a Google-controlled surface. And I am not even talking about their browser monopoly.

Your work, your writing or art do matter a bit still: As (unpaid) raw material for their synthetic text extruders. You get to work for free so Google can have tight control on the flow of information and make sure that the responses people get are in line with what they need them to be. But your work is no longer seen as an important cultural artifact you can share with others.

This is a literal *revolution* but one against the participatory web, *against us*: The goal is to take away the web and guide people into Google’s abstraction on top of it. An abstraction they control and moderate. It’s about monopolizing access to information. A true Metaverse unbound by open standards and your ability to build your own corner of the web according to your needs and desires. Which – given how strong Google’s influence is on web standards – will change the shape of the standards for the technological landscape we are building the web on.

The next step will be Google or other companies in that space developing and deploying a new derogatory term for the web marking it as unclean, unruly, dangerous, bad (similar to “the Dark Web”) and making their abstraction the “safe” web.

If you do care about the web, about people’s ability to participate in it as more than mere passive consumers, this needs to be taken seriously. De-googlifying your mental apparatus becomes more urgent today. Find other search engines, don’t use the Chrome browser. Or wake up in a slopified AOL kind of environment where your access to information is limited to what Google’s synthetic text extruders deem relevant.

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.