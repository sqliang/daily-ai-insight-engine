---
title: Bring back crappy forums
source: https://tedium.co/2026/07/01/online-web-forums-retrospective/
author:
- '[[pentagrama]]'
published: '2026-07-02'
created: '2026-07-02'
description: 'Article URL: https://tedium.co/2026/07/01/online-web-forums-retrospective/
  Comments URL: https://news.ycombinator.com/item?id=48755731 Points: 252 # Comments:
  150'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 985dec6aa94dbbec
manifest_dates:
- '2026-07-02'
source_type: community_discussion
tldr: 本文回顾了网络论坛从 Usenet 到现代论坛软件的完整历史，认为老式论坛虽然技术粗糙但社区凝聚力远超今日社交媒体，并列举了 UBB、Slash、vBulletin、phpBB、Discourse
  等关键论坛平台及其历史影响。
objective_summary: Tedium 作者 Ernie 以自身在 Bluesky 积累 2 万粉丝却感到空洞为引，指出 2000 年代的论坛（如 Visual
  Editors）尽管技术简陋但社区体验远优于现代社交平台。文章追溯了论坛的源头——1970 年代末的 Usenet 和 1994 年 CERN 的 WWW Interactive
  Talk（WIT），梳理了从商业软件 WebCrossing（1995 年）到免费开源方案 WWWboard、UBB、Slash、vBulletin、phpBB，再到现代论坛
  Discourse 的演进脉络，并介绍了 BBCode 作为论坛专用标记语言的历史作用。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - CERN
  - NCSA
  - Lundeen & Associates
  - Salon
  - The New York Times
  - Social Strata
  - CrowdStack
  - Slashdot
  - SoylentNews
  - Discourse
  technologies:
  - Usenet
  - BBCode
  - Markdown
  - CGI
  - Perl
  - PHP
  - Ruby
  key_people:
  - Ernie
  - Eric Hunting
  - Ari Luotonen
  - Rob Malda
  - Jeff Atwood
  - Robin Ward
  - Sam Saffron
key_logic_flow:
- 作者认为现代社交媒体虽然吸引了大量关注但让人感到空洞，老式论坛尽管技术简陋却拥有更强的社区凝聚力。
- Usenet 作为 1970 年代末最早的论坛式系统，在 1990 年代末因缺乏图形界面而逐渐衰落。
- 1994 年 CERN 的 Ari Luotonen 开发了被认为是最早的 Web 论坛软件 WWW Interactive Talk（WIT）。
- 1995 年 Lundeen & Associates 推出商业论坛软件 WebCrossing，被《纽约时报》和 Salon 等主流媒体采用。
- Matt's Script Archive 的 WWWboard 作为免费的 Perl 论坛工具大幅降低了普通用户搭建论坛的门槛。
- Discourse 在 2014 年由 Jeff Atwood 等人创立，使用 Ruby 代码库重构论坛体验，延续了 Stack Exchange 的设计理念。
extract_result: success
object_mentions:
- object_type: project
  name: WWW Interactive Talk (WIT)
  canonical_name: WWW Interactive Talk
  url: https://github.com/
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 1994 年 6 月 CERN 的 Ari Luotonen 开发了被认为是最早的 Web 论坛软件 WWW Interactive Talk（WIT），作者将其上传到了
    GitHub 并使其能在 Docker 容器中运行。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: WebCrossing
  canonical_name: WebCrossing
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Lundeen & Associates 在 1995 年秋季发布了 WebCrossing 论坛工具，《纽约时报》和 Salon 等主要媒体在一年内将其投入使用。
  - Salon 使用 WebCrossing 作为数字社区核心超过 15 年，直到 2011 年才因顾虑发展方向而关闭。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: WWWboard
  canonical_name: WWWboard
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Matt's Script Archive 开发的 WWWboard 是免费的 Perl 论坛工具，虽然技术简陋且存在安全问题，但让普通用户也能搭建在线论坛。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: Ultimate Bulletin Board (UBB)
  canonical_name: Ultimate Bulletin Board
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - UBB（后称 UBB.classic）由 Social Strata 在 1996 年左右开发，凭借低成本价格在互联网上获得了广泛流行。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: Slash
  canonical_name: Slash
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Rob Malda 在 1998 年为管理 Slashdot 论坛开发了 Slash，其自我审核功能后来被 Hacker News、Digg 和 Reddit
    等平台借鉴。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: vBulletin
  canonical_name: vBulletin
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - vBulletin 是最知名的论坛平台之一，Something Awful 论坛使用了该软件但经过多年大幅修改和定制。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: phpBB
  canonical_name: phpBB
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - phpBB 始终是免费开源软件，因此聚集了大量开发扩展的社区，与之类似的 nodeBB 是其现代化版本。
  article_id: 985dec6aa94dbbec
- object_type: project
  name: Discourse
  canonical_name: Discourse
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Jeff Atwood、Robin Ward 和 Sam Saffron 在 2014 年创立 Discourse，采用 Ruby 代码库重构论坛软件，是
    Stack Exchange 理念的延续。
  article_id: 985dec6aa94dbbec
- object_type: product
  name: The Well (The Whole Earth 'Lectronic Link)
  canonical_name: The Well
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - The Well 始于 1985 年，是数字文化中持续运营时间最长的在线社区之一，成功从拨号 BBS 过渡到 Web 并至今作为付费私人社区活跃。
  article_id: 985dec6aa94dbbec
- object_type: product
  name: Visual Editors
  canonical_name: Visual Editors
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Visual Editors 是 2000 年代中期面向新闻设计师的论坛，虽然经常宕机但社区氛围极佳，被作者视为有史以来最喜欢的社交网络。
  article_id: 985dec6aa94dbbec
impact_score:
  score: 1.2
  reason: 该文章是一篇关于网络论坛历史的文化反思类文章，并非AI行业技术事件或产品发布。文章回顾了从Usenet、WIT、WebCrossing到Discourse的论坛软件发展史，反思现代社交媒体的空洞感，但未提出任何新技术、新产品或新范式，对AI行业短期竞争格局和方向无实质影响。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 网络论坛社区价值的回溯及其与现代社交媒体的对比反思，开发者可能对论坛软件历史细节感兴趣但无实际行动导向
hype_assessment:
  level: low
  reason: 文章是Tedium博主Ernie的怀旧反思文章，语调平实克制，没有使用'颠覆'、'革命性'等PR夸饰词汇。全文基于历史事实和个人经验叙述，属于严肃文化评论而非概念炒作。
information_entropy: medium
domain_disruption:
  technical_innovation: 无
  business_model: 无
engineering_complexity: conceptual
compound_value:
  score: 3.0
  reason: 本文是一篇回顾性的文化评论，而非具体的市场事件、产品发布或融资新闻。它反映的用户对算法社交媒体的倦怠情绪和对垂直社区平台的怀旧需求是真实存在的趋势，但已被市场认知（Discourse/Substack/Discord
    的崛起已部分印证）。作为单一文章，不具备改变竞争格局或触发投资轮动的影响力，且未涉及任何 AI 技术突破或商业信号。长期复利价值有限，主要作为情绪风向上的微弱佐证。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- Discourse
- Substack
- Discord
competitive_casualty:
- Twitter/X
- Bluesky
- Facebook
market_opportunities:
- 创业者可基于'反社交'理念打造非算法驱动的、有意限制规模的垂直社区平台，精准服务于特定职业或兴趣群体，如针对设计师、研究者等小众圈层的付费社区
- 面向企业或组织的论坛即服务产品可借鉴Discourse的成功经验，结合现代技术栈（Docker、Ruby）和去中心化架构，帮助品牌从社交平台回收用户关系并建立自有社区资产
- 个人或团队可探索复古网络文化的商业化路径，如基于BBCode/复古论坛UI的轻量协作工具、Usenet精华内容的整理与付费订阅服务
risk_matrix:
  regulatory: 运行在线论坛平台需承担内容审核义务，欧盟DSA等法规可能对中小论坛运营者构成合规成本压力；用户生成内容的版权侵权风险也需关注
  technological: 无
  competitive: 社交媒体巨头（Bluesky、X、Threads、Discord）已深度占据用户注意力和社交心智，网络效应极强，新论坛类产品获客成本高、冷启动难度大
  ethical: 论坛的匿名性可能助长网络暴力与恶意言论，但过度实名化又会抑制自由讨论，如何平衡匿名与问责是核心伦理挑战；文章提及的'点赞经济'导致空虚感反映了现代社交产品的心理健康隐忧
  additional:
  - 怀旧偏见风险——对早期论坛的正面记忆可能存在幸存者偏差，忽略了其垃圾信息、运营维护负担和低参与率的真实历史
confidence:
  impact: low
  compound: medium
  hype: low
actionable_insight: speculative_watch
object_insights:
- object_type: project
  name: WWW Interactive Talk (WIT)
  canonical_name: WWW Interactive Talk
  url: https://github.com/
  positioning: 1994 年由 CERN 开发的已知最早 Web 论坛软件，作为概念验证原型现已归档至 GitHub 并支持 Docker 运行。
  technical_signal: 基于 CGI 和 Perl 技术在短短数天内快速开发完成，代表了早期 Web 互动技术的探索性成果。
  adoption_signal: 未在 W3C 网站长期留存，实际使用周期很短，更多作为历史概念验证品存在。
  ecosystem_relevance: 作为 CERN 早期 Web 技术生态的组成部分，与万维网初期交互模式的演化史直接相关。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为已知最早的 Web 论坛软件，它的 GitHub 存档和 Docker 化尝试为早期 Web 互动技术提供了可复现的历史标本，值得关注其社区维护与数字遗产保存状态。
  risk_notes:
  - 该软件原本寿命很短，长期维护完全依赖社区兴趣驱动。
  - 作为 1994 年的快速原型，代码架构缺乏现代可扩展性标准。
  score: 3.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - 1994 年 6 月 CERN 的 Ari Luotonen 开发了被认为是最早的 Web 论坛软件 WWW Interactive Talk（WIT），作者将其上传到了
    GitHub 并使其能在 Docker 容器中运行。
- object_type: project
  name: WebCrossing
  canonical_name: WebCrossing
  url: null
  positioning: 1995 年发布的商业论坛软件，被《纽约时报》和 Salon 等主流媒体采用并持续开发超过 30 年。
  technical_signal: 作为早期商业论坛工具，其架构支撑了《纽约时报》1996 年总统选举报道的在线互动讨论功能。
  adoption_signal: 被 Salon 作为数字社区核心使用超过 15 年（1996-2011），证明了其企业级部署的稳定性和可靠性。
  ecosystem_relevance: 作为最早一批将 Web 论坛商业模式化的产品，对后续论坛软件生态的商业化路径产生了深远影响。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为持续开发超过 30 年的互联网原生软件工具，WebCrossing 的长期演变是观察 Web 论坛技术商业化与主流媒体社区运营变迁的独特窗口。
  risk_notes:
  - Salon 在 2011 年因认为其发展方向不合时宜而关闭社区，存在被时代淘汰的风险。
  - 在其他论坛平台广泛流行的背景下，WebCrossing 的市场存在感已大幅降低。
  score: 3.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - Lundeen & Associates 在 1995 年秋季发布了 WebCrossing 论坛工具，《纽约时报》和 Salon 等主要媒体在一年内将其投入使用。
  - Salon 使用 WebCrossing 作为数字社区核心超过 15 年，直到 2011 年才因顾虑发展方向而关闭。
- object_type: project
  name: WWWboard
  canonical_name: WWWboard
  url: null
  positioning: Matt's Script Archive 开发的免费 Perl 论坛工具，以技术简陋但零门槛的特点推动了 Web 论坛的民主化普及。
  technical_signal: 使用 Perl 语言编写，作为免费工具虽然存在安全漏洞但极大降低了普通用户搭建在线论坛的技术门槛。
  adoption_signal: 作为早期免费的论坛解决方案，被大量个人站长和小型社区采用，是当时最流行的自助建站工具之一。
  ecosystem_relevance: 与 Perl 开源生态紧密相关，代表了 1990 年代中后期 Perl 语言在 Web 论坛领域的广泛应用模式。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Web 论坛平民化的标志性项目，WWWboard 以零成本模式撬动海量用户的技术遗产和设计哲学至今仍对理解社区产品普及策略有参考意义。
  risk_notes:
  - 代码存在已知的安全问题，技术质量受到广泛批评。
  - 随着 Perl 在 Web 开发领域的地位下降，该项目已基本停止活跃维护。
  score: 2.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - Matt's Script Archive 开发的 WWWboard 是免费的 Perl 论坛工具，虽然技术简陋且存在安全问题，但让普通用户也能搭建在线论坛。
- object_type: project
  name: Ultimate Bulletin Board (UBB)
  canonical_name: Ultimate Bulletin Board
  url: null
  positioning: 1996 年由 Social Strata 开发的低价论坛软件，凭借性价比优势在互联网初期获得广泛流行。
  technical_signal: UBB.classic 版本代表了 Perl 论坛技术向商业化产品演进的重要方向，采用了当时成熟的 CGI 交互模式。
  adoption_signal: 凭借低成本定价策略吸引了大量中小型网站和兴趣社区，成为互联网早期最流行的论坛平台之一。
  ecosystem_relevance: 为后来的商业化论坛软件（如 vBulletin）铺平了市场道路，在论坛软件商业生态中占有承前启后的历史地位。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为早期互联网论坛文化的代表性软件，UBB 的商业化路径和社区运营模式对理解 2000 年代在线社区的增长策略有参考价值。
  risk_notes:
  - 随着免费开源论坛如 phpBB 的兴起，UBB 的市场份额被大幅挤压。
  - 商业化定价模式面临来自免费替代品的持续竞争压力。
  score: 2.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - UBB（后称 UBB.classic）由 Social Strata 在 1996 年左右开发，凭借低成本价格在互联网上获得了广泛流行。
- object_type: project
  name: Slash
  canonical_name: Slash
  url: null
  positioning: 1998 年为 Slashdot 论坛开发的软件，其自我审核机制深刻影响了后续社交新闻平台的用户治理模式。
  technical_signal: 创新性地实现了用户自我审核功能，该设计理念在架构层面为大规模内容治理提供了新的技术范式。
  adoption_signal: 作为 Slashdot 的驱动引擎在技术社区中获得极高采用率，服务于数百万技术从业者的日常讨论。
  ecosystem_relevance: 自我审核机制的设计影响了 Hacker News、Digg 和 Reddit 等平台的内容治理逻辑，在社交新闻生态中具有奠基性地位。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Slash 的自我审核模型是用户驱动内容治理的经典工程案例，对现代内容平台面临的审核与社区自治平衡问题依然具有借鉴价值。
  risk_notes:
  - 自我审核模式难以有效应对大规模恶意行为和高级水军攻击。
  - 项目自身的更新迭代速度较慢，技术栈与现代 Web 标准存在差距。
  score: 3.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - Rob Malda 在 1998 年为管理 Slashdot 论坛开发了 Slash，其自我审核功能后来被 Hacker News、Digg 和 Reddit
    等平台借鉴。
- object_type: project
  name: vBulletin
  canonical_name: vBulletin
  url: null
  positioning: 曾是最主流的商业论坛解决方案之一，以高度可定制性支撑了大量知名大型在线社区。
  technical_signal: 支持深度的功能定制和模板修改，如 Something Awful 论坛对其进行了多年的大规模改造以适应独特社区文化。
  adoption_signal: 在 2000 年代占据论坛软件市场的大部分份额，被海量商业网站和兴趣社区选为首选平台。
  ecosystem_relevance: 在论坛软件黄金时代占据核心位置，形成了庞大的插件和模板开发者生态，推动了 Web 社区技术的商业化繁荣。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为论坛软件黄金时代的代表性产品，vBulletin 的兴衰轨迹折射出 Web 社区平台从商业闭源向开源与现代 SaaS 演进的产业趋势。
  risk_notes:
  - 商业化授权模式在免费开源论坛的冲击下用户持续流失。
  - 面对 Discourse 等现代论坛软件的竞争，市场份额与社区活跃度均大幅下降。
  score: 2.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - vBulletin 是最知名的论坛平台之一，Something Awful 论坛使用了该软件但经过多年大幅修改和定制。
- object_type: project
  name: phpBB
  canonical_name: phpBB
  url: null
  positioning: 始终免费开源的老牌论坛软件，凭借活跃的扩展开发社区成为互联网上部署最广泛的论坛平台之一。
  technical_signal: 基于 PHP 语言开发并采用开源架构，允许全球开发者社区广泛参与功能贡献和扩展生态建设。
  adoption_signal: 因为完全免费开源，聚集了庞大的扩展开发者社区，被数以百万计的网站采用为默认论坛方案。
  ecosystem_relevance: 代表了开源论坛软件的中坚力量，其扩展生态对 Web 论坛的全球普及起到了关键推动作用，nodeBB 是其现代化继任者。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为长期活跃的开源论坛项目，phpBB 二十年来的社区治理模式与可持续维护策略是研究开源项目长寿秘诀的重要参考。
  risk_notes:
  - 传统论坛架构在面对社交网络和即时通讯工具的竞争中日渐式微。
  - 安全漏洞修复的及时性是长期开源项目面临的持续运营挑战。
  score: 3.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - phpBB 始终是免费开源软件，因此聚集了大量开发扩展的社区，与之类似的 nodeBB 是其现代化版本。
- object_type: project
  name: Discourse
  canonical_name: Discourse
  url: null
  positioning: 2014 年创立的现代开源论坛软件，基于 Ruby 技术栈重构论坛体验，已成为技术社区和开源项目的首选讨论平台。
  technical_signal: 使用 Ruby 代码库构建，延续了 Stack Exchange 的设计理念，实现了移动优先、实时交互的现代化论坛架构。
  adoption_signal: 在技术社区和开源项目中获得广泛采用，大量知名 AI 项目（如 Hugging Face）使用 Discourse 作为官方用户讨论平台。
  ecosystem_relevance: 作为当前最活跃的现代论坛框架，被 AI 和开源社区广泛选用，直接推动了论坛软件在社交媒体时代的复兴。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为当前最活跃的现代论坛平台，Discourse 的产品演进方向直接反映了在线社区软件的未来趋势，尤其对 AI 开发社区的基础设施选择具有指示意义。
  risk_notes:
  - 服务器资源消耗相比传统论坛软件更高，对小型自建站点的部署门槛较高。
  - 在 Discord 等即时通讯工具和社交媒体的双重挤压下，论坛形态本身面临用户习惯变迁的结构性挑战。
  score: 5.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - Jeff Atwood、Robin Ward 和 Sam Saffron 在 2014 年创立 Discourse，采用 Ruby 代码库重构论坛软件，是
    Stack Exchange 理念的延续。
- object_type: product
  name: The Well (The Whole Earth 'Lectronic Link)
  canonical_name: The Well
  url: null
  positioning: 始于 1985 年的数字社区先驱，成功从拨号 BBS 过渡到 Web，至今作为付费私人社区持续活跃运营。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 数字文化深度参与者
  - 偏好深度长文讨论的用户
  - 追求逃离算法社交媒体的高质量社群人士
  product_signal: 从拨号 BBS 到 Web 的成功技术迁移证明了产品架构的适应性和商业模式的可持续性。
  market_signal: 作为持续运营超过 40 年的在线社区产品，展示了超长生命周期数字产品的市场可行性与品牌忠诚度。
  differentiation: 区别于以广告和增长为核心的现代社交媒体，坚持付费会员制模式，以深度讨论而非流量扩张为运营核心。
  watch_reason: 作为数字文化史上运营时间最长的在线社区之一，The Well 的付费会员商业模式和社区自治策略对理解可持续社区产品的设计原则有不可替代的参考价值。
  risk_notes:
  - 付费私人社区的商业模式导致用户规模天然受限，增长空间狭窄。
  - 面对免费社交平台的激烈竞争，付费模式在争取年轻用户方面面临显著挑战。
  score: 4.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - The Well 始于 1985 年，是数字文化中持续运营时间最长的在线社区之一，成功从拨号 BBS 过渡到 Web 并至今作为付费私人社区活跃。
- object_type: product
  name: Visual Editors
  canonical_name: Visual Editors
  url: null
  positioning: 2000 年代中期面向新闻设计师的垂直专业论坛，以技术不稳定但社区凝聚力极强而著称。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 新闻行业排版与设计从业者
  - 深夜等待版面校对的设计师群体
  product_signal: 虽然经常宕机，但凭借夜间校对讨论等特色功能形成了极强的用户粘性和行业专属归属感。
  market_signal: 作为垂直领域的专业社区证明了利基市场产品的生存空间，但因缺乏商业化扩张动力而规模有限。
  differentiation: 区别于泛化社交平台，通过极度垂直的行业定位和深夜协作文化建立起技术简陋但情感连接极深的独特社区身份。
  watch_reason: 被作者誉为"有史以来最喜欢的社交网络"，Visual Editors 的案例锋利地揭示了垂直专业社区的魔力来源——深度归属感远超技术完美度，对理解社区产品设计有深刻启示。
  risk_notes:
  - 技术稳定性差，频繁宕机严重影响用户体验。
  - 高度依赖少数核心成员的参与驱动，一旦核心兴趣转移社区将难以维系。
  score: 3.0
  article_ids:
  - 985dec6aa94dbbec
  evidence_snippets:
  - Visual Editors 是 2000 年代中期面向新闻设计师的论坛，虽然经常宕机但社区氛围极佳，被作者视为有史以来最喜欢的社交网络。
---

**Today in Tedium:**Recently, I passed 20,000 followers on Bluesky, which I didn’t really say anything about. Sure, I thought about it, but then I had decided to myself, what’s the point? Soon, there will be another mark I can point to and feel weird about. The thing about social media these days is that the good stuff all too often pulls you in, but at the end of the day, you end up feeling hollow. Perhaps it’s for this reason that, when I spotted a thread asking about what my favorite social network of all time was, my answer wasn’t Twitter or Bluesky or even Tumblr. It was, of all things, a forum for news designers that existed in the mid-2000s called Visual Editors. It barely worked, honestly: It had a chat option that was popular with designers waiting for their pages to get proofed late in the evening, but it would often go down with no warning. But from a community standpoint, it was spectacular. Why don’t many modern social networks feel like that? Today’s Tedium ponders the fate of the web forum.

*— Ernie @ Tedium*

### 110k

**The number of newsgroups** that many modern Usenet providers, including GigaNews and SuperNews, promote as being available on their services. The Usenet system, with roots in the late 1970s, was the first forum-like system many early internet users relied on, with the other primary option being email listservs. But by the late 1990s, the not-particularly-graphical Usenet was already falling out of favor.

### Why the Web eventually moved in the direction of forums

**If you think about it,** the web forum was a terrible fit for the way the Web worked. We already technically had a tool that allowed people to communicate with one another in a forum setting in the early ’90s—Usenet.

Or, at least, that’s what it seemed like. So I wondered, well, what did people think about the growth of web forums on Usenet? And that led me in the direction of a fascinating post from modern-day futurist Eric Hunting.

Posting on alt.hypertext in the thread “Forums in the Web,” in April 1994, Hunting more or less predicted what web forums would become in just a couple of years:

One of the things lacking in the environment of the Web is a means of using Web pages as a medium for conducting open discussions or forums as you have in USENET. The reason for this is probably that there is no means of packaging pages, along with all their associated graphics and multimedia data, like forum posts nor would it be practical to distribute such potentially huge amounts of data among forum servers as with USENET.


His post, which is a bit wordy, describes the concept of threads, URLs as organizing structures, and what might or might not work. Essentially, the addition of images and multimedia, a second-class citizen on a text-based forum like Usenet, would significantly reshape how people interacted on forums. One area where he was wrong, unfortunately, is a common one. He assumed that the lack of anonymity would lead people to behave a bit better online:

It’s one thing to toss out a hundred lines of spontaneous vindictiveness to the faceless USENET server, another thing to have to maintain that mass of nastiness for a specific period of time on one’s own computer. A Web Forum post wouldn’t be a message on a paper airplane tossed to the aether. It would be a billboard in your own home.


Welp, not so much. But Hunting wouldn’t have to wait long to see an implementation of a web forum in the wild. In June 1994, CERN’s Ari Luotonen developed what is believed to be the first Web-based forum software, WWW Interactive Talk (WIT).

“[Bear] in mind that this was put together in a big hurry in a few days

so forgive me if it doesn’t do yet all the things that it could do,” Luotonen wrote.

The software did not live for long, and no longer appears on the W3C website—a surprise because much of its early work has more or less stayed online. Not this, though—though a little Internet Archive Wayback-foo eventually helped me find where the archive file was hiding.

In hopes of kicking back off a trend in W3C-generated forums, I uploaded the software to GitHub. And for kicks, I got it to run in a Docker container.

(Want to try it yourself? I put it on the Web here. Watch out for falling spam.)

While the W3C was first, there are lots of examples of similar tools out there. For example, the Collaborative Cork Board (CoCoBoard) was developed at the University of Illinois’ National Center for Supercomputing Applications (NCSA), the same place that launched Mosaic into the world. That tool essentially turned email replies into forum threads.

It wasn’t long before this pie in the sky concept, once the experimental territory of early Web developers working in CGI and Perl, found interest with big businesses. These were promoted as one of many examples of groupware. Odds are, you probably did not get your first experience posting on a Web forum using an open-source tool, but a commercial one.

One of the first companies to successfully launch a web forum startup was Lundeen & Associates, which created the WebCrossing forum tool, which was announced in the fall of 1995. Within a year, a number of major publications, including the Minneapolis *Star-Tribune*, *The New York Times*, and *Salon*, had put the software to work—in the *Times*’ case, it was part of its 1996 election coverage. While later tools became better known, WebCrossing may be one of the few internet-native software tools to remain in active development for more than 30 years.

(A testament to its legacy: *Salon* used the software as the anchor of its digital community for more than 15 years, only shutting it down in 2011 out of concerns it wasn’t where the Web was going. With another 15 years of retrospect, can we argue that this was probably a bad move? Perhaps.)

But WebCrossing was far from alone. The website Perlwatch has a list of literally hundreds of different forum systems, some of which vary in levels of obscurity. The list, as far as I can tell, has not been updated in years, despite the site claiming otherwise. But it is an excellent historic document of what it was like looking for a bulletin board system in the late ’90s and early 2000s.

But even with all this competition, the most dominant player in ’90s forum software benefited from being the free option. Matt’s Script Archive, a collection of Perl-based website tools (including guestbooks and page counters), hit on something important with WWWboard.

That tool, a primitive forum technology that barely worked, nonetheless made threaded discussions accessible by normal people, even if it meant forums that extended well past the point of loadability and security issues that never get patched. (We wrote a whole thing about it last week in case you want to dive in more.)

We quickly surpassed the limited capabilities of WWWBoard. But the forum itself would eventually get left in the dust, too.

### Five key examples of web forum software that are essential to internet history

**Ultimate Bulletin Board.**This software, later known as UBB and UBB.classic, found broad popularity on the internet thanks in large part to its low cost. It was a significant step up from WWWboard, in a good way. The software was originally developed around 1996 by Social Strata, which exists today under the name CrowdStack. (That said, its history is a bit winding, so not every version may work the same.)**Slash.**Developed by Rob Malda in 1998 as a way to help manage the forums on his popular tech-news site Slashdot, Slash proved supremely influential as a community management tool. (A big part of the reason? It came with really strong self-moderation features that were later copied by platforms like Hacker News, Digg, and Reddit.) While it’s not totally clear if Slashdot itself still uses Slash today (Malda, for one, left years ago), the site SoylentNews is known to use a direct fork of it.**vBulletin.**This is one of the more recognizable forum platforms on the internet, in part because of its use on some very prominent forums. Notably, Something Awful’s infamous forums use vBulletin, but that’s only half the story there: The software was forked years ago, and has been heavily modified and customized by SA’s moderators and owners over the past two decades. At this point, it’s more theirs than vBulletin’s.**phpBB.**While vBulletin, which came out around the same time as phpBB, is a commercial tool, phpBB has always been free and open source, and as a result, has found a massive community of people willing to write extensions for it. The similar nodeBB is a modernization of the phpBB approach and mostly works the same.**Discourse.**While it’s not the only tool of its kind, the decision by Jeff Atwood, Robin Ward, and Sam Saffron to build a new type of forum software was a big deal in 2014. After all, it was a medium in severe need of reinvention. (The move to a Ruby codebase, for example, was an important shift at a time when many forums still ran on PHP or Perl.) It can be seen as a continuation of Stack Exchange, a popular platform for programmer discussions that Atwood co-founded in 2008.

### 1985

**The year that The Whole Earth ‘Lectronic Link,** also known as The Well, first got its start. It is one of the longest continuously running online communities in digital culture, and unlike most bulletin boards or online services of its kind, it successfully made the jump to the Web. It remains active today as a paid private community. (The Well actually sponsored Tedium a million moons ago, which I realize is a cool thing to be able to say.)

### Before there was Markdown, there was BBCode

One challenge that a lot of early forums had to navigate was the necessity of sanitizing the text that people posted in forums. People could post literally anything in a form, and it could break the site, encourage exploits, the whole bit.

(When you don’t sanitize, you run into issues like making it possible to put CSS on MySpace pages.)

But on the other hand, you still wanted your websites to have at least *some* style to them, in a controlled way, without a lot of extra junk. These days, a lot of platforms use Markdown to solve this problem, in part because of its ubiquity. But before that, people posting on forums needed alternative options that made room for fun if not for putting malware on your forum.

That led to the creation of BBCode in 1998, first starting with UBB, then spreading to other forum platforms like phpBB and vBulletin. (There is a BBCode dot org dedicated to this scripting language, but I refuse to link to it because it’s now a Web3 SEO play.) While it doesn’t get the modern level of attention Markdown does, it is both older and more capable than Markdown is, for better or worse.

A subset of HTML, it effectively replaced the `<`

or `>`

with `[`

and `]`

, and removed the ability to add a bunch of extra stuff that the HTML spec was capable of doing. Forum owners naturally appreciated this because it gave them a bit of control over what users could do on their platform. JavaScript might be off the table, but 300 point text? Suddenly possible. A library of common images? Absolutely, they were called image macros. And features that make the forum more usable? You bet.

This lingo would sometimes shape the community as a whole. Fans of Something Awful, for example, likely remember the forums had a number of image macros, most notably :10bux:, which displayed an image of a $10 bill, reflecting the forum’s infamous one-time entry fee. And on some forums, BBCode would end up getting used in experimental ways, helping to generate some early meme culture. In its own way, BBCode was what made forums more than just Usenet in HTML format.

The downside is that the security reasons were more pronounced in theory than in practice. A 2005 blog post by developer Chris Shiflett argued that the security reason for BBCode was a lot weaker than it seemed:

As regular readers of Security Corner know, input must always be filtered. When you’re allowing users to enter very complex data, creating a whitelist of acceptable characters can be very difficult. Because of this, many developers employ very weak filtering rules for such input and rely on the escaping performed by

`htmlentities()`

for protection.While

`htmlentities()`

can save you from poorly filtered data, relying on escaping alone is not ideal. Because an attacker can send any type of data, it’s equally unwise to rely on BBCode for protection—you can’t assume that the attackers will abide by your rules unless you enforce those rules in your programming logic.

But even if the security reasons didn’t matter so much, Shiflett conceded that it was good for users and may in some cases even be easier to remember than actual HTML. (Though on the other hand, one presumes BBCode did discourage some people from trying out forums entirely. Those were the people who eventually went to Facebook.)

A similar concept in content management systems associated with WordPress, the shortcode, became a popular technique for helping visually modify or organize content on a page. (Tedium uses shortcodes with Markdown.)

*More video games should be programmed with a little BBCode.*

But what may be the most interesting legacy for BBCode in the modern day might not even be forums. The game development tool Godot has adopted the scripting language for writing formatted text within its node-driven interface. Which, given Godot’s surge in popularity over the past few years, likely means that a lot of modern games you enjoy might be secretly taking advantage of a tool developed for forum software built in Perl roughly 30 years ago.

Guess we can indirectly blame Unity for helping give BBCode a second wind. What a story arc.

## “We’re shrinking the world. It used to be that just a few people saw your photo. Now many do. We helped people in Tunisia broadcast what was happening, and they could hear people around the world supporting them.”


**— Dick Costolo,** the former CEO of Twitter (in the pre-Elon days), discussing what made Twitter such a powerful tool. While this shrinking of our world might seem like a good thing (with the Arab Spring a go-to example at the time Costolo was leading the company), recent thinking has moved in a different direction. “There is something terribly wrong with social media,” psychologist Nigel Barber argued in 2024. “The problem is that they are run by an engagement algorithm that ignores the principles of successful communities.” The concept of content collapse likely also plays a role here. “The problem is not lack of context,” cultural anthropologist Michael Wesch wrote in 2009 about the then-new concept of YouTube. “It is context collapse: an infinite number of contexts collapsing upon one another into that single moment of recording.”

**Why did forums lose out to social media?** I think the short answer comes down to novelty. Much like Usenet a decade earlier, we were ready for something different, having seen the weaknesses of forums in the late 1990s and early 2000s. We were ready to let someone else handle the technology part.

Plus, there’s the issue of scale. In so many ways, having a forum run by someone in a community on shared hosting meant that you couldn’t have a community unless there was someone willing to take on that commitment. They were on the hook not just to pay for the hosting, but to spend a terrible night managing things when the server got full, hacked, or simply overheated because Slashdot linked one of your threads.

In many ways, the technical argument made it an easy target for Web 2.0. There’s a reason why Digg, Reddit, and StackOverflow are perhaps the best manifestations of that era of technology. They were purpose-built community platforms that modernized things just enough that people who were looking for something a little better than we were getting from the thing that your friend built.

We tried the forum thing. We wanted something else. Not necessarily because it was better, though sure, maybe it was. But because it was different.

I want to pose a question: Is it possible that online users just have nonstop shiny object syndrome, and even if forums worked correctly and did the job, users would still move onto something else because we’re never happy? I think the argument is pretty strongly yes.

That said, I do think that as the internet matures into something that is more furniture in our lives, perhaps some of us will slow down. Maybe we’ll log into a forum and realize what we actually wanted out of our online experience was never the ability to reach everyone, but to reach the small number of people that think kind of like us. Maybe the “collisions” that modern social networks create just make things worse, even if it means we don’t get the occasional ego boost of Patton Oswalt replying to our tweet or whatever.

There was charm to all that barely-working PHP and Perl code that I think we’re still trying to recapture a quarter-century later.

--

Find this one an interesting read? Share it with a pal!

And we just added a bunch of new items to the Tedium Shopping Network. Maybe you might see something there you don’t need. Check it out.