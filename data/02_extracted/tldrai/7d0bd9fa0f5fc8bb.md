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
tldr: NVlabs 发布 LongLive 2.0，一个基于 NVFP4 精度的实时长视频生成框架，支持序列并行和多镜头训练，推理速度达 45.7 FPS，并开源了全部训练和推理代码。
objective_summary: NVlabs 于 2026 年 5 月 13 日发布 LongLive 2.0，这是一个面向长视频生成的并行基础设施。它支持
  NVFP4 精度（W4A4）、平衡序列并行、AR 多镜头训练、DMD 蒸馏和异步解码。LongLive 2.0-5B-NVFP4-2Step 模型在推理时达到
  45.7 FPS，VBench 评分为 83.14。此前 LongLive 1.0 已于 2025 年 9 月开源，并于 2026 年 1 月被 ICLR-2026
  接收。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - NVlabs
  technologies:
  - NVFP4
  - AR
  - DMD
  - TriAttention
  - KV Cache
  - RoPE
  - SANA-Video
  - BF16
  - W4A4
  - TransformerEngine
  - FourOverSix
  - VBench
  key_people: []
key_logic_flow:
- NVlabs 在 2026 年 5 月 13 日发布了 LongLive 2.0，一个基于 NVFP4 精度的长视频生成并行基础设施。
- LongLive 2.0 支持平衡序列并行、AR 多镜头或单镜头训练、NVFP4 精度下的 AR 训练与少步蒸馏。
- 推理方面，LongLive 2.0 支持 NVFP4 W4A4 推理、NVFP4 KV Cache、多镜头注意力汇聚、序列并行推理和异步解码。
- LongLive 2.0-5B-NVFP4-2Step 模型达 45.7 FPS，VBench 评分为 83.14；2.0-5B-NVFP4-4Step 为 29.7
  FPS，评分 84.51。
- LongLive 1.0 已于 2025 年 9 月开源全部代码与权重，并于 2026 年 1 月被 ICLR-2026 接收。
- LongLive 还支持 TriAttention 实现 50% KV 缓存压缩无质量损失，并已适配 SANA-Video 线性注意力模型以生成 60 秒交互视频。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: project
  name: LongLive
  canonical_name: NVlabs/LongLive
  url: https://github.com/NVlabs/LongLive
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVlabs 于 2025 年 9 月 29 日开源了 LongLive 的论文、全部训练和推理代码、模型权重以及演示页面。
  - LongLive 1.0 实现了实时交互式长视频生成，支持注意力汇聚、KV 重缓存和流式长视频微调技术。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: project
  name: LongLive 2.0
  canonical_name: NVlabs/LongLive
  url: https://github.com/NVlabs/LongLive
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 2026 年 5 月 13 日发布的 LongLive 2.0 是一个基于 NVFP4 精度的长视频生成并行基础设施。
  - LongLive 2.0 支持 NVFP4 推理（W4A4）和 NVFP4 KV Cache，推理速度最高达 45.7 FPS。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: model
  name: LongLive-1.3B
  canonical_name: LongLive-1.3B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - LongLive-1.3B 模型参数为 1.3B，推理速度 20.7 FPS，VBench 评分 84.87。
  - 该模型权重与训练推理代码一同于 2025 年 9 月 29 日开源发布。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: model
  name: LongLive-2.0-5B
  canonical_name: LongLive-2.0-5B
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - LongLive-2.0-5B 模型参数为 5B，推理速度 24.8 FPS，VBench 评分 85.06，支持多镜头生成。
  - 该模型的 NVFP4 4 步蒸馏版本达 29.7 FPS，2 步蒸馏版本达 45.7 FPS。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: project
  name: LongLive 1.0
  canonical_name: NVlabs/LongLive
  url: https://github.com/NVlabs/LongLive/tree/v1.0
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - LongLive 1.0 是原始版本，支持实时交互式长视频生成，现位于 v1.0 分支。
  - LongLive 1.0 的核心技术包括注意力汇聚、KV 重缓存和流式长视频微调。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: project
  name: TriAttention
  canonical_name: TriAttention
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LongLive 于 2026 年 4 月 12 日支持了 TriAttention KV 缓存压缩技术，实现 50% KV 缩减且无质量下降。
  article_id: 7d0bd9fa0f5fc8bb
- object_type: model
  name: SANA-Video
  canonical_name: SANA-Video
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 2025 年 11 月 3 日，LongLive 被实现在线性注意力模型 SANA-Video 上，使其能实时生成 60 秒交互视频。
  article_id: 7d0bd9fa0f5fc8bb
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