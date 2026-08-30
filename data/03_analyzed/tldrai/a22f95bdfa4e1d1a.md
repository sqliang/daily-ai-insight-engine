---
title: 'Introducing Flex: Let the Model Write the Code (16 minute read)'
source: https://www.cmpnd.ai/blog/let-the-model-write-the-code.html?utm_source=tldrai
author: []
published: ''
created: '2026-08-07'
manifest_dates:
- '2026-08-07'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: a22f95bdfa4e1d1a
source_type: news_media
tldr: DSPy 推出新模块 Flex，让 GEPA 优化器不仅能重写提示词，还能直接改写程序代码。在位置融合任务上，Flex 配合 GEPA 将准确率从 90.4%
  提升至 95.0%，成本较基线降低 28%，速度提升 40%。
objective_summary: CMU 博士生 Michael Isaac 在 cmpnd 实习期间为 DSPy 实现了新模块 Flex，该模块允许优化器同时优化提示词与程序代码本身。在位置融合评测（1029
  条标注对、240 条保留集）中，Flex 配合 GEPA 达到 95.0% 准确率，每千条成本 0.70 美元，比基线便宜 28% 且快 40%。Flex 生成的代码默认在沙箱解释器中执行，不在宿主进程内运行，只有预测器调用与显式提供的工具可桥接回宿主进程。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - cmpnd
  - Carnegie Mellon University
  - Anthropic
  technologies:
  - DSPy
  - Flex
  - GEPA
  - MIPROv2
  - BootstrapFewShot
  - Predict
  - ReAct
  - RLM
  key_people:
  - Michael Isaac
  - Drew
key_logic_flow:
- Flex 是 DSPy 本周新引入的模块，允许优化器 GEPA 不仅重写程序指令，还直接改写程序代码本身。
- Flex 以 dspy.Flex(YourSignature) 形式使用，可嵌入现有 Predict、ReAct 或 RLM 程序，优化前行为与 Predict
  一致。
- 模型生成的代码默认在沙箱解释器中执行，不在宿主进程运行，只有预测器调用和显式提供的工具可桥接回宿主进程。
- 在 1029 条标注对、240 条保留集的位置融合任务上，基线 Predict 准确率为 90.4%，成本每千条 0.98 美元。
- 仅优化提示词的 GEPA 将准确率提升至 92.5%，但成本涨至每千条 2.88 美元，且推理速度慢 48%。
- Flex 配合 GEPA 将准确率提升至 95.0%，成本降至每千条 0.70 美元，比基线便宜 28% 且快 40%。
object_mentions:
- object_type: project
  name: Flex
  canonical_name: DSPy Flex
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 文章正式介绍了加入 DSPy 的新模块 Flex，它利用模型的编程能力重写程序代码而不只是指令。
  - Flex 可嵌入现有 Predict、ReAct 或 RLM 程序，优化前它就是一个 Predict 模块或 RLM。
  - 在位置融合评测中，Flex 配合 GEPA 将准确率从 90.4% 提升至 95.0%，成本低于基线。
  article_id: a22f95bdfa4e1d1a
- object_type: project
  name: DSPy
  canonical_name: DSPy
  url: https://github.com/stanfordnlp/dspy
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 文章围绕 DSPy 框架展开，Flex 是 DSPy 的新模块，核心立场是任务可随 AI 生态演进被重新实现。
  - Flex 以 dspy.Flex(YourSignature) 的形式提供，用户可直接替换原有 dspy.Predict 调用并保持相同结果。
  article_id: a22f95bdfa4e1d1a
- object_type: project
  name: GEPA
  canonical_name: DSPy GEPA
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - GEPA 是 DSPy 的优化器，过去通过重写指令改进程序，如今配合 Flex 还能优化代码本身。
  - 将 Flex 模块交给 dspy.GEPA 后，反射模型可能分解程序、编写辅助函数、实现路由逻辑并重写提示词。
  article_id: a22f95bdfa4e1d1a
extract_result: success
impact_score:
  score: 6.5
  reason: 评分依据：Flex 将 DSPy 优化器的优化对象从"提示词"扩展到"程序代码本身"，让优化器能自动分解程序、编写辅助函数、实现路由逻辑并在适当时机跳过模型调用，这是
    LLM 编程范式从"提示词工程"向"程序合成"演进的关键一步。评测数据真实可信（准确率 90.4%→95.0%，成本降 28%、速度提升 40%，且披露了仅优化提示词的副作用），对
    DSPy 生态内用户价值显著。但该事件属于框架层迭代而非行业范式转移：证据仅来自单一"位置融合"任务，跨任务泛化性未验证，且 DSPy 在 LLM 应用框架市场仅为主要玩家之一，冲击力尚未达到"改变行业格局"的
    8 分以上级别，故综合给 6.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 优化器自动改写程序代码的可靠性边界与沙箱安全隔离机制
hype_assessment:
  level: low
  reason: 判定依据：文章标题"Let the Model Write the Code"及"models have become excellent programmers"带有一定叙事包装，但核心内容是具体可复现的实验数据（1029
    条标注对 + 240 条保留集、全程禁用缓存、成本与延迟全量披露），并坦诚给出了仅优化提示词时的成本副作用（成本涨至 2.9 倍、速度慢 48%）。全文未滥用"颠覆""革命性"等
    PR 词汇，且对模型生成代码的安全边界（沙箱解释器执行、仅预测器调用与显式工具桥接回宿主、max_predictor_calls 上限）做了交代。唯一保留是证据集中于单一任务，泛化性尚未证明，但不足以构成概念炒作，故判定为低炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 核心突破在于将 LLM 程序的优化闭环从"提示词层"下沉到"代码层"：Flex 向优化器暴露模块源码，使 GEPA
    能自动分解程序、编写辅助函数、实现路由逻辑，并在程序内部直接完成解析与比较后把更窄的问题抛给模型，实现"更少的调用、更精准的调用"。工程上通过沙箱解释器隔离模型生成的不可信代码，仅以预测器调用和显式提供的工具桥接回宿主进程，并设置
    max_predictor_calls 上限约束每次前向传播的桥接次数，解决了模型自写代码的安全执行边界问题。这标志着优化范式从 Prompt 搜索/改写正式转向程序合成，模型从"被调用的黑盒"变成"程序的作者"。
  business_model: 对 LLM 应用开发生态的商业模式影响：Flex 实测将推理成本降低 28%、速度提升 40%，直接强化了 DSPy 这类"声明式任务定义
    + 自动优化"框架的商业价值主张——开发者只需定义任务、签名与评估指标，优化器产出更便宜更快的程序，这会重塑 LLM 应用的交付与运维方式，推动"优化即服务"、企业级程序优化工具链等潜在商业化路径，同时弱化传统提示词工程模板/咨询服务的市场价值。
engineering_complexity: prototype
compound_value:
  score: 8.0
  reason: Flex 标志着 AI 程序优化从『提示词工程』跃迁到『程序工程』：优化器不再局限于改写指令，而是直接生成、分解、路由并重写代码本身。复利效应体现在三个层面：其一，优化产物（program
    artifact）可保存、可 diff、可审计，使优化成果沉淀为可累积的工程资产而非一次性提示词，具备典型的『越用越值钱』特征；其二，沙箱解释器 + max_predictor_calls
    上限从机制上解决了『模型生成代码不可信』的核心安全障碍，这是该范式能否规模化落地的关键闸门，DSPy 率先给出工程化答案；其三，实证数据（准确率 90.4%→95.0%、成本降
    28%、速度提 40%）验证了『更少调用、更精准调用』的结构性降本逻辑，且相比纯提示词优化（成本涨 2.9 倍、慢 48%）有代际优势。主要风险在于 DSPy
    作为开源框架的独立商业变现路径尚不清晰，且该能力高度依赖顶级闭源模型的代码生成水平（文中依赖 Claude Opus 5），但 3-5 年内『模型写程序』大概率成为
    AI 系统工程的基础设施范式，故给予 8.0 分。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- DSPy
- Anthropic
- cmpnd
competitive_casualty:
- 纯提示词优化工具
- 低代码/无代码 AI 平台
- 手动编排的 Agent 框架（LangChain 类）
market_opportunities:
- 使用 DSPy 的团队可将现有 Predict/ReAct 模块替换为 Flex，借助 GEPA 对提示词与程序代码的联合优化，在提升准确率的同时降低推理成本与延迟，适合在位置融合等高判断成本任务中优先试点
- Flex 将优化目标从提示词扩展到程序代码，为 MLOps 与 LLM 应用交付平台提供了新的差异化功能方向，可围绕'自动化程序优化 + 成本/延迟优化'构建商业化工具或托管服务
- 模型生成代码的沙箱执行与受控桥接机制具有独立的工程价值，可借鉴该隔离模式开发面向 AI 生成代码的安全执行环境、审计与可观测性工具链，满足企业级合规与安全需求
risk_matrix:
  regulatory: 模型生成并持续变异的代码难以满足金融、医疗等强监管行业对算法可审计、可解释的要求；若优化后的程序处理个人数据（如位置信息），还需评估数据隐私与合规责任归属问题
  technological: AI 生成的代码本质上是不可信代码，尽管默认在沙箱解释器中执行，仍存在沙箱逃逸或预测器桥接被滥用的残余风险；优化产物可读性差、难以维护和调试，且结果依赖特定反射模型（如
    Claude Opus），底层模型变更可能导致优化行为不稳定
  competitive: 代码级优化的范式门槛并不高，LangChain、LlamaIndex 等主流框架及大型模型厂商可能快速跟进同质化能力，DSPy 的先发优势存在被稀释的风险
  ethical: AI 自行改写代码可能放大训练数据中隐含的偏见，且优化后的决策逻辑对终端用户不透明、难以解释和申诉，存在算法问责与透明度的隐患
  additional:
  - 优化阶段需反复调用高性能反射模型（如 Claude Opus），一次性优化成本较高，小团队或低成本场景需谨慎权衡优化投入与推理节省
  - 当前评测仅基于单任务（位置融合），跨任务与跨领域的泛化效果尚未得到验证，宣传数字的代表性有限
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: Flex
  canonical_name: DSPy Flex
  url: null
  positioning: Flex 是 DSPy 新引入的模块，允许优化器（如 GEPA）在优化提示词的同时直接改写程序代码本身，让模型编程能力参与程序迭代优化。
  technical_signal: Flex 暴露程序代码与指令给优化器，模型生成的代码默认在沙箱解释器中执行，仅预测器调用与显式工具可桥接回宿主进程，并以 max_predictor_calls
    设限。
  adoption_signal: Flex 可嵌入现有 Predict、ReAct 或 RLM 程序，优化前行为与 Predict 一致，能以 dspy.Flex(YourSignature)
    形式即插即用。
  ecosystem_relevance: Flex 属于 DSPy 生态的核心演进，将“优化器重写提示词”升级为“优化器重写程序代码”，延续 DSPy 让任务定义可随模型能力演进的核心理念。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Flex 让优化器同时改写提示词与代码，为可编程 AI 程序提供了新的优化维度。位置融合任务上它以低于基线的成本实现更高准确率，其代码沙箱执行与可保存、可加载的程序工件设计，可能重塑
    DSPy 等框架的程序优化范式，值得持续跟踪其在更多任务上的泛化表现与生态采用情况。
  risk_notes:
  - 模型生成的代码仍属不可信代码，沙箱执行策略虽降低风险，但桥接宿主进程的预测器调用仍可能引入安全隐患。
  - Flex 依赖 GEPA 等优化器与强反射模型配合，优化效果对模型编程能力与评测任务的泛化存在不确定性。
  score: 8.0
  article_ids:
  - a22f95bdfa4e1d1a
  evidence_snippets:
  - 文章正式介绍了加入 DSPy 的新模块 Flex，它利用模型的编程能力重写程序代码而不只是指令。
  - Flex 可嵌入现有 Predict、ReAct 或 RLM 程序，优化前它就是一个 Predict 模块或 RLM。
  - 在位置融合评测中，Flex 配合 GEPA 将准确率从 90.4% 提升至 95.0%，成本低于基线。
- object_type: project
  name: GEPA
  canonical_name: DSPy GEPA
  url: null
  positioning: GEPA 是 DSPy 的优化器，过去通过重写指令改进程序，如今配合 Flex 可同时优化提示词与程序代码，成为驱动程序级自动优化的核心组件。
  technical_signal: GEPA 在 Flex 加持下可让反射模型分解程序、编写辅助函数、实现路由逻辑并重写提示词，以最大化评测指标为目标生成优化后程序。
  adoption_signal: GEPA 配合 Flex 在位置融合任务上以每千条 0.70 美元成本达到 95.0% 准确率，较仅优化提示词的成本与延迟显著更优。
  ecosystem_relevance: GEPA 与 Flex 共同构成 DSPy 提示词与代码双维优化链路，推动 DSPy 生态从“指令优化”走向“程序优化”的新阶段。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: GEPA 作为 DSPy 的核心优化器，从仅重写指令升级为可改写程序代码，配合 Flex 在成本、速度与准确率三方面同时改善，代表程序级自动优化的新方向，其反射模型驱动代码生成的方式值得长期跟踪。
  risk_notes:
  - GEPA 优化依赖大型反射模型生成代码，优化过程的 token 成本与推理延迟较高，在部分场景可能抵消推理端的收益。
  - 其优化效果高度依赖评测指标设计与训练集质量，代码改写可能引入超出预期的行为偏差或过拟合风险。
  score: 7.0
  article_ids:
  - a22f95bdfa4e1d1a
  evidence_snippets:
  - GEPA 是 DSPy 的优化器，过去通过重写指令改进程序，如今配合 Flex 还能优化代码本身。
  - 将 Flex 模块交给 dspy.GEPA 后，反射模型可能分解程序、编写辅助函数、实现路由逻辑并重写提示词。
---

*This is a guest post by Michael Isaac, a PhD student in software engineering at Carnegie Mellon University, written during his internship at cmpnd. Michael implemented Flex, the module this post introduces, for DSPy.*

The core position of DSPy is that you can define a task once, in a way that lets it be re-implemented as the AI ecosystem advances. The history of these re-implementations can be understood as a history of the models; of weaknesses we worked around and strengths we leveraged:

- In 2022, models needed to be shown what a task looked like, so optimizers like BootstrapFewShot automated the picking of few-shot examples.
- Models then grew to be capable prompt authors, so optimizers like MIPROv2 and GEPA could improve programs by rewriting their instructions.
- Lately, models have become excellent programmers.

This week, we're introducing `Flex`

to DSPy, which leverages the coding skills of models to rewrite not just the instructions of your program, but the code itself.

## Flex Lets GEPA Optimize the Code

`dspy.Flex(YourSignature)`

is a DSPy module, which can be dropped into any of your existing `Predict`

, `ReAct`

, or `RLM`

programs. For example:

```
my_signature = "question -> answer"
my_program = dspy.Predict(my_signature)
# Make it Flex!
my_program = dspy.Flex(my_signature)
```


If we run either of these programs, we'd get the same result. Prior to optimization, Flex is just a Predict module (or RLM if you provide tools).

What makes Flex different is what it exposes to an optimizer: `Flex`

exposes its code, in addition to its instructions. Hand a Flex module to `dspy.GEPA`

and the reflection model might decompose your program, write helper functions, implement routing logic, *and* rewrite your prompts. The output is an optimized program that performs best against the metric you gave it.

This is how you'd optimize a Flex module with GEPA. `SamePlace`

here is the signature for the location conflation task we'll walk through in the next section:

```
program = dspy.Flex(SamePlace) # was: dspy.Predict(SamePlace)
# cheap LM to use during inference
dspy.configure(lm=dspy.LM("anthropic/claude-haiku-4-5"))
# big LM to write the code and instructions
big_lm = dspy.LM("anthropic/claude-opus-5")
optimized = dspy.GEPA(
metric=make_metric(penalty=0.2),
reflection_lm=big_lm,
max_metric_calls=400,
).compile(program, trainset=train, valset=val)
```


After optimization, `optimized.save("program.json")`

persists the source and `dspy.Flex(SamePlace).load(...)`

restores it. The artifact is a file you can open, read, diff, and reason about.

What you get back is a program the reflection model wrote to score as high as it can against your metric. Two things tend to follow. Sometimes it doesn't call the model at all, because it found a case it could settle in code. And when it does call, the call is better aimed, because the module has already done the parsing and comparison and hands the model a narrower question. Fewer calls, better calls, and a program that outperforms the one you handed it.

Code written by a model is still untrusted code, so by default **it never runs in your process**. Flex executes the generated source inside a sandboxed interpreter. Only predictor calls and the tools you explicitly provided bridge back to the host process, and a `max_predictor_calls`

cap bounds how many times per forward that bridge can be crossed.

## Location Conflation Task

Last year, Drew demonstrated prompt optimization at the Data + AI Summit with a geospatial conflation task: given two place listings, decide whether they're the same physical place. It's deceptively hard in the tail. KIN CAFE and KIN at the same address are the same place. CONCESSION #2 KEN MERCER SPORTS PARK and KEN MERCER SPORTS PARK at the same address are not.

We replaced `Predict`

with `Flex`

and ran GEPA on this task: 1,029 labeled pairs, evaluated on 240 held-out records (class-balanced, so 50% is chance). Caches were disabled throughout, so the cost and latency figures below are what cold production traffic would pay.

The **baseline** is the original `dspy.Predict`

, one model call per record: 90.4% accuracy at $0.98 per thousand records.

**Optimizing only the prompt** with GEPA, no Flex, lifts accuracy to 92.5%. But the only lever a prompt optimizer has is the instruction, so it wrote a much longer one, and every record pays for those extra tokens at inference: $2.88 per thousand records, 2.9x the baseline cost, and 48% slower.

**Flex gives the optimizer a second lever: the module code.** Running GEPA, unchanged, on the Flex program lifted accuracy from 90.4% to 95.0% at a cost of $0.70 per thousand records. By optimizing the prompt *and* the code, Flex produced a program that is 28% cheaper and 40% faster than the baseline.