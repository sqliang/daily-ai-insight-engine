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
impact_score:
  score: 7.0
  reason: LongLive 2.0 不是一个范式转移级别的突破，但它是实时视频生成领域一个重要的工程里程碑。核心评分依据：(1) 从 1.0 的 20.7
    FPS 跃升至 2.0 的 45.7 FPS，性能翻倍以上，且模型参数从 1.3B 扩大到 5B，同时保持 VBench 质量分数基本不降（83.14 vs
    84.87），这在实时视频生成中极为罕见；(2) NVFP4 W4A4 量化基础设施的构建具有通用参考价值，不局限于单一模型；(3) ICLR-2026 接收增加了学术可信度；(4)
    Apache 2.0 开源且包含完整训练/推理代码和模型权重，降低了社区复现门槛。但局限在于：依赖 NVIDIA 专有硬件生态（NVFP4），且实时交互式长视频生成的应用场景仍在探索中，尚未形成产品级的行业冲击。综合判断为重要基础设施级发布，改变本地竞争格局但未构成范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: NVFP4 W4A4量化+序列并行+DMD少步蒸馏的组合拳，如何在5B参数模型上实现45.7 FPS实时推理，以及开源代码能否在自己硬件上复现
hype_assessment:
  level: low
  reason: README 全文以技术规格和基准测试为主，无'颠覆'、'革命性'、'AGI'等 PR 滥用词汇。所有性能声明均有明确的对比表格支撑（包含 FPS、参数量、VBench
    分数、多镜头支持四个维度）。代码示例完整可运行，配置路径清晰。学术同行评审（ICLR-2026）进一步验证了其技术声明的可信度。判定为实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破在于构建了一套完整的 NVFP4 量化并行基础设施，覆盖训练（平衡序列并行 AR 训练 + DMD 少步蒸馏）和推理（W4A4
    推理 + NVFP4 KV Cache + 序列并行 + 异步解码）全链路。配合 TriAttention 50% KV 缓存无损压缩和 KV-cache
    相对 RoPE 适配（支持无限长视频），形成了从内存带宽、计算效率到生成长度的系统性优化方案。这不是单一算法改进，而是系统级的工程架构创新。
  business_model: 45.7 FPS 的实时推理能力将单卡视频生成的边际成本降至可商业化水平，使实时交互式 AI 视频应用（游戏引擎辅助、虚拟主播、交互式广告、实时视频编辑）从'可能但昂贵'进入'实用且经济'阶段。NVFP4
    生态锁定效应也可能推动 NVIDIA 数据中心 GPU 的采购需求，强化其在 AI 推理硬件市场的话语权。
engineering_complexity: production_ready
compound_value:
  score: 8.0
  reason: LongLive 2.0 构建了从硬件量化（NVFP4）、模型架构（Attention Sink/KV-recache/TriAttention）、训练范式（序列并行AR训练+DMD少步蒸馏）到推理优化（异步解码/流式VAE）的全栈技术壁垒。核心复利逻辑在于：①NVFP4是NVIDIA
    Blackwell架构的专有量化格式，形成硬件-软件协同锁定，每增加一个采纳者即加固NVIDIA GPU生态；②TriAttention 50% KV无损压缩、KV-cache相对RoPE无限长视频生成、序列并行推理等模块化技术可独立迭代，形成持续积累的技术飞轮；③2-Step蒸馏模型在VBench仅微降至83.14的情况下达到45.7
    FPS，实用化路径清晰，已跨越从'可行'到'可用'的阈值；④Apache 2.0开源降低采纳门槛加速生态扩散，但NVFP4绑定确保核心价值回流至NVIDIA。ICLR-2026接收提供学术正统性背书。风险在于实时交互视频生成的市场需求尚处早期验证阶段，且NVFP4的封闭性可能限制跨硬件生态扩展。综合判断：3-5年内大概率成为NVIDIA视频AI基础设施的关键支柱，具备强复利效应。
value_capture_layer: hardware_compute
moat_impact: strengthens_monopoly
key_beneficiaries:
- NVIDIA
- CoreWeave
- Lambda Labs
competitive_casualty:
- Runway
- Pika Labs
- AMD
market_opportunities:
- 实时视频生成达到45.7 FPS意味着视频生成从'离线渲染'进入'实时交互'时代，创业团队可基于LongLive 2.0的Apache 2.0开源代码，开发面向直播电商、虚拟主播、游戏实时过场动画等低延迟场景的垂直产品，利用NVFP4量化在消费级GPU上实现可部署的推理性能
- NVFP4的W4A4量化训练+推理全栈方案为视频生成模型的端侧部署提供了可复制的技术路径，硬件厂商和模型优化团队可借鉴其'量化训练+少步蒸馏+KV缓存压缩'的组合策略，构建面向移动端和边缘设备的视频生成SDK
- 多镜头AR训练和序列并行推理的工程方案为长视频内容创作工具提供了新范式，建议视频编辑SaaS厂商关注该架构，探索将实时交互式视频生成集成到专业创作工作流中，实现'边说边生成'的新型内容生产模式
risk_matrix:
  regulatory: 实时交互式长视频生成技术将显著降低深度伪造的制作门槛和成本，45.7 FPS的实时性意味着可生成直播级别的虚假视频流，预计将加速欧盟AI
    Act对生成式视频的监管细则出台，以及中国《深度合成管理规定》的执法力度升级；同时，开源模型权重（Apache 2.0）的广泛可用性使得出口管制和技术封锁难以有效执行，可能引发地缘政治层面的技术扩散争议
  technological: 该架构深度绑定NVIDIA的NVFP4量化生态（依赖TransformerEngine或FourOverSix后端），若AMD、Intel等竞争对手推出不兼容的量化方案，或开源社区发展出硬件无关的替代方案（如GGUF/Triton），当前技术栈可能面临迁移成本；此外，SANA-Video线性注意力路线的探索表明DiT架构并非唯一路径，存在架构替代风险
  competitive: NVIDIA通过NVFP4将硬件优势（H100/B200的FP4支持）与软件生态（LongLive开源）深度绑定，形成'硬件+框架+模型'三位一体的竞争壁垒，对Google（Veo）、Meta（Movie
    Gen）、Runway等纯软件方案提供商构成生态挤压；同时，45.7 FPS的性能基线大幅提高了视频生成赛道的入场门槛，后来者需要在速度或质量上实现数量级超越才有竞争力
  ethical: 实时交互式视频生成（用户连续输入prompt即可实时生成对应视频）大幅降低了生成虚假视频内容的技术门槛，结合多镜头能力和60秒时长支持，可用于实时Deepfake直播、虚假新闻视频生成等恶意场景；5B参数模型的开源使得恶意行为者可在消费级硬件上部署，现有内容审核机制难以应对实时生成的视频流，存在严重的社会信任侵蚀和就业冲击风险（影视制作、直播行业）
  additional:
  - 能源消耗与算力集中风险：5B模型实现45.7 FPS依赖NVIDIA最新GPU的FP4算力，大规模部署将加剧算力资源向头部云厂商集中，中小机构面临算力获取不平等
  - 学术生态失衡风险：NVIDIA以硬件厂商身份主导开源模型发布，其NVFP4技术路线可能通过开源生态锁定学术界的研究方向，削弱对硬件无关的量化技术和替代架构的探索动力
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: strategic_invest
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