---
title: 'MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video'
source: https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui
author:
- '[[vblanco]]'
published: '2026-08-03'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: 'Article URL: https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui
  Comments URL: https://news.ycombinator.com/item?id=49155629 Points: 293 # Comments:
  85'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e5e903aa32caf5fe
source_type: community_discussion
tldr: MiniMax 发布开放权重视频模型 H3，ComfyUI 当日零点即原生支持。H3 接受文本、图像、视频或音频输入，生成带原生立体声、最高 2K、最长
  15 秒的视频，经优化可在 RTX 3060 上本地运行。
objective_summary: MiniMax 今日发布第三代视频模型 H3，这是其继 Hailuo 01、Hailuo 02 之后首个开放权重的版本，ComfyUI
  当日提供原生支持。H3 接受文本、图像、视频、音频输入，在同一 pass 中生成最高 2K、最长 15 秒、带原生立体声的视频，并支持文生视频、图生视频、首尾帧控制与参考视频运动迁移。ComfyUI
  团队将约 40% 的调制权重替换为等效查找表，配合 int8 convrot 量化与自定义内核，把内存占用从 123.6 GB 降至 42.5 GB，使模型可在
  RTX 3060 上本地运行。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - MiniMax
  - Comfy Org
  - Hugging Face
  technologies:
  - text-to-video
  - image-to-video
  - multimodal generation
  - int8 convrot quantization
  - VRAM offloading
  - stereo audio generation
  key_people: []
key_logic_flow:
- MiniMax 今日发布开放权重的第三代视频模型 H3，ComfyUI 于当日零点起提供原生支持。
- H3 接受文本、图像、视频或音频输入，可生成带原生立体声、最高 2K 分辨率、最长 15 秒的视频。
- 模型支持文生视频、图生视频、首尾帧控制、参考视频运动迁移与就地编辑等多种生成方式。
- ComfyUI 团队将约占 40% 参数的调制权重替换为功能等效的查找表，并配合 int8 convrot 量化与自定义内核降低显存峰值。
- 优化后模型内存占用由全精度的 123.6 GB 降至 42.5 GB，减少约 66%，结合动态 VRAM 卸载可在 RTX 3060 上本地运行。
- 用户需将 ComfyUI 更新到 0.30.0 或使用 Comfy Cloud，从模板库下载工作流，并从 HuggingFace 的 Comfy-Org/MiniMax-H3
  下载模型权重。
object_mentions:
- object_type: model
  name: MiniMax H3
  canonical_name: MiniMax H3
  url: https://huggingface.co/Comfy-Org/MiniMax-H3
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MiniMax 于今日发布开放权重的视频模型 H3，这是其继 Hailuo 01 和 Hailuo 02 之后首个开放权重的版本。
  - H3 支持输入文本、图像、视频或音频，可生成带原生立体声、最高 2K 分辨率、最长 15 秒的视频。
  - 经 ComfyUI 优化后，H3 的内存占用从全精度的 123.6 GB 降至 42.5 GB，可在 RTX 3060 上本地运行。
  article_id: e5e903aa32caf5fe
- object_type: project
  name: ComfyUI
  canonical_name: ComfyUI
  url: https://comfy.org
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - ComfyUI 于模型发布当天零点起原生支持 MiniMax H3，用户需要将 ComfyUI 更新到 0.30.0 版本才能使用。
  - ComfyUI 团队通过剪枝调制权重、int8 量化和自定义内核将 H3 的内存占用减少约 66%。
  article_id: e5e903aa32caf5fe
- object_type: product
  name: Comfy Cloud
  canonical_name: Comfy Cloud
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文章指出用户除了将 ComfyUI 更新到 0.30.0，也可以选择前往 Comfy Cloud 在云端运行 H3 模型。
  article_id: e5e903aa32caf5fe
- object_type: model
  name: Hailuo 01
  canonical_name: MiniMax Hailuo 01
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - H3 是 MiniMax 第三代视频模型，前两代产品分别为 Hailuo 01 和 Hailuo 02，H3 是首个开放权重的版本。
  article_id: e5e903aa32caf5fe
- object_type: model
  name: Hailuo 02
  canonical_name: MiniMax Hailuo 02
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - H3 是 MiniMax 第三代视频模型，前两代产品分别为 Hailuo 01 和 Hailuo 02，H3 是首个开放权重的版本。
  article_id: e5e903aa32caf5fe
extract_result: success
impact_score:
  score: 7.8
  reason: 先看定性依据：这是 MiniMax 首个开放权重的视频生成模型，且 ComfyUI 当日零点原生支持，属于大厂开放权重视频模型的关键节点。工程上
    ComfyUI 团队通过等效查找表替换约 40% 调制权重 + int8 convrot 量化，将显存需求从 123.6GB 压至 42.5GB（降幅 66%），使
    2K/15 秒/原生立体声的 omni-modal 视频模型首次能在 RTX 3060 消费级显卡上本地运行，这直接改写了本地视频生成与闭源 API 模型（Sora/Veo/Kling）的竞争格局，显著冲击闭源视频
    API 的定价权。但另一方面，该模型尚未经大规模社区实测验证、与同代开源视频模型（Wan、HunyuanVideo）的实际对比数据缺失，也远未达到 ChatGPT
    发布级别的行业范式转移，故评为 7.8 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 开源权重且能在 RTX 3060 上本地跑 2K 视频模型，外加同 pass 生成原生立体声音频
hype_assessment:
  level: medium
  reason: 先看措辞：这是 ComfyUI 官方博客，使用 'next-generation'、'powerful' 等推广性表达，属于自家生态的宣传口径。再看实料：显存压缩数字（123.6GB→42.5GB）、int8
    量化方案、部署门槛等核心指标具体且可复现，40% 调制权重替换为查找表这一优化路径也有清晰工程描述。但 'omni-modal'、'collapses five
    tasks into one model' 等表述存在能力夸张，且查找表替换/量化对画质与音频质量的实际损失尚无第三方评测佐证，故判定为中等包装而非概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 单模型在同一前向中接受文本/图像/视频/音频输入并输出带原生立体声的 2K 视频，实现真正的跨模态上下文理解；工程上
    ComfyUI 用功能等效查找表替换约 40% 调制权重、配合 int8 convrot 量化与自定义内核，把显存从 123.6GB 压缩到 42.5GB，首次让开放权重视频大模型在消费级
    GPU 上可本地部署，这是本地视频生成从'实验室'到'个人电脑'的关键一步。
  business_model: MiniMax 以开放权重策略入局，直接冲击 Sora/Veo/Kling 等闭源 API 视频生成按量计费模式——用户可免费本地跑而无需按秒付费；同时强化
    ComfyUI 作为开源视频模型事实分发入口的地位，推动视频生成商业模式从'闭源 API 卖算力'向'开源模型 + 工具链/云服务增值变现'迁移。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 评估逻辑：其一，H3 是 MiniMax 首个开放权重视频模型，开放权重+Day-0 ComfyUI 生态接入会带来复利效应——社区围绕权重构建工作流、LoRA、二次训练，形成超越单一模型版本迭代的网络效应，这是可持续积累的资产。其二，ComfyUI
    的工程优化（约 40% 调制权重替换为查找表、int8 convrot 量化、内存占用从 123.6GB 降至 42.5GB）验证了一条可复制的消费级显卡本地推理路径，这种'降本方法论'本身具有长期基础设施价值，能沉淀为行业通用实践。其三，'同
    pass 生成原生立体声音频+视频'是多模态生成的真实技术差异化，可作为长期壁垒。但需要扣分：视频生成赛道迭代极快（Wan、Kling、HunyuanVideo
    等同期竞争），MiniMax 作为中国公司的地缘与出海合规不确定性会限制其全球生态建设速度；且开放权重模式下直接变现有限，价值兑现依赖企业级/云端服务。综合判断：有潜力成为开放视频生成赛道的细分基础设施，但需持续验证，故给
    7.5 分。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- MiniMax
- ComfyUI
- Hugging Face
- NVIDIA
- 独立创作者与小型AI工作室
competitive_casualty:
- Runway
- Pika
- Luma Labs
- 闭源视频生成API服务商
- 传统影视后期SaaS
market_opportunities:
- 开放权重加消费级显卡（RTX 3060）可本地运行的组合，让独立创作者与小团队能以极低成本搭建本地视频生成管线，建议关注基于 ComfyUI 的影视预告片、广告物料与批量短视频生产服务
- 原生立体声与画面同 pass 生成，将音频与视频两条传统管线合并，可催生一站式口播配音、音乐可视化与视频配乐自动化的产品机会
- 参考视频运动迁移与就地编辑能力贴合专业 VFX/后期迭代场景，开发者可围绕 H3 开发 ComfyUI 自定义节点、高级工作流模板与面向工作室的付费插件
risk_matrix:
  regulatory: 开放权重视频模型叠加参考音频声纹迁移，大幅降低深度伪造门槛，面临欧盟 AI Act 生成媒体标注、来源披露与内容真实性追溯要求；MiniMax
    为中国公司，其权重在全球分发可能受地缘政治与出口管制不确定性影响
  technological: 视频生成赛道迭代极快，Sora、Veo、Kling 等闭源模型与 Hunyuan Video、LTX 等开源模型持续更新，H3 的开放权重优势窗口有限；ComfyUI
    将约 40% 调制权重替换为查找表并做 int8 量化，可能在高动态场景带来画质与音质损失
  competitive: 巨头与开源社区密集入局，开源视频模型与闭源云服务价格战激烈，H3 作为 MiniMax 首个开放权重版本缺乏生态沉淀，先发优势可能被快速侵蚀
  ethical: 开放权重降低深度伪造与声音克隆的技术门槛，参考音频可迁移真人声纹，存在未经同意生成拟真内容、色情/虚假信息滥用及隐私侵犯风险；开放权重模型难以被事后约束或收回
  additional:
  - 模型优化后仍需约 42.5GB 显存，RTX 3060 档位运行依赖动态 VRAM 卸载，实际生成速度与长视频稳定性可能低于宣传预期
  - 权重托管于 HuggingFace，若遭遇政策审查或平台下架，依赖该模型的本地工作流将面临供应链中断风险
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Comfy Cloud
  canonical_name: Comfy Cloud
  url: null
  positioning: Comfy Cloud 是 ComfyUI 的云端工作流运行平台，让用户无需高性能本地硬件即可运行 H3 等重模型。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 本地硬件不足的 ComfyUI 用户
  - 需要即开即用云端算力的视频创作者
  product_signal: Comfy Cloud 提供 H3 的云端运行路径，与本地 ComfyUI 构成互补，是官方推荐的两种使用方式之一。
  market_signal: 开源视频模型普遍依赖高显存，Comfy Cloud 的出现反映重模型上云按需获取算力的市场趋势。
  differentiation: 相比本地部署需下载权重并配置显存，Comfy Cloud 强调开箱即用，降低创作者的上手门槛。
  watch_reason: Comfy Cloud 是观察开源视频模型云端商业化的重要样本，其能否稳定承载 H3 这类 42.5 GB 显存级别的重模型，将直接影响创作者对云端工作流平台的采用信心与付费意愿。
  risk_notes:
  - 文章对 Comfy Cloud 的提及仅一句带过，缺乏性能、定价与可用性等具体信息支撑。
  - 云端运行 H3 的实际体验与成本控制尚待验证，存在与服务承诺不符的不确定性。
  score: 4.0
  article_ids:
  - e5e903aa32caf5fe
  evidence_snippets:
  - 文章指出用户除了将 ComfyUI 更新到 0.30.0，也可以选择前往 Comfy Cloud 在云端运行 H3 模型。
---

# MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video

### An open-weights omni-modal video model with real stereo sound and 2K output — this powerful model is greatly optimized in ComfyUI and can run locally on a 3060.


MiniMax H3 dropped today with open weights, and it’s natively supported in ComfyUI as of this morning. Day zero.

This is a next-generation open-weights video model. Feed it text, images, video, or audio and it generates video with real stereo sound, up to 2K, up to 15 seconds a clip. It is MiniMax’s third-generation video model, following Hailuo 01 and Hailuo 02, and the first the company has released with open weights.

## Model Highlights

**Text-to-video**— prompt only.**Image-to-video**— bring an image to life.**First-and-last-frame**— control the opening frame, the closing frame, or both, and let the model fill in the rest.**Reference-to-video**— supply reference images, video, or audio and carry a subject, a motion, or a voice through the clip.

Output runs to 2K and up to 15 seconds. Audio is generated with the video in the same pass, in stereo, not bolted on afterward.

#### Multimodal context understanding

This is the capability MiniMax leads with, and it’s what collapses five separate tasks into one model. Real work rarely draws on one modality. H3 takes images, audio, and video together and resolves them against a prompt that explains how they relate. Describe the relationship between your inputs and the shot you want, and the model handles the cross-modal work itself.

#### Native stereo audio

Audio is a property of the model, not a post-process. Every audio output is native stereo.

#### Editing and motion transfer

Motion transfer is the one that matters most for graph work. A reference video can supply movement — a camera move, a performance, a cutting rhythm — while the subject and style come from elsewhere. Combined with in-place editing, that means iterating on a shot.

## Example Outputs

```
Bold comic-book ink style, heavy linework, red and blue-black palette, night city. Use <Picture 2> and <Picture 1> as reference frames and <Audio 1> exactly as it is.
CUT 1: top-down view of the little boy superhero on the rooftop — red cape fluttering in the wind, hands planted on his hips, freckles and a cocky grin as he looks straight up into the camera. The camera slowly descends toward him as he delivers his line — as he speaks, comic-book graphic overlay text word by word in sync with his voice: "GET READY TO" - "MEET" — "YOUR" — "MAKER" — huge jagged comic lettering, white with heavy black outlines and red drop shadows, tilted at scrappy angles, until the three words hang stacked in the air above him between his face and the lens.
TRANSITION: a violent WHIP PAN off the rooftop that SMEARS the floating words away with it, motion-streaked —
CUT 2: low hero angle on the colossal black mech-kaiju towering over the skyline as it rears back and unleashes a GIANT terrifying ROAR — jaws wide with fangs, red eyes and chest-core flaring blinding bright, blue lightning arcing off its head, the roar's shockwave rippling dust and rattling windows down the buildings, comic-style speed-lines and ink splatter bursting from the impact of the sound. It leans INTO the camera as the roar peaks. Hold on the roar.
```


```
Editorial tech product film. The transparent gaming mouse from <Picture 1> in its original scene: a pitch-black studio void with a dark, subtle reflective surface, lit by dramatic duotone vibrant blue and warm neon orange rim lighting, deep soft shadow falloff into pure black. Monochromatic dark palette with electric blue and amber accents. Material motif: glowing internal metallic micro-components and glossy acrylic refractions. The environment is constant throughout.
SHOT 1: The scene opens exactly on image 1, the mouse resting confidently on the dark surface; the blue and orange lights slowly pulse brighter, refracting deeply through the transparent acrylic shell as the camera executes a slow, deliberate push-in to reveal the intricate circuitry.
SHOT 2: Cut to an extreme macro profile of the ridged scroll wheel and layered internal micro-components; the camera glides slowly along the side as a sharp beam of warm orange light sweeps across the metallic textures, contrasting perfectly against the deep blue ambient glow.
SHOT 3: Cut to a low-angle beauty shot: the mouse levitates weightlessly a few centimeters above the dark reflective surface, rotating in a slow, precise orbit; the duotone lighting flares gently along the glassy transparent edges before fading slowly into a sleek silhouette.
Audio: deep pulsing sub-bass room tone, sharp tactile mechanical clicks, a sweeping glassy whoosh on cuts, and a rising electronic swell that resolves to near-silence on the final fade.
```


```
High-fashion editorial film, luxurious slow motion throughout, soft gradient studio sky.
MUSIC & SFX: a cinematic score fusing deep taiko drums, shimmering koto plucks and modern sub-bass drives the film
SHOT 1: beside her, the mask hangs BROKEN — shattered into the floating shard formation of <Picture 2>, every kintsugi piece suspended and slowly rotating in place, the gold seams between them dim and waiting. She turns her eyes to it.
SHOT 2: THE ASSEMBLY, with enormous energy — the gold seams IGNITE, arcs of molten light leaping shard to shard like welding fire, and the pieces snap together one by one, accelerating from slow to rapid-fire, each snap flaring gold, molten droplets spinning off, the surrounding liquid ribbons shuddering with shockwave ripples — until the final shard slams home and the whole mask fuses, its kintsugi veins blazing.
SHOT 3: the golden dragon of <Picture 3> SWOOPS through the frame in one huge serpentine fly-through — red glass antlers first, its coils wrapping the space around her and the mask, scales throwing golden light, its wake dragging the crimson liquid into a spiral behind it.
SHOT 4: in the dragon's wake the mask magnetically RIPS across the air onto her face — a fast, hard, perfectly straight pull — seating with a deep flare as every gold crack lights, and glowing kintsugi veins spread from the mask's edge down her neck and across the sunset jacket, embroidery igniting thread by thread.
SHOT 5: she descends and lands softly ON the dark liquid wave, snapping into a poised warrior stance and holding it like a lookbook frame — the dragon coiled behind her shoulder, both liquids spiraling upward around her into a double helix. Held editorial poster frame as the camera settles.
Use <Picture 1>, <Picture 2>, <Picture 3> as reference images.
```


```
Vibrant fisheye product commercial, hyper-saturated summer light, the woman from <Picture 1> in a yellow raincoat crouched by a jungle waterfall holding a rainbow-gradient soda can toward the lens, condensation dripping.
MUSIC: an upbeat tropical house track drives the entire film — punchy kick drum, bright steel-drum plucks, warm bass groove.
CUT 1 : the fisheye hero frame — as she looks into the lens, GIANT BOLD TYPOGRAPHY stamps across the background behind her, one word per beat: "STAY" then "HYDRATED" — massive clean white block letters spanning the whole scene, curving with the fisheye distortion, sitting behind her but in front of the waterfall. She reaches her opposite hand towards the can and hooks a finger under the tab.
TRANSITION: extreme close-up of the tab — it OPENS with a crisp CLICK-hiss, and exactly on the click the fisheye lens iris shutters closed to black, like a camera blinking.
CUT 2: the iris reopens on a new POV — the can EXTREMELY distorted in the foreground, huge and warped by the fisheye, she smiles and dumps the liquid out of the can onto the floor, droplets scattering weightlessly, sunlight refracting rainbow through the stream, the waterfall soft behind her.
TRANSITION: she lowers the can and one fat droplet falls toward the lens, filling the frame —
CUT 3: through the droplet into the final wide: the rainbow can floating upright and serene in the turquoise waterfall pool, label facing camera, bobbing gently in the mist, the waterfall thundering softly behind — and "STAY COMFY" shimmering as a reflection on the water's surface beside it. Hold the product hero frame.
Crisp, joyful, premium product-ad energy. Fisheye distortion in every shot.
```


## Optimized for local inference in ComfyUI

Getting H3 to run well on consumer hardware took significant machine learning engineering. We found that the model's modulation weights (~40% of the total parameters) could be pruned and replaced with a functionally equivalent lookup table, dramatically shrinking the memory footprint with no loss in output quality.

On top of that, the weights ship with an accurate and efficient int8 convrot quantization, and custom kernels reduce the peak VRAM use during inference.

The result gives a total memory footprint **reduced by 66%, from 123.6 GB in full precision to 42.5 GB** with the smallest models variants. Combining this with our dynamic VRAM offloading enables a next-generation 2K video model to run locally on a GPU like the RTX 3060.

## Getting started

Update ComfyUI to the latest version

**0.30.0 or go to Comfy Cloud**Download the workflows below, or find them in the template library.

Follow the note in the workflow to download the models and save them in the correct model directory.

Write your prompt, connect any frame or reference inputs, and run.


Model weights: 🤗 Comfy-Org/MiniMax-H3

As always, enjoy creating!