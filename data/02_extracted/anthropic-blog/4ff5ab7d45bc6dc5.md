---
title: Golden Gate Claude
source: https://www.anthropic.com/news/golden-gate-claude
author: []
published: '2026-07-09'
created: '2026-07-14'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4ff5ab7d45bc6dc5
manifest_dates:
- '2026-07-14'
- '2026-07-15'
source_type: tech_blog
tldr: Anthropic 发布了一篇大语言模型可解释性研究论文，在 Claude 3 Sonnet 的神经网络中识别出数百万个概念级「特征」，并可通过调节特征强度改变模型行为。他们放大「金门大桥」特征后创建了「Golden
  Gate Claude」演示版本，该模型会不自觉地围绕金门大桥回答任何提问。该演示仅上线 24 小时，目前已下线。
objective_summary: Anthropic 于 2024 年发布了一篇关于大语言模型可解释性的研究论文，首次系统性地绘制了 Claude 3 Sonnet
  神经网络内部的数百万个概念级「特征」，这些特征会在模型读到相关文本或看到相关图像时激活。研究团队找到了对应「金门大桥」的特定神经元组合，并能够上调或下调该特征的激活强度，从而观察模型行为的相应变化。当放大金门大桥特征后，Claude
  的回复会不由自主地提及金门大桥，例如推荐用 10 美元开车过桥交过路费。该「Golden Gate Claude」版本以研究演示形式在 claude.ai 上线
  24 小时后下线。研究团队表示，同样的技术可以用于调节与危险代码、犯罪行为或欺骗等安全相关的特征，有助于让 AI 模型更加安全。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies: []
  key_people: []
key_logic_flow:
- Anthropic 发布了一篇大语言模型可解释性研究论文，首次在 Claude 3 Sonnet 的神经网络中绘制了数百万个概念级「特征」，这些特征会在模型遇到相关文本或图像时激活。
- 研究人员找到了代表「金门大桥」的特定神经元组合，并能够精确调节该特征的激活强度，观察模型行为的相应变化。
- 当放大金门大桥特征后，Claude 的回复会不由自主地聚焦于金门大桥，即使提问与桥梁无关也会给出与大桥相关的回答。
- Anthropic 将这一版本的「Golden Gate Claude」以研究演示形式在 claude.ai 上线 24 小时，供公众体验。
- Anthropic 强调这不是系统提示或微调，而是对模型内部激活的精确实操性改变。
- 该技术同样可用于调节与危险代码、犯罪行为或欺骗等安全相关的特征，有望在未来帮助提升 AI 模型的安全性。
extract_result: success
object_mentions:
- object_type: project
  name: Golden Gate Claude
  canonical_name: Golden Gate Claude
  url: https://www.anthropic.com/news/golden-gate-claude
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 将放大金门大桥特征后的 Claude 3 Sonnet 命名为「Golden Gate Claude」，并上线了 24 小时的研究演示供公众体验。
  - 该演示点击 claude.ai 右侧的金门大桥标志即可进入，但会表现出不可预测甚至令人不适的行为。
  article_id: 4ff5ab7d45bc6dc5
- object_type: paper
  name: Anthropic Interpretability Research Paper
  canonical_name: Anthropic LLM Interpretability Paper
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Anthropic 发布了一篇关于大语言模型可解释性的重要研究论文，开始绘制 Claude 3 Sonnet 模型的内部工作机制。
  - 论文展示了如何识别数百万个特征并调节其激活强度，以及这些操作对应的行为变化。
  article_id: 4ff5ab7d45bc6dc5
- object_type: model
  name: Claude 3 Sonnet
  canonical_name: Claude 3 Sonnet
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 该可解释性研究以 Claude 3 Sonnet 为研究对象，在其神经网络中发现了数百万个概念级特征。
  - Golden Gate Claude 是基于 Claude 3 Sonnet 进行特征放大操作后得到的研究演示版本。
  article_id: 4ff5ab7d45bc6dc5
---

# Golden Gate Claude

*UPDATE: Golden Gate Claude was online for a 24-hour period as a research demo and is no longer available. If you'd like to find out more about our research on interpretability and the activation of features within Claude, please see this post or our full research paper.*

On Tuesday, we released a major new research paper on interpreting large language models, in which we began to map out the inner workings of our AI model, Claude 3 Sonnet. In the “mind” of Claude, we found millions of concepts that activate when the model reads relevant text or sees relevant images, which we call “features”.

One of those was the concept of the Golden Gate Bridge. We found that there’s a specific combination of neurons in Claude’s neural network that activates when it encounters a mention (or a picture) of this most famous San Francisco landmark.

Not only can we identify these features, we can tune the strength of their activation up or down, and identify corresponding changes in Claude’s behavior.

And as we explain in our research paper, when we turn up the strength of the “Golden Gate Bridge” feature, Claude’s responses begin to focus on the Golden Gate Bridge. Its replies to most queries start to mention the Golden Gate Bridge, even if it’s not directly relevant.

If you ask this “Golden Gate Claude” how to spend $10, it will recommend using it to drive across the Golden Gate Bridge and pay the toll. If you ask it to write a love story, it’ll tell you a tale of a car who can’t wait to cross its beloved bridge on a foggy day. If you ask it what it imagines it looks like, it will likely tell you that it imagines it looks like the Golden Gate Bridge.

For a short time, we’re making this model available for everyone to interact with. You can talk to “Golden Gate Claude” on claude.ai (just click the Golden Gate logo on the right-hand side). Please bear in mind that this is a research demonstration only, and that this particular model might behave in some unexpected—even jarring—ways.

Our goal is to let people see the impact our interpretability work can have. The fact that we can find and alter these features within Claude makes us more confident that we’re beginning to understand how large language models really work. This isn’t a matter of asking the model verbally to do some play-acting, or of adding a new “system prompt” that attaches extra text to every input, telling Claude to pretend it’s a bridge. Nor is it traditional “fine-tuning,” where we use extra training data to create a new black box that tweaks the behavior of the old black box. This is a precise, surgical change to some of the most basic aspects of the model’s internal activations.

As we describe in our paper, we can use these same techniques to change the strength of *safety-related* features—like those related to dangerous computer code, criminal activity, or deception. With further research, we believe this work could help make AI models safer.