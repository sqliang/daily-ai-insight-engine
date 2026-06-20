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
pipeline_stage: ingested
id: c253faf4fbc7c43d
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