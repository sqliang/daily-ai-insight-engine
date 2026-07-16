---
title: Hack suggests AI music generator Suno scraped YouTube for training data
source: https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/
author:
- '[[Amanda Silberling]]'
published: '2026-07-15'
created: '2026-07-16'
manifest_dates:
- '2026-07-16'
description: The hacker used an employee's credentials to access source code, which
  revealed how Suno scraped decades of audio.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 29f4ab98d1ecdbdf
source_type: news_media
tldr: AI音乐生成器Suno遭供应链攻击，黑客获取员工凭证后访问了源代码，声称找到了Suno从YouTube Music、Deezer、Genius等平台抓取数十年音频数据用于AI训练的证据。Suno未告知用户此次数据泄露，并称事件已快速控制。
objective_summary: 2025年11月，AI音乐生成器Suno遭到供应链攻击，黑客通过入侵获取了员工凭证，进而访问了公司源代码。根据404 Media报道，源代码显示Suno疑似从YouTube
  Music、Deezer、Genius、库存音乐库和播客RSS抓取了数十年音频数据用于训练AI模型。Suno此前承认使用公开网络上的音乐文件训练AI，并主张合理使用原则。三大唱片公司正在起诉Suno，指控其违反DMCA故意绕过YouTube的反抓取保护措施。黑客还获取了客户邮箱、电话号码和Stripe中的部分信用卡号。Suno未通知用户此次泄露，仅称其为一次已快速控制的有限安全事件。
event_type: policy_and_safety
epistemic_status: rumor_leak
entities:
  companies:
  - Suno
  - YouTube
  - Deezer
  - Genius
  - Google
  - Stripe
  - 404 Media
  technologies: []
  key_people: []
key_logic_flow:
- Suno在2025年11月遭供应链攻击，黑客通过入侵员工凭证获取了源代码访问权限。
- 源代码显示Suno疑似从YouTube Music、Deezer、Genius、库存音乐库和播客RSS抓取了数十年音频数据用于AI训练。
- 三大唱片公司正在起诉Suno，指控其违反DMCA故意绕过YouTube的反抓取保护措施，并违反YouTube服务条款。
- 黑客还获取了客户数据，包括邮箱、电话号码和Stripe中的部分信用卡号。
- Suno未向客户通报此次数据泄露，仅声称是一次已快速控制的有限安全事件。
- 竞争对手Udio也面临类似的YouTube数据抓取指控，Google同样因版权侵权被多家出版商起诉。
object_mentions:
- object_type: product
  name: Suno
  canonical_name: Suno AI
  url: https://suno.com
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章以Suno被黑客攻击为核心事件展开报道。
  - 文章详细描述Suno被指控从YouTube等平台抓取音频数据用于训练AI。
  - 三大唱片公司正在起诉Suno，指控其违反DMCA。
  article_id: 29f4ab98d1ecdbdf
- object_type: product
  name: Udio
  canonical_name: Udio
  url: https://udio.com
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到Suno的竞争对手Udio也被指控抓取YouTube数据。
  article_id: 29f4ab98d1ecdbdf
- object_type: product
  name: 404 Media
  canonical_name: 404 Media
  url: https://www.404media.co
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 黑客向404 Media提供了入侵细节和证据。
  - 文章说明报道来源为404 Media的调查报道。
  article_id: 29f4ab98d1ecdbdf
extract_result: success
---

The AI music generator Suno was hacked, according to a report from 404 Media.

The hacker told the publication that they used a supply chain attack in November to access an employee’s credentials, allowing them to then access source code showing how Suno allegedly scraped decades of audio from YouTube Music, Deezer, Genius, stock music libraries, and podcast RSS feeds.

Suno previously admitted that it trains its AI on “publicly available music files” on the open internet, arguing that it can train on copyrighted material under the fair use doctrine, a subjective carve-out of copyright law. But according to the major record labels actively suing Suno, it is illegal under the Digital Millennium Copyright Act (DMCA) to deliberately circumvent YouTube’s protections against data scraping; it also violates YouTube’s terms of service.

Udio, a competitor to Suno, has also been accused of scraping YouTube data. Google, the parent company of YouTube, faces similar allegations of copyright infringement from a variety of major book publishers.

The hacker reportedly accessed customer data including customer emails, phone numbers, and partial credit card numbers in Stripe.

Suno did not notify customers about the November 2025 breach and claims that this was a “limited security incident that was quickly contained.”