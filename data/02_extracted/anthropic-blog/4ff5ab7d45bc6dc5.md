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
tldr: Anthropic发布可解释性研究：通过调整神经网络特征强度精确操控Claude行为
objective_summary: Anthropic发布大语言模型可解释性研究论文，在Claude 3 Sonnet中发现数百万个概念特征。通过调高"金门大桥"特征的激活强度，实现了对模型行为的精确手术式操控，并认为该技术可用于提升AI安全性。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies:
  - Claude 3 Sonnet
  key_people: []
key_logic_flow:
- Anthropic发布了大语言模型可解释性研究论文，首次绘制出Claude 3 Sonnet神经网络内部的数百万个概念特征
- 研究团队定位了对应"金门大桥"概念的特定神经元组合，可识别并调整其激活强度
- 调高"金门大桥"特征后，Claude的回答会不由自主地围绕该主题展开，即使用10美元的推荐也变成过大桥缴费
- 该技术是对模型内部激活的精确定位手术式修改，不同于提示词工程、系统提示或传统微调
- 该技术同样适用于调整安全相关特征（危险代码、犯罪活动、欺骗等），有望用于提升AI模型安全性
- 该模型作为研究演示限时24小时在线，供公众交互体验
extract_result: success
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