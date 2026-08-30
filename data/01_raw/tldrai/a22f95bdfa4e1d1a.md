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
pipeline_stage: ingested
id: a22f95bdfa4e1d1a
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