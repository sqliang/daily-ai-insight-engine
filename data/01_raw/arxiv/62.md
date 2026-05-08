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