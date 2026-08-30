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
impact_score:
  score: 6.0
  reason: 评分依据：这是生成式视频赛道的一次重要但迭代型产品更新，而非范式转移。真正的技术亮点在于场景扩展的上下文窗口从 1 秒跃升至 10 秒（10 倍提升），配合
    10 秒增量、累计 40 秒时长，让长叙事一致性有了质的改善；首尾帧关键帧控制与 360p 快速草稿（提速 60%、成本 1/3）+ 4K 超分的能力组合，使生成式视频从'能生成'走向'可控制、可迭代、可交付'的生产级工作流，对开发者工具生态有实际价值。但另一方面，这仍是
    Omni 模型家族的版本升级，核心生成架构未见根本性突破，且 Veo/Sora/Runway/Kling 等竞品差距在收窄，40 秒累计时长仍限制长片场景。综合判断为局部竞争格局改变，够不上
    8 分以上的范式级事件，故给 6.0 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 生成式视频的成本阶梯与可控性——360p 草稿快速迭代、4K 超分交付，以及 10 秒上下文带来的角色/叙事一致性
hype_assessment:
  level: low
  reason: 判定依据：正文虽带有'production-ready''bring real-world reasoning'等 PR 措辞和客户案例展示，但核心内容是具体的功能规格与可验证指标（10
    秒上下文、40 秒累计、60% 提速、1/3 成本、4K 超分），并附带了可运行的 Gemini API 代码示例与文档入口。60% 提速声明有星号脚注说明口径，未出现'颠覆''革命性'等无实证的滥用词汇。整体是'有干货的发布'，仅存在轻微的营销包装，水分较低。
information_entropy: high
domain_disruption:
  technical_innovation: 场景扩展上下文从 1 秒提升到 10 秒并支持 10 秒增量累计 40 秒，是视频生成叙事连贯性的实质性工程突破；首尾帧关键帧插值实现相机环绕、无缝循环等精确镜头控制；360p/720p/4K
    分层分辨率与超分通道构成可调的成本-质量光谱。本质是围绕生成式视频的'可控性'和'生产成本'做架构级优化，让视频生成从一次性生成进化为可分镜迭代的工程化管线，而非提出全新生成范式。
  business_model: 以分辨率分层定价（360p 草稿为 720p 的三分之一）构建成本阶梯，把分镜/预览（previs）成本大幅拉低，使独立开发者和小型工作室也能负担
    AI 视频工作流，同时 4K 超分为专业制作留出高价值变现空间；通过 Agent Platform API 分发表明视频生成正成为 agent 工作流中的标准能力组件，视频生成从'独立创意工具'向'平台型基础设施服务'演进。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 从复利视角看，Omni 1.1 Flash 的核心价值不在模型本身（视频生成模型迭代极快、能力趋同），而在于三层结构性因素：其一，360p 草稿模式以
    720p 三分之一的成本将视频生成从'昂贵试错'变为'可高频迭代'，这种 draft-to-upscale 的成本架构是可持续的商业模式创新，有望沉淀为视频工作流的默认范式；其二，谷歌借助
    TPU 基础设施成本优势 + AI Studio/Gemini API/Agent Platform 分发，具备对独立视频模型创业公司持续的定价压制力；其三，10
    秒上下文场景扩展 + 角色一致性 + 4K 超分构成可控性提升，利于嵌入专业制作流程。但需警惕：视频生成赛道拥挤（Sora、可灵、Runway、Pika、Luma
    等），能力快速商品化，且谷歌在开发者心智上尚未形成类似 OpenAI/Anthropic 的粘性，场景扩展/首尾帧等控制能力正成为行业标配。综合判断为有潜力成为视频生成细分赛道的基础设施层，但护城河仍待持续验证，给予
    6.5 分。
value_capture_layer: foundation_model
moat_impact: strengthens_monopoly
key_beneficiaries:
- Google
- Google Cloud
- Gemini API 开发者生态
competitive_casualty:
- Runway
- Pika
- Luma AI
- 小型视频生成初创公司
market_opportunities:
- 创业者可基于 Gemini Omni 1.1 Flash 的场景扩展与首尾帧控制能力，面向广告与短视频制作团队开发自动化分镜预演工具（搭配 360p 草稿模式实现低成本快速迭代）
- 建议关注利用多模态视频参考实现角色一致性的能力，切入动画、游戏、虚拟主播等领域的角色绑定与数字替身创作工具赛道
- 360p 草稿（成本约为 720p 三分之一）+ 4K 超分的分层定价结构，为开发者构建'批量预渲染 + 精选成片'的媒体生产 SaaS 提供了成本优势
risk_matrix:
  regulatory: AI 生成内容披露义务趋严（欧盟 AI Act 透明度条款及各国深度伪造立法）；角色一致性与首尾帧功能可能被用于未经授权的肖像/版权视频生成，面临肖像权与著作权诉讼风险
  technological: 生成式视频技术迭代极快，40 秒累计时长、10 秒上下文等能力边界或很快被 Sora、可灵、Runway 等反超；'提速 60%''成本三分之一'为厂商自报数据，需实测验证
  competitive: 赛道竞争白热化：OpenAI Sora、快手可灵、Runway、Pika、Luma 多线夹击，谷歌自家 Veo 亦存在定位重叠；Flash
    低价档位或加剧 API 价格战，压缩商业变现空间
  ethical: 高保真生成视频放大深度伪造与虚假信息传播风险；视频参考与角色替换能力可被滥用制造未经同意的数字替身；影视/VFX/广告制作岗位面临自动化替代的就业冲击
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: product
  name: Google Flow
  canonical_name: Google Flow
  url: null
  positioning: Google Flow 是谷歌面向 AI Plus、Pro 与 Ultra 订阅用户开放的生成式创作应用，承载 Gemini Omni
    1.1 的视频生成能力，服务于订阅制用户的日常内容生产。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Google AI Plus 订阅用户
  - Google AI Pro 订阅用户
  - Google AI Ultra 订阅用户
  product_signal: Google Flow 集成 Gemini Omni 1.1 的视频生成能力，向全部 AI Plus、Pro 和 Ultra 订阅用户开放场景扩展等新功能。
  market_signal: 谷歌将 Omni 1.1 能力通过订阅制产品分发，表明生成式视频正成为订阅增值核心卖点，且面向全球用户开放。
  differentiation: 与 AI Studio、Agent Platform 面向开发者不同，Google Flow 以订阅用户为目标，提供低门槛的生成式视频创作体验。
  watch_reason: Google Flow 作为谷歌订阅生态中的生成式创作入口，其与 Gemini Omni 1.1 视频能力的集成程度，直接反映谷歌将前沿视频生成模型产品化的节奏与订阅策略，值得持续跟踪其功能演进。
  risk_notes:
  - Google Flow 的能力开放范围依赖谷歌订阅策略，存在功能调整、权限分级或定价变化的可能性。
  - 生成式视频赛道竞争激烈，Google Flow 需持续证明其在专业创作工作流中的不可替代价值，否则易被同类工具分流。
  score: 5.0
  article_ids:
  - 7d8f7d49cd6deab3
  evidence_snippets:
  - Omni 1.1 自发布之日起向全球所有 Google AI Plus、Pro 和 Ultra 订阅用户在 Google Flow 中开放使用。
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