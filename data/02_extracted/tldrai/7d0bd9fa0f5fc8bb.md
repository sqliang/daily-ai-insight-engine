---
title: Real-Time Long Video Generation (GitHub Repo)
source: https://github.com/NVlabs/LongLive?utm_source=tldrai
author: []
published: ''
created: '2026-05-21'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
id: 7d0bd9fa0f5fc8bb
source_type: news_media
tldr: NVIDIA发布LongLive 2.0，基于NVFP4实现45.7 FPS实时长视频生成，论文被ICLR-2026接收。
objective_summary: NVIDIA NVlabs于2025年9月发布LongLive 1.0实时交互式长视频生成系统，2026年5月发布2.0版本。2.0引入NVFP4量化基础设施，支持多镜头AR训练、DMD少步蒸馏和序列并行推理，在5B参数模型上达45.7
  FPS。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - NVIDIA
  - NVlabs
  technologies:
  - LongLive
  - NVFP4
  - KV Cache
  - TriAttention
  - Causal Diffusion
  - DMD
  - RoPE
  - SANA-Video
  - Attention Sink
  - Sequence Parallel
  - VBench
  key_people: []
key_logic_flow:
- LongLive 1.0 提出 attention sink、KV-recache 和 streaming long tuning 三项核心技术，实现用户通过连续
  prompt 交互的实时长视频生成
- LongLive 2.0 构建在 NVFP4 并行基础设施之上，支持 W4A4 量化的训练（AR 训练 + DMD 少步蒸馏）和推理
- 训练层面支持平衡序列并行 AR 训练（teacher-forcing）、多镜头/单镜头视频训练，以及 NVFP4 或 BF16 精度选项
- 推理层面支持 NVFP4 推理（W4A4）、NVFP4 KV Cache、多镜头 attention sink、序列并行推理和异步解码
- 通过 DMD 少步蒸馏，2-Step 模型达到 45.7 FPS，4-Step 模型达到 29.7 FPS，均显著优于 1.0 版本 1.3B 模型的 20.7
  FPS
- 项目集成 TriAttention KV 缓存压缩（50% KV 缩减无损质量）和 KV-cache 相对 RoPE 适配（支持无限长视频生成），并在 SANA-Video
  线性注意力模型上实现 60 秒实时交互视频生成
pipeline_stage: fact_extracted
---

- 🔥 [2026.05.13] We release
**LongLive 2.0**, infra with NVFP4, parallelism and multi-shot for AR training, DMD distillation, and inference (⚡45.7 FPS). The original LongLive 1.0 is now in the v1.0 branch. - 🔥 [2026.04.12] LongLive supports kv cache compression with TriAttention, with 50% KV reduction and no quality drop. Check it here
- 🎉 [2026.1.27] LongLive is accepted by
**ICLR-2026**. - 🔥 [2026.1.11] LongLive supports adapting LongLive's original RoPE into KV-cache relative RoPE and generates infinite long videos!
- 🔥 [2025.11.3] We implement LongLive on linear attention model SANA-Video! Now SANA-Video can generate 60s interactive videos in real-time.
- 🔥 [2025.9.29] We release Paper, this GitHub repo LongLive with all training and inference code, the model weight LongLive-1.3B, and demo page Website.

**LongLive 1.0**: Real-time Interactive Long Video Generation. You can find it here in our V1.0 branch.

**LongLive 2.0**: an NVFP4 Parallel Infrastructure for Long Video Generation

- For training, it supports
- Balanced sequence parallel for AR training (teacher-forcing).
- AR training on multi-shot (or single-shot) videos.
- NVFP4 (or BF16) for both AR training and few-step distillation.

- For inference, it supports
- NVFP4 inference (W4A4) and NVFP4 KV Cache.
- Multi-shot attention sink.
- Sequence parallel inference.
- Async decoding.


**LongLive 1.0**: Real-time Interactive Long Video Generation. It accepts sequential user prompts and generates corresponding videos in real time, enabling user-guided long video generation. The key insights are attention sink, KV-recache, and streaming long tuning.

```
import torch
from omegaconf import OmegaConf
from pipeline import CausalDiffusionInferencePipeline
from utils.config import normalize_config
from utils.inference_utils import (
load_generator_checkpoint,
place_vae_for_streaming,
prepare_single_prompt_inputs,
save_video,
)
prompt = "A compact silver robot walks through a clean robotics lab."
merged_checkpoint_path = "LongLive-2.0-5B/model_bf16.pt"
config = normalize_config(OmegaConf.load("configs/inference.yaml"))
device = torch.device("cuda")
torch.set_grad_enabled(False)
pipe = CausalDiffusionInferencePipeline(config, device=device)
load_generator_checkpoint(pipe.generator, merged_checkpoint_path)
pipe = pipe.to(device=device, dtype=torch.bfloat16)
place_vae_for_streaming(pipe, config) # honor streaming_vae + vae_device when set
pipe.generator.model.eval().requires_grad_(False)
noise, prompts = prepare_single_prompt_inputs(config, prompt, device)
video = pipe.inference(noise=noise, text_prompts=prompts)
save_video(video[0], "videos/quickstart/sample.mp4", fps=24)
```

`place_vae_for_streaming`

is a no-op unless `inference.streaming_vae`

is true and `inference.vae_device`

is set, so toggling streaming-pipeline decode in your yaml is enough — the script does not need to change.

Point `checkpoints.generator_ckpt`

in `configs/nvfp4/inference_nvfp4.yaml`

at the downloaded checkpoint and set `model_quant_use_transformer_engine`

according to the backend you are using:

- TransformerEngine checkpoint (
`model_te.pt`

):`model_quant_use_transformer_engine: true`

- FourOverSix checkpoint (
`model_4o6.pt`

):`model_quant_use_transformer_engine: false`


`setup_nvfp4_pipeline`

handles checkpoint loading, NVFP4 module wrapping, weight materialization, dtype/device placement, and the streaming-pipeline VAE relocation for both backends — the bf16 `pipe.to(...)`

shortcut is unsafe here because it would cast the quantized buffers.

```
import torch
from omegaconf import OmegaConf
from pipeline import CausalDiffusionInferencePipeline
from utils.config import normalize_config
from utils.inference_utils import prepare_single_prompt_inputs, save_video, setup_nvfp4_pipeline
prompt = "A compact silver robot walks through a clean robotics lab."
config = normalize_config(OmegaConf.load("configs/nvfp4/inference_nvfp4.yaml"))
device = torch.device("cuda")
torch.set_grad_enabled(False)
pipe = CausalDiffusionInferencePipeline(config, device=device)
setup_nvfp4_pipeline(pipe, config, device)
pipe.generator.model.eval().requires_grad_(False)
noise, prompts = prepare_single_prompt_inputs(config, prompt, device)
video = pipe.inference(noise=noise, text_prompts=prompts)
save_video(video[0], "videos/quickstart/sample_nvfp4.mp4", fps=24)
```

| Model | FPS ↑ | Params | VBench ↑ | Multi-shot |
|---|---|---|---|---|
| LongLive-1.3B | 20.7 | 1.3B | 84.87 | |
| LongLive-2.0-5B | 24.8 | 5B | 85.06 | ✅ |
| LongLive-2.0-5B-NVFP4-4Step | 29.7 | 5B | 84.51 | ✅ |
| LongLive-2.0-5B-NVFP4-2Step | 45.7 | 5B | 83.14 | ✅ |

This repository is released under the Apache 2.0 license. See LICENSE for details.

Please consider citing our work if you find them useful: