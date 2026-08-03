---
title: Lightricks/LTX-2
source: https://github.com/Lightricks/LTX-2
author: []
published: ''
created: '2026-06-19'
description: 'Official Python inference and LoRA trainer package for the LTX-2 audio–video
  generative model.LTX-2 LTX-2 is the first DiT-based audio-video foundation model
  that contains all core capabilities of modern video generation in one model: synchronized
  audio and video, high fidelity, multiple performance modes, production-ready outputs,
  API access, and open access. 🚀 Quick Start # Clone the repository git clone https://github.com/Lightricks/LTX-2.git
  cd LTX-2 # Set up the environment uv sync --frozen source .venv/bin/activate Required
  Models Download the following models from the LTX-2.3 HuggingFace repository: LTX-2.3
  Model Checkpoint (choose and download one of the following) ltx-2.3-22b-dev.safetensors
  - Download ltx-2.3-22b-distilled-1.1.safetensors - Download Spatial Upscaler - Required
  for current two-stage pipeline implementations in this repository ltx-2.3-spatial-upscaler-x2-1.1.safetensors
  - Download ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors - Download Temporal Upscaler
  - Supported by the model and will be required for future pipeline implementations
  ltx-2.3-temporal-upscaler-x2-1.0.safetensors - Download Distilled LoRA - Required
  for current two-stage pipeline implementations in this repository (except DistilledPipeline,
  ICLoraPipeline, and LipDubPipeline) ltx-2.3-22b-distilled-lora-384-1.1.safetensors
  - Download Gemma Text Encoder (download all assets from the repository) Gemma 3
  LoRAs LTX-2.3-22b-IC-LoRA-Union-Control - Download LTX-2.3-22b-IC-LoRA-Motion-Track-Control
  - Download LTX-2-19b-IC-LoRA-Detailer - Download LTX-2-19b-IC-LoRA-Pose-Control
  - Download LTX-2-19b-LoRA-Camera-Control-Dolly-In - Download LTX-2-19b-LoRA-Camera-Control-Dolly-Left
  - Download LTX-2-19b-LoRA-Camera-Control-Dolly-Out - Download LTX-2-19b-LoRA-Camera-Control-Dolly-Right
  - Download LTX-2-19b-LoRA-Camera-Control-Jib-Down - Download LTX-2-19b-LoRA-Camera-Control-Jib-Up
  - Download LTX-2-19b-LoRA-Camera-Control-Static - Download LTX-2.3-22b-IC-LoRA-HDR
  - HDR IC-LoRA and pre-computed text embeddings for HDRICLoraPipeline LTX-2.3-22b-IC-LoRA-LipDub
  - Download Available Pipelines TI2VidTwoStagesPipeline - Production-quality text/image-to-video
  with 2x upsampling (recommended) TI2VidTwoStagesHQPipeline - Same two-stage flow
  as above but uses the res_2s second-order sampler (fewer steps, better quality)
  TI2VidOneStagePipeline - Single-stage generation for quick prototyping DistilledPipeline
  - Fastest inference with 8 predefined sigmas ICLoraPipeline - Video-to-video and
  image-to-video transformations (uses distilled model.) KeyframeInterpolationPipeline
  - Interpolate between keyframe images A2VidPipelineTwoStage - Audio-to-video generation
  conditioned on an input audio file RetakePipeline - Regenerate a specific time region
  of an existing video HDRICLoraPipeline - Video-to-video with HDR output (linear
  float frames via LogC3 inverse decode, suitable for EXR export and tonemapping)
  LipDubPipeline - Lip dubbing, rephrasing, matching speaker identity (distilled model,
  single IC-LoRA, Two stages). ⚡ Optimization Tips Use DistilledPipeline - Fastest
  inference with only 8 predefined sigmas (8 steps stage 1, 4 steps stage 2) Enable
  FP8 quantization - Enables lower memory footprint: --quantization fp8-cast (CLI)
  or quantization=QuantizationPolicy.fp8_cast() (Python). Fp8-cast should be used
  with bf16 checkpoints, it shall downcast them on the fly. For Hopper GPUs with TensorRT-LLM,
  use --quantization fp8-scaled-mm for FP8 scaled matrix multiplication. Fp8-scaled-mm
  should be used with fp8 checkpoints. Install attention optimizations - On datacenter
  Blackwell GPUs (B200), install FlashAttention 4 manually: uv pip install ''flash-attn-4==4.0.0b9''
  (this specific revision is the one we have verified against torch 2.9.1+cu128; newer
  betas have known issues on consumer Blackwell). On other CUDA GPUs (including Hopper),
  use xFormers (uv sync --extra xformers). Use gradient estimation - Reduce inference
  steps from 40 to 20-30 while maintaining quality (see pipeline documentation) Skip
  memory cleanup - If you have sufficient VRAM, disable automatic memory cleanup between
  stages for faster processing Choose single-stage pipeline - Use TI2VidOneStagePipeline
  for faster generation when high resolution isn''t required ✍️ Prompting for LTX-2
  When writing prompts, focus on detailed, chronological descriptions of actions and
  scenes. Include specific movements, appearances, camera angles, and environmental
  details - all in a single flowing paragraph. Start directly with the action, and
  keep descriptions literal and precise. Think like a cinematographer describing a
  shot list. Keep within 200 words. For best results, build your prompts using this
  structure: Start with main action in a single sentence Add specific details about
  movements and gestures Describe character/object appearances precisely Include background
  and environment details Specify camera angles and movements Describe lighting and
  colors Note any changes or sudden events For additional guidance on writing a prompt
  please refer to https://ltx.video/blog/how-to-prompt-for-ltx-2 Automatic Prompt
  Enhancement LTX-2 pipelines support automatic prompt enhancement via an enhance_prompt
  parameter. 🔌 ComfyUI Integration To use our model with ComfyUI, please follow the
  instructions at https://github.com/Lightricks/ComfyUI-LTXVideo/. 📦 Packages This
  repository is organized as a monorepo with three main packages: ltx-core - Core
  model implementation, inference stack, and utilities ltx-pipelines - High-level
  pipeline implementations for text-to-video, image-to-video, and other generation
  modes ltx-trainer - Training and fine-tuning tools for LoRA, full fine-tuning, and
  IC-LoRA Each package has its own README and documentation. See the Documentation
  section below. 📚 Documentation Each package includes comprehensive documentation:
  LTX-Core README - Core model implementation, inference stack, and utilities LTX-Pipelines
  README - High-level pipeline implementations and usage guides LTX-Trainer README
  - Training and fine-tuning documentation with detailed guides'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d8accc04bfd9f24f
source_type: community_discussion
tldr: Lightricks 开源了首个基于 DiT 架构的音视频基础模型 LTX-2，将同步音视频生成、高保真输出、多性能模式整合在单一模型中。仓库提供多种推理管线、FP8
  量化支持和 ComfyUI 集成，并以单体仓库形式包含核心实现、高级管线与训练工具三个包。
objective_summary: Lightricks 于 GitHub 发布 LTX-2，这是首个基于 DiT（Diffusion Transformer）的音频-视频基础模型，将同步音频与视频生成、高保真输出、生产级输出、API
  访问和开放访问等核心能力整合在单一模型中。该仓库以单体仓库结构组织，包含 ltx-core（核心模型与推理栈）、ltx-pipelines（高级生成管线，如 TI2VidTwoStagesPipeline、DistilledPipeline、LipDubPipeline
  等）和 ltx-trainer（LoRA 微调与全参数训练工具）三个核心包，支持 FP8 量化与 FlashAttention 4 优化，并提供 ComfyUI
  集成方案。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Lightricks
  technologies:
  - DiT
  - LoRA
  - IC-LoRA
  - FP8
  - FlashAttention 4
  - xFormers
  - Gemma
  - HDR
  - ComfyUI
  key_people: []
key_logic_flow:
- LTX-2 是 Lightricks 发布的基于 DiT 架构的音频-视频基础模型，将同步音视频生成、高保真输出、多性能模式等核心能力整合在单一模型中。
- 仓库以单体仓库结构组织，包含 ltx-core（核心模型与推理栈）、ltx-pipelines（高级管线实现）和 ltx-trainer（LoRA 与全参数微调工具）三个核心包。
- 提供多种推理管线，包括 TI2VidTwoStagesPipeline（生产级文生/图生视频）、DistilledPipeline（8 步快速推理）、LipDubPipeline（唇形同步配音）以及
  A2VidPipelineTwoStage（音频驱动视频生成）等。
- 模型支持 FP8 量化以降低显存占用，在 B200 GPU 上使用 FlashAttention 4，在其他 CUDA GPU 上使用 xFormers 进行注意力优化。
- 用户可通过 Lightricks/ComfyUI-LTXVideo 仓库在 ComfyUI 中使用 LTX-2 模型，实现可视化工作流集成。
extract_result: success
object_mentions:
- object_type: project
  name: Lightricks/LTX-2
  canonical_name: Lightricks/LTX-2
  url: https://github.com/Lightricks/LTX-2
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - LTX-2 是首个基于 DiT 架构的音频-视频基础模型，将同步音频与视频生成、高保真输出、API 访问和开放访问等核心能力整合在单一模型中。
  - 该仓库以单体仓库结构组织，包含 ltx-core、ltx-pipelines 和 ltx-trainer 三个核心包，分别实现模型推理栈、高级管线与训练微调工具。
  article_id: d8accc04bfd9f24f
- object_type: project
  name: Lightricks/ComfyUI-LTXVideo
  canonical_name: Lightricks/ComfyUI-LTXVideo
  url: https://github.com/Lightricks/ComfyUI-LTXVideo
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 用户可按照 Lightricks/ComfyUI-LTXVideo 仓库的说明在 ComfyUI 中使用 LTX-2 模型进行可视化工作流集成。
  article_id: d8accc04bfd9f24f
- object_type: model
  name: LTX-2.3
  canonical_name: LTX-2.3
  url: https://huggingface.co/Lightricks/LTX-2.3
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LTX-2.3 模型检查点从 HuggingFace 仓库下载，包含 Spatial Upscaler、Temporal Upscaler 和 Distilled
    LoRA 等组件。
  - LTX-2.3 附加了 IC-LoRA 模型如 HDR IC-LoRA 和 LipDub IC-LoRA，分别用于 HDR 输出和唇形同步配音。
  article_id: d8accc04bfd9f24f
impact_score:
  score: 7.2
  reason: LTX-2 是首个基于 DiT 架构的音频-视频联合基础模型，填补了开源领域同步音视频生成的技术空白。其开放了完整的训练工具链（LoRA/IC-LoRA/全参微调）、多种推理管线以及
    FP8/FlashAttention-4 等生产级加速方案，显著降低了社区在视频生成方向的研究门槛。虽然不构成类似 ChatGPT 级别的范式转移，但它在开源视频生成赛道中是里程碑式的发布，将改变该领域的竞争格局，迫使其他闭源视频模型在开放策略上做出回应。综合评定
    7.2 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 首个开源 DiT 音视频联合模型的可用性与训练微调能力
hype_assessment:
  level: low
  reason: 该项目的 GitHub 发布文风偏技术实操，没有使用'颠覆'、'革命性'等 PR 滥用词汇，而是详细列出了技术架构、加速方案、依赖版本和具体使用方法。'first
    DiT-based audio-video foundation model' 的定位是事实性陈述且有技术依据。整体信息呈现务实、干货导向，不存在明显的概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 首次将 DiT 架构扩展到音视频联合生成领域，实现单一基础模型内的文生视频、图生视频、音频转视频、口型同步、关键帧插值等多模态能力，并支持
    FP8 量化、FlashAttention-4（Blackwell）、xFormers（Hopper）等分层加速方案，在工程上实现了训练与推理的完整工具链开源。
  business_model: Lightricks 将核心基础模型完全开源（含训练工具），走'开源社区生态 + 商业 API 服务'双轨模式，类似于 Meta
    的 Llama 策略。这种'开源底座 + 增值云服务'的路径将对 Runway、Pika 等闭源视频生成公司形成竞争压力，推动行业整体向更开放的方向演进。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: LTX-2 作为首个开源 DiT 音视频联合基础模型，具备显著的长期复利潜力。核心投资逻辑：(1) 音视频同步生成是视频生成领域尚未被充分占领的技术高地，LTX-2
    率先以开源方式卡位，有机会成为社区事实标准；(2) 提供 ltx-trainer + 多种 LoRA 控制（姿态/轨迹/相机/HDR/唇形同步），降低开发者二次开发门槛，形成平台效应；(3)
    支持 FP8 量化、FlashAttention-4、xFormers 等显存优化，降低了推理成本，加速生态扩散。但风险在于：开源视频模型赛道竞争激烈（CogVideo、Open-Sora、Mochi
    等），Lightricks 作为盈利性公司能否长期持续投入开源项目存在不确定性；此外视频生成极度依赖算力，社区贡献者的算力门槛限制了生态成长速度。综合评估，若能建成活跃的开源生态，3-5
    年后有望成为视频生成领域的 Linux 级基础设施，但当前仍处于早期验证阶段。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Lightricks
- ComfyUI
- NVIDIA
- Hugging Face
- 开源 AI 视频社区
competitive_casualty:
- Runway ML
- Pika Labs
- 闭源视频生成 API 服务商
- OpenAI Sora (潜在市场份额侵蚀)
market_opportunities:
- 内容创作者和影视制作团队可直接利用 LTX-2 开源模型搭建一站式音视频生成管线，大幅降低从文本/图片到成品视频的后期制作成本
- 企业可基于 LTX-2 的多种 LoRA 控制能力（姿态、相机运动、口型同步等），开发面向广告营销、游戏过场动画、虚拟主播等垂直场景的微调解决方案
- 围绕 LTX-2 的 ComfyUI 集成生态和训练工具链（LoRA/IC-LoRA/全量微调），可以构建面向创作者的模型服务 SaaS 或企业级定制化训练平台
risk_matrix:
  regulatory: 视频生成模型在欧盟 AI Act 下可能被归类为高风险应用，特别是同步音频生成能力面临合成媒体标识（watermarking）、深度伪造检测等合规要求；开源发布增加了监管追溯难度
  technological: DiT 架构正快速演进，Sora、CogVideoX 等竞品持续迭代，LTX-2 的架构领先窗口期有限；FP8 量化与 FlashAttention-4
    的加速方案高度依赖特定 GPU 平台（Blackwell/Hopper），普通用户的推理成本仍较高
  competitive: 视频生成赛道竞争白热化，Runway、Pika、OpenAI Sora、Meta 等巨头持续投入，LTX-2 作为开源方案虽在可控性和成本上有优势，但商业生态可能被闭源巨头的
    API 生态挤压
  ethical: 音频-视频联合生成能力大幅降低了深度伪造门槛，口型同步（LipDub）和音频转视频功能极易被用于政治虚假信息、色情替换等恶意场景，且开源分发增加了滥用追踪的难度
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Lightricks/LTX-2
  canonical_name: Lightricks/LTX-2
  url: https://github.com/Lightricks/LTX-2
  positioning: LTX-2 是首个基于 DiT 架构的开源音视频基础模型，将同步音频与视频生成、高保真输出与多种性能模式整合在单一模型中。
  technical_signal: 采用 Diffusion Transformer 架构实现同步音频与视频联合生成，支持 FP8 量化降低显存占用，并兼容 FlashAttention
    4 与 xFormers 注意力优化方案。
  adoption_signal: 提供 TI2Vid、DistilledPipeline、LipDubPipeline 等多种高级生成管线，支持 LoRA 微调与全参数训练，并已集成
    ComfyUI 可视化工作流。
  ecosystem_relevance: 作为开源 DiT 音视频基础模型填补了领域空白，通过 ComfyUI 集成降低社区使用门槛，单体仓库设计便于第三方贡献与生态扩展。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: LTX-2 是首个开源 DiT 音视频基础模型，整合了同步音频生成、唇形同步配音、音频驱动视频生成等创新管线，有望在音视频生成领域培育开放生态，值得持续跟踪其社区接纳度和生成质量演进。
  risk_notes:
  - 模型参数量较大，推理对 B200 等高端 GPU 依赖较强，FP8 量化虽能降低显存占用但实际效果需进一步验证。
  - LTX-2 刚进入开源阶段，社区贡献活跃度和第三方工具生态仍处早期建设过程中，成熟度有待持续检验。
  score: 8.0
  article_ids:
  - d8accc04bfd9f24f
  evidence_snippets:
  - LTX-2 是首个基于 DiT 架构的音频-视频基础模型，将同步音频与视频生成、高保真输出、API 访问和开放访问等核心能力整合在单一模型中。
  - 该仓库以单体仓库结构组织，包含 ltx-core、ltx-pipelines 和 ltx-trainer 三个核心包，分别实现模型推理栈、高级管线与训练微调工具。
---

**LTX-2** is the first DiT-based audio-video foundation model that contains all core capabilities of modern video generation in one model: synchronized audio and video, high fidelity, multiple performance modes, production-ready outputs, API access, and open access.

## ltx-2.mp4

```
# Clone the repository
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
# Set up the environment
uv sync --frozen
source .venv/bin/activate
```

Download the following models from the LTX-2.3 HuggingFace repository:

**LTX-2.3 Model Checkpoint** (choose and download one of the following)

**Spatial Upscaler** - Required for current two-stage pipeline implementations in this repository

`ltx-2.3-spatial-upscaler-x2-1.1.safetensors`

- Download`ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors`

- Download

**Temporal Upscaler** - Supported by the model and will be required for future pipeline implementations

**Distilled LoRA** - Required for current two-stage pipeline implementations in this repository (except DistilledPipeline, ICLoraPipeline, and LipDubPipeline)

**Gemma Text Encoder** (download all assets from the repository)

**LoRAs**

`LTX-2.3-22b-IC-LoRA-Union-Control`

- Download`LTX-2.3-22b-IC-LoRA-Motion-Track-Control`

- Download`LTX-2-19b-IC-LoRA-Detailer`

- Download`LTX-2-19b-IC-LoRA-Pose-Control`

- Download`LTX-2-19b-LoRA-Camera-Control-Dolly-In`

- Download`LTX-2-19b-LoRA-Camera-Control-Dolly-Left`

- Download`LTX-2-19b-LoRA-Camera-Control-Dolly-Out`

- Download`LTX-2-19b-LoRA-Camera-Control-Dolly-Right`

- Download`LTX-2-19b-LoRA-Camera-Control-Jib-Down`

- Download`LTX-2-19b-LoRA-Camera-Control-Jib-Up`

- Download`LTX-2-19b-LoRA-Camera-Control-Static`

- Download`LTX-2.3-22b-IC-LoRA-HDR`

- HDR IC-LoRA and pre-computed text embeddings for`HDRICLoraPipeline`

`LTX-2.3-22b-IC-LoRA-LipDub`

- Download

**TI2VidTwoStagesPipeline**- Production-quality text/image-to-video with 2x upsampling (recommended)**TI2VidTwoStagesHQPipeline**- Same two-stage flow as above but uses the res_2s second-order sampler (fewer steps, better quality)**TI2VidOneStagePipeline**- Single-stage generation for quick prototyping**DistilledPipeline**- Fastest inference with 8 predefined sigmas**ICLoraPipeline**- Video-to-video and image-to-video transformations (uses distilled model.)**KeyframeInterpolationPipeline**- Interpolate between keyframe images**A2VidPipelineTwoStage**- Audio-to-video generation conditioned on an input audio file**RetakePipeline**- Regenerate a specific time region of an existing video**HDRICLoraPipeline**- Video-to-video with HDR output (linear float frames via LogC3 inverse decode, suitable for EXR export and tonemapping)**LipDubPipeline**- Lip dubbing, rephrasing, matching speaker identity (distilled model, single IC-LoRA, Two stages).

**Use DistilledPipeline**- Fastest inference with only 8 predefined sigmas (8 steps stage 1, 4 steps stage 2)**Enable FP8 quantization**- Enables lower memory footprint:`--quantization fp8-cast`

(CLI) or`quantization=QuantizationPolicy.fp8_cast()`

(Python). Fp8-cast should be used with bf16 checkpoints, it shall downcast them on the fly. For Hopper GPUs with TensorRT-LLM, use`--quantization fp8-scaled-mm`

for FP8 scaled matrix multiplication. Fp8-scaled-mm should be used with fp8 checkpoints.**Install attention optimizations**- On datacenter Blackwell GPUs (B200), install FlashAttention 4 manually:`uv pip install 'flash-attn-4==4.0.0b9'`

(this specific revision is the one we have verified against torch 2.9.1+cu128; newer betas have known issues on consumer Blackwell). On other CUDA GPUs (including Hopper), use xFormers (`uv sync --extra xformers`

).**Use gradient estimation**- Reduce inference steps from 40 to 20-30 while maintaining quality (see pipeline documentation)**Skip memory cleanup**- If you have sufficient VRAM, disable automatic memory cleanup between stages for faster processing**Choose single-stage pipeline**- Use`TI2VidOneStagePipeline`

for faster generation when high resolution isn't required

When writing prompts, focus on detailed, chronological descriptions of actions and scenes. Include specific movements, appearances, camera angles, and environmental details - all in a single flowing paragraph. Start directly with the action, and keep descriptions literal and precise. Think like a cinematographer describing a shot list. Keep within 200 words. For best results, build your prompts using this structure:

- Start with main action in a single sentence
- Add specific details about movements and gestures
- Describe character/object appearances precisely
- Include background and environment details
- Specify camera angles and movements
- Describe lighting and colors
- Note any changes or sudden events

For additional guidance on writing a prompt please refer to https://ltx.video/blog/how-to-prompt-for-ltx-2

LTX-2 pipelines support automatic prompt enhancement via an `enhance_prompt`

parameter.

To use our model with ComfyUI, please follow the instructions at https://github.com/Lightricks/ComfyUI-LTXVideo/.

This repository is organized as a monorepo with three main packages:

**ltx-core**- Core model implementation, inference stack, and utilities**ltx-pipelines**- High-level pipeline implementations for text-to-video, image-to-video, and other generation modes**ltx-trainer**- Training and fine-tuning tools for LoRA, full fine-tuning, and IC-LoRA

Each package has its own README and documentation. See the Documentation section below.

Each package includes comprehensive documentation:

**LTX-Core README**- Core model implementation, inference stack, and utilities**LTX-Pipelines README**- High-level pipeline implementations and usage guides**LTX-Trainer README**- Training and fine-tuning documentation with detailed guides