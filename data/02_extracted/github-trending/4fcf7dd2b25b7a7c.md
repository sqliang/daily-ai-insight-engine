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