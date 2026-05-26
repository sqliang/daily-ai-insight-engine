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