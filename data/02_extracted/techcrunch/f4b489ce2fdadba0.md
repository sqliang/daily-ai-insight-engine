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
---

Patreon, the membership platform for creators, is cracking down on AI scraping its content for training purposes. On Thursday, the company shared that it’s working with internet infrastructure provider Cloudflare to directly block access to AI bots designed to train their AI models on creators’ work without permission.

The strengthened measures were necessary because AI scraping has become more sophisticated since it first put measures in place to deter AI crawlers in 2023, the company says. In addition, Patreon’s paywall has long locked much of creators’ content out of reach of crawlers. But more recently, the company introduced new discovery tools like a redesigned Home Feed and its tweet-like Quips, which could expose more content to crawlers.

The changes come about as more online publishers and content creators are coming to grips with how AI is ingesting their work for the purpose of making their AI models smarter. To combat this, Cloudflare now offers tools that allow website publishers to restrict AI bots, including a marketplace that lets websites charge AI bots for scraping, dubbed Pay Per Crawl. Earlier this month, it changed its policies so that “mixed-use” crawlers, meaning those that both index and train on a website’s content, are blocked by default on any pages that host ads.

Patreon says that it’s extending its existing work with Cloudflare to use the company’s AI Crawl Control technology to update its AI policies and enforcement tools. The difference here is that instead of simply asking AI crawlers not to scrape content using the robots.txt files — a standard way to provide bots with instructions on how they can use its site — Patreon is now actively blocking AI training bots.

“Consent shouldn’t depend on whether a scraper chooses to behave,” a Patreon blog post explains, referencing the stricter measures.

When testing the features, individual AI training crawlers’ weekly attempts to access Patreon went from “thousands of attempts to zero,” the post noted. That indicates that the AI scrapers were ignoring Patreon’s robots.txt file and scraping the site anyway, despite its requests.

However, the company said that it will allow bots that index pages and organize information that can be used to send users back to Patreon.

“As AI agents become increasingly powerful and popular, creators deserve a meaningful say in how their work is used by AI companies,” remarked Patreon’s product chief Drew Rowny in the announcement. “On most of the Internet, creators have to accept AI training on their work just to reach and grow an audience. Patreon has a different vision: creators should be able to grow their audience and control how their work is used.”