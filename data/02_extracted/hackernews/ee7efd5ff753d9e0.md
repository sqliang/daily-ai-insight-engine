---
title: Running Kimi K3 on MI355X at Better Performance per Dollar Than B300
source: https://www.wafer.ai/blog/kimi-k3-mi355x
author:
- '[[ilreb]]'
published: '2026-08-02'
created: '2026-08-02'
manifest_dates:
- '2026-08-02'
description: 'Article URL: https://www.wafer.ai/blog/kimi-k3-mi355x Comments URL:
  https://news.ycombinator.com/item?id=49141073 Points: 126 # Comments: 35'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ee7efd5ff753d9e0
source_type: community_discussion
tldr: Wafer 发布实测基准：AMD MI355X 以 952 tok/s 的节点聚合吞吐与 118 tok/s 单流解码运行 2.8T 参数的 Kimi
  K3，性能每美元达 48 tok/s/美元，超过 B300 与 B200。工程上通过修复 sglang 的 top_k_renorm_prob 缺失和 AITER
  MLA 预填充头数对齐，实现约 2-3 倍预填充加速。
objective_summary: Wafer 在官方博客公布在 AMD MI355X（8 卡 TP8）上服务 2.8T 参数开源模型 Kimi K3 的实测基准：1024
  token 输入/400 token 输出下，节点聚合吞吐 952 tok/s、单流解码 118 tok/s，性能每美元 48 tok/s/美元。对比双节点 TP16
  的 B200 聚合吞吐 498 tok/s、单节点 B300 为 1568 tok/s，但 B300 单价约为 MI355X 的 2.4 倍。工程上，团队用 RadixArk
  Kimi-K3-DSpark 草稿模型实现投机解码，为 sglang 的 ROCm 分支补齐 top_k_renorm_prob 定义，并将 AITER MLA
  预填充内核头数从 12 零填充到 16，使 172k token 冷预填充提速约 2-3 倍。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Wafer
  - AMD
  - NVIDIA
  - RadixArk
  - Moonshot AI
  - DeepSeek
  - Zhipu AI
  technologies:
  - ROCm
  - CUDA
  - Triton
  - MLA
  - MTP
  - EAGLE
  - speculative decoding
  - KV cache
  - TP8
  - HBM
  - sglang
  - AITER
  key_people: []
key_logic_flow:
- Kimi K3 是 2.8T 参数的开源模型，权重加上 1M token 上下文的 KV 缓存需要超过 1.5TB 显存，单个 B200 节点无法容纳。
- AMD MI355X 单卡拥有 288GB 显存，平均单价约为 B300 的 2.4 折、B200 的 1.7 折，成为服务超大模型的高性价比替代方案。
- 基准测试显示 MI355X 节点聚合吞吐 952 tok/s、单流解码 118 tok/s，性能每美元 48 tok/s/美元，全面优于 B200 的 7 tok/s/美元和
  B300 的 33 tok/s/美元。
- K3 未附带任何草稿张量，投机解码依赖外部草稿模型 RadixArk Kimi-K3-DSpark；sglang 的 ROCm 分支缺少 top_k_renorm_prob
  定义导致调度器崩溃。
- 用单个 PyTorch 函数补齐 top_k_renorm_prob 定义后，单流性能提升约 2.2 倍，峰值聚合吞吐增长 18%，并稳定运行在更高并发度上。
- MI355X 上 172k token 冷预填充耗时 51 秒明显慢于 B300 的 23 秒，根因是 AITER MLA 内核因头数形状不匹配而回退到 Triton，零填充到
  16 头后预填充提速约 2-3 倍。
object_mentions:
- object_type: model
  name: Kimi K3
  canonical_name: Kimi K3
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Kimi K3 是 2.8T 参数的开源大模型，权重加 1M token 上下文的 KV 缓存需要超过 1.5TB 显存，单个 B200 节点无法容纳。
  - Kimi K3 未附带任何草稿张量（无 MTP、无 EAGLE），在 MI355X 上依赖外部投机解码路径才能达到当前吞吐。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: AMD MI355X
  canonical_name: AMD MI355X
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - AMD MI355X 单卡拥有 288GB 显存，平均单价约为 B300 的 2.4 折、B200 的 1.7 折，是服务超大模型的成本替代方案。
  - MI355X 在 1024 输入/400 输出基准下达到 952 tok/s 节点聚合吞吐和 118 tok/s 单流解码。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: NVIDIA B300
  canonical_name: NVIDIA B300
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - B300 节点在聚合吞吐上以约 1.65 倍领先 MI355X，但单价约为 MI355X 的 2.4 倍，性能每美元反而落后。
  - B300 每 GPU 拥有 288GB 显存，单价假设为 6 美元每 GPU 小时，性能每美元约 33 tok/s/美元。
  article_id: ee7efd5ff753d9e0
- object_type: product
  name: NVIDIA B200
  canonical_name: NVIDIA B200
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - B200 因 Kimi K3 无法放入单个 8×192GB 节点而需双节点 TP16 部署，跨节点 all-reduce 位于解码关键路径上。
  - B200 的 TP16 部署聚合吞吐 498 tok/s 是两块节点的总和，平均每节点仅约 249 tok/s，性能每美元仅 7 tok/s/美元。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: RadixArk Kimi-K3-DSpark
  canonical_name: RadixArk Kimi-K3-DSpark
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Kimi K3 未附带任何草稿张量，投机解码只能依赖外部块扩散草稿模型 RadixArk 的 Kimi-K3-DSpark，在 CUDA 上可直接运行。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: sglang
  canonical_name: sglang
  url: https://github.com/sgl-project/sglang
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - sglang 的接受采样校验器在稠密路径调用 top_k_renorm_prob，但 ROCm 构建未定义该符号，请求落地时触发 NameError 并带崩调度器。
  - 修复方式是直接在 sglang 的 ROCm 采样分支用排序、masked_fill 和除法实现 top-k 重归一化，无需自定义内核。
  article_id: ee7efd5ff753d9e0
- object_type: project
  name: AITER
  canonical_name: AITER
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - AITER 的 MLA 预填充内核只支持 4、8 或 16 倍数的注意力头数，K3 在 TP8 下每 rank 有 12 头，导致回退到慢速 Triton
    内核。
  - 将头数从 12 零填充到 16 后启用 AITER MLA 预填充内核，预填充速度从约 4-7k tok/s 提升到约 13k tok/s。
  article_id: ee7efd5ff753d9e0
- object_type: model
  name: DeepSeek V4-Pro
  canonical_name: DeepSeek V4-Pro
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - DeepSeek V4-Pro 拥有 1.6T 参数，文章认为其智能水平已达到接近闭源 Opus 级别，是开源模型能力爆发的代表之一。
  article_id: ee7efd5ff753d9e0
- object_type: model
  name: GLM5.2
  canonical_name: GLM5.2
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - GLM5.2 拥有 753B 参数，智能水平接近 Opus，文章以它作为框架类 bug 数量的对比基准，称 MI355X 适配 K3 的 bug 比 GLM5.2
    更少。
  article_id: ee7efd5ff753d9e0
extract_result: success
---

Over the past several months, we’ve seen an explosion in the capabilities of open source models. With DeepSeek V4-Pro and GLM5.2 reaching near-Opus levels of intelligence, open source has emerged as a real, cost-efficient alternative to the closed source models we’ve been married to.

But we have yet to see one like Kimi K3. Promising Fable/Sol levels of intelligence, Kimi K3 marks the start of a new era for open source.

But a smarter model means a **bigger** model — and these models are expanding in size just as fast as they are in capabilities. GLM5.2 has 753B parameters, DeepSeek V4-Pro 1.6T, and Kimi K3 weighs in at 2.8T (!!) parameters. That’s over 1.5TB of VRAM *before* allocating a KV cache for 1M tokens of context. Not even a B200 node (8 GPUs) can fit Kimi K3. That leaves you with limited options: serve on a node of B300s, which have 288GB of VRAM per GPU, or commit two B200 nodes (TP16) to serving Kimi.

But guess which other non-NVIDIA GPU has 288GB of VRAM? AMD’s MI355X. Can you tell we like these chips yet? At around ~2.4× cheaper per GPU on average versus a B300 and ~1.7× cheaper than a B200, the MI355X is a cost-efficient alternative to Blackwells with comparable hardware specs. The only problem with AMD is software support — slower kernels and less day-0 support on inference frameworks make serving frontier models on AMD a real engineering effort. Our claim at Wafer is that agents are improving at kernel and model optimization, closing this gap as we speak. But with AMD shipping day-0 support for Kimi K3, most of the work was already done for us.

The results are great: on a 1,024-token input / 400-token output benchmark, the MI355X reaches 952 tok/s/node and 118 tok/s single stream — over 3.8× the aggregate throughput per node and over 1.3× the single-stream decode of our TP16 B200 deployment (whose 498 tok/s is a 16-GPU, 2-node total — ~249/node). B300 nodes still win ~1.65× on aggregate throughput over the MI355X, but at 2.4× the price, the MI355X crushes the B300 on performance per dollar.

8× MI355X (TP8) |
2×8 B200 (TP16) | B300 (TP8+DCP8) | |
|---|---|---|---|
| Decode tok/s per stream | 118 tok/s |
90 tok/s | 172 tok/s |
| Peak aggregate | 952 tok/s |
498 tok/s | 1,568 tok/s |
| Peak aggregate per GPU | 119 tok/s |
31 tok/s | 196 tok/s |
| Peak aggregate per $/GPU-hr | 48 tok/s/$ |
7 tok/s/$ | 33 tok/s/$ |

*Perf/dollar at $2.50/GPU-hr for the MI355X, $6.00 for the B300, and $4.25 for the B200.*

To the B200’s defence, its numbers are somewhat deflated by the fact that it pays a cross-node all-reduce on the decode critical path (RoCE v2 at ~195 Gb/s) — it’s the only config here that spans two nodes, because Kimi K3 won’t fit weights plus a 1M-token KV pool on a single 8×192GB node. But that’s exactly the point: Kimi K3 at its size is one of the first models we’ve seen where the MI355X’s focus on HBM capacity gives it a practical, measurable edge over the B200.

## How we did it

While Kimi K3 served out of the box, there was still work to be done to get it to its current throughput number.

The main lever was speculative decode. K3 ships zero draft tensors — no MTP, no EAGLE — so the only speculative path is an external block-diffusion draft: RadixArk’s Kimi-K3-DSpark. On CUDA it just runs. On ROCm our first real request breaks the scheduler with this error:

`NameError: name 'top_k_renorm_prob' is not defined. Did you mean: 'top_p_renorm_prob'?`


sglang’s accept-sampling verifier has two ways to build the target distribution: a dense path that calls `top_k_renorm_prob`

, and a sparse fast path that routes through `torch.topk`

directly. The CUDA build imports `top_k_renorm_prob`

from `sgl_kernel`

; the ROCm build aliases only a Triton top-p kernel and leaves `top_k_renorm_prob`

undefined — there’s no top-k renorm kernel for gfx950 to alias. So the moment a request lands on the dense path, the verifier hits that `NameError`

and takes the scheduler down with it.

The fix is a single PyTorch function. Top-k renorm is a small operation: take the model’s probability vector, keep the k highest entries, zero the rest, and rescale what’s left to sum to 1. A `sort`

, a `masked_fill`

, a divide — dropped straight into sglang’s ROCm sampling branch, the same computation the CUDA build gets from `sgl_kernel`

. No custom kernel: the reflex on ROCm is to assume you need one, but here it was a missing definition, not a missing kernel.

With spec dec fixed and hardened, we gained ~2.2× performance single-stream, ~1.7× per-stream at moderate load, and +18% peak aggregate. More importantly, our peak aggregate throughput landed on much higher concurrency (c64 vs c24 no-spec).

## Prefill optimizations

Discussion around model performance tends to highlight decode tokens per second. But in many cases decode tok/s is fool’s gold — decode is over-glorified, while time-to-first-token, the number users *feel* the most, gets overlooked.

The MI355X struggles here: an identical 172k-token cold prefill took ~51s on MI355X versus ~23s on a B300. On a 1M-context model, a lot of workloads have huge prefills (sometimes cold), and having GPUs spin on prefill for minutes can render entire fleets of nodes useless.

The gap was almost entirely one kernel. K3 on ROCm was falling back to slow generic Triton attention because the fast AITER MLA prefill kernel wouldn’t load. The problem was a shape mismatch, not a missing kernel — K3 at TP8 gives 12 attention heads per rank, and AITER’s MLA path is built for 4, 8, or multiples of 16. The fix was trivially simple: zero-pad the head count 12→16, run the fast kernel, and extract the real 12 heads from the output.

The result: on the same 172k cold prefill, the AITER MLA prefill ASM runs at ~13k tok/s steady-state vs the Triton fallback’s ~4–7k, speeding up prefill by ~2–3×. It’s a TTFT lever, not an aggregate-throughput one — decode is unchanged, so it doesn’t move the numbers above; it moves the number a user waits on before the first token appears.

## Takeaways

Achieving the best performance-per-dollar ratio on the MI355X was relatively out of the box. There were some expected framework-related bugs — but fewer than GLM5.2, and this time it certainly did not require custom kernels.

SOTA on AMD is imminent. Is the CUDA moat dead?