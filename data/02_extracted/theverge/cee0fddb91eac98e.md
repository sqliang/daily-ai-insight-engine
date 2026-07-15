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
tldr: 同人小说社群发布AO3皮肤插件检测Claude生成的文本，引发点名羞辱争议
objective_summary: 2025年6月29日，匿名X账号@heatedrivalryai发布了一款AO3皮肤插件，通过检测Claude注入的代码标识符来识别AI生成的同人作品。该插件被用于公开点名和羞辱被标记的作者，引发对检测方法有效性和伦理的争议。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - Archive of Our Own (AO3)
  technologies:
  - Claude
  - ChatGPT
  key_people:
  - '@heatedrivalryai'
key_logic_flow:
- 2025年6月29日，匿名X账号@heatedrivalryai发布了一款AO3皮肤插件，通过检测Anthropic Claude注入的HTML代码标识符'font-claude-response-body'来识别AI直接粘贴的同人作品。
- 该皮肤插件在检测到Claude生成的文本痕迹时将整个页面背景变为红色，以此做出视觉警示。
- 经验证，该工具仅能检测直接从Claude聊天界面复制粘贴到AO3编辑器的文本，改写后或使用ChatGPT等其他AI工具生成的内容无法被识别。
- 同人小说社群迅速围绕该工具展开行动，对被标记的作者进行公开点名和羞辱，尽管工具创建者声称其意图是展示系统有效而非制造不信任环境。
- 该事件揭示了同人创作社群对生成式AI的强烈抵触情绪，以及AI使用检测手段在准确性和伦理上引发的深层分歧。
extract_result: success
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