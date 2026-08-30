---
title: cactus-compute/needle
source: https://github.com/cactus-compute/needle
author: []
published: ''
created: '2026-08-13'
manifest_dates:
- '2026-08-13'
- '2026-08-14'
- '2026-08-15'
- '2026-08-16'
- '2026-08-17'
description: '14MB foundation model for tiny devices; phones, wearables, smart home,
  and robots. Needle 2 Needle 2 is an open 45M-parameter model for tool calling, device
  use and structured extraction. The whole model is a single 14MB binary that runs
  a full session in about 28MB of RAM. It is built on our Simple Attention Network
  findings, compressed to CQ2-bit with Cactus Quants, and baked into its own engine.
  On the benchmarks below, Needle 2 trades wins with other small models like FunctionGemma
  270M, LFM2.5 230M and Apple FM, at 5x to 70x smaller, and 2 bits against their f16.
  This repository is the Python package: inference, LoRA fine-tuning, and export.
  pip install cactus-needle, describe your tools, and call them from Python. The inference
  engine is fetched once from Hugging Face and cached; there is nothing else to build.
  Self-contained: weights baked into a single 14MB engine; no separate model files
  to manage, and inference does no network. Simple contract: tool calls come back
  as structured data, text in, JSON out; a byte-level grammar compiled from your schemas
  constrains every token. Confidence-gated: every response carries a calibrated confidence
  score from a learned head; set a threshold, act above it, escalate below it. Tool
  retrieval: declare a large catalogue and a built-in retrieval head renders only
  the top five tools per turn, with the grammar constrained to that subset. Bounded
  memory: a 256-token sliding window with the tools pinned as KV sinks, so total memory
  stays near 28MB no matter how long the conversation runs. Weights: huggingface.co/Cactus-Compute/needle2
  · source: github.com/cactus-compute/needle. Simple Attention Network Needle 2 is
  a Simple Attention Network, our dense small-model recipe: a Hadamard MLP in place
  of the FFN, GQA attention, engram key-value memory, and multi-lane hyper-connections.
  See the paper for the design and ablations: arXiv:2607.18363. Each block carries
  its update rule. Here x̂ is the RMS-normalised flattening of the four residual streams,
  H the orthonormal Walsh-Hadamard transform (a fixed matrix, applied in n log n time
  with no weights to read), (kₜ, vₜ) rows gathered from hashed n-gram tables, and
  P the doubly-stochastic normalisation of the routing logits A, computed by Sinkhorn
  iteration; a, b, g and all σ-gates are learned and input-dependent. Both attention
  and MLP residuals are sandwich-normed and gated, the engram sites fire at two layers,
  and decoding is constrained by a byte-level grammar compiled from the declared schemas.
  Quickstart pip install cactus-needle Needle reads your tool descriptions to decide
  what to call and how to fill arguments, so describing them well is the whole game.
  You can do it three ways, from least to most control. Simple: decorate a function.
  The signature gives the argument types, the docstring is the tool description, and
  run() completes the loop: model picks the call, Needle executes your function, feeds
  the result back, and returns the final response with the executed tool results attached
  as results. import needle @needle.tool def get_weather(city: str): "Get the current
  weather for a city." return {"city": city, "temp_c": 27, "sky": "clear"} agent =
  needle.Needle(tools=[get_weather]) print(agent.run("what''s it like in Lagos right
  now?")["results"]) # [{''city'': ''Lagos'', ''temp_c'': 27, ''sky'': ''clear''}]
  Medium: describe each argument and offer choices. Needle reads a Google-style Args:
  block for per-parameter descriptions; a default makes an argument optional; a Literal
  becomes a fixed set the model must choose from (it cannot emit anything else). from
  typing import Literal @needle.tool def set_thermostat(temperature: int, mode: Literal["heat",
  "cool", "auto"] = "auto"): """Set the thermostat. Args: temperature: target temperature
  in Celsius mode: heating strategy to use """ return {"temperature": temperature,
  "mode": mode} agent = needle.Needle(tools=[set_thermostat]) agent.run("make it 21
  and cool the room") Advanced: constrain the values with needle.Field, attached inline
  via Annotated. Ranges, patterns, lengths, and item counts are compiled into the
  decode grammar, so the model can only ever emit values that satisfy them. from typing
  import Annotated @needle.tool def send_money( amount: Annotated[float, needle.Field(gt=0,
  le=10000, description="USD, up to 10,000")], to: Annotated[str, needle.Field(pattern=r"^@[a-z0-9_]+$",
  description="recipient handle")], memo: Annotated[str, needle.Field(max_length=80)]
  = "", ): "Send money to a handle." return {"sent": amount, "to": to} Field supports
  description, enum, const, ge/le/gt/lt, multiple_of, min_length/max_length, pattern,
  format, min_items/max_items, and unique_items. Extraction: to pull structured data
  out of text, declare the shape and call extract(). Pass a Pydantic model and you
  get a typed object back. from pydantic import BaseModel class Invoice(BaseModel):
  vendor: str total: float due_date: str invoice = needle.extract("Invoice from Acme
  Corp, $1,200.00, due 2026-09-01", Invoice) print(invoice.vendor, invoice.total)
  # -> Acme Corp 1200.0 By hand - the decorator just builds a JSON schema; you can
  pass that schema directly, which is exactly what Needle consumes. This is how you
  set descriptions and constraints without the decorator: tools = [{ "name": "set_lights",
  "description": "Turn a room''s lights on or off and set brightness", "parameters":
  { "type": "object", "properties": { "room": {"type": "string", "description": "which
  room to control"}, "on": {"type": "boolean"}, "brightness": {"type": "integer",
  "minimum": 0, "maximum": 100}, }, "required": ["room", "on"], }, }] agent = needle.Needle(tools=tools)
  Prefer to drive the loop yourself instead of run()? complete() returns the raw call
  and you execute it: import json response = agent.complete("dim the living room to
  30") if response["type"] == "call": result = set_lights(**response["function_calls"][0]["arguments"])
  response = agent.complete(json.dumps(result)) # feed the result back With a large
  catalogue, persist tool embeddings across runs with needle.Needle(tools=..., tool_index_path="tools.idx").
  Every turn returns one JSON object: { "type": "call", "success": true, "error":
  null, "error_code": null, "function_calls": [ { "name": "set_lights", "arguments":
  { "room": "living room", "on": true, "brightness": 30 } } ], "reasoning": "''living
  room'' -> room; ''dim'' -> on true, brightness 30", "confidence": 0.94, "prefill_tps":
  4300.0, "decode_tps": 850.0 } Playground Try any model in the browser: pick a preset,
  edit the tools or prompt, and Run. Follow-up queries continue the same conversation.
  needle playground # base model, http://127.0.0.1:7860 needle playground --weights
  my.cact # a tuned model The server downloads and initializes the model before serving,
  so the first query is instant. The Finetune on these tools button runs the fine-tuning
  pipeline below from the UI and hands back a downloadable .cact. Behaviour Needle
  solves every problem as a function call. The context declares what may be called;
  the model answers with calls. Performing an action and extracting structured data
  are the same operation, the only difference is what you declare. A request no declared
  tool can serve is refused with the empty call []. That is the whole contract for
  off-topic input; there is no free-text fallback. Arguments contain only values evidenced
  by the input. An optional field with no evidence is omitted, not guessed; omission
  is the field-level []. reasoning is the model''s short derivation of each argument
  from its source span (''ten minutes'' -> minutes 10). It is generated unconstrained;
  only the call itself is grammar-constrained, so the JSON cannot be malformed while
  the derivation stays legible. After you execute a call, pass the result back as
  the next complete(). The model continues from it, and later arguments may depend
  on earlier results: search_for_contact first, then send_instant_message with the
  returned contact_id. A final "type": "respond" with empty function_calls signals
  the loop is done; the answer is the tool results themselves, which run() collects
  on the final response as results. No free text is generated. A session shares one
  toolset. Later turns are bare queries against the same tools; reset() rewinds the
  conversation and keeps the tools loaded. Extraction Extraction is not a separate
  mode - it is tool calling with one tool. Declare the record as the only schema and
  pass the content where the query goes; the returned call''s arguments are the extracted
  fields. With one declared tool the grammar admits exactly one call of that name,
  so schema conformance is guaranteed rather than requested. Use the extract() helper
  for a typed result (shown in Quickstart), or pass a plain schema and read the call:
  receipt = [{ "name": "receipt", "description": "A purchase receipt shared as text",
  "parameters": { "type": "object", "properties": { "merchant": {"type": "string"},
  "total": {"type": "number"}, "currency": {"type": "string"}, "line_items": {"type":
  "array", "items": {"type": "object"}}, }, "required": ["merchant", "total"], },
  }] agent = needle.Needle(tools=receipt) print(agent.complete("GreenMart receipt:
  oat milk 3.50, total 7.75 paid by visa")["function_calls"]) # -> [{"name": "receipt",
  "arguments": {"merchant": "GreenMart", "total": 7.75}}] Because it is the same operation,
  everything else applies unchanged: confidence gates the extraction, unsupported
  input returns the empty call [], and fine-tuning uses the same data format (the
  record as the tool, the passage as the query). System facts An optional system turn
  carries environment state as facts, never instructions: agent = needle.Needle(tools=tools,
  system="date: 2026-07-21 Tue 14:30; locale: en-US; device: phone; battery: 62%")
  Recognized keys are date, locale, device, battery, network, location, user, and
  assistant. The model resolves relative language against them: "tomorrow at 7" becomes
  an absolute time only when a date: fact licenses it, otherwise the human phrase
  passes through verbatim. assistant: declares the identity the model binds to. Needle
  trains with and without the turn, so omitting it is safe; instructions placed there
  do not steer the model. Tool retrieval Five or fewer declared tools render directly.
  Above that, retrieval engages: at init every tool schema is embedded once by a built-in
  contrastive head, each turn embeds the query, and only the five highest-scoring
  tools enter the context, with the grammar rebuilt over just that subset. An unselected
  tool is unreachable, not merely unlikely. tool_index_path persists the embeddings
  on disk, keyed by a fingerprint over the schemas and the model; a matching fingerprint
  loads instantly, a changed schema re-embeds only what changed. Confidence The confidence
  field is the minimum of two signals: a calibrated post-hoc head that scores the
  full prompt plus the call the model just produced, and the decoding probability
  of the call tokens. A call is accepted only when both agree, so the failure mode
  is escalation, not wrong execution. The contract: pick a threshold for your product,
  act at or above it, re-ask or route to a bigger model below it. Off-topic requests
  return the empty call []. Fine-tuning Needle fine-tunes with LoRA on the frozen
  base and merges the adapter at export, so a run is cheap and the tuned model is
  still a single .cact that runs on the same engine. The workflow is: (optionally)
  synthesize data, LoRA fine-tune, then build a tuned .cact. Data format. A JSONL
  file, one example per line. reasoning is optional; an off-topic example has answers:
  []. {"query": "dim the kitchen to 10", "tools": [{"name": "set_lights", "parameters":
  {"type": "object", "properties": {"room": {"type": "string"}, "brightness": {"type":
  "integer"}}, "required": ["room"]}}], "answers": [{"name": "set_lights", "arguments":
  {"room": "kitchen", "brightness": 10}}], "reasoning": "''kitchen'' -> room; ''dim
  to 10'' -> brightness 10"} 1. Synthesize data (optional). Needs OPENROUTER_API_KEY.
  Seed from a tool schema file, or expand an existing set: export OPENROUTER_API_KEY=sk-or-...
  needle generate-data --tools my_tools.json --num-samples 500 --output data.jsonl
  needle generate-data --augment data.jsonl --num-samples 500 # expand an existing
  JSONL 2. LoRA fine-tune. The base checkpoint auto-downloads from Hugging Face if
  you do not pass --checkpoint. --generate N first synthesizes N more examples from
  the tools in your data (also needs OPENROUTER_API_KEY). needle finetune data.jsonl
  --epochs 3 needle finetune data.jsonl --epochs 3 --generate 300 --lora-rank 16 --lora-alpha
  32 Key options: --lora-rank (default 16), --lora-alpha (32), --lr (1e-4), --batch-size
  (16), --max-len (1024), --checkpoint <base.pkl>, --out <adapter.pkl>. The adapter
  is written to checkpoints/needle_lora.pkl. 3. Build a tuned .cact. Merge the adapter
  into the base and quantize. The base auto-downloads if absent. needle build checkpoints/needle2.pkl
  --lora checkpoints/needle_lora.pkl --out my_needle.cact Add --bits 2 (default 4)
  for a smaller model, or set NEEDLE_HF_REPO=<you>/<model> and pass --upload to publish
  the .cact. 4. Run it. The engine is weights-agnostic, so a tuned .cact runs on it
  directly - no recompilation: import needle agent = needle.Needle(weights="my_needle.cact",
  tools=[...]) agent.run("...") Citation Needle 2 is built by the Cactus Compute team.
  If you use it in your work, please cite: @misc{needle2_2026, title = {Needle 2:
  A 45M-Parameter Foundation Tool-Calling Model for Tiny Devices}, author = {Ndubuaku,
  Henry and Mosoyan, Karen and Mroz, Jakub and Cylich, Noah and Kumar, Satyajit and
  Sandhu, Parkirat and Shemet, Roman and Lee, Justin H.}, year = {2026}, organization
  = {Cactus Compute, Inc.}, howpublished = {\url{https://github.com/cactus-compute/needle}}
  } Reach out on founders@cactuscompute.com for partnerships, collaborations, synergies
  and deploying Needle2 in your product.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e1739cedc6f9ead7
source_type: community_discussion
tldr: Needle 2 是 Cactus Compute 开源的 4500 万参数工具调用模型，单个 14MB 二进制文件可在约 28MB RAM 中运行，支持从
  Python 函数或 Pydantic 模型直接生成受约束的 JSON 工具调用与结构化抽取。
objective_summary: Cactus Compute 在 GitHub 上发布了 Needle 2，一个基于 Simple Attention Network
  的 45M 参数工具调用与结构化抽取模型。该模型使用 Cactus Quants 量化为 CQ2-bit，整个推理引擎与权重打包为单个 14MB 二进制，典型会话内存占用约
  28MB。它通过 Python 包 cactus-needle 提供，支持用装饰器、JSON Schema 或 Pydantic 模型声明工具，并以内置的字节级语法、置信度打分、工具检索头和
  256-token 滑动窗口 KV sink 来保证输出合法、可控且低内存。论文为 arXiv:2607.18363，权重托管于 HuggingFace 的 Cactus-Compute/needle2。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Cactus Compute
  technologies:
  - Needle 2
  - Simple Attention Network
  - GQA
  - LoRA
  - CQ2-bit
  - Cactus Quants
  - Walsh-Hadamard transform
  - Sinkhorn iteration
  - Pydantic
  key_people: []
key_logic_flow:
- Cactus Compute 发布并开源了 Needle 2，定位为小型工具调用、设备控制与结构化抽取模型。
- Needle 2 基于 Simple Attention Network，采用 Hadamard MLP、GQA 注意力、engram KV 记忆与多通道超连接，并用
  CQ2-bit 量化将全模型压入 14MB。
- Python 包 cactus-needle 提供装饰器与 Schema 驱动接口，输入文本后模型输出受语法约束的 JSON 工具调用。
- 内置置信度头对每次调用打分，并支持工具检索头从大量工具中只选择前 5 个进入当前轮次上下文。
- 通过 256-token 滑动窗口将工具作为 KV sink 固定，可在约 28MB RAM 内维持长会话。
- 支持 LoRA 微调并导出为单个 .cact 文件，同时提供 needle playground 浏览器界面用于快速试验。
object_mentions:
- object_type: project
  name: cactus-compute/needle
  canonical_name: cactus-compute/needle
  url: https://github.com/cactus-compute/needle
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该 GitHub 仓库对应 Python 包 cactus-needle，提供推理、LoRA 微调和导出功能，安装命令为 pip install cactus-needle。
  - 开发者可用 @needle.tool 装饰器自动从函数签名与文档字符串生成 JSON Schema，并通过 agent.run() 完成调用—执行—返回的闭环。
  - 包内同时提供 needle.extract 与 complete() 接口，分别用于 Pydantic 模型驱动的结构化抽取和手动控制工具调用循环。
  article_id: e1739cedc6f9ead7
- object_type: model
  name: Needle 2
  canonical_name: Needle 2
  url: https://huggingface.co/Cactus-Compute/needle2
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Needle 2 是 Cactus Compute 发布的 45M 参数开源模型，面向工具调用、设备使用与结构化抽取任务。
  - 模型基于 Simple Attention Network，经 Cactus Quants 量化为 CQ2-bit，整个引擎与权重打包为一个 14MB 二进制文件。
  - 在公开基准上，Needle 2 与 FunctionGemma 270M、LFM2.5 230M 和 Apple FM 互有胜负，但体积仅为这些 f16 模型的
    5 到 70 分之一。
  article_id: e1739cedc6f9ead7
- object_type: product
  name: needle playground
  canonical_name: needle playground
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 命令行工具 needle playground 可在浏览器中启动交互式界面，默认监听 127.0.0.1:7860，支持选择预设并编辑工具或提示词。
  - 浏览器界面提供 Finetune on these tools 按钮，能直接触发 LoRA 微调流程并生成可下载的 .cact 模型文件。
  article_id: e1739cedc6f9ead7
extract_result: success
impact_score:
  score: 6.8
  reason: Needle 2 把 45M 参数的工具调用与结构化抽取模型压缩到单个 14MB 二进制、约 28MB RAM 运行，直接冲击端侧/边缘 AI
    Agent 的落地门槛；它在极小体积内提供受约束 JSON 输出、工具检索头和 LoRA 微调，属于重要的产品/工程发布。但尚未达到 ChatGPT/Transformer
    级别的范式转移，主要改变的是小模型工具调用与边缘部署的局部竞争格局，因此评 6.8 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 45M 小模型在 28MB 内存内能否稳定完成工具调用与结构化抽取，以及实际精度与延迟表现
hype_assessment:
  level: medium
  reason: 原文使用了 'trades wins'、'5x to 70x smaller'、'whole model is a single 14MB binary'
    等 PR 化表述，具有一定包装色彩；但同时提供了具体参数量、量化位数、内存占用、Python 接口、论文 arXiv 编号和 HuggingFace 权重，属于可验证的工程发布，炒作程度中等，不算严重概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 基于 Simple Attention Network（Hadamard MLP、GQA、engram KV、多通道超连接）与
    CQ2-bit 量化，将完整推理引擎与权重打包为 14MB 单文件；通过字节级语法约束、置信度头、工具检索头和 256-token KV sink 实现低内存、可控的
    JSON 工具调用与结构化抽取。
  business_model: 以开源模型 + pip 包 + playground 的方式切入边缘/设备端 Agent 市场，可能替代部分依赖云端 API 的工具调用与结构化抽取场景；潜在商业化路径包括企业级微调服务、设备厂商授权、边缘推理优化工具及托管
    API。
engineering_complexity: production_ready
market_opportunities:
- 创业者可围绕 Needle 2 等超小模型开发端侧 AI Agent 运行方案，面向智能家居、工业控制器、可穿戴设备等低内存场景提供本地化工具调用与结构化抽取能力
- 可基于 Needle 2 的 LoRA 微调与 .cact 单文件导出能力，为垂直行业（如金融合规、医疗表单、物联网控制）提供领域特定的工具调用模型微调与部署服务
- 建议关注置信度门控与字节级语法约束结合的安全产品机会，为自动化工具调用场景提供可解释的风险控制与人工升级机制
risk_matrix:
  regulatory: 无显著监管风险；模型开源且参数量小，暂不受出口管制关注，但若用于金融转账、设备控制等关键场景，需关注行业-specific 合规要求
  technological: 存在替代风险；Simple Attention Network 与 CQ2-bit 量化方案仍需社区验证，且 45M 参数模型在复杂多步推理、长上下文工具链上的能力可能弱于更大模型，存在被
    FunctionGemma、LFM 等同类小模型或新一代端侧模型超越的风险
  competitive: 小模型工具调用赛道竞争激烈，FunctionGemma 270M、LFM2.5 230M、Apple FM 以及各大厂商的端侧模型均可能快速跟进，Cactus
    Compute 作为初创公司面临生态与品牌壁垒
  ethical: 工具调用模型若部署在智能家居、支付、工业控制等场景，置信度阈值设置不当可能导致误操作；此外端侧结构化抽取若处理敏感个人信息，存在隐私泄露与滥用风险
  additional:
  - 2-bit 极端量化可能带来精度损失和输出不稳定风险
  - 项目生态与社区成熟度尚处早期，长期维护和工具链完善度存在不确定性
  - 依赖 HuggingFace 分发引擎与权重，存在供应链与可用性风险
confidence:
  impact: medium
  compound: low
  hype: medium
actionable_insight: monitor
object_insights:
- object_type: project
  name: cactus-compute/needle
  canonical_name: cactus-compute/needle
  url: https://github.com/cactus-compute/needle
  positioning: Needle 2 是 Cactus Compute 开源的 45M 参数工具调用与结构化抽取小模型，以单 14MB 二进制实现端侧低内存运行。
  technical_signal: 基于 Simple Attention Network，采用 Hadamard MLP、GQA 注意力、engram KV
    记忆与 CQ2-bit 量化，全模型压入 14MB 并可在约 28MB RAM 中推理。
  adoption_signal: 通过 pip install cactus-needle 直接安装，提供装饰器、JSON Schema、Pydantic 三种工具声明方式，并支持
    LoRA 微调与浏览器 Playground。
  ecosystem_relevance: 面向工具调用、设备控制与结构化抽取场景，与 FunctionGemma 270M 等小模型竞争，权重托管于 HuggingFace，提供本地推理引擎。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该项目将 45M 参数工具调用模型压缩到 14MB 单文件，在端侧和物联网设备上具备极低部署门槛，若 benchmark 表现持续稳定，可能成为小型
    Agent 和设备控制的新基座。
  risk_notes:
  - 模型规模仅 45M，复杂多步推理与长上下文能力仍需验证。
  - CQ2-bit 极端量化可能带来精度损失，需关注实际任务置信度。
  - 生态尚处早期，工具市场和社区贡献度有限。
  score: 8.0
  article_ids:
  - e1739cedc6f9ead7
  evidence_snippets:
  - 该 GitHub 仓库对应 Python 包 cactus-needle，提供推理、LoRA 微调和导出功能，安装命令为 pip install cactus-needle。
  - 开发者可用 @needle.tool 装饰器自动从函数签名与文档字符串生成 JSON Schema，并通过 agent.run() 完成调用—执行—返回的闭环。
  - 包内同时提供 needle.extract 与 complete() 接口，分别用于 Pydantic 模型驱动的结构化抽取和手动控制工具调用循环。
compound_value:
  score: 6.5
  reason: Needle 2 切中的是端侧/边缘设备上的工具调用与结构化抽取需求，这一场景随 AI Agent 向本地、低功耗、隐私敏感部署渗透而结构性增长。14MB
    单二进制、28MB RAM、CQ2-bit 量化与字节级语法约束显著降低了部署门槛和推理成本，使其可能成为物联网、机器人、本地 Agent 等细分赛道的“轻量基础设施”。然而，长期复利价值存在三点不确定性：其一，Cactus
    Compute 作为初创公司，商业化路径（开源+企业服务/企业版？）尚未清晰；其二，大模型厂商随时可能以类似的蒸馏/量化方案进入端侧工具调用市场；其三，45M
    参数模型虽然极致压缩，但能力边界较云上大模型窄，需持续验证在更复杂任务上的泛化能力。因此它属于“有细分赛道基础设施潜力，但仍需验证”的区间，而非 3-5 年后大概率仍是行业基石的标的。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Cactus Compute
- HuggingFace
- 端侧 AI 与边缘计算开发者生态
- Pydantic/Python 开发者生态
competitive_casualty:
- FunctionGemma 270M
- LFM2.5 230M
- Apple FM
- 云端 Function Calling API 服务商（如 OpenAI、Google）
- 规则式/正则工具调用解析方案
---

Needle 2 is an open 45M-parameter model for tool calling, device use and structured extraction. The whole model is a single 14MB binary that runs a full session in about 28MB of RAM. It is built on our Simple Attention Network findings, compressed to CQ2-bit with Cactus Quants, and baked into its own engine. On the benchmarks below, Needle 2 trades wins with other small models like FunctionGemma 270M, LFM2.5 230M and Apple FM, at 5x to 70x smaller, and 2 bits against their f16.

This repository is the Python package: inference, LoRA fine-tuning, and export. `pip install cactus-needle`

, describe your tools, and call them from Python. The inference engine is fetched once from Hugging Face and cached; there is nothing else to build.

**Self-contained**: weights baked into a single 14MB engine; no separate model files to manage, and inference does no network.**Simple contract**: tool calls come back as structured data, text in, JSON out; a byte-level grammar compiled from your schemas constrains every token.**Confidence-gated**: every response carries a calibrated confidence score from a learned head; set a threshold, act above it, escalate below it.**Tool retrieval**: declare a large catalogue and a built-in retrieval head renders only the top five tools per turn, with the grammar constrained to that subset.**Bounded memory**: a 256-token sliding window with the tools pinned as KV sinks, so total memory stays near 28MB no matter how long the conversation runs.

Weights: huggingface.co/Cactus-Compute/needle2 · source: github.com/cactus-compute/needle.

Needle 2 is a Simple Attention Network, our dense small-model recipe: a Hadamard MLP in place of the FFN, GQA attention, engram key-value memory, and multi-lane hyper-connections. See the paper for the design and ablations: arXiv:2607.18363.

Each block carries its update rule. Here x̂ is the RMS-normalised flattening of the four residual streams, H the orthonormal Walsh-Hadamard transform (a fixed matrix, applied in n log n time with no weights to read), (kₜ, vₜ) rows gathered from hashed n-gram tables, and P the doubly-stochastic normalisation of the routing logits A, computed by Sinkhorn iteration; a, b, g and all σ-gates are learned and input-dependent. Both attention and MLP residuals are sandwich-normed and gated, the engram sites fire at two layers, and decoding is constrained by a byte-level grammar compiled from the declared schemas.

`pip install cactus-needle`

Needle reads your tool descriptions to decide what to call and how to fill arguments, so describing them well is the whole game. You can do it three ways, from least to most control.

**Simple**: decorate a function. The signature gives the argument types, the docstring is the tool description, and `run()`

completes the loop: model picks the call, Needle executes your function, feeds the result back, and returns the final response with the executed tool results attached as `results`

.

```
import needle
@needle.tool
def get_weather(city: str):
"Get the current weather for a city."
return {"city": city, "temp_c": 27, "sky": "clear"}
agent = needle.Needle(tools=[get_weather])
print(agent.run("what's it like in Lagos right now?")["results"])
# [{'city': 'Lagos', 'temp_c': 27, 'sky': 'clear'}]
```

**Medium**: describe each argument and offer choices. Needle reads a Google-style `Args:`

block for per-parameter descriptions; a default makes an argument optional; a `Literal`

becomes a fixed set the model must choose from (it cannot emit anything else).

```
from typing import Literal
@needle.tool
def set_thermostat(temperature: int, mode: Literal["heat", "cool", "auto"] = "auto"):
"""Set the thermostat.
Args:
temperature: target temperature in Celsius
mode: heating strategy to use
"""
return {"temperature": temperature, "mode": mode}
agent = needle.Needle(tools=[set_thermostat])
agent.run("make it 21 and cool the room")
```

**Advanced**: constrain the values with `needle.Field`

, attached inline via `Annotated`

. Ranges, patterns, lengths, and item counts are compiled into the decode grammar, so the model can only ever emit values that satisfy them.

```
from typing import Annotated
@needle.tool
def send_money(
amount: Annotated[float, needle.Field(gt=0, le=10000, description="USD, up to 10,000")],
to: Annotated[str, needle.Field(pattern=r"^@[a-z0-9_]+$", description="recipient handle")],
memo: Annotated[str, needle.Field(max_length=80)] = "",
):
"Send money to a handle."
return {"sent": amount, "to": to}
```

`Field`

supports `description`

, `enum`

, `const`

, `ge`

/`le`

/`gt`

/`lt`

, `multiple_of`

, `min_length`

/`max_length`

, `pattern`

, `format`

, `min_items`

/`max_items`

, and `unique_items`

.

**Extraction**: to pull structured data out of text, declare the shape and call `extract()`

. Pass a Pydantic model and you get a typed object back.

```
from pydantic import BaseModel
class Invoice(BaseModel):
vendor: str
total: float
due_date: str
invoice = needle.extract("Invoice from Acme Corp, $1,200.00, due 2026-09-01", Invoice)
print(invoice.vendor, invoice.total) # -> Acme Corp 1200.0
```

**By hand** - the decorator just builds a JSON schema; you can pass that schema directly, which is exactly what Needle consumes. This is how you set descriptions and constraints without the decorator:

```
tools = [{
"name": "set_lights",
"description": "Turn a room's lights on or off and set brightness",
"parameters": {
"type": "object",
"properties": {
"room": {"type": "string", "description": "which room to control"},
"on": {"type": "boolean"},
"brightness": {"type": "integer", "minimum": 0, "maximum": 100},
},
"required": ["room", "on"],
},
}]
agent = needle.Needle(tools=tools)
```

Prefer to drive the loop yourself instead of `run()`

? `complete()`

returns the raw call and you execute it:

```
import json
response = agent.complete("dim the living room to 30")
if response["type"] == "call":
result = set_lights(**response["function_calls"][0]["arguments"])
response = agent.complete(json.dumps(result)) # feed the result back
```

With a large catalogue, persist tool embeddings across runs with `needle.Needle(tools=..., tool_index_path="tools.idx")`

. Every turn returns one JSON object:

```
{
"type": "call",
"success": true,
"error": null,
"error_code": null,
"function_calls": [ { "name": "set_lights", "arguments": { "room": "living room", "on": true, "brightness": 30 } } ],
"reasoning": "'living room' -> room; 'dim' -> on true, brightness 30",
"confidence": 0.94,
"prefill_tps": 4300.0,
"decode_tps": 850.0
}
```

Try any model in the browser: pick a preset, edit the tools or prompt, and Run. Follow-up queries continue the same conversation.

```
needle playground # base model, http://127.0.0.1:7860
needle playground --weights my.cact # a tuned model
```

The server downloads and initializes the model before serving, so the first query is instant. The **Finetune on these tools** button runs the fine-tuning pipeline below from the UI and hands back a downloadable `.cact`

.

Needle solves every problem as a function call. The context declares what may be called; the model answers with calls. Performing an action and extracting structured data are the same operation, the only difference is what you declare.

- A request no declared tool can serve is refused with the empty call
`[]`

. That is the whole contract for off-topic input; there is no free-text fallback. - Arguments contain only values evidenced by the input. An optional field with no evidence is omitted, not guessed; omission is the field-level
`[]`

. `reasoning`

is the model's short derivation of each argument from its source span (`'ten minutes' -> minutes 10`

). It is generated unconstrained; only the call itself is grammar-constrained, so the JSON cannot be malformed while the derivation stays legible.- After you execute a call, pass the result back as the next
`complete()`

. The model continues from it, and later arguments may depend on earlier results:`search_for_contact`

first, then`send_instant_message`

with the returned`contact_id`

. A final`"type": "respond"`

with empty`function_calls`

signals the loop is done; the answer is the tool results themselves, which`run()`

collects on the final response as`results`

. No free text is generated. - A session shares one toolset. Later turns are bare queries against the same tools;
`reset()`

rewinds the conversation and keeps the tools loaded.

Extraction is not a separate mode - it is tool calling with one tool. Declare the record as the only schema and pass the content where the query goes; the returned call's `arguments`

are the extracted fields. With one declared tool the grammar admits exactly one call of that name, so schema conformance is guaranteed rather than requested. Use the `extract()`

helper for a typed result (shown in Quickstart), or pass a plain schema and read the call:

```
receipt = [{
"name": "receipt",
"description": "A purchase receipt shared as text",
"parameters": {
"type": "object",
"properties": {
"merchant": {"type": "string"},
"total": {"type": "number"},
"currency": {"type": "string"},
"line_items": {"type": "array", "items": {"type": "object"}},
},
"required": ["merchant", "total"],
},
}]
agent = needle.Needle(tools=receipt)
print(agent.complete("GreenMart receipt: oat milk 3.50, total 7.75 paid by visa")["function_calls"])
# -> [{"name": "receipt", "arguments": {"merchant": "GreenMart", "total": 7.75}}]
```

Because it is the same operation, everything else applies unchanged: `confidence`

gates the extraction, unsupported input returns the empty call `[]`

, and fine-tuning uses the same data format (the record as the tool, the passage as the query).

An optional system turn carries environment state as facts, never instructions:

`agent = needle.Needle(tools=tools, system="date: 2026-07-21 Tue 14:30; locale: en-US; device: phone; battery: 62%")`

Recognized keys are `date`

, `locale`

, `device`

, `battery`

, `network`

, `location`

, `user`

, and `assistant`

. The model resolves relative language against them: "tomorrow at 7" becomes an absolute time only when a `date:`

fact licenses it, otherwise the human phrase passes through verbatim. `assistant:`

declares the identity the model binds to. Needle trains with and without the turn, so omitting it is safe; instructions placed there do not steer the model.

Five or fewer declared tools render directly. Above that, retrieval engages: at init every tool schema is embedded once by a built-in contrastive head, each turn embeds the query, and only the five highest-scoring tools enter the context, with the grammar rebuilt over just that subset. An unselected tool is unreachable, not merely unlikely. `tool_index_path`

persists the embeddings on disk, keyed by a fingerprint over the schemas and the model; a matching fingerprint loads instantly, a changed schema re-embeds only what changed.

The `confidence`

field is the minimum of two signals: a calibrated post-hoc head that scores the full prompt plus the call the model just produced, and the decoding probability of the call tokens. A call is accepted only when both agree, so the failure mode is escalation, not wrong execution. The contract: pick a threshold for your product, act at or above it, re-ask or route to a bigger model below it. Off-topic requests return the empty call `[]`

.

Needle fine-tunes with LoRA on the frozen base and merges the adapter at export, so a run is cheap and the tuned model is still a single `.cact`

that runs on the same engine. The workflow is: (optionally) synthesize data, LoRA fine-tune, then build a tuned `.cact`

.

**Data format.** A JSONL file, one example per line. `reasoning`

is optional; an off-topic example has `answers: []`

.

`{"query": "dim the kitchen to 10", "tools": [{"name": "set_lights", "parameters": {"type": "object", "properties": {"room": {"type": "string"}, "brightness": {"type": "integer"}}, "required": ["room"]}}], "answers": [{"name": "set_lights", "arguments": {"room": "kitchen", "brightness": 10}}], "reasoning": "'kitchen' -> room; 'dim to 10' -> brightness 10"}`

**1. Synthesize data (optional).** Needs `OPENROUTER_API_KEY`

. Seed from a tool schema file, or expand an existing set:

```
export OPENROUTER_API_KEY=sk-or-...
needle generate-data --tools my_tools.json --num-samples 500 --output data.jsonl
needle generate-data --augment data.jsonl --num-samples 500 # expand an existing JSONL
```

Set `OPENROUTER_URL`

to use an OpenAI-compatible gateway instead of the default OpenRouter endpoint.

**2. LoRA fine-tune.** The base checkpoint auto-downloads from Hugging Face if you do not pass `--checkpoint`

. `--generate N`

first synthesizes N more examples from the tools in your data (also needs `OPENROUTER_API_KEY`

).

```
needle finetune data.jsonl --epochs 3
needle finetune data.jsonl --epochs 3 --generate 300 --lora-rank 16 --lora-alpha 32
```

Key options: `--lora-rank`

(default 16), `--lora-alpha`

(32), `--lr`

(1e-4), `--batch-size`

(16), `--max-len`

(1024), `--checkpoint <base.pkl>`

, `--out <adapter.pkl>`

. The adapter is written to `checkpoints/needle_lora.pkl`

.

**3. Build a tuned .cact.** Merge the adapter into the base and quantize. The base auto-downloads if absent.

`needle build checkpoints/needle2.pkl --lora checkpoints/needle_lora.pkl --out my_needle.cact`

Add `--bits 2`

(default 4) for a smaller model, or set `NEEDLE_HF_REPO=<you>/<model>`

and pass `--upload`

to publish the `.cact`

.

**4. Run it.** The engine is weights-agnostic, so a tuned `.cact`

runs on it directly - no recompilation:

```
import needle
agent = needle.Needle(weights="my_needle.cact", tools=[...])
agent.run("...")
```

Needle 2 is built by the Cactus Compute team. If you use it in your work, please cite:

```
@misc{needle2_2026,
title = {Needle 2: A 45M-Parameter Foundation Tool-Calling Model for Tiny Devices},
author = {Ndubuaku, Henry and Mosoyan, Karen and Mroz, Jakub and Cylich, Noah and
Kumar, Satyajit and Sandhu, Parkirat and Shemet, Roman and Lee, Justin H.},
year = {2026},
organization = {Cactus Compute, Inc.},
howpublished = {\url{https://github.com/cactus-compute/needle}}
}
```

Reach out on founders@cactuscompute.com for partnerships, collaborations, synergies and deploying Needle2 in your product.