---
title: Our decision on Cursor following its acquisition by SpaceX
source: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
author:
- '[[meetpateltech]]'
published: '2026-08-29'
created: '2026-08-29'
manifest_dates:
- '2026-08-29'
description: 'Article URL: https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
  Comments URL: https://news.ycombinator.com/item?id=49486172 Points: 504 # Comments:
  266'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dacd64b8ccca0019
source_type: community_discussion
tldr: OpenAI 官方宣布终止向被 SpaceX 收购的 Cursor 提供其模型，理由是马斯克旗下公司有违反合同与服务条款的前科；拟定 2026 年 11
  月 12 日关闭，期间不再提供包括 Astra 在内的未来模型，并为受影响开发者提供支持。
objective_summary: OpenAI 发布官方公告，宣布已通知 SpaceX 终止向其旗下 Cursor 提供 OpenAI 模型的合同，拟定关闭日期为
  2026 年 11 月 12 日。终止原因是 OpenAI 基于马斯克旗下公司（Twitter、xAI）先前违反合同与服务条款的历史，无法确信 SpaceX 会合规使用其技术。OpenAI
  选择在合同允许的最晚日期取消合作，此后不再向 Cursor 提供包括 Astra 在内的未来新模型，并承诺为受影响的开发者提供支持。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - OpenAI
  - SpaceX
  - Cursor
  - xAI
  - Twitter
  technologies:
  - Astra
  key_people:
  - Elon Musk
key_logic_flow:
- OpenAI 于今日通知 SpaceX，计划终止向 Cursor 提供 OpenAI 模型的合同，拟定关闭日期为 2026 年 11 月 12 日，并给出合同允许的最长通知期。
- 终止合作的直接原因是 OpenAI 无法确信 SpaceX 会遵守其服务条款，依据是马斯克旗下公司此前多次违反合同的历史。
- 马斯克在收购 Twitter（现已并入 SpaceX）后曾违反合同条款，并于今年早些时候在宣誓下承认 xAI（同样已并入 SpaceX）违反过 OpenAI 服务条款。
- OpenAI 与 Cursor 的定制协议允许在控制权变更后的有限时间窗口内取消合同，OpenAI 决定将取消日期推迟到合同允许的最晚时点。
- 随着 AI 能力增强，OpenAI 对其即将推出的模型 Astra 提出更高问责要求，决定在取消合同后不再向 Cursor 提供未来的新模型。
- OpenAI 与 Cursor 已合作近四年，表示尊重其团队与产品，并愿意为受影响的开发者提供支持。
object_mentions:
- object_type: product
  name: Cursor
  canonical_name: Cursor
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - OpenAI 已通知 SpaceX，计划在 2026 年 11 月 12 日终止向 Cursor 提供 OpenAI 模型的合同，并给出合同允许的最长通知期。
  - OpenAI 表示与 Cursor 合作近四年，尊重其团队与产品，深知最受影响的是依赖 Cursor 中 OpenAI 模型的开发者，并愿提供额外支持。
  article_id: dacd64b8ccca0019
- object_type: model
  name: Astra
  canonical_name: Astra
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - OpenAI 指出随着 AI 能力进步，其即将推出的新模型 Astra 的使用必须符合自身服务条款，这也是决定不再向 Cursor 提供未来模型的原因之一。
  article_id: dacd64b8ccca0019
extract_result: success
---

Today, we notified SpaceX that we intend to wind down our contract providing OpenAI models to Cursor, with a proposed shutoff date of November 12, 2026. To maximize the time that developers can retain access to our models through Cursor, we are giving the maximum notice provided by our contract. This decision was incredibly tough, as we care deeply about our models being broadly available for developers. We are making this choice because we cannot be confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts.

To work with a large partner like SpaceX, we typically rely on custom contracts to ensure compliance with our terms of service and that the integration provides for safety at scale. After Musk acquired Twitter, now part of SpaceX, the company __broke__(opens in a new window) the terms of our contract (alongside many others). Under oath earlier this year, Musk __admitted__(opens in a new window) that xAI, now also part of SpaceX, had violated OpenAI’s terms of service (terms which are similar to xAI’s own).

Our custom agreement with Cursor gives us a limited time window to cancel it after a change of control. As AI capabilities advance, we also have a new level of accountability to ensure our upcoming model, __Astra__, is being used in accordance with our terms. Given all of this, we’ve decided to hold the contract cancellation to the latest date we can while not providing future models to Cursor.

We’ve worked with Cursor for nearly four years and have enormous respect for their team, their product, and what they’ve built for the developer community. We know that the people most affected by this decision are the developers who rely on OpenAI models in Cursor. We care about their experience in this transition and we’re ready to go above and beyond to support them.