---
title: 'Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots'
source: https://cactuscompute.com/needle
author:
- '[[HenryNdubuaku]]'
published: '2026-08-10'
created: '2026-08-11'
manifest_dates:
- '2026-08-11'
description: 'Hey HN,Henry from Cactus here!We previously released Cactus Needle,
  a 14MB agentic LLM for tool call, device use, and structured extraction for phones,
  wearables, smart homes, small robots and microcontrollers. We got really great feedback
  here, and have now incorporated the suggestions to release Needle 2.The whole model
  is a single 14MB binary that runs a full session in 28MB of RAM; 45m parameters
  at 2bit compression. Needle hits 500 tokens/sec decode speed on a Raspberry Pi 5,
  sits between 400-1,500 tokens/sec on VR devices like Meta Quest 3S and Apple Vision
  Pro, and ranges 300-700 on sub-$200 phones such as the Samsung A-Series.On the tool
  call and mobile device use benchmarks, Needle 2 trades wins with closest small models
  like LFM2.5 230M and Apple Foundation Model, at 5x to 70x smaller, both at f16 vs
  Needle 2 at 2bit. Needle is based on Simple Attention Networks from our paper (https://arxiv.org/abs/2607.18363).Edge
  AI has lately meant Macs and PCs, but that is just 1.5 billion of over 21 billion
  connected IoT devices in the world today, and in emerging markets most phones ship
  under $200, no NPU, cheap GPUs. These include budget phones, Raspberry Pis, microcontrollers,
  wearables, small robots like Reachy Mini, and connected home devices.A conventional
  transformer of Needle''s width and depth spends 164 MFLOPs per token, and even one
  squeezed down to Needle''s parameter count spends 87, Needle spends 70. Even on
  a high-end phone, an always-on assistant lives inside a power budget; every MFLOP
  is milliwatt-hours, and Needle spends 7x to 85x fewer of them per token than the
  smallest performant LLMs. More about the architecture in the link.When we structure
  intelligence for consumer devices as functions with typed parameters, the only hard
  part is mapping a messy sentence onto them; which function, with which values. Our
  research found that when framed that way, the problem needs no world knowledge and
  no open-ended prose, which is why 45M parameters suffice.Needle 2 expands to structured
  extraction where the schema can be passed in-place of tools and the model returns
  structured output. You can use Needle as a text-classification model with an enum
  field, as a summarization model by providing a schema that extracts key fields,
  everything but free-range decode.Every product has its own tool vocabulary and fine-tuning
  needle helps it achieve frontier-level performance on custom tasks, so using the
  python package (https://github.com/cactus-compute/needle), Needle can be fine-tuned
  Needle on a Mac/PC in minutes to a few hours, with automated data-generation pipeline,
  just pass a couple samples.Nonetheless, every response carries a learned confidence
  score based our Cactus Hybrid technique. If above your threshold, act, below it,
  escalate to the cloud or bigger model. Combining Needle 2 with a private DeepSeek-v4-Flash
  deployment works particularly well for enterprise-level tasks at barely any cost,
  we can help with this setup.We have put a lot of thoughts into Needle 2 but might
  still be missing quite a lot, please use the playground in the provided link to
  test Needle and share your thoughts, always appreciated! Comments URL: https://news.ycombinator.com/item?id=49246804
  Points: 325 # Comments: 117'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d7dddac5c9c6043e
source_type: community_discussion
tldr: Cactus Compute 发布 Needle 2，一款 45M 参数、14MB 文件大小的端侧 agentic LLM，面向手机、手表、智能家居与机器人等低价设备。它通过全程
  2bit 量化训练与语法约束解码实现 800+ tok/s，并已被 Pebble 的 Index 01 应用本地采用。
objective_summary: Cactus Compute 发布 Needle 2，一个 45M 参数、14MB 文件大小、28MB 会话内存上限的 agentic
  语言模型，面向无 GPU/NPU、成本低于 200 美元的手机、手表、智能家居与小型机器人。模型在 1150 亿 token 语料上预训练并在 380 亿 token
  上后训练，全程采用 Cactus Quants 2bit 量化、Hadamard MLP、engram 与 256 token 滑动窗口，每 token 算力约
  70 MFLOPs。官方在 Mobile Actions 基准测得准确率 63.7%，接近 LFM2.5 230M 的 69.1%，但每 token 算力消耗低约
  6.6 倍。Pebble 已在无屏幕的 Index Ring 所配套的 Index 01 应用中本地运行该模型，将语音请求转为设备动作。
event_type: application_landing
epistemic_status: pr_statement
entities:
  companies:
  - Cactus Compute
  - Pebble
  - Google
  - Apple
  technologies:
  - Cactus Quants
  - QAT
  - Hadamard MLP
  - engram
  - KV cache
  - function calling
  - WASM
  - RISC-V
  - int8
  key_people: []
key_logic_flow:
- Cactus Compute 发布 Needle 2，一个 45M 参数、14MB 文件大小的 agentic 语言模型，目标硬件是内存仅数百 MB、无 GPU/NPU
  的低于 200 美元边缘设备。
- 核心思路是将设备控制重构为函数调用映射：只需把用户话语映射到带类型的函数参数上，因此 45M 参数即可胜任，无需世界知识与开放式文本生成。
- 模型从预训练到后训练全程使用 Cactus Quants 2bit 量化（而非事后量化），并采用 Hadamard MLP、engram 哈希表与 256 token
  滑动窗口，将每 token 算力降至 70 MFLOPs、内存固定为 28MB。
- 推理引擎为单一无依赖 C++ 二进制，启动时探测 CPU 并选择内核，语法约束解码在结构 token 上可跳过至多 98% 的词汇投影计算，算术路径端到端保持
  int8。
- 在五个公开函数调用基准上，Needle 2 的 Mobile Actions 准确率 63.7%，接近 LFM2.5 230M 的 69.1%，而每 token
  算力消耗约为后者的七分之一。
- Pebble 已在无屏幕的 Index Ring 配套的 Index 01 应用中本地运行 Needle 2，将语音请求转为动作，不依赖网络连接。
object_mentions:
- object_type: model
  name: Needle 2
  canonical_name: Needle 2
  url: https://cactuscompute.com/needle
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Needle 2 是一个 45M 参数、文件大小仅 14MB 的 agentic 语言模型，面向手机、手表、智能家居和机器人等低价边缘设备设计。
  - Needle 2 从预训练到后训练全程使用 Cactus Quants 2bit 量化，因此部署的 14MB 模型就是被训练的模型，不做事后量化。
  - 官方评测中 Needle 2 在 Mobile Actions 基准上准确率为 63.7%，每 token 算力消耗约 70 MFLOPs。
  article_id: d7dddac5c9c6043e
- object_type: product
  name: Pebble Index Ring
  canonical_name: Pebble Index Ring
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Pebble 作为可穿戴行业的先驱，在 Index 01 应用中本地运行 Cactus Needle，将语音请求转为设备动作而不依赖网络。
  - Pebble Index Ring 没有屏幕，因此用户对它说话时动作必须每次都能执行，无论是否联网。
  article_id: d7dddac5c9c6043e
- object_type: product
  name: Pebble Index 01 app
  canonical_name: Pebble Index 01 app
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Pebble 的 Index 01 应用在本地运行 Cactus Needle，而不是依赖云端，因为模型体积小且性能从不让人失望。
  article_id: d7dddac5c9c6043e
- object_type: model
  name: LFM2.5 230M
  canonical_name: LFM2.5 230M
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - LFM2.5-230M 是评测基准模型，在 Mobile Actions 上准确率 69.1%，但每 token 算力消耗约 460 MFLOPs，约为 Needle
    2 的 6.6 倍。
  article_id: d7dddac5c9c6043e
- object_type: model
  name: FunctionGemma 270M
  canonical_name: FunctionGemma 270M
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - FunctionGemma 270M 是评测基准模型之一，在 DroidCall 测试上准确率 17.5%，与 Needle 2 的 17.0% 接近。
  article_id: d7dddac5c9c6043e
- object_type: model
  name: Apple FM
  canonical_name: Apple FM
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Apple FM 是 Apple 的端侧模型，在 Mobile Actions 基准上以 on-device 方式取得 57.6% 的准确率。
  article_id: d7dddac5c9c6043e
extract_result: success
impact_score:
  score: 7.5
  reason: Needle 2 代表了端侧 AI 的极端工程化方向：将 LLM 从通用对话压缩为专用函数调用映射器，以 45M 参数/14MB 体积/28MB
    内存跑在低于 200 美元的设备上。它验证了「设备控制不需要 frontier model」这一范式，对超过 200 亿台的 IoT 设备市场具有直接商业意义。但影响范围目前主要局限于边缘
    AI/IoT 垂直领域，尚未达到改变全行业范式的程度。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 端侧 agentic LLM 的极致压缩与函数调用范式的工程可行性
hype_assessment:
  level: low
  reason: 虽然标题使用了 800+ tok/s 等吸睛数字，但正文提供了大量可验证的技术细节：全程 2bit QAT（非事后量化）、Hadamard MLP、engram
    哈希表、256 token 滑动窗口、具体基准测试（Mobile Actions 63.7% vs LFM2.5-230M 69.1%）、以及 Pebble
    Index Ring 的真实生产部署。没有滥用「颠覆」「革命性」等空泛词汇，架构选择和性能数据均具备可复现性。
information_entropy: high
domain_disruption:
  technical_innovation: 将设备控制重构为结构化函数调用问题，而非开放式文本生成；采用全程 2bit QAT 训练（权重、激活、KV cache
    统一量化），配合 Hadamard MLP、engram 哈希表与语法约束解码（跳过 98% 词汇投影），实现了单一无依赖 C++ 二进制跨平台推理。这是端侧模型在工程实现上的系统性极致压缩。
  business_model: 为海量低成本 IoT 设备（无 GPU/NPU、数百 MB RAM）提供离线、零订阅、隐私优先的本地 AI 交互层；支持在 Mac/PC
    上快速微调以适配特定设备的工具词汇，可能重塑智能家居、可穿戴设备和机器人行业的交互协议与 SaaS 收费模式。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: 端侧AI Agent是覆盖210亿IoT设备的确定性趋势。Cactus Compute的核心赌注——将设备控制重构为函数调用映射（而非开放式聊天）——精准切中了低于200美元设备的算力与内存约束。全程2bit
    QAT训练、语法约束解码可跳过98%词汇投影、模型-推理协同设计（单一无依赖C++二进制）构成了深厚的工程护城河，且已有Pebble的Index 01应用在生产环境落地验证。若能在碎片化硬件生态（ARM/RISC-V/WASM）中成为事实标准，3-5年内将成为边缘智能的基础设施层。主要风险在于小团队面对Apple、Google等巨头自有端侧方案的挤压，以及在21亿设备碎片生态中的规模化交付与生态运营能力。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Cactus Compute
- Pebble
competitive_casualty:
- Liquid AI
- Amazon
- Google
- 依赖云端API的IoT语音方案
- 高参数端侧模型竞品
market_opportunities:
- 针对智能家居、可穿戴及低价手机场景，开发者可基于超轻量端侧模型构建离线语音控制与函数调用方案，摆脱云端依赖并降低硬件成本门槛。
- 端侧模型私有化微调服务存在创业机会：为硬件厂商提供分钟级到小时级的设备专属工具词汇训练，打造“即插即用”的端侧 Agent 定制平台。
- 随着端侧 Agent 直接控制物理设备并处理敏感语音指令，围绕本地推理隐私合规、置信度阈值管理与边缘-云回退路径的安全审计工具将成为新兴需求。
risk_matrix:
  regulatory: 端侧处理语音数据可能触发 GDPR/CCPA 等隐私法规，无屏幕可穿戴设备（如戒指）持续采集语音的生物特征合规风险尤为突出；此外，2bit
    量化模型的可解释性与欧盟 AI Act 对高风险系统的审计要求存在潜在冲突。
  technological: 状态空间模型、线性注意力等长上下文技术可能突破 256 token 滑动窗口限制；Apple/Google/Qualcomm 等巨头端侧框架若原生支持极端量化将挤压自研
    C++ 引擎生态；更大规模的轻量化模型（如 LFM 系列）可能通过效率优化进一步下沉。
  competitive: Apple Intelligence、Google Gemini Nano 等巨头端侧生态可能通过系统级集成形成锁定；开源社区（llama.cpp、MLX）快速跟进
    2bit 量化技术，可能催生免费替代方案；OEM 大规模采购意愿尚待验证，仅靠 Pebble 单一客户背书难以支撑持续竞争优势。
  ethical: 离线运行导致内容过滤和偏见修正困难，错误函数调用可能直接引发物理安全风险（如智能家居误操作）；语音戒指的持续监听模式存在隐私侵犯和社会接受度争议；低算力设备上的
    AI 普及可能加速低端服务业自动化替代。
  additional:
  - 2bit 量化模型的对抗鲁棒性尚未充分验证，存在被恶意语音指令操控的安全隐患
  - 商业模式可持续性存疑：B2B 硬件授权面临开源替代品的价格压力
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: monitor
---

- 45M
- Params
- 800+ tok/s
- Pi5 prefill
- 500+ tok/s
- Pi5 decode
- CQ2-bit
- Compression
- 14 MB
- File size
- 28 MB
- Session RAM

## Our Bet

**Bringing On-Device AI to <$200 Devices:** Edge AI has lately meant Macs and PCs, but the edge is mostly cheap hardware: over 21 billion connected IoT devices against roughly 1.5 billion PCs, and in emerging markets most phones ship under $200. Count budget phones, Raspberry Pis, microcontrollers, wearables, small robots like Reachy Mini, and connected home devices, and roughly four in five edge devices cost under $200. That is the hardware Needle targets: no GPU, no NPU, a few hundred MB of RAM.

**Function Call & Device Use:** Turning on a light does not need a frontier model. A watch, a home, a robot: each already exposes its abilities as functions with typed parameters, so the only hard part is mapping a messy sentence onto them: which function, with which values. Framed that way, the problem needs no world knowledge and no open-ended prose, which is why 45M parameters suffice where chat needs billions. That smaller formulation is the bet everything else follows from.

**Extraction & Structured Outputs:** The schema is the interface, and the same formulation covers documents: a schema plus a paragraph returns typed fields, an enum field is a classifier, an array field collects a list in one call. We enforce this with a contract, not a convention: every turn is answered with a call envelope, the empty call is the refusal, and a byte-level grammar compiled from the declared schemas constrains every token. The grammar carries the syntax, so all 45M parameters go to choosing functions and grounding arguments in the user's words.

**Edge-Cloud Collaboration:** No small model covers everything, so Needle says so instead of guessing: every response carries a learned confidence score, and off-topic requests return the empty call. Above your threshold, act; below it, re-ask or escalate to the cloud. Most device requests are routine control, so escalation stays rare and the default path stays private, instant, and free.

**Lossless 2bit Quantization:** Small models break under post-hoc quantization, so we never quantize post-hoc: Needle 2 trains against Cactus Quants from pretrain through post-train, weights, activations, and KV cache alike. The 2bit model you deploy is the model that was trained. That is what fits 45M parameters into 14MB with nothing lost on our battery.

**Co-designed Model & Inference:** Every architectural choice was benchmarked on the target hardware before it earned its parameters, and the deliverable is the pair, not the weights: a single dependency-free C++ binary that probes the CPU at startup and picks its kernels, with the model, tokenizer, and grammar compiler sealed inside. One artifact runs from Cortex-M to x86 to WebAssembly. There is nothing to install and nothing to download.

**Fine-tune on your Mac/PC:** Every product has its own tool vocabulary, and a 45M model is small enough to retrain where it runs: the repo and python package tune and test on your own computer in minutes to a few hours. Ship a Needle that speaks your device's tools, not a generic assistant.

## Production

Needle is production-ready for products that require a minimal RAM footprint, low latency, privacy, and offline reliability. Pebble - the pioneer of the modern wearable industry - runs it locally in the Index 01 app to turn spoken requests into actions without depending on a network connection.

The Pebble Index Ring has no screen. So when you speak to it, the action just has to happen, every time, with or without internet connection. We run Cactus Needle locally in the app, instead of relying on the cloud. The model's footprint is tiny and the performance never lets us down.


## Architecture

Needle 2 is pretrained on a proprietary 115B-token corpus and post-trained on 38B tokens with compact reasoning traces and careful dataset distribution design. For scale: LFM2.5-230M was pretrained on 19 trillion tokens, roughly 120× Needle's total, and the evaluation below shows the two trading wins. Each component exists to buy capability without buying bandwidth. The Hadamard MLP replaces the usual dense up-and-down projections with a fixed Walsh transform and learned diagonals, so the channel mixing that dominates a small model's weight reads costs almost no parameters at all. The engram moves world knowledge out of the stack into hashed n-gram tables that are read a few rows per token: capacity that is nearly free at decode time, which matters on devices where every megabyte read from flash is latency and battery. The multi-lane residual streams give a 27-layer, 512-wide network the routing flexibility of a much wider one, at the cost of a few dot products per layer rather than more attention or MLP volume.

The memory system is designed backwards from fixed-RAM devices. Attention uses a 256-token sliding window so the KV cache is bounded no matter how long a session runs, and the system prompt and tool declarations are pinned as permanent sinks so the one thing a tool-calling model must never forget—its tools—is structurally unable to be evicted. The cache itself is trained with QAT, and weights are stored in Cactus Quants at a mixed bits per weight averaging 2bit. The result is that quality decisions and deployment decisions stay decoupled: one trained model, specialized to whatever precision and window a target device can afford.

The engine earns its speed from what it refuses to compute. Weights never decompress into RAM: the 2-bit codes are expanded inside vector registers, fused into integer dot products, so resident memory stays at blob size and the arithmetic path is int8 end to end—activations, KV cache, and the lane routing tables alike. The grammar is an optimization, not just a guarantee: because the matcher knows which tokens are legal before the logits exist, the engine computes output scores only for candidate rows, skipping up to 98% of the vocabulary projection on structural tokens, and skips it entirely on steps whose output is already forced. One universal binary probes the CPU at startup and self-selects its kernel tier—SDOT, NEON, AVX2, RISC-V vectors, wasm SIMD, or scalar—and the thread pool spins through the short serial sections of a token instead of sleeping, which alone nearly doubled decode. None of this changes a single output: every trick is either exact or validated token-for-token against the reference path.

All of it is ultimately an energy argument. On device silicon, moving a byte out of flash or DRAM costs orders of magnitude more than a multiply-accumulate, so the budget that matters is FLOPs per token and bytes per token together. The architecture cuts the first: a conventional transformer of Needle's width and depth spends 164 MFLOPs per token, and even one squeezed down to Needle's parameter count spends 87, because every parameter it owns must be exercised through a matmul. Needle spends 70, and keeps a fifth of its parameters as gathered memory that costs no arithmetic at all. The binary cuts the second, as the engine section showed: nothing rematerializes, the arithmetic stays int8 end to end, and the grammar prunes compute outright, so decoding a token reads at most the 14MB blob once, and on structural tokens meaningfully less. This is what battery life is made of. Even on a high-end phone, an always-on assistant lives inside a power budget; every MFLOP is milliwatt-hours, and Needle spends 7× to 85× fewer of them per token than the models it is benchmarked against.

### Compute per token

| Model | Params | Matmul-active | MFLOPs / token |
|---|---|---|---|
| Needle 2 | 45M | 35M | 70 |
| Same-shape transformer, dense MLP | 82M | 82M | 164 |
| Transformer at matched params | 43M | 43M | 87 |
| LFM2.5 230M | 230M | 230M | 460 |
| FunctionGemma 270M | 270M | 270M | 540 |
| Apple FM | ~3B | ~3B | ~6,000 |

Bounded session memory is what puts microcontrollers in reach. Because the sliding window caps state, Needle 2's RAM is a deterministic 28MB ceiling, not a curve that grows with conversation length. That fits MCU-class parts with external RAM, such as ESP32-P4 with 32MB of PSRAM, or STM32H7 and NXP i.MX RT boards with SDRAM. The engine compiles single-threaded for bare metal and ships as a static library for Cortex-M4, M7, and M55.

## Evaluation

We evaluate on five public function-calling benchmarks: Google's Mobile Actions, DroidCall, the Seal-Tools in-domain and out-of-domain tests, and BFCL v4 single-turn. Scoring is ordered strict exact match: a row passes only if the function names, the call order, and every argument value match. All Needle 2 numbers are measured end-to-end through the shipped C++ engine in its production configuration: CQ2-bit weights, tool retrieval on, and the 256-token sliding KV window. Nothing is relaxed for benchmarking; the numbers reflect the exact engine a device runs, window eviction included. Baselines run the released checkpoints under vLLM at full context, and Apple FM runs on-device.

Two asymmetries make this comparison hard, and we state both upfront. Precision: the baselines stay at f16 deliberately, because conventional post-training quantization to 2 bits collapses models that were never trained for aggressive compression, while Cactus Quants is baked into Needle's training from the ground up. That skew favors the baselines. Scope: Needle is trained specifically for agentic tool calling and nothing else, while every baseline is a general language model carrying chat, prose, and world knowledge alongside its tool calling. That skew favors Needle. There is no clean way to level both at once, so we do not try. The tables answer one narrow question: which model executes tool calls correctly within an on-device budget. We accept the skew; it still paints the picture we intend.

### Mobile Actions (961 rows)

| Model | Accuracy | Name acc. | Non-empty | 1-call | 2-call |
|---|---|---|---|---|---|
| LFM2.5 230M (f16, vLLM) | 69.1 | 93.0 | 98.9 | 76.1 | 55.0 |
| FunctionGemma 270M (f16, vLLM) | 64.0 | 87.3 | 98.9 | 73.0 | 46.2 |
| Needle 2 (CQ2-bit) | 63.7 | 98.3 | 99.4 | 71.3 | 48.4 |
| Apple FM (on-device) | 57.6 | 94.2 | 95.5 | 64.5 | 43.8 |

### DroidCall test split (200 rows)

| Model | Accuracy | Name acc. | Non-empty | 1-call | 2-call |
|---|---|---|---|---|---|
| FunctionGemma 270M (f16, vLLM) | 17.5 | 37.5 | 59.5 | 22.7 | 0.0 |
| Needle 2 (CQ2-bit) | 17.0 | 36.5 | 47.5 | 22.1 | 0.0 |
| LFM2.5 230M (f16, vLLM) | 11.0 | 21.5 | 22.5 | 14.3 | 0.0 |

### Seal-Tools in-domain (700 rows)

| Model | Accuracy | Name acc. | 1-call | 2–3-call | 4+-call |
|---|---|---|---|---|---|
| Needle 2 (CQ2-bit) | 32.6 | 64.9 | 63.0 | 21.8 | 14.6 |
| LFM2.5 230M (f16, vLLM) | 26.9 | 45.4 | 54.5 | 17.1 | 10.4 |
| FunctionGemma 270M (f16, vLLM) | 16.3 | 56.0 | 47.0 | 4.5 | 2.1 |

### Seal-Tools out-of-domain (654 rows)

| Model | Accuracy | Name acc. | 1-call | 2–3-call | 4+-call |
|---|---|---|---|---|---|
| Needle 2 (CQ2-bit) | 28.7 | 58.7 | 56.4 | 27.1 | 15.4 |
| LFM2.5 230M (f16, vLLM) | 17.0 | 35.0 | 42.6 | 13.7 | 9.8 |
| FunctionGemma 270M (f16, vLLM) | 15.6 | 48.9 | 50.0 | 11.0 | 6.3 |

Needle was not trained for general function calling: its corpus is consumer device actions—smart home, mobile, wearables, TV, car—plus structured extraction, and BFCL's general-purpose and enterprise API surfaces, including the Java and JavaScript SDK categories, sit entirely outside that distribution. It extrapolates nonetheless: on Python simple calls it lands within a point of FunctionGemma, a model six times larger trained for exactly this task, and it keeps a 93.4 well-formed rate across all 3,641 rows. The gap concentrates where its training data has never been: Java, JavaScript, and the parallel multi-call categories.

### BFCL v4 single-turn (3,641 rows)

| Category | Apple FMon-device | LFM2.5 230Mf16 · vLLM | FunctionGemma 270Mf16 · vLLM | Needle 2CQ2-bit |
|---|---|---|---|---|
| Simple | 73.3 | 63.2 | 48.1 | 40.8 |
| — Python | 86.8 | 85.5 | 62.3 | 61.2 |
| — Java | 67.0 | 48.0 | 38.0 | 29.0 |
| — JavaScript | 66.0 | 56.0 | 44.0 | 32.0 |
| Multiple | 84.0 | 78.5 | 60.0 | 57.0 |
| Parallel | 65.0 | 64.0 | 36.5 | 30.0 |
| Parallel multiple | 52.0 | 51.5 | 30.5 | 22.5 |
| Live simple | 70.5 | 45.0 | 33.7 | 36.8 |
| Live multiple | 45.9 | 47.8 | 25.2 | 27.9 |
| Live parallel | 50.0 | 43.8 | 18.8 | 25.0 |
| Live parallel multiple | 58.3 | 45.8 | 25.0 | 29.2 |
| Relevance | 100.0 | 68.8 | 81.2 | 81.2 |
| Irrelevance | 28.3 | 77.7 | 72.1 | 60.8 |
| Overall | 61.7 | 60.8 | 46.1 | 42.6 |
| Well-formed rate | 95.0 | 94.2 | 100.0 | 93.4 |