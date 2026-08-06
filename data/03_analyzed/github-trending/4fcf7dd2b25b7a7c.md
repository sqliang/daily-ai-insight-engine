---
title: firecrawl/pdf-inspector
source: https://github.com/firecrawl/pdf-inspector
author: []
published: ''
created: '2026-08-04'
manifest_dates:
- '2026-08-04'
- '2026-08-05'
description: 'Fast Rust library for PDF inspection, classification, and text extraction.
  Intelligently detects scanned vs text-based PDFs to enable smart routing decisions.pdf-inspector
  Fast Rust library for PDF classification and text extraction. Detects whether a
  PDF is text-based or scanned, extracts text with position awareness, and converts
  to clean Markdown — all without OCR. Includes bindings for Python, Node.js, and
  browser WebAssembly. Built by Firecrawl to handle text-based PDFs locally in under
  200ms, skipping expensive OCR services for the ~54% of PDFs that don''t need them.
  Features Smart classification — Detect TextBased, Scanned, ImageBased, or Mixed
  PDFs in ~10-50ms by sampling content streams. Returns a confidence score (0.0-1.0)
  and per-page OCR routing. Text extraction — Position-aware extraction with font
  info, X/Y coordinates, and automatic multi-column reading order. Markdown conversion
  — Headings (H1-H4 via font size ratios), bullet/numbered/letter lists, code blocks
  (monospace font detection), tables (rectangle-based and heuristic), bold/italic
  formatting, URL linking, and page breaks. Table detection — Dual-mode: rectangle-based
  detection from PDF drawing ops, plus heuristic detection from text alignment. Handles
  financial tables, footnotes, and continuation tables across pages. CID font support
  — ToUnicode CMap decoding for Type0/Identity-H fonts, UTF-16BE, UTF-8, and Latin-1
  encodings. Multi-column layout — Automatic detection of newspaper-style columns,
  sequential reading order, and RTL text support. Encoding issue detection — Automatically
  flags broken font encodings so callers can fall back to OCR. Single document load
  — The document is parsed once and shared between detection and extraction, avoiding
  redundant I/O. Browser WebAssembly — Run the same Rust parser locally in browsers
  and Web Workers, with embedded CMaps and no server round trip. Lightweight — Pure
  Rust, no ML models, no external services. Single dependency on lopdf for PDF parsing.
  Benchmark Evaluated on the opendataloader-bench corpus (200 PDFs). Only local engines
  without model-based PDF parsing are shown; OCR was disabled. Scores are 0-1, higher
  is better. Engine Overall Reading Order (NID) Tables (TEDS) Headings (MHS) Speed
  (200 docs) pdf-inspector 0.875 0.915 0.814 0.788 0.470s liteparse 0.873 0.913 0.693
  0.811 0.750s opendataloader 0.831 0.902 0.489 0.739 2.569s pymupdf4llm 0.735 0.886
  0.401 0.424 17.117s markitdown 0.589 0.844 0.273 0.000 16.165s Results were refreshed
  on July 31, 2026, on an Apple M4 Pro. Engine versions were pdf-inspector 0.2.6,
  LiteParse 2.10.1, OpenDataLoader 2.2.1, PyMuPDF4LLM 0.2.0, and MarkItDown 0.1.5.
  Speed is the median of five alternating or rotating complete corpus runs after an
  excluded warm-up run, with each parser processing documents sequentially in a single
  process. The complete parser configuration, per-document predictions, evaluator
  output, and generated charts are available in the reproducible results branch. Best
  fit: Native-text PDFs where speed, reading order, and table structure matter. In
  this comparison, pdf-inspector delivered the higher overall, reading-order, and
  table scores, along with the fastest complete run. That makes it a strong local
  default for reports, research papers, financial documents, invoices, and legal PDFs
  that need clean, structured Markdown without adding OCR latency or infrastructure.
  Use the paired benchmark harness to compare two local builds against the exact same
  corpus and evaluator revision. Quick start Python pip install maturin maturin develop
  --release import pdf_inspector result = pdf_inspector.process_pdf("document.pdf")
  print(result.pdf_type) # "text_based", "scanned", "image_based", "mixed" print(result.markdown)
  # Markdown string or None Full API reference: docs/python.md Node.js npm install
  @firecrawl/pdf-inspector import { readFileSync } from ''fs''; import { processPdf,
  classifyPdf } from ''@firecrawl/pdf-inspector''; const result = processPdf(readFileSync(''document.pdf''));
  console.log(result.pdfType); // "TextBased", "Scanned", "ImageBased", "Mixed" console.log(result.markdown);
  // Markdown string or null Full API reference: napi/README.md Browser WebAssembly
  npm install @firecrawl/pdf-inspector-wasm import init, { processPdf } from ''@firecrawl/pdf-inspector-wasm'';
  await init(); const response = await fetch(''/document.pdf''); const pdf = new Uint8Array(await
  response.arrayBuffer()); const result = processPdf(pdf); console.log(result.pdfType);
  console.log(result.markdown); Full API reference: wasm/README.md Rust Install from
  crates.io: cargo add pdf-inspector Or add it manually: [dependencies] pdf-inspector
  = "0.1" use pdf_inspector::process_pdf; let result = process_pdf("document.pdf")?;
  println!("Type: {:?}", result.pdf_type); if let Some(markdown) = &result.markdown
  { println!("{}", markdown); } Full API reference: docs/rust-api.md CLI # Install
  the CLI tools cargo install pdf-inspector # Convert PDF to Markdown pdf2md document.pdf
  # JSON output (for piping) pdf2md document.pdf --json # Positioned TextItem JSON,
  including is_underline metadata pdf2md document.pdf --items-json # Raw markdown
  only (no headers) pdf2md document.pdf --raw # Token-efficient output (collapses
  long dot leaders and similar source padding) pdf2md document.pdf --compact # Insert
  page break markers (<!-- Page N -->) pdf2md document.pdf --pages # Process only
  specific pages pdf2md document.pdf --select-pages 1,3,5-10 # Detection only (no
  extraction) detect-pdf document.pdf detect-pdf document.pdf --json # Detection +
  layout analysis (tables, columns) detect-pdf document.pdf --analyze --json From
  a source checkout, use cargo run --bin pdf2md -- document.pdf or cargo run --bin
  detect-pdf -- document.pdf instead. Architecture PDF bytes │ ├─► detector → PdfType
  (TextBased / Scanned / ImageBased / Mixed) │ └─► extractor ├─ fonts → font widths,
  encodings ├─ content_stream → walk PDF operators → TextItems + PdfRects ├─ xobjects
  → Form XObject text, image placeholders ├─ links → hyperlinks, AcroForm fields └─
  layout → column detection → line grouping → reading order │ ├─► tables │ ├─ detect_rects
  → rectangle-based tables (union-find) │ ├─ detect_heuristic → alignment-based tables
  │ ├─ grid → column/row assignment → cells │ └─ format → cells → Markdown table │
  └─► markdown ├─ analysis → font stats, heading tiers ├─ preprocess → merge headings,
  drop caps ├─ convert → line loop + table/image insertion ├─ classify → captions,
  lists, code └─ postprocess → cleanup → final Markdown The document is loaded once
  via load_document_from_path / load_document_from_mem and shared between the detection
  and extraction stages, so there''s no redundant parsing. Project structure src/
  lib.rs — Public API, PdfOptions builder, convenience functions python.rs — PyO3
  Python bindings types.rs — Shared types: TextItem, TextLine, PdfRect, ItemType text_utils.rs
  — Character/text helpers (CJK, RTL, ligatures, bold/italic) process_mode.rs — ProcessMode
  enum (DetectOnly, Analyze, Full) detector.rs — Fast PDF type detection without full
  document load glyph_names.rs — Adobe Glyph List → Unicode mapping tounicode.rs —
  ToUnicode CMap parsing for CID-encoded text extractor/ — Text extraction pipeline
  tables/ — Table detection and formatting markdown/ — Markdown conversion and structure
  detection bin/ — CLI tools (pdf2md, detect_pdf) napi/ — Node.js/Bun bindings (napi-rs)
  wasm/ — Browser bindings (wasm-bindgen) How classification works Parse the xref
  table and page tree (no full object load) Select pages based on ScanStrategy (default:
  all pages with early exit) Look for Tj/TJ (text operators) and Do (image operators)
  in content streams Classify based on text operator presence across sampled pages
  This detects 300+ page PDFs in milliseconds. The result includes pages_needing_ocr
  — a list of specific page numbers that lack text, enabling per-page OCR routing
  instead of all-or-nothing. Scan strategies Strategy Behavior Best for EarlyExit
  (default) Scan all pages, stop on first non-text page Pipelines routing TextBased
  PDFs to fast extraction Full Scan all pages, no early exit Accurate Mixed vs Scanned
  classification Sample(n) Sample n evenly distributed pages (first, last, middle)
  Very large PDFs where speed matters more than precision Pages(vec) Only scan specific
  1-indexed page numbers When the caller knows which pages to check Markdown output
  The converter handles: Element How it''s detected Headings (H1-H4) Font size tiers
  relative to body text, with 0.5pt clustering Bold/italic Font name patterns (Bold,
  Italic, Oblique) Bullet lists *, -, *, ○, ●, ◦ prefixes Numbered lists 1., 1), (1)
  patterns Letter lists a., a), (a) patterns Code blocks Monospace fonts (Courier,
  Consolas, Monaco, Menlo, Fira Code, JetBrains Mono) and keyword detection Tables
  Rectangle-based detection from PDF drawing ops + heuristic detection from text alignment
  Financial tables Token splitting for consolidated numeric values Captions "Figure",
  "Table", "Source:" prefix detection Sub/superscript Font size and Y-offset relative
  to baseline URLs Converted to Markdown links Hyphenation Rejoins words broken across
  lines Page numbers Filtered from output Drop caps Large initial letters merged with
  following text Dot leaders TOC-style dots collapsed to " ... " Use case: smart PDF
  routing pdf-inspector was built for pipelines that process PDFs at scale. Instead
  of sending every PDF through OCR: PDF arrives → pdf-inspector classifies it (~20ms)
  → TextBased + high confidence? YES → extract locally (~150ms), done NO → send to
  OCR service (2-10s) This saves cost and latency for the majority of PDFs that are
  already text-based (reports, papers, invoices, legal docs). Debugging See docs/debugging.md
  for RUST_LOG environment variable usage. License MIT'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 4fcf7dd2b25b7a7c
source_type: community_discussion
tldr: Firecrawl 发布开源 Rust 库 pdf-inspector，可在 10-50ms 内分类 PDF 类型（文本/扫描/图片/混合），约 200ms
  本地提取文本并转 Markdown，无需 OCR。支持 Python、Node.js、WebAssembly 与 Rust 绑定，在 opendataloader-bench
  评测中综合得分 0.875 且速度最快。
objective_summary: Firecrawl 在 GitHub 发布开源项目 pdf-inspector，这是一个纯 Rust 实现的 PDF 分类与文本提取库，仅依赖
  lopdf，不含机器学习模型。它通过采样内容流在约 10-50ms 内判定 PDF 类型并返回置信度，随后在本地约 200ms 内完成带位置感知的文本提取与 Markdown
  转换。该项目提供 Python、Node.js、浏览器 WebAssembly、Rust crate 及 CLI 工具等绑定。在 opendataloader-bench
  语料库（200 个 PDF）上，pdf-inspector 综合得分 0.875、处理耗时 0.470 秒，均优于 liteparse、opendataloader
  等本地对比引擎。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Firecrawl
  technologies:
  - WebAssembly
  - PyO3
  - napi-rs
  - wasm-bindgen
  - ToUnicode CMap
  - CID
  - OCR
  - lopdf
  key_people: []
key_logic_flow:
- pdf-inspector 是 Firecrawl 开发的开源 Rust 库，核心功能是 PDF 类型分类、位置感知文本提取与 Markdown 转换。
- 检测阶段通过采样内容流中的文本与图像操作符，在约 10-50 毫秒内将 PDF 分类为文本型、扫描件、图片型或混合型，并返回置信度与需要 OCR 的页号列表。
- 提取阶段将文档只解析一次，检测与提取共享结果，支持多栏阅读顺序、矩形与启发式表格检测、CID 字体解码、URL 链接和代码块识别等特性。
- 该项目提供 Python、Node.js、浏览器 WebAssembly、Rust crate 与 CLI 工具等五种使用方式。
- 在 opendataloader-bench 语料库（200 个 PDF）评测中，pdf-inspector 综合得分 0.875、200 份文档处理耗时 0.470
  秒，均优于 liteparse、opendataloader 等本地引擎。
- 设计目标是让流水线先对 PDF 分类，文本型且高置信度的在本地快速提取，其余才送往 OCR 服务，从而节省成本与延迟。
object_mentions:
- object_type: project
  name: firecrawl/pdf-inspector
  canonical_name: firecrawl/pdf-inspector
  url: https://github.com/firecrawl/pdf-inspector
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - pdf-inspector 是 Firecrawl 开发的开源 Rust 库，用于 PDF 分类和文本提取，可判定 PDF 是文本型还是扫描件并转换为 Markdown。
  - 在 opendataloader-bench 语料库 200 个 PDF 的评测中，pdf-inspector 综合得分 0.875，处理 200 份文档耗时
    0.470 秒，为对比引擎中最高分与最快速度。
  - 该库提供 Python、Node.js、浏览器 WebAssembly、Rust crate 与 CLI 工具等五种使用方式。
  article_id: 4fcf7dd2b25b7a7c
- object_type: product
  name: pdf2md
  canonical_name: pdf2md
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - 通过 cargo install pdf-inspector 可安装 CLI 工具，用 pdf2md 命令将 PDF 转为 Markdown 或 JSON
    输出，支持 --select-pages 与 --compact 等参数。
  article_id: 4fcf7dd2b25b7a7c
- object_type: product
  name: '@firecrawl/pdf-inspector'
  canonical_name: '@firecrawl/pdf-inspector'
  url: https://www.npmjs.com/package/@firecrawl/pdf-inspector
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 通过 npm install @firecrawl/pdf-inspector 安装后，可在 Node.js 中调用 processPdf 与 classifyPdf
    函数处理 PDF 文件并输出 Markdown。
  article_id: 4fcf7dd2b25b7a7c
- object_type: product
  name: '@firecrawl/pdf-inspector-wasm'
  canonical_name: '@firecrawl/pdf-inspector-wasm'
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 通过 npm install @firecrawl/pdf-inspector-wasm 可在浏览器与 Web Worker 中本地运行同一套 Rust 解析器，无需服务器往返。
  article_id: 4fcf7dd2b25b7a7c
- object_type: project
  name: LiteParse
  canonical_name: LiteParse
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在评测中，LiteParse 2.10.1 的综合得分为 0.873，200 份文档处理耗时 0.750 秒，整体表现最接近 pdf-inspector。
  article_id: 4fcf7dd2b25b7a7c
- object_type: project
  name: OpenDataLoader
  canonical_name: OpenDataLoader
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在评测中，OpenDataLoader 2.2.1 的综合得分为 0.831，处理 200 份文档耗时 2.569 秒，表格识别得分仅 0.489。
  article_id: 4fcf7dd2b25b7a7c
- object_type: project
  name: PyMuPDF4LLM
  canonical_name: PyMuPDF4LLM
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在评测中，PyMuPDF4LLM 0.2.0 的综合得分为 0.735，处理 200 份文档耗时 17.117 秒，速度明显慢于 pdf-inspector。
  article_id: 4fcf7dd2b25b7a7c
- object_type: project
  name: MarkItDown
  canonical_name: MarkItDown
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 在评测中，MarkItDown 0.1.5 的综合得分为 0.589，标题识别得分为 0.000，处理 200 份文档耗时 16.165 秒。
  article_id: 4fcf7dd2b25b7a7c
extract_result: success
impact_score:
  score: 6.5
  reason: 该工具精准击中了 RAG/Agent 数据接入流水线的高频痛点——PDF 解析，在质量与速度上实现了数量级领先（200 份文档 0.47s，而
    pymupdf4llm 需 17s、markitdown 需 16s），且分类+提取的单次解析架构、无需 OCR 的设计对文档处理成本结构有实质影响。但本质仍是一款单一开源库的发布，未触及模型或平台层格局，冲击范围集中在文档处理与工程社区，尚达不到范式转移级别，故给
    6.5 分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 本地免 OCR 的 PDF→Markdown 处理速度与质量，以及基准评测结果的可复现性是否属实
hype_assessment:
  level: low
  reason: 全文基于可复现的基准评测展开：明确给出引擎版本号（0.2.6）、测试硬件（Apple M4 Pro）、评测口径（5 次交替运行取中位数、预热排除、OCR
    禁用）以及 reproducible results 分支，通篇未见'颠覆/革命性'等 PR 滥用词汇，数据务实，属于实打实的工程干货。
information_entropy: high
domain_disruption:
  technical_innovation: 纯 Rust 实现、仅依赖 lopdf 的轻量架构：通过采样内容流中的文本/图像操作符在 10-50ms 内完成 PDF
    分类并返回置信度与逐页 OCR 路由，检测与提取共享单次文档解析；位置感知提取支持多栏阅读顺序、RTL、CID/ToUnicode CMap 字体解码、矩形+启发式双模表格检测，并能自动标记编码异常引导
    OCR 兜底——整个链路无需任何 ML 模型即达到高质量结构化输出。
  business_model: 对 Firecrawl 而言这是成本护城河：约 54% 的文本型 PDF 可在本地 200ms 内完成转换，直接削减 OCR 服务的调用量、成本与延迟；对生态而言，该库将
    PDF→Markdown 基础设施化并开源商品化，显著降低 RAG/Agent 数据接入对付费 OCR API 的依赖，利好自建文档处理管线的边际成本优化。
engineering_complexity: production_ready
compound_value:
  score: 6.0
  reason: 从复利视角看，PDF 解析是 AI 文档流水线（RAG、Agent、企业知识库）中最高频、最刚需的预处理环节，技术面优势可量化且显著：在 opendataloader-bench
    200 份文档上综合 0.875 分且耗时仅 0.470s，比 pymupdf4llm 快约 36 倍、比 markitdown 快约 34 倍，且分类→本地提取→OCR
    兜底的路由设计直接命中'约 54% 文本型 PDF 无需 OCR'的成本痛点。但护城河偏弱：纯 Rust、仅依赖 lopdf、无 ML 模型，复刻门槛低，且面临
    Microsoft MarkItDown 等大厂生态竞争，商业化变现依赖 Firecrawl 自身平台整合。长期复利取决于能否被 LangChain/LlamaIndex
    等 Agent 框架默认采纳成为细分基础设施——当前证据支持'有潜力但需持续验证'的定位，故给 6.0 而非更高分。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Firecrawl
- LangChain
- LlamaIndex
- Pinecone
- Qdrant
competitive_casualty:
- Microsoft MarkItDown
- PyMuPDF (pymupdf4llm)
- 商业 OCR 服务（AWS Textract / Google Document AI）
- liteparse
- opendataloader
market_opportunities:
- RAG/文档智能流水线团队可将 pdf-inspector 作为本地前置解析层：先分类 PDF，文本型（约 54%）在本地毫秒级提取为 Markdown，仅对扫描件路由到
  OCR 服务，可显著降低文档处理的成本与延迟。
- WebAssembly 绑定支持在浏览器与 Web Worker 中直接解析 PDF，可催生完全客户端化的文档分析产品，如本地优先、隐私合规的文档问答与检索工具，规避数据出境风险。
- 该库在表格提取（TEDS 0.814）与阅读顺序还原上的领先表现，适合金融报表、发票、法律文书等结构化文档场景，可围绕其构建垂直领域的文档清洗与知识抽取增值服务。
risk_matrix:
  regulatory: 无直接监管风险；本地处理反而降低数据出境合规压力。但若将该能力包装为云端服务处理含个人信息的文档，仍需遵守《个人信息保护法》等数据保护法规。
  technological: 纯 Rust 无 OCR 方案对扫描件/图片型 PDF 无能为力，依赖分类置信度正确路由，误判可能造成内容静默丢失；项目仍处 0.2.x
    早期版本，仅依赖单一 lopdf 解析库，长期维护性与 PDF 格式兼容性存在不确定性。
  competitive: 微软 MarkItDown、PyMuPDF4LLM、LiteParse 等本地解析引擎竞争激烈，且大厂可能将原生 PDF 解析能力内置到各自平台（如
    Office/AI 助手），挤压独立开源库的生态位；Firecrawl 作为商业公司，存在以开源项目作获客漏斗的策略风险。
  ethical: 文本提取质量直接决定下游 LLM 应用的数据完整性，分类置信度误判会导致内容被丢弃或错误路由，形成'垃圾进垃圾出'的连锁偏差；涉及敏感文档时，提取结果在工具链中的流转需明确隐私边界。
  additional:
  - 基准测试由 Firecrawl 自报（自家基准线、自家引擎版本 0.2.6），存在评测偏差与自我选择效应，需第三方复测验证。
  - 项目维护集中于单一商业公司，bus factor 低，若公司战略转向可能影响开源可持续性与接口稳定性。
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: firecrawl/pdf-inspector
  canonical_name: firecrawl/pdf-inspector
  url: https://github.com/firecrawl/pdf-inspector
  positioning: Firecrawl 开源的高性能 Rust PDF 解析库，无需 OCR 即可在本地完成文本型 PDF 的分类、位置感知文本提取与 Markdown
    转换。
  technical_signal: 纯 Rust 实现、仅依赖 lopdf，通过采样内容流约 10-50 毫秒完成 PDF 类型分类，支持多栏阅读顺序、表格检测与
    CID 字体解码。
  adoption_signal: 提供 Python、Node.js、浏览器 WebAssembly、Rust crate 与 CLI 工具五种使用方式，在 opendataloader-bench
    评测中综合得分 0.875 且速度最快。
  ecosystem_relevance: 作为 Firecrawl 生态的开源组件，与网页抓取流水线互补，让文本型 PDF 在本地快速处理并降低对 OCR 服务的依赖。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: pdf-inspector 在 PDF 解析这一高频数据管线环节展现出显著的速度与质量优势，其分类优先路由的设计有望降低本地文档处理的成本结构，值得持续跟踪其在真实业务场景的采用与版本演进。
  risk_notes:
  - 该库明确不做 OCR，扫描件与图片型 PDF 仍需依赖外部 OCR 服务，能力边界需要调用方自行评估。
  - 评测基于 opendataloader-bench 单一语料库与 M4 Pro 环境，跨文档类型与平台的实际表现仍需更多验证。
  score: 8.0
  article_ids:
  - 4fcf7dd2b25b7a7c
  evidence_snippets:
  - pdf-inspector 是 Firecrawl 开发的开源 Rust 库，用于 PDF 分类和文本提取，可判定 PDF 是文本型还是扫描件并转换为 Markdown。
  - 在 opendataloader-bench 语料库 200 个 PDF 的评测中，pdf-inspector 综合得分 0.875，处理 200 份文档耗时
    0.470 秒，为对比引擎中最高分与最快速度。
  - 该库提供 Python、Node.js、浏览器 WebAssembly、Rust crate 与 CLI 工具等五种使用方式。
- object_type: project
  name: LiteParse
  canonical_name: LiteParse
  url: null
  positioning: LiteParse 是 PDF 解析领域的一款本地引擎，在 opendataloader-bench 评测中综合得分 0.873，为最接近
    pdf-inspector 的竞品。
  technical_signal: 综合得分 0.873、阅读顺序 0.913、标题识别 0.811 均处第一梯队，但表格识别 0.693 明显落后于 pdf-inspector
    的 0.814。
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: LiteParse 综合得分 0.873 与 pdf-inspector 仅差 0.002，是当前最接近的本地竞品，其标题识别优势与表格短板并存，后续版本演进将直接影响本地
    PDF 解析竞争格局。
  risk_notes:
  - 评测仅覆盖 opendataloader-bench 单一语料库与单台硬件环境，结论外推需谨慎。
  - 文章未披露 LiteParse 的架构细节与社区采用情况，可观测信息有限。
  score: 4.0
  article_ids:
  - 4fcf7dd2b25b7a7c
  evidence_snippets:
  - 在评测中，LiteParse 2.10.1 的综合得分为 0.873，200 份文档处理耗时 0.750 秒，整体表现最接近 pdf-inspector。
- object_type: project
  name: OpenDataLoader
  canonical_name: OpenDataLoader
  url: null
  positioning: OpenDataLoader 是本地 PDF 解析引擎之一，在 opendataloader-bench 评测中综合得分 0.831
    位居中游，表格识别能力明显偏弱。
  technical_signal: 综合得分 0.831 居中游，表格识别 0.489 是主要短板，200 份文档处理耗时 2.569 秒，速度落后于第一梯队。
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: OpenDataLoader 以 0.831 综合得分处于评测中游，表格识别 0.489 与 2.569 秒耗时构成清晰改进方向，其针对表格与速度的后续优化将决定能否追赶第一梯队。
  risk_notes:
  - 表格识别得分仅 0.489，在金融表格与发票等结构化文档场景下的可用性存在明显风险。
  - 文章未披露其架构细节与社区规模，信息不足以评估长期生命力。
  score: 3.0
  article_ids:
  - 4fcf7dd2b25b7a7c
  evidence_snippets:
  - 在评测中，OpenDataLoader 2.2.1 的综合得分为 0.831，处理 200 份文档耗时 2.569 秒，表格识别得分仅 0.489。
- object_type: project
  name: PyMuPDF4LLM
  canonical_name: PyMuPDF4LLM
  url: null
  positioning: PyMuPDF4LLM 是面向 LLM 文档处理的 PDF 转 Markdown 引擎，在评测中综合得分 0.735，速度明显落后于
    pdf-inspector。
  technical_signal: 综合得分 0.735，阅读顺序 0.886 尚可，但表格识别 0.401 与标题识别 0.424 偏弱，200 份文档处理耗时
    17.117 秒。
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: PyMuPDF4LLM 在评测中综合得分 0.735、处理耗时 17.117 秒，暴露出既有方案在效率与结构还原上的瓶颈，其后续版本表现可作为衡量本地解析竞争演进的参照。
  risk_notes:
  - 表格与标题识别得分均低于 0.43，复杂文档结构还原能力可能不稳定。
  - 处理 200 份文档耗时 17 秒，吞吐量不足将限制其在规模化管线中的使用。
  score: 3.0
  article_ids:
  - 4fcf7dd2b25b7a7c
  evidence_snippets:
  - 在评测中，PyMuPDF4LLM 0.2.0 的综合得分为 0.735，处理 200 份文档耗时 17.117 秒，速度明显慢于 pdf-inspector。
- object_type: project
  name: MarkItDown
  canonical_name: MarkItDown
  url: null
  positioning: MarkItDown 是文档转 Markdown 的解析引擎，在 opendataloader-bench 评测中综合得分 0.589
    居末位，结构化还原能力严重不足。
  technical_signal: 综合得分 0.589 居对比末位，标题识别得分 0.000、表格识别 0.273，处理 200 份文档耗时 16.165 秒，结构与速度均落后。
  adoption_signal: null
  ecosystem_relevance: null
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: MarkItDown 在评测中综合得分 0.589 居末位、标题识别得分为零，暴露出严重的结构还原短板，其作为对比基准的后续版本表现值得持续观察。
  risk_notes:
  - 标题识别得分 0.000 说明其 Markdown 标题层级生成基本失效，直接影响结构化输出质量。
  - 16 秒级处理耗时使其在规模化批量转换场景下效率堪忧。
  score: 2.0
  article_ids:
  - 4fcf7dd2b25b7a7c
  evidence_snippets:
  - 在评测中，MarkItDown 0.1.5 的综合得分为 0.589，标题识别得分为 0.000，处理 200 份文档耗时 16.165 秒。
---

Fast Rust library for PDF classification and text extraction. Detects whether a PDF is text-based or scanned, extracts text with position awareness, and converts to clean Markdown — all without OCR. Includes bindings for Python, Node.js, and browser WebAssembly.

Built by Firecrawl to handle text-based PDFs locally in under 200ms, skipping expensive OCR services for the ~54% of PDFs that don't need them.

**Smart classification**— Detect TextBased, Scanned, ImageBased, or Mixed PDFs in ~10-50ms by sampling content streams. Returns a confidence score (0.0-1.0) and per-page OCR routing.**Text extraction**— Position-aware extraction with font info, X/Y coordinates, and automatic multi-column reading order.**Markdown conversion**— Headings (H1-H4 via font size ratios), bullet/numbered/letter lists, code blocks (monospace font detection), tables (rectangle-based and heuristic), bold/italic formatting, URL linking, and page breaks.**Table detection**— Dual-mode: rectangle-based detection from PDF drawing ops, plus heuristic detection from text alignment. Handles financial tables, footnotes, and continuation tables across pages.**CID font support**— ToUnicode CMap decoding for Type0/Identity-H fonts, UTF-16BE, UTF-8, and Latin-1 encodings.**Multi-column layout**— Automatic detection of newspaper-style columns, sequential reading order, and RTL text support.**Encoding issue detection**— Automatically flags broken font encodings so callers can fall back to OCR.**Single document load**— The document is parsed once and shared between detection and extraction, avoiding redundant I/O.**Browser WebAssembly**— Run the same Rust parser locally in browsers and Web Workers, with embedded CMaps and no server round trip.**Lightweight**— Pure Rust, no ML models, no external services. Single dependency on`lopdf`

for PDF parsing.

Evaluated on the opendataloader-bench corpus (200 PDFs). Only local engines without model-based PDF parsing are shown; OCR was disabled. Scores are 0-1, higher is better.

| Engine | Overall | Reading Order (NID) | Tables (TEDS) | Headings (MHS) | Speed (200 docs) |
|---|---|---|---|---|---|
| pdf-inspector | 0.875 |
0.915 |
0.814 |
0.788 | 0.470s |
| liteparse | 0.873 | 0.913 | 0.693 | 0.811 |
0.750s |
| opendataloader | 0.831 | 0.902 | 0.489 | 0.739 | 2.569s |
| pymupdf4llm | 0.735 | 0.886 | 0.401 | 0.424 | 17.117s |
| markitdown | 0.589 | 0.844 | 0.273 | 0.000 | 16.165s |

Results were refreshed on July 31, 2026, on an Apple M4 Pro. Engine versions were pdf-inspector 0.2.6, LiteParse 2.10.1, OpenDataLoader 2.2.1, PyMuPDF4LLM 0.2.0, and MarkItDown 0.1.5. Speed is the median of five alternating or rotating complete corpus runs after an excluded warm-up run, with each parser processing documents sequentially in a single process.

The complete parser configuration, per-document predictions, evaluator output, and generated charts are available in the reproducible results branch.

**Best fit:** Native-text PDFs where speed, reading order, and table structure matter. In this comparison, pdf-inspector delivered the higher overall, reading-order, and table scores, along with the fastest complete run. That makes it a strong local default for reports, research papers, financial documents, invoices, and legal PDFs that need clean, structured Markdown without adding OCR latency or infrastructure.

Use the paired benchmark harness to compare two local builds against the exact same corpus and evaluator revision.

```
pip install maturin
maturin develop --release
```

```
import pdf_inspector
result = pdf_inspector.process_pdf("document.pdf")
print(result.pdf_type) # "text_based", "scanned", "image_based", "mixed"
print(result.markdown) # Markdown string or None
```

Full API reference: docs/python.md


`npm install @firecrawl/pdf-inspector`

```
import { readFileSync } from 'fs';
import { processPdf, classifyPdf } from '@firecrawl/pdf-inspector';
const result = processPdf(readFileSync('document.pdf'));
console.log(result.pdfType); // "TextBased", "Scanned", "ImageBased", "Mixed"
console.log(result.markdown); // Markdown string or null
```

Full API reference: napi/README.md


`npm install @firecrawl/pdf-inspector-wasm`

```
import init, { processPdf } from '@firecrawl/pdf-inspector-wasm';
await init();
const response = await fetch('/document.pdf');
const pdf = new Uint8Array(await response.arrayBuffer());
const result = processPdf(pdf);
console.log(result.pdfType);
console.log(result.markdown);
```

Full API reference: wasm/README.md


Install from crates.io:

`cargo add pdf-inspector`

Or add it manually:

```
[dependencies]
pdf-inspector = "0.1"
```

```
use pdf_inspector::process_pdf;
let result = process_pdf("document.pdf")?;
println!("Type: {:?}", result.pdf_type);
if let Some(markdown) = &result.markdown {
println!("{}", markdown);
}
```

Full API reference: docs/rust-api.md


```
# Install the CLI tools
cargo install pdf-inspector
# Convert PDF to Markdown
pdf2md document.pdf
# JSON output (for piping)
pdf2md document.pdf --json
# Positioned TextItem JSON, including is_underline metadata
pdf2md document.pdf --items-json
# Raw markdown only (no headers)
pdf2md document.pdf --raw
# Token-efficient output (collapses long dot leaders and similar source padding)
pdf2md document.pdf --compact
# Insert page break markers (<!-- Page N -->)
pdf2md document.pdf --pages
# Process only specific pages
pdf2md document.pdf --select-pages 1,3,5-10
# Detection only (no extraction)
detect-pdf document.pdf
detect-pdf document.pdf --json
# Detection + layout analysis (tables, columns)
detect-pdf document.pdf --analyze --json
```

From a source checkout, use `cargo run --bin pdf2md -- document.pdf`

or `cargo run --bin detect-pdf -- document.pdf`

instead.

```
PDF bytes
│
├─► detector → PdfType (TextBased / Scanned / ImageBased / Mixed)
│
└─► extractor
├─ fonts → font widths, encodings
├─ content_stream → walk PDF operators → TextItems + PdfRects
├─ xobjects → Form XObject text, image placeholders
├─ links → hyperlinks, AcroForm fields
└─ layout → column detection → line grouping → reading order
│
├─► tables
│ ├─ detect_rects → rectangle-based tables (union-find)
│ ├─ detect_heuristic → alignment-based tables
│ ├─ grid → column/row assignment → cells
│ └─ format → cells → Markdown table
│
└─► markdown
├─ analysis → font stats, heading tiers
├─ preprocess → merge headings, drop caps
├─ convert → line loop + table/image insertion
├─ classify → captions, lists, code
└─ postprocess → cleanup → final Markdown
```


The document is loaded **once** via `load_document_from_path`

/ `load_document_from_mem`

and shared between the detection and extraction stages, so there's no redundant parsing.

```
src/
lib.rs — Public API, PdfOptions builder, convenience functions
python.rs — PyO3 Python bindings
types.rs — Shared types: TextItem, TextLine, PdfRect, ItemType
text_utils.rs — Character/text helpers (CJK, RTL, ligatures, bold/italic)
process_mode.rs — ProcessMode enum (DetectOnly, Analyze, Full)
detector.rs — Fast PDF type detection without full document load
glyph_names.rs — Adobe Glyph List → Unicode mapping
tounicode.rs — ToUnicode CMap parsing for CID-encoded text
extractor/ — Text extraction pipeline
tables/ — Table detection and formatting
markdown/ — Markdown conversion and structure detection
bin/ — CLI tools (pdf2md, detect_pdf)
napi/ — Node.js/Bun bindings (napi-rs)
wasm/ — Browser bindings (wasm-bindgen)
```


- Parse the xref table and page tree (no full object load)
- Select pages based on
`ScanStrategy`

(default: all pages with early exit) - Look for
`Tj`

/`TJ`

(text operators) and`Do`

(image operators) in content streams - Classify based on text operator presence across sampled pages

This detects 300+ page PDFs in milliseconds. The result includes `pages_needing_ocr`

— a list of specific page numbers that lack text, enabling per-page OCR routing instead of all-or-nothing.

| Strategy | Behavior | Best for |
|---|---|---|
`EarlyExit` (default) |
Scan all pages, stop on first non-text page | Pipelines routing TextBased PDFs to fast extraction |
`Full` |
Scan all pages, no early exit | Accurate Mixed vs Scanned classification |
`Sample(n)` |
Sample `n` evenly distributed pages (first, last, middle) |
Very large PDFs where speed matters more than precision |
`Pages(vec)` |
Only scan specific 1-indexed page numbers | When the caller knows which pages to check |

The converter handles:

| Element | How it's detected |
|---|---|
| Headings (H1-H4) | Font size tiers relative to body text, with 0.5pt clustering |
| Bold/italic | Font name patterns (Bold, Italic, Oblique) |
| Bullet lists | `*` , `-` , `*` , `○` , `●` , `◦` prefixes |
| Numbered lists | `1.` , `1)` , `(1)` patterns |
| Letter lists | `a.` , `a)` , `(a)` patterns |
| Code blocks | Monospace fonts (Courier, Consolas, Monaco, Menlo, Fira Code, JetBrains Mono) and keyword detection |
| Tables | Rectangle-based detection from PDF drawing ops + heuristic detection from text alignment |
| Financial tables | Token splitting for consolidated numeric values |
| Captions | "Figure", "Table", "Source:" prefix detection |
| Sub/superscript | Font size and Y-offset relative to baseline |
| URLs | Converted to Markdown links |
| Hyphenation | Rejoins words broken across lines |
| Page numbers | Filtered from output |
| Drop caps | Large initial letters merged with following text |
| Dot leaders | TOC-style dots collapsed to " ... " |

pdf-inspector was built for pipelines that process PDFs at scale. Instead of sending every PDF through OCR:

```
PDF arrives
→ pdf-inspector classifies it (~20ms)
→ TextBased + high confidence?
YES → extract locally (~150ms), done
NO → send to OCR service (2-10s)
```


This saves cost and latency for the majority of PDFs that are already text-based (reports, papers, invoices, legal docs).

See docs/debugging.md for `RUST_LOG`

environment variable usage.