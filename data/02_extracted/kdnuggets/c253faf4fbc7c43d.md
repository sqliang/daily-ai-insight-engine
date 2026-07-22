---
title: 5 Useful Python Scripts to Automate Boring PDF Tasks
source: https://www.kdnuggets.com/5-useful-python-scripts-to-automate-boring-pdf-tasks
author:
- '[[Bala Priya C]]'
published: '2026-06-10'
created: '2026-06-11'
description: PDFs are used everywhere, and these five Python scripts help you automate
  the most common PDF tasks.
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: c253faf4fbc7c43d
source_type: news_media
tldr: 本文介绍了5个用于自动化PDF处理的Python脚本，涵盖PDF合并与拆分、文本和表格提取、水印和页码添加等常见任务，全部基于pypdf和pdfplumber等库从命令行运行。
objective_summary: KDnuggets于2026年7月21日发布了一篇技术教程，详细介绍了5个自动化PDF处理的Python脚本。这些脚本使用pypdf和pdfplumber等库，支持从命令行运行和批量处理，覆盖了PDF合并与拆分、文本与表格提取为结构化文件、以及水印/页码/页眉页脚添加等常见操作，可通过配置文件调整行为。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - KDnuggets
  technologies:
  - pypdf
  - pdfplumber
  key_people: []
key_logic_flow:
- 第一个脚本使用pypdf库实现PDF合并与拆分功能，合并时按文件名排序顺序写入，拆分时支持按页范围列表、固定块大小或特定页码三种方式。
- 第二个脚本结合pypdf和pdfplumber从PDF中提取文本和表格数据，文本输出为纯文本或Markdown文件，表格输出为CSV或Excel格式。
- 第三个脚本支持对PDF批量添加文字或图片水印、页眉页脚和页码，所有参数均可配置，可处理整个文件夹。
- 所有脚本均设计为命令行运行并支持批量处理，旨在替代手动操作以提升重复性PDF处理任务的效率。
extract_result: success
object_mentions:
- object_type: project
  name: pypdf
  canonical_name: pypdf
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章第一个脚本使用pypdf进行所有页面级操作，在合并模式下从输入文件夹读取所有PDF并按文件名排序后顺序写入到一个输出文件中。
  - 文章第二个脚本使用pypdf进行基础文本提取，结合pdfplumber实现布局感知的文本和表格检测。
  article_id: c253faf4fbc7c43d
- object_type: project
  name: pdfplumber
  canonical_name: pdfplumber
  url: null
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 文章第二个脚本使用pdfplumber进行布局感知的提取和表格检测，逐页运行并利用其表格查找器识别表格区域，提取的表格会经过空行移除和表头检测等规范化处理。
  article_id: c253faf4fbc7c43d
---

# 5 Useful Python Scripts to Automate Boring PDF Tasks

PDFs are used everywhere, and these five Python scripts help you automate the most common PDF tasks.



## # Introduction


PDF files are widely used in many workflows. You might need to merge reports, split large files, extract text or tables, add watermarks, or redact sensitive content. These are all routine tasks, but handling them manually for multiple files can be slow and error-prone. These five Python scripts automate the process. They run from the command line, support batch processing, and are easy to configure.


## # 1. Merging and Splitting PDF Files


#### // The Pain Point

Combining multiple PDF files into one, or splitting a large PDF into separate files by page range, are among the most common PDF tasks. Both are tedious to do manually, particularly when dealing with many files or large page counts.


#### // What the Script Does

Merges a folder of PDF files into a single output file in a configurable order, or splits a single PDF into separate files by fixed page ranges, every `N`

pages, or by a list of specific page numbers. Both operations are handled by the same script via a mode flag.


#### // How It Works

The script uses **pypdf** for all page-level operations. In merge mode, it reads all PDFs from an input folder, sorts them by filename (or a custom order defined in a text file), and writes them sequentially into a single output PDF. In split mode, it accepts either a page range list, a fixed chunk size, or a list of page numbers to split on. Each split segment is written to a numbered output file. Metadata from the first input file is preserved in merge mode.


## # 2. Extracting Text and Tables from PDFs


#### // The Pain Point

Getting usable data out of a PDF — whether it's text from a report or tabular data from a statement — is something that needs to happen before any further processing can occur. Copy-pasting from a PDF viewer is impractical for anything beyond a few pages, and the output is rarely clean.


#### // What the Script Does

Extracts text and tables from one or more PDF files and writes the results to structured output files. Text is written to plain text or markdown files. Tables are written to CSV or Excel, with one sheet per table found. Supports both text-based PDFs and basic layout-preserving extraction.


#### // How It Works

The script uses pypdf for basic text extraction and **pdfplumber** for layout-aware extraction and table detection. For each input file, it runs page by page, extracting text blocks and detecting table regions using pdfplumber's table finder. Extracted tables are normalized — empty rows removed, headers detected — and written to separate output files. A summary report lists how many pages and tables were found in each file, and flags any pages where extraction produced no output.


## # 3. Stamping, Watermarking, and Adding Page Numbers


#### // The Pain Point

Adding a watermark, a stamp, or page numbers to a batch of PDFs before distributing them is straightforward in concept but slow to do one file at a time through a graphical user interface (GUI). When the batch is large or the requirement is recurring, it needs automating.


#### // What the Script Does

Applies a text or image stamp to every page of one or more PDF files. Supports diagonal watermarks, header/footer text, page numbers, and image overlays. Position, font size, opacity, and color are all configurable. Processes entire folders in batch.


#### // How It Works