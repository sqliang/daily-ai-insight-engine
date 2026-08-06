---
title: Twenty Years of Pandoc
source: https://pandoc.org/twenty-years-of-pandoc.html
author:
- '[[fiddlosopher]]'
published: '2026-08-03'
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
description: 'Article URL: https://pandoc.org/twenty-years-of-pandoc.html Comments
  URL: https://news.ycombinator.com/item?id=49156750 Points: 246 # Comments: 30'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 28fdaaf39e6fc5e3
source_type: community_discussion
tldr: 2006年8月3日，John MacFarlane 发布首个 pandoc 版本，二十年间从约3000行 Haskell 代码的工具发展为支持50多种文档格式、被
  Quarto 与 Jupyter Notebook 集成、安装于数百万台计算机的流行开源项目。
objective_summary: 作者 John MacFarlane 于 2006 年 8 月 3 日以 GPL 许可发布 pandoc 0.1，采用 Haskell
  解析器组合子构建 AST 再渲染输出的架构，实现 N 个解析器与 M 个渲染器的灵活转换体系。二十年间该项目发布超过 200 个版本，支持 50 多种文档格式，成为最受欢迎的
  Haskell 程序，并被 Quarto、Jupyter Notebook 等学术写作工具集成。项目还催生了 commonmark 规范，多数 Markdown
  处理器以其为核心规则。2017 年发布 pandoc 2.0，与 Jesse Rosenthal 合作完成 reader/writer 支持 I/O 的架构调整。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  - Google
  - Debian
  - Reddit
  - Stack Overflow
  technologies:
  - Haskell
  - Markdown
  - commonmark
  - LaTeX
  - reStructuredText
  - HTML
  - Lua
  - JSON
  - YAML
  - AST
  - CSL
  - EPUB
  - DocBook
  - ODT
  - Org-mode
  - parsec
  - GHC
  key_people:
  - John MacFarlane
  - John Gruber
  - Greg Restall
  - Recai Oktaş
  - Michel Fortin
  - Andrea Rossato
  - Matthew Pickering
  - Jesse Rosenthal
  - Albert Krewinkel
  - Puneeth Chaganti
key_logic_flow:
- 2006年8月3日，John MacFarlane 将 pandoc 首个版本以 GPL 许可发布到个人网站，该版本约3000行 Haskell 代码，可将 Markdown、reStructuredText、HTML、LaTeX
  互转并输出 RTF 或 S5。
- pandoc 采用解析器组合子构建真实语法树（AST）再渲染输出的架构，通过 N 个解析器与 M 个渲染器实现 N×M 种格式转换，与当时基于正则表达式的其他
  Markdown 实现形成差异。
- 2006年10月，土耳其开发者 Recai Oktaş 将 pandoc 打包进 Debian；2007年 pandoc 0.4 首次登上 Hackage 仓库，cabal-install
  的诞生使项目可以依赖外部包。
- 2008年发布的 pandoc 1.0 新增 MediaWiki、OpenDocument、ODT 等 writer 及带自动语法高亮的围栏代码块，并为此配套开发了
  zip-archive、highlighting-kate 等 Haskell 库。
- 2014年8月，MacFarlane 撰写 Markdown 规范并附 JavaScript 与 C 解析器，因 John Gruber 反对其“Standard
  Markdown”命名而改名为 commonmark，多数 Markdown 处理器随后以其为核心规则。
- 2017年发布的 pandoc 2.0 与 Jesse Rosenthal 协作完成重大架构调整，使 reader 与 writer 摆脱纯函数限制、具备 I/O
  能力，以支持 reStructuredText 文件包含等需要读写操作的完整保真转换。
object_mentions:
- object_type: project
  name: pandoc
  canonical_name: pandoc
  url: https://pandoc.org
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 2006年8月3日，John MacFarlane 将 pandoc 首个版本以 GPL 许可发布，该版本约3000行 Haskell 代码，仅依赖 GHC
    标准库。
  - 二十年间 pandoc 发布超过200个版本，支持50多种文档格式，成为最流行的 Haskell 程序并被安装在数百万台计算机上。
  - Pandoc 被集成进 Quarto 和 Jupyter Notebook 等学术写作工具，用于文档格式转换与学术出版流程。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: commonmark
  canonical_name: commonmark
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 2014年8月，MacFarlane 撰写 Markdown 规范并附 JavaScript 与 C 解析器，因 John Gruber 反对“Standard
    Markdown”命名而改名为 commonmark。
  - Pandoc 1.14 起支持 commonmark 及其扩展，最初通过绑定 C 库 libcmark，2020 年起改用自研的 commonmark 等
    Haskell 包。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: texmath
  canonical_name: texmath
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - MacFarlane 开发 texmath 库用于将 TeX 数学公式转换为 MathML，供 DocBook 或 HTML 使用，并在 pandoc 1.9
    中加入对 Word OMML 格式的支持。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: zip-archive
  canonical_name: zip-archive
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 为支持 ODT 输出，MacFarlane 创建了 zip-archive 包，当时 Haskell 生态尚无现成的 zip 归档库，项目借助 binary
    包完成二进制解析与序列化。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: highlighting-kate
  canonical_name: highlighting-kate
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 为给围栏代码块提供自动语法高亮，MacFarlane 编写了 highlighting-kate 库，解析 Kate 编辑器的 XML 语法定义并生成 Haskell
    代码高亮器。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: pandoc-citeproc
  canonical_name: pandoc-citeproc
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 2013年，引文处理从 pandoc 核心移出，成为独立的 pandoc-citeproc 外部过滤器，负责基于 CSL 样式自动生成引文与参考文献。
  article_id: 28fdaaf39e6fc5e3
- object_type: product
  name: Quarto
  canonical_name: Quarto
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Pandoc 被集成进 Quarto 和 Jupyter Notebook 等学术写作工具，成为这些产品文档格式转换与出版流程的底层能力。
  article_id: 28fdaaf39e6fc5e3
- object_type: product
  name: Jupyter Notebook
  canonical_name: Jupyter Notebook
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - Jupyter Notebook 等学术写作工具集成了 pandoc，用于笔记本内容与多种文档格式之间的转换。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: PHP Markdown Extra
  canonical_name: PHP Markdown Extra
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 围栏代码块语法由 pandoc 与 PHP Markdown Extra 维护者 Michel Fortin 协作制定，pandoc 还借鉴了其定义列表语法。
  article_id: 28fdaaf39e6fc5e3
- object_type: project
  name: libcmark
  canonical_name: libcmark
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - Pandoc 1.14 最初通过绑定 C 库 libcmark 支持 commonmark 解析，2020 年起改用纯 Haskell 的 commonmark
    系列包。
  article_id: 28fdaaf39e6fc5e3
extract_result: success
impact_score:
  score: 2.5
  reason: 这是一篇二十周年回顾性文章，而非新产品发布、融资或技术范式突破。它对文档转换社区的凝聚意义大于短期行业影响：文章系统梳理了 Pandoc 从 3000
    行 Haskell 工具成长为被 Quarto、Jupyter 集成的行业基础设施的历史，但并未带来任何改变竞争格局的新信息，属于纪念性内容而非事件性新闻。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 庆祝 Pandoc 二十年的持续生命力，以及其催生的 commonmark 规范对 Markdown 生态的深远影响
hype_assessment:
  level: low
  reason: 作者以朴素克制的笔触撰写回顾，甚至自嘲项目起源于'拖延症的产物'，全文未出现'颠覆''革命'等 PR 滥用词汇，所述版本演进、贡献者合作与架构调整均为可验证的历史事实，无任何炒作包装。
information_entropy: medium
domain_disruption:
  technical_innovation: Pandoc 以解析器组合子构建真实语法树（AST）再渲染输出的架构，取代了当时基于正则表达式的 Markdown
    实现，通过 N 个 reader 与 M 个 writer 实现 N×M 格式转换；其催生的 commonmark 规范成为多数 Markdown 处理器的核心规则，这两项是文档处理领域的本质性技术突破。
  business_model: Pandoc 作为 GPL 开源工具本身没有直接商业模式，但它是 Quarto、Jupyter Notebook 等学术写作工具及无数
    CI 文档管线的底层免费基础设施，以'公共品'形式重塑了文档转换生态的成本结构与竞争格局。
engineering_complexity: infrastructure
compound_value:
  score: 6.5
  reason: 推理链：①20 年、200+ 版本、被 Quarto/Jupyter 集成、装机量数百万，证明其作为文档转换事实标准的耐用性与网络效应，属于'时间越长越难替代'型资产；②N
    解析器×M 渲染器 + AST 架构与 CommonMark 规范形成标准化壁垒，兼容性库随时间复利积累，这是核心复利来源；③但 GPL 开源属性决定了价值捕获发生在下游集成方（Posit/Quarto、Jupyter、GitHub）而非
    pandoc 自身，缺乏直接商业变现通道，VC 视角下'基座稳、capture 弱'；④AI 时代存在双重路径：LLM 可原生跨格式转换形成旁路风险，但确定性、可复现的文档处理仍是
    agent 工具链的刚性需求，pandoc 更可能成为编码/写作 agent 的标准工具而非被替代。综合：细分赛道基础设施地位稳固，3-5 年后大概率仍是行业基石，但商业复利效应有限，故给
    6.5 分而非更高。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Posit (Quarto)
- Project Jupyter
- GitHub
- CommonMark 生态开发者
- AI 编码代理 (Claude Code 等)
competitive_casualty:
- 传统商业文档转换软件
- 付费在线格式转换服务
- 闭源 Markdown/出版排版工具链
market_opportunities:
- 在 AI 数据管线（RAG 检索、LLM 训练语料）中，pandoc 的 AST 架构可作为'任意格式→统一结构化表示'的归一化基础层，开发者可将 JSON AST
  与 Lua 过滤器封装为面向大模型语料清洗与知识库构建的文档预处理流水线，这是成熟可靠且成本极低的方案
- 围绕 commonmark 规范与 pandoc 生态，可开发面向学术写作的 AI 辅助产品（如引用管理、跨格式排版生成、结合大模型的文献综述产出），类似 Quarto
  但内置生成式 AI 能力，瞄准科研与出版场景
- pandoc 的可编程转换范式可被封装为低代码文档转换 SaaS（多格式互转、批量治理、模板化输出），服务企业内部遗留文档与合规归档需求，避开与大厂通用 API
  直接竞争，聚焦行业垂直场景
risk_matrix:
  regulatory: 无
  technological: 大模型驱动的端到端文档转换（多模态模型直接识别版式并转 Markdown/HTML）正快速成熟，可能逐步替代基于规则与 AST 的传统转换方案；若
    AI 原生工具达到同等保真度，pandoc 的核心技术壁垒将被削弱
  competitive: Typst 等新一代排版系统、云厂商文档解析 API 以及 Quarto 等高层封装工具都在分流直接使用 pandoc 的用户；文档转换赛道同质化竞争加剧，依赖
    pandoc 单点生态存在被挤压的风险
  ethical: pandoc 本身几乎无数据伦理风险，但若嵌入 AI 流水线需注意将受版权保护书籍/论文转换为语料涉及的版权与隐私问题，以及格式转换中语义信息丢失导致的下游模型事实偏差
  additional:
  - 单点维护者风险：项目高度依赖 John MacFarlane 个人长期维护，存在 bus factor（人员风险），长期可持续性依赖社区接力；GPL 许可证的传染性对商业闭源集成构成约束
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: monitor
object_insights:
- object_type: project
  name: pandoc
  canonical_name: pandoc
  url: https://pandoc.org
  positioning: 通用文档格式转换工具，基于 Haskell 解析器组合子构建 AST 架构，实现 Markdown 与 50 多种文档格式的双向互转。
  technical_signal: 采用解析器组合子解析并构建真实语法树（AST）再渲染输出的架构，以 N 个解析器与 M 个渲染器支撑 N×M 种格式转换，与基于正则表达式的传统
    Markdown 实现显著不同。
  adoption_signal: 二十年间发布超过200个版本，被安装于数百万台计算机，并集成进 Quarto 与 Jupyter Notebook 等学术写作工具。
  ecosystem_relevance: pandoc 催生了 commonmark 规范，多数 Markdown 处理器以其为核心规则，并衍生出 zip-archive、highlighting-kate
    等一批 Haskell 生态库。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: pandoc 作为最流行的 Haskell 程序与事实上的文档格式转换枢纽，其架构演进、生态衍生（commonmark 规范与配套库）及在学术写作工具链中的嵌入程度，是判断通用文档转换与
    Markdown 生态未来走向的关键观察点。
  risk_notes:
  - 项目由 John MacFarlane 个人长期主导维护，存在单点维护者风险；格式数量庞大，新格式保真与老格式兼容的平衡日益困难。
  score: 9.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 2006年8月3日，John MacFarlane 将 pandoc 首个版本以 GPL 许可发布，该版本约3000行 Haskell 代码，仅依赖 GHC
    标准库。
  - 二十年间 pandoc 发布超过200个版本，支持50多种文档格式，成为最流行的 Haskell 程序并被安装在数百万台计算机上。
  - Pandoc 被集成进 Quarto 和 Jupyter Notebook 等学术写作工具，用于文档格式转换与学术出版流程。
- object_type: project
  name: commonmark
  canonical_name: commonmark
  url: null
  positioning: 由 MacFarlane 撰写的 Markdown 规范及参考实现，为 Markdown 语法提供确定性统一标准，并成为多数 Markdown
    处理器的核心规则。
  technical_signal: 2014 年 8 月发布的规范附 JavaScript 与 C 解析器参考实现，因 John Gruber 反对 Standard
    Markdown 命名而改名为 commonmark，确立了可精确验证的 Markdown 语法标准。
  adoption_signal: 多数 Markdown 处理器以其规范为核心规则，pandoc 自 1.14 起支持 commonmark 及其扩展。
  ecosystem_relevance: commonmark 为 Markdown 生态提供跨实现的兼容基准，推动 GitHub 等平台渲染走向统一，是 Markdown
    标准化的关键基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: commonmark 作为 Markdown 事实标准的地位持续影响编辑器、渲染器与文档工具链的兼容性设计，其规范演进与扩展方言（如
    GFM）的发展值得长期跟踪。
  risk_notes:
  - commonmark 属社区事实标准而非正式国际标准，规范演进需协调多方实现利益；GFM 等扩展方言可能削弱统一性。
  score: 7.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 2014年8月，MacFarlane 撰写 Markdown 规范并附 JavaScript 与 C 解析器，因 John Gruber 反对“Standard
    Markdown”命名而改名为 commonmark。
  - Pandoc 1.14 起支持 commonmark 及其扩展，最初通过绑定 C 库 libcmark，2020 年起改用自研的 commonmark 等
    Haskell 包。
- object_type: project
  name: texmath
  canonical_name: texmath
  url: null
  positioning: 用于将 TeX 数学公式转换为 MathML 的 Haskell 数学排版库，供 DocBook 或 HTML 使用，并在 pandoc
    1.9 起支持 Word OMML 格式。
  technical_signal: 实现 TeX 数学公式到 MathML 及 Word OMML 的转换，填补 Haskell 生态在数学公式互转方向的能力空缺，支撑
    pandoc 的学术文档输出。
  adoption_signal: 随 pandoc 分发的数学公式转换能力，被 DocBook 与 HTML 输出路径使用，属于学术文档工具链的组成部分。
  ecosystem_relevance: texmath 与 zip-archive、highlighting-kate 等一样，是 pandoc 为解决自身需求而催生的
    Haskell 生态组件，体现个人项目驱动生态建设的路径。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: texmath 是 pandoc 学术输出能力（尤其数学公式保真）的关键依赖，其格式支持范围与转换精度直接影响 pandoc 在学术出版场景的可用性。
  risk_notes:
  - 依赖项与 pandoc 主项目同步演进，维护者精力分散可能影响更新节奏；数学公式转换边界场景众多，保真度难以全面覆盖。
  score: 5.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - MacFarlane 开发 texmath 库用于将 TeX 数学公式转换为 MathML，供 DocBook 或 HTML 使用，并在 pandoc 1.9
    中加入对 Word OMML 格式的支持。
- object_type: project
  name: zip-archive
  canonical_name: zip-archive
  url: null
  positioning: Haskell 生态的 ZIP 归档处理库，为 pandoc 的 ODT 输出而创建，借助 binary 包完成二进制解析与序列化，是
    pandoc 的底层依赖。
  technical_signal: 在 Haskell 生态缺乏现成 zip 库的背景下，基于 binary 包实现二进制解析与序列化，解决了 pandoc 生成
    ODT 所需的归档能力。
  adoption_signal: 作为 pandoc 配套库随项目分发使用，同时沉淀为 Haskell 生态可复用的通用 zip 归档组件。
  ecosystem_relevance: zip-archive 是 pandoc 为解决自身需求而创建的基础库，随后成为 Haskell 生态中可复用的通用组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 pandoc ODT 输出能力的基础依赖，zip-archive 的维护状态与兼容性直接影响 pandoc 对 OpenDocument
    格式的支持质量。
  risk_notes:
  - 属于工具性基础库，更新频率可能较低；对新兴压缩格式与安全漏洞（如解压路径穿越）的响应能力有待观察。
  score: 4.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 为支持 ODT 输出，MacFarlane 创建了 zip-archive 包，当时 Haskell 生态尚无现成的 zip 归档库，项目借助 binary
    包完成二进制解析与序列化。
- object_type: project
  name: highlighting-kate
  canonical_name: highlighting-kate
  url: null
  positioning: 为 pandoc 提供自动语法高亮的 Haskell 库，解析 Kate 编辑器的 XML 语法定义并生成代码高亮器，支撑围栏代码块功能。
  technical_signal: 通过解析 Kate 编辑器的 XML 语法定义自动生成 Haskell 代码高亮器，使 pandoc 得以开箱支持大量编程语言的语法高亮。
  adoption_signal: 随 pandoc 1.0 起为围栏代码块提供开箱即用的语法高亮，覆盖大量编程语言语法。
  ecosystem_relevance: highlighting-kate 展示了从编辑器语法定义到库代码生成的高亮方案，是 pandoc 生态中支撑开发者文档体验的组件。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 代码高亮是开发者文档工具链的刚需，highlighting-kate 的维护状态及后续被替代的情况，反映 pandoc 生态对周边能力演进的取舍。
  risk_notes:
  - 基于 XML 语法定义生成高亮器的方式维护成本偏高，新语言支持依赖语法定义质量；后继可能出现更轻量的替代方案。
  score: 4.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 为给围栏代码块提供自动语法高亮，MacFarlane 编写了 highlighting-kate 库，解析 Kate 编辑器的 XML 语法定义并生成 Haskell
    代码高亮器。
- object_type: project
  name: pandoc-citeproc
  canonical_name: pandoc-citeproc
  url: null
  positioning: 从 pandoc 核心独立出的引文处理外部过滤器，负责基于 CSL 样式自动生成引文与参考文献，服务学术写作场景。
  technical_signal: 2013 年引文处理从 pandoc 核心解耦为独立过滤器，基于 CSL 样式自动生成引文与参考文献，支持学术写作工作流。
  adoption_signal: 作为 pandoc 学术写作能力的重要插件，支撑自动引文与参考文献生成，被学术用户广泛使用。
  ecosystem_relevance: 引文处理是 pandoc 区别于普通文档转换器的学术特性，pandoc-citeproc 的独立演进体现了对 CSL
    引文生态的对接。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 学术写作工具链（如 Quarto、Typst）对引文管理能力持续重视，pandoc-citeproc 的演进方向与 CSL 标准兼容性是观察学术出版软件栈的窗口。
  risk_notes:
  - 独立过滤器形态增加安装与配置复杂度；CSL 样式生态庞大，样式兼容与引文格式保真需要持续维护。
  score: 4.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 2013年，引文处理从 pandoc 核心移出，成为独立的 pandoc-citeproc 外部过滤器，负责基于 CSL 样式自动生成引文与参考文献。
- object_type: project
  name: PHP Markdown Extra
  canonical_name: PHP Markdown Extra
  url: null
  positioning: PHP 生态的 Markdown 扩展实现，其围栏代码块语法与 pandoc 协作制定，并贡献了定义列表等 Markdown 语法特性。
  technical_signal: 围栏代码块语法由 pandoc 与 PHP Markdown Extra 维护者 Michel Fortin 协作制定，其定义列表语法也被
    pandoc 借鉴采用。
  adoption_signal: 围栏代码块与定义列表语法后被广泛采用，成为 Markdown 生态的通用特性。
  ecosystem_relevance: PHP Markdown Extra 与 pandoc 的语法协作体现了 Markdown 生态早期各实现互相借鉴、共同演化的特点。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 作为 Markdown 扩展语法的早期推动者之一，PHP Markdown Extra 对围栏代码块等特性的贡献持续影响当前 Markdown
    方言的设计。
  risk_notes:
  - 文章仅为历史回顾提及，缺乏项目当前活跃度的公开信息，需谨慎判断其后续演进状态。
  score: 3.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - 围栏代码块语法由 pandoc 与 PHP Markdown Extra 维护者 Michel Fortin 协作制定，pandoc 还借鉴了其定义列表语法。
- object_type: project
  name: libcmark
  canonical_name: libcmark
  url: null
  positioning: commonmark 规范附带的 C 语言参考解析库，曾作为 pandoc 1.14 绑定支持 commonmark 解析的底层依赖。
  technical_signal: 作为 commonmark 的 C 参考实现，被 pandoc 1.14 通过绑定方式用于 commonmark 解析，后于
    2020 年被纯 Haskell 实现替代。
  adoption_signal: 文章仅回顾了其在 pandoc 中的历史使用，2020 年后不再作为 pandoc 的 commonmark 解析路径。
  ecosystem_relevance: libcmark 是 commonmark 参考实现的一部分，为其他语言绑定提供基准，但其在 pandoc 中被替换反映了
    Haskell 生态自研替代的取向。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: libcmark 与 commonmark 参考实现的演进取舍，反映 Markdown 标准化在解析器实现层面的技术路线变化，值得持续观察。
  risk_notes:
  - 对 pandoc 而言已是历史依赖，当前项目活跃度与独立演进价值有限，跟踪优先级较低。
  score: 3.0
  article_ids:
  - 28fdaaf39e6fc5e3
  evidence_snippets:
  - Pandoc 1.14 最初通过绑定 C 库 libcmark 支持 commonmark 解析，2020 年起改用纯 Haskell 的 commonmark
    系列包。
---

# Twenty Years of Pandoc

On August 3, 2006, I uploaded the first version of pandoc to my website, releasing it under the free GPL license. Pandoc 0.1 consisted of about 3000 lines of Haskell code, with no dependencies aside from GHC’s standard library. It could convert Markdown, reStructuredText, HTML, and LaTeX documents into any of these formats, plus RTF or S5. I had no idea at the time that this would just be the first of over two hundred releases over the next twenty years; that the project would become the most popular program written in Haskell; that I would spend countless hours on bug-fixes, improvement, and project management; that I would collaborate with programmers in many other countries; that pandoc would come to support over fifty document formats; that it would allow automatic generation of citations and bibliographies; that it would become integrated into academic writing tools like Quarto and Jupyter Notebook; that it would be installed on millions of computers around the world.

How did this happen? I want to take advantage of pandoc’s birthday to tell the story of the project, as best I can remember it.

*John MacFarlane*

*August 2, 2026*

## Prehistory

People often ask: Why is pandoc written in Haskell? There could have been good answers to this question: Haskell is a very good language for writing this kind of application. But in fact, I didn’t decide to write a document converter, then decide to use Haskell for it. I decided to use Haskell, and then decided to write a document converter in it.

I had heard about Haskell from the blog of a philosophical logician friend, Greg Restall. Of an introductory book on Haskell, he said: “I’m glad that this wasn’t the textbook in my introductory computer science course, long ago in 1986. If it were, I may have fallen in love with computing and never become a philosopher” (consequently.org).

Intrigued by this (and not heeding Restall’s warning about the
potential effects on my future philosophical productivity), I read
*A Gentle
Introduction to Haskell* to get a basic understanding of
the language. But the only way to really learn a programming
language is to write something in it. I saw that Haskell was good
for writing parsers and compilers, and it came with a really nice
parser combinator library (parsec), so I decided to write a
Markdown parser.

At that time, there were implementations of Markdown in Perl,
Python, Ruby, and PHP; they all transformed Markdown directly to
HTML through a sequence of regex
transformations. Pandoc took a different approach. It parsed the
Markdown using parser combinators and produced a real abstract
syntax tree (AST), which it could then render to HTML or
another format. This was a more reliable architecture (avoiding
many quirks of the regex versions). It was also a more extensible
one: by writing *N* parsers (“readers”) and *M*
renderers (“writers”), one could support *N × M*
conversions. Soon I added a reader for reStructuredText, because I
kept a lot of my lecture notes and handouts in that format. And I
added a writer for LaTeX, because I wanted to be able to produce
PDFs. Then I added a writer for Markdown, so I could start to
convert my reStructuredText notes to Markdown. And from there the
project just snowballed.

Thus, a project that started out as nothing more than the product of procrastination was nurtured by the joy of writing in Haskell and by its increasing usefulness for my own academic work.

## First releases (2006–8)

In August 3, 2006, I decided to make the source code available on my website. By now pandoc supported HTML, LaTeX, RST, and Markdown as input and output formats, and RTF as an output format; also PDF via LaTeX.

I made no attempts to advertise the project, other than emailing two friends. This was before social media (which I’ve never used anyway), before GitHub, and before Hackage, the Haskell package repository. But apparently some people stumbled across it on my website and started using it. In October I was contacted by a Turkish developer, Recai Oktaş, who was trying to get certified as a Debian developer and wanted to package pandoc for Debian linux. So I worked with him to do that. This was a great learning experience for me and it greatly increased the visibility of the project.

During 2007, I continued to improve pandoc, largely guided by
my own needs. Version 0.3 added the DocBook writer and the
now-standard syntax for footnotes in Markdown. Version 0.4 added
support for Markdown tables, definition lists, super/subscript,
strikeout, and enhanced ordered lists, as well as writers for
groff man pages and ConTeXt. This was the first release to go on
the Hackage Haskell
package repository, which was started in 2007. The Hackage archive
and the new `cabal-install`

tool, which automatically
resolved and fetched dependencies, opened up the possibility of
depending on external packages.

## Pandoc 1 (2008–17)

Pandoc 1.0 was released in September 2008, with new writers for
MediaWiki, GNU Texinfo (contributed by Peter Wang), OpenDocument
(contributed by Andrea Rossato), ODT, and delimited code blocks
(now called “fenced”) with automatic syntax highlighting. Support
for ODT requires the ability to create a zip archive, and at the
time there was no Haskell package for this, so I created one (`zip-archive`

),
using the excellent `binary`

package for binary parsing
and serialization. Support for syntax highlighting required a
syntax highlighting library, which also did not exist in Haskell.
For this, I wrote `highlighting-kate`

,
which parsed the XML syntax definitions used by the Kate text
editor and turned them into Haskell code highlighters. This
allowed pandoc to support a large number of syntaxes right off the
bat. This version also contained support for automatic generation
of citations and a bibliography using CSL style, using Andrea
Rossato’s `citeproc-hs`

library.

Throughout this period, I was involved in discussions with
other Markdown implementers on the (now defunct) `markdown-discuss`

mailing list. The syntax for delimited code blocks, which
pandoc supported long before GitHub popularized fenced code
blocks, was worked out in collaboration with Michel Fortin, the
maintainer of PHP Markdown Extra. I took care when adding
extensions to pandoc’s Markdown to pay attention to prior art, for
example copying PHP Markdown Extra’s definition list syntax.
During this period, I also became aware of many ambiguities in
Markdown’s syntax—a situation I would later try to improve in the
commonmark project.

The next big change to pandoc came in version 1.4 (released in January 2010), which introduced a flexible template system, replacing hard-coded headers and making pandoc’s output much more customizable.

In 2010, we moved from Google Code
to GitHub, which would
do even more to increase the visibility of the project. Further
releases in 2010 and 2011 added support for EPUB output, Org-mode
output (due to Puneeth Chaganti), and Textile input (due to Paul
Rivier). Pandoc also gained support for converting TeX math to
MathML (for DocBook or HTML), via my `texmath`

library.

Pandoc 1.9, published in 2012, finally made it possible to
produce Word docx output. To handle the equations properly, I
added support for Word’s OMML format to `texmath`

. This
release also added an AsciiDoc writer and support for Beamer and
DZSlides, and in 1.9.3 we gained a DocBook reader (with
contributions from Mauro Bieg, who became a long-time
contributor).

In 2013, we focused on several features that made pandoc much
more flexible and customizable. The first was a fine-grained
system of Markdown
“extensions,” allowing support for the many variants of
Markdown that were then proliferating. The second was the ability
to include YAML
metadata blocks in Markdown, with arbitrary structured fields
that populate template variables. The third was the ability to
create custom
writers in Lua, allowing ad hoc output formats to be supported
by users. The fourth was the introduction of JSON
filters—user-created programs that transform a JSON
serialization of the pandoc AST, allowing the document to be
customized between the parsing phase and the rendering phase.
Citation processing was moved from the core of pandoc into an
external filter, `pandoc-citeproc`

.

This era saw the addition of reveal.js, EPUB v3, DokuWiki, and FictionBook2 output; OPML input and output; and Haddock and MediaWiki input. Notable contributors include David Lazar (Haddock) and Sergey Astanin (FictionBook2).

The year 2014 saw the arrival of three new contributors who
would go on to make many contributions to the project. Albert
Krewinkel added support for Org-mode input; Jesse Rosenthal added
a Word docx reader (complete with track-changes awareness); and
Matthew Pickering (at the time a student at Oxford whom I
“advised” as a Google Summer of Code Student) added support for
EPUB and Txt2Tags as input formats. Supporting EPUB input required
being able to convert MathML equations, so Pickering also worked
on `texmath`

. We were in very different time zones, and
I remember waking up every morning to find all the work Pickering
had done during the night. (Pickering has gone on to become one of
the core maintainers of the `ghc`

compiler.) All of
these contributions were released in pandoc 1.13, together with
Clare Macrae’s DokuWiki writer.

Since 2012, I had been involved in a working group that aimed to produce an unambiguous specification of Markdown’s syntax, initiated by Jeff Atwood and including representatives from GitHub, Reddit, and Stack Overflow. The group held intensive discussions in 2012, which petered out in 2013. I still believed in the project and didn’t want to let the work we’d done go to waste, so I sat down in August 2014, before the academic year began, and wrote up a spec for Markdown, as well as parsers in JavaScript and C. I sent the draft spec to John Gruber for comment and did not get a response, so a few weeks later we posted the spec. At this point, Gruber strongly objected and demanded that we not call the project “Standard Markdown,” so we changed the name to “commonmark.” The project has been a success, in that with a few exceptions, most Markdown processors implement the commonmark spec for their core rules. (Commonmark does not concern itself with extensions.)

Pandoc 1.14 (2015) added support for commonmark and a number of
extensions (at first via bindings to the C library `libcmark`

,
but later, in 2020, via my Haskell packages `commonmark`

,
`commonmark-extensions`

, and
`commonmark-pandoc`

). I intend eventually to
replace pandoc’s legacy Markdown parser with a commonmark core,
but there are still a few key extensions that have not been
implemented, so pandoc users must still choose between parsing
their documents as `markdown`

(Markdown with pandoc’s
extensions) or as `gfm`

or `commonmark`

or
`commonmark_x`

(commonmark with a number of
extensions). Ironically, although I was the author of the
commonmark spec, pandoc still uses a pre-commonmark Markdown
parser!

The next year brought some important changes in the pandoc AST, with the addition of image and link attributes, a SoftBreak element (enabling pandoc to preserve line breaks from the original source, or wrap, depending on a command line setting), and a LineBlock element. MarLinn added an ODT reader, Chris Forster added a TEI writer, and Ivo Clarysse added support for DocBook 5.

## Pandoc 2 (2017–23)

Pandoc 2.0 (released in 2017) brought some big architectural changes, worked out in collaboration with Jesse Rosenthal. In the past, most of pandoc’s readers (parsers) and writers (renderers) had been “pure” (that is, they had Haskell types that prevented them from having any side effects, including I/O operations). But some formats needed to be able to do I/O for a fully faithful conversion. (For example, reStructuredText has a syntax for including files, so the parser needs to be able to read files; in some other formats, images require explicit sizes, so a renderer has to be able to read image files, perhaps fetching them using HTTP, and determine their sizes.) We designed a system that allowed pandoc readers and writers to run in any instance of the PandocMonad typeclass, and we provided both a pure instance (which could be used for controlled testing, and in situations where we wanted to forbid I/O) and an instance that allowed I/O operations. The system also provided a way to handle images included as resources in formats like docx or EPUB.

The other big change was the introduction of Lua filters:
filters running in an embedded Lua interpreter and operating
directly on the pandoc AST, requiring no software other than
pandoc itself and offering far better performance than JSON
filters. This was made possible by the massive efforts of Albert
Krewinkel, building on the `hslua`

,
a Haskell-Lua bridge library.

In addition, pandoc 2.0 introduced the raw attribute syntax in
pandoc’s Markdown, and support for GitHub-flavored
Markdown, Emacs Muse (Alexander Krotov), TikiWiki, Vimwiki
(Yuchen Pei), Creole (Sascha Wilde), groff ms, and JATS. The old
`highlighting-kate`

was replaced by the new `skylighting`

,
which offered better performance and more accurate interpretation
of KDE syntax definitions. A PowerPoint writer (due to Jesse
Rosenthal) soon followed, as well as support for FictionBook2
(Krotov) and man (Yan Pashkovsky and me) as input formats.

In 2018, the project received a generous $100,000 donation from Handshake, which we used over the next five years to give small stipends to the most active maintainers.

In 2019, support for `ipynb`

(Jupyter notebooks) was
added, allowing pandoc to be used in data science workflows, and
Jira wiki markup was supported as an output format. With pandoc
2.8, it became possible to specify collections of default options
using defaults
files.

Users had long complained that pandoc’s model of a table was too restrictive, not even supporting row and colspans. After extensive discussion of what was needed in a table format, Christian Despres designed the new types for tables and modified all of the readers and writers to use it (a big job).

At this point pandoc had supported citation resolution for many
years, by means of the `pandoc-citeproc`

filter that
used Andrea Rossato’s `citeproc-hs`

. This was slow and
somewhat buggy, and Rossato had long since disappeared from the
scene, so I wrote a Haskell
citeproc library from scratch, using just the CSL spec and
test cases. Pandoc 2.11 depended on this library and offered far
better citation support: faster, more faithful to CSL, and with no
need for an external filter. In order to get citations to sort
properly, I had to write a another library (`unicode-collation`

)
implementing the Unicode Collation algorithm in pure Haskell.

During this era Pandoc came to support conversions between
bibliography database formats: BibTeX, BibLaTeX, and CSL JSON,
EndNote XML and RIS; conversion from CSV and TSV to pandoc table
formats; conversion to Markua; and conversion from RTF. With
pandoc 2.15 a `--sandbox`

option was added, which guarantees that pandoc’s parsers and
renderers have no I/O side effects. (This was possible because of
the PandocMonad abstraction we added back in pandoc 2.0.) With
pandoc 2.16.2 it became possible to write custom readers in Lua to
complement the custom Lua writers that had been added in 2013. And
with pandoc 2.19.1 it became possible to run pandoc as a web
server exporting an API.

## Pandoc 3 (2023–present)

By 2023, pandoc had become a very big, monolithic project. Some
users wanted a leaner program, one that didn’t include a full web
server and Lua interpreter. So with the pandoc 3.0 release, we
split pandoc into four parts: `pandoc`

remained the
Haskell library, `pandoc-lua-engine`

brought the Lua
integration, and `pandoc-server`

exposed the library
over HTTP as an API. The command-line program, now in the
`pandoc-cli`

package, could optionally be compiled
without server or Lua support. We also introduced a native Figure
element in the AST and a “chunked HTML” writer for multi-chapter
HTML books and documentation.

The first versions of Typst, a
modern LaTeX competitor with incremental compilation, were
released in 2023. I wanted to help the project by providing an
easy on- and off-ramp, making it easy for others to try Typst. It
turned out that creating a Typst reader for pandoc required
implementing an interpreter for a fairly full-featured programming
language. The result was the `typst`

package on Hackage. Typst support was added in pandoc 3.1.3.

In 2018 I had published an essay “Beyond
Markdown” in which I described the six features of Markdown
that I thought had created the most difficulties, both for writing
a spec and for implementations, and I explained how I thought
these flaws could be fixed in a future Markdown-like light markup
syntax. In 2022, I published a syntax description for such a
syntax, djot, together with code in
Lua, JavaScript and (later) Haskell. Pandoc 3.1.12,
published in 2024, added `djot`

as both an input and
output format.

Subsequent releases in 2024 and 2025 saw the addition of an
ANSI writer for formatted terminal output and a reader for the
mdoc and POD formats (all due to Evan Silberman), a reader and
writer for an XML representation of the pandoc AST (massifrg), a
vimdoc writer (reptee), a PowerPoint reader (Anton Antich), an
Excel spreadsheet reader (Anton Antich), and a BBCode writer
(reptee), and an AsciiDoc reader (supported by my `asciidoc`

package).

Pandoc 3.9, released in February 2026, included support for compiling pandoc to WASM, which allowed a full-featured version of pandoc to run in the browser. Most of the key work was done by TerrorJack. The GUI interface “pandoc for the people” was designed with the help of Claude Opus.

I still work on pandoc almost every day. Most of this work doesn’t involve the kind of new features or architectural changes I have focused on in this narrative. Mostly it consists in fixing small bugs, making tiny improvements, reviewing issues and pull requests, repairing infrastructure (continuous integration, building releases, code signing, website), improving documentation, and engaging in discussions with maintainers and users.

## Statistics

Pandoc currently supports 51 input formats and 76 output formats, thus 3876 distinct conversions (not counting the variants that are possible by adjusting extensions).

The four core packages (`pandoc`

,
`pandoc-lua-engine`

, `pandoc-server`

,
`pandoc-cli`

) consist of 85,684 lines of Haskell code,
not including tests. If one includes dependencies that exist
mainly for the sake of pandoc (`texmath`

,
`typst`

, `djot`

, `commonmark`

,
`asciidoc`

, `citeproc`

, and the pandoc/Lua
interface packages), this number approximately doubles.

On GitHub, 7346 issues have been resolved.

Over 600 people have contributed to pandoc over the years. The top twenty contributors (measured by numbers of source lines changed) are:

| Contributor | Lines changed | Years active |
|---|---|---|
| John MacFarlane | 372,317 | 2006– |
| Albert Krewinkel | 77,136 | 2014– |
| Jesse Rosenthal | 39,664 | 2014– |
| Christian Despres | 15,314 | 2019–2021 |
| Alexander Krotov | 8,657 | 2017–2019 |
| Matthew Pickering | 6,919 | 2014–2015 |
| MarLinn | 4,142 | 2015 |
| Evan Silberman | 3,478 | 2024– |
| Nikolay Yakimov | 3,362 | 2014–2020 |
| Mauro Bieg | 3,044 | 2012–2020 |
| Emily Bourke | 2,196 | 2021 |
| Yan Pas | 2,035 | 2018 |
| reptee | 1,732 | 2025 |
| Anton Antich | 1,552 | 2025 |
| massifrg | 1,171 | 2025– |
| Nathan Gass | 1,011 | 2010–2011 |
| Tuong Nguyen Manh | 801 | 2022– |
| Joseph C. Sible | 767 | 2020–2024 |
| Clare Macrae | 759 | 2013–2015 |
| Sergey Astanin | 718 | 2011–2012 |

Here are the twenty contributors who have contributed over the longest spans of time:

| Contributor | Years active | |
|---|---|---|
| John MacFarlane | 2006–2026 | |
| Albert Krewinkel | 2014–2026 | |
| Andrew Dunning | 2015–2026 | |
| Nikolay Yakimov | 2014–2025 | |
| Thomas Hodgson | 2015–2026 | |
| Mauro Bieg | 2012–2022 | |
| Kolen Cheung | 2016–2025 | |
| Pablo Rodríguez | 2014–2023 | |
| Pascal Wagler | 2019–2026 | |
| Felix Yan | 2016–2023 | |
| Sergei Trofimovich | 2011–2018 | |
| Tristano Ajmone | 2017–2024 | |
| Frerich Raabe | 2015–2022 | |
| Salim B | 2017–2024 | |
| Yihui Xie | 2014–2020 | |
| Sascha Wilde | 2017–2023 | |
| Jose Luis Duran | 2013–2019 | |
| Jesse Rosenthal | 2014–2020 | |
| John Muccigrosso | 2016–2022 | |
| Jan Tojnar | 2020–2026 | |
| Brian Leung | 2018–2023 |

## Retrospective: the choice of Haskell

As I noted at the beginning, I didn’t choose Haskell because I judged it to be the best language to use for a project like pandoc. But was it?

It’s hard to answer this confidently, because I’m not very familiar with what would now be the most obvious alternative: Rust. But I have created and maintained significant projects in a number of languages, including Pascal, C, Ruby, and JavaScript/TypeScript. I don’t think I would have been able to manage a project like this in my spare time if it had been written in one of these languages.

Haskell has a number of features that have been very helpful in developing pandoc:

Its

*algebraic data types*give us a very clean, ergonomic representation of a structured documentIts

*strong type system*, which gives you a compiler error if you don’t combine the types of things in the right way, allows one to make big changes to the program with confidence that you’re not breaking anything; the compiler will show you everything that needs to be changed, and when the code compiles, you are very often done. When working with languages without a strong type system, e.g. Python and JavaScript, the lack of these safeguards always make me afraid to make big changes, especially when I am maintaining code long after I’ve written it.Haskell is a

*pure*language; nothing can have side effects that aren’t explicitly allowed for in the types. If you have a pure function, you know it won’t create a file or delete one or make a web request or launch missiles or change a global variable. This is extremely useful for preventing bugs. In pandoc we also use it to give us a really strong guarantee that, when run in sandbox mode, the readers and writers won’t touch the file system.The choice of Haskell has also led to a high quality and low volume of contributors (a combination that is good for a project without a lot of resources).


From what I have seen, Rust appears to have many of the good
features of Haskell, while producing faster, more
memory-efficient, and more compact code. But Haskell still strikes
me as more “ergonomic,” better suited to express abstractions, and
just closer to the ideal of a language that helps the developer
*think*.

## Whither Pandoc

I plan to continue improving pandoc. There are many ways in which it can be improved. But sometimes I wonder how long such a tool will continue to be necessary.

Just as current LLMs can do a very good job translating from one human language to another, they can do a decent job translating from one document format to another. In my small tests, ChatGPT did a good job translating from Markdown to HTML, and a decent (but notably worse) job converting to reStructuredText. My guess is that you could write a document in a light markup language you just had invented, and an LLM could do a decent job guessing your intent and translating it to HTML or another format.

Perhaps, then, in the future, people will no longer have a need for tools like pandoc. As things stand now, though, I think that using pandoc to convert texts has several large advantages over relying on an LLM. The first is ecological; it simply requires far less energy for the same conversion. The second is that pandoc’s output is deterministic; if you convert your text with pandoc, you’ll always get the same result, and you’ll be able to predict what that result is. The third is that, for the moment at least, pandoc’s conversions are going to be more reliable. But that could change in the coming years. Indeed, a time may come when LLMs can produce more reliable conversions than pandoc or anything that works like it.

In designing the commonmark spec, we had the goal of interpreting complex strings in the way that a human would naturally interpret them. This turns out to be quite difficult to achieve: witness the complex rules for emphasis. What we found is that, no matter how complex we made the rules for nested emphasis, it was always possible to come up with cases where the algorithm diverges from the meaning a human would naturally find in the string. In such cases, I would often remark, “until our programs have AI, we are going to have edge cases like this; at some point we have to accept that and stop trying to develop more complex rules.” Interestingly, now we do have tools that can understand (or at least simulate understanding) of the meaning and intent of the text, and can potentially do better at recognizing the formatting intended by the author than any light markup syntax that could be designed.

Whatever the future may bring, I am proud of the 20-year
history of this project, which has saved people all over the world
countless hours of drudgery. *Happy 20th birthday,
pandoc!*

In honor of this occasion, I have produced some pandoc mugs and stickers: