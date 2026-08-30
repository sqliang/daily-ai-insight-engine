---
title: Choose Boring Technology (2015)
source: https://mcfunley.com/choose-boring-technology
author:
- '[[tosh]]'
published: '2026-08-13'
created: '2026-08-14'
manifest_dates:
- '2026-08-14'
description: 'Article URL: https://mcfunley.com/choose-boring-technology Comments
  URL: https://news.ycombinator.com/item?id=49289512 Points: 338 # Comments: 176'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f9c2faed5b010c6e
source_type: community_discussion
tldr: 前 Etsy 工程师 Dan McKinley 提出「选择无聊技术」的工程选型原则：公司应把有限创新代币花在核心业务上，优先选用成熟、故障模式已知的技术栈，并在引入新技术前通过全局成本评估与组织共识流程加以约束。
objective_summary: Dan McKinley 在 2015 年发表博客文章，结合自身在 Etsy 的经历以及前主管 Kellan 的技术决策影响，系统阐述「选择无聊技术」的选型哲学。文章将公司可承受的技术创新量类比为固定数量的「创新代币」，主张用成熟技术解决多数问题，只有在现有栈确实无法经济地解决问题时才引入新技术，并强调任何新技术引入都应经过组织层面的公开讨论、迁移承诺和成本评估。文中以
  Etsy 早期因堆砌 Python 中间层导致数年无法交付、以及用 PHP/MySQL/Memcached/Gearman 构建 activity feeds
  并随平台自然扩展 20 倍的案例，说明克制选型对长期运营可靠性的价值。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies:
  - Etsy
  technologies:
  - MySQL
  - Postgres
  - PHP
  - Python
  - Memcached
  - Squid
  - Cron
  - NodeJS
  - MongoDB
  - Ruby
  - Scala
  - Redis
  - Gearman
  - Solr
  - Java
  key_people:
  - Dan McKinley
  - Kellan
  - Don Rumsfeld
  - Socrates
key_logic_flow:
- 作者以 Kellan 在 Etsy 的技术决策为起点，提出「拥抱无聊」的选型原则，认为工程师应将有限注意力集中在公司业务使命而非工具创新上。
- 文章引入「创新代币」概念，指出每个公司在成熟前大约只有三枚可消耗的创新代币，选择 NodeJS、MongoDB、自研数据库等新潮技术都会消耗这些珍贵资源。
- 作者区分了「已知未知」与「未知未知」，强调成熟技术的优势不仅在于能力已知，更在于故障模式和运维边界已被充分理解。
- 文章批评「为每个任务选最佳工具」的局部优化思维，认为真正要优化的是公司整体运营成本、认知负载和长期可靠性。
- 作者提出引入新技术的约束流程：先在现有栈内求解、书面记录旧栈的不可行之处、明确迁移旧功能的承诺与时间表，并组织全公司可见的讨论。
- Etsy 的案例从正反两方面印证了观点：早期为 Python 程序员强造中间层导致数年无法交付，而 activity feeds 基于 PHP/MySQL/Memcached/Gearman
  却在无人专门维护时随平台自然扩展 20 倍。
object_mentions:
- object_type: product
  name: MySQL
  canonical_name: MySQL
  url: https://www.mysql.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者将 MySQL 列为「无聊但足够好」的技术范例，认为其能力与失败模式已被充分理解。
  - 文章指出成熟技术如 MySQL、Postgres、PHP、Python 的共有特征是 boring and good，适合作为默认选型。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Postgres
  canonical_name: PostgreSQL
  url: https://www.postgresql.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Postgres 被作者归入「无聊但良好」的技术清单，作为推荐默认选择的关系型数据库之一。
  - 作者用 Postgres 与 MySQL 并列，说明 boring 不等于 bad，而是代表运维经验丰富、风险可控。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: PHP
  canonical_name: PHP
  url: https://www.php.net/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - PHP 被文章列为 boring 技术的代表，作者认为它能力已知、失败模式已知。
  - Etsy 曾努力将大部分系统统一迁移到 PHP，并基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Python
  canonical_name: Python
  url: https://www.python.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Python 被列入无聊但可接受的技术清单，说明其成熟度足以作为默认工具。
  - Etsy 早期案例显示，公司招聘了一批 Python 程序员后为他们强造了一个无意义的中间层，导致长期技术债。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Memcached
  canonical_name: Memcached
  url: https://memcached.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Memcached 被列为 boring 技术的典型代表，适合作为默认缓存方案。
  - Etsy 使用 PHP/MySQL/Memcached/Gearman 技术栈实现 activity feeds，并在数年间随平台自然扩展 20 倍。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Redis
  canonical_name: Redis
  url: https://redis.io/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Redis 被用作反例，说明如果用新潮技术实现 activity feeds 可能会更简单，但也会增加未知风险。
  - 文章强调，即使 Redis 可能让 activity feeds 更易实现，Etsy 仍选择基于现有栈构建，以获得长期可维护性。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Gearman
  canonical_name: Gearman
  url: http://gearman.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Gearman 被描述为 PHP 的作业服务器，是 Etsy 统一技术栈的一部分。
  - Etsy 基于 PHP/MySQL/Memcached/Gearman 构建 activity feeds，证明有限技术栈可以支撑复杂功能。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: Solr
  canonical_name: Apache Solr
  url: https://solr.apache.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Solr 是文章中少数被明确认定为必须引入的新技术案例，因为用原始 PHP 实现带分面的全文搜索并不现实。
  - 作者用 Solr 说明其立场并非绝对化：当现有栈确实无法经济地解决问题时，引入新技术是合理的。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: NodeJS
  canonical_name: Node.js
  url: https://nodejs.org/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 作者用 NodeJS 作为消耗创新代币的例子，说明选择它会占用公司有限的技术冒险预算。
  - 文章认为，除非公司是 JavaScript 咨询公司，否则把创新代币花在 NodeJS 这类工具上会增加失败或延迟的风险。
  article_id: f9c2faed5b010c6e
- object_type: product
  name: MongoDB
  canonical_name: MongoDB
  url: https://www.mongodb.com/
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - MongoDB 被作为消耗一枚创新代币的典型例子，说明新潮数据库的未知风险较高。
  - 作者指出，除非公司是数据库公司，否则把创新资源投入在底层数据存储技术上并不明智。
  article_id: f9c2faed5b010c6e
- object_type: project
  name: Etsy activity feeds
  canonical_name: Etsy Activity Feeds
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 作者以 Etsy 的 activity feeds 功能为例，说明基于 PHP/MySQL/Memcached/Gearman 的保守实现能够在数年间随平台自然扩展
    20 倍。
  - 该项目在上线后数年无人专门维护，但因使用共享平台而稳定运行，体现了克制技术选型的长期收益。
  article_id: f9c2faed5b010c6e
extract_result: success
---

Probably the single best thing to happen to me in my career was having had Kellan placed in charge of me. I stuck around long enough to see Kellan’s technical decisionmaking start to bear fruit. I learned a great deal *from* this, but I also learned a great deal as a *result* of this. I would not have been free to become the engineer that wrote Data Driven Products Now! if Kellan had not been there to so thoroughly stick the landing on technology choices.

In the year since leaving Etsy, I’ve resurrected my ability to care about technology. And my thoughts have crystallized to the point where I can write them down coherently. What follows is a distillation of the Kellan gestalt, which will hopefully serve to horrify him only slightly.

##### Embrace Boredom.

Let’s say every company gets about three innovation tokens. You can spend these however you want, but the supply is fixed for a long while. You might get a few more *after* you achieve a certain level of stability and maturity, but the general tendency is to overestimate the contents of your wallet. Clearly this model is approximate, but I think it helps.

If you choose to write your website in NodeJS, you just spent one of your innovation tokens. If you choose to use MongoDB, you just spent one of your innovation tokens. If you choose to use service discovery tech that’s existed for a year or less, you just spent one of your innovation tokens. If you choose to write your own database, oh god, you’re in trouble.

Any of those choices might be sensible if you’re a javascript consultancy, or a database company. But you’re probably not. You’re probably working for a company that is at least ostensibly rethinking global commerce or reinventing payments on the web or pursuing some other suitably epic mission. In that context, devoting any of your limited attention to innovating ssh is an excellent way to fail. Or at best, delay success [1].

What counts as boring? That’s a little tricky. “Boring” should not be conflated with “bad.” There is technology out there that is both boring and bad [2]. You should not use any of that. But there are many choices of technology that are boring and good, or at least good enough. MySQL is boring. Postgres is boring. PHP is boring. Python is boring. Memcached is boring. Squid is boring. Cron is boring.

The nice thing about boringness (so constrained) is that the capabilities of these things are well understood. But more importantly, their failure modes are well understood. Anyone who knows me well will understand that it’s only with a overwhelming sense of malaise that I now invoke the spectre of Don Rumsfeld, but I must.

When choosing technology, you have both known unknowns and unknown unknowns [3].

- A known unknown is something like:
*we don’t know what happens when this database hits 100% CPU.* - An unknown unknown is something like:
*geez it didn’t even occur to us that writing stats would cause GC pauses.*

Both sets are typically non-empty, even for tech that’s existed for decades. But for shiny new technology the magnitude of unknown unknowns is significantly larger, and this is important.

##### Optimize Globally.

I unapologetically think a bias in favor of boring technology is a good thing, but it’s not the only factor that needs to be considered. Technology choices don’t happen in isolation. They have a scope that touches your entire team, organization, and the system that emerges from the sum total of your choices.

Adding technology to your company comes with a cost. As an abstract statement this is obvious: if we’re already using Ruby, adding Python to the mix doesn’t feel sensible because the resulting complexity would outweigh Python’s marginal utility. But somehow when we’re talking about Python and Scala or MySQL and Redis people lose their minds, discard all constraints, and start raving about using the best tool for the job.

Your function in a nutshell is to map business problems onto a solution space that involves choices of software. If the choices of software were truly without baggage, you could indeed pick a whole mess of locally-the-best tools for your assortment of problems.

But of course, the baggage exists. We call the baggage “operations” and to a lesser extent “cognitive overhead.” You have to monitor the thing. You have to figure out unit tests. You need to know the first thing about it to hack on it. You need an init script. I could go on for days here, and all of this adds up fast.

The problem with “best tool for the job” thinking is that it takes a myopic view of the words “best” and “job.” Your job is keeping the company in business, god damn it. And the “best” tool is the one that occupies the “least worst” position for as many of your problems as possible.

It is basically always the case that the long-term costs of keeping a system working reliably vastly exceed any inconveniences you encounter while building it. Mature and productive developers understand this.

##### Choose New Technology, Sometimes.

Taking this reasoning to its *reductio ad absurdum* would mean picking Java, and then trying to implement a website without using anything else at all. And that would be crazy. You need some means to add things to your toolbox.

An important first step is to acknowledge that this is a process, and a conversation. New tech eventually has company-wide effects, so adding tech is a decision that requires company-wide visibility. Your organizational specifics may force the conversation, or they may facilitate developers adding new databases and queues without talking to anyone. One way or another you have to set cultural expectations that **this is something we all talk about**.

One of the most worthwhile exercises I recommend here is to **consider how you would solve your immediate problem without adding anything new**. First, posing this question should detect the situation where the “problem” is that someone really wants to use the technology. If that is the case, you should immediately abort.

It can be amazing how far a small set of technology choices can go. The answer to this question in practice is almost never “we can’t do it,” it’s usually just somewhere on the spectrum of “well, we could do it, but it would be too hard” [4]. If you think you can’t accomplish your goals with what you’ve got now, you are probably just not thinking creatively enough.

It’s helpful to **write down exactly what it is about the current stack that makes solving the problem prohibitively expensive and difficult.** This is related to the previous exercise, but it’s subtly different.

New technology choices might be purely additive (for example: “we don’t have caching yet, so let’s add memcached”). But they might also overlap or replace things you are already using. If that’s the case, you should **set clear expectations about migrating old functionality to the new system.** The policy should typically be “we’re committed to migrating,” with a proposed timeline. The intention of this step is to keep wreckage at manageable levels, and to avoid proliferating locally-optimal solutions.

This process is not daunting, and it’s not much of a hassle. It’s a handful of questions to fill out as homework, followed by a meeting to talk about it. I think that if a new technology (or a new service to be created on your infrastructure) can pass through this gauntlet unscathed, adding it is fine.

##### Just Ship.

Polyglot programming is sold with the promise that letting developers choose their own tools with complete freedom will make them more effective at solving problems. This is a naive definition of the problems at best, and motivated reasoning at worst. The weight of day-to-day operational toil this creates crushes you to death.

Mindful choice of technology gives engineering minds real freedom: the freedom to contemplate bigger questions. Technology for its own sake is snake oil.

*Update, July 27th 2015: I wrote a talk based on this article. You can see it here.*

- Etsy in its early years suffered from this pretty badly. We hired a bunch of Python programmers and decided that we needed to find something for them to do in Python, and the only thing that came to mind was creating a pointless middle layer that required years of effort to amputate. Meanwhile, the 90th percentile search latency was about two minutes. Etsy didn't fail, but it went several years without shipping anything at all. So it took longer to succeed than it needed to.
- We often casually refer to the boring/bad intersection of doom as “enterprise software,” but that terminology may be imprecise.
- In saying this Rumsfeld was either intentionally or unintentionally alluding to the Socratic Paradox. Socrates was by all accounts a thoughtful individual in a number of ways that Rumsfeld is not.
-
A good example of this from my experience is Etsy’s activity feeds. When we built this feature, we were working pretty hard to consolidate most of Etsy onto PHP, MySQL, Memcached, and Gearman (a PHP job server). It was much more complicated to implement the feature on that stack than it might have been with something like Redis (or maybe not). But it is absolutely possible to build activity feeds on that stack.

An amazing thing happened with that project: our attention turned elsewhere for several years. During that time, activity feeds scaled up 20x while

*nobody was watching it at all.*We made no changes whatsoever specifically targeted at activity feeds, but everything worked out fine as usage exploded because we were using a shared platform. This is the long-term benefit of restraint in technology choices in a nutshell.This isn’t an absolutist position--while activity feeds stored in memcached was judged to be practical, implementing full text search with faceting in raw PHP wasn't. So Etsy used Solr.