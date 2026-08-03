---
title: 'Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series
  Mac'
source: https://github.com/drumih/turbo-fieldfare
author:
- '[[gitpusher42]]'
published: '2026-07-29'
created: '2026-07-30'
manifest_dates:
- '2026-07-30'
description: 'Hi HN,I built a specialized inference engine for running 4-bit Gemma
  4 26B-A4B-IT on any M-series Mac using about 2 GB of RAM. It is called TurboFieldfare
  and is written in Swift and Metal.I have always adored on-device AI. It feels like
  magic that you can run a powerful NN on your Mac or iPhone. So I wanted to push
  the limits a bit and run a model whose weights don’t fit in memory.The model’s 4-bit
  quantized weights occupy roughly 14 GB, which makes running it with conventional
  inference tools almost impossible on an 8 GB or even 16 GB Mac once the OS, applications,
  and KV cache are included.The trick is to keep the shared part of the model and
  the KV cache in RAM, then stream only the routed experts needed for each token from
  SSD. An SSD is way slower than RAM, so the runtime uses a small expert cache and
  bounded parallel `pread`. While those reads are in flight, the GPU runs the shared
  part of the layer.I ran more than 100 experiments. Most didn’t work. A few got me
  here. The experiments are described in the GitHub repo.It currently generates 5–6
  tok/s on an 8 GB M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro.I also added
  an experimental OpenAI-compatible local server. It supports streaming and tool calls,
  and reuses one prompt prefix from the KV cache.Try it! The Mac app is easy to install.
  On the first run, it will download 15 GB of weights from Hugging Face. The model
  is surprisingly capable.I would love any kind of feedback! Comments URL: https://news.ycombinator.com/item?id=49098510
  Points: 793 # Comments: 280'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 7af3ac00212dbeff
source_type: community_discussion
tldr: TurboFieldfare 是一个开源的 Swift + Metal 推理引擎，可在任意 Apple Silicon Mac（含 8 GB 内存机型）上以约
  2 GB 内存运行 Gemma 4 26B-A4B。它通过从 SSD 流式加载路由专家避免载入完整 14.3 GB 模型，实测 M2 解码 5.1-6.3 tok/s、M5
  Pro 达 31-35 tok/s。
objective_summary: iOS 与 Metal 工程师 Andrey Mikhaylov 发布了 TurboFieldfare，一个针对 Google
  Gemma 4 26B-A4B 指令模型的专用 Swift + Metal 推理运行时。它将共享 1.35 GB 核心与 FP16 KV 缓存驻留内存，按 token
  从 SSD 流式加载所需专家，使模型可在最低 8 GB 内存的 Mac 上以约 2 GB 权重内存运行。项目提供原生 Mac 应用、CLI 与实验性 loopback
  OpenAI 兼容服务器，实测在 8 GB M2 MacBook Air 上解码速度为 5.1-6.3 tok/s，在 24 GB M5 Pro 上为 31-35
  tok/s。代码以 Apache License 2.0 开源，模型权重需从 Hugging Face 固定版本单独下载。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - Hugging Face
  technologies:
  - Gemma 4 26B-A4B
  - Swift
  - Metal
  - MLX
  - MoE
  - KV cache
  key_people:
  - Andrey Mikhaylov
  - Maarten Grootendorst
key_logic_flow:
- TurboFieldfare 是一个面向 Apple Silicon Mac 的专用 Swift + Metal 推理运行时，目标是在约 2 GB 内存中运行
  Gemma 4 26B-A4B，最低支持 8 GB 内存机型。
- 其核心机制是仅将共享的 1.35 GB 核心权重与 FP16 KV 缓存驻留内存，其余路由专家按每个 token 从 SSD 流式加载，从而避免一次性载入完整的
  14.3 GB 模型。
- 项目以 Swift 包形式提供六个产品，包括原生 Mac 应用、命令行界面、OpenAI 兼容的 loopback 服务器、流式安装器与一次性解码服务。
- 实测性能显示，8 GB M2 MacBook Air 解码速度为 5.1-6.3 tok/s，24 GB M5 Pro 为 31-35 tok/s，结果受提示长度与页面缓存状态影响。
- TurboFieldfare 仅支持文本推理，采用 4-bit MLX affine 量化与 8-bit 路由器，代码以 Apache License 2.0
  开源，模型权重需从 Hugging Face 单独下载。
object_mentions:
- object_type: project
  name: drumih/turbo-fieldfare
  canonical_name: drumih/turbo-fieldfare
  url: https://github.com/drumih/turbo-fieldfare
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - TurboFieldfare 是一个用 Swift 和 Metal 编写的专用推理运行时，可在约 2 GB 内存中运行 Gemma 4 26B-A4B 模型，最低支持
    8 GB 内存的 Apple Silicon Mac。
  - 该项目提供原生 Mac 应用、命令行界面、流式安装器和实验性 OpenAI 兼容服务器，源代码以 Apache License 2.0 开源。
  article_id: 7af3ac00212dbeff
- object_type: model
  name: Gemma 4 26B-A4B
  canonical_name: Gemma 4 26B-A4B
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Gemma 4 26B-A4B 是 Google 的指令微调模型，共有 260 亿参数，每个 token 约激活 38.8 亿参数，安装后占用约 14.3
    GB 存储空间。
  - TurboFieldfare 仅将共享核心与 FP16 KV 缓存驻留内存，按 token 从 SSD 流式加载所需专家，使 Gemma 4 26B-A4B
    可在 8 GB 内存的 Mac 上运行。
  article_id: 7af3ac00212dbeff
extract_result: success
impact_score:
  score: 5.5
  reason: 评分依据：这是 Show HN 社区讨论帖，工程价值真实且测量严谨——正文给出 103 条实测记录、8GB M2 与 24GB M5 Pro 的明确吞吐数据，其
    SSD 流式加载 MoE 专家的思路有望被 llama.cpp、MLX 等主流运行时借鉴，从而改写 Apple Silicon 上本地大模型的内存经济学，属于对局部竞争格局（边缘/本地推理）的实质性影响；但它本质是单模型专用运行时（仅支持
    Gemma 4 26B-A4B）、要求 macOS 26 + Metal 4 + Swift 6.2 的较新平台栈，受众有限，且 8GB 机型上 5-6 tok/s
    的吞吐决定了它难以短期改变消费级体验，也未触及训练或推理范式的根本性变革。综合判断为重要但局部性的技术突破，冲击力中等偏上。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 2GB 内存跑 26B MoE 模型的 SSD 专家流式技术，以及对本地推理硬件门槛的改写
hype_assessment:
  level: low
  reason: 判定依据：正文通篇是工程细节与实测数据（1.35GB 共享核心 + 约 2GB 权重内存、MLX affine 4-bit 量化、字节范围流式安装器、103
    条基准记录），并主动声明吞吐受页面缓存与提示长度影响、'是参考点而非性能天花板'，同时坦诚列出限制（纯文本、arm64-only、不支持旧系统），未出现'颠覆'、'革命性'等
    PR 滥用词汇，结论与实际测量一致，属实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 针对 MoE 架构的选择性专家 SSD 流式加载——仅常驻共享核心权重与 FP16 KV cache，按 token
    从 SSD 拉取所需路由专家，将内存占用从完整模型尺寸（14.3GB）解耦至约 2GB；配套字节范围流式安装器避免中间检查点落盘，将安装峰值内存与磁盘占用同时压到有界。该思路对通用运行时（llama.cpp/MLX）具有直接借鉴价值，可显著降低
    Apple Silicon 上本地 MoE 大模型的内存门槛。
  business_model: Apache 2.0 开源，推动本地推理在消费级 Mac（含 8GB 入门机型）上的普及，可能分流一部分云端 API 推理负载；同时放大
    Google Gemma 开放模型生态的部署半径，对'高端硬件/云 API 才能跑大模型'的传统商业模式构成边际冲击，也为 Mac 本地优先的 AI 应用铺路。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 该项目本身的独立投资价值有限——Apache 2.0 开源、个人维护者主导、仅针对单一模型（Gemma 4 26B-A4B）专用运行时，难以直接捕获商业价值。但需区分资产与信号：它验证了'SSD
    流式 MoE 专家卸载'这一技术路径，通过仅驻留 1.35GB 共享核心+KV cache、按 token 从 SSD 拉取路由专家，将 26B 稀疏模型压缩进
    2GB 内存运行，这在 8GB 内存 Apple Silicon 设备上开辟了此前不存在的端侧推理能力边界。该技术范式若被 MLX/llama.cpp 等主流框架吸收，将成为端侧推理的标准基础设施组件，具备跨模型、跨硬件复用的复利潜力；但若主流框架快速跟进，本项目作为'单模型专用运行时'的独立壁垒会被侵蚀。综合判断：处于'细分赛道基础设施候选'区间，方向正确但需观察其能否从专用引擎进化为通用方案，以及端侧推理市场随
    Apple Silicon 保有量增长的实际扩容速度。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Apple
- Google
- Hugging Face
competitive_casualty:
- 消费级云端推理 API 服务商
- 未跟进 SSD 流式 MoE 技术的通用本地推理框架（如 llama.cpp/MLX 若慢一步）
- 高内存 Mac 硬件升级溢价空间
market_opportunities:
- 开发者可借鉴"按 token 从 SSD 流式加载 MoE 路由专家"的推理范式，面向 8GB 内存 Mac、AI PC 或移动端等内存受限设备，打造本地大模型推理工具与中间件
- 该项目内置的 OpenAI 兼容 loopback 服务器，让开发者可在本地 Mac 上搭建零云依赖的 AI 应用原型，可作为"本地优先 AI 应用"与隐私敏感场景（如企业内网、个人助手）的落地切入点
- 围绕 .gturbo 流式安装/重打包格式与社区基准测试形成的工具链，可延伸为针对 MoE 大模型本地化部署的优化咨询、量化与性能调优服务
risk_matrix:
  regulatory: Apache 2.0 仅覆盖 Swift/Metal 运行时代码，模型权重来自 Hugging Face 固定版本，须遵守 Google
    Gemma 许可条款（对商用场景与用途有限制），整体合规风险较低但需注意权重与代码的许可边界
  technological: 该引擎为模型专属实现而非通用框架，绑定 Gemma 4 26B-A4B 单一模型与 macOS 26/Metal 4/Swift
    6.2 最新平台，模型迭代或平台升级即可导致失效；性能依赖页面缓存状态，8GB 机型 5-6 tok/s 的可用性有限，且仅支持文本推理
  competitive: MLX、llama.cpp 等通用推理框架持续演进，一旦原生支持 MoE 分片流式加载将直接挤压单模型专用工具空间；Apple 官方
    CoreML/Foundation Models 生态同样是潜在竞争者，存在生态挤压与价格战风险
  ethical: 本地推理天然规避云端数据隐私泄露，但模型仍会生成错误或重复内容（项目自述承认），且文本生成能力存在被用于制造误导性内容的通用滥用风险；好在项目不执行工具、仅文本输出，风险相对可控
  additional:
  - 按 token 从 SSD 流式加载专家权重带来持续高 I/O 压力，长时间运行可能加速 SSD 磨损
  - 约 15GB 模型下载与 14.3GB 存储占用对低配设备构成硬件门槛
  - 仅 arm64 且要求最新 macOS/硬件，目标用户群狭窄
confidence:
  impact: medium
  compound: medium
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: drumih/turbo-fieldfare
  canonical_name: drumih/turbo-fieldfare
  url: https://github.com/drumih/turbo-fieldfare
  positioning: TurboFieldfare 是面向 Apple Silicon Mac 的专用 Swift + Metal 推理运行时，目标以约 2
    GB 内存运行 Gemma 4 26B-A4B 模型，最低支持 8 GB 内存机型。
  technical_signal: 其核心机制是将共享的 1.35 GB 核心权重与 FP16 KV 缓存驻留内存，其余路由专家按每个 token 从 SSD
    流式加载，从而避免一次性载入完整的 14.3 GB 模型。
  adoption_signal: 项目已实测 103 组跨内核、缓存、I/O、prefill 与解码的基准结果，8 GB M2 MacBook Air 解码 5.1-6.3
    tok/s，24 GB M5 Pro 达 31-35 tok/s。
  ecosystem_relevance: 该项目属于 Apple Silicon 本地大模型推理生态，兼容 Google Gemma 权重生态，并依赖 macOS
    26 与 Metal 4 平台能力，是专有运行时而非 MLX 或 llama.cpp 的封装。
  target_users:
  - 低内存 Apple Silicon Mac 用户
  - 本地大模型推理开发者与研究者
  - 注重隐私与离线推理的 Mac 用户
  product_signal: Swift 包对外暴露六个产品，包括原生 Mac 应用、命令行界面、OpenAI 兼容的 loopback 服务器与流式安装器，覆盖从安装、解码到服务化调用的完整链路。
  market_signal: 在内存成本上升的背景下，该项目以约 2 GB 内存运行 26B 参数模型，切入低端 Mac 本地推理的差异化市场，与主流云推理形成互补。
  differentiation: 不同于通用封装 MLX 或 llama.cpp 的方案，TurboFieldfare 是模型特定的专用运行时，仅支持 Gemma
    4 26B-A4B 文本推理，以极致内存优化换取推理能力。
  watch_reason: TurboFieldfare 展示了在 8 GB 内存 Mac 上运行 26B 参数模型的技术路径，通过 SSD 流式加载路由专家把内存需求压到约
    2 GB，兼具原生应用与 OpenAI 兼容服务，代表低端设备本地推理的前沿方向，值得持续跟踪其性能表现与生态发展。
  risk_notes:
  - 项目仅支持文本推理，不支持图像、音频与视频等多模态输入，能力边界较为有限。
  - 运行时仅适配 arm64 架构、macOS 26 与 Metal 4，老版本 macOS 与 Metal 不受支持，兼容范围受限。
  - 解码速度受提示长度、页面缓存状态与硬件影响，8 GB M2 上实测 5-6 tok/s 的实际体验仍有待验证。
  - 模型权重需从 Hugging Face 固定版本单独下载，约 15 GB 安装体积对网络带宽与本地存储有较高要求。
  score: 7.0
  article_ids:
  - 7af3ac00212dbeff
  evidence_snippets:
  - TurboFieldfare 是一个用 Swift 和 Metal 编写的专用推理运行时，可在约 2 GB 内存中运行 Gemma 4 26B-A4B 模型，最低支持
    8 GB 内存的 Apple Silicon Mac。
  - 该项目提供原生 Mac 应用、命令行界面、流式安装器和实验性 OpenAI 兼容服务器，源代码以 Apache License 2.0 开源。
---

**Gemma 4 26B-A4B inference in about 2 GB of RAM**

A custom Swift + Metal runtime for any Apple Silicon Mac, even the 8 GB ones.

Quick start · Local server · Benchmarks · Contribute results · How it works · Experiments · References

Memory got expensive. So I gave a 26-billion-parameter model a ~2 GB budget.

TurboFieldfare runs the instruction-tuned
**Gemma 4 26B-A4B**
without loading the entire 14.3 GB model into memory. It keeps the shared
1.35 GB core and FP16 KV cache in memory, then streams only the experts needed
for each token from SSD. This is what lets the model run on Macs with 8 GB of
RAM.

The runtime, streaming installer, CLI, and native Mac app are written in Swift and Metal. TurboFieldfare is model-specific rather than a wrapper around MLX or llama.cpp. The curated experiment record summarizes 103 measured results across kernels, caching, I/O, prefill, and decode.

```
git clone https://github.com/drumih/turbo-fieldfare.git
cd turbo-fieldfare
swift build -c release
.build/release/TurboFieldfareMac
```

On the first run, Swift Package Manager downloads and builds the Swift packages required by the tokenizer. The complete release build includes the foreground Mac app and its sibling decode-service executable.

When the app opens, choose **Download** and let TurboFieldfare fetch and repack
the pinned model (about 15 GB). Once it is ready, choose **Load Model**, type
your prompt, and press **Generate**.

| Metric | Value |
|---|---|
| Model | Gemma 4 26B-A4B IT, 26B total parameters, about 3.88B active per token |
| Weights | MLX affine 4-bit, group 64; 8-bit router; 4-bit shared and routed experts |
| Memory | ~2 GB of weights and 4K KV cache |
| Storage | About 14.3 GB for the installed text-only model |
| Hardware | Apple Silicon Mac; 8 GB of RAM |
| Platform | macOS 26, Metal 4, Swift 6.2 |
| M2 measured decode | 5.1-6.3 tok/s on an 8 GB M2 MacBook Air |
| M5 measured decode | 31-35 tok/s on a 24 GB M5 Pro |

The measured result is a reference point, not a performance ceiling. Prompt length, generated length, page-cache state, and hardware all affect throughput. To help measure another Apple Silicon Mac, follow the community benchmark guide.

TurboFieldfare provides a native Mac app, a command-line interface, and an
experimental loopback OpenAI-compatible server. They use the same `.gturbo`

model directory, but only one model-owning product should run at a time.

The Swift package exposes six products:

| Product | Purpose |
|---|---|
`TurboFieldfare` |
Swift library containing the runtime and Metal kernels |
`TurboFieldfareMac` |
Native Mac app for installation and generation |
`TurboFieldfareDecodeService` |
One-shot local model and Metal owner used by the Mac app |
`TurboFieldfareCLI` |
Command-line instruction chat and raw completion |
`TurboFieldfareServer` |
Loopback OpenAI-compatible Chat Completions server |
`TurboFieldfareRepack` |
Streaming model installer and install verifier |

- An Apple Silicon Mac; the validated target is an 8 GB M2 MacBook Air
- macOS 26 with Metal 4
- Xcode 26 and Swift 6.2 or newer
- Enough free storage for the ~14.3 GB model installation
- An internet connection for the first model install

The package is arm64-only. Older macOS and Metal versions are not supported.

The Mac app treats what you type as an instruction and handles Gemma's chat formatting automatically. Just describe the task and include any context the model needs.

Generation defaults to temperature `0.2`

, Top-K `64`

, and Top-P `0.95`

. Set
temperature to `0`

for deterministic greedy output. The model can still repeat
itself or give incorrect answers, so check important results.

TurboFieldfare is text-only. The app and CLI support user and model messages plus optional system guidance; they do not expose or execute tools. The loopback server accepts function-tool declarations and returns model-produced tool calls for the client to authorize and execute. Images, audio, and video are not supported.

Clone the repository, then run the app from its root:

```
swift build -c release
.build/release/TurboFieldfareMac
```

Build the complete package so the app and its sibling decode service are both
available. When launched from this checkout, the app stores the model in
`scratch/gemma4.gturbo`

.

On first launch, the app checks the available storage and shows the download
and installed sizes. Choose **Download** to begin.

The installer never materializes the full source checkpoint. It streams the
required byte ranges from the pinned Hugging Face revision and repacks them
directly into the `.gturbo`

layout as they arrive. This avoids a second full
checkpoint on disk and keeps scratch memory bounded.

The first installation transfers about 15 GB through bounded Hugging Face
range requests. Network speed and Hugging Face response times vary, so it can
take a while. The completed `.gturbo`

installation occupies about 14.3 GB and
is accepted only after its manifest and file hashes have been validated.
Installation does not load the model into memory.

After installation:

- Choose
**Load Model**. - Enter a prompt in the composer.
- Choose
**Generate**, or press`Command`+`Return`. - Use the stop button or
`Escape`to end generation early.

The status bar shows generation progress, decode speed, and memory use. Use the right pane to configure sampling, context length, expert-cache slots, and runtime options. See Runtime controls for details and defaults.

The CLI uses an existing `.gturbo`

installation. If you installed the model
through the Mac app, it is already available at `scratch/gemma4.gturbo`

.
Otherwise, install it from the command line:

```
swift run -c release TurboFieldfareRepack \
--output scratch/gemma4.gturbo \
--overwrite
```

Continue a cancelled or interrupted download:

```
swift run -c release TurboFieldfareRepack \
--output scratch/gemma4.gturbo \
--overwrite \
--resume
```

Remove saved download state:

```
swift run -c release TurboFieldfareRepack \
--discard-partial \
--output scratch/gemma4.gturbo
```

The runtime accepts only a completed `.gturbo`

directory with a final
`manifest.json`

.

Verify an existing installation without loading the model:

```
swift run -c release TurboFieldfareRepack \
--verify-install \
--input-gturbo scratch/gemma4.gturbo
```

Put chat messages in a JSON array and pass it with `--messages-file`

:

```
[
{"role": "user", "content": "Explain why chunked prefill reduces time to first token while keeping memory bounded."}
]
```

```
swift run -c release TurboFieldfareCLI \
--model scratch/gemma4.gturbo \
--messages-file messages.json
```

This formats messages in the same way as the Mac app. The CLI response limit
is set with `--max-new`

, which defaults to 1,024 tokens. The Mac app can
generate until the selected context window is full.

`--prompt`

is available for raw completion and reproducible comparisons. It
passes the text directly to the model without chat formatting. Use
`--messages-file`

for instruction-response conversations.

```
swift run -c release TurboFieldfareCLI \
--model scratch/gemma4.gturbo \
--prompt "The capital of France is" \
--max-new 64 \
--temperature 0
```

This example deliberately requests a short greedy completion.

Common generation options include `--max-context`

, `--temperature`

, `--top-k`

,
`--top-p`

, `--repetition-penalty`

, `--seed`

, and repeatable `--stop`

strings.
The public CLI uses production runtime defaults. Run the following command for
the complete option list:

`swift run -c release TurboFieldfareCLI --help`

Generated text goes to standard output. Timing statistics go to standard error;
add `--quiet`

to suppress that footer in scripts.

Build the server and point it at an installed model:

```
swift build -c release --product TurboFieldfareServer
.build/release/TurboFieldfareServer \
--model scratch/gemma4.gturbo
```

It listens on `http://127.0.0.1:8080/v1`

and supports Chat Completions,
streaming, function tools, and single-prefix prompt reuse. The client must
authorize and run every tool call. Keep the server on loopback; it has no
remote authentication or TLS.

See Local server for a test request, Python and OpenCode setup, prompt reuse, tool handling, and the supported API subset.

Run the public test suite serially:

`Scripts/test.sh`

Before starting a model run, close memory-heavy apps and check
`memory_pressure -Q`

. If it reports little free memory, postpone the run. Run
only one TurboFieldfare app, decode service, CLI, server, test, or other
local-model process at a time.

To contribute a comparable performance result, follow the community benchmark guide.

At each transformer layer, Metal computes attention and the router from
resident weights. The CPU uses the router's top-8 expert IDs to plan against
the layer's 16-slot LFU cache, then fills misses with bounded parallel `pread`

calls into Metal-visible buffers. Metal computes the resident shared-expert
branch while those reads run, then combines the shared and routed outputs.

Prompt prefill uses chunks of up to 128 tokens so one fetched expert can serve
multiple rows. Generation repeats the routed layer loop one token at a time.
The installer applies the same bounded-memory rule: it repacks remote ranges
directly into `.gturbo`

without staging a full shard or tensor.

For a visual introduction to the model architecture, see Maarten Grootendorst's A Visual Guide to Gemma 4.

System design explains the `.gturbo`

layout, memory
ownership, prefill, router handoff, `cb1`

/`io`

/`cb2`

phases, Metal kernels, and
correctness invariants.

TurboFieldfare currently includes:

- Remote streaming repack into the
`.gturbo`

model format - Instruction-tuned Gemma 4 26B-A4B with verified text-only chat formatting
- 4-bit MLX affine embedding, attention, shared-expert, and routed-expert weights, with an 8-bit router
- Custom Metal kernels for quantized GEMV, attention, MoE, normalization, RoPE, sampling, and production fusions
- SSD-backed routed-expert streaming with a bounded expert cache
- Chunked single-prompt prefill and token-by-token generation
- FP16 KV storage with bounded circular storage for 25 sliding-window layers and linear storage for 5 full-attention layers
- Exact split-K/V decode attention with distinct normalized K and V paths
- A Swift library, streaming installer, command-line interface, loopback OpenAI-compatible server, and native SwiftUI/AppKit Mac app with a one-shot local decode service

Current scope is text-only inference from the pinned Gemma 4 26B-A4B instruction checkpoint on Apple Silicon Macs with at least 8 GB of RAM.

- Build iPhone and iPad apps, then measure inference speed and memory use on mobile hardware.
- Benchmark more Apple Silicon Macs, especially the base 16 GB M4 Mac mini and other 8 GB models.

The experiments that shaped TurboFieldfare explain the largest wins, the plausible ideas that failed, and the early results that reversed under stronger validation. The detailed experiment record keeps all 103 audited entries as optional evidence.

Useful entry points:

- Local OpenAI-compatible server
- System design
- Benchmarks
- The experiments that shaped TurboFieldfare
- Experiment inventory and summaries
- Implementation references

TurboFieldfare's source and documentation are licensed under the Apache License 2.0.

Model weights are not included. The installer downloads them separately from the pinned Hugging Face checkpoint, and the weights remain governed by their source terms. See THIRD_PARTY_NOTICES.md for the model and Swift package license review.

TurboFieldfare is an independent research project. It is not affiliated with, sponsored by, or endorsed by Google.

Thanks for checking out this project!

My name is Andrey Mikhaylov. You can find me on LinkedIn. I am the author of TurboFieldfare and an iOS and Metal engineer. Most of my work is with images, video, and on-device AI.

I dedicate this project to my wife, Sasha, the most supportive person I know. She stands by me even through the hardest times. She loves wildlife, goes birdwatching, and volunteers with our local birding community. Because of her, I have also grown closer to birds and nature.

TurboFieldfare is named after the fieldfare, a member of the thrush family and my favourite bird. It is not the most noticeable or brightly coloured bird, but it definitely has a character and unique features of its own. I think the same is true of this project: it may not be the most practical, but I built it with my favourite tools, especially Metal, in my favourite field, on-device ML inference. It definitely has its own character and unique features.

Next time you are outside, touch the grass and listen to the birds. Sometimes it is the most beautiful thing you can do. And if you can, support your local wildlife community. They do important work.

Thank you!