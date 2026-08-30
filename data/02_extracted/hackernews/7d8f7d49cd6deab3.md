---
title: Gemini Omni 1.1 Flash
source: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
author:
- '[[saretup]]'
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
description: 'Article URL: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
  Comments URL: https://news.ycombinator.com/item?id=49467922 Points: 248 # Comments:
  186'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7d8f7d49cd6deab3
source_type: community_discussion
tldr: 谷歌发布 Gemini Omni 1.1 Flash，为生成式视频新增场景扩展（最长累计 40 秒）、首尾帧指定、360p 快速草稿与 4K 超分等创意控制能力，通过
  Gemini API 在 Google AI Studio 面向开发者开放。
objective_summary: 谷歌发布 Gemini Omni 1.1 Flash，这是 Omni 系列模型的 1.1 版本更新，新增多项生成式视频创意控制能力。模型可分析最多
  10 秒的先前视频上下文，以 10 秒为增量将场景扩展至累计 40 秒；支持指定首尾帧生成连续视频；360p 草稿模式生成速度最高提升 60% 且成本为 720p
  的三分之一；输出可超分至 1080p 或 4K。多模态输入中可引用最多三秒视频以保持角色一致性。该模型通过 Gemini API 在 Google AI Studio
  提供，企业可通过 Agent Platform API 使用，并向 Google AI Plus、Pro、Ultra 订阅用户在 Google Flow 中开放。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - Google
  technologies:
  - Gemini Omni 1.1 Flash
  - Gemini API
  - Agent Platform API
  - Google Flow
  key_people: []
key_logic_flow:
- 谷歌发布 Gemini Omni 1.1 Flash，为开发者带来一套新的创意控制与生成式视频能力，通过 Gemini API 在 Google AI Studio
  中提供。
- 场景扩展功能让模型可分析最多 10 秒的先前视频上下文，并以 10 秒为增量将视频扩展至累计 40 秒长度。
- 新模型支持用户指定视频首尾关键帧，在两个关键帧之间生成连续视频，适用于相机环绕、变焦过渡与无缝循环片段。
- 360p 分辨率下视频草稿生成速度最高比标准 720p 快 60%，成本仅为后者的三分之一，便于快速原型与分镜迭代。
- 模型支持将输出升级至 1080p 或 4K 分辨率，并可在多模态输入中引用最多三秒的视频参考以保持角色一致。
- Omni 1.1 面向企业通过 Agent Platform API 开放，同时向 Google AI Plus、Pro 和 Ultra 订阅用户在 Google
  Flow 及 Gemini 应用中提供。
object_mentions:
- object_type: model
  name: Gemini Omni 1.1 Flash
  canonical_name: Gemini Omni 1.1 Flash
  url: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 谷歌发布 Gemini Omni 1.1 Flash，为生成式视频带来场景扩展、首尾帧指定、360p 快速草稿和 4K 超分等一系列创意控制能力，使其适用于专业生产场景。
  article_id: 7d8f7d49cd6deab3
- object_type: product
  name: Google AI Studio
  canonical_name: Google AI Studio
  url: https://aistudio.google.com/
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Omni 1.1 通过 Google AI Studio 中的 Gemini API 向开发者开放，开发者可直接在 AI Studio 中试用新的生成式视频控制能力。
  article_id: 7d8f7d49cd6deab3
- object_type: product
  name: Gemini API
  canonical_name: Gemini API
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 开发者在 Gemini API 中调用 gemini-omni-1.1-flash 模型时，可通过 interactions.create 接口并指定 previous_interaction_id
    来实现视频场景扩展。
  article_id: 7d8f7d49cd6deab3
- object_type: product
  name: Gemini Enterprise Agent Platform
  canonical_name: Gemini Enterprise Agent Platform
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 企业可以通过 Agent Platform API 直接使用 Gemini Omni Flash，文中展示的客户案例表明该模型已被投入实际生产流程。
  article_id: 7d8f7d49cd6deab3
- object_type: product
  name: Google Flow
  canonical_name: Google Flow
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Omni 1.1 自发布之日起向全球所有 Google AI Plus、Pro 和 Ultra 订阅用户在 Google Flow 中开放使用。
  article_id: 7d8f7d49cd6deab3
extract_result: success
---

# Gemini Omni 1.1 Flash lets you build with more control

Today, we’re introducing Gemini Omni 1.1 Flash, a new suite of creative controls and generative video capabilities to support developers. Gemini Omni brought real-world reasoning to generative creation, and today’s updates make Omni 1.1 production-ready for professional use via the Gemini API in Google AI Studio.

Whether you’re building generative video workflows, creative tools, or media editing software, these updates make generative video more controllable, faster to iterate on, and polished for real-world deployment. Here’s a look at what’s new:

## Extend scenes for longer storytelling

Scene extension allows you to take an existing video and continue generating footage seamlessly from where it left off.

With Omni 1.1, the model can now analyze up to 10 seconds of prior context — a leap from previous models that only referenced the final second. The result is improved visual consistency and narrative adherence, letting you build longer stories or branch into new creative directions. You can extend videos in 10-second increments up to a total cumulative length of 40 seconds.

Here’s how you can extend your scene with the Gemini API:

```
from google import genai
client = genai.Client()
interaction = client.interactions.create(
model="gemini-omni-1.1-flash",
previous_interaction_id=previous_video_interaction.id,
input=[
{"type": "text", "text": "Continue the scene."}
],
response_format={
"resolution": "360p",
},
)
```


## Specify first and last frames

Achieve smooth transitions and camera movements by specifying the starting and ending frames of a shot. Omni 1.1 generates continuous video between two keyframes, making it ideal for complex camera orbits, zoom transitions, or seamless looping clips.

Prompt 1: A close-up low-angle shot of a stylish drummer in a beige suit playing a red drum kit in a grand hall transitions as the camera whip-pans to the side, revealing an older saxophonist playing alongside a ballet dancer spinning in a white outfit under soft purple stage lights. One continuous shot, no jump cuts.

Prompt 2: The camera zooms into the TV screen, where we see the same woman and the same scene from the beginning. Seamless video. One continuous shot, no jump cuts.

## Draft videos more efficiently in 360p

Generate lightweight previews in 360p resolution up to 60% faster* and at a third of the cost compared to Omni 1.1’s standard 720p resolution. This is helpful for rapid prototyping, storyboard iteration, and quick rendering in developer platforms.

*Up to 60% faster generation based on system throughput of 360p vs. 720p resolution

Prompt: A microscopic view of iridescent marine diatoms, displaying intricate, glass-like silica shells with breathtaking natural symmetry. The colors range from deep volcanic amber and warm copper to vibrant turquoise and violet, mimicking the rich palette of earth and ocean. Tiny, delicate structures glow softly against a clean dark field background. High-fidelity scientific imaging, sharp details, organic textures, micro-photography. Maintain the microscope lens effect throughout the entire video.

## Upscale up to 4K resolution

Generate polished, high-resolution 1080p or 4K outputs that are ready for professional production with Omni 1.1.

Prompt 1: Fish swimming, tracking shot

Prompt 2: A little chipmunk darting out of the woods from the left side of the screen and sniffing the air inquisitively before darting out of frame on the right side

Prompt 3: Cinematic macro close-up of vibrant golden-orange Japanese maple leaves on a delicate branch, gently rustling and swaying in a soft, rhythmic autumn breeze. Sunlight filters through the translucent foliage, creating a warm, glowing effect. Shallow depth of field, dreamy bokeh background, hyper-detailed textures, photorealistic, 4k.

## Add video references in your multimodal input

Reference up to three seconds of video when crafting your scene, allowing you to maintain visual context and character consistency based on video references.

Prompt: Use the three uploaded videos of dancers and replace them with the provided characters. Have them perform their individual dances from the reference videos, all together in the large, open space from the provided image.

The dog character dog.png should do the classical dance from dance3.mp4. The octopus octo.png should do the hip hop dance from dance1.mp4, and the bear bear.png should do the breakdance from dance2.mp4. The final result should be one continuous shot with no scene cuts.

## Inspiring concepts for what you can build

Here are a few ideas showing how developers can put these new capabilities into action across custom tools and creative workflows.

## See how customers are putting Omni Flash in production

Our customers are already driving real-world production with Gemini Omni Flash via the Agent Platform API. Explore the videos they've created and hear about how they are using the model below.

## Build with Gemini Omni 1.1 Flash Today

Pricing table for Gemini Omni 1.1 Flash.

Omni 1.1 is rolling out across the Google developer ecosystem:

**Start building in Google AI Studio:**Try out Omni 1.1 directly in Google AI Studio.**Build on Gemini Enterprise Agent Platform**: Enterprises can build with Omni 1.1 directly via Agent Platform API.**Explore the developer documentation:**Check out the official documentation, the cookbook and prompting guides to learn how to integrate scene extensions, video references, and upscaling into your applications.

Omni 1.1 is also available to all Google AI Plus, Pro and Ultra subscribers globally in Google Flow, starting today. Scene extension is available to all Google AI Plus, Pro and Ultra subscribers globally in the Gemini app.