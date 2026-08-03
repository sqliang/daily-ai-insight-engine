---
title: 'Clinical failure rates over the decades: yikes'
source: https://www.science.org/content/blog-post/clinical-failure-rates-over-decades-yikes
author:
- '[[EA-3167]]'
published: '2026-07-25'
created: '2026-07-26'
manifest_dates:
- '2026-07-26'
description: 'Article URL: https://www.science.org/content/blog-post/clinical-failure-rates-over-decades-yikes
  Comments URL: https://news.ycombinator.com/item?id=49052628 Points: 100 # Comments:
  77'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: de99fefd746ab1ac
source_type: community_discussion
tldr: 一篇综述性论文汇总了自1960年代以来药物临床试验的失败率数据，发现最近三个十年（2000s、2010s）的临床失败率稳定在91%左右，1970-80年代略低（80-81%），但整体始终极高。
objective_summary: Science.org 博客文章引用了一篇2026年发表于 ScienceDirect 的综述论文，该论文汇总了1960年代以来所有可获取的药物临床试验失败率数据并评估了其可靠性。数据显示：1960年代失败率90%，1970年代81%，1980年代80%，1990年代88%，2000年代和2010年代均为91%。文章作者认为，失败率长期居高不下的原因包括已有有效药物的治疗领域（如高血压、高胆固醇、糖尿病、HIV）新药需超越现有标准，以及阿尔茨海默症等难度更大的疾病领域本身就难以突破。
event_type: policy_and_safety
epistemic_status: verified_fact
entities:
  companies: []
  technologies: []
  key_people: []
key_logic_flow:
- 药物行业的临床失败率是所有令外界困惑的现象的根本原因，该指标长期维持在极高水平。
- 一项新综述论文汇总了1960年代以来的临床失败率数据：1960年代90%，1970年代81%，1980年代80%，1990年代88%，2000年代和2010年代均达91%。
- 1970-80年代失败率略低，可能得益于分子生物学时代前以组织切片和表型筛选为主导的研发方式，以及当时尚有"低垂果实"可摘。
- 高血压、高胆固醇、II型糖尿病、HIV、丙肝等领域已有多种有效药物，新药必须超越现有标准，难度更大。
- 阿尔茨海默症等尚无有效药物的疾病领域则因其本身生物学难度极高而难以突破。
- 如果91%的汽车设计无法出厂或91%的飞机模型无法起飞，任何行业都无法承受如此高的失败率，但药物行业别无选择。
object_mentions:
- object_type: paper
  name: 'Clinical Failure Rates Over the Decades: A Systematic Review'
  canonical_name: 'Clinical Failure Rates Over the Decades: A Systematic Review'
  url: https://www.sciencedirect.com/science/article/pii/S3050620426000448
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 一篇新论文汇总了自1960年代以来药物临床试验失败率的各项估计，评估了所有可获取数据源的覆盖范围和可靠性。
  - 该论文发现1970和1980年代通过临床的候选药物略多于1960年代或现在，但失败率始终极高。
  - 论文数据显示2000年代和2010年代的临床失败率均为91%，最近三个十年均在相同区间内。
  article_id: de99fefd746ab1ac
extract_result: success
impact_score:
  score: 1.5
  reason: 本文并非AI行业事件，而是Science.org博客对制药行业临床失败率的历史综述评论。文章引用了一篇2026年发表于ScienceDirect的论文，提供1960-2010年代各十年的临床失败率数据（近三个十年稳定在91%）。对AI行业的直接影响极低：不涉及任何AI技术、模型、产品、融资或政策。间接层面上，91%的高失败率可为AI制药（如Recursion、Insilico
    Medicine等）的价值主张提供背景支撑——如果AI能降低这一数字将是巨大突破，但文章本身未提及AI。作为非AI事件，短期行业冲击力接近零。
sentiment: negative
developer_sentiment:
  tone: neutral
  primary_focus: 非AI话题，AI开发者对此关注度极低；AI制药领域从业者可能关注91%失败率对其技术路线的挑战与机会
hype_assessment:
  level: low
  reason: 文章完全基于一篇经过同行评议的综述论文（ScienceDirect 2026），提供了系统性的跨年代失败率数据，明确标注了数据四舍五入和误差棒范围，讨论了不同年代数据的可靠性和解释局限性。作者没有使用'颠覆'、'革命性'、'突破'等PR词汇，反而以'Yikes'（哎呀）表达对数据的坦诚感叹。全篇为数据驱动的严谨评论，无任何炒作成分。
information_entropy: high
domain_disruption:
  technical_innovation: 无。本文并非技术突破报道，而是对历史数据的汇总评论。
  business_model: 无。文章未讨论商业模式或产业策略，仅呈现失败率事实并反思其行业含义。
engineering_complexity: conceptual
compound_value:
  score: 8.0
  reason: 该文章揭示的91%临床失败率（持续三个十年未改善）是制药行业最深层的结构性痛点。在一个年研发支出超2500亿美元的行业中，任何能系统性降低这一指标的技术都将创造万亿美元级别的价值。AI驱动的药物发现——从AlphaFold蛋白质结构预测到生成式化学再到临床预测模型——是当今最有希望破解该难题的路径。长期复利效应体现在：先发AI制药公司一旦验证'湿实验+AI闭环'（数据积累→模型优化→临床成功率提升→更多数据），将形成极强的基础设施级护城河。但需注意，生物学复杂性和监管壁垒决定了这一过程不会线性爆发，评分落在8分而非更高。文章本身虽非AI技术突破报道，但作为投资逻辑的'锚定数据'极具说服力。
value_capture_layer: end_application
moat_impact: creates_new_moat
key_beneficiaries:
- Isomorphic Labs
- Recursion Pharmaceuticals
- Insilico Medicine
- NVIDIA
- Schrödinger
competitive_casualty:
- 传统 CRO 企业
- 未拥抱 AI 的大型药企
- 传统高通量筛选平台
market_opportunities:
- AI制药创业公司应聚焦于临床前候选分子的毒性预测与患者分层模型，通过提升临床试验成功率来证明AI/ML的实际价值，而非仅停留在靶点发现环节
- 基于多模态生物数据（基因组学、蛋白质组学、影像学）构建端到端的临床试验模拟平台，在进入人体试验前更精准地预测失败风险，这比单纯追求新靶点发现更具商业确定性和落地紧迫性
- 现有药物重定位（drug repurposing）是短期内回报最确定的AI应用方向——利用已有安全数据的已获批药物寻找新适应症，可避开Phase I安全性失败的高达~50%的淘汰率
risk_matrix:
  regulatory: AI驱动的临床试验预测工具若被FDA或EMA认定为医疗器械或关键决策依据，将面临严格的验证标准与审批流程，模型的"可解释性"问题可能成为监管障碍
  technological: AI模型倚赖历史数据训练，而历史数据本身包含了91%的临床失败样本，模型可能只学会拟合"为什么失败"的表象而非生物学本质；当靶点空间转向难成药蛋白质和复杂疾病（如阿尔茨海默症）时，AI预测精度可能断崖式下跌
  competitive: AI制药赛道已十分拥挤（Recursion、Insilico、BenevolentAI、Atomwise、薛定谔等均有成熟平台），新进入者在资金、数据壁垒和人才上均面临激烈竞争，且91%的客观失败率意味着即使技术领先也无法保证商业化成功
  ethical: 过度炒作AI在药物发现中的能力可能导致资本错配——资金涌入"AI发现新靶点"的故事而忽视基础生物学研究，延缓真正的科学突破；同时，训练数据中的历史偏倚可能导致AI系统性地忽略特定人群的药物安全性
  additional: []
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

Title: Clinical Failure Rates Over the Decades: Yikes

URL Source: https://www.science.org/content/blog-post/clinical-failure-rates-over-decades-yikes

Markdown Content:
I’m fond of saying that the most important single statistic about the drug industry is the clinical failure rate, which is (by any reasonable standard) appallingly high. To my mind, everything that is infuriating or inexplicable to outside observers (or patients!) about the biopharma industry traces back to that number, which represents a rate of failure that no other major industry operates under.

[Here’s a new paper](https://www.sciencedirect.com/science/article/pii/S3050620426000448) bringing together estimate of that failure rate since the 1960s, reviewing every data source the authors could find and assessing them for scope and reliability. They find that slightly more clinical candidates were making it through in the 1970s and 1980s as compared to today (or even as compared to the 1960s), but that the rates have always been very high indeed.

Here we go: in the 1960s, the clinical failure rate was 90%. In the 1970s, 81%. In the 1980s, it was 80%, and in the 1990s it was 88%. In the 2000s, 91% of all clinical candidates failed, and in the 2010s, it was 91% as well. I have rounded the decimal points here, because there are of course error bars on these numbers (and those spreads are naturally higher on the older numbers). But the numbers for the last three decades all lie within the same bounds, so if you quote a failure rate of 91% you cannot be far wrong.

The 70s and 80s numbers are interesting. The authors don’t speculate on the reasons for those rates being somewhat lower. If those data are really representative, my guess is that this was the final pre-molecular-biology era for clinical candidates, when compounds were more likely to be evaluated in tissue-slice assays rather than with isolated proteins (and quite possible when more preclinical development work was guided through phenotypic approaches in animal studies than later on). And it might well also represent the intersection of modernizing techniques with the available “low-hanging fruit”, an era when some classic drug targets got their first clinical development.

One way or another, I think it would be a mistake to look at these numbers and think that we could go back to 80% failure rates but turning back the clock somehow in our techniques. This is after all scientific research, and some of those clocks just cannot be turned back. We have already worked over those great earlier targets and moved on to harder ones; resetting the calendar is not going to bring back ACE and HMG-CoA reductase as new clinical programs (to pick two big winners that led to whole series of marketed drugs).

You can look at it by therapeutic area as well, using those as an example: whole disease areas like high blood pressure, high cholesterol, type II diabetes, HIV, hepatitis C and others now have multiple effective drugs to treat them. You can always do better, but you’re going to have to beat what’s already on the market, which is not so easy. Or you could always try to dig deeper into the underlying causes of these diseases and outdo the existing drugs that way, but you’re going to hit a lot of brick walls when you try that, too. Meanwhile, the disease areas that *don’t* have such lists of effective drugs are in that category because they have proven harder to crack - it’s not that we don’t see them! Alzheimer’s disease is a perfect example.

So it’s 2026 and there’s nothing we can do about that. We know a lot more about the biology of disease - although God knows, not nearly enough - and we don’t get to ignore the difficult pathways full of proteins lacking obvious small-molecule binding sites just because they’re harder to work on. We have been discovering whole new therapeutic modalities in recent years, and it’s for sure that many of the candidate programs in these are not going to work out, for reasons that we are soon to discover and then to learn how to deal with.

But let’s think about that 91% failure rate for a moment. When I bring this up in presentations, I invite the audience to consider what the auto industry would look like of 91% of new car designs proved unable to roll out of the factory, or if 91% of new airliner models were unable to leave the ground - and if you only found that out after spending all the R&D money to build them at full size and trying to fly them. No cutting-edge restaurant could survive if 91% of its innovative dishes proved inedible or outright poisonous. What other industries operate under these bizarre conditions? So when we do get something to work and something that people are willing to pay money for, we try to squeeze every dollar out of it because we never know when the next one will come along. It’s a nerve-wracking way to live, but there’s no alternative in sight.