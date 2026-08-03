---
title: Run Kimi K3 using 29 GB of RAM at 0.50 tok/s
source: https://github.com/sqliteai/waste
author:
- '[[marcobambini]]'
published: '2026-07-31'
created: '2026-08-01'
manifest_dates:
- '2026-08-01'
description: 'Article URL: https://github.com/sqliteai/waste Comments URL: https://news.ycombinator.com/item?id=49123386
  Points: 247 # Comments: 102'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: d6cfb2eda47ef1ed
source_type: community_discussion
tldr: sqliteai 发布纯 C 编写的 WASTE 嵌入式推理引擎，可将 2.78 万亿参数的完整开放权重 Kimi K3 模型转换为 982 GiB 容器，在
  64GB 内存的消费级笔记本上以约 0.5 tok/s 的速度从磁盘流式运行。
objective_summary: sqliteai 团队在 GitHub 上发布 WASTE 推理引擎，该引擎用 C 语言实现且无第三方运行时依赖，通过将模型主干驻留内存、按需从磁盘流式读取激活的专家权重、并用剩余
  RAM 作为有界专家缓存来运行超大 MoE 模型。它使完整开放权重的 Kimi K3 模型（2.78 万亿参数）在 64GB MacBook Pro 上以 0.49
  至 0.54 tok/s 运行，最低内存门槛为 29.05 GiB。引擎逐层通过 PyTorch 参考校验，最终 logits 一致到 3.6e-06，且同一引擎可用
  19 GB 容器运行 Kimi-Linear-48B 模型达到 10.7 tok/s。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Moonshot AI
  - sqliteai
  technologies:
  - Mixture of Experts
  - residual vector quantization
  - NVMe streaming
  - C11
  key_people: []
key_logic_flow:
- WASTE 是一个纯 C 编写的可嵌入式推理引擎，无第三方运行时依赖，核心思路是让模型主干驻留内存、按需从磁盘流式读取专家权重、并用剩余 RAM 作为有界专家缓存。
- 完整开放权重的 Kimi K3 模型（2.78 万亿参数）被转换为 982 GiB 容器，在 64GB MacBook Pro 上实测约 0.49 至 0.54
  tok/s，最低 29.05 GiB 内存即可打开模型。
- 引擎将每个专家记录按 4 KiB 对齐存储，路由一个专家只需一次 pread，读取绕过页缓存（macOS 用 F_NOCACHE、Linux 用 O_DIRECT、Windows
  用 FILE_FLAG_NO_BUFFERING），专家权重以 3 位残差向量量化存储。
- 内存预算测试显示 32 GB 与 46 GB 预算时吞吐稳定在 0.50 与 0.53 至 0.55 tok/s，而 52 GB 与 58 GB 预算会因系统分页导致吞吐崩塌且结果不可复现。
- 引擎逐层通过 PyTorch 参考校验，最终 logits 与参考一致到 3.6e-06，视觉塔与自身 oracle 一致到 2.3e-06。
- 同一引擎与格式可运行 Kimi-Linear-48B-A3B-Instruct，容器仅 19 GB、内存下限 1.87 GB、速度达 10.7 tok/s，是尝试
  WASTE 的轻量路径。
object_mentions:
- object_type: project
  name: sqliteai/waste
  canonical_name: sqliteai/waste
  url: https://github.com/sqliteai/waste
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - WASTE 是一个用 C 编写的可嵌入式推理引擎，无任何第三方运行时依赖，将模型主干驻留内存并按需从磁盘流式读取专家权重。
  - WASTE 的当前证明点是完整开放权重的 Kimi K3 模型，以 982 GiB 容器运行在 64GB MacBook Pro 上，速度约 0.49 至
    0.54 个 token 每秒。
  - 该引擎提供二十六个公共函数，可通过 C API 在内存上限约束下打开模型、生成文本、保存会话并关闭。
  article_id: d6cfb2eda47ef1ed
- object_type: model
  name: Kimi K3
  canonical_name: Kimi K3
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Kimi K3 拥有 2.78 万亿参数，是 WASTE 引擎运行的完整开放权重模型，转换后容器大小为 982 GiB，并非蒸馏或剪枝变体。
  - Kimi K3 每个 token 需在 92 层中每层触及 16 个专家，合计读取约 17.0 GB 的专家权重。
  article_id: d6cfb2eda47ef1ed
- object_type: model
  name: Kimi-Linear-48B-A3B-Instruct
  canonical_name: Kimi-Linear-48B-A3B-Instruct
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 同一引擎和格式可运行 Kimi-Linear-48B-A3B-Instruct，其容器仅 19 GB、内存下限 1.87 GB，实测速度达 10.7 tok/s。
  - 文章将 Kimi-Linear 视为在投入整块硬盘存储 K3 之前先体验 WASTE 的推荐轻量路径。
  article_id: d6cfb2eda47ef1ed
extract_result: success
impact_score:
  score: 7.0
  reason: 评分依据：该事件是本地推理领域的一次实质性工程突破——首次在公开渠道验证了完整 2.78 万亿参数开放权重模型可在消费级 64GB 内存笔记本上通过磁盘流式运行，此前万亿级
    NVMe 流式推理无公开先例。这直接挑战了'前沿模型必须依赖数据中心级硬件或云端 API'的行业假设，对本地推理、边缘 AI 与隐私敏感部署的竞争格局有局部重塑意义。但
    0.5 tok/s 的吞吐对交互式使用完全不实用，短期内更偏向工程示范而非可落地产品，且需要 1TB 磁盘 + 64GB 内存的苛刻门槛限制了受众，故未达范式转移级别。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 磁盘流式推理能否让万亿级模型真正跑在消费级硬件上，以及 0.5 tok/s 的性能水分有多大
hype_assessment:
  level: low
  reason: 判定依据：文章用词高度克制且反 PR 套路——主动声明'未找到先例'是'邀请反例而非结论'、明确承认'它很慢且不应用作免责声明'、公开记录失败数字于
    docs/LEARNED.md、所有性能数据均标注在发布 commit 上实测。通篇无'颠覆''革命性'等包装词，反而详细披露了被测量后放弃的优化路径（路由器无尾部可降级、缓存无法驻留），属于典型的干货型工程文档，炒作水分极低。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破在于把 MoE 模型的稀疏性工程化到极致：每个 token 仅激活约 4% 的专家，因此将 97% 以上的闲置权重驻留磁盘，通过
    4 KiB 对齐的专家记录、路由一次即一次 pread、绕过页缓存（macOS F_NOCACHE / Linux O_DIRECT / Windows FILE_FLAG_NO_BUFFERING）实现按需流式读取，配合
    3 位残差向量量化将 K3 容器从 1.42 TB 压缩至 982 GiB。这把瓶颈从'内存容量'重构为'磁盘带宽'，并用 I/O 与算力重叠（约 1.6x
    收益）隐藏读取延迟，最终 logits 与 PyTorch 参考一致到 3.6e-06，证明了精度无损的可行性。
  business_model: 对云端 API 按 token 计费模式构成长期结构性挑战：万亿级模型若能在本地磁盘上运行，数据无需离开设备，'不得把数据发给
    API'与'就在本地跑'的边界被打破，可催生医疗、金融、法律等隐私敏感场景的本地部署形态。虽然 K3 档位 0.5 tok/s 尚不实用，但同一引擎在 48B
    档位达 10.7 tok/s 已接近可用，可能推动'模型即本地文件'的发行与分发模式，并对云推理服务商以'只有数据中心跑得动'为基础的定价叙事形成渐进式压力。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: 强制CoT：WASTE 的价值锚点不在 0.5 tok/s 的速度，而在它验证了一个可复利的技术命题——MoE 模型每 token 仅激活约 4%
    参数，'空闲权重不需要驻留内存、只需要按时可达'，磁盘流式 + 专家缓存可绕过消费级硬件的显存墙。该命题随开放权重前沿模型趋势（Kimi K3 2.78T
    真开源、而非蒸馏裁剪版）同步放大：只要开源前沿模型持续发布、消费级内存涨幅跟不上参数规模，磁盘流式推理就具备从极客证明演变为本地推理基础设施标准能力的路径，且其技术手法（O_DIRECT/F_NOCACHE
    绕过页缓存、4KiB 对齐单次 pread、3-bit 残差量化）大概率被 llama.cpp/MLX 等更广生态吸收，形成长期复利。扣分项：当前 0.5
    tok/s 仅支撑隐私敏感、气隙隔离、数据不出域等利基场景，可寻址市场有限；项目是社区级 proof-of-concept、无商业化路径与公司载体；且同时面临量化压缩、蒸馏小模型、云推理成本持续下降等多条替代技术路线的竞争。故落在'有潜力成为细分赛道基础设施、但需持续验证'的
    6-7 分区间，取 6.5。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Moonshot AI
- Apple
- sqliteai/WASTE
- llama.cpp 生态
competitive_casualty:
- 云端推理 API（隐私敏感/本地化场景）
- 闭源前沿模型厂商的云独占叙事
- 超大显存推理服务器方案
market_opportunities:
- 数据安全敏感型行业（金融、医疗、政务等）可借鉴 WASTE 的本地流式推理范式，将大参数模型部署于本地磁盘而非云端 API，从根本上规避数据传输合规风险，形成'本地私有化大模型'的差异化产品方案
- WASTE 中的专家级 NVMe 流式读取、4 KiB 对齐单次 pread、3-bit 残差向量量化等工程技术可被移植到 Ollama、llama.cpp 等本地推理生态，催生面向
  MoE 模型的端侧推理优化工具链创业机会
- 围绕超大模型本地运行的配套硬件与服务（高速 NVMe 存储、64GB+ 内存工作站、模型容器化转换服务）存在新的商业需求，可面向 AI 研究者与小规模团队提供一站式部署方案
risk_matrix:
  regulatory: Kimi K3 为 Moonshot AI 开放权重模型，本地部署可能涉及模型许可条款与跨境出口管制问题；本地运行绕过了 API 提供方的内容审核与合规控制，一旦被用于生成违法内容，责任可能转移至部署方，需评估模型来源国与使用地的合规边界
  technological: 当前 0.5 tok/s 的吞吐与每 token 读取 17GB 的磁盘 I/O 使其仅适用于非实时、低交互任务；WASTE 容器为专有格式，未来
    MoE 架构演进（更稠密路由、专家结构变化）可能使该格式失效；投机解码、KV 缓存压缩等新推理优化可能改变技术路线，使其优势被稀释
  competitive: 本地推理赛道已存在 llama.cpp、Ollama、vLLM 等成熟开源生态，主流云厂商的 API 服务在速度、成本与易用性上仍占压倒性优势；WASTE
    目前为个人/小团队维护，缺乏商业支持、文档生态与社区背书，恐难形成大规模采用
  ethical: 本地无监督运行万亿级模型将弱化安全对齐与内容护栏的作用，可能被用于离线生成有害或虚假内容，且难以被第三方审计；同时持续高负载磁盘流式读取带来显著能耗与
    SSD 寿命损耗，存在硬件层面的可持续性问题
  additional:
  - 982 GiB 容器外加 1.42 TB 暂存空间的高存储门槛大幅限制了普及范围，普通用户难以触达
  - 当前仅凭单一仓库自述，缺乏独立第三方复现验证，需警惕对'消费级设备运行万亿模型'叙事的技术炒作式误读
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: sqliteai/waste
  canonical_name: sqliteai/waste
  url: https://github.com/sqliteai/waste
  positioning: WASTE 是一个纯 C 编写的可嵌入式推理引擎，通过磁盘流式读取专家权重，让超大规模 MoE 开放权重模型能在消费级硬件上本地运行。
  technical_signal: 引擎将专家记录按 4 KiB 对齐存储，路由一个专家仅需一次 pread 并绕过页缓存直读磁盘，且逐层通过 PyTorch
    校验，最终 logits 一致到 3.6e-06。
  adoption_signal: null
  ecosystem_relevance: 项目支持无网络、无按 token 计费、数据不出本机的本地推理，与隐私敏感和离线优先场景下的开放权重模型生态直接相关。
  target_users: []
  product_signal: null
  market_signal: 文章以云端推理按 token 付费与数据中心耗电为对照，主张消费级本地推理可终结这种浪费，具备清晰且鲜明的市场叙事。
  differentiation: 项目方称未找到同等规模模型在消费级机器上磁盘流式运行的公开先例，宣称本项目的突破点在于可行性而非速度。
  watch_reason: WASTE 首次公开演示 2.78 万亿参数开放权重模型在 64GB 消费级笔记本上本地运行，突破了超大规模 MoE 的内存瓶颈，且引擎与格式同具体模型解耦，是本地推理可行性的关键信号。
  risk_notes:
  - 运行速度仅约 0.5 token/秒，单句回答需约 31 秒，实用性严重受限，现阶段只适合可行性验证。
  - 模型容器达 982 GiB，需准备 1TB 级内部 NVMe 磁盘，且 32GB 内存机器会严重分页，64GB 才是实际门槛。
  - 仓库无参考文献与对比表，宣称无同类公开先例属自述结论，尚缺第三方独立复现与验证。
  score: 7.0
  article_ids:
  - d6cfb2eda47ef1ed
  evidence_snippets:
  - WASTE 是一个用 C 编写的可嵌入式推理引擎，无任何第三方运行时依赖，将模型主干驻留内存并按需从磁盘流式读取专家权重。
  - WASTE 的当前证明点是完整开放权重的 Kimi K3 模型，以 982 GiB 容器运行在 64GB MacBook Pro 上，速度约 0.49 至
    0.54 个 token 每秒。
  - 该引擎提供二十六个公共函数，可通过 C API 在内存上限约束下打开模型、生成文本、保存会话并关闭。
---

**Kimi K3 — 2.78 trillion parameters — running on a consumer laptop.**

```
$ waste run ~/models/k3.waste 'What is the capital of Italy?'
waste: no --budget, using 46.24 GB of 64.00 GB (expert cache 17.56 GB)
The capital of Italy is **Rome**.
[16 tokens, 31.09 s, 0.51 tok/s | experts 3357 hit / 20195 miss = 14%]
```


WASTE is an embeddable inference engine written in C, with no third-party runtime dependencies. It keeps the model trunk in memory, streams selected experts directly from disk, and uses the remaining RAM as a bounded expert cache.

Its current proof point is the complete open-weights Kimi K3 model: 2.78 trillion parameters, converted into a 982 GiB container and running on a 64 GB MacBook Pro at 0.49–0.54 tokens per second. **This is not a distilled, pruned, or reduced variant**.

| Model | Container | Minimum RAM | Tested speed |
|---|---|---|---|
Kimi K3 2.78T |
982 GiB | 29.05 GiB | 0.49–0.54 tok/s |
Kimi-Linear 48B |
19 GiB | 1.87 GiB | 10.7 tok/s |

WASTE was written for that one model and that one constraint: **K3 does
not fit in the RAM of current mainstream consumer systems.** It is 1.42 TB
as published and 982 GB after conversion. But a mixture of experts
activates about 4% of itself per token, so almost all of that weight is
idle at any instant — and idle weight does not need to be in memory, it
needs to be *reachable in time*. WASTE keeps it on disk in a layout where
one expert costs exactly one read, streams what each token actually
needs, and spends every remaining byte of RAM on the part that repeats.

The engine is correct: every layer is validated against a PyTorch reference, the final logits agree to 3.6e-06, and the vision tower matches its own oracle to 2.3e-06. It is also slow — half a token per second, thirty seconds for the sentence above.

Both of those matter, and the second one should not be read as a disclaimer. We are not aware of another published demonstration of a model this size streaming from disk on a consumer machine: we found none for trillion-scale NVMe streaming, and the best-documented 671B-class recipes assume a server with a terabyte of DDR5. That is a report of what our search turned up rather than a survey — this repository carries no bibliography and no comparison table, so read it as an invitation to send a counter-example, not as a result. The interesting part is not the speed, it is that the whole thing is in the reachable range on a single consumer machine — and that from here the question is engineering rather than feasibility.

Where the levers were is not where they are. Overlapping the expert reads with the arithmetic was worth ~1.6x and shipped; the two that looked bigger — reading fewer bytes per token, and keeping more of them in RAM — were both measured and both refused, one because this family's router has no tail to demote and one because a cache the machine will not leave resident cannot be bought at any price. Even with the reads overlapped they are still 55% of a decode step against the arithmetic's 27%, so what is left is a faster disk or a machine with more RAM, not another pass over the kernels. docs/EFFICIENCY.md is the account of how each of those was priced, including the two that were built before being measured.

What that opens up, concretely: a frontier-scale model that answers with no network, no per-token invoice, and nothing leaving the machine — which is the difference between "you may not send that data to an API" and "run it here". The format and the engine are not K3-specific in any deep way; K3 is simply the hardest case that exists today, and a model that streams at 2.78T streams comfortably at 48B.

Every number in this document was measured on the commit it is published with, and the ones that were wrong are recorded as wrong in docs/LEARNED.md rather than quietly corrected.

Every token answered by a cloud service is paid for twice: once on the invoice, and once in the electricity of a datacenter running a model that would fit — barely, awkwardly, but genuinely — on hardware already sitting on a desk. WASTE means to be the first concrete step toward ending that waste of tokens. The acronym came second.

disk, for the model |
982 GB for the converted container — plan a terabyte |
| disk, to convert it | another 1.42 TB of staging for the published shards, freed afterwards |
RAM |
29.05 GB minimum to open K3 at 4K context; 64 GB for the numbers here |
| storage speed | the container must be on internal NVMe — see below |
| build | a C11 compiler and `make` . No BLAS, no CUDA, no Python at run time |

Sizes here are powers of two, the way `df`

and the engine both report
them: the container is 982 GiB, which a disk vendor would call 1.05 TB.

The RAM floor is what the engine refuses to start below, and it is almost entirely the 27.28 GB resident trunk. Useful throughput starts higher: on a 64 GB machine the engine gives itself a 46 GB budget, of which 17.56 GB is expert cache, and that is the top of the measured curve. A 32 GB machine can technically open the model and will page badly; treat 64 GB as the real requirement.

**Storage speed is not a detail.** A token reads 17 GB of experts. On the
internal SSD that is 12.78 GB/s and the model streams; over a USB
enclosure it is 0.94 GB/s and the same token takes thirteen seconds.
Convert onto internal NVMe, and use the external disk for the download
only.

If a terabyte is not available, the same engine and the same format run
`Kimi-Linear-48B-A3B-Instruct`

from a **19 GB** container with a
**1.87 GB** floor, at 10.7 tok/s. That is the good path for trying WASTE
out before committing a disk to K3.

**Self-contained.**One`libwaste.a`

, one`waste`

binary, nothing at run time beyond libc and pthreads.**Zero dependencies.**No BLAS, no ONNX, no Python in the inference path, nothing to install. The Python under`tools/`

converts models and validates the engine; it never runs alongside it.**Fully embeddable.**Twenty-six public functions in src/waste.h: open a model under a RAM ceiling, generate, save the session, close. The CLI is a client of that API and touches nothing private — if the CLI can do it, so can an embedding host.

```
waste_cfg cfg;
waste_cfg_init(&cfg);
cfg.ram_budget_bytes = 46ULL << 30; /* a hard ceiling, not a hint;
0 sizes it to this machine */
waste_ctx *ctx;
if (waste_open("/path/to/k3.waste", &cfg, &ctx) != WASTE_OK) return 1;
waste_generate(ctx, ids, n, ¶ms, on_token, user);
waste_close(ctx);
```

The path is the container directory the converter wrote — no `~`

expansion here, that is the shell's job.

A model is converted once into a `.waste`

container: a JSON manifest, a
resident trunk, and one expert bank per layer. Each expert record is
4 KiB-aligned with its gate, up and down matrices adjacent, so routing to
an expert costs exactly **one pread** — not three, not a seek per
matrix. The arithmetic was never the bottleneck.

Reads bypass the page cache (`F_NOCACHE`

on macOS, `O_DIRECT`

on Linux,
`FILE_FLAG_NO_BUFFERING`

on Windows). That is deliberate: with a container
smaller than RAM the kernel would cache everything, and the hit rates
measured that way are a fiction that does not survive contact with a
982 GB model.

Every record's header is checked on the way in — right magic, the expert
the index asked for, offsets that fit — so a bank that has been truncated
or spliced stops the generation and names the record instead of answering
from the wrong bytes. That costs nothing measurable. The record also
carries a `crc32`

over its payload, and checking *that* is `--verify`

,
off by default: it is a pass over every record on every cache miss, about
5% on Kimi-Linear and 1% on K3. Worth it for a container you copied or
downloaded and have not read since; not worth it on every token of one
you converted yourself. See docs/FORMAT.md.

Experts are stored as residual vector quantization — three stages of 256-entry codebooks over 8-dimensional vectors, 3.00 bits per weight — and the matrix is never materialized. For each token the engine builds a table of partial dot products, one per codebook entry per vector position, after which every expert row is three table reads and two adds.

The trunk stays at 4 and 8 bits. The model was trained with
quantization-aware training on the *experts* only, so it has no trained
tolerance for a squeezed trunk: a 3-bit trunk was built and measured, the
cache prediction held, the throughput did not, and the output collapsed.

The most predictive number in this project. K3 touches 16 experts in each
of 92 layers per token: **17.0 GB**. Below that, an expert cached for one
token is evicted before the next token asks for it, and the hit rate is
not low — it is zero.

What crossing it buys has changed, though, and the table below is the first
one to show it. Going from a 0% hit rate to 17% is worth about 8% of
throughput now — 0.50 to 0.54 — because read-ahead already hides most of
the I/O the cache would have saved. **The sharp bend in this curve is no
longer the climb above the floor; it is the collapse above 46 GB**, where
the engine stops fitting in the machine.

| budget | expert cache | hit rate | decode, observed |
|---|---|---|---|
| 32 GB | 3.32 GB | 0% | 0.50 tok/s |
| 46 GB | 17.32 GB | 17% | 0.53–0.55 tok/s |
| 52 GB | 23.32 GB | 31% | 0.04–0.15 — not reproducible |
| 58 GB | 29.32 GB | 39% | 0.02–0.03 tok/s |

**Ranges, not measurements**, and the width is the finding. Every run behind
a row reports cache statistics identical to the digit — the engine does the
same work each time — so what varies is the machine, not the engine.

The two rows that fit are tight. 32 and 46 GB reproduce to within a few percent, because the engine's whole footprint fits with room to spare and nothing has to be taken from anything.

**52 GB has no value.** Two runs of the default configuration gave 0.04 and
0.15; three more with the trunk wired gave 0.46, 0.19 and 0.03 — seven-fold
in the column above and fifteen-fold across both configurations,
against `3652 hit / 8124 miss`

every single time. That budget sits exactly
where the engine's footprint either does or does not fit beside whatever
else the machine is holding, and which side it lands on is decided before
the process starts. A row that spans 15x is not a slow row; it is a row
whose mean would invite a comparison there is nothing to compare.

58 GB is uniformly bad and reproducibly so.

Order still matters, and more than the table shows. Re-run *after* the 52
and 58 GB rows have driven the machine into paging, 46 GB collapses — 0.02
tok/s in one such run — while again reporting identical counts. Sweep
upward, one budget per quiet machine, and treat anything measured after a
paging row as void.

Read-ahead made the rows that fit faster and left the others where they
were, so the step is larger than when this was first measured: 46 GB went
0.32 to 0.54. Wiring the resident trunk with `WASTE_MLOCK=trunk`

does not
move it either — 32 and 46 GB are unchanged, 58 GB stays hopeless, and 52 GB
has no value to change. docs/LEARNED.md §30–33.

Everything in the memory design exists to get above that line, which is why the engine works to free RAM rather than to save it.

**And there is a ceiling on the other side, closer than it looks.** Read
that table twice: the hit rate climbs all the way down. At 58 GB on a
64 GB machine the cache serves 39% of experts from RAM and the engine is
*twenty times slower* than at 46 GB, where it serves 17%. The engine is
inside its budget; the *machine* is not, so the OS pages out the expert
cache, and a "hit" becomes a page fault instead of the disk read the
engine was managing.

So the usable window is narrow. It opens at ~46 GB, where the cache finally clears one token's working set, and it has already closed by 52 — on an otherwise idle machine, with 49 GB free before the run. It is also sharp enough to move under a change that looks unrelated: taking 1.11 GB of embedding table off the resident set fed straight into the cache at a fixed budget, and on the build of the day that was enough to push 58 GB from 0.32 tok/s to 0.04.

**So the default does not fill the machine.** Expert cache is only worth
anything in whole multiples of that working set, and the remainder above a
multiple buys a few points of hit rate while pushing the machine towards
paging. When it picks a budget for itself the engine steps down a whole
working set at a time and takes the largest that fits under seven eighths
of RAM: K3 asks for floor + 3× — 80.63 GB — and gets floor + 1× on this
laptop, a 46 GB budget and a 17.56 GB cache. That is the top of the curve
above, reached with no flag. A 128 GB machine still gets the full 3×.

An earlier version took every byte up to the cap instead, which put a 27 GB cache on this machine — between two budgets measured at 0.11 and 0.04 tok/s. The real lesson is that a cache you do not control is not a cache, and the corollary is that an engine should stop asking for memory before the OS starts taking it back.

K3's attention is a 3:1 hybrid: Kimi Delta Attention, which carries a
fixed-size recurrent state instead of a growing KV cache, and gated
multi-head latent attention. The MLA layers cache the 512-wide latent
rather than expanded per-head keys and values, with `kv_b_proj`

absorbed
into the query and the output:

```
q_nope · (W_kb c) == (W_kbᵀ q_nope) · c
Σ_s a_s (W_vb c_s) == W_vb (Σ_s a_s c_s)
```


Identical logits to 1.2e-05, and **53× less cache**: 11.25 GB becomes
0.21 GB at 4K context. It is also what makes long context possible at all
— the expanded layout wants 360 GB at 128K tokens, the latent one 7.2.

MacBook Pro M5 Pro, 64 GB, container on the internal SSD. Every figure was measured on the commit it is published with.

| minimum RAM | 29.05 GB at 4K context |
| 30.54 GB at 32K, 35.63 GB at 128K, 83.21 GB at 1M | |
| resident trunk | 27.28 GB |
| read per token | 17.0 GB, read ahead on two threads so it overlaps the matmuls |
| model load | 20 s |
| prefill | 0.47 tok/s chunked, 0.29 sequential (before read-ahead) |
| decode | 0.49–0.54 tok/s at the default budget, the best this machine gives |
| vision tower | 15.7 s for a 1024-patch image, 27 layers |
| image in a prompt | 256 positions for 896x896, 2.8 s each — as text |

The floor is almost entirely the resident trunk. Useful throughput starts above ~46 GB, where the expert cache finally clears one token's working set, and is gone again by 52, where the machine starts paging. Below the first line extra RAM buys nothing; above the second it costs, badly. The window is one budget wide on this machine.

The tower is not what an image costs. Encoding 1024 patches takes 15.7 s;
the 256 positions it produces then go through the 92 MoE layers like any
other token, which is the other 731 s. An image is priced as text of the same
length, so the patch budget in `vision.json`

is a real dial: halving the
grid halves the prompt.

| minimum RAM | 1.87 GB |
| decode | 10.7 tok/s at an 8 GB budget, 78% cache hit |

The same engine and the same format, on a model that fits comfortably. This is what WASTE looks like when it is not fighting.

Decode on K3, 17.32 GB of cache and still cold — 6.7% hit over ten steps, which is the state a fresh prompt starts in:

| share | |
|---|---|
| MoE, all of it | 82.5% |
| of which expert I/O | 53.5% |
| of which expert matmul | 20.0% |
| KDA layers | 14.5% |
| MLA layers | 2.8% |
| lm_head | 0.2% |

Reproduce with `WASTE_PROFILE=1 WASTE_CACHE_MB=17735 ./test_forward MODEL 1008,10484,318,15383,387 out.bin 5`

. The I/O share falls as the
cache warms, so a long session sits lower than this; the ranking does
not change.

The I/O already runs near the hardware limit — 17.0 GB per token at ~9.9 GB/s against the SSD's measured 12.78 — so it only gets cheaper by happening less often, which means cache, which means RAM. That is the whole optimization story so far, and the reason the next steps are about memory rather than arithmetic.

```
git clone https://github.com/sqliteai/waste && cd waste
make # libwaste.a, waste, libwastevq
make check # 23 pass, 11 skip on a fresh clone
```

No configure step and no dependency resolution. `make check`

needs no
model: it builds a small synthetic container and runs the engine against
it. The eleven skips are the checks that need something a clone does not
carry — the PyTorch oracle, the round-trip against the source shards,
anything driving the CLI with text, since the synthetic container carries
no tokenizer, and the K3 checks, which want the container and the release
on disk. With both containers present the suite is 36 checks.

Conversion is the one step that needs Python, and it happens once. The source is moonshotai/Kimi-K3 exactly as published — 96 safetensors shards, 1.42 TB, nothing patched:

```
# 1. preflight: reachable? how big? does it fit?
tools/fetch_weights.sh --dest /Volumes/staging/k3 --dry-run
# 2. download — resumable, safe to kill, safe to re-run
tools/fetch_weights.sh --dest /Volumes/staging/k3
# 3. convert into a container
uv run --with torch --with safetensors python tools/convert.py \
--src /Volumes/staging/k3 \
--out ~/models/k3.waste --jobs 3
```

That produces the 982 GB container every number above was measured on. It
takes about **4.7 hours** with three processes on the M5 Pro (23.7 with
the pure-torch encoder — see docs/K3.md), and wants ~1.0 TB
free on the target volume. The converter is resumable too: a layer whose
bank is already written is skipped, so an interrupted run costs only the
layer it was in the middle of.

The download is the part that goes wrong. A 1.42 TB pull over hours will
hit dropped connections, CDN 5xx and at least one interrupted run, so
every shard resumes mid-file rather than restarting, retries with
exponential backoff and jitter, and counts as done only when its size
matches Content-Length — recorded in a state file, so a re-run skips
finished shards without even a HEAD request. `--check`

re-verifies
everything on disk against the remote and downloads nothing (96 shards in
34 s). `--repo`

points it at another model, `HF_TOKEN`

at a gated one.
macOS and Linux.

Give `--dest`

a staging disk rather than the volume that will hold the
container. The shards are read once, by the converter; the container is
read continuously, at every token. On this machine the external enclosure
measures **0.94 GB/s** against the internal NVMe's **12.78** — see
docs/GATES.md, Gate H — which is the difference between
a model that streams and one that stalls.

`tools/pipeline.sh`

chains the whole thing unattended — download, convert,
round-trip the container against the source weights, generate, then diff
the logits against the PyTorch oracle — and leaves a report next to the
container. The same converter handles the other member of the family,
`Kimi-Linear-48B-A3B-Instruct`

, into the 19 GB container of the second
benchmark; `--src`

is the only thing that changes.

**Pre-converted containers are on their way to
huggingface.co/sqliteai**, at which
point this whole section becomes a download and the Python is only needed
for models we have not published.

The container is the directory the converter wrote, so give it that path —
`~/models/k3.waste`

throughout this README:

```
waste run ~/models/k3.waste "The capital of France is" -n 32
waste chat ~/models/k3.waste # multi-turn, state kept
waste eval ~/models/k3.waste "2 + 2 =" --top-k 5 # next-token distribution
waste plan ~/models/k3.waste --budget 46G # what fits, what does not
echo "prompt" | waste run ~/models/k3.waste # stdin works too
```

`-n`

is a cap, not a requirement: without it generation stops at the
container's end-of-sequence token or at 128 tokens, whichever comes
first. The examples pass it because 128 tokens of K3 is six minutes.

`--budget`

is optional, and leaving it out is the right default rather
than a fallback: the engine takes the container's recommendation, steps it
down a whole token working set at a time until it fits under seven eighths
of physical RAM, and never goes below the floor — a budget you set
explicitly under the floor is refused rather than swapped into. It then
says on stderr what it landed on, so the same command on two machines is
not silently two different runs:

```
waste: no --budget, using 46.24 GB of 64.00 GB (expert cache 17.56 GB)
```


`--verify`

checks each expert record's `crc32`

as it comes off the disk.
It is off by default, and that is a throughput decision rather than a
claim that containers do not rot: it is a pass over every record on every
cache miss, about 5% on Kimi-Linear and about 1% on K3, where the read
dominates. Turn it on once for a container you copied, downloaded, or left
on a disk you do not trust, and for anything whose wrong answers would be
believed; leave it off for one you converted yourself and have been
reading since. `WASTE_VERIFY=1`

in the environment does the same thing,
and the server takes `--verify`

as well. Any of them turns it on; none of
them turns it off.

What is checked either way: a short read, and a record header that does
not describe the expert the bank index asked for. Those are O(1), they
cost nothing measurable, and they are what keeps a damaged offset out of
the arithmetic — `--verify`

only adds the pass over the payload.

`waste --help`

lists all nine commands. `--json`

makes `eval`

, `tokenize`

,
`plan`

, `info`

and `bench`

machine-readable.

`serve/`

is an OpenAI-compatible HTTP server — the second client of the
public API, alongside the CLI, reaching the same engine through ctypes
rather than keeping a copy of the model code in Python:

```
make libwaste.dylib # or libwaste.so on Linux
python3 -m serve ~/models/k3.waste --port 8000
```

```
curl localhost:8000/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"k3","messages":[{"role":"user","content":"Why is the sky blue?"}]}'
```

`/v1/chat/completions`

(streaming and not), `/v1/completions`

,
`/v1/models`

, `/health`

. It carries the whole of K3's prompt format, not
the four-string subset a container's `chat.json`

can hold: **tool
definitions and tool results, typed call arguments, JSON response schemas,
tool_choice, the think channel and thinking_effort, and images** — plus
the parser that reads the reply back into reasoning, answer and


`tool_calls`

. Stdlib only.The prompt renderer is a port of `encoding_k3.py`

from the release, and the
test suite checks it against that file **segment for segment** on a corpus
of 38 conversations whenever the weights directory is on disk.
docs/SERVE.md is the reference.

K3 is multimodal — a 401M ViT, 27 layers, patch 14 — and so is the engine.
`--image`

attaches a picture; repeat it for several:

```
$ waste run ~/models/k3.waste 'What is in this picture?' --image landscape.png
[landscape.png: 192 image tokens]
The picture shows a simple, stylized landscape with:
- A **blue sky** with a gradient from darker blue at the top to lighter blue near the horizon.
- A **yellow sun** in the upper right.
- A **gray hill or mountain** in the middle distance.
- A **green field** covering the lower part of the image.
[78 tokens, 234.25 s, 0.33 tok/s | experts 15314 hit / 99502 miss = 13%]
```


(That transcript predates read-ahead and its timing line is the old one — the picture it was run against is not in this repository, so it is left as recorded rather than re-timed. Same tokens, about 1.6x less waiting.)

That is a 448×336 image, and every element of the description is in it — including the sky gradient, which is the kind of detail that separates a tower that works from one that merely runs. The picture was generated by a twenty-line script rather than photographed, so the answer can be checked against what was drawn instead of against an impression.

PNG, JPEG, GIF, BMP, TGA and PSD, decoded by the one vendored header in
`third_party/`

. It works on `run`

, `chat`

and `eval`

; inside a chat,
`/image FILE`

attaches a picture to the next message, and it is spliced
once — the positions are in the attention state afterwards, so later turns
discuss the same photograph without re-encoding it. The 27-layer ViT is
loaded only when an image is present. Its weights are 434 MB, but the
reservation is 1.12 GB: the bounded source decode, the tower's activations
and the queued image embeddings are memory too, and all of it otherwise
comes straight out of the expert cache.

An image is not one token. The tower turns a 14-pixel patch grid into one
embedding per merged 2×2 patch, and each occupies a position in the
sequence — the 448×336 above is 192 of them, an 896×896 photo at the
default budget is 256. That is worth knowing before wondering where a
context window went, and it is most of what an image costs: the 234 s in
the transcript is the 78 generated tokens alone, and the picture is paid
for before that, in prefill. **An image is priced as text of the same
length.** The tower is the cheap part — 15.7 s for a full 1024-patch
image — and its output then walks through 92 MoE layers like any other
token. Halving `max_patches`

in `vision.json`

halves the bill.

Through the library it is three calls, because a host needs to size the prompt before committing to it:

```
size_t rows;
waste_image_add(ctx, "photo.png", &rows); /* encode and queue */
waste_image_expand(ctx, raw, n, ids, cap, &n_ids); /* placeholder -> N */
waste_generate(ctx, ids, n_ids, ¶ms, cb, u); /* consumes the queue */
```

The tower's shape, the patch budget and the pixel normalization live in
`vision.json`

, which the converter writes from the release's own nested
`vision_config`

and from `preprocessor_config.json`

. K3 normalizes to
[-1, 1] with mean = std = 0.5.

That last sentence was wrong here for a day, and the way it was wrong is
worth keeping. This section used to say **K3 ships no preprocessor
config**, so the normalization was "the CLIP convention this lineage of
towers uses rather than a value read out of the release" — an assumption,
labelled as one. The release does ship the file; the downloader fetched a
hardcoded list of filenames and never asked the repo what it contained.
The tower still matched its oracle at 2.3e-06 throughout, because the
oracle is fed random pixels and never touches the normalization. An
honest caveat is not a substitute for reading the file.

| build | model-free suite | backend | |
|---|---|---|---|
| macOS arm64 | yes | 23 pass / 0 fail / 11 skip | NEON |
| Linux arm64 | yes | 23 pass / 0 fail / 11 skip | NEON |
| Linux x86_64 | yes | 23 pass / 0 fail / 11 skip | AVX2 |
| Windows x86_64 | yes | container, CLI and forward pass — see below | AVX2 |

The first three run the same suite and now agree check for check: same
23 passes, same 11 skips, same list. CI has no container, so
`tests/run.sh`

builds a synthetic one and the checks that need real
weights say SKIP rather than passing quietly. All three also pass the
sanitizer suite and 400 fuzz cases.

Windows is cross-compiled with MinGW-w64 on a Linux runner and then run
on a Windows one: the binary reads a synthetic container, opens it from
the CLI, and produces the same logits token-by-token as it does in
chunks. It is not the same suite — `tests/run.sh`

is a bash script that
rebuilds first, and the Windows job runs binaries it did not build — so
what is claimed is what that job checks and no more. Nobody has run it on
a real container there.

The platform is the variable, the suite is not, and that is the point:
both Linux targets produce the same continuation as macOS and pass
*engine matches the PyTorch oracle* when given a container, so the
numerics carry across architectures and compilers.

SIMD is selected at run time from CPUID, so a single x86 binary uses AVX-512 where it exists and AVX2 where it does not. Accelerator backends are build-time options. A Metal backend exists and is off by default because it is correct and 22% slower: this engine issues several hundred small dependent matvecs per token, the worst possible shape for an accelerator, and the CPU path already runs at the machine's memory bandwidth.

```
src/ the engine — 6,000 lines of C, no dependencies
model.c forward pass, MoE routing, KDA and MLA layers
ecache.c bounded LFRU expert cache over the banks
vision.c the 27-layer ViT and the projector into text space
image.c a file on disk to the patch tensor the tower wants
waste.c the public API
simd_*.c per-ISA kernels, selected at run time
cli/ the CLI, a client of the public API
serve/ the OpenAI-compatible server, the other client
xtml.py K3's prompt format, ported from the release's encoding_k3.py
regions.py its replies, back into reasoning / answer / tool calls
engine.py libwaste through ctypes, and the request queue
server.py /v1/chat/completions and friends
tools/ conversion and validation (Python, never at run time)
docs/ format, engine, backends, and what was learned
tests/ 34 checks, and a diff against a PyTorch oracle given a model
serve/ 149 more for the server, incl. a differential vs upstream
examples/ chat.json for K3 and ChatML, the format a container carries
third_party/ stb_image.h, the single vendored header — see its README
```


docs/LEARNED.md is the one to read before contributing. It records what was measured, including the optimizations that were refuted — index-layout blocking, a 3-bit trunk, GPU offload, per-expert bit allocation — with the numbers that killed them.

The API is not frozen, as above. The rest is stated plainly too, because finding these out for yourself is worse than reading them here:

- a container carries its chat format in
`chat.json`

, and the converter can only fill it in for a model whose format has been transcribed from its reference encoder — K3 today. Neither Kimi release distributes a template, so for anything else the CLI says so and continues raw rather than guessing a format, which would produce plausible wrong answers instead of visibly wrong ones. Kimi-Linear is in that position now; - AVX-512 compiles and is dispatched from CPUID, and has still never
executed an instruction. This laptop is ARM and its x86 emulation is
Rosetta, which reports AVX2 and leaves the ZMM state disabled in XCR0;
the hosted x86 runner is an AMD EPYC 7763, which answers
`avx512f/bw/dq/vl: no`

, so CI says**AVX2**as well — on Linux and on Windows both. The workflow prints the runner's flags before every build, so the day a runner has them the*SIMD backend matches the CPU baseline*check becomes the confirmation without anyone arranging it; **Windows builds and runs, on one toolchain and one CPU.**MinGW-w64 x86_64, cross-compiled, with`src/platform.h`

holding the six calls that are not POSIX: the positional read, the aligned allocation, the CPU count, the file size and`FILE_FLAG_NO_BUFFERING`

for the cache-bypass open. MSVC is a different port and has not been attempted — the sources use GNU C. ARM64 Windows is not built. Neither is the page-cache bypass proven under load there: CI confirms Windows grants it on the runner's filesystem, which is not the same as measuring a hit rate against a container that does not fit in RAM;**the expert checksum is off unless you ask for it**(`--verify`

), and the trunk has no checksum at all. The first is a decision — 5% of throughput on every token, against a container that is usually fine — and it means the default build of a rotted container still answers with whatever the damaged bytes decode to. Run`--verify`

once after copying a container, to establish that it arrived intact.`tools/verify_container.py`

does not stand in for that: it re-derives records against the**source**weights, so it wants torch and the original checkpoint on disk, and it answers whether the conversion was right rather than whether the copy still is. The second is not a decision: the trunk and the codebooks have nothing to check against in the format, and nothing has been built in its place;- every expert in a container is at the same bit width. The non-uniform
per-expert allocation the format was designed around is
**not coming**: it was measured on both models rather than built, and the importance it would allocate against does not vary — the value of the third bit spreads at most 1.15x between experts in a layer and 1.01x between layers, so the optimal allocator and a coin flip write the same container. The one signal that is not flat, routing frequency, buys disk footprint and almost no I/O, which is the resource that is actually scarce. docs/LEARNED.md §20 has the table and the one measurement that would revive it.

Apache 2.0 — see LICENSE. Copyright 2026 SQLite Cloud, Inc.