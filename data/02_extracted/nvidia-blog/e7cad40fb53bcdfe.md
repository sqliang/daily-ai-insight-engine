---
title: NVIDIA and AWS Collaborate to Bring AI to Production at Scale
source: https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale/
author:
- '[[Josiah Byers]]'
published: '2026-06-24'
created: '2026-06-24'
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
tldr: NVIDIA与AWS合作推出EC2 G7实例和GPU加速OpenSearch向量搜索
objective_summary: NVIDIA与AWS宣布合作，推出搭载RTX PRO 4500 Blackwell GPU的EC2 G7实例，AI推理性能较G6提升4.6倍；同时将cuVS库集成到OpenSearch
  Serverless实现GPU向量搜索加速；AWS获NVIDIA GB300 Exemplar Cloud认证。
event_type: infrastructure_update
epistemic_status: pr_statement
entities:
  companies:
  - NVIDIA
  - Amazon Web Services
  - AWS
  technologies:
  - RTX PRO 4500 Blackwell Server Edition
  - cuVS
  - OpenSearch Serverless
  - EC2 G7
  - cuDF
  - EFA
  - NVMe SSD
  - GB300
  key_people: []
key_logic_flow:
- NVIDIA与AWS合作，针对低延迟推理、快速向量搜索和GPU性价比三大约束，推动AI生产级规模化部署。
- AWS推出搭载NVIDIA RTX PRO 4500 Blackwell Server Edition GPU的EC2 G7实例，支持AI推理、图形、空间计算和数据加速分析等多类型工作负载。
- EC2 G7实例相比G6实例，AI推理性能提升最高4.6倍，图形性能提升最高2.1倍，并支持最多8块GPU、256GB GPU内存、700Gbps EFA网络和7.6TB本地NVMe
  SSD存储。
- NVIDIA cuVS库成为Amazon OpenSearch Serverless向量集合的默认计算选择，实现GPU加速向量索引，无需客户管理基础设施。
- AWS获得NVIDIA GB300 Exemplar Cloud认证，表明其训练工作负载达到NVIDIA认可的峰值优化性能。
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