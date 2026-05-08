---
title: 'CLAMP: Contrastive Learning for 3D Multi-View Action-Conditioned Robotic Manipulation
  Pretraining'
source: https://arxiv.org/abs/2602.00937
author:
- '[[I-Chun Arthur Liu, Krzysztof Choromanski, Sandy Huang, Connor Schenck]]'
published: '2026-05-07'
created: '2026-05-08'
description: 'arXiv:2602.00937v3 Announce Type: replace-cross Abstract: Leveraging
  pre-trained 2D image representations in behavior cloning policies has achieved great
  success and has become a standard approach for robotic manipulation. However, such
  representations fail to capture the 3D spatial information about objects and scenes
  that is essential for precise manipulation. In this work, we introduce Contrastive
  Learning for 3D Multi-View Action-Conditioned Robotic Manipulation Pretraining (CLAMP),
  a novel 3D pre-training framework that utilizes point clouds and robot actions.
  From the merged point cloud computed from RGB-D images and camera extrinsics, we
  re-render multi-view four-channel image observations with depth and 3D coordinates,
  including dynamic wrist views, to provide clearer views of target objects for high-precision
  manipulation tasks. The pre-trained encoders learn to associate the 3D geometric
  and positional information of objects with robot action patterns via contrastive
  learning on large-scale simulated robot trajectories. During encoder pre-training,
  we pre-train a Diffusion Policy to initialize the policy weights for fine-tuning,
  which is essential for improving fine-tuning sample efficiency and performance.
  After pre-training, we fine-tune the policy on a limited amount of task demonstrations
  using the learned image and action representations. We demonstrate that this pre-training
  and fine-tuning design substantially improves learning efficiency and policy performance
  on unseen tasks. Furthermore, we show that CLAMP outperforms state-of-the-art baselines
  across six simulated tasks and five real-world tasks. The project website and videos
  can be found at https://clamp3d.github.io/CLAMP/.'
tags:
- clippings
id: cebdf79be2de609a
source_type: academic_paper
tldr: CLAMP提出一种基于对比学习的3D多视图机器人操作预训练框架，利用点云和动作数据提升策略学习效率。
objective_summary: 该论文提出CLAMP框架，从RGB-D图像生成融合点云并重新渲染多视图四通道图像，通过对比学习将物体3D几何信息与机器人动作模式关联，预训练扩散策略后微调，在六个模拟和五个真实世界任务上超越现有基线方法。
event_type: framework_tools
epistemic_status: theoretical_claim
entities:
  companies: []
  technologies:
  - CLAMP
  - Diffusion Policy
  - contrastive learning
  - point clouds
  - RGB-D
  - behavior cloning
  - 3D multi-view
  key_people: []
key_logic_flow:
- CLAMP利用RGB-D图像和相机外参计算融合点云，并重新渲染多视图四通道图像观察（含动态腕部视图）以提供清晰的目标视角。
- 通过对比学习，预训练编码器将物体的3D几何与位置信息关联到机器人动作模式。
- 在编码器预训练的同时，预训练一个扩散策略（Diffusion Policy）用于初始化微调权重，从而提升微调样本效率和性能。
- 预训练完成后，使用少量任务演示数据对策略进行微调，利用已学习的图像和动作表示适应新任务。
- 实验结果显示CLAMP在六个模拟任务和五个真实世界任务上均超越现有最先进基线方法。
---

# Computer Science > Robotics

# Title:CLAMP: Contrastive Learning for 3D Multi-View Action-Conditioned Robotic Manipulation Pretraining

View PDF HTML (experimental)Abstract:Leveraging pre-trained 2D image representations in behavior cloning policies has achieved great success and has become a standard approach for robotic manipulation. However, such representations fail to capture the 3D spatial information about objects and scenes that is essential for precise manipulation. In this work, we introduce Contrastive Learning for 3D Multi-View Action-Conditioned Robotic Manipulation Pretraining (CLAMP), a novel 3D pre-training framework that utilizes point clouds and robot actions. From the merged point cloud computed from RGB-D images and camera extrinsics, we re-render multi-view four-channel image observations with depth and 3D coordinates, including dynamic wrist views, to provide clearer views of target objects for high-precision manipulation tasks. The pre-trained encoders learn to associate the 3D geometric and positional information of objects with robot action patterns via contrastive learning on large-scale simulated robot trajectories. During encoder pre-training, we pre-train a Diffusion Policy to initialize the policy weights for fine-tuning, which is essential for improving fine-tuning sample efficiency and performance. After pre-training, we fine-tune the policy on a limited amount of task demonstrations using the learned image and action representations. We demonstrate that this pre-training and fine-tuning design substantially improves learning efficiency and policy performance on unseen tasks. Furthermore, we show that CLAMP outperforms state-of-the-art baselines across six simulated tasks and five real-world tasks. The project website and videos can be found at this https URL.

### Current browse context:

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.