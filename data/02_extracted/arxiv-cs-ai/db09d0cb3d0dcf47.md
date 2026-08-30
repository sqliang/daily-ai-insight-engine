---
title: 'TeXFix-Bench: An Empirically Grounded Multi-Format Benchmark for LLM-Based
  Document Source Repair'
source: https://arxiv.org/abs/2608.07617
author:
- '[[Prajwal S. Venkateshmurthy]]'
published: '2026-08-11'
created: '2026-08-11'
manifest_dates:
- '2026-08-11'
description: 'arXiv:2608.07617v1 Announce Type: new Abstract: Scientific and technical
  writing depends on markup sources that must compile: LaTeX, Typst, and Markdown
  pipelines fail on missing delimiters, mismatched environments, broken imports, or
  package conflicts. Existing document-repair evaluations inject faults with ad-hoc
  edits that lack an empirical fault model. We present TeXFix-Bench, a multi-format
  benchmark for LLM-based full-source document repair grounded in a mined fault taxonomy.
  A Grounded-Theory study of localized hard-crash LaTeX faults from TeX Stack Exchange,
  GitHub commits, and package documentation (168 verified faults, dual open coding
  at $\kappa$=0.34) yields an 18-category taxonomy instantiated as DocMut: 48 AST-aware
  operators across three formats. A three-model cross-benchmark shows DocMut faults
  are 5.6-9.2 pp harder to repair than pattern-based mutations on the same seeds,
  and a real-error case study (88 mined human crashes, 67.0% repair success) brackets
  both synthetic sets from below. We construct 10,437 instances from 743 openly licensed
  seeds and evaluate seven LLMs under a fixed zero-shot protocol with provider-pinned
  routing, collecting 48,651 attempts at about USD 200 total inference cost. A complete
  6,613-instance x 7-model balanced matrix confirms all rankings. A pinned engine
  gate yields a 27.5-point intention-to-treat compile spread (56.7-84.2%). Typst is
  markedly harder than LaTeX and Markdown. A restoration oracle over 28,129 compiling
  repairs shows that 13.6-18.5% of compiling repairs materially alter document text,
  and restoration rank diverges from compile rank: the model with the lowest compile
  rate restores content best among its successes. Compile success alone overstates
  repair quality. We release the taxonomy, DocMut, and all campaign artifacts.'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: db09d0cb3d0dcf47
source_type: academic_paper
tldr: 论文发布 TeXFix-Bench，一个基于实证挖掘故障分类学的多格式基准，用于评估大语言模型修复 LaTeX、Typst、Markdown 文档源码的能力；其配套工具
  DocMut 含 48 个 AST 感知算子，实验评估了 7 个模型。
objective_summary: 论文提出 TeXFix-Bench，基于对 TeX Stack Exchange、GitHub 提交及包文档中 168 个已验证故障的扎根理论分析，构建了含
  18 个类别的故障分类学，并实例化为 DocMut 的 48 个 AST 感知算子。基准从 743 个开放许可种子构建 10,437 个实例，以固定零样本协议评估
  7 个大语言模型，共收集 48,651 次尝试，总推理成本约 200 美元。结果显示 DocMut 注入的故障比基于模式的突变难修复 5.6 到 9.2 个百分点，Typst
  的修复难度明显高于 LaTeX 和 Markdown。恢复 oracle 分析 28,129 个编译成功的修复，发现其中 13.6% 到 18.5% 会实质改变文档文本，说明仅凭编译成功率会高估修复质量。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - arXiv
  - TeX Stack Exchange
  - GitHub
  technologies:
  - LLM
  - LaTeX
  - Typst
  - Markdown
  - AST
  - DocMut
  key_people: []
key_logic_flow:
- 论文提出 TeXFix-Bench，一个基于实证挖掘故障分类学的多格式基准，用于评估大语言模型对文档源代码的整体修复能力。
- 通过对 TeX Stack Exchange、GitHub 提交和包文档中 168 个已验证故障进行扎根理论双重编码，研究构建了含 18 个类别的故障分类学。
- 该分类学被实例化为 DocMut 工具，包含跨 LaTeX、Typst、Markdown 三种格式的 48 个 AST 感知算子。
- 跨模型基准测试表明，DocMut 注入的故障比基于模式的突变难以修复 5.6 到 9.2 个百分点，真实错误案例研究的修复成功率为 67.0%。
- 基准从 743 个开放许可种子构建 10,437 个实例，在固定零样本协议下评估 7 个模型，编译成功率区间为 56.7% 到 84.2%。
- 恢复 oracle 分析显示 13.6% 到 18.5% 的编译成功修复会实质改变文档文本，且恢复排名与编译排名并不一致，说明编译成功率单独使用会高估修复质量。
object_mentions:
- object_type: project
  name: TeXFix-Bench
  canonical_name: TeXFix-Bench
  url: https://arxiv.org/abs/2608.07617
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 论文提出 TeXFix-Bench，一个基于挖掘故障分类学的多格式基准，用于评估大语言模型对文档源代码的修复能力。
  - 该基准从 743 个开放许可种子构建了 10,437 个实例，并评估了 7 个大语言模型的修复表现。
  article_id: db09d0cb3d0dcf47
- object_type: project
  name: DocMut
  canonical_name: DocMut
  url: null
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 研究将 18 类故障分类学实例化为 DocMut，包含跨三种格式的 48 个 AST 感知算子，用于注入文档源码故障。
  - 跨模型基准测试显示 DocMut 注入的故障比基于模式的突变难以修复 5.6 到 9.2 个百分点。
  article_id: db09d0cb3d0dcf47
- object_type: dataset
  name: 18-category fault taxonomy
  canonical_name: TeXFix-Bench fault taxonomy
  url: null
  confidence: medium
  article_role: primary_subject
  evidence_snippets:
  - 扎根理论研究对来自 TeX Stack Exchange、GitHub 提交和包文档的 168 个已验证故障进行双重编码，最终形成含 18 个类别的故障分类学。
  - 论文与分类学、DocMut 及全部实验产物一起对外发布。
  article_id: db09d0cb3d0dcf47
extract_result: success
---

# Computer Science > Artificial Intelligence

# Title:TeXFix-Bench: An Empirically Grounded Multi-Format Benchmark for LLM-Based Document Source Repair

View PDF HTML (experimental)Abstract:Scientific and technical writing depends on markup sources that must compile: LaTeX, Typst, and Markdown pipelines fail on missing delimiters, mismatched environments, broken imports, or package conflicts. Existing document-repair evaluations inject faults with ad-hoc edits that lack an empirical fault model. We present TeXFix-Bench, a multi-format benchmark for LLM-based full-source document repair grounded in a mined fault taxonomy. A Grounded-Theory study of localized hard-crash LaTeX faults from TeX Stack Exchange, GitHub commits, and package documentation (168 verified faults, dual open coding at $\kappa$=0.34) yields an 18-category taxonomy instantiated as DocMut: 48 AST-aware operators across three formats. A three-model cross-benchmark shows DocMut faults are 5.6-9.2 pp harder to repair than pattern-based mutations on the same seeds, and a real-error case study (88 mined human crashes, 67.0% repair success) brackets both synthetic sets from below. We construct 10,437 instances from 743 openly licensed seeds and evaluate seven LLMs under a fixed zero-shot protocol with provider-pinned routing, collecting 48,651 attempts at about USD 200 total inference cost. A complete 6,613-instance x 7-model balanced matrix confirms all rankings. A pinned engine gate yields a 27.5-point intention-to-treat compile spread (56.7-84.2%). Typst is markedly harder than LaTeX and Markdown. A restoration oracle over 28,129 compiling repairs shows that 13.6-18.5% of compiling repairs materially alter document text, and restoration rank diverges from compile rank: the model with the lowest compile rate restores content best among its successes. Compile success alone overstates repair quality. We release the taxonomy, DocMut, and all campaign artifacts.

# Bibliographic and Citation Tools

# Code, Data and Media Associated with this Article

# Demos

# Recommenders and Search Tools

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.