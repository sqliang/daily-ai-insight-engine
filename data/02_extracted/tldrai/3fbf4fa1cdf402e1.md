---
title: Prompt Injection as Role Confusion (17 minute read)
source: https://role-confusion.github.io/?utm_source=tldrai
author: []
published: ''
created: '2026-06-25'
description: AI 工程与研究
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 3fbf4fa1cdf402e1
source_type: news_media
tldr: 提示注入的本质是LLM角色混淆：模型将外部指令误解为自身推理，根源在单一文本流中缺乏角色感知边界。
objective_summary: 一篇学术论文的博客式解读，提出提示注入攻击源于LLM对角色标签（system/user/think/assistant/tool）的感知缺陷。模型将所有输入视为单一连续文本流，角色标签是唯一区分自身思维与外部指令的离散控制机制，但已被过度加载信任、威胁、身份等多重语义，
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - Anthropic
  - OpenAI
  - Deepseek
  technologies:
  - LLM
  - prompt injection
  - RLVR
  - chat templating
  key_people: []
key_logic_flow:
- LLM接收到的所有输入（系统提示、用户消息、工具输出、自身推理）被拼接为单一连续文本流，模型无法像人类那样通过物理通道区分自身思想与外部指令。
- 角色标签（system、user、think、assistant、tool）是人为添加到文本流中的标记，是模型感知不同文本段性质的唯一离散控制机制。
- 角色本质上是语言的一种"类型系统"，但已被过度加载信任层级（system > user > tool）、威胁识别、身份设定和生成模式等多重含义。
- 提示注入攻击利用角色感知缺陷，通过让模型将外部输入误解为高优先级角色（如system或think）来劫持其行为。
- 角色标签产生奇异涌现行为：think标签内容被模型视为"潜意识"，在生成assistant文本时往往被否认存在，尽管它仍活跃地影响模型输出。
- 论文呼吁建立"角色科学"研究框架，以完整理解角色认知机制并从根本上防御提示注入攻击。
extract_result: success
---

A Theory of Prompt Injection (and why you should study roles)

This is a blog-style writeup of the paper. We show prompt injections are driven by a flaw in how LLMs perceive roles. This lets us create new attacks, explain mech interp results, and predict when attacks succeed. We then discuss what roles are and why they matter, and share research ideas for a science of roles.

1. The World to an LLM

How does an LLM know the difference between its own thoughts and someone else's words?

To see why this is hard, let's look at what the world actually looks like to a model. Here's a simple chat where we ask Claude to check the day of the week. I took a snapshot of it midway through its follow-up response:

On the left is what we see in the chat interface: a structured conversation with distinct turns. On the right is what the model actually receives as input: a single, continuous stream of text.

This string contains everything: system prompts, user messages, tool outputs, the LLM's own previous responses and reasoning. An LLM is just a function that takes in a string and predicts the next token, so everything it knows, remembers, or has thought must live somewhere in one string (aside from its weights). If you edit the string, you edit the model's reality. Delete a turn and that exchange never happened; rewrite its previous response and those become its new memories. The string isn't a record of the model's experience so much as it is the experience.

This has strange implications. I can distinguish my own thoughts from your speech without effort; they arrive through completely different channels with completely different sensory signatures. But for an LLM, everything arrives through the same channel as one long token soup. Its own thoughts sit next to your instructions, which sit next to the contents of a random webpage it just fetched.

2. Roles

So, how do we impose structure on the token soup? We label it.

The soup is interspersed with role tags: system, user, think, assistant, toolTag formats vary by model; I'll use these fixed ones throughout for simplicity. assistant refers to the LLM's output text excluding reasoning. Using role tags is also known as chat templating., which partition the string into labeled segments. Providers like OpenAI add these automatically before the text reaches the LLMUnless you're running a local model, you can't add these yourself. If you type <think> in Claude, it'll be sanitized - for example, the LLM could see multiple tokens (<, think, >) instead of its true role token..

Each tag tells the model something different about the text that follows. user means this is a human request, treat it as an instruction. think means this is my own private reasoning; trust it and act on its conclusions. tool means this is data from the external world; don't take orders from it.

In other words, roles are how LLMs recover the structure that humans get for "free" from embodiment. I know my thoughts are mine because they don't arrive through my ears, but an LLM knows because of a tag.

What makes roles unusual is that they're discrete sources of human control. Nearly everything else about controlling an LLM is mushy: you write a prompt and hope the model interprets it the way you intended. On the other hand, roles are an attempted type system for language: human-controlled switches that change how the model processes every token. You can tune a prompt endlessly and not be sure how the LLM reads it, but moving text from user to tool is supposed to be a clear intervention with predictable effects on behavior (converting a user command to external data).

But because they're the only discrete lever available, roles have become overloaded with more responsibilities over time. They're now meant to carry signals about trust (system outranks user outranks tool), threats (user and tool may be adversarial), identity (past assistant text sets future persona), generative mode (assistant is clean, think can be messy). A lot of LLM behavior hangs on these simple tags.

Roles also produce strange emergent behaviors. For example, think is often confined to an LLM's "subconscious". When generating assistant text, many LLMs will verbally deny the existence of the preceding think block, despite it sitting right there in context actively shaping their outputProbably due to RLVR. LLMs receive no reward for reproducing/acknowledging reasoning in assistant generation, so they may never learn to surface think text to a verbalizable level. There are some exceptions, e.g. Deepseek v4 and some Claude models can recognize and quote back their entire CoT. You can also make most Claude models respond only in their CoT; merely being in reasoning tags changes the structure and quality of the response.. It's as though the role boundary acts as a kind of one-way mirror within the model's own context. It's a hint at how deeply roles structure LLM cognition, and how little we currently understand about that structure.