---
title: NVIDIA and AWS Collaborate to Bring AI to Production at Scale
source: https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale/
author:
- '[[Josiah Byers]]'
published: '2026-06-24'
created: '2026-06-26'
description: Building AI systems at scale is demanding, requiring low-latency inference,
  fast vector search, strong GPU price-performance and infrastructure that can grow
  without multiplying operational complexity. NVIDIA’s latest work with Amazon Web
  Services (AWS) addresses each of those constraints. Across Amazon OpenSearch and
  Amazon EC2, NVIDIA AI infrastructure is giving enterprises more practical paths
  to deploy [&#8230;]
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: e7cad40fb53bcdfe
source_type: tech_blog
tldr: NVIDIA 与 AWS 合作推出搭载 RTX PRO 4500 Blackwell GPU 的 Amazon EC2 G7 实例，并将 NVIDIA
  cuVS 驱动的 GPU 向量索引设为 Amazon OpenSearch Serverless 的默认计算方案，以降低企业将 AI 部署到生产环境的复杂度。
objective_summary: NVIDIA 在其官方博客宣布与 Amazon Web Services 合作，推出基于 NVIDIA RTX PRO 4500
  Blackwell Server Edition GPU 的 Amazon EC2 G7 实例，相比 G6 实例提供最高 4.6 倍 AI 推理性能和 2.1
  倍图形性能，支持 AI 推理、图形渲染、数据分析等多种工作负载。同时，NVIDIA 将 cuVS 库集成到 Amazon OpenSearch Serverless
  中，使 GPU 加速向量索引成为所有向量集合的默认计算选项，用于支持智能体 AI 工作负载。AWS 还获得了 NVIDIA GB300 的 Exemplar Cloud
  状态认证，确保训练工作负载的峰值优化性能。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Amazon Web Services (AWS)
  technologies:
  - NVIDIA RTX PRO 4500 Blackwell Server Edition
  - NVIDIA cuVS
  - NVIDIA cuDF
  - Amazon EC2 G7
  - Amazon OpenSearch Serverless
  - Amazon EMR
  - Amazon EKS
  - Amazon ECS
  - Amazon SageMaker AI
  - EFA
  - NVMe SSD
  - NVIDIA GB300
  key_people: []
key_logic_flow:
- NVIDIA 与 AWS 合作推出 Amazon EC2 G7 实例，搭载 NVIDIA RTX PRO 4500 Blackwell Server Edition
  GPU，覆盖 AI 推理、图形、视频、空间计算和数据分析等混合工作负载。
- G7 实例相比上一代 G6 实例提供最高 4.6 倍 AI 推理性能和 2.1 倍图形性能，支持最多 8 块 GPU、256GB GPU 显存、700 Gbps
  EFA 网络和 7.6TB 本地 NVMe SSD 存储。
- G7 实例通过 AWS Deep Learning AMIs、Amazon EMR、Amazon EKS、Amazon ECS 等渠道提供，即将登陆 Amazon
  SageMaker AI。
- NVIDIA cuVS 库被集成到 Amazon OpenSearch Serverless 中，使 GPU 加速向量索引成为所有向量集合的默认计算选项，无需客户管理底层基础设施。
- AWS 获得了 NVIDIA GB300 的 Exemplar Cloud 状态认证，表明 AWS 基础设施可为训练工作负载提供峰值优化性能。
extract_result: success
object_mentions:
- object_type: product
  name: Amazon EC2 G7 instances
  canonical_name: Amazon EC2 G7
  url: https://aws.amazon.com/ec2/instance-types/g7/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Amazon EC2 G7 instances bring NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs
    to AWS for AI inference, graphics, spatial computing and GPU-accelerated data
    analytics.
  - Compared with G6 instances, G7 delivers up to 4.6x AI inference performance, up
    to 2.1x graphics performance and significantly faster GPU-accelerated data analytics.
  - G7 instances support up to eight GPUs, 256GB of total GPU memory, 700 Gbps of
    EFA-enabled networking and up to 7.6TB of local NVMe SSD storage.
  article_id: e7cad40fb53bcdfe
- object_type: product
  name: NVIDIA RTX PRO 4500 Blackwell Server Edition
  canonical_name: NVIDIA RTX PRO 4500 Blackwell Server Edition GPU
  url: https://www.nvidia.com/en-us/design-visualization/rtx-pro/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs power the new Amazon EC2 G7
    instances for multi-workload AI inference, graphics, spatial computing and data
    analytics.
  - G7 instances deliver up to 4.6x AI inference performance compared with G6 instances,
    driven by the RTX PRO 4500 Blackwell Server Edition GPUs.
  article_id: e7cad40fb53bcdfe
- object_type: project
  name: NVIDIA cuVS
  canonical_name: NVIDIA cuVS
  url: https://developer.nvidia.com/cuvs
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - The next generation of Amazon OpenSearch Serverless uses GPU-accelerated vector
    indexing, powered by NVIDIA cuVS, as the default compute choice for all vector
    collections.
  - NVIDIA cuVS library accelerates the retrieval layer by making GPU-powered vector
    indexing the default in OpenSearch Serverless.
  article_id: e7cad40fb53bcdfe
- object_type: product
  name: Amazon OpenSearch Serverless
  canonical_name: Amazon OpenSearch Serverless
  url: https://aws.amazon.com/opensearch-service/features/serverless/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - The next generation of Amazon OpenSearch Serverless powers agentic AI and dynamic
    workloads with no infrastructure management required.
  - Amazon OpenSearch Serverless uses GPU-accelerated vector indexing, powered by
    NVIDIA cuVS, as the default compute choice for all vector collections.
  article_id: e7cad40fb53bcdfe
- object_type: product
  name: NVIDIA GB300
  canonical_name: NVIDIA GB300
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - AWS achieved NVIDIA Exemplar Cloud status for NVIDIA GB300, ensuring customers
    receive peak optimized performance for their training workloads.
  article_id: e7cad40fb53bcdfe
- object_type: project
  name: NVIDIA cuDF
  canonical_name: NVIDIA cuDF
  url: https://github.com/rapidsai/cudf
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - G7 instances deliver significantly faster GPU-accelerated data analytics on Amazon
    EMR using the NVIDIA cuDF library for Apache Spark workloads.
  article_id: e7cad40fb53bcdfe
---

Building AI systems at scale is demanding, requiring low-latency inference, fast vector search, strong GPU price-performance and infrastructure that can grow without multiplying operational complexity.

NVIDIA’s latest work with Amazon Web Services (AWS) addresses each of those constraints. Across Amazon OpenSearch and Amazon EC2, NVIDIA AI infrastructure is giving enterprises more practical paths to deploy AI at production scale.

EC2 G7 instances powered by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs expand the compute layer for AI, graphics, video and data analytics workloads, while the NVIDIA cuVS library accelerates the retrieval layer by making GPU-powered vector indexing the default in OpenSearch Serverless. And with AWS achieving NVIDIA Exemplar Cloud status for NVIDIA GB300, customers can trust they’re receiving peak optimized performance for their training workloads.

**NVIDIA RTX PRO 4500 Blackwell Server Edition Multi-Workload GPUs Power New Amazon EC2 G7 Instances**

Amazon EC2 G7 instances bring NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs to AWS for AI inference, graphics, spatial computing and GPU-accelerated data analytics — delivering a new instance type engineered for production workloads that need performance without the operational overhead of a customer-managed GPU platform.

Compared with G6 instances, G7 delivers up to 4.6x AI inference performance, up to 2.1x graphics performance and significantly faster GPU-accelerated data analytics on Amazon EMR using the NVIDIA cuDF library for Apache Spark workloads.

With support for up to eight GPUs, 256GB of total GPU memory, 700 Gbps of EFA-enabled networking and up to 7.6TB of local NVMe SSD storage — across one-, two-, four- and eight- GPU configurations plus bare metal, coming soon — G7 instances let customers right-size infrastructure for their workloads instead of over-provisioning for them.

The platform’s versatility means AI teams get lower-latency inference. Media and entertainment teams get high-resolution video workflows and rendering. Simulation, computer-aided design, virtual desktop infrastructure, gaming and spatial computing teams get the same instance type for graphics-intensive applications. And data teams can apply the GPU memory, local storage and networking improvements to analytics pipelines and vector database workloads.

G7 instances are accessible through AWS Deep Learning Amazon Machine Images (AMIs), Amazon Deep Learning Containers, Amazon EMR, Amazon EKS, Amazon ECS and graphics AMIs — and coming soon to Amazon SageMaker AI.

**NVIDIA cuVS Makes GPU-Accelerated Vector Search the Default in Amazon OpenSearch**

The next generation of Amazon OpenSearch Serverless powers agentic AI and dynamic workloads with no infrastructure management required. It uses GPU-accelerated vector indexing, powered by NVIDIA cuVS, as the default compute choice for all vector collections.