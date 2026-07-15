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
tldr: NVIDIA 与 AWS 合作推出 EC2 G7 实例和 cuVS 加速库，提升 AI 生产级部署性能
objective_summary: NVIDIA 与 AWS 合作推出搭载 RTX PRO 4500 Blackwell GPU 的 EC2 G7 实例（AI 推理性能提升
  4.6 倍），并将 NVIDIA cuVS 库集成至 Amazon OpenSearch Serverless 实现 GPU 加速向量搜索作为默认计算选项。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Amazon Web Services (AWS)
  technologies:
  - NVIDIA RTX PRO 4500 Blackwell Server Edition
  - Amazon EC2 G7
  - NVIDIA cuVS
  - Amazon OpenSearch Serverless
  - NVIDIA cuDF
  - Amazon EMR
  key_people: []
key_logic_flow:
- NVIDIA 与 AWS 合作推出 EC2 G7 实例，搭载 RTX PRO 4500 Blackwell Server Edition GPU，覆盖 AI 推理、图形渲染、空间计算和数据分析等工作负载
- EC2 G7 相比 G6 实例提供高达 4.6 倍 AI 推理性能和 2.1 倍图形性能，支持最多 8 颗 GPU、256GB GPU 内存、700 Gbps
  EFA 网络和 7.6TB NVMe SSD 存储
- NVIDIA 将 cuVS 库集成至 Amazon OpenSearch Serverless，使 GPU 加速向量索引成为所有向量集合的默认计算选择，面向智能体
  AI 和动态工作负载
- AWS 获得 NVIDIA GB300 Exemplar Cloud 认证，表明其训练工作负载获得峰值优化性能保障
- G7 实例通过 AWS Deep Learning AMIs、Amazon EMR、EKS、ECS 等渠道可用，即将支持 Amazon SageMaker AI
extract_result: success
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