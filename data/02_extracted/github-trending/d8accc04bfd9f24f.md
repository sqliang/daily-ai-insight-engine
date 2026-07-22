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