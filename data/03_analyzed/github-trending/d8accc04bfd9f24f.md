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
tldr: Lightricks 发布开源 DiT 音视频基础模型 LTX-2
objective_summary: Lightricks 于 GitHub 开源发布 LTX-2，这是首个基于 DiT 架构的音频-视频联合基础模型，支持同步音视频生成、文生视频、图生视频、音频转视频、口型同步等多种推理管线，提供
  FP8 量化与 FlashAttention 加速，并附带训练与微调工具。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Lightricks
  technologies:
  - DiT
  - FP8量化
  - FlashAttention-4
  - xFormers
  - LoRA
  - IC-LoRA
  - HDR
  - Gemma Text Encoder
  key_people: []
key_logic_flow:
- Lightricks 发布 LTX-2，这是首个基于 DiT 架构的音频-视频基础模型，支持同步音频与视频生成。
- 项目以开源形式发布在 GitHub，包含 ltx-core（核心模型）、ltx-pipelines（推理管线）、ltx-trainer（训练工具）三大子包。
- 提供多种推理管线，涵盖文生视频、图生视频、音频转视频、口型同步、关键帧插值、视频重拍等功能。
- 支持 FP8 量化、FlashAttention-4（Blackwell GPU）、xFormers（Hopper GPU）等加速方案以降低显存占用。
- 模型支持多种 LoRA 控制方式，包括 IC-LoRA 联合控制、运动轨迹控制、姿态控制、相机运动控制等。
- 用户可通过命令行或 Python API 调用模型，并支持 ComfyUI 集成。
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