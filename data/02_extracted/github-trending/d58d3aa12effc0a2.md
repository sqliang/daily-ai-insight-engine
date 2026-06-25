---
title: HKUDS/ViMax
source: https://github.com/HKUDS/ViMax
author: []
published: ''
created: '2026-05-21'
description: '"ViMax: Agentic Video Generation (Director, Screenwriter, Producer,
  and Video Generator All-in-One)" ViMax: Agentic Video Generation 🚨 Current Video
  Generation Limitations: ❌ Limited to Short Clips - Most AI tools generate only seconds
  of footage. ❌ Consistency Chaos - Characters and scenes change unpredictably across
  frames. ❌ Visual-Only Focus - Missing scripts, audio, narrative structure, and storytelling
  depth. 💡 ViMax Solution: 🎬 Director, Screenwriter, Producer, and Video Generator
  All-in-One! We''re exploring a future where AI becomes a complete creative powerhouse.
  💡 Simply input your concept. ViMax autonomously handles the rest. It orchestrates
  scriptwriting, storyboarding, character creation, and final video generation—all
  end-to-end. 🚀 https://github.com/user-attachments/assets/5bad46b2-8276-4e1d-9480-3522640744b2
  📑 Table of Contents 💡 Key Features 🔮 Demos 🏗️ Architecture 🚀 Quick Start 💡Key Features
  🌟 Idea2Video From Spark to Screen Transform raw ideas into complete video stories
  through intelligent multi-agent workflows automating storytelling, character design,
  and production . 🎨 Novel2Video Smart Literary Adaptation Engine Transform complete
  novels into episodic video content with intelligent narrative compression, character
  tracking, and scene-by-scene visual adaptation ⚙️ Script2Video Unlimited Screenplay
  Video Creation Unleash your creativity by writing any screenplay from personal stories
  to epic adventures, giving you complete control over every aspect of your visual
  storytelling. 🤳 AutoCameo Generate Video from Your Photo Create your own cameo video,
  transforming yourself/pet into a guest star who appears across limitless creative
  scripts, cinematic sequences, and interactive storylines. 🔮Video Demos Generated
  from Scratch 🎯 End-to-End Video Creation Engine The Challenges: 🌅 Reference Images:
  Time-consuming acquisition, organization, and alignment of reference frames that
  accurately capture characters, objects, positions, and environments. 🫠 Consistency
  Check: Sometimes, the image generator may generate unusable images even if it is
  given the correct characters, position, environment reference image and prompts.
  📄 Scripts Generation: Professional and high-quality videos need to have rich information
  density and structured design. 📝 Storyboard Design: Converting stories into visual
  narratives requires expertise in cinematography, scene composition, and visual storytelling
  that most creators lack. 🎬 Shot Design: Creating coherent camera sequences with
  proper angles, transitions, and pacing while maintaining narrative flow across complex
  scenes. 🎨 Development Delays: Ensuring character appearances, environments, and
  artistic style remain consistent across hundreds of shots in long-form content.
  ⏱️ Production Efficiency: Traditional video creation involves multiple specialists
  and lengthy workflows, creating barriers for independent creators and rapid prototyping.
  🎥 Scaling AI Generated Video: AI-generated videos are usually only a few seconds
  long, high-quality long videos at the minute or even hour level require complex
  cross-scene continuity and multi-storyboards design and processing capabilities.
  ViMAX: eliminates these production bottlenecks by automating the entire video creation
  pipeline from narrative input to final video output. 🔥 Why ViMax? 🧠 Effortless Production
  🚀 Complete Creative Freedom 🔊 Audio and Video Binding 🎨 Professional Quality 🤩 Interactive
  Video One-Prompt to Finished Video From Any Narrative to Reality Synchronized Storytelling
  Movie-Grade Output Make Your Own Cameo Video Skip the technical complexity—just
  describe your vision and let ViMax handle script generation, storyboarding, shot
  design, reference management, and consistency validation No creative limits—whether
  it''s a trailer, short story, novel chapter, or original concept, ViMax intelligently
  structures narratives and designs cinematography to bring any idea to life Seamlessly
  integrate character voice, and sound effects with visual content to create immersive
  experiences where audio and video work in perfect harmony Automated quality control
  ensures character consistency, proper scene composition, and professional visual
  standards across every frame of your video Interact in your own short stories by
  uploading your photo—ViMax intelligently integrates you as a character with consistent
  appearance and natural interactions throughout the entire video ☄️ Coming Soon 👨‍💻
  Google AI Studio API config✅ 📹 Dev mode branch 🤳 AutoCameo integrate 📺 More demos
  🎞️ Shot planning 🤖 New features 🏗️ Architecture 📊 System Overview ViMax is a multi-agent
  video framework that enables automated multi-shot video generation while ensuring
  character and scene consistency. Our system seamlessly translates your ideas into
  corresponding videos, allowing you to focus on storytelling rather than technical
  implementation. 🎯 Technical Capabilities: 🧬 Intelligent Long Script Generation RAG-based
  long script design engine that intelligently analyzes lengthy, novel-like stories
  and automatically segments them into a multi-scene script format. The process meticulously
  ensures that all key plot developments and character dialogues are accurately retained
  within the new structure. 🪄 Expressive Storyboard Design Shot-level storyboard design
  system that create expressive storyboards through cinematography language based
  on user requirements and target audiences, which establishs the narrative rhythm
  for subsequent video generation. 🔮 Multi-camera Filming Simulation Simulates multi-camera
  filming to deliver an immersive viewing experience while maintaining consistent
  character positioning and backgrounds within the same scene. 🧸 Intelligent Reference
  Images Selection Intelligently select the reference image required for the first
  frame of the current video, including the storyboards that occurred in the previous
  timeline, to ensure the accuracy of multiple characters and environmental elements
  as the video becomes longer. ⚙️ Automated Images Generation Based on the selected
  reference image and the visual logical order on the previous timeline, the prompt
  of the image generator is automatically generated to reasonably arrange the spatial
  interaction position between the character and the environment. ✅ Automated Image
  Generation Consistency Check Generate multiple images in parallel and select the
  best consistent image as the first frame through MLLM/VLM to imitate the workflow
  of human creators. ⚡ High-efficiency Parallel Shot Generation Parallel processing
  for sequential shots captured from the same camera enables highly efficient video
  production. 🤖 Multi-Agent Video Generation Pipeline 🧠 INPUT LAYER 📝 Idea & Scripts
  & Novels • 💭 Natural Language Prompts • 🖼️ Reference Images • 🎨 Style Directives
  • 🧩 Configs 🧭 CENTRAL ORCHESTRATION Agent Scheduling • Stage Transitions • Resource
  Management • Retry/Fallback Logic 🧾 SCRIPT UNDERSTANDING Character/Environment Extraction
  • Scene Boundaries • Style Intent 🎥 SCENE & SHOT PLANNING Storyboard Steps • Shot
  List • Key Frames & Beats 🧪 VISUAL ASSET PLANNING Reference Image Selection • Look/Style
  Guidance • Prompt Conditioning 🗂️ ASSET INDEXING Frames/Refs Catalog • Embeddings
  • Retrieval for Reuse ♻️ CONSISTENCY & CONTINUITY Character/Environment Tracking
  • Ref Matching • Temporal Coherence ✂️ VISUAL SYNTHESIS & ASSEMBLY Image Generation
  • Best-Frame Selection • First/Last-Frame→Video • Cut & Timeline Assembly 🚀 OUTPUT
  LAYER 🖼️ Frames • 🎞️ Clips & Final Videos • 📜 Logs • 📦 Working Directory Artifacts
  🚀Quick Start 🖥️ Environment OS: Linux, Windows 📥 Clone and Install We use uv to
  manage the environment. For uv installation, please refer to the https://docs.astral.sh/uv/getting-started/installation/.
  git clone https://github.com/HKUDS/ViMax.git cd ViMax uv sync 🎯 Usage main_idea2video.py
  is used to convert your ideas into videos. You need to configure the model and API
  key information in the configs/idea2video.yaml file, including three parts—the chat
  model, the image generator, and the video generator, as shown below chat_model:
  init_args: model: google/gemini-2.5-flash-lite-preview-09-2025 model_provider: openai
  api_key: <YOUR_API_KEY> base_url: https://openrouter.ai/api/v1 image_generator:
  class_path: tools.ImageGeneratorNanobananaGoogleAPI init_args: api_key: <YOUR_API_KEY>
  video_generator: class_path: tools.VideoGeneratorVeoGoogleAPI init_args: api_key:
  <YOUR_API_KEY> working_dir: .working_dir/idea2video Then, provide a simple yet thoughtful
  idea and the corresponding creative requirements in main_idea2video.py. idea = \
  """ If a cat and a dog are best friends, what would happen when they meet a new
  cat? """ user_requirement = \ """ For children, do not exceed 3 scenes. """ style
  = "Cartoon" Using MiniMax as Chat Model Provider MiniMax models can be used as an
  alternative chat model provider. MiniMax offers OpenAI-compatible API access to
  models such as MiniMax-M2.7 (1M context window) and MiniMax-M2.5 (204K context).
  Simply set model_provider: minimax in your config — the base URL is resolved automatically:
  chat_model: init_args: model: MiniMax-M2.7 model_provider: minimax api_key: <YOUR_MINIMAX_API_KEY>
  Or export the API key as an environment variable and leave api_key empty: export
  MINIMAX_API_KEY=<YOUR_KEY> See configs/idea2video_minimax.yaml and configs/script2video_minimax.yaml
  for complete examples. Model Context Note MiniMax-M2.7 1M tokens Latest, recommended
  MiniMax-M2.7-highspeed 1M tokens Fast variant MiniMax-M2.5 204K tokens Stable MiniMax-M2.5-highspeed
  204K tokens Fast variant main_script2video.py generates a video based on a specific
  script. You similarly need to set up the API configuration in configs/script2video.yaml
  file. Then, provide a scene script and the corresponding creative requirements in
  main_script2video.py, as shown below. script = \ """ EXT. SCHOOL GYM - DAY A group
  of students are practicing basketball in the gym. The gym is large and open, with
  a basketball hoop at one end and a large crowd of spectators at the other end. John
  (18, male, tall, athletic) is the star player, and he is practicing his dribble
  and shot. Jane (17, female, short, athletic) is the assistant coach, and she is
  helping John with his practice. The other students are watching the practice and
  cheering for John. John: (dribbling the ball) I''m going to score a basket! Jane:
  (smiling) Good job, John! John: (shooting the ball) Yes! ... """ user_requirement
  = \ """ Fast-paced with no more than 20 shots. """ style = "Animate Style" 🌟 If
  this project helps you, please give us a Star! ❤️ Thanks for visiting ✨ ViMax!'
tags:
- clippings
extraction_status: success
id: d58d3aa12effc0a2
source_type: community_discussion
tldr: HKUDS发布ViMax多智能体视频生成框架，实现从创意到成片的端到端自动化视频制作
objective_summary: 香港大学数据科学实验室（HKUDS）在GitHub开源发布ViMax多智能体视频框架。该框架接收用户创意或脚本输入，自动完成脚本生成、分镜设计、角色创建和视频生成，支持Google
  Gemini和MiniMax等多种模型后端，提供idea2video和script2video两种工作模式。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - HKUDS
  - Google
  - MiniMax
  - OpenRouter
  technologies:
  - ViMax
  - RAG
  - MLLM
  - VLM
  - Gemini-2.5-Flash-Lite
  - MiniMax-M2.7
  - Veo
  - Nanobanana
  key_people: []
key_logic_flow:
- ViMax是一个多智能体视频生成框架，通过中央编排调度实现从创意输入到最终视频输出的全自动化流程
- 框架包含脚本理解、场景与镜头规划、视觉资产规划、资产索引、一致性校验、视觉合成与组装六大核心模块
- 采用RAG引擎处理长篇故事类输入，自动分段为多场景脚本并保留关键情节与角色对话
- 通过MLLM/VLM自动生成多张候选图像并选出最佳一致帧，模拟人类创作者的筛选工作流
- 支持同一机位的连续镜头并行处理，以提高长视频制作效率
- 提供idea2video和script2video两种输入模式，通过OpenAI兼容API接入Google Gemini、MiniMax等多种模型
pipeline_stage: fact_extracted
extract_result: success
---

- ❌
**Limited to Short Clips**- Most AI tools generate only seconds of footage. - ❌
**Consistency Chaos**- Characters and scenes change unpredictably across frames. - ❌
**Visual-Only Focus**- Missing scripts, audio, narrative structure, and storytelling depth.

🎬 **Director**, **Screenwriter**, **Producer**, and **Video Generator** **All-in-One**! We're exploring a future where AI becomes a complete creative powerhouse. 💡 Simply input your concept. ViMax autonomously handles the rest. It orchestrates scriptwriting, storyboarding, character creation, and final video generation—all end-to-end. 🚀

## vimax_demo.mp4

|
Transform |
Transform |
Unleash your creativity by writing |
|

## f1.mp4 |
## underwater.mp4 |
## otter.mp4 |
## carrier.mp4 |
## vampire.mp4 |
## skydiving.mp4 |
## tree.mp4 |
## cameo_skycastle.mp4 |
## cameo_cat.mp4 |

**The Challenges**:

-
🌅

**Reference Images**: Time-consuming acquisition, organization, and alignment of reference frames that accurately capture characters, objects, positions, and environments. -
🫠

**Consistency Check**: Sometimes, the image generator may generate unusable images even if it is given the correct characters, position, environment reference image and prompts. -
📄

**Scripts Generation**: Professional and high-quality videos need to have rich information density and structured design. -
📝

**Storyboard Design**: Converting stories into visual narratives requires expertise in cinematography, scene composition, and visual storytelling that most creators lack. -
🎬

**Shot Design**: Creating coherent camera sequences with proper angles, transitions, and pacing while maintaining narrative flow across complex scenes. -
🎨

**Development Delays**: Ensuring character appearances, environments, and artistic style remain consistent across hundreds of shots in long-form content. -
⏱️

**Production Efficiency**: Traditional video creation involves multiple specialists and lengthy workflows, creating barriers for independent creators and rapid prototyping. -
🎥

**Scaling AI Generated Video**: AI-generated videos are usually only a few seconds long, high-quality long videos at the minute or even hour level require complex cross-scene continuity and multi-storyboards design and processing capabilities.

**ViMAX**: eliminates these production bottlenecks by automating the entire video creation pipeline from narrative input to final video output.

🧠 Effortless Production |
🚀 Complete Creative Freedom |
🔊 Audio and Video Binding |
🎨 Professional Quality |
🤩 Interactive Video |
|---|---|---|---|---|
| One-Prompt to Finished Video | From Any Narrative to Reality | Synchronized Storytelling | Movie-Grade Output | Make Your Own Cameo Video |
| Skip the technical complexity—just describe your vision and let ViMax handle script generation, storyboarding, shot design, reference management, and consistency validation | No creative limits—whether it's a trailer, short story, novel chapter, or original concept, ViMax intelligently structures narratives and designs cinematography to bring any idea to life | Seamlessly integrate character voice, and sound effects with visual content to create immersive experiences where audio and video work in perfect harmony | Automated quality control ensures character consistency, proper scene composition, and professional visual standards across every frame of your video | Interact in your own short stories by uploading your photo—ViMax intelligently integrates you as a character with consistent appearance and natural interactions throughout the entire video |

- 👨💻
**Google AI Studio API config✅** - 📹
**Dev mode branch** - 🤳
**AutoCameo integrate** - 📺
**More demos** - 🎞️
**Shot planning** - 🤖
**New features**

**ViMax** is a multi-agent video framework that enables automated multi-shot video generation while ensuring character and scene consistency. Our system seamlessly translates your ideas into corresponding videos, allowing you to focus on storytelling rather than technical implementation.

🎯 **Technical Capabilities**:

🧬 **Intelligent Long Script Generation**

RAG-based long script design engine that intelligently analyzes lengthy, novel-like stories and automatically segments them into a multi-scene script format. The process meticulously ensures that all key plot developments and character dialogues are accurately retained within the new structure.

🪄 **Expressive Storyboard Design**

Shot-level storyboard design system that create expressive storyboards through cinematography language based on user requirements and target audiences, which establishs the narrative rhythm for subsequent video generation.

🔮 **Multi-camera Filming Simulation**

Simulates multi-camera filming to deliver an immersive viewing experience while maintaining consistent character positioning and backgrounds within the same scene.

🧸 **Intelligent Reference Images Selection**

Intelligently select the reference image required for the first frame of the current video, including the storyboards that occurred in the previous timeline, to ensure the accuracy of multiple characters and environmental elements as the video becomes longer.

⚙️ **Automated Images Generation**

Based on the selected reference image and the visual logical order on the previous timeline, the prompt of the image generator is automatically generated to reasonably arrange the spatial interaction position between the character and the environment.

✅ **Automated Image Generation Consistency Check**

Generate multiple images in parallel and select the best consistent image as the first frame through MLLM/VLM to imitate the workflow of human creators.

⚡ **High-efficiency Parallel Shot Generation**

Parallel processing for sequential shots captured from the same camera enables highly efficient video production.

🧠 INPUT LAYER📝 Idea & Scripts & Novels • 💭 Natural Language Prompts • 🖼️ Reference Images • 🎨 Style Directives • 🧩 Configs |
||
🧭 CENTRAL ORCHESTRATIONAgent Scheduling • Stage Transitions • Resource Management • Retry/Fallback Logic |
||
🧾 SCRIPT UNDERSTANDINGCharacter/Environment Extraction • Scene Boundaries • Style Intent |
🎥 SCENE & SHOT PLANNINGStoryboard Steps • Shot List • Key Frames & Beats |
|
🧪 VISUAL ASSET PLANNINGReference Image Selection • Look/Style Guidance • Prompt Conditioning |
||
🗂️ ASSET INDEXINGFrames/Refs Catalog • Embeddings • Retrieval for Reuse |
♻️ CONSISTENCY & CONTINUITYCharacter/Environment Tracking • Ref Matching • Temporal Coherence |
|
✂️ VISUAL SYNTHESIS & ASSEMBLYImage Generation • Best-Frame Selection • First/Last-Frame→Video • Cut & Timeline Assembly |
||
🚀 OUTPUT LAYER🖼️ Frames • 🎞️ Clips & Final Videos • 📜 Logs • 📦 Working Directory Artifacts |

```
OS: Linux, Windows
```


We use uv to manage the environment. For uv installation, please refer to the https://docs.astral.sh/uv/getting-started/installation/.

```
git clone https://github.com/HKUDS/ViMax.git
cd ViMax
uv sync
```

main_idea2video.py is used to convert your ideas into videos. You need to configure the model and API key information in the configs/idea2video.yaml file, including three parts—the chat model, the image generator, and the video generator, as shown below

```
chat_model:
init_args:
model: google/gemini-2.5-flash-lite-preview-09-2025
model_provider: openai
api_key: <YOUR_API_KEY>
base_url: https://openrouter.ai/api/v1
image_generator:
class_path: tools.ImageGeneratorNanobananaGoogleAPI
init_args:
api_key: <YOUR_API_KEY>
video_generator:
class_path: tools.VideoGeneratorVeoGoogleAPI
init_args:
api_key: <YOUR_API_KEY>
working_dir: .working_dir/idea2video
```

Then, provide a simple yet thoughtful idea and the corresponding creative requirements in main_idea2video.py.

```
idea = \
"""
If a cat and a dog are best friends, what would happen when they meet a new cat?
"""
user_requirement = \
"""
For children, do not exceed 3 scenes.
"""
style = "Cartoon"
```

MiniMax models can be used as an alternative chat model provider. MiniMax offers OpenAI-compatible API access to models such as **MiniMax-M2.7** (1M context window) and **MiniMax-M2.5** (204K context).

Simply set `model_provider: minimax`

in your config — the base URL is resolved automatically:

```
chat_model:
init_args:
model: MiniMax-M2.7
model_provider: minimax
api_key: <YOUR_MINIMAX_API_KEY>
```

Or export the API key as an environment variable and leave `api_key`

empty:

`export MINIMAX_API_KEY=<YOUR_KEY>`

See `configs/idea2video_minimax.yaml`

and `configs/script2video_minimax.yaml`

for complete examples.

| Model | Context | Note |
|---|---|---|
| MiniMax-M2.7 | 1M tokens | Latest, recommended |
| MiniMax-M2.7-highspeed | 1M tokens | Fast variant |
| MiniMax-M2.5 | 204K tokens | Stable |
| MiniMax-M2.5-highspeed | 204K tokens | Fast variant |

main_script2video.py generates a video based on a specific script. You similarly need to set up the API configuration in configs/script2video.yaml file. Then, provide a scene script and the corresponding creative requirements in main_script2video.py, as shown below.

```
script = \
"""
EXT. SCHOOL GYM - DAY
A group of students are practicing basketball in the gym. The gym is large and open, with a basketball hoop at one end and a large crowd of spectators at the other end. John (18, male, tall, athletic) is the star player, and he is practicing his dribble and shot. Jane (17, female, short, athletic) is the assistant coach, and she is helping John with his practice. The other students are watching the practice and cheering for John.
John: (dribbling the ball) I'm going to score a basket!
Jane: (smiling) Good job, John!
John: (shooting the ball) Yes!
...
"""
user_requirement = \
"""
Fast-paced with no more than 20 shots.
"""
style = "Animate Style"
```

**🌟 If this project helps you, please give us a Star!**

* ❤️ Thanks for visiting ✨ ViMax!*