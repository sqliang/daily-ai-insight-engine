---
title: How To Scale Your Model
source: https://jax-ml.github.io/scaling-book/?utm_source=tldrai
author: null
published: null
created: 2026-05-07
description: 'Training LLMs often feels like alchemy, but understanding and optimizing
  the performance of your models doesn''t have to. This book aims to demystify the
  science of scaling language models: how TPUs (and GPUs) work and how they communicate
  with each other, how LLMs run on real hardware, and how to parallelize your models
  during training and inference so they run efficiently at massive scale. If you''ve
  ever wondered “how expensive should this LLM be to train” or “how much memory do
  I need to serve this model myself” or “what''s an AllGather”, we hope this will
  be useful to you.'
tags:
- clippings
id: 4eaeb8d96a1a9adf
source_type: news_media
tldr: JAX团队发布《How To Scale Your Model》在线技术书籍，系统讲解TPU/GPU上LLM训练与推理的并行化策略与性能优化方法。
objective_summary: Google JAX团队在jax-ml.github.io上线了《How To Scale Your Model》在线技术书籍。全书共12章，从roofline分析模型出发，深入讲解TPU/GPU硬件架构、矩阵分片乘法、Transformer参数量与FLOPs计算，
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Google
  - Meta
  technologies:
  - JAX
  - TPU
  - GPU
  - Transformer
  - XLA
  - FSDP
  - Megatron
  - ZeRO
  - Pipeline Parallelism
  - Tensor Parallelism
  - Data Parallelism
  - Expert Parallelism
  - KV Cache
  - Roofline Analysis
  - Gradient Accumulation
  - Rematerialisation
  key_people:
  - James Bradbury
  - Blake Hechtman
key_logic_flow:
- 该书核心主张：理解硬件工作原理后，即使在数万芯片规模下，模型性能优化也不再是黑魔法，而是可以遵循相对简单的原则
- 第一部分建立roofline分析基础框架——算法性能的瓶颈始终来自计算、通信和内存三者之一，以此为全书提供统一的分析语言
- 第二部分深入TPU架构：单芯片的计算单元与内存层次、多芯片间互联拓扑与带宽约束，以及如何在不同分片布局下高效完成矩阵乘法
- 第四部分对Transformer架构进行逐层拆解，精确计算每个矩阵乘法的参数量与FLOPs，为后续并行化决策提供量化依据
- 第五至第八章是全书核心：系统对比四种并行策略的适用场景与通信开销，并引入重计算、ZeRO优化器分片、主机卸载、梯度累积等内存优化手段
- 实战部分以LLaMA 3为例，在TPU v5e上估算训练成本与时间、推理延迟与吞吐量的权衡，最后通过JAX+TensorBoard分析器教授性能调试方法；第十二章新增GPU章节作为补充
pipeline_stage: fact_extracted
impact_score:
  score: 6.0
  reason: 该在线技术书籍填补了大规模模型训练与推理优化领域的系统性知识空白。此前相关知识散落于学术论文、博客和技术报告中，JAX团队将其整合为12章结构化教材，涵盖roofline分析、TPU/GPU硬件架构、四种并行策略对比及实战案例，是ML基础设施领域的重要教育贡献。短期将显著降低工程师进入大规模训练优化的门槛，但本质是知识整合与传播，而非新产品发布或范式级研究突破，冲击力限于技术教育层面。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 系统化的TPU/GPU并行训练与推理优化实战指南，从硬件原理到LLaMA 3完整案例的端到端教学
hype_assessment:
  level: low
  reason: 全书使用克制、务实的技术语言，明确反对将性能优化视为'黑魔法'，强调理解硬件后遵循相对简单的原则即可。未出现'颠覆'、'革命性'等PR词汇，核心主张是'理解硬件工作原理后优化不再神秘'，属于实打实的工程技术教育内容。
information_entropy: high
domain_disruption:
  technical_innovation: 本书的技术突破不在于提出新算法或新架构，而在于将roofline分析、并行策略（数据/张量/流水线/专家并行）、内存优化（重计算、ZeRO分片、主机卸载）等分散知识整合为统一的分析框架，并以LLaMA
    3+TPU v5e为完整案例进行端到端推演，形成可复用的工程方法论。新增的GPU章节（第12章）进一步扩展了跨硬件平台的适用性。
  business_model: 作为免费开放在线书籍，其商业模式影响在于降低企业自研大模型训练基础设施的人才门槛，使中小型AI团队也能系统掌握原本仅存在于Google/
    Meta等大厂内部的知识体系，间接推动训练优化工具的普及和云TPU/GPU资源的更高效利用。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: 该书籍建立了以roofline分析为核心的系统化硬件性能优化方法论，将'计算-通信-内存'三者权衡作为统一分析语言，这些原则具有跨代际的持久性——无论未来硬件架构如何演进，瓶颈分析框架不会过时。但作为教育性资源而非产品或平台，其复利效应依赖于社区持续更新和JAX/TPU生态的扩张速度。若Google持续维护更新（类比NVIDIA
    CUDA文档生态），3-5年后有望成为LLM系统优化的'龙书'级参考标准；若一次性发布后断更，则价值随时间衰减。目前定位为细分赛道的重要基础设施，长期地位仍需验证。
value_capture_layer: hardware_compute
moat_impact: democratizes_access
key_beneficiaries:
- Google
- JAX
- NVIDIA
- ML工程师社区
competitive_casualty:
- 闭源LLM训练优化工具/课程平台
- 以模型优化咨询为核心业务的小型服务公司
market_opportunities:
- AI基础设施工具创业者可基于该书的roofline分析与并行策略框架，开发跨硬件平台的模型训练成本估算与性能调优SaaS工具，填补当前市场在"训练前成本预测"环节的空白，帮助企业在GPU/TPU采购决策前精准评估资源需求
- 企业AI团队可将该书作为系统化培训教材，结合内部模型架构进行实战演练，系统性提升ML工程师的硬件感知编程能力，直接降低大模型训练推理的试错成本与资源浪费
- 云计算厂商与AI芯片公司可借鉴该书的"硬件优先"方法论，围绕自家硬件产品编写类似的结构化性能优化指南，作为开发者生态建设的差异化竞争手段，降低新硬件平台的采纳门槛
risk_matrix:
  regulatory: 无
  technological: 该书以TPU/JAX为主要视角，GPU章节为后期补充且深度有限；若团队技术栈以CUDA/PyTorch为主，核心方法论虽可迁移但具体实现细节需自行适配，存在学习转化成本；JAX生态社区规模与第三方库丰富度仍远不及PyTorch
  competitive: Google通过此书系统性强化JAX+TPU生态的开发者教育，可能加速部分高性能计算场景下PyTorch用户向JAX迁移，对开源PyTorch生态和商业GPU云服务商构成长期竞争压力；同时大幅降低TPU使用门槛，可能逐步改变AI训练芯片的市场格局
  ethical: 无
  additional:
  - 大规模模型训练门槛的系统性降低可能加速全球AI军备竞赛，使更多中小机构具备训练千亿参数模型的能力，间接推高AI安全治理的复杂度与能源消耗的外部性风险
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: strategic_invest
---

A Systems View of LLMs on TPUs

Training LLMs often feels like alchemy, but understanding and optimizing the performance of your models doesn't have to. This book aims to demystify the science of scaling language models: how TPUs (and GPUs) work and how they communicate with each other, how LLMs run on real hardware, and how to parallelize your models during training and inference so they run efficiently at massive scale. If you've ever wondered “how expensive should this LLM be to train” or “how much memory do I need to serve this model myself” or “what's an AllGather”, we hope this will be useful to you.

![](https://jax-ml.github.io/scaling-book/assets/img/dragon.png)

Much of deep learning still boils down to a kind of black magic, but optimizing the performance of your models doesn’t have to — even at huge scale! Relatively simple principles apply everywhere — from dealing with a single accelerator to tens of thousands — and understanding them lets you do many useful things:

- Ballpark how close parts of your model are to their theoretical optimum.
- Make informed choices about different parallelism schemes at different scales (how you split the computation across multiple devices).
- Estimate the cost and time required to train and run large Transformer models.
- Design algorithms that take advantage of [specific](https://arxiv.org/abs/2205.14135) [hardware](https://arxiv.org/abs/1911.02150) [affordances](https://arxiv.org/abs/2007.00072).
- Design hardware driven by an explicit understanding of what limits current algorithm performance.

**Expected background:** We’re going to assume you have a basic understanding of LLMs and the Transformer architecture but not necessarily how they operate at scale. You should know the basics of LLM training and ideally have some basic familiarity with JAX. Some useful background reading might include [this blog post](https://jalammar.github.io/illustrated-transformer/) on the Transformer architecture and [the original Transformer paper](https://arxiv.org/abs/1706.03762). Also check out [this list](https://jax-ml.github.io/scaling-book/conclusion#further-reading) for more useful concurrent and future reading.

**Goals & Feedback:** By the end, you should feel comfortable estimating the best parallelism scheme for a Transformer model on a given hardware platform, and roughly how long training and inference should take. If you don’t, email us or leave a comment! We’d love to know how we could make this clearer.

You might also enjoy reading the new [Section 12](https://jax-ml.github.io/scaling-book/gpus) on NVIDIA GPUs!

### Why should you care?

Three or four years ago, I don’t think most ML researchers would have needed to understand any of the content in this book. But today even “small” models run so close to hardware limits that doing novel research requires you to think about efficiency at scale.

[^1]

**A 20% win on benchmarks is irrelevant if it comes at a 20% cost to roofline efficiency.** Promising model architectures routinely fail either because they *can’t* run efficiently at scale or because no one puts in the work to make them do so.

**The goal of “model scaling” is to be able to increase the number of chips used for training or inference while achieving a proportional, linear increase in throughput.** This is known as “ *strong scaling* ”. Although adding additional chips (“parallelism”) usually decreases the computation time, it also comes at the cost of added communication between chips. When communication takes longer than computation we become “communication bound” and cannot scale strongly.

<sup>2</sup>

If we understand our hardware well enough to anticipate where these bottlenecks will arise, we can design or reconfigure our models to avoid them.

<sup>3</sup>

*Our goal in this book is to explain how TPU (and GPU) hardware works and how the Transformer architecture has evolved to perform well on current hardware. We hope this will be useful both for researchers designing new architectures and for engineers working to make the current generation of LLMs run fast.*

## High-Level Outline

The overall structure of this book is as follows:

[Section 1](https://jax-ml.github.io/scaling-book/roofline) explains roofline analysis and what factors can limit our ability to scale (communication, computation, and memory). [Section 2](https://jax-ml.github.io/scaling-book/tpus) and [Section 3](https://jax-ml.github.io/scaling-book/sharding) talk in detail about how TPUs work, both as individual chips and — of critical importance — as an interconnected system with inter-chip links of limited bandwidth and latency. We’ll answer questions like:

- How long should a matrix multiply of a certain size take? At what point is it bound by compute or by memory or communication bandwidth?
- How are TPUs wired together to form training clusters? How much bandwidth does each part of the system have?
- How long does it take to gather, scatter, or re-distribute arrays across multiple TPUs?
- How do we efficiently multiply matrices that are distributed differently across devices?
![](https://jax-ml.github.io/scaling-book/assets/img/pointwise-product.gif)

Figure: a diagram from Section 2 showing how a TPU performs an elementwise product. Depending on the size of our arrays and the bandwidth of various links, we can find ourselves compute-bound (using the full hardware compute capacity) or memory-bound (bottlenecked by memory loading).

Five years ago ML had a colorful landscape of architectures — ConvNets, LSTMs, MLPs, Transformers — but now we mostly just have the Transformer

- **Attention is all you need**  
	A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L. Kaiser, I. Polosukhin.  
	arXiv \[cs.CL\]. 2017.

\[1\]

. We strongly believe it’s worth understanding every piece of the Transformer architecture: the exact sizes of every matrix, where normalization occurs, how many parameters and FLOPs

<sup>4</sup>

are in each part. [Section 4](https://jax-ml.github.io/scaling-book/transformers) goes through this “Transformer math” carefully, showing how to count the parameters and FLOPs for both training and inference. This tells us how much memory our model will use, how much time we’ll spend on compute or comms, and when attention will become important relative to the feed-forward blocks.

![](https://jax-ml.github.io/scaling-book/assets/img/transformer-diagram.png)

Figure: a standard Transformer layer with each matrix multiplication (matmul) shown as a dot inside a circle. All parameters (excluding norms) are shown in purple. Section 4 walks through this diagram in more detail.

[Section 5: Training](https://jax-ml.github.io/scaling-book/training) and [Section 7: Inference](https://jax-ml.github.io/scaling-book/inference) are the core of this book, where we discuss the fundamental question: given a model of some size and some number of chips, how do I parallelize my model to stay in the “strong scaling” regime? This is a simple question with a surprisingly complicated answer. At a high level, there are 4 primary parallelism techniques used to split models over multiple chips (**data**, **tensor**, **pipeline**, and **expert**), and a number of other techniques to reduce the memory requirements (**rematerialisation**, **optimizer/model sharding (aka ZeRO)**, **host offload**, **gradient accumulation**). We discuss many of these here.

We hope by the end of these sections you should be able to choose among them yourself for new architectures or settings. [Section 6](https://jax-ml.github.io/scaling-book/applied-training) and [Section 8](https://jax-ml.github.io/scaling-book/applied-inference) are practical tutorials that apply these concepts to LLaMA 3, a popular open-source model.

Finally, [Section 9](https://jax-ml.github.io/scaling-book/profiling) and [Section 10](https://jax-ml.github.io/scaling-book/jax-stuff) look at how to implement some of these ideas in JAX and how to profile and debug your code when things go wrong. [Section 12](https://jax-ml.github.io/scaling-book/gpus) is a new section that dives into GPUs as well.

Throughout we try to give you problems to work for yourself. Please feel no pressure to read all the sections or read them in order. And please leave feedback. For the time being, this is a draft and will continue to be revised. Thank you!

*We’d like to acknowledge James Bradbury and Blake Hechtman who derived many of the ideas in this book.*

## Links to Sections

*This series is probably longer than it needs to be, but we hope that won’t deter you. The first three chapters are preliminaries and can be skipped if you’re already familiar with the material, although they introduce notation used later. The final three parts might be the most practically useful, since they explain how to work with real models.*

**Part 1: Preliminaries**

- [**Chapter 1: A Brief Intro to Roofline Analysis**](https://jax-ml.github.io/scaling-book/roofline). Algorithms are bounded by three things: compute, communication, and memory. We can use these to approximate how fast our algorithms will run.
- [**Chapter 2: How to Think About TPUs**](https://jax-ml.github.io/scaling-book/tpus). How do TPUs work? How does that affect what models we can train and serve?
- [**Chapter 3: Sharded Matrices and How to Multiply Them**](https://jax-ml.github.io/scaling-book/sharding). Here we explain model sharding and multi-TPU parallelism by way of our favorite operation: (sharded) matrix multiplications.

**Part 2: Transformers**

- [**Chapter 4: All the Transformer Math You Need to Know**](https://jax-ml.github.io/scaling-book/transformers). How many FLOPs does a Transformer use in its forward and backward pass? Can you calculate the number of parameters? The size of its KV caches? We work through this math here.
- [**Chapter 5: How to Parallelize a Transformer for Training**](https://jax-ml.github.io/scaling-book/training). FSDP. Megatron sharding. Pipeline parallelism. Given some number of chips, how do I train a model of a given size with a given batch size as efficiently as possible?
- [**Chapter 6: Training LLaMA 3 on TPUs**](https://jax-ml.github.io/scaling-book/applied-training). How would we train LLaMA 3 on TPUs? How long would it take? How much would it cost?
- [**Chapter 7: All About Transformer Inference**](https://jax-ml.github.io/scaling-book/inference). Once we’ve trained a model, we have to serve it. Inference adds a new consideration — latency — and changes up the memory landscape. We’ll talk about how disaggregated serving works and how to think about KV caches.
- [**Chapter 8: Serving LLaMA 3 on TPUs**](https://jax-ml.github.io/scaling-book/applied-inference). How much would it cost to serve LLaMA 3 on TPU v5e? What are the latency/throughput tradeoffs?

**Part 3: Practical Tutorials**

- [**Chapter 9: How to Profile TPU Code**](https://jax-ml.github.io/scaling-book/profiling). Real LLMs are never as simple as the theory above. Here we explain the JAX + XLA stack and how to use the JAX/TensorBoard profiler to debug and fix real issues.
- [**Chapter 10: Programming TPUs in JAX**](https://jax-ml.github.io/scaling-book/jax-stuff). JAX provides a bunch of magical APIs for parallelizing computation, but you need to know how to use them. Fun examples and worked problems.

**Part 4: Conclusions and Bonus Content**

- [**Chapter 11: Conclusions and Further Reading**](https://jax-ml.github.io/scaling-book/conclusion). Closing thoughts and further reading on TPUs and LLMs.
- [**Chapter 12: How to Think About GPUs**](https://jax-ml.github.io/scaling-book/gpus). A bonus section about GPUs, how they work, how they’re networked, and how their rooflines differ from TPUs.

### Footnotes

1. Historically, ML research has followed something of a tick-tock cycle between systems innovations and software improvements. Alex Krizhevsky had to write unholy CUDA code to make CNNs fast but within a couple of years, libraries like Theano and TensorFlow meant you didn't have to. Maybe that will happen here too and everything in this book will be abstracted away in a few years. But scaling laws have pushed our models perpetually to the very frontier of our hardware, and it seems likely that, for the foreseeable future, doing cutting-edge research will be inextricably tied to an understanding of how to efficiently scale models to large hardware topologies.
2. As your computation time decreases, you also typically face bottlenecks at the level of a single chip. Your shiny new TPU or GPU may be rated to perform 500 trillion operations-per-second, but if you aren't careful it can just as easily do a tenth of that if it's bogged down moving parameters around in memory. The interplay of per-chip computation, memory bandwidth, and total memory is critical to the scaling story.
3. Hardware designers face the inverse problem: building hardware that provides just enough compute, bandwidth, and memory for our algorithms while minimizing cost. You can imagine how stressful this "co-design" problem is: you have to bet on what algorithms will look like when the first chips actually become available, often 2 to 3 years down the road. The story of the TPU is a resounding success in this game. Matrix multiplication is a unique algorithm in the sense that it uses far more FLOPs per byte of memory than almost any other (N FLOPs per byte), and early TPUs and their systolic array architecture achieved far better perf / $ than GPUs did at the time they were built. TPUs were designed for ML workloads, and GPUs with their Tensor Cores are rapidly changing to fill this niche as well. But you can imagine how costly it would have been if neural networks had not taken off, or had changed in some fundamental way that TPUs (which are inherently less flexible than GPUs) could not handle.
4. FLoating point OPs, basically the total number of adds and multiplies required. While many sources take FLOPs to mean "operations per second", we use FLOPs/s to indicate that explicitly.

### References

### Miscellaneous

<sup>*</sup> Work done at Google DeepMind, now at MatX.

### Citation

For attribution in academic contexts, please cite this work as:

```
Austin et al., "How to Scale Your Model", Google DeepMind, online, 2025.
```

or as a BibTeX entry:

```
@article{scaling-book,
  title = {How to Scale Your Model},
   = {Austin, Jacob and Douglas, Sholto and Frostig, Roy and Levskaya, Anselm and Chen, Charlie and Vikram, Sharad
  and Lebron, Federico and Choy, Peter and Ramasesh, Vinay and Webson, Albert and Pope, Reiner},
  publisher = {Google DeepMind},
  howpublished = {Online},
  note = {Retrieved from https://jax-ml.github.io/scaling-book/},
  year = {2025}
}
```

[^1]: Attention is all you need  
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L. and Polosukhin, I., 2017. arXiv \[cs.CL\].