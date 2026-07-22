---
title: The fanfiction community is at war with AI — and itself
source: https://www.theverge.com/tech/960854/ai-fanfiction-ao3-claude-detector
author:
- '[[Jess Weatherbed]]'
published: '2026-07-04'
created: '2026-07-05'
description: Over the past week, a new fanworks movement has kicked off, with the
  aim to root out authors using generative AI. But the detection methods being implemented
  are questionable, and any fanfic writer could be caught in the crossfire. Broad
  distaste around the use of Claude, ChatGPT, and other AI tools has long been a [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cee0fddb91eac98e
manifest_dates:
- '2026-07-05'
source_type: news_media
tldr: 匿名账户@heatedrivalryai为Archive of Our Own (AO3)发布了一款检测皮肤工具，通过识别Claude自动注入的'font-claude-response-body'代码标记来判定AI生成的同人作品，引发社区内关于检测方法可靠性和误伤风险的广泛争议。
objective_summary: 2025年6月29日，匿名X账户@heatedrivalryai为同人作品平台AO3发布了一款皮肤工具，该工具利用Claude在粘贴文本时自动注入的'font-claude-response-body'代码标记来检测AI生成内容。实测显示直接从Claude粘贴到AO3的内容会触发全屏红色背景警告，而经手动处理的相同文本则不会触发。该工具发布后同人社区迅速将其用于公开点名和指责被标记的创作者，引发了关于AI检测方法可靠性、误伤风险以及社区信任的争议。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Archive of Our Own (AO3)
  technologies:
  - Claude
  - ChatGPT
  - generative AI
  key_people: []
key_logic_flow:
- 2025年6月29日，匿名X账户@heatedrivalryai发布了一款用于AO3平台的皮肤工具，宣称可检测由Claude生成的同人作品。
- 该皮肤通过识别Claude在粘贴文本时自动注入的'font-claude-response-body'代码标记来判断内容是否由AI生成。
- 实测验证显示直接从Claude聊天界面粘贴到AO3编辑器中的文本会触发该皮肤显示全屏红色背景警告，而手动复制的相同文本则不会触发。
- 该工具的发布导致同人社区迅速动员起来，公开点名和指责被标记的创作者，引发了关于AI检测方法误伤风险和社区信任的讨论。
- 皮肤创建者称其目的是保护同人社区的'人性元素和创造力火花'，而非制造不信任环境或针对特定用户。
extract_result: success
object_mentions:
- object_type: project
  name: AO3 Claude detector skin
  canonical_name: AO3 Claude detector skin
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该皮肤由匿名X账户@heatedrivalryai发布，通过识别Claude注入的'font-claude-response-body'代码标记来检测AI生成内容。
  - 当用户访问包含该代码的页面时，皮肤会将整个背景变为红色，以此提示作品可能由Claude生成。
  - 从Claude直接粘贴到AO3编辑器的内容会触发皮肤检测，而手动粘贴的相同文本则不会触发，表明检测依赖原始格式标记。
  article_id: cee0fddb91eac98e
- object_type: product
  name: Archive of Our Own (AO3)
  canonical_name: Archive of Our Own (AO3)
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - AO3是流行的同人作品存储库，该检测皮肤专为AO3平台设计并以AO3自定义皮肤形式运行。
  article_id: cee0fddb91eac98e
- object_type: product
  name: Claude
  canonical_name: Claude
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Claude生成的回复在直接粘贴到AO3时会被自动注入'font-claude-response-body'代码标记，这正是该检测工具识别的关键痕迹。
  article_id: cee0fddb91eac98e
---

Over the past week, a new fanworks movement has kicked off, with the aim to root out authors using generative AI. But the detection methods being implemented are questionable, and any fanfic writer could be caught in the crossfire.

# The fanfiction community is at war with AI — and itself

Readers are scrambling to develop ways to detect whether generative AI was used to write fanworks. The results are questionable.

# The fanfiction community is at war with AI — and itself

Readers are scrambling to develop ways to detect whether generative AI was used to write fanworks. The results are questionable.

Broad distaste around the use of Claude, ChatGPT, and other AI tools has long been *a thing* in creative communities, including the world of fanfiction. Readers and writers have passed around tips for spotting supposedly AI-generated works, citing anything from em dashes to the broad concept of purple prose. But on June 29th, an anonymous X account called @heatedrivalryai promised a seemingly more reliable solution. It posted a skin — similar to an extension — for the popular fanfic repository Archive of Our Own (AO3) that would purportedly identify coding artifacts left behind by Anthropic’s Claude bot.

“When a Claude-generated response is pasted directly into AO3 from Claude, the text is wrapped by a Claude-injected code ‘font-claude-response-body,’” said the @heatedrivalryai account. “Its presence indicates the use of Claude definitively.” When a user visits a page (like a work of fanfic) with this code, the skin turns the entire background red.

Several test posts have been published to AO3 that allow users to check if it works. The screen immediately turned red when I tested the skin against these examples myself, and I published a Claude-generated short story to run my own experiment just in case. The red screen appeared when I directly pasted from the chatbot into the editor and vanished if I pasted text (including the exact same generated story) that didn’t come straight from Claude.

The Claude detector post was accompanied by examples of fanfic where the artifacts were spotted, which the anonymous creator said was meant to demonstrate the system works, not “create an environment of mistrust or accuse particular users.” But fanfic communities have quickly mobilized to publicly name and shame writers whose published works were flagged by the tool, and its creator certainly doesn’t consider AI a positive thing. “Fandom is a uniquely connective, collaborative space. It thrives on the human element and the creative spark which drives it and feeds off it,” they said. “If we unknowingly allow AI to corrupt these spaces, what will be left of them?”