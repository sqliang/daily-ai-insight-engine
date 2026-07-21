---
title: kvcache-ai/ktransformers
source: https://github.com/kvcache-ai/ktransformers
author: []
published: ''
created: '2026-07-20'
manifest_dates:
- '2026-07-20'
description: 'A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune
  Optimizations A Flexible Framework for Experiencing Cutting-edge LLM Inference/Fine-tune
  Optimizations 🎯 Overview | 🚀 Inference | 🎓 SFT | 🔥 Citation | 🚀 Roadmap(2026Q2)
  🎯 Overview KTransformers is a research project focused on efficient inference and
  fine-tuning of large language models through CPU-GPU heterogeneous computing. The
  project now exposes two user-facing capabilities from the kt-kernel source tree:
  Inference and SFT. 🔥 Updates June 21, 2026: MiniMax-M3 Day0 Support! (Tutorial)
  June 17, 2026: GLM-5.2 Day0 Support! (Tutorial) May 6, 2026: KTransformers at GOSIM
  Paris 2026 — "Agentic AI on Edge" track. We''ll present KT''s inference performance
  on consumer hardware. May 02, 2026: DeepSeek-V4-Flash Support! (Tutorial) Apr 30,
  2026: KTransformers v0.6.1 refreshes kt-kernel inference and SFT docs with separate
  Inference and SFT Quick Start entry points. Mar 26, 2026: Support AVX2-only CPU
  backend for KT-Kernel inference. (Tutorial) Feb 13, 2026: MiniMax-M2.5 Day0 Support!
  (Tutorial) Feb 12, 2026: GLM-5 Day0 Support! (Tutorial) Jan 27, 2026: Kimi-K2.5
  Day0 Support! (Tutorial) (SFT Tutorial) Jan 22, 2026: Support CPU-GPU Expert Scheduling,
  Native BF16 and FP8 per channel Precision and AutoDL unified fine-tuning and inference
  Dec 24, 2025: Support Native MiniMax-M2.1 inference. (Tutorial) Dec 22, 2025: Support
  RL-DPO fine-tuning with LLaMA-Factory. (Tutorial) Dec 5, 2025: Support Native Kimi-K2-Thinking
  inference (Tutorial) Nov 6, 2025: Support Kimi-K2-Thinking inference (Tutorial)
  and fine-tune (Tutorial) Nov 4, 2025: KTransformers Fine-Tuning × LLaMA-Factory
  Integration. (Tutorial) Oct 27, 2025: Support Ascend NPU. (Tutorial) Oct 10, 2025:
  Integrating into SGLang. (Roadmap, Blog) Sept 11, 2025: Support Qwen3-Next. (Tutorial)
  Sept 05, 2025: Support Kimi-K2-0905. (Tutorial) July 26, 2025: Support SmallThinker
  and GLM4-MoE. (Tutorial) July 11, 2025: Support Kimi-K2. (Tutorial) June 30, 2025:
  Support 3-layer (GPU-CPU-Disk) prefix cache reuse. May 14, 2025: Support Intel Arc
  GPU (Tutorial). Apr 29, 2025: Support AMX-Int8、 AMX-BF16 and Qwen3MoE (Tutorial)
  Apr 9, 2025: Experimental support for LLaMA 4 models (Tutorial). Apr 2, 2025: Support
  Multi-concurrency. (Tutorial). Mar 15, 2025: Support ROCm on AMD GPU (Tutorial).
  Mar 5, 2025: Support unsloth 1.58/2.51 bits weights and IQ1_S/FP8 hybrid weights.
  Support 139K Longer Context for DeepSeek-V3 and R1 in 24GB VRAM. Feb 25, 2025: Support
  FP8 GPU kernel for DeepSeek-V3 and R1; Longer Context. Feb 15, 2025: Longer Context
  (from 4K to 8K for 24GB VRAM) & Slightly Faster Speed （+15%, up to 16 Tokens/s),
  update docs and online books. Feb 10, 2025: Support Deepseek-R1 and V3 on single
  (24GB VRAM)/multi gpu and 382G DRAM, up to 3~28x speedup. For detailed show case
  and reproduction tutorial, see here. Aug 28, 2024: Decrease DeepseekV2''s required
  VRAM from 21G to 11G. Aug 15, 2024: Update detailed tutorial for injection and multi-GPU.
  Aug 14, 2024: Support llamfile as linear backend. Aug 12, 2024: Support multiple
  GPU; Support new model: mixtral 8*7B and 8*22B; Support q2k, q3k, q5k dequant on
  gpu. Aug 9, 2024: Support windows native. 📦 Capabilities 🚀 Inference - High-Performance
  kt-kernel Serving CPU-optimized kernel operations for heterogeneous LLM inference.
  Key Features: AMX/AVX Acceleration: Intel AMX and AVX512/AVX2 optimized kernels
  for INT4/INT8 quantized inference MoE Optimization: Efficient Mixture-of-Experts
  inference with NUMA-aware memory management Quantization Support: CPU-side INT4/INT8
  quantized weights, GPU-side GPTQ support Easy Integration: Clean Python API for
  SGLang and other frameworks Quick Start: cd kt-kernel pip install . Use Cases: CPU-GPU
  hybrid inference for large MoE models Integration with SGLang for production serving
  Heterogeneous expert placement (hot experts on GPU, cold experts on CPU) Performance
  Examples: Model Hardware Configuration Total Throughput Output Throughput DeepSeek-R1-0528
  (FP8) 8×L20 GPU + Xeon Gold 6454S 227.85 tokens/s 87.58 tokens/s (8-way concurrency)
  👉 Full Documentation → 🎓 SFT - Fine-Tuning with LLaMA-Factory KTransformers × LLaMA-Factory
  integration for ultra-large MoE model fine-tuning. Key Features: Multi-Backend Support:
  CPU/GPU hybrid fine-tuning with INT8/INT4 quantization Ultra-Large MoE Support:
  Fine-tune models like DeepSeek-V3/R1 on limited GPU memory Faster than ZeRO-Offload:
  6-12x training speedup in benchmarked MoE SFT workloads Lower CPU Memory: About
  half the CPU memory of the previous KT SFT path in the benchmarked setup LLaMA-Factory
  Integration: Seamless integration with popular fine-tuning framework Model GPU Memory
  Training Speed Hardware DeepSeek-V3 ~80GB total 3.7 it/s 4x RTX 4090 DeepSeek-R1
  ~80GB total 3.7 it/s 4x RTX 4090 Qwen3-30B-A3B ~24GB total 8+ it/s 1x RTX 4090 Quick
  Start: cd /path/to/LLaMA-Factory pip install -e . pip install -r requirements/ktransformers.txt
  CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \ --config_file examples/ktransformers/accelerate/fsdp2_kt_int8.yaml
  \ src/train.py \ examples/ktransformers/train_lora/qwen3_5moe_lora_sft_kt.yaml 👉
  Quick Start → 👉 Full Documentation → 🔥 Citation If you use KTransformers in your
  research, please cite our paper: @inproceedings{10.1145/3731569.3764843, title =
  {KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE
  Models}, author = {Chen, Hongtao and Xie, Weiyu and Zhang, Boxin and Tang, Jingqi
  and Wang, Jiahao and Dong, Jianwei and Chen, Shaoyuan and Yuan, Ziwei and Lin, Chen
  and Qiu, Chengyu and Zhu, Yuening and Ou, Qingliang and Liao, Jiaqi and Chen, Xianglin
  and Ai, Zhiyuan and Wu, Yongwei and Zhang, Mingxing}, booktitle = {Proceedings of
  the ACM SIGOPS 31st Symposium on Operating Systems Principles}, year = {2025} }
  👥 Contributors & Team Developed and maintained by: MADSys Lab @ Tsinghua University
  Approaching.AI 9#AISoft Community contributors We welcome contributions! Please
  feel free to submit issues and pull requests. 💬 Community & Support GitHub Issues:
  Report bugs or request features WeChat Group: See archive/WeChatGroup.png 📦 KT original
  Code The original integrated KTransformers framework has been archived to the archive/
  directory for reference. The project now organizes the two capabilities above from
  the kt-kernel source tree for clearer documentation and maintenance. For the original
  documentation with full quick-start guides and examples, see: archive/README.md
  (English) archive/README_ZH.md (中文)'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: cdbcdde49a4f0343
source_type: community_discussion
tldr: KTransformers 是清华大学 MADSys Lab 主导的开源项目，通过 CPU-GPU 异构计算实现大语言模型的高效推理与微调，支持 DeepSeek-V3/R1、Kimi-K2、GLM-5
  等最新 MoE 模型，提供 kt-kernel 推理引擎和 LLaMA-Factory 微调集成两大能力，研究论文发表于 ACM SIGOPS SOSP 2025。
objective_summary: KTransformers 由清华大学 MADSys Lab、Approaching.AI 和 9#AISoft 联合开发，研究论文已被
  ACM SIGOPS SOSP 2025 会议收录。项目通过 kt-kernel 推理引擎和 KTransformers × LLaMA-Factory 微调集成两条路径，实现
  MoE 大模型在消费级硬件上的 CPU-GPU 异构运行。kt-kernel 利用 Intel AMX/AVX 指令集和 INT4/INT8 量化实现高效推理，微调路径支持
  DeepSeek-V3 在 4×RTX 4090 上以 3.7 it/s 的速度训练。项目持续为 MiniMax-M3、GLM-5.2、DeepSeek-V4-Flash
  等前沿模型提供 Day0 支持，并兼容 AMD ROCm、Intel Arc 和 Ascend NPU 等硬件后端。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Tsinghua University
  - MADSys Lab
  - Approaching.AI
  - 9#AISoft
  technologies:
  - MoE
  - CPU-GPU heterogeneous computing
  - AMX
  - AVX
  - INT4 quantization
  - INT8 quantization
  - SFT
  - GPTQ
  - NUMA
  - FP8
  - BF16
  - ROCm
  - Ascend NPU
  - unsloth
  - GPU-CPU-Disk prefix cache
  key_people:
  - Hongtao Chen
  - Weiyu Xie
  - Boxin Zhang
  - Jingqi Tang
  - Mingxing Zhang
key_logic_flow:
- KTransformers 是清华大学 MADSys Lab 等团队开发的开源研究项目，通过 CPU-GPU 异构计算技术实现大语言模型的高效推理和微调，研究论文已被
  ACM SIGOPS SOSP 2025 收录。
- 项目整理为两条核心能力路径：kt-kernel 推理引擎专注于 CPU 优化的异构推理，KTransformers × LLaMA-Factory 集成专注于超大规模
  MoE 模型的微调。
- kt-kernel 利用 Intel AMX/AVX512/AVX2 指令集优化 INT4/INT8 量化推理，支持 MoE 专家路由的 NUMA 感知内存管理，以及
  GPU 侧 GPTQ 量化，可达成 DeepSeek-R1-0528 在 8×L20 GPU 上 227.85 tokens/s 的总吞吐量。
- KTransformers × LLaMA-Factory 集成支持 CPU-GPU 混合微调，在 DeepSeek-V3 上仅需 4×RTX 4090 约 80GB
  总显存即可达到 3.7 it/s 的训练速度，相比 ZeRO-Offload 实现 6-12 倍加速。
- 项目持续追踪前沿模型发布，为 MiniMax-M3、GLM-5.2、DeepSeek-V4-Flash、Kimi-K2.5 等模型提供 Day0 推理和微调支持，并已扩展至
  AMD ROCm、Intel Arc GPU 和 Ascend NPU 等多样化硬件后端。
- kt-kernel 提供简洁的 Python API 可集成到 SGLang 等生产级推理框架中，并支持 3 层（GPU-CPU-磁盘）前缀缓存复用和多并发推理。
object_mentions:
- object_type: project
  name: kvcache-ai/ktransformers
  canonical_name: kvcache-ai/ktransformers
  url: https://github.com/kvcache-ai/ktransformers
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - KTransformers 是清华大学 MADSys Lab 主导的开源研究项目，专注于通过 CPU-GPU 异构计算实现大语言模型的高效推理与微调。
  - 项目提供 kt-kernel 推理引擎和 KTransformers × LLaMA-Factory 微调集成两条核心能力路径，已从原始集成框架迁移至 kt-kernel
    源码树组织。
  - KTransformers 的研究论文已被 ACM SIGOPS SOSP 2025 会议收录，论文作者来自清华大学 MADSys Lab、Approaching.AI
    和 9#AISoft。
  article_id: cdbcdde49a4f0343
- object_type: project
  name: kt-kernel
  canonical_name: kt-kernel
  url: https://github.com/kvcache-ai/ktransformers
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - kt-kernel 是 KTransformers 的推理引擎子项目，提供 AMX/AVX 加速的 CPU 优化内核操作，支持 INT4/INT8 量化推理和
    MoE 模型的 CPU-GPU 异构部署。
  - kt-kernel 支持 DeepSeek-R1-0528 在 8×L20 GPU 加 Xeon Gold 6454S 配置下达到 227.85 tokens/s
    的总吞吐量。
  - kt-kernel 提供简洁的 Python API 可集成到 SGLang 等框架中，并支持多硬件后端包括 AMD ROCm、Intel Arc GPU
    和 Ascend NPU。
  article_id: cdbcdde49a4f0343
- object_type: project
  name: LLaMA-Factory
  canonical_name: LLaMA-Factory
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - KTransformers 与 LLaMA-Factory 集成实现超大规模 MoE 模型的 CPU-GPU 混合微调，在 4×RTX 4090 上 DeepSeek-V3
    训练速度可达 3.7 it/s。
  - KTransformers 微调路径相比 ZeRO-Offload 实现 6-12 倍训练加速，CPU 内存占用约为此前 KT 微调路径的一半。
  - 集成支持通过 accelerate 和 FSDP2 配置启动微调，提供预设的 LoRA SFT 训练配置文件。
  article_id: cdbcdde49a4f0343
- object_type: project
  name: SGLang
  canonical_name: SGLang
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - KTransformers 计划将 kt-kernel 集成到 SGLang 中，相关路线图和博客已在 GitHub 上发布。
  - kt-kernel 提供简洁的 Python API，支持与 SGLang 等生产级推理框架的集成。
  article_id: cdbcdde49a4f0343
extract_result: success
impact_score:
  score: 7.0
  reason: KTransformers 通过 CPU-GPU 异构计算显著降低了 MoE 大模型的部署和微调门槛：4×RTX 4090 即可微调 DeepSeek-V3，6-12x
    加速相比 ZeRO-Offload，SOSP 2025 顶会论文验证了技术严谨性。这不是范式转移（不改变模型能力上限），但对 AI 产业链的部署成本结构有实质性重塑——让消费级硬件运行前沿
    MoE 模型成为可行选项，直接降低了实验门槛和加速开源生态创新。评分 7.0 属于'改变局部竞争格局'范畴的高端。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 消费级硬件（4×RTX 4090）即可微调 DeepSeek-V3 等千亿参数 MoE 模型
hype_assessment:
  level: low
  reason: 项目提供具体可验证的性能指标（227.85 tokens/s 吞吐量、3.7 it/s 训练速度、6-12x 加速比），已在实际硬件上跑通，支持多种硬件后端和前沿模型
    Day0 支持。有 SOSP 2025 顶会论文背书，README 采用技术文档式叙述，无明显 '颠覆''革命性' 等 PR 滥用词汇。
information_entropy: high
domain_disruption:
  technical_innovation: CPU-GPU 异构计算架构实现 MoE 模型在消费级硬件上的实用化推理与微调。核心创新包括：NUMA 感知的 MoE
    专家路由调度、Intel AMX/AVX512 指令集优化的 CPU 侧 INT4/INT8 量化推理、3 层 GPU-CPU-磁盘前缀缓存复用、以及混合训练中相比
    ZeRO-Offload 实现 6-12 倍加速的 CPU-GPU 协同微调策略。
  business_model: 作为开源基础设施，直接挑战云 API 推理和微调的定价模式——使团队无需租赁 A100/H100 集群即可在本地运行和微调前沿
    MoE 模型。这降低了 AI 实验的资本门槛，可能催生更多 '本地优先' 的 AI 应用生态，并改变 MoE 模型的部署经济学。
engineering_complexity: production_ready
compound_value:
  score: 7.5
  reason: KTransformers 的长期复利逻辑建立在 MoE 模型参数量持续增长与消费级硬件算力瓶颈之间的结构性剪刀差上：(1) 随着 DeepSeek、Kimi、GLM
    等前沿 MoE 模型的专家数量和总参数持续膨胀，CPU-GPU 异构计算的必要性只会递增而非递减，这是一个不可逆的技术趋势；(2) SOSP 2025 顶会论文背书赋予项目学术壁垒和人才吸引力，降低了被纯工程方案替代的风险；(3)
    Day0 支持最新模型的策略创造了强大的用户黏性和社区网络效应——用户习惯一旦建立，迁移成本很高；(4) 同时覆盖推理和微调两大核心场景，且已集成到 SGLang
    生产级框架中，具备从工具向平台跃迁的潜力。但扣分项在于：项目是清华主导的开源研究项目，缺乏清晰的商业化闭环和收入模型，长期价值捕获严重依赖 Approaching.AI
    和 9#AISoft 的商业化落地能力，存在开源项目被大厂 fork 或社区分裂的风险。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Intel
- AMD
- Approaching.AI
- 9#AISoft
- SGLang
- LLaMA-Factory
competitive_casualty:
- NVIDIA 推理级 GPU 需求
- 闭源推理优化引擎
- 纯 GPU 密集型云推理服务
market_opportunities:
- 中小企业与个人开发者可在消费级显卡上对DeepSeek-V3/R1等超大规模MoE模型进行微调，大幅降低大模型私有化部署的硬件门槛，催生模型定制服务和行业垂直微调方案的商业机会
- 基于kt-kernel推理引擎可为AI Agent等延迟敏感场景提供CPU-GPU混合推理服务，利用冷热专家路由策略在单机多卡环境下实现高吞吐，有望成为边缘AI和本地化推理的基础设施组件
- KTransformers的Day0模型适配能力使其具备成为MoE模型生态"桥梁层"的潜力，围绕该项目的部署咨询、性能调优和硬件适配服务可形成可持续的技术服务商业模式
risk_matrix:
  regulatory: 项目涉及中美学术机构联合开发和Intel特定指令集优化，在AI芯片出口管制和中美技术脱钩背景下，后续国际协作和硬件兼容性可能面临合规不确定性
  technological: CPU-GPU异构计算方案在推理延迟上仍无法与纯GPU方案匹敌，且NVIDIA等厂商持续提升单卡显存容量（如B200的192GB），长期可能削弱异构方案的市场需求；依赖Intel
    AMX指令集的性能优势在非Intel硬件上难以复现
  competitive: vLLM、SGLang等主流推理框架持续优化MoE模型支持，NVIDIA Triton Inference Server也在推动GPU端原生MoE优化，KTransformers面临主流生态挤压和用户注意力分散的风险
  ethical: 通过降低超大规模模型本地部署门槛加速了AI能力的民主化，有利于缓解AI资源集中在少数巨头手中的问题，正面社会价值大于伦理风险
  additional:
  - 项目核心贡献高度依赖清华MADSys Lab学术团队和少数核心开发者，长期维护和社区治理的持续性存在不确定性
  - 项目快速迭代Day0支持各前沿模型，但若上游模型（如DeepSeek系列）发布节奏或架构发生重大变化，适配维护工作量将急剧增加
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: kvcache-ai/ktransformers
  canonical_name: kvcache-ai/ktransformers
  url: https://github.com/kvcache-ai/ktransformers
  positioning: KTransformers 是清华大学 MADSys Lab 主导的开源项目，通过 CPU-GPU 异构计算实现 MoE 大模型的高效推理与微调，论文被
    ACM SIGOPS SOSP 2025 收录。
  technical_signal: kt-kernel 推理引擎利用 Intel AMX/AVX512/AVX2 指令集优化 INT4/INT8 量化推理，支持
    NUMA 感知内存管理和 GPU 侧 GPTQ 量化。
  adoption_signal: 项目持续为 MiniMax-M3、GLM-5.2、DeepSeek-V4-Flash、Kimi-K2.5 等前沿 MoE 模型提供
    Day0 推理和微调支持，社区贡献活跃。
  ecosystem_relevance: kt-kernel 提供简洁 Python API 可集成到 SGLang 等生产推理框架，已扩展至 AMD ROCm、Intel
    Arc GPU 和 Ascend NPU 等多样化硬件后端。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: KTransformers 通过 CPU-GPU 异构计算大幅降低了 MoE 大模型的使用门槛，使 DeepSeek-V3/R1 等前沿模型可在消费级硬件上运行和微调，论文被
    SOSP 2025 收录证明了学术价值，持续提供 Day0 模型支持使其成为追踪 MoE 生态演进的关键节点。
  risk_notes:
  - CPU-GPU 异构推理的性能高度依赖 Intel AMX/AVX 指令集优化，在非 Intel 硬件上可能无法达到最佳加速效果。
  - 项目核心优化紧密绑定 MoE 模型架构，若 MoE 范式发生变革或新架构出现，现有优化策略可能需要大规模重构。
  - 作为开源研究项目，其长期维护节奏和社区贡献活跃度存在不确定性，且需持续跟进快速演进的模型生态。
  score: 8.0
  article_ids:
  - cdbcdde49a4f0343
  evidence_snippets:
  - KTransformers 是清华大学 MADSys Lab 主导的开源研究项目，专注于通过 CPU-GPU 异构计算实现大语言模型的高效推理与微调。
  - 项目提供 kt-kernel 推理引擎和 KTransformers × LLaMA-Factory 微调集成两条核心能力路径，已从原始集成框架迁移至 kt-kernel
    源码树组织。
  - KTransformers 的研究论文已被 ACM SIGOPS SOSP 2025 会议收录，论文作者来自清华大学 MADSys Lab、Approaching.AI
    和 9#AISoft。
---

KTransformers is a research project focused on efficient inference and fine-tuning of large language models through CPU-GPU heterogeneous computing. The project now exposes two user-facing capabilities from the kt-kernel source tree: Inference and SFT.

**June 21, 2026**: MiniMax-M3 Day0 Support! (Tutorial)**June 17, 2026**: GLM-5.2 Day0 Support! (Tutorial)**May 6, 2026**: KTransformers at GOSIM Paris 2026 — "Agentic AI on Edge" track. We'll present KT's inference performance on consumer hardware.**May 02, 2026**: DeepSeek-V4-Flash Support! (Tutorial)**Apr 30, 2026**: KTransformers v0.6.1 refreshes kt-kernel inference and SFT docs with separate Inference and SFT Quick Start entry points.**Mar 26, 2026**: Support AVX2-only CPU backend for KT-Kernel inference. (Tutorial)**Feb 13, 2026**: MiniMax-M2.5 Day0 Support! (Tutorial)**Feb 12, 2026**: GLM-5 Day0 Support! (Tutorial)**Jan 27, 2026**: Kimi-K2.5 Day0 Support! (Tutorial) (SFT Tutorial)**Jan 22, 2026**: Support CPU-GPU Expert Scheduling, Native BF16 and FP8 per channel Precision and AutoDL unified fine-tuning and inference**Dec 24, 2025**: Support Native MiniMax-M2.1 inference. (Tutorial)**Dec 22, 2025**: Support RL-DPO fine-tuning with LLaMA-Factory. (Tutorial)**Dec 5, 2025**: Support Native Kimi-K2-Thinking inference (Tutorial)**Nov 6, 2025**: Support Kimi-K2-Thinking inference (Tutorial) and fine-tune (Tutorial)**Nov 4, 2025**: KTransformers Fine-Tuning × LLaMA-Factory Integration. (Tutorial)**Oct 27, 2025**: Support Ascend NPU. (Tutorial)**Oct 10, 2025**: Integrating into SGLang. (Roadmap, Blog)**Sept 11, 2025**: Support Qwen3-Next. (Tutorial)**Sept 05, 2025**: Support Kimi-K2-0905. (Tutorial)**July 26, 2025**: Support SmallThinker and GLM4-MoE. (Tutorial)**July 11, 2025**: Support Kimi-K2. (Tutorial)**June 30, 2025**: Support 3-layer (GPU-CPU-Disk) prefix cache reuse.**May 14, 2025**: Support Intel Arc GPU (Tutorial).**Apr 29, 2025**: Support AMX-Int8、 AMX-BF16 and Qwen3MoE (Tutorial)**Apr 9, 2025**: Experimental support for LLaMA 4 models (Tutorial).**Apr 2, 2025**: Support Multi-concurrency. (Tutorial).**Mar 15, 2025**: Support ROCm on AMD GPU (Tutorial).**Mar 5, 2025**: Support unsloth 1.58/2.51 bits weights and IQ1_S/FP8 hybrid weights. Support 139K Longer Context for DeepSeek-V3 and R1 in 24GB VRAM.**Feb 25, 2025**: Support FP8 GPU kernel for DeepSeek-V3 and R1; Longer Context.**Feb 15, 2025**: Longer Context (from 4K to 8K for 24GB VRAM) & Slightly Faster Speed （+15%, up to 16 Tokens/s), update docs and online books.**Feb 10, 2025**: Support Deepseek-R1 and V3 on single (24GB VRAM)/multi gpu and 382G DRAM, up to 3~28x speedup. For detailed show case and reproduction tutorial, see here.**Aug 28, 2024**: Decrease DeepseekV2's required VRAM from 21G to 11G.**Aug 15, 2024**: Update detailed tutorial for injection and multi-GPU.**Aug 14, 2024**: Support llamfile as linear backend.**Aug 12, 2024**: Support multiple GPU; Support new model: mixtral 8*7B and 8*22B; Support q2k, q3k, q5k dequant on gpu.**Aug 9, 2024**: Support windows native.

CPU-optimized kernel operations for heterogeneous LLM inference.

**Key Features:**

**AMX/AVX Acceleration**: Intel AMX and AVX512/AVX2 optimized kernels for INT4/INT8 quantized inference**MoE Optimization**: Efficient Mixture-of-Experts inference with NUMA-aware memory management**Quantization Support**: CPU-side INT4/INT8 quantized weights, GPU-side GPTQ support**Easy Integration**: Clean Python API for SGLang and other frameworks

**Quick Start:**

```
cd kt-kernel
pip install .
```

**Use Cases:**

- CPU-GPU hybrid inference for large MoE models
- Integration with SGLang for production serving
- Heterogeneous expert placement (hot experts on GPU, cold experts on CPU)

**Performance Examples:**

| Model | Hardware Configuration | Total Throughput | Output Throughput |
|---|---|---|---|
| DeepSeek-R1-0528 (FP8) | 8×L20 GPU + Xeon Gold 6454S | 227.85 tokens/s | 87.58 tokens/s (8-way concurrency) |

KTransformers × LLaMA-Factory integration for ultra-large MoE model fine-tuning.

**Key Features:**

**Multi-Backend Support**: CPU/GPU hybrid fine-tuning with INT8/INT4 quantization**Ultra-Large MoE Support**: Fine-tune models like DeepSeek-V3/R1 on limited GPU memory**Faster than ZeRO-Offload**: 6-12x training speedup in benchmarked MoE SFT workloads**Lower CPU Memory**: About half the CPU memory of the previous KT SFT path in the benchmarked setup**LLaMA-Factory Integration**: Seamless integration with popular fine-tuning framework

| Model | GPU Memory | Training Speed | Hardware |
|---|---|---|---|
| DeepSeek-V3 | ~80GB total | 3.7 it/s | 4x RTX 4090 |
| DeepSeek-R1 | ~80GB total | 3.7 it/s | 4x RTX 4090 |
| Qwen3-30B-A3B | ~24GB total | 8+ it/s | 1x RTX 4090 |

**Quick Start:**

```
cd /path/to/LLaMA-Factory
pip install -e .
pip install -r requirements/ktransformers.txt
CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch \
--config_file examples/ktransformers/accelerate/fsdp2_kt_int8.yaml \
src/train.py \
examples/ktransformers/train_lora/qwen3_5moe_lora_sft_kt.yaml
```

👉 **Quick Start →**
👉 **Full Documentation →**

If you use KTransformers in your research, please cite our paper:

```
@inproceedings{10.1145/3731569.3764843,
title = {KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models},
author = {Chen, Hongtao and Xie, Weiyu and Zhang, Boxin and Tang, Jingqi and Wang, Jiahao and Dong, Jianwei and Chen, Shaoyuan and Yuan, Ziwei and Lin, Chen and Qiu, Chengyu and Zhu, Yuening and Ou, Qingliang and Liao, Jiaqi and Chen, Xianglin and Ai, Zhiyuan and Wu, Yongwei and Zhang, Mingxing},
booktitle = {Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles},
year = {2025}
}
```

Developed and maintained by:

- MADSys Lab @ Tsinghua University
- Approaching.AI
- 9#AISoft
- Community contributors

We welcome contributions! Please feel free to submit issues and pull requests.

**GitHub Issues**: Report bugs or request features**WeChat Group**: See archive/WeChatGroup.png

The original integrated KTransformers framework has been archived to the `archive/`

directory for reference. The project now organizes the two capabilities above from the kt-kernel source tree for clearer documentation and maintenance.

For the original documentation with full quick-start guides and examples, see:

- archive/README.md (English)
- archive/README_ZH.md (中文)