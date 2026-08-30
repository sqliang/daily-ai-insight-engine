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