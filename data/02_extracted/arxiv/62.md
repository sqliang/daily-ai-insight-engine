---
title: Example-Based Object Detection
source: https://arxiv.org/abs/2605.04501
author:
- '[[ZhiXin Sun]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2605.04501v1 Announce Type: cross Abstract: In recent years, object
  detection has achieved significant progress, especially in the field of open-vocabulary
  object detection. Unlike traditional methods that rely on predefined categories,
  open-vocabulary approaches can detect arbitrary objects based on human-provided
  prompts. With the advancement of prompt-based detection techniques, models such
  as SAM3 can even outperform some category-specific detectors trained on particular
  datasets without requiring additional training on those datasets. However, despite
  these advancements, false positives and false negatives still occur. In practical
  engineering applications, persistent misdetections or missed detections of the same
  object are unacceptable. Yet retraining the model every time such errors occur incurs
  substantial costs in terms of human effort, computational resources, and time. Therefore,
  how to leverage existing false positive and false negative samples to prevent such
  errors from recurring remains a highly challenging and urgent problem. To address
  this issue, we propose EBOD (Example-Based Object Detection), which integrates a
  prompt-based detector (SAM3) with robust feature matching modules (DINOv3 and LightGlue).
  The proposed framework effectively suppresses the repeated occurrence of false positives
  and false negatives by leveraging previous error examples, without requiring additional
  model retraining. Code is available at https://github.com/sunzx97/examples_based_object_detection.'
tags:
- clippings
id: efc7dfa66f4a631e
source_type: academic_paper
tldr: EBOD 框架利用先前错误样本抑制目标检测中的重复误检和漏检，无需重新训练模型。
objective_summary: 该论文提出 EBOD 框架，将提示式检测器 SAM3 与特征匹配模块 DINOv3 和 LightGlue 结合，利用历史误检和漏检样本作为参考，在不重新训练模型的前提下抑制同类错误重复出现。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - EBOD
  - SAM3
  - DINOv3
  - LightGlue
  key_people: []
key_logic_flow:
- 现有开放词汇目标检测方法（如 SAM3）虽已取得进展，但在实际工程应用中仍存在反复出现误检和漏检的问题。
- 每次出现检测错误就重新训练模型在人力、算力和时间上成本过高，不切实际。
- EBOD 框架将基于提示的检测器 SAM3 与鲁棒特征匹配模块 DINOv3 和 LightGlue 集成，利用错误样本作为参考来抑制错误。
- 该方法无需额外模型训练即可有效防止同类误检和漏检的重复发生。
- 论文提供了代码开源链接，便于复现和验证。
---

# Computer Science > Computer Vision and Pattern Recognition

# Title:Example-Based Object Detection

View PDF HTML (experimental)Abstract:In recent years, object detection has achieved significant progress, especially in the field of open-vocabulary object detection. Unlike traditional methods that rely on predefined categories, open-vocabulary approaches can detect arbitrary objects based on human-provided prompts. With the advancement of prompt-based detection techniques, models such as SAM3 can even outperform some category-specific detectors trained on particular datasets without requiring additional training on those datasets. However, despite these advancements, false positives and false negatives still occur. In practical engineering applications, persistent misdetections or missed detections of the same object are unacceptable. Yet retraining the model every time such errors occur incurs substantial costs in terms of human effort, computational resources, and time. Therefore, how to leverage existing false positive and false negative samples to prevent such errors from recurring remains a highly challenging and urgent problem. To address this issue, we propose EBOD (Example-Based Object Detection), which integrates a prompt-based detector (SAM3) with robust feature matching modules (DINOv3 and LightGlue). The proposed framework effectively suppresses the repeated occurrence of false positives and false negatives by leveraging previous error examples, without requiring additional model retraining. Code is available at this https URL.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.