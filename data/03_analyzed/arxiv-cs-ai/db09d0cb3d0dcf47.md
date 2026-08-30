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
impact_score:
  score: 5.5
  reason: 该论文填补了文档源码修复评估缺乏实证故障模型的空白：用扎根理论双重编码 168 个真实崩溃故障构建 18 类分类学，实例化为 DocMut 的
    48 个 AST 感知算子，并给出一个关键方法论洞见——13.6%~18.5% 的编译成功修复会实质改变文档文本，编译成功率单独使用会高估修复质量。这些成果在学术写作/排版自动化（LaTeX、Typst、Markdown）垂直赛道有真实价值，可能成为该子领域的事实性评测基准。但该领域属于较窄的技术子域，对整体
    AI 行业竞争格局不构成范式级冲击，影响更多局限在工具链与评测圈层。综合评定为 5.5 分。
sentiment: neutral
developer_sentiment:
  tone: neutral
  primary_focus: 编译成功率会高估修复质量这一方法论警示，以及 DocMut 基准工具的开源可复现性
hype_assessment:
  level: low
  reason: 论文通篇为实证方法论风格，无'颠覆''革命性'等 PR 滥用词汇；全文给出可核验的具体细节（编码信度 κ=0.34、48,651 次尝试、总推理成本约
    200 美元、10,437 实例），并主动披露'编译成功不能代表修复质量'的局限性，属于典型的低水分学术干货，不构成概念炒作。
information_entropy: high
domain_disruption:
  technical_innovation: 核心创新在于以扎根理论对 168 个来自 TeX Stack Exchange、GitHub 提交和包文档的真实崩溃故障做双重编码，构建
    18 类故障分类学并实例化为 DocMut 的 48 个跨格式 AST 感知算子，将文档修复评估从'ad-hoc 临时突变'升级为'具备实证故障模型的系统性注入'；此外，恢复
    oracle 方法（检验编译成功的修复是否实质改变文档文本）也是一项可推广的评估方法论创新。
  business_model: 对商业模式直接影响有限，但对学术写作与排版自动化赛道（Overleaf、Typst、AI 辅助写作与文档工具）提供了可复用的评测标准与故障注入基础设施，有望推动该垂直领域形成'编译成功
    + 内容保真'双指标的产品化评估共识，进而影响文档工具厂商对 LLM 修复能力的选型与质量把控。
engineering_complexity: production_ready
compound_value:
  score: 5.0
  reason: 这是一个学术基准而非商业实体，但其复利价值体现在三层：一是'恢复性 oracle'评估方法论——证明编译成功率会高估修复质量（13.6%-18.5%
    的编译成功修复实质改变了文档文本），这一发现可迁移到所有代码/文档修复型 Agent 的评测设计中，具备方法论层面的长期复用价值；二是 18 类故障分类学
    + 48 个 AST 感知算子被开源，成为后续文档修复工具研发的公共基础设施，存在被 Overleaf、Typst 等平台产品化的可能；三是多格式（LaTeX/Typst/Markdown）实证设计使其在垂直领域有成为参照基准的潜力。但制约因素明显：文档源码修复是
    Agentic Coding 大叙事下的窄垂直场景，市场规模有限；基准由学术团队维护，长期可持续性存疑；随着大模型能力提升，该能力很可能被并入更广义的编码评测（如
    SWE-bench 类）而丧失独立基准地位。综合判断：细分赛道内有基础设施潜力，但难以成为 3-5 年后的行业基石，故给 5.0 分。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Overleaf
- Typst
- DocMut
- Anthropic
- OpenAI
competitive_casualty:
- 模式化修复工具
- 传统规则式 LaTeX 检查器
- 编译成功率导向的文档修复产品
market_opportunities:
- 学术写作工具厂商（如 Overleaf、Typst 及国产论文协作平台）可将 DocMut 的 AST 感知修复能力产品化，提供提交前自动排错、一键修复 LaTeX/Typst
  源码的增值功能
- 基于'编译成功不等于内容保真'的核心发现，可打造面向大模型写作助手的文档修复内容保真校验工具，作为防止语义静默漂移的质量闸门
- Typst 作为新兴排版格式其修复难度显著高于 LaTeX/Markdown，针对 Typst 生态的自动修复与故障检测工具存在先发机会
risk_matrix:
  regulatory: 基准数据基于 TeX Stack Exchange（CC BY-SA 等开放许可）与开源仓库，商用化派生工具需注意分享相同方式许可的合规要求
  technological: DocMut 故障分类学固定为 18 类 48 算子，随模型能力提升或训练数据污染其区分度可能快速衰减；文档源码修复也可能被模型原生能力或更全面的代码修复基准覆盖
  competitive: 通用大模型厂商与 Overleaf、Typst 等编辑器均在布局文档/代码修复能力，专门基准和修复工具的生态位面临平台级能力挤压；Typst
    生态规模尚小，商业化落地支撑不足
  ethical: 修复工具可能静默改变文档语义（13.6%-18.5% 的编译成功修复实质改变文本），在学术写作与出版场景存在误导风险；若用于自动化批量改写，可能绕过作者对内容的最终审核
  additional:
  - 评测依赖固定零样本协议与 provider-pinned 路由，模型 API 版本迭代或推理引擎更换会导致结果难以复现
  - 从 Stack Exchange/GitHub 挖掘的故障样本存在生态偏差，难以覆盖真实用户的长尾文档场景
confidence:
  impact: medium
  compound: low
  hype: high
actionable_insight: monitor
object_insights:
- object_type: project
  name: TeXFix-Bench
  canonical_name: TeXFix-Bench
  url: https://arxiv.org/abs/2608.07617
  positioning: 一个基于实证挖掘故障分类学的多格式基准，用于评估大语言模型修复 LaTeX、Typst、Markdown 文档源代码的整体能力。
  technical_signal: 基准从 743 个开放许可种子构建 10,437 个实例，以固定零样本协议评估 7 个模型并收集 48,651 次尝试。
  adoption_signal: null
  ecosystem_relevance: 填补了文档源码修复评估缺乏实证故障模型的空白，与 LaTeX、Typst、Markdown 生态及大语言模型修复研究直接相关。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 该基准以实证挖掘的故障分类学替代临时的 ad-hoc 编辑，首次系统评估大语言模型对多种文档格式源码的修复能力，并揭示编译成功率会高估修复质量这一重要发现，对文档修复评测方法与模型改进具有持续参考价值。
  risk_notes:
  - 论文的故障分类学双重编码一致性系数仅为 0.34，分类标准的稳定性存在不确定性。
  - 基准主要依赖编译成功率评估，但研究自身表明该指标会高估修复质量，评测有效性仍需更多验证。
  - Typst 修复难度明显高于 LaTeX 和 Markdown，跨格式差异可能影响不同格式间结论的可比性。
  score: 6.0
  article_ids:
  - db09d0cb3d0dcf47
  evidence_snippets:
  - 论文提出 TeXFix-Bench，一个基于挖掘故障分类学的多格式基准，用于评估大语言模型对文档源代码的修复能力。
  - 该基准从 743 个开放许可种子构建了 10,437 个实例，并评估了 7 个大语言模型的修复表现。
- object_type: project
  name: DocMut
  canonical_name: DocMut
  url: null
  positioning: 一个将 18 类实证故障分类学实例化的文档源码故障注入工具，提供跨三种格式的 48 个 AST 感知算子。
  technical_signal: DocMut 提供跨 LaTeX、Typst、Markdown 三种格式的 48 个 AST 感知算子，注入的故障比模式突变难修复
    5.6 到 9.2 个百分点。
  adoption_signal: null
  ecosystem_relevance: 作为 TeXFix-Bench 的配套工具，DocMut 为文档修复评测提供可复用的标准化故障注入能力，服务于大语言模型修复研究。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: DocMut 以 AST 感知算子替代传统的模式突变进行故障注入，实证表明其故障更难修复、更能反映真实错误场景，且与 TeXFix-Bench
    基准及全部评测工件一同公开释放，便于复现与后续研究。
  risk_notes:
  - DocMut 的故障注入建立在编码一致性仅 0.34 的分类学之上，算子设计可能继承分类标准的不稳定性。
  - 工具仅覆盖 LaTeX、Typst、Markdown 三种格式，对更广泛的文档生态和编译链支持有限。
  score: 5.0
  article_ids:
  - db09d0cb3d0dcf47
  evidence_snippets:
  - 研究将 18 类故障分类学实例化为 DocMut，包含跨三种格式的 48 个 AST 感知算子，用于注入文档源码故障。
  - 跨模型基准测试显示 DocMut 注入的故障比基于模式的突变难以修复 5.6 到 9.2 个百分点。
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