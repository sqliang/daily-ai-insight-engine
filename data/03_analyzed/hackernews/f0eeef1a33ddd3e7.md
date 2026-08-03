---
title: Pruning RAG context down to what the answer actually needs
source: https://www.kapa.ai/blog/how-we-prune-rag-context
author:
- '[[emil_sorensen]]'
published: '2026-07-06'
created: '2026-07-07'
description: 'Article URL: https://www.kapa.ai/blog/how-we-prune-rag-context Comments
  URL: https://news.ycombinator.com/item?id=48809354 Points: 103 # Comments: 19'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: f0eeef1a33ddd3e7
manifest_dates:
- '2026-07-07'
source_type: community_discussion
tldr: Kapa.ai 在 RAG 管道中引入了一个轻量 LLM 作为上下文修剪器，在检索器和生成器之间过滤掉约 68% 的检索块，同时保持约 96% 的召回率，每次查询成本降低约
  34%。
objective_summary: Kapa.ai 联合创始人 Lars Baltensperger 发表博客文章，介绍了该公司在其 AI 助手的 RAG 管道中新增的第三个步骤：在检索器和生成器之间插入一个小型
  LLM 作为上下文修剪器。该修剪器同时读取用户问题和所有检索到的文本块，按五级评分体系（ESSENTIAL 到 UNRELATED）对每个块评分，丢弃低于阈值的块。经过标注集评测和真实生产流量回放验证，该方案可丢弃约
  68% 的检索块，保持约 96% 的召回率，每次查询成本净降低约 34%，延迟增加约 0.7 秒。该功能默认在 Product Agent SDK 的知识库搜索中启用，并在检索
  API 和 MCP 服务器中可选使用。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - kapa.ai
  technologies:
  - RAG
  - LLM
  key_people:
  - Lars Baltensperger
key_logic_flow:
- Kapa.ai 发现检索到的文本块约占每次查询成本的 2/3，减少上下文块可以直接降低查询成本。
- 基于重排序分数设定固定截断阈值的方案不可行，因为重排序分数是排序依据而非绝对度量，跨查询无法校准。
- 基于锚点文档（anchor documents）的校准方案也因重排序器无法判断集合相关性而失败——一个块只有与其他块组合时才显示其价值。
- Kapa.ai 的解决方案是在重排序器和生成器之间加入一个轻量 LLM 调用，该模型同时查看问题和所有检索块，按五级评分体系对每个块独立评分，使用固定阈值决定保留或丢弃。
- 该方案在标注测试集上实现约 68% 的上下文压缩率和约 96% 的召回保持率，每次查询成本下降约 34%，延迟增加约 0.7 秒。
- 修剪功能默认在 Product Agent SDK 的知识库搜索中启用，并在检索 API 和 MCP 服务器中可选使用。
extract_result: success
object_mentions:
- object_type: company
  name: kapa.ai
  canonical_name: kapa.ai
  url: https://www.kapa.ai
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Kapa 构建能够回答涉及大型产品知识库的复杂问题的 AI 助手，涵盖技术文档、API 参考、PDF、论坛和支持线程等多种来源。
  - Kapa 在检索器和生成器之间加入了一个小型 LLM 作为上下文修剪器，该修剪器同时读取问题和所有检索块并评分。
  article_id: f0eeef1a33ddd3e7
- object_type: product
  name: Product Agent SDK
  canonical_name: kapa.ai Product Agent SDK
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 修剪功能默认在 Product Agent SDK 的知识库搜索中启用，客户可以在基于 Kapa 检索构建的 Agent 中使用该功能以减少上下文占用。
  article_id: f0eeef1a33ddd3e7
impact_score:
  score: 5.5
  reason: 该方案在 RAG 流水线中引入了一个轻量级 LLM 裁剪步骤，通过集合级评分而非点式评分，解决了点式重排器无法判断块间关系的根本缺陷。虽然并非范式转移级别的创新，但这是一项非常实用的工程优化——丢弃
    68% 上下文、保持 96% 召回率、净成本降低 34%，且有明确的设计决策记录（为什么点式重排器、锚定文档等方法都失效）。这一模式可能被 RAG 工程社区广泛借鉴，成为标准流水线组件，影响局部竞争格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 在几乎不损失召回率的前提下大幅降低 RAG 推理成本的实际工程方案
hype_assessment:
  level: low
  reason: 文章非常务实，没有使用'颠覆性''革命性'等 PR 词汇。作者明确列出了方案的局限性（增加约 0.7 秒延迟、需要小型模型、非旗舰模型可胜任），并坦诚解释了为什么点式重排器和锚定文档方法都行不通。所有性能数字均有来源（68%
    丢弃率、96% 召回率、34% 成本降低），透明度高。
information_entropy: high
domain_disruption:
  technical_innovation: 在 RAG 检索器与生成器之间引入集合级（listwise）LLM 裁剪步骤，使用五级评分体系（ESSENTIAL/CONTRIBUTING/SUPPORTING/TANGENTIAL/UNRELATED）对检索块进行上下文感知的集体评分，从根本上解决了点式交叉编码器（pointwise
    cross-encoder）无法判断块间集合关系的缺陷，这是对传统重排-截断范式的实质性改进。
  business_model: 该方案直接降低了 RAG 系统的每次查询成本（约 34%），使大知识库场景下的 AI 助手在成本结构上更具商业可行性。Kapa
    将其默认集成到 Product Agent SDK 中，形成了差异化的竞争壁垒——对于竞品而言，仅靠单纯增加重排器无法达到同样的成本-质量平衡。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: 该方案直击了点式重排器（pointwise cross-encoder）无法评估块间集合关系的根本缺陷，通过 listwise LLM 评分实现
    34% 净成本下降和 96% 召回率保留，已在生产环境中验证。其价值具有复利属性：(1) '检索→裁剪→生成'的三段式架构很可能成为 RAG 流水线的标准范式，具备广泛可复制性；(2)
    成本节约在大规模查询下呈线性放大效应；(3) 思路可自然扩展至多轮 agent 上下文窗口管理，应用边界不止于 RAG。但扣分项在于：核心方法论（listwise
    分级+固定阈值）的护城河较浅——提示词工程层面的创新容易被竞争对手快速复现和优化，且不构成平台级基础设施或网络效应。因此给予 7.0 分，作为细分赛道最佳实践具备持续价值，但尚未达到
    8+ 所需的不可替代平台壁垒。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Kapa.ai
- 采用 RAG 架构的企业客户
- 小型高效推理模型提供商（如 Groq、Together AI）
- 开源 RAG 框架（LangChain、LlamaIndex）
competitive_casualty:
- 传统点式重排器服务商（Cohere 等）
- 未做上下文裁剪的 RAG SaaS 平台
- 依赖固定 Top-N 截断的 RAG 检索方案
market_opportunities:
- 开发者可基于 Kapa 的五级评分裁剪思路，构建通用的 RAG 上下文优化中间件，为各类 AI 知识库产品提供开箱即用的降本方案
- AI Agent 场景中裁剪的边际成本更低，创业者可针对多轮 Agent 对话开发专门的上下文压缩与检索优化工具
- 现有 RAG 框架（如 LangChain、LlamaIndex）可集成类似集合级评分裁剪功能作为默认优化步骤，提升产品竞争力
risk_matrix:
  regulatory: 无
  technological: 本方案依赖小型 LLM 的评分质量，若未来更强的大模型原生支持超长上下文并降低定价，裁剪层的必要性可能被削弱；同时该方案增加了 0.7
    秒延迟，对毫秒级响应的场景不够友好
  competitive: 该方案技术门槛不高，容易被主流 RAG 平台快速复刻集成，Kapa 的先发优势窗口期有限；大厂可能直接在检索侧通过更好的 reranker
    或端到端模型解决同样问题
  ethical: 自动裁剪可能系统性丢弃某些长尾但关键的上下文块（如小众技术细节、非主流语言文档），导致生成答案产生无意识的信息偏差
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: product
  name: Product Agent SDK
  canonical_name: kapa.ai Product Agent SDK
  url: null
  positioning: Kapa.ai 推出的企业级 AI 助手产品化 SDK，基于多源知识库（技术文档、API 参考和社区论坛）为开发者提供检索增强的智能问答
    Agent 构建能力。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - 需要为产品文档构建智能问答助手的开发者团队
  - 使用 RAG 技术构建知识密集型 Agent 的 AI 应用开发者
  product_signal: 新增轻量 LLM 上下文修剪器，在检索器和生成器之间对检索块进行五级评分，可丢弃约 68% 的上下文且保持约 96% 的召回率。
  market_signal: 每次查询成本净降低约 34%，延迟仅增加 0.7 秒，在成本敏感型 RAG 应用中具备显著竞争优势。
  differentiation: 采用 listwise LLM 评分方式同时审视所有检索块，解决了点式重排序分数无法判断集合相关性的根本缺陷。
  watch_reason: Kapa.ai 的上下文修剪方案直接回应了 RAG 系统中检索块膨胀导致的成本问题，以极低延迟代价实现大幅成本降低，该方法有望成为
    RAG 管道的标准组件，值得持续跟踪其在行业内的采用进展和竞品跟进情况。
  risk_notes:
  - 额外 LLM 调用带来的 0.7 秒延迟在实时交互场景中可能影响用户体验。
  - 五级评分体系效果高度依赖 prompt 质量，在跨领域知识库上的泛化能力尚未验证。
  score: 7.0
  article_ids:
  - f0eeef1a33ddd3e7
  evidence_snippets:
  - 修剪功能默认在 Product Agent SDK 的知识库搜索中启用，客户可以在基于 Kapa 检索构建的 Agent 中使用该功能以减少上下文占用。
---

## How we taught a small LLM to throw away 68% of our RAG context

Pruning agent context down to what the answer actually needs, while keeping 96% of recall

###### by

###### Lars Baltensperger

Kapa builds AI assistants that answer complex questions over large product knowledge bases. Think technical documentation, API references, PDFs, forums, support threads. Developers use our retrieval API to give their agents context about their product, and the same retrieval layer powers our end-to-end assistants.

For all the debate in 2026 about whether agents still need RAG, in our domain nothing comes close when knowledge bases get large and complex. Our retrieval comes in several forms, some agentic, some single-pass, but they all share the same shape: a retriever, which finds the chunks of documentation relevant to a question, and a generator, the LLM that writes the answer from them.

The short version of this post: we added a third step between the two. A small, cheap LLM reads the question and all the retrieved chunks together, and throws out the chunks the answer will not need before the expensive model ever sees them. It drops about 68% of the context, keeps about 96% of recall, and cuts the cost of a query by a third, net of its own cost. This post explains how we got there.

**Ignored chunks still cost money**

A retriever is a funnel. Embedding and keyword search cut a knowledge base of hundreds of thousands of chunks down to a few hundred candidates, a reranker orders them, and the top 15 or so reach the generator, the largest and most expensive model in the chain. Even then, most of what the generator reads is not needed for the question. That is deliberate: retrievers aim for maximum recall and trust the generator to ignore the noise.

But the generator is billed for every chunk it ignores. In our assistants, retrieved chunks are about two-thirds of the cost of a query, more than the answer, the conversation history, and the system prompt combined. Every chunk fewer cuts the query cost by about 4%. And in an agent, every tool call pours its output into the same context, so the context grows quickly; a tighter retrieval result buys room for everything else the agent has to hold and leaves less context to rot.

The catch is recall. Drop a chunk the answer needed and you traded a few cents for a wrong answer. A pruner is exactly as good as that tradeoff: compression gained per point of recall lost.

**The obvious fix does not work**

We already rerank before returning the top K, so we are sometimes asked to just expose the rerank scores and let callers cut on them: keep everything above 0.7, drop the rest. It fails for two reasons, and the second shaped everything we built.

First, a rerank score is an ordering, not a measurement. It says chunk A beats chunk B on this query, nothing more. The scores are not calibrated across queries, Cohere too says as much, so no fixed cutoff works. The only cutoff a ranking supports is positional, top-N, and that drops the last chunk whether it is noise or the answer.

Second, and this survives even perfect calibration: relevance is not a property of a single chunk. The rerankers in most pipelines are pointwise cross-encoders. They score each query-chunk pair alone, never alongside the other chunks it was retrieved with. Here is an anonymized production example:

The second chunk never mentions audit logs, so it scores as noise, yet it is half the answer, and no pointwise score can see that, because the chunk is only relevant next to the first one. Chunks also split multi-part questions between them, each useless alone. The real question is never whether a chunk is relevant by itself, but whether it belongs to a set that together answers the question.

**A clever fix that fails the same way**

Before giving up on the reranker we tried anchor documents (Sinhababu et al.): make the reranker's scale absolute by planting synthetic chunks of known relevance into the ranking, one written per level from Essential to Unrelated, then drop every real chunk that ranks below the anchor of the lowest level you want to keep. One extra LLM call on top of a rerank you already run, and genuinely elegant.

It did not work, for the same underlying reason. Anchors fix calibration, but they cannot fix the scores, and the reranker kept placing partially and indirectly relevant chunks below plainly irrelevant ones. To keep them, the anchor has to sit so low that hardly anything gets pruned.

That failure was the useful result: whatever prunes has to see the question and all the chunks at once, because the thing being judged is the set.

**So we let an LLM grade the chunks**

What we shipped is one listwise LLM call between the reranker and the generator. It gets the question and all the chunks, and grades every chunk against a five-level scale written into its prompt:

|
|
|
5 | ESSENTIAL | The answer cannot be produced without this chunk, whether it answers directly or is a definition or prerequisite another chunk depends on. |
4 | CONTRIBUTING | Does not answer on its own, but supplies something a complete answer needs in combination with other chunks. |
3 | SUPPORTING | On topic and plausibly useful, but the answer is likely complete without it. |
2 | TANGENTIAL | Same domain or shared terminology, no concrete contribution. |
1 | UNRELATED | No meaningful connection. |

Chunks at or above a threshold survive. The design answers both failures from earlier. Because each level is defined in words, a 4 means the same thing on every query, so a fixed cutoff finally works. And because the model sees the question and all the chunks together, it can judge the set, so partial and indirect relevance finally have somewhere to land.

Three knobs matter:

**The model:**the pruner is paid for out of what it saves, so flagship models are ruled out by construction; the small fast tiers all judged similarly, so we picked the fastest and cheapest at low reasoning effort.**The threshold**: the main dial between compression and recall.**keep-top-k**: the top few reranked chunks pass regardless of grade, protecting the strongest chunks from a grading mistake.

We also ran two simpler designs to keep ourselves honest. Budget-select: keep the top few, let the LLM add at most N more; predictable size, but once the budget is spent every further chunk is dropped no matter how relevant. And the simplest possible pruner: just ask the LLM which chunks to keep, no scale. If a scheme cannot beat asking directly, it is not worth building.

**The results**

We measured recall on a labeled set of real questions where we know exactly which chunks the answer needs, then verified compression, cost, and latency by replaying every configuration over a random month of production conversations, on the exact chunks each query actually sent to the generator.

Every point is one configuration, plotted by the two things that matter. Compression, on the x-axis, is the share of retrieved chunks the pruner throws away. Recall preserved, on the y-axis, is the share of questions that still have every chunk their answer needs after pruning: at 100% no question lost a chunk it needed, at 90% one in ten did. Up and to the right is better. The lines connect each strategy's best configurations, and the dashed grey line is the baseline any pruner has to beat: naive top-N truncation, just returning fewer chunks from the reranker.

Everything beats it, by a lot. Hold recall at 98%: truncation can drop one chunk, about 7% compression. Every LLM strategy reaches 30% or more, and relevance scoring drops close to half the chunks. The scoring line also dominates the other two at every compression level, so the only decision left was where on it to sit.

We picked a point near the aggressive end: about 96% recall preserved, about 68% of chunks dropped. One question in twenty-five loses a chunk it needed; in exchange, two-thirds of the context is gone, and the per-query bill falls by about 34%, net of the pruner's own cost.

**What it costs in latency**

The pruner runs between retrieval and generation, in the critical path, so its model call is added to every query, and its speed decides what that costs. Across the production set, the configuration we picked ran in about 0.7 seconds per query. Heavier settings climb fast, so a small model at low reasoning effort is what keeps the addition under a second.

The generation barely speeds up in return: fewer chunks mean fewer input tokens for the generator, so it starts responding a little sooner, but only a fraction of a second, nowhere near enough to cancel out the pruner's own call.

So pruning buys its compression at the cost of a small, fixed amount of latency, well under a second on the configuration we ship. On a latency-sensitive single-shot path that is a real cost to weigh. Inside an agent, which already makes several model calls per turn, one more lean call is marginal.

**Where we turned it on**

We rolled it out first where retrieval is one tool among many: customers building agents on top of our retrieval. An agent carries dozens of tools, every call pours output into the same context, and a documentation search that returns two-thirds less buys room for everything else. The lost recall is also less dangerous there: an agent that notices something missing can search again.

Pruning is on by default in our Product Agent SDK's knowledge base search, and optional in the retrieval API and MCP servers.