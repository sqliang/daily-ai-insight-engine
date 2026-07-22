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
tldr: 该论文提出提示注入攻击的根源在于大语言模型将所有输入（系统提示、用户消息、工具输出和自身响应）视为单一连续文本流，仅靠角色标签（system、user、assistant、think、tool）区分内容类型。角色标签作为语言中唯一的离散控制机制已承载过多职责（信任、威胁、身份、生成模式），导致模型容易通过标签混淆被攻击。
objective_summary: 一篇以博客形式呈现的学术论文，提出提示注入攻击的本质是角色混淆（Role Confusion）。LLM 将所有输入——系统提示、用户消息、工具输出、自身推理和响应——拼接成一条连续的
  token 字符串，没有任何感官通道来区分"自己的想法"和"别人的话"。模型只能依赖插入在文本中的角色标签（system、user、assistant、think、tool）来恢复结构。这些标签原本应是离散的控制机制，但随着时间推移被赋予了信任层级、威胁识别、身份设定和生成模式等多重职责，导致过载和脆弱性。文章还展示了角色边界的单向镜效应，如许多
  LLM 会在 assistant 输出中否认 think 块的存在。
event_type: policy_and_safety
epistemic_status: theoretical_claim
entities:
  companies:
  - OpenAI
  - Anthropic
  - DeepSeek
  technologies:
  - Prompt Injection
  - RLVR
  - Chain of Thought
  - Chat Templating
  key_people: []
key_logic_flow:
- 大语言模型的所有输入（系统提示、用户消息、工具输出、自身推理和响应）被拼接成一条连续的 token 字符串，模型只能通过角色标签来区分不同来源的内容。
- 角色标签（system、user、assistant、think、tool）是语言中唯一的离散控制机制，但已被过载地承载了信任层级、威胁识别、身份设定和生成模式等多重职责。
- 提示注入攻击之所以成功，是因为攻击者可以在统一 token 流中插入或篡改角色标签，使模型将恶意输入误认为高信任级别的指令。
- 角色边界在模型内部产生了类似单向镜的效应，例如许多 LLM 在生成 assistant 文本时会口头否认前文 think 块的存在，尽管该块仍在上下文中影响输出。
- 文章认为理解角色的本质是建立 AI 安全科学的基础，并呼吁对角色机制进行系统性研究。
extract_result: success
object_mentions:
- object_type: paper
  name: Prompt Injection as Role Confusion
  canonical_name: Prompt Injection as Role Confusion
  url: https://role-confusion.github.io/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该文章是一篇博客风格的学术论文，提出提示注入攻击的根源在于大语言模型对角色标签的混淆处理机制。
  - 文章展示了 LLM 将所有输入视为单一连续 token 流，仅靠角色标签区分内容，从而解释了提示注入为何能成功。
  - 文章还讨论了角色边界的单向镜效应，例如许多 LLM 在 assistant 生成中否认 think 块的存在。
  article_id: 3fbf4fa1cdf402e1
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