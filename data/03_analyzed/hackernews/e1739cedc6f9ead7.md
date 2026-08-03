---
title: 'Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model'
source: https://github.com/cactus-compute/needle
author:
- '[[HenryNdubuaku]]'
published: '2026-05-12'
created: '2026-05-13'
description: 'Hey HN, Henry here from Cactus. We open-sourced Needle, a 26M parameter
  function-calling (tool use) model. It runs at 6000 tok/s prefill and 1200 tok/s
  decode on consumer devices.We were always frustrated by the little effort made towards
  building agentic models that run on budget phones, so we conducted investigations
  that led to an observation: agentic experiences are built upon tool calling, and
  massive models are overkill for it. Tool calling is fundamentally retrieval-and-assembly
  (match query to tool name, extract argument values, emit JSON), not reasoning. Cross-attention
  is the right primitive for this, and FFN parameters are wasted at this scale.Simple
  Attention Networks: the entire model is just attention and gating, no MLPs anywhere.
  Needle is an experimental run for single-shot function calling for consumer devices
  (phones, watches, glasses...).Training: - Pretrained on 200B tokens across 16 TPU
  v6e (27 hours) - Post-trained on 2B tokens of synthesized function-calling data
  (45 minutes) - Dataset synthesized via Gemini with 15 tool categories (timers, messaging,
  navigation, smart home, etc.)You can test it right now and finetune on your Mac/PC:
  https://github.com/cactus-compute/needleThe full writeup on the architecture is
  here: https://github.com/cactus-compute/needle/blob/main/docs/simp...We found that
  the "no FFN" finding generalizes beyond function calling to any task where the model
  has access to external structured knowledge (RAG, tool use, retrieval-augmented
  generation). The model doesn''t need to memorize facts in FFN weights if the facts
  are provided in the input. Experimental results to published.While it beats FunctionGemma-270M,
  Qwen-0.6B, Granite-350M, LFM2.5-350M on single-shot function calling, those models
  have more scope/capacity and excel in conversational settings. We encourage you
  to test on your own tools via the playground and finetune accordingly.This is part
  of our broader work on Cactus (https://github.com/cactus-compute/cactus), an inference
  engine built from scratch for mobile, wearables and custom hardware. We wrote about
  Cactus here previously: https://news.ycombinator.com/item?id=44524544Everything
  is MIT licensed. Weights: https://huggingface.co/Cactus-Compute/needle GitHub: https://github.com/cactus-compute/needle
  Comments URL: https://news.ycombinator.com/item?id=48111896 Points: 515 # Comments:
  156'
tags:
- clippings
id: e1739cedc6f9ead7
source_type: community_discussion
tldr: Cactus Compute 将 Gemini 3.1 蒸馏为 26M 参数的简易注意力网络 Needle，权重、数据集和微调工具全部开源，支持本地 Mac/PC
  微调。
objective_summary: Cactus Compute 团队于 2026 年将 Gemini 3.1 蒸馏为一个仅 26M 参数的简易注意力网络（Simple
  Attention Network），命名为 Needle。该模型在 16 块 TPU v6e 上预训练 200B token（27 小时），后训练 2B token
  的函数调用数据（45 分钟），生产环境可达 6000 toks/sec 预填充和 1200 toks/sec 解码速度。权重与数据集已在 GitHub 开源，并提供命令行和
  Web UI 界面支持本地微调。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Cactus Compute
  technologies:
  - Simple Attention Network
  - GQA
  - RoPE
  - BPE
  key_people:
  - Henry Ndubuaku
  - Jakub Mroz
  - Karen Mosoyan
  - Roman Shemet
  - Parkirat Sandhu
  - Satyajit Kumar
  - Noah Cylich
  - Justin H. Lee
key_logic_flow:
- Cactus Compute 将 Gemini 3.1 蒸馏为仅 26M 参数的简易注意力网络 Needle，专为单次函数调用场景优化。
- Needle 在 16 块 TPU v6e 上预训练 200B token 耗时 27 小时，后训练 2B token 的函数调用数据耗时 45 分钟。
- 生产环境下 Needle 达到 6000 toks/sec 预填充和 1200 toks/sec 解码速度，可在本地 Mac/PC 微调。
- 在单次函数调用任务上，Needle 超越了 FunctionGemma-270M、Qwen-0.6B、Graninte-350M 和 LFM2.5-350M。
- Needle 提供 CLI 工具（needle finetune、needle run）和 Web UI 界面（http://127.0.0.1:7860）供用户测试与微调。
- 模型权重、数据集生成代码及全部训练脚本均已在 GitHub 上以 cactus-compute/needle 开源。
extract_result: success
object_mentions:
- object_type: project
  name: cactus-compute/needle
  canonical_name: cactus-compute/needle
  url: https://github.com/cactus-compute/needle
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Cactus Compute 将 Gemini 3.1 蒸馏为 26M 参数的简易注意力网络 Needle，权重和数据集已完全开源。
  - Needle 提供 needle finetune、needle run 等 CLI 命令，以及 playground Web UI 供用户测试和微调。
  - 在生产环境中 Needle 运行于 Cactus 平台，达到 6000 toks/sec 预填充和 1200 toks/sec 解码速度。
  article_id: e1739cedc6f9ead7
- object_type: model
  name: Gemini 3.1
  canonical_name: Gemini 3.1
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - Needle 是从 Gemini 3.1 蒸馏而来，后训练阶段使用 Gemini 生成单次函数调用数据集。
  - 在 Needle 的训练流程中，Gemini 3.1 被用作教师模型来合成训练数据。
  article_id: e1739cedc6f9ead7
- object_type: project
  name: Simple Attention Network
  canonical_name: Simple Attention Network
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Needle 基于 Simple Attention Network 架构构建，该架构专为消费级设备（手机、手表、眼镜）重新定义小型 AI。
  - 模型配置为 d=512, 8 头注意力/4 KV 头, BPE 词表大小 8192，编码器 12 层、解码器 8 层，无 FFN。
  article_id: e1739cedc6f9ead7
pipeline_stage: fact_extracted
impact_score:
  score: 5.5
  reason: 该工作将 Gemini 3.1 的工具调用能力蒸馏为仅 26M 参数的微型模型，且在单次函数调用任务上超越 FunctionGemma-270m、Qwen-0.6B
    等数倍至数十倍参数量的模型，具有明确的工程价值。但其应用范围高度聚焦于单一任务（single-shot function calling），作者也明确承认通用对话能力不及对比模型，且团队规模较小、项目定位为实验性探索。综合来看，这对端侧
    AI 工具调用细分赛道有局部竞争格局影响，但远未达到行业范式转移级别，故评 5.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 26M 参数模型在工具调用任务上超越数百M参数模型，且完全开源可本地微调
hype_assessment:
  level: medium
  reason: 文章整体技术数据详实（架构图、训练时长、token 数、推理速度均有具体数字），但存在一定包装成分：如 'redefining tiny AI
    for consumer devices' 这类宏大叙事与其单一任务定位之间存在落差；与更大模型的性能对比仅限于 single-shot function
    calling 这一狭窄场景，未展示通用能力对比，存在选择性展示的嫌疑。整体属于有干货但适度包装的水平。
information_entropy: high
domain_disruption:
  technical_innovation: 采用 Simple Attention Network 架构（8层 Decoder + 12层 Encoder，GQA+RoPE
    注意力，无 FFN 的纯注意力 Encoder），从 Gemini 3.1 蒸馏出单一工具调用能力，证明了大规模模型特定能力可被高度压缩至端侧可运行的微型模型中。架构上
    Encoder 不使用前馈网络（FFN）、Decoder 与 Encoder 通过 Cross Attention 连接的设计较为精简独特。
  business_model: 若该蒸馏范式成熟，端侧设备（手机、手表、眼镜）可在无云端依赖的情况下完成高质量工具调用，可能削弱当前以 API 调用为核心计费模式的
    AI Agent 商业闭环，推动 Agent 推理从云端向端侧迁移。但目前仅为实验阶段，商业影响尚需验证。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 正向逻辑：26M参数在单次函数调用任务上击败270M-600M的竞品，性能密度极高；6000 toks/s的prefill速度使其在手机、手表、眼镜等边缘设备上的部署可行性大幅提升，契合on-device
    AI的长期趋势。负向逻辑：(1) 蒸馏策略本质是跟随者模式——高度依赖Gemini作为教师模型，若Gemini的tool calling出现代际升级或被其他模型超越，Needle的竞争壁垒将迅速瓦解；(2)
    仅聚焦single-shot function calling，TAM受限，大概率被多用途小型模型（如Apple Intelligence或Google的端侧模型）吸收为子功能；(3)
    完全开源意味着零直接变现路径，Cactus Compute的收益更可能是品牌认知度提升而非持续现金流。3-5年维度看，这个特定模型大概率被替代，但'蒸馏专用微型模型+Simple
    Attention Network架构'这一范式可能沉淀为边缘AI的参考模式，因此给予5.5分——技术上有亮点但投资回报的长期复利效应存疑。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Cactus Compute
- Google DeepMind
- 边缘AI硬件厂商（如Qualcomm、MediaTek、AR眼镜厂商）
- 开源AI工具链生态（HuggingFace、Ollama等）
competitive_casualty:
- Apple（其Apple Intelligence的端侧tool calling需面对开源替代方案的压力）
- 其他小型专用模型团队（FunctionGemma、Granite等被直接对标超越）
- 纯云端tool calling API提供商（on-device方案侵蚀其低延迟场景市场）
market_opportunities:
- 智能硬件厂商可将Needle集成至智能手表、AR眼镜等端侧设备，实现离线工具调用（如语音控制家居、查询天气），无需依赖云端大模型API，显著降低延迟与隐私风险。
- 开发者可基于Needle的开源权重和微调工具链，针对特定垂直领域（如金融数据查询、医疗术语映射、企业内部API调度）打造定制化的轻量级Agent工具调用层，形成差异化SaaS产品。
- AI从业者可将蒸馏流水线方法论（Gemini → 26M小模型、200B预训练+2B后训练）作为参考范式，探索将前沿大模型能力压缩至端侧部署的技术路线，该方向有望成为2026-2027年AI工程化的核心技能。
risk_matrix:
  regulatory: 利用Gemini 3.1输出进行模型蒸馏可能触及Google的API服务条款中关于竞品模型训练的限制条款，若Google收紧蒸馏政策，Needle的数据合成管线将面临合规风险。此外，端侧工具调用能力若被用于绕过App
    Store审核机制，可能引发平台监管介入。
  technological: Needle仅针对单次函数调用优化，缺乏多轮对话与上下文理解能力，在实际复杂Agent场景中的泛化性存疑。Simple Attention
    Network架构（无FFN的Encoder设计）尚未经过学术社区广泛验证，存在被更成熟的MoE或SSM小模型方案替代的风险。
  competitive: Google Gemini Nano、Apple Intelligence等端侧AI已深度集成至操作系统层，具备生态锁定优势。若Google将工具调用蒸馏为Gemini
    Nano的默认能力，Needle的开源优势将大幅削弱。此外，HuggingFace上的smol系列等竞品也在快速迭代。
  ethical: 26M参数模型在蒸馏过程中可能继承Gemini的偏见模式，且由于体积过小，缺乏安全对齐冗余。端侧工具调用若无权限管控，可能被滥用于自动化执行敏感操作（如批量发送消息、自动下单），形成新型自动化滥用载体。
  additional:
  - 训练数据依赖Gemini API合成，若Gemini后续版本改变工具调用格式或弃用相关API，数据管线需重新适配，维护成本高
  - 16块TPU v6e的预训练门槛限制了社区复现能力，开源不等于可复现，可能导致生态发展依赖单一团队
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: cactus-compute/needle
  canonical_name: cactus-compute/needle
  url: https://github.com/cactus-compute/needle
  positioning: Needle 是一个从 Gemini 3.1 蒸馏至仅 26M 参数的简易注意力网络，专注于消费级设备上的单次函数调用场景，模型与数据完全开源。
  technical_signal: 基于 12 层编码器和 8 层解码器的简易注意力架构（无 FFN），在 16 块 TPU v6e 上预训练 200B token
    共 27 小时，后训练 2B token 函数调用数据仅需 45 分钟。
  adoption_signal: 模型在 GitHub 完全开源，提供 CLI 和 Web UI 两种交互方式，用户可在本地 Mac 或 PC 上使用自有数据一键微调，降低使用门槛。
  ecosystem_relevance: 面向手机、手表和眼镜等消费级设备的个人 AI 助手场景，填补了超小参数模型在函数调用领域的空白，为边缘 AI 代理提供了新的技术路径。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Needle 以仅 26M 参数在单次函数调用上超越 270M-350M 量级的更大模型，证明蒸馏极小型模型在特定工具调用场景的可行性，其完全开源和极高推理速度使其成为边缘设备
    AI 代理值得持续关注的方案。
  risk_notes:
  - Needle 目前处于实验阶段，生产环境稳定性有待更广泛场景部署验证，且小模型在推理中可能存在输出不稳定的问题。
  - Needle 专为单次函数调用优化，在多轮对话和通用语言理解场景的能力远不及同规模的通用小语言模型。
  score: 7.0
  article_ids:
  - e1739cedc6f9ead7
  evidence_snippets:
  - Cactus Compute 团队从 Gemini 3.1 蒸馏出仅 26M 参数的简易注意力网络 Needle，完全开源了模型权重、数据集生成代码和全部训练脚本，支持用户在本地
    Mac 或 PC 上微调。
  - Needle 提供 needle finetune 和 needle run 等 CLI 命令行工具以及基于 Web 的 playground 图形界面，用户可在浏览器中一键测试模型或使用自有工具数据进行本地微调。
  - Needle 在生产环境运行于 Cactus 平台，达到 6000 toks/sec 预填充速度和 1200 toks/sec 解码速度，在单次函数调用任务上超越
    FunctionGemma-270M 和 Qwen-0.6B 等参数更大的模型。
---

We distilled Gemini 3.1 into a 26m parameter "Simple Attention Network" that you can even finetune locally on your Mac/PC. In production, Needle runs on Cactus at 6000 toks/sec prefill and 1200 decode speed. Weights are fully open on Cactus-Compute/needle, as well as the dataset generation.

```
d=512, 8H/4KV, BPE=8192
┌──────────────┐
│ Tool Call │
└──────┬───────┘
┌┴──────────┐
│ Softmax │
└─────┬─────┘
┌─────┴─────┐
│ Linear (T)│ ← tied
└─────┬─────┘
┌─────┴─────┐
│ ZCRMSNorm │
└─────┬─────┘
┌────────┴────────┐
│ Decoder x 8 │
│┌───────────────┐│
││ ZCRMSNorm ││
││ Masked Self ││
││ Attn + RoPE ││
││ Gated Residual││
│├───────────────┤│
┌──────────────┐ ││ ZCRMSNorm ││
│ Encoder x 12 │──────────────────────▶Cross Attn ││
│ │ ││ Gated Residual││
│ ┌──────────┐ │ │└───────────────┘│
│ │ZCRMSNorm │ │ └────────┬────────┘
│ │Self Attn │ │ ┌─────┴─────┐
│ │ GQA+RoPE │ │ │ Embedding │ ← shared
│ │Gated Res │ │ └─────┬─────┘
│ │ │ │ ┌───────┴───────-┐
│ │ (no FFN) │ │ │[EOS]<tool_call>│
│ └──────────┘ │ │ + answer │
│ │ └───────────────-┘
└──────┬───────┘
│
┌────┴──────┐
│ Embedding │
└────┬──────┘
│
┌────┴──────┐
│ Text │
│ query │
└───────────┘
```


- Pretrained on 16 TPU v6e for 200B tokens (27hrs).
- Post-trained on 2B tokens of single-shot function call dataset (45mins).

Needle is an experimental run for Simple Attention Networks, geared at redefining tiny AI for consumer devies (phones, watches, glasses...). So while it beats FunctionGemma-270m, Qwen-0.6B, Graninte-350m, LFM2.5-350m on single-shot function call for personal AI, Those model are have more scope/capacity and excel in conversational settings. Also, small models can be finicky. Please use the UI in the next section to test on your own tools, and finetune accordingly, at the click of a button.

```
git clone https://github.com/cactus-compute/needle.git
cd needle && source ./setup
needle playground
```

Opens a web UI at http://127.0.0.1:7860 where you can test and finetune on your own tools. Weights are auto-downloaded.

```
from needle import SimpleAttentionNetwork, load_checkpoint, generate, get_tokenizer
params, config = load_checkpoint("checkpoints/needle.pkl")
model = SimpleAttentionNetwork(config)
tokenizer = get_tokenizer()
result = generate(
model, params, tokenizer,
query="What's the weather in San Francisco?",
tools='[{"name":"get_weather","parameters":{"location":"string"}}]',
stream=False,
)
print(result)
# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]
```

```
# Playground (generates data via Gemini, trains, evaluates, bundles result)
needle playground
# CLI (auto-downloads weights if not local)
needle finetune data.jsonl
```

```
needle playground Test and finetune via web UI
needle finetune <data.jsonl> Finetune on your own data
needle run --query "..." --tools Single inference
needle train Full training run
needle pretrain Pretrain on PleIAs/SYNTH
needle eval --checkpoint <path> Evaluate a checkpoint
needle tokenize Tokenize dataset
needle generate-data Synthesize training data via Gemini
needle tpu <action> TPU management (see docs/tpu.md)
```


```
@misc{ndubuaku2026needle,
title={Needle},
author={Henry Ndubuaku, Jakub Mroz, Karen Mosoyan, Roman Shemet, Parkirat Sandhu, Satyajit Kumar, Noah Cylich, Justin H. Lee},
year={2026},
url={https://github.com/cactus-compute/needle}
}
```