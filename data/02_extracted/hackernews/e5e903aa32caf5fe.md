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