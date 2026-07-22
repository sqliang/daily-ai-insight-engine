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