---
title: Twitch streamers can now opt out from training Amazon’s AI
source: https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai
author:
- '[[Jay Peters]]'
published: '2026-08-12'
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
description: Twitch users can now opt out of allowing their content to be used to
  train Amazon's generative AI models. Opting out means that "your streams, VODs,
  clips, stream chats, and pictures and text on your channel" won't be used in "future
  training" of an Amazon AI model "whose purpose is to generate or synthesize text,
  [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: da3ea3dbc9d0910a
source_type: news_media
tldr: Twitch 新增隐私开关，允许用户选择不让自己的直播、回放、聊天等频道内容被用于训练 Amazon 的生成式 AI 模型，但其他 AI 辅助功能仍正常运行。
objective_summary: Twitch（隶属于 Amazon）在其设置中上线了“Training for Generative AI”开关，位于 Security
  and Privacy 标签页。用户关闭后，其直播、视频回放、剪辑、聊天、图片和文字将不会被用于未来旨在生成或合成文本、音频、图像、视频的 Amazon 生成式
  AI 模型训练；其他 AI 支持功能（如字幕、安全工具、推荐、赞助辅助）仍然有效。记者发现自己账号中该开关默认为开启，并已向 Amazon 求证默认策略。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies:
  - Twitch
  - Amazon
  technologies:
  - generative AI
  - AI-supported features
  key_people: []
key_logic_flow:
- Twitch 新增“Training for Generative AI”开关，允许用户退出将其频道内容用于 Amazon 生成式 AI 模型训练。
- 退出后，直播、视频回放、剪辑、聊天、图片和文字不会被用于未来旨在生成或合成文本、音频、图像、视频的 Amazon AI 模型训练。
- 其他 AI 支持功能（如字幕、安全工具、AutoMod、观众发现推荐、实时赞助辅助）在退出后仍可继续运行。
- 在他人直播间中发送的聊天内容是否被用于训练，由该直播间主播的退出偏好决定。
- 记者发现该开关在其账号中初始为开启状态，并已向 Amazon 确认这是否为默认设置。
object_mentions:
- object_type: product
  name: Twitch “Training for Generative AI” toggle
  canonical_name: Twitch Training for Generative AI toggle
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Twitch 用户在设置的 Security and Privacy 标签下可以看到新的 Training for Generative AI 开关，用于控制是否允许频道内容训练
    Amazon 的生成式 AI 模型。
  - Twitch 支持页面说明，关闭该开关后，直播、VOD、剪辑、聊天、图片和文字不会被用于未来 Amazon 生成式 AI 模型的训练。
  article_id: da3ea3dbc9d0910a
- object_type: model
  name: Amazon generative AI content models
  canonical_name: Amazon generative AI content models
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 开关说明中称允许频道内容用于训练 Amazon 的生成式 AI 内容模型，其用途是生成或合成文本、音频、图像或视频。
  - Twitch 支持页面表示，退出训练意味着这些内容不会被用于未来 Amazon 生成式 AI 模型的训练。
  article_id: da3ea3dbc9d0910a
- object_type: product
  name: AI-supported Twitch features
  canonical_name: Twitch AI-supported features
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Amazon 的开关说明列举，AI 支持的 Twitch 功能包括促进主播增长与变现的实时赞助活动辅助、观众发现推荐以及社区安全功能 AutoMod。
  - 其他 AI 支持功能如字幕和安全工具在退出生成式 AI 训练后仍可正常运行。
  article_id: da3ea3dbc9d0910a
extract_result: success
---

Twitch users can now opt out of allowing their content to be used to train Amazon’s generative AI models. Opting out means that “your streams, VODs, clips, stream chats, and pictures and text on your channel” won’t be used in “future training” of an Amazon AI model “whose purpose is to generate or synthesize text, audio, images, or video,” according to a Twitch support page.

# Twitch streamers can now opt out from training Amazon’s AI

Flip the new Twitch toggle if you don’t want your content to be used to train Amazon’s generative AI content models.

Flip the new Twitch toggle if you don’t want your content to be used to train Amazon’s generative AI content models.

Other “AI-supported” features like captions and safety tools will still function if you opt-out of generative AI training. However, if you participate in a chat on another person’s stream, “their opt-out preferences govern if that chat can be used for training,” Twitch says.

The “Training for Generative AI” toggle is present for me in Twitch’s settings under the Security and Privacy tab. It was toggled on when I found it, and I’ve asked Amazon if that’s the default.

Here’s the full text of Amazon’s description for the toggle:

Allow your channel content to train generative AI content models at Amazon. Turning this off does not opt you out of Twitch and Amazon using your channel content for other purposes described in the Twitch Privacy Notice, including using AI-supported Twitch features that benefit the community by facilitating streamer growth and monetization (such as real-time sponsorship campaign assistance), viewer discovery (such as recommendations), and community safety (such as AutoMod). Learn more


**Follow topics and authors**from this story to see more like this in your personalized homepage feed and to receive email updates.

## Most Popular

- Google’s Pixel 11 series pairs a little new hardware with a lot of new software
- Xbox Elite 3 prototype pad leaks with tiny built-in screen
- How Google’s new Pixel 11 phones compare to last year’s models
- The 7 biggest announcements of Google’s Pixel 11 launch
- The Pixel Tag is Google’s answer to the AirTag