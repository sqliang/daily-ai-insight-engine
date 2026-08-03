---
title: MoonshotAI/FlashKDA
source: https://github.com/MoonshotAI/FlashKDA
author: []
published: ''
created: '2026-07-30'
manifest_dates:
- '2026-07-30'
description: 'FlashKDA: high-performance Kimi Delta Attention kernelsFlashKDA FlashKDA:
  Flash Kimi Delta Attention — high-performance KDA kernels built on CUTLASS News
  2026-04-22 — Deep-Dive Blog: the design decisions behind FlashKDA v1, read it here.
  Requirements SM90 and above CUDA 12.9 and above PyTorch 2.4 and above Installation
  git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda cd flash-kda git
  submodule update --init --recursive pip install -v --no-build-isolation . By default,
  the build detects the current CUDA device and compiles for that architecture. For
  wheel or CI builds, compile all supported architectures explicitly: FLASH_KDA_CUDA_ARCHS=all
  pip install -v --no-build-isolation . Supported values are auto (default), all,
  or a comma-separated arch list such as 90a,100a. Using FlashKDA as an FLA backend
  Once installed, FlashKDA is auto-dispatched from flash-linear-attention''s chunk_kda.
  See fla-org/flash-linear-attention#852 for integration details. Requirements Install
  flash-linear-attention >= 0.5.0:pip install -U flash-linear-attention Call chunk_kda
  under torch.inference_mode()import torch from fla.ops.kda import chunk_kda with
  torch.inference_mode(): out, final_state = chunk_kda( q=q, k=k, v=v, g=g, beta=beta,
  scale=scale, initial_state=h0, output_final_state=True, use_gate_in_kernel=True,
  use_qk_l2norm_in_kernel=True, use_beta_sigmoid_in_kernel=True, safe_gate=True, A_log=A_log,
  dt_bias=dt_bias, lower_bound=lower_bound, transpose_state_layout=True, cu_seqlens=cu_seqlens,
  ) Opt out: set FLA_FLASH_KDA=0 to fall back to the Triton path. Debug dispatch:
  add logging.basicConfig(level=logging.INFO) to see [FLA Backend] kda.chunk_kda ->
  flashkda on hit, or ... rejected: <reason> on miss. Performance See BENCHMARK_H20.md.
  Tests bash tests/test.sh tests/test_fwd.py — correctness tests (exact match against
  the torch reference; compared with flash-linear-attention) Kernel API flash_kda.fwd
  flash_kda.fwd(q, k, v, g, beta, scale, out, A_log, dt_bias, lower_bound, initial_state=None,
  final_state=None, cu_seqlens=None) Parameters: Parameter Dtype Shape Description
  q bf16 [B, T, H, K] Query k bf16 [B, T, H, K] Key v bf16 [B, T, H, V] Value g bf16
  [B, T, H, K] Gate before activation beta bf16 [B, T, H] Beta logits (pre-activation;
  sigmoid applied internally) scale float scalar scaling factor out bf16 [B, T, H,
  V] Output tensor A_log fp32 [H] Log-gate parameter dt_bias fp32 [H, K] Gate bias
  lower_bound float scalar Gate lower bound (range from -5.0 to 0) initial_state bf16/fp32/None
  [B, H, V, K] or [N, H, V, K] (optional) Initial recurrent state final_state bf16/fp32/None
  [B, H, V, K] or [N, H, V, K] (optional, output) Final recurrent state cu_seqlens
  int64 [N+1] (optional) Cumulative sequence lengths for variable-length batching
  Currently requires K = V = 128. initial_state / final_state accept None (stateless),
  bf16, or fp32 tensors. When both are provided, their dtypes must match. When cu_seqlens
  is provided, B must be 1, T is the total length across all sequences, and initial_state
  / final_state have shape [N, H, V, K]. When cu_seqlens is None, each batch element
  is treated as an independent sequence, and the state shape is [B, H, V, K]. Development
  To set up IntelliSense (clangd) for the CUDA/C++ sources, run: bash setup_clangd.sh
  This generates a .clangd file with the correct repository paths and installs the
  global clangd config.yaml to ~/.config/clangd/. Citation @misc{flashkda2026, title={FlashKDA:
  Flash Kimi Delta Attention}, author={Yutian Chen, Zhiyuan Li, Yucheng Wang, Ming
  Wei}, year={2026}, publisher = {GitHub}, howpublished = {\url{https://github.com/MoonshotAI/FlashKDA}},
  }'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ded4e7e6458f4aee
source_type: community_discussion
tldr: MoonshotAI 发布 FlashKDA v1，一个基于 CUTLASS 构建的高性能 Kimi Delta Attention（KDA）内核，面向
  SM90 及以上 GPU。它可被 flash-linear-attention 的 chunk_kda 自动调度，支持可变长批量与 bf16/fp32 循环状态。
objective_summary: 2026 年 4 月 22 日，MoonshotAI 在 GitHub 发布 FlashKDA（Flash Kimi Delta
  Attention）v1，这是一个基于 CUTLASS 构建的高性能 KDA 计算内核。它要求 SM90 及以上 GPU 架构、CUDA 12.9 以上以及 PyTorch
  2.4 以上，安装后会被 flash-linear-attention 的 chunk_kda 自动调度。当前实现要求 K=V=128，支持 bf16/fp32
  的初始与最终循环状态，并可通过 cu_seqlens 处理可变长批量推理。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - MoonshotAI
  - fla-org
  technologies:
  - CUTLASS
  - KDA
  - flash-linear-attention
  - CUDA
  - PyTorch
  - Triton
  key_people:
  - Yutian Chen
  - Zhiyuan Li
  - Yucheng Wang
  - Ming Wei
key_logic_flow:
- MoonshotAI 于 2026 年 4 月 22 日在 GitHub 发布 FlashKDA v1，这是一个基于 CUTLASS 构建的高性能 KDA 内核。
- FlashKDA 的运行环境要求为 SM90 及以上 GPU 架构、CUDA 12.9 及以上版本以及 PyTorch 2.4 及以上版本。
- 安装 FlashKDA 后，它会被 flash-linear-attention 的 chunk_kda 自动调度，用户无需手动切换后端。
- 设置 FLA_FLASH_KDA=0 可以关闭 FlashKDA 并回退到 Triton 路径。
- 当前 FlashKDA 要求 K=V=128，支持 bf16/fp32 的初始与最终循环状态，并通过 cu_seqlens 参数支持可变长批量推理。
- 仓库附带 tests/test.sh 与 tests/test_fwd.py 正确性测试，结果与 torch 参考实现及 flash-linear-attention
  进行对比。
object_mentions:
- object_type: project
  name: MoonshotAI/FlashKDA
  canonical_name: MoonshotAI/FlashKDA
  url: https://github.com/MoonshotAI/FlashKDA
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - MoonshotAI 于 2026 年 4 月 22 日在 GitHub 发布 FlashKDA v1，这是一个基于 CUTLASS 构建的高性能 KDA
    内核。
  - FlashKDA 要求 SM90 及以上 GPU 架构、CUDA 12.9 及以上版本以及 PyTorch 2.4 及以上版本，安装后会被 flash-linear-attention
    的 chunk_kda 自动调度。
  - 当前实现要求 K=V=128，支持 bf16/fp32 的初始与最终循环状态，并可通过 cu_seqlens 参数处理可变长批量推理。
  article_id: ded4e7e6458f4aee
- object_type: project
  name: fla-org/flash-linear-attention
  canonical_name: fla-org/flash-linear-attention
  url: https://github.com/fla-org/flash-linear-attention
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - FlashKDA 安装后被 flash-linear-attention 的 chunk_kda 自动调度，集成细节见 fla-org/flash-linear-attention
    的 pull request 852。
  - 使用 FlashKDA 需要安装 flash-linear-attention 0.5.0 及以上版本，并在 torch.inference_mode 下调用
    fla.ops.kda 的 chunk_kda 函数。
  article_id: ded4e7e6458f4aee
extract_result: success
impact_score:
  score: 6.0
  reason: 该事件是 MoonshotAI 将其生产级 KDA 推理内核以 CUTLASS 实现开源，并深度集成进 flash-linear-attention
    的自动调度路径，属于线性注意力/状态空间模型方向的重要工程落地，对 KDA 生态的推理性能与部署成本有直接改变，可能影响线性注意力路线的竞争格局。但受限于
    K=V=128 的硬约束、SM90+/CUDA 12.9+ 的硬件门槛，且 KDA 本身并非行业通用注意力范式，冲击范围被限定在特定架构与特定硬件用户圈层，远未达到范式转移级别。综合判定为局部竞争格局改变级别的高分区间。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: CUTLASS 手写内核相对 Triton 路径的实际性能提升幅度，以及 K=V=128 约束带来的通用性限制
hype_assessment:
  level: low
  reason: 全文为技术性发布说明，无'颠覆''革命'等 PR 滥用词汇；附带 correctness 测试脚本、与 torch 参考实现及 flash-linear-attention
    的对比、H20 基准文档，并诚实标注了 K=V=128、硬件版本等限制条件，属于实打实的工程干货。
information_entropy: high
domain_disruption:
  technical_innovation: 基于 CUTLASS 将 KDA 的前向计算（含门控 sigmoid、QK L2 归一化、安全门控等此前在 Triton
    中逐算子融合的环节）固化为手写 CUDA 内核，并通过 cu_seqlens 支持可变长批量、支持 bf16/fp32 循环状态传递，在 Hopper+ 硬件上为线性注意力变体提供了超越
    Triton 生成代码的性能底座，属于推理内核工程层面的实质突破。
  business_model: 对 MoonshotAI 而言，开源生产内核意味着其 Kimi 架构在开源生态中获得更低的部署门槛与更强的生态渗透力；对行业而言，KDA
    内核性能的提升直接降低了运行该类线性注意力模型的推理算力成本，为基于 KDA 的商用模型服务提供了更经济的算力曲线，间接影响线性注意力路线的商业化落地节奏。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 评分逻辑（正向复利因素）：(1) KDA 是 Moonshot 自研的 delta-rule 线性注意力架构，将其高性能 CUTLASS 内核开源并接入
    flash-linear-attention 的 chunk_kda 自动调度，等于把私有架构推向生态标准，具备 FlashAttention 式的'地基层'潜质——若线性注意力成为长上下文主导范式，该内核将随
    fla 生态持续沉淀并积累调用量；(2) CUTLASS 手写内核相比 Triton 路径在 SM90+ 上有明确性能优势，技术含量高，能强化 Moonshot
    在开源社区的生态位并吸引顶级工程人才，属于战略性'基础设施投资'。反向折价因素：(1) 内核层迭代极快，硬件代际更替（SM90→SM100/110）会周期性淘汰内核投入，复利积累弱于模型层与应用层；(2)
    当前仅支持 K=V=128、SM90+、CUDA 12.9+，适用范围窄，存量 GPU 算力大多无法直接受益，覆盖面有限；(3) 开源内核竞争格局拥挤（FlashAttention、DeepSeek
    FlashMLA 等已占心智），KDA 范式能否胜出尚未验证，且开源行为本身会摊薄其专属算力优势。综合判定：具备成为线性注意力细分赛道基础设施的潜力，但需验证跨架构泛化与范式胜出，故给
    6.5 分。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- MoonshotAI
- fla-org
- NVIDIA
competitive_casualty:
- Triton 内核路径（KDA 场景被替换）
- 闭源推理内核优化服务商
- 追赶型线性注意力内核项目
market_opportunities:
- 部署 Kimi 类线性注意力/长上下文模型的推理团队可集成 FlashKDA 内核，在 H100/H200/B200 上直接获得吞吐提升与推理成本下降，建议结合
  flash-linear-attention 生态先跑基准验证实际收益
- FlashKDA 强化了 flash-linear-attention 生态在高性能 GPU 上的竞争力，面向长文本/线性注意力推理的 MaaS 与云服务商可借此构建差异化低延迟服务
- 在高端 NVIDIA 算力受出口管制约束的背景下，将 CUTLASS 内核设计模式迁移到国产 GPU（昇腾/寒武纪）或自研同类线性注意力内核具有战略价值；AI
  Infra 工程师也可将 CUTLASS 内核开发作为稀缺技能储备方向
risk_matrix:
  regulatory: 无
  technological: 适用范围较窄：当前硬性要求 K=V=128、SM90+ GPU 架构（A100/4090 等存量卡无法使用）、CUDA 12.9+
    与 PyTorch 2.4+；线性注意力架构仍在快速演进（Mamba/GLA/KDA 相互竞争），若 KDA 被替代或 Moonshot 修改注意力设计，该内核需重写才能跟上
  competitive: flash-attention 生态与 Triton 编译器持续进步，定制 CUTLASS 内核的相对性能优势可能被稀释；flash-linear-attention
    自带 Triton 兜底路径（FLA_FLASH_KDA=0），用户若无显著收益不会主动迁移；NVIDIA 官方优化库与云厂商自研内核也可能形成生态挤压
  ethical: 无
  additional:
  - 地缘与供应链风险：依赖 SM90+ NVIDIA 数据中心 GPU，受出口管制与供货瓶颈影响，对 Moonshot 等中国厂商尤为敏感
  - 维护可持续性风险：项目主要由 MoonshotAI 单一公司驱动，若公司战略调整，长期兼容性与社区维护存在不确定性
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: MoonshotAI/FlashKDA
  canonical_name: MoonshotAI/FlashKDA
  url: https://github.com/MoonshotAI/FlashKDA
  positioning: MoonshotAI 开源的高性能 Kimi Delta Attention（KDA）计算内核，基于 CUTLASS 构建，面向 SM90
    及以上 GPU，可被 flash-linear-attention 的 chunk_kda 自动调度。
  technical_signal: 基于 CUTLASS 实现高性能 KDA 内核，要求 SM90+ GPU、CUDA 12.9+ 与 PyTorch 2.4+，当前限定
    K=V=128，支持 bf16/fp32 循环状态与 cu_seqlens 可变长批量。
  adoption_signal: 安装后会被 flash-linear-attention 的 chunk_kda 自动调度，用户无需手动切换后端；设置 FLA_FLASH_KDA=0
    可回退到 Triton 路径。
  ecosystem_relevance: 作为 flash-linear-attention 的官方可替换后端接入其 chunk_kda 接口，直接补强线性注意力开源生态的高性能内核能力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: FlashKDA 是 MoonshotAI 将 Kimi 的 Delta Attention 推理内核开源并反哺 flash-linear-attention
    生态的关键动作，代表线性注意力在生产级 GPU 上落地的最新进展，值得跟踪其基准性能、架构演进与生态采用情况。
  risk_notes:
  - 当前实现仅支持 K=V=128 且要求 SM90 及以上 GPU，适用的硬件与模型配置范围较为有限。
  - 内核依赖 CUDA 12.9 与 PyTorch 2.4 以上较新工具链，生产环境升级与适配存在额外成本。
  score: 7.0
  article_ids:
  - ded4e7e6458f4aee
  evidence_snippets:
  - MoonshotAI 于 2026 年 4 月 22 日在 GitHub 发布 FlashKDA v1，这是一个基于 CUTLASS 构建的高性能 KDA
    内核。
  - FlashKDA 要求 SM90 及以上 GPU 架构、CUDA 12.9 及以上版本以及 PyTorch 2.4 及以上版本，安装后会被 flash-linear-attention
    的 chunk_kda 自动调度。
  - 当前实现要求 K=V=128，支持 bf16/fp32 的初始与最终循环状态，并可通过 cu_seqlens 参数处理可变长批量推理。
---

FlashKDA: Flash Kimi Delta Attention — high-performance KDA kernels built on CUTLASS

**2026-04-22**— Deep-Dive Blog: the design decisions behind FlashKDA v1, read it here.

- SM90 and above
- CUDA 12.9 and above
- PyTorch 2.4 and above

```
git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda
cd flash-kda
git submodule update --init --recursive
pip install -v --no-build-isolation .
```

By default, the build detects the current CUDA device and compiles for that architecture. For wheel or CI builds, compile all supported architectures explicitly:

`FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation .`

Supported values are `auto`

(default), `all`

, or a comma-separated arch list such as `90a,100a`

.

Once installed, FlashKDA is auto-dispatched from `flash-linear-attention`

's `chunk_kda`

. See fla-org/flash-linear-attention#852 for integration details.

**Requirements**

- Install
`flash-linear-attention >= 0.5.0`

:pip install -U flash-linear-attention

- Call
`chunk_kda`

under`torch.inference_mode()`

import torch from fla.ops.kda import chunk_kda with torch.inference_mode(): out, final_state = chunk_kda( q=q, k=k, v=v, g=g, beta=beta, scale=scale, initial_state=h0, output_final_state=True, use_gate_in_kernel=True, use_qk_l2norm_in_kernel=True, use_beta_sigmoid_in_kernel=True, safe_gate=True, A_log=A_log, dt_bias=dt_bias, lower_bound=lower_bound, transpose_state_layout=True, cu_seqlens=cu_seqlens, )


**Opt out:** set `FLA_FLASH_KDA=0`

to fall back to the Triton path.

**Debug dispatch:** add `logging.basicConfig(level=logging.INFO)`

to see `[FLA Backend] kda.chunk_kda -> flashkda`

on hit, or `... rejected: <reason>`

on miss.

See BENCHMARK_H20.md.

`bash tests/test.sh`

`tests/test_fwd.py`

— correctness tests (exact match against the torch reference; compared with`flash-linear-attention`

)

```
flash_kda.fwd(q, k, v, g, beta, scale, out, A_log, dt_bias, lower_bound,
initial_state=None, final_state=None, cu_seqlens=None)
```

**Parameters:**

| Parameter | Dtype | Shape | Description |
|---|---|---|---|
`q` |
bf16 | `[B, T, H, K]` |
Query |
`k` |
bf16 | `[B, T, H, K]` |
Key |
`v` |
bf16 | `[B, T, H, V]` |
Value |
`g` |
bf16 | `[B, T, H, K]` |
Gate before activation |
`beta` |
bf16 | `[B, T, H]` |
Beta logits (pre-activation; sigmoid applied internally) |
`scale` |
float | scalar | scaling factor |
`out` |
bf16 | `[B, T, H, V]` |
Output tensor |
`A_log` |
fp32 | `[H]` |
Log-gate parameter |
`dt_bias` |
fp32 | `[H, K]` |
Gate bias |
`lower_bound` |
float | scalar | Gate lower bound (range from -5.0 to 0) |
`initial_state` |
bf16/fp32/None | `[B, H, V, K]` or `[N, H, V, K]` |
(optional) Initial recurrent state |
`final_state` |
bf16/fp32/None | `[B, H, V, K]` or `[N, H, V, K]` |
(optional, output) Final recurrent state |
`cu_seqlens` |
int64 | `[N+1]` |
(optional) Cumulative sequence lengths for variable-length batching |

- Currently requires
`K = V = 128`

. `initial_state`

/`final_state`

accept`None`

(stateless), bf16, or fp32 tensors. When both are provided, their dtypes must match.- When
`cu_seqlens`

is provided,`B`

must be 1,`T`

is the total length across all sequences, and`initial_state`

/`final_state`

have shape`[N, H, V, K]`

. - When
`cu_seqlens`

is`None`

, each batch element is treated as an independent sequence, and the state shape is`[B, H, V, K]`

.

To set up IntelliSense (clangd) for the CUDA/C++ sources, run:

`bash setup_clangd.sh`

This generates a `.clangd`

file with the correct repository paths and installs the global clangd `config.yaml`

to `~/.config/clangd/`

.

```
@misc{flashkda2026,
title={FlashKDA: Flash Kimi Delta Attention},
author={Yutian Chen, Zhiyuan Li, Yucheng Wang, Ming Wei},
year={2026},
publisher = {GitHub},
howpublished = {\url{https://github.com/MoonshotAI/FlashKDA}},
}
```