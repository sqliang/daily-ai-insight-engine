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
pipeline_stage: ingested
id: f4b489ce2fdadba0
---

Patreon, the membership platform for creators, is cracking down on AI scraping its content for training purposes. On Thursday, the company shared that it’s working with internet infrastructure provider Cloudflare to directly block access to AI bots designed to train their AI models on creators’ work without permission.

The strengthened measures were necessary because AI scraping has become more sophisticated since it first put measures in place to deter AI crawlers in 2023, the company says. In addition, Patreon’s paywall has long locked much of creators’ content out of reach of crawlers. But more recently, the company introduced new discovery tools like a redesigned Home Feed and its tweet-like Quips, which could expose more content to crawlers.

The changes come about as more online publishers and content creators are coming to grips with how AI is ingesting their work for the purpose of making their AI models smarter. To combat this, Cloudflare now offers tools that allow website publishers to restrict AI bots, including a marketplace that lets websites charge AI bots for scraping, dubbed Pay Per Crawl. Earlier this month, it changed its policies so that “mixed-use” crawlers, meaning those that both index and train on a website’s content, are blocked by default on any pages that host ads.

Patreon says that it’s extending its existing work with Cloudflare to use the company’s AI Crawl Control technology to update its AI policies and enforcement tools. The difference here is that instead of simply asking AI crawlers not to scrape content using the robots.txt files — a standard way to provide bots with instructions on how they can use its site — Patreon is now actively blocking AI training bots.

“Consent shouldn’t depend on whether a scraper chooses to behave,” a Patreon blog post explains, referencing the stricter measures.

When testing the features, individual AI training crawlers’ weekly attempts to access Patreon went from “thousands of attempts to zero,” the post noted. That indicates that the AI scrapers were ignoring Patreon’s robots.txt file and scraping the site anyway, despite its requests.

However, the company said that it will allow bots that index pages and organize information that can be used to send users back to Patreon.

“As AI agents become increasingly powerful and popular, creators deserve a meaningful say in how their work is used by AI companies,” remarked Patreon’s product chief Drew Rowny in the announcement. “On most of the Internet, creators have to accept AI training on their work just to reach and grow an audience. Patreon has a different vision: creators should be able to grow their audience and control how their work is used.”