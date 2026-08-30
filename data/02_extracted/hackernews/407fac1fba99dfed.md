---
title: 'Show HN: The load-bearing vocabulary of Claude'
source: https://louisabraham.github.io/load-bearing/
author:
- '[[Labo333]]'
published: '2026-08-27'
created: '2026-08-28'
manifest_dates:
- '2026-08-28'
description: 'Article URL: https://louisabraham.github.io/load-bearing/ Comments URL:
  https://news.ycombinator.com/item?id=49461817 Points: 508 # Comments: 240'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 407fac1fba99dfed
source_type: community_discussion
tldr: 开发者louisabraham推出load-bearing项目，每天抓取1000个GitHub Pull Request，用KL散度k-means将词汇聚成10个簇，发现一个2026年出现的词汇簇占上月人类署名PR的40%，其代表词汇是编码智能体用户的典型用语。
objective_summary: 开发者louisabraham以Show HN形式在Hacker News上展示load-bearing项目。该项目每天抓取1000个GitHub
  Pull Request，使用KL散度k-means方法将2025年以来的PR词汇聚成10个簇。其中2026年出现的一个词汇簇在上月所有人类署名的Pull Request中占比达到40%，其代表性词汇对使用编码智能体的开发者来说十分熟悉。
event_type: framework_tools
epistemic_status: pr_statement
entities:
  companies:
  - GitHub
  - Anthropic
  technologies:
  - k-means
  - KL-divergence
  - coding agents
  key_people:
  - louisabraham
key_logic_flow:
- load-bearing项目每天抓取1000个GitHub Pull Request，用于持续分析编码词汇的使用趋势。
- 项目基于2025年以来的GitHub PR数据，使用KL散度k-means方法将词汇聚成10个不同的簇。
- 有一个词汇簇于2026年才出现，但在上月所有人类署名的Pull Request中占比高达40%。
- 该簇的代表性词汇对使用编码智能体的开发者来说非常熟悉，说明大量PR写作已带有AI编码助手的词汇特征。
object_mentions:
- object_type: project
  name: load-bearing
  canonical_name: load-bearing
  url: https://louisabraham.github.io/load-bearing/
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该项目每天抓取1000个GitHub Pull Request，利用KL散度k-means方法将2025年以来的PR按词汇聚成10个簇，用于分析编码词汇的使用趋势。
  - 分析发现一个于2026年出现的词汇簇，在上月所有人类署名的Pull Request中占比达到40%，其代表词汇是编码智能体用户熟悉的典型用语。
  article_id: 407fac1fba99dfed
- object_type: product
  name: Claude
  canonical_name: Claude
  url: null
  confidence: low
  article_role: mentioned_reference
  evidence_snippets:
  - 文章标题'The load-bearing vocabulary of Claude'将Claude作为编码智能体的典型代表，围绕其词汇特征展开数据分析。
  article_id: 407fac1fba99dfed
extract_result: success
---

We scrape 1,000 GitHub Pull Requests daily to analyse trends in
vocabulary.

So far we have analysed:

We grouped GitHub PRs since 2025 into **10** clusters of vocabulary using KL-divergence k-means.

One of the clusters appeared in 2026 and represented **40%** of all human-attributed pull requests last month.

Its most representative words should look familiar to anyone who uses coding agents.

hover to see a week

hover to see a week