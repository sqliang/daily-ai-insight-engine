---
title: John Carmack on Fabrice Bellard
source: https://twitter.com/ID_AA_Carmack/status/2064095424420487226
author:
- '[[apitman]]'
published: '2026-06-16'
created: '2026-06-16'
description: 'https://xcancel.com/ID_AA_Carmack/status/2064095424420487226 Comments
  URL: https://news.ycombinator.com/item?id=48550779 Points: 236 # Comments: 143'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 285efcbfbbf2b106
source_type: community_discussion
tldr: id Software 创始人 John Carmack 公开称赞法国工程师 Fabrice Bellard 是比他更优秀的程序员。Bellard 30
  年间编写的视频流媒体和虚拟机代码支撑了 YouTube、Netflix、TikTok 等全球互联网服务，但公众知名度极低。
objective_summary: John Carmack 在 Twitter 上发表了对法国软件工程师 Fabrice Bellard 的高度评价。Carmack
  认为 Bellard 在整体编程能力上优于自己。文章指出 Bellard 在过去 30 年中编写了支撑 YouTube、Netflix、TikTok 等全球主流视频平台的流媒体基础代码，以及被广泛使用的虚拟机软件，但他的名字在大众中几乎不为人知。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - YouTube
  - Netflix
  - TikTok
  - ByteDance
  technologies:
  - QEMU
  - FFmpeg
  - libavcodec
  key_people:
  - John Carmack
  - Fabrice Bellard
key_logic_flow:
- John Carmack 公开表示他钦佩 Fabrice Bellard，并认为 Bellard 的整体编程能力几乎肯定超过自己。
- Fabrice Bellard 是一位居住在巴黎的法国软件工程师，已持续编写软件长达 30 年。
- Bellard 编写的核心代码支撑了 YouTube、Netflix、TikTok 等全球主流视频平台的流媒体播放功能。
- Bellard 还编写了被广泛使用的虚拟机软件。
- 尽管 Bellard 的软件被全球互联网广泛依赖，但他的名字在大众层面几乎不为人知。
extract_result: success
object_mentions:
- object_type: project
  name: FFmpeg
  canonical_name: FFmpeg
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出 Fabrice Bellard 编写了支撑 YouTube、Netflix、TikTok 每一条视频流的底层代码，即被广泛使用的视频编解码库 FFmpeg/libavcodec。
  article_id: 285efcbfbbf2b106
- object_type: project
  name: QEMU
  canonical_name: QEMU
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章提到 Fabrice Bellard 编写了驱动所有虚拟机的底层代码，即他所创建的开源虚拟化软件 QEMU。
  article_id: 285efcbfbbf2b106
---

I admire Fabrice Bellard. He is almost certainly a better overall programmer than I am.

A French engineer who lives quietly in Paris has spent 30 years writing software that the entire internet now runs on without knowing his name.
He wrote the code that streams every YouTube video, every Netflix show, every TikTok clip. He wrote the code that runs the virtual