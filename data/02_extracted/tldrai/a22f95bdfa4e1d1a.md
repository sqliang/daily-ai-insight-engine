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