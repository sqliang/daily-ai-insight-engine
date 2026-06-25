---
title: A low-carbon computing platform from your retired phones
source: https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/
author:
- '[[vikas-sharma]]'
published: '2026-06-13'
created: '2026-06-14'
description: 'Article URL: https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/
  Comments URL: https://news.ycombinator.com/item?id=48515336 Points: 288 # Comments:
  152'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 0fc7ad260e9ac9bb
source_type: community_discussion
tldr: 谷歌与加州大学圣地亚哥分校利用废旧手机搭建低碳计算集群，计划部署2000台Pixel手机
objective_summary: 加州大学圣地亚哥分校研究人员在谷歌支持下，将废旧智能手机主板提取后组成集群，重新部署为通用计算平台。计划部署2000台Pixel手机组成的数据中心，预计2026年秋季启动。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - University of California San Diego
  - AWS
  technologies:
  - Kubernetes
  - Android
  - Linux
  key_people:
  - Jennifer Switzer
  - David Patterson
  - Ryan Kastner
  - Patrick Pannuto
key_logic_flow:
- 计算机碳足迹由运营碳（使用能耗）和隐含碳（硬件制造）两部分构成，其中制造环节的碳排放更难解决。
- 加州大学圣地亚哥分校研究人员提出"手机集群计算"方案，将废旧智能手机主板提取后组成集群重新部署为通用计算平台。
- 现代智能手机单线程性能已媲美甚至超越多核服务器，但内存容量（8-12GB）和核心数量有限，需针对适合的应用场景。
- 25-50台手机的性能相当于一台现代服务器，项目使用Kubernetes管理容器化应用，将手机组织为自管理集群。
- 研究团队计划部署2000台Pixel手机的计算集群，预计可同时支持100门计算机科学课程的作业评测需求。
- 该部署还将作为消费级硬件在持续使用下可靠性的测试平台，完整系统预计2026年秋季上线。
extract_result: success
---

June 12, 2026

Jennifer Switzer, Visiting Postdoctoral Researcher, and David Patterson, Fellow, Google

With support from Google, Researchers at the University of California San Diego are building a useful second-life for consumer smartphones.

The carbon footprint of computing is a key sustainability challenge. It is driven by two major sources: *operational carbon* reflects emissions from energy consumed during use, and *embodied carbon* encompasses emissions associated with hardware manufacturing. While operational carbon is often addressed with efforts such as improved energy efficiency and using clean energy, the manufacturing footprint represents a more complex hurdle.

To address this, researchers at the University of California San Diego are building a pathway for the second life of phones through the exploration of “phone cluster computing.” This is a process whereby the motherboards of retired smartphones are extracted, collected into clusters, and redeployed as a general-purpose computing platform. With Google’s support, the university plans to deploy a datacenter built from 2,000 Pixel smartphones that will provide hundreds of researchers and students with low-cost, low-carbon cloud computing, reducing the need for newly-manufactured hardware and their associated emissions.

On average, people replace their phone every four years. This is generally driven by people’s desire for a new device, including for the functionalities provided by new models. Many replaced phones, however, have their core compute functionalities intact and are still relatively powerful computers with integrated processors, accelerators, memory, and storage. While an old phone might no longer be of interest to its first purchaser, putting it back in service can directly reduce the environmental footprint of computing by avoiding the need for further raw material extraction.

This blog discusses a novel strategy: *re-deploying unwanted smartphones for cloud computing applications.*

The single-threaded performance of modern smartphones’ performance processor cores is on-par with or better than those of modern multicore servers (see figure below). The most significant difference between a smartphone and a server is their size: servers contain dozens of powerful multithreaded processor cores and a huge memory capacity, while a smartphone has a handful of heterogeneous processor cores and 8-12GB of memory. One of the key challenges, then, is to target applications that fit into, or can be made to fit into, the capacity of a smartphone.

Redeploying unmodified consumer smartphones in a datacenter environment would be hazardous and inefficient. Smartphones’ compute elements are wrapped in components that aren’t needed in the server context — display, battery, chassis, and peripheral hardware like cameras. In addition to taking up valuable space, some components, such as batteries, contain materials not rated for a datacenter environment.

Prior to deployment, smartphones must be processed to remove all but the motherboard, which contains the core compute functionality. Note that the motherboard is responsible for the largest fraction of embodied carbon (approximately 50% based on internal carbon footprinting assessments), so this effort targets the most impactful components.

The Android operating system (OS) is already based on Linux, but the mobile-oriented Android userspace must be replaced with a general-purpose Linux distro. Updating the OS doesn't just get programmability; it also switches off many of the protections that are important for consumer devices, but unnecessary for cloud computing. For example, phones have a “low memory killer” daemon, which throttles memory-hungry applications.

The challenge of orchestrating jobs across the large number of devices that are needed to meet the performance of a traditional server — SPEC benchmarking results indicate that 25-50 phones equate to a modern server — is addressed by the use of containerized applications managed by Kubernetes. The phones are organized into self-managing clusters of 25-50 devices.

At many universities, an abundance of EdTech, grading, and research applications are already being run on the cloud. These applications range from tiny machines for hosting Jupyter notebooks to expensive GPU-based servers for parallel computing classes. The vast majority of these applications are within the capabilities of a single smartphone to host, with the standard grading backend running on small cloud instances such as AWS’ t3.micro (2 vCPU, 1 GB memory).

Researchers at the University of California San Diego are planning a 2,000-phone computing cluster to support computer science classes such as Parallel Computation and Systems Programming. Early experiments show that even a moderately-sized cluster of 20 phones is capable of supporting peak submission rates for a 75+ student class, with grading latencies below the default AWS backend. A 2,000 phone deployment will be capable of supporting a hundred such classes at once.

In addition to the direct benefit of providing 50 server-equivalents worth of compute at a fraction of the usual cost, the deployment will also act as a testbed for smartphone-based computing at scale. In particular, the project will investigate the reliability of consumer-grade hardware under sustained use. The full system is expected to launch in Fall 2026.

Read more about our approach to reducing carbon emissions associated with consumer electronics in our Consumer Hardware Carbon Reduction Guide.

*This projected was supported by Googlers Efren Robles, Federico Centola, Nischal Agarwal, Rajiv Andrade, Manoj Vishwanathan, Ron Vered, Behnam Heydarshahi, Karina Repetz, Ted Briggs, Julie Rapoport, David Bourne, and Tom Kennedy. UC San Diego collaborators include Aramesh Ranganathan, Chris Crutchfield, Gabriel Marcano, Computer Science Prof. Ryan Kastner, and Computer Science Prof. Patrick Pannuto.*