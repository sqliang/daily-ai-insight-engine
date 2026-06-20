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