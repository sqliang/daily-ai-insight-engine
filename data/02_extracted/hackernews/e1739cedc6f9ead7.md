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