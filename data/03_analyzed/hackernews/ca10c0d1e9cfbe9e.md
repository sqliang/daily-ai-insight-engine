---
title: 'Retraction: The App Store Rejection of the Week That Was a Correct Rejection'
source: https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week
author:
- '[[minimaxir]]'
published: '2026-08-09'
created: '2026-08-09'
manifest_dates:
- '2026-08-09'
description: 'Thread for original post: https://news.ycombinator.com/item?id=49214863
  Comments URL: https://news.ycombinator.com/item?id=49228166 Points: 178 # Comments:
  17'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ca10c0d1e9cfbe9e
source_type: community_discussion
tldr: John Gruber 撤回其前一天发表的关于苹果错误拒绝天文应用 Dark Hours 的文章，承认被开发者 Terry Godier 误导。真相是
  Godier 提交的应用 Asterly 实为占星应用且含塔罗牌功能，苹果的拒绝是正确的。
objective_summary: '2026年8月8日，Daring Fireball 作者 John Gruber 全面撤回前一天发布的文章 App Store
  Rejection of the Week: Dark Hours，承认其前提完全错误。经核实，开发者 Terry Godier 最初提交给苹果 App Store
  的应用名为 Asterly，完全致力于占星术并含每日塔罗牌功能，因此苹果的拒绝与 App Review Board 的维持裁决均为正确。Godier 后将天文版本以
  Dark Hours 之名移植到网页 darkhours.io，因与 Miguel Beher 的开源项目 DarkHours 撞名且存在相同 bug，最终下线并重定向域名至
  Beher 的 darkhours.app。这是 Gruber 24 年写作生涯中首次撤回文章。'
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Apple
  - The Verge
  - Hacker News
  - Bluesky
  technologies:
  - RSS
  key_people:
  - John Gruber
  - Terry Godier
  - Miguel Beher
  - David Pierce
key_logic_flow:
- 'John Gruber 于前一天发表题为 App Store Rejection of the Week: Dark Hours 的文章，声称苹果错误拒绝了
  Terry Godier 的天文应用，但现已因前提完全错误而整体撤回。'
- 真相是 Godier 最初向 App Store 提交的应用名为 Asterly，完全致力于占星术并包含塔罗牌每日占卜功能，因此苹果的拒绝及 App Review
  Board 的维持裁决都是正确的。
- Godier 在博客更新中说明，App Store 审核人员表示从未收到过移除占星内容后的更新构建，应用重新提交应该没有问题。
- Godier 将天文版本移植到网页并以 Dark Hours 之名在 darkhours.io 上线，引发与 Miguel Beher 开源项目 DarkHours
  的撞名争议。
- Beher 指出 Godier 的 Dark Hours 存在与其项目相同的把用户路由到墨西哥随机地块的 bug，随后 Godier 下线应用并将域名重定向到
  Beher 的 darkhours.app。
- 这是 Gruber 24 年写作生涯中首次撤回文章，他向读者及 App Store 审核人员公开道歉，并承认自身偏信与把关失误。
object_mentions:
- object_type: product
  name: Dark Hours
  canonical_name: Dark Hours
  url: https://darkhours.io
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Godier 在应用被拒后把天文版本移植到网页，上周以 Dark Hours 之名在 darkhours.io 域名上线。
  - 在与 Miguel Beher 发生撞名争议后，Godier 将网页应用下线，并把 darkhours.io 域名重定向到 Beher 的 darkhours.app。
  article_id: ca10c0d1e9cfbe9e
- object_type: product
  name: Asterly
  canonical_name: Asterly
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Godier 于一月向 App Store 提交的占星应用名为 Asterly，完全致力于占星术并包含塔罗牌每日占卜功能。
  - Asterly 在四月被 App Review Board 维持拒绝裁决时仍沿用此名，苹果从未收到过名为 Dark Hours 的应用。
  article_id: ca10c0d1e9cfbe9e
- object_type: project
  name: mbeher2200/DarkHours
  canonical_name: DarkHours
  url: https://github.com/mbeher2200/DarkHours
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Miguel Beher 的开源项目 DarkHours 是一个天文摄影与暗空规划工具，源代码托管在 GitHub 上。
  - Beher 在 Bluesky 上指出 Godier 的 Dark Hours 与其项目存在把用户路由到墨西哥随机地块的相同 bug。
  article_id: ca10c0d1e9cfbe9e
- object_type: product
  name: Current
  canonical_name: Current
  url: https://www.terrygodier.com/current
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Godier 的 RSS 阅读器 Current 是他为践行交互式文章中的理念而制作的，被认为是名副其实的突破性产品。
  - The Verge 的 David Pierce 将 Current 列入让他不想换回 Android 的 iOS 独占应用短名单。
  article_id: ca10c0d1e9cfbe9e
extract_result: success
impact_score:
  score: 1.5
  reason: 该事件本质是 Daring Fireball 作者 Gruber 因被开发者误导而错误指责苹果审核、随后公开撤回的媒体纠错事件，核心是 App
    Store 审核透明度与开发者诚信问题，不涉及任何 AI 技术进展或行业格局变化。对 AI 行业的短期冲击力极低，仅在 iOS 独立开发者社群中引发短暂讨论，故评分为
    1.5。
sentiment: neutral
developer_sentiment:
  tone: skeptical
  primary_focus: App Store 审核机制的透明度以及开发者借媒体造势误导舆论的诚信问题
hype_assessment:
  level: low
  reason: 本文是一篇撤回声明，主动承认前一天文章的前提完全错误，并公开保留原文全文（含 PDF/Markdown 存档）供读者核验，属于去伪存真的纠错行为，没有任何概念包装或'颠覆'、'革命'类
    PR 话术，反而体现了对公信力的负责任态度。
information_entropy: medium
domain_disruption:
  technical_innovation: 无，该事件不涉及任何技术架构或工程实现突破，核心是应用商店审核政策与媒体公信力问题；唯一的边缘技术细节（Dark Hours
    网页版存在将用户路由到墨西哥随机地块的 bug）也只是撞名纠纷的佐证，而非创新点。
  business_model: 无，对商业模式或 SaaS 生态无重塑力，仅折射出 iOS 独立开发者对不透明审核流程的依赖与借助 KOL 发声的公关路径，未形成任何结构性商业变化。
engineering_complexity: conceptual
compound_value:
  score: 2.0
  reason: 投资逻辑推演：首先，该事件本质是科技媒体把关失误与苹果 App Store 审核正确性的一次个案验证，不涉及任何 AI 技术突破、资本流向或基础设施沉淀，不具备复利积累的底层资产。其次，虽然苹果审核流程被证明正确、平台治理公信力得到一次背书，但这只是对既有垄断地位的边际强化，不构成新的结构性壁垒，也不会改变开发者和资本的平台选择决策。最后，事件中的受益方（如
    DarkHours 开源项目）仅获得流量转移级别的短期关注，无商业模式或护城河层面的增量。综合判断：属于一次性媒体事件，无长期资本回报路径，score 落在
    1-3 区间。
value_capture_layer: end_application
moat_impact: neutral
key_beneficiaries:
- Apple
- DarkHours 开源项目 (Miguel Beher)
competitive_casualty:
- Terry Godier
- Daring Fireball (John Gruber)
- 独立开发者群体的 App Store 拒审申诉公信力
market_opportunities:
- 科技媒体可开发基于多源交叉验证的事实核查工具，在发表前自动比对开发者公开声称与应用商店记录、代码仓库、域名解析等一手证据的一致性，降低被信息源误导的风险
- 应用审核生态存在透明度痛点，创业者可打造面向开发者的审核政策合规预审与申诉辅助工具，帮助识别内容分类（如占星与天文）等易引发拒绝的边界场景
- 品牌与命名冲突检测（开源项目撞名、域名占位）是一个可产品化的轻量级方向，可为独立开发者提供发布前的名称/域名冲突预警，避免上线后被迫下线的损失
risk_matrix:
  regulatory: 苹果应用审核对占星/迷信类内容的分类判定标准不透明，开发者与第三方报道者因信息不对称可能产生误读，进而引发对平台政策公信力的争议；但本事件中苹果的拒绝及
    App Review Board 的维持裁决均被证实正确，监管直接风险较低。
  technological: 事件中 Godier 的 Web 应用 Dark Hours 与开源项目 DarkHours 共享同一 bug（将用户路由到墨西哥随机地块），凸显复用代码时的技术债与身份混淆风险；同时信息传播依赖博客
    RSS，缺乏结构化的事实验证机制。
  competitive: 独立开发者与开源项目之间的命名冲突（Dark Hours vs DarkHours）及域名占位问题，反映小型团队在生态中缺乏品牌保护能力，易被同名项目或资源更雄厚的竞争者挤压。
  ethical: 本次事件核心是开发者通过公开博客与私下通讯系统性误导资深媒体人，导致不实信息经高信任渠道扩散后需整体撤回，凸显科技媒体信任与把关危机；被隐瞒的占星/塔罗内容本身也涉及迷信内容对用户的潜在误导。
  additional:
  - 媒体声誉风险：John Gruber 24 年写作生涯首次撤回文章，此类事件会侵蚀媒体机构公信力，进而影响其后续报道的传播权重与读者信任
  - 平台叙事风险：即便苹果本次判定正确，应用审核机制长期被批评不透明，事件仍可能被误读为'平台打压独立开发者'的叙事素材
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: product
  name: Dark Hours
  canonical_name: Dark Hours
  url: https://darkhours.io
  positioning: Dark Hours 是开发者 Terry Godier 推出的面向普通用户的天文网站，由被 App Store 拒绝的应用移植到网页后上线，现已因撞名争议下线。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 普通天文爱好者
  - 对暗空观测感兴趣的普通用户
  product_signal: 作为纯天文科普版本，Dark Hours 面向普通人的暗空观测需求，但被发现与开源项目共享同一路由 bug，已随争议下线。
  market_signal: 产品上线一周便因撞名与代码问题被迫下线，域名重定向至开源项目，显示独立网页应用的命名与质量风险较高。
  differentiation: 与最初提交审核的占星应用 Asterly 形成鲜明对比，Dark Hours 主打硬科学天文内容，却因与已有开源项目同名而丧失独特性。
  watch_reason: Dark Hours 完整呈现了独立开发者从 App Store 被拒到转战网页、再因撞名争议下线的典型路径，可作为应用审核与网页产品生命周期的观察样本。
  risk_notes:
  - 产品已下线并将域名重定向到他人项目，事实上已停止运营，后续活跃度存疑。
  - 开发者陷入向公众与媒体隐瞒应用真实性质的信任争议，连带影响品牌可信度。
  score: 3.0
  article_ids:
  - ca10c0d1e9cfbe9e
  evidence_snippets:
  - Godier 在应用被拒后把天文版本移植到网页，上周以 Dark Hours 之名在 darkhours.io 域名上线。
  - 在与 Miguel Beher 发生撞名争议后，Godier 将网页应用下线，并把 darkhours.io 域名重定向到 Beher 的 darkhours.app。
- object_type: product
  name: Asterly
  canonical_name: Asterly
  url: null
  positioning: Asterly 是 Terry Godier 于 2026 年 1 月提交给苹果 App Store 的占星应用，完全致力于占星术并提供每日塔罗牌占卜，因内容违规被审核拒绝。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 占星术与塔罗牌兴趣人群
  product_signal: Asterly 的功能核心是占星与每日塔罗牌，不包含天文内容，苹果的拒绝及 App Review Board 的维持裁决均被证实正确。
  market_signal: 应用自一月提交至四月维持驳回，开发者未再提交移除占星内容的更新构建，产品未能进入 App Store 市场。
  differentiation: 与后来以 Dark Hours 名义出现的纯天文版本相比，Asterly 本质上是占星应用，二者在内容属性上截然不同。
  watch_reason: Asterly 是苹果 App Store 审核机制正确运作的典型案例，其驳回、复议与开发者事后误导媒体的全过程，为理解应用审核与开发者诚信问题提供了完整样本。
  risk_notes:
  - 应用含占星与塔罗内容，被苹果认定违规，即便移除相关内容重新提交，审核结果仍存在不确定性。
  - 开发者曾对外声称应用不含占星功能，存在误导公众与媒体的诚信风险。
  score: 2.0
  article_ids:
  - ca10c0d1e9cfbe9e
  evidence_snippets:
  - Godier 于一月向 App Store 提交的占星应用名为 Asterly，完全致力于占星术并包含塔罗牌每日占卜功能。
  - Asterly 在四月被 App Review Board 维持拒绝裁决时仍沿用此名，苹果从未收到过名为 Dark Hours 的应用。
- object_type: project
  name: mbeher2200/DarkHours
  canonical_name: DarkHours
  url: https://github.com/mbeher2200/DarkHours
  positioning: DarkHours 是 Miguel Beher 开发并托管在 GitHub 的开源天文摄影与暗空规划工具，为天文爱好者提供暗空定位与拍摄辅助能力。
  technical_signal: 项目以开源形式托管在 GitHub，聚焦天文摄影与暗空规划，代码可被社区自由审查、复用与协作改进。
  adoption_signal: Beher 在 Bluesky 上公开指出克隆应用与其共享同一路由 bug，说明项目代码已被他人参考或复制，具备一定可见度。
  ecosystem_relevance: 在 Godier 撞名事件中，DarkHours 成为社区对照的原始项目，凸显开源命名与代码归属在开发者生态中的辨识度价值。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该开源项目意外卷入网页应用撞名与代码 bug 争议，反映出天文工具类开源项目在品牌保护与代码质量上面临的共性问题，其后续维护值得持续跟踪。
  risk_notes:
  - 同名克隆应用曾分流用户并引发混淆，开源项目面临品牌被冒用而难以追溯的治理风险。
  - 项目被发现存在把用户路由到墨西哥随机地块的 bug，暗空规划工具的地理准确性存疑。
  score: 3.0
  article_ids:
  - ca10c0d1e9cfbe9e
  evidence_snippets:
  - Miguel Beher 的开源项目 DarkHours 是一个天文摄影与暗空规划工具，源代码托管在 GitHub 上。
  - Beher 在 Bluesky 上指出 Godier 的 Dark Hours 与其项目存在把用户路由到墨西哥随机地块的相同 bug。
- object_type: product
  name: Current
  canonical_name: Current
  url: https://www.terrygodier.com/current
  positioning: Current 是 Terry Godier 开发的 iOS 独占 RSS 阅读器，用于践行其交互式文章《Phantom Obligation》中的订阅源阅读设计理念，被视为突破性产品。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - iOS 用户
  - RSS 订阅阅读爱好者
  - 交互式文章读者
  product_signal: 作为 RSS 阅读器，Current 将交互式文章中的产品理念落地，被 The Verge 的 David Pierce 列入不想换回
    Android 的 iOS 独占应用短名单。
  market_signal: Current 上线后获得专业媒体背书，进入 iOS 独占独立应用推荐短名单，在订阅阅读细分市场建立了差异化口碑。
  differentiation: 相较主流 RSS 客户端，Current 由交互式产品理念驱动、专注 iOS 平台，并以独立开发者身份获得头部科技媒体的认可。
  watch_reason: Current 是被专业媒体认可的突破性 RSS 产品，但其开发者 Godier 深陷 App Store 误导争议，产品声誉与后续发展面临不确定性，值得跟踪观察。
  risk_notes:
  - 开发者卷入误导媒体与隐瞒应用性质的信任争议，可能连带损害 Current 的公众形象与口碑。
  - 作为独立开发者新晋产品，Current 的长期维护、商业化路径与竞品压力仍是未知数。
  score: 4.0
  article_ids:
  - ca10c0d1e9cfbe9e
  evidence_snippets:
  - Godier 的 RSS 阅读器 Current 是他为践行交互式文章中的理念而制作的，被认为是名副其实的突破性产品。
  - The Verge 的 David Pierce 将 Current 列入让他不想换回 Android 的 iOS 独占应用短名单。
---

Title: Retraction: The App Store Rejection of the Week That Was, in Fact, a Correct Rejection

URL Source: https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week

Markdown Content:
Yesterday I published an article titled “App Store Rejection of the Week: Dark Hours”. I have retracted it. Its premise was so fundamentally wrong that there’s no point merely correcting or editing it. Even the title, as I explain below, was inaccurate. Although the original is now retracted, I’m not memory-holing it. The text of the original story is available, for transparency and accountability, [in plain text](https://daringfireball.net/misc/2026/08/app_store_rejection_of_the_week_dark_hours.text) (Markdown, natch) and [PDF](https://daringfireball.net/misc/2026/08/App_Store_Rejection_of_the_Week_-_Dark_Hours.pdf) (preserving original presentation). Both of those versions include a preface at the top linking to this retraction. [The URL](https://daringfireball.net/2026/08/app_store_rejection_of_the_week_dark_hours) for the original story now redirects to this one that you are currently reading.

To the best of my recollection, this is the first post I’ve retracted in the 24 years I’ve been writing Daring Fireball. I hope it’s the last. I was misled, both overtly and through omissions, in several ways, but what I publish is my responsibility, and I apologize for the error.

Terry Godier first came to my attention in February, when [I linked to](https://daringfireball.net/linked/2026/02/25/godier-phantom-obligation) his excellent interactive essay on RSS feed reader design, “[Phantom Obligation](https://www.terrygodier.com/phantom-obligation)”, which essay introduced [Current](https://www.terrygodier.com/current), Godier’s new RSS reader that he made to exemplify the ideas from his essay. Current is, deservedly, a bit of a breakout hit. (E.g., David Pierce, at The Verge, [put it on a very short list](https://www.theverge.com/tech/899602/best-phone-android-ios-app-store?view_token=eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IkpKUk05aEQ3ZHYiLCJwIjoiL3RlY2gvODk5NjAyL2Jlc3QtcGhvbmUtYW5kcm9pZC1pb3MtYXBwLXN0b3JlIiwiZXhwIjoxNzc2MDMzMDU5LCJpYXQiOjE3NzU2MDEwNTl9.c8VIrq4Kl5DbAbr8ujYsehwxWVKN7dvXMV7yYkqADu0) of iOS-exclusive indie apps that keep him from switching to Android.) In March [I linked to another](https://daringfireball.net/linked/2026/03/16/the-last-quiet-thing) interactive essay from Godier, “[The Last Quiet Thing](https://www.terrygodier.com/the-last-quiet-thing)”, and again [in April to a post](https://daringfireball.net/linked/2026/04/16/app-store-reviews-are-busted) regarding the App Store’s 5-star review system. I struck up an iMessage correspondence with Godier around when I first linked to his work.

Yesterday Godier posted “[Browsers Have Standards, the App Store Has Judgment](https://blog.terrygodier.com/2026/08/07/browsers-have-standards-the-app.html)”. As originally published, that post contained these two paragraphs:

> A while ago I tried to submit an iOS app for [Dark Hours](https://darkhours.io/), my astronomy website for normal people. It was rejected on the grounds that it was astrology.
> 
> 
> It has no tarot function, no horoscopes, and nothing that I, or anyone else I’ve asked, would associate with astrology.

Those paragraphs, at this writing (August 8, 11:00 pm ET), have been deleted and replaced by this:

> Note: the original version of this post had a section here about an astronomy app I am working on that began as an astrology app and was rejected after having the astrology content removed. App store [_sic_] review reached out to me and let me know that they had apparently never been given the updated build and that the app should be fine to submit now.

You can now see the problem that has led me to fully retract my original post, given that my post was entirely predicated on the premise that Godier’s original description of the rejected app was true — that the app “has no tarot function, no horoscopes, and nothing that I, or anyone else I’ve asked, would associate with astrology.” The truth is, the app, as originally submitted by Godier to the App Store (under the name “Asterly”, not “Dark Hours”), was entirely dedicated to astrology, not astronomy, and did in fact include a “Tarot card of the day” feature amongst other occultist horseshit.

The grounds of Apple’s original App Store rejection of the app, and the rejection’s upholding by the App Review Board, were correct.[1](https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week#fn1-2026-08-08) I wrongly took Godier at his word, both in his public blog post and in private iMessage correspondence yesterday, that the rejection wasn’t just merely debatable, but completely and rather preposterously ungrounded. Whether Godier ever submitted a build of “Asterly” to the App Store that contained no occult horseshit and only the hard-science astronomy features that were present in his “Dark Hours” website that was available for the last week, I don’t know. But I have no reason to believe that he did.

My [disdain for astrology](https://daringfireball.net/linked/2024/04/11/astrology-astronomy-eclipse) is so utter, and my esteem for Godier’s previous work so high, that it simply never occurred to me that he might have actually made and submitted to the App Store an astrology app, let alone that he’d then feign surprise and frustration that an astrology app was rejected for being an astrology app. I showed him a draft of my post before publication, to make sure I had the story straight, and he offered not a word of caution, only gratitude for my drawing attention to the matter.

It gets messier. Godier’s astrology app that he submitted to the App Store back in January was named “Asterly”. That was still the name when the App Review Board upheld its rejection in April. According to Godier, frustrated by the App Store’s rejection, he ported the astronomy version to the web, [launching it last week](https://bsky.app/profile/terrygodier.com/post/3ms2lm4kcfc2j) under the name “Dark Hours” at the domain `darkhours.io`. (This is why it was incorrect for me, in the very title of my post, to claim that Apple had rejected an app named “Dark Hours”. They rejected an app named “Asterly” and had never seen an app from Godier named “Dark Hours”.) Yesterday, after I linked to Godier’s post and [Hacker News then linked to my post](https://news.ycombinator.com/item?id=49214863), Godier’s “Dark Hours” (with a space) [came to the attention](https://bsky.app/profile/mmmeh.bsky.social/post/3msjump44fs2h) (and justifiable surprise) of Miguel Beher, creator of an open-source “astrophotography and dark-sky planner” project named DarkHours (no space). [Beher’s GitHub project](https://github.com/mbeher2200/DarkHours) contains the source code, and the actual web app is [freely available at the domain `darkhours.app`](https://darkhours.app/). In an uncomfortable exchange between Beher and Godier on Bluesky, Beher pointed out that Godier’s Dark Hours had the same bug as Beher’s that [routed people to “random fields in Mexico”](https://bsky.app/profile/mmmeh.bsky.social/post/3mslc3b3u4c2l). Earlier today, Godier took his web app down and redirected his `darkhours.io` domain to Beher’s `darkhours.app`.

At the end of my now-retracted post yesterday, assuming I had righteously and rightly skewered Apple for an egregiously erroneous App Store review rejection, I wrote:

> Mistakes happen. But in a functioning system mistakes get corrected, and mistakes as obvious as this one get corrected almost instantly and include a quick apology for the conflation.

Obviously it was _I_ who was mistaken. _This_ article is my correction, and I apologize to [all](https://news.ycombinator.com/item?id=49214863) who read and believed my now-retracted post, and to the reviewers at the App Store whose competence (if not literacy) I besmirched. Sorry about that. Won’t happen again.

* * *

1.   Regardless of one’s opinion regarding pseudoscience and occultist horseshit — pro, con, or indifferent — one might reasonably think it wrong for Apple to disallow or discourage such apps from the App Store. In fact, there exist plenty of such apps in the App Store, and Apple has even run “[Best Astrology Apps](https://apps.apple.com/us/story/id1681180517)” editorial features. Apple’s stance is basically that the App Store has enough of these apps (and I suspect they’re a common source of scams, given that by their very nature they target the gullible). [Guideline 4.3(b) states](https://developer.apple.com/app-store/review/guidelines/) (emphasis added):

> Certain kinds of apps, such as dating, flashlight, sound effects, wallpaper, simple timers, and _fortune telling_, are well established on the App Store and we will not accept new submissions unless they offer a meaningfully different or improved experience. We may remove these apps from the App Store going forward if they are not updated, improved, or do not attract customers. Other kinds of apps, such as drinking games, Kama Sutra, fart, and burp apps, are mediocre, low-quality, or low-effort and do not add value to the App Store.

That serial comma, ever useful, gives hope to anyone hard at work on a “fart and burp” app.[↩︎](https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week#fnr1-2026-08-08 "Jump back to footnote 1 in the text.")