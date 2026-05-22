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
tldr: NVlabs 发布 LongLive 2.0，支持 NVFP4 的实时长视频生成框架
objective_summary: NVlabs 于 2026 年 5 月 13 日发布 LongLive 2.0，引入 NVFP4 并行基础设施，支持 W4A4
  量化和序列并行推理，在 2 步推理下达到 45.7 FPS 的实时长视频生成速度。该项目已于 2026 年 1 月被 ICLR-2026 接收。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - NVlabs
  technologies:
  - NVFP4
  - TriAttention
  - AR
  - DMD
  - RoPE
  - SANA-Video
  - KV Cache
  - BF16
  key_people: []
key_logic_flow:
- NVlabs 于 2026 年 5 月 13 日发布 LongLive 2.0，引入 NVFP4 并行基础设施，支持序列并行训练与推理、多镜头视频 AR 训练、W4A4
  量化及 NVFP4 KV Cache，在 2 步蒸馏推理下达到 45.7 FPS。
- LongLive 1.0 通过注意力汇聚（attention sink）、KV 重缓存（KV-recache）和流式长序列微调（streaming long tuning）实现实时交互式长视频生成，支持用户连续输入
  prompt 并实时生成对应视频。
- LongLive 支持 TriAttention KV 缓存压缩技术，可在无质量损失的情况下减少 50% KV 缓存占用。
- LongLive 1.0 已适配 KV-cache 相对 RoPE，支持无限长视频生成，并在线性注意力模型 SANA-Video 上实现 60 秒实时交互视频生成。
- LongLive 于 2026 年 1 月 27 日被 ICLR-2026 接收为会议论文。
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