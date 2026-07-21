---
title: allenai/olmocr
source: https://github.com/allenai/olmocr
author: []
published: ''
created: '2026-07-02'
description: 'Toolkit for linearizing PDFs for LLM datasets/training A toolkit for
  converting PDFs and other image-based document formats into clean, readable, plain
  text format. Try the online demo: https://olmocr.allenai.org/ Features: Convert
  PDF, PNG, and JPEG based documents into clean Markdown Support for equations, tables,
  handwriting, and complex formatting Automatically removes headers and footers Convert
  into text with a natural reading order, even in the presence of figures, multi-column
  layouts, and insets Efficient, less than $200 USD per million pages converted (Based
  on a 7B parameter VLM, so it requires a GPU) News October 21, 2025 - v0.4.0 - New
  model release, boosts olmOCR-bench score by ~4 points using synthetic data and introduces
  RL training. August 13, 2025 - v0.3.0 - New model release, fixes auto-rotation detection,
  and hallucinations on blank documents. July 24, 2025 - v0.2.1 - New model release,
  scores 3 points higher on olmOCR-Bench, also runs significantly faster because it''s
  default FP8, and needs much fewer retries per document. July 23, 2025 - v0.2.0 -
  New cleaned up trainer code, makes it much simpler to train olmOCR models yourself.
  June 17, 2025 - v0.1.75 - Switch from sglang to vllm based inference pipeline, updated
  docker image to CUDA 12.8. May 23, 2025 - v0.1.70 - Official docker support and
  images are now available! See Docker usage May 19, 2025 - v0.1.68 - olmOCR-Bench
  launch, scoring 77.4. Launch includes 2 point performance boost in olmOCR pipeline
  due to bug fixes with prompts. Mar 17, 2025 - v0.1.60 - Performance improvements
  due to better temperature selection in sampling. Feb 25, 2025 - v0.1.58 - Initial
  public launch and demo. Benchmark olmOCR-Bench: We also ship a comprehensive benchmark
  suite covering over 7,000 test cases across 1,400 documents to help measure performance
  of OCR systems. ArXiv Oldscansmath Tables Oldscans Headers&footers Multicolumn Longtinytext
  Base Overall Mistral OCR API 77.2 67.5 60.6 29.3 93.6 71.3 77.1 99.4 72.0±1.1 Marker
  1.10.1 83.8 66.8 72.9 33.5 86.6 80.0 85.7 99.3 76.1±1.1 MinerU 2.5.4* 76.6 54.6
  84.9 33.7 96.6 78.2 83.5 93.7 75.2±1.1 DeepSeek-OCR 77.2 73.6 80.2 33.3 96.1 66.4
  79.4 99.8 75.7±1.0 Nanonets-OCR2-3B 75.4 46.1 86.8 40.9 32.1 81.9 93.0 99.6 69.5±1.1
  PaddleOCR-VL* 85.7 71.0 84.1 37.8 97.0 79.9 85.7 98.5 80.0±1.0 Infinity-Parser 7B*
  84.4 83.8 85.0 47.9 88.7 84.2 86.4 99.8 82.5±? Chandra OCR 0.1.0* 82.2 80.3 88.0
  50.4 90.8 81.2 92.3 99.9 83.1±0.9 olmOCR v0.4.0 83.0 82.3 84.9 47.7 96.1 83.7 81.9
  99.7 82.4±1.1 Installation System Dependencies You will need to install poppler-utils
  and additional fonts for rendering PDF images. Install dependencies (Ubuntu/Debian):
  sudo apt-get update sudo apt-get install poppler-utils ttf-mscorefonts-installer
  msttcorefonts fonts-crosextra-caladea fonts-crosextra-carlito gsfonts lcdf-typetools
  Python Installation Set up a conda environment and install olmocr. The requirements
  for running olmOCR are difficult to install in an existing python environment, so
  please do make a clean python environment to install into. conda create -n olmocr
  python=3.11 conda activate olmocr Choose the installation option that matches your
  use case: Option 1: Remote Inference (Lightweight) If you plan to use a remote vLLM
  server with the --server flag, install the base package: pip install olmocr This
  avoids installing heavy GPU dependencies like PyTorch (~2GB+). Option 2: Local GPU
  Inference Requirements: Recent NVIDIA GPU (tested on RTX 4090, L40S, A100, H100)
  with at least 12 GB of GPU RAM 30GB of free disk space For running inference with
  your own GPU: pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128
  # Recommended: Install flash infer for faster inference on GPU pip install https://download.pytorch.org/whl/cu128/flashinfer/flashinfer_python-0.2.5%2Bcu128torch2.7-cp38-abi3-linux_x86_64.whl
  Option 3: Beaker Cluster Execution For submitting jobs to Beaker clusters with the
  --beaker flag: pip install olmocr[beaker] Option 4: Benchmark Suite For running
  the olmOCR benchmark suite: pip install olmocr[bench] Combined Installation You
  can combine multiple options: # GPU + Beaker support pip install olmocr[gpu,beaker]
  --extra-index-url https://download.pytorch.org/whl/cu128 # GPU + Benchmark support
  pip install olmocr[gpu,bench] --extra-index-url https://download.pytorch.org/whl/cu128
  Troubleshooting If you run into errors about too many open files, update your ulimit:
  ulimit -n 65536 Usage Examples For quick testing, try the web demo. Convert a Single
  PDF (Local GPU): # Download a sample PDF curl -o olmocr-sample.pdf https://olmocr.allenai.org/papers/olmocr_3pg_sample.pdf
  # Convert it to markdown olmocr ./localworkspace --markdown --pdfs olmocr-sample.pdf
  Convert an Image file: olmocr ./localworkspace --markdown --pdfs random_page.png
  Convert Multiple PDFs: olmocr ./localworkspace --markdown --pdfs tests/gnarly_pdfs/*.pdf
  Use Remote Inference Server: olmocr ./localworkspace --server http://remote-server:8000/v1
  --model allenai/olmOCR-2-7B-1025-FP8 --markdown --pdfs *.pdf With the --markdown
  flag, results will be stored as markdown files inside of ./localworkspace/markdown/.
  Note: You can also use python -m olmocr.pipeline instead of olmocr if you prefer.
  Viewing Results The ./localworkspace/ workspace folder will then have both Dolma
  and markdown files (if using --markdown). cat localworkspace/markdown/olmocr-sample.md
  olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models ... Using
  an Inference Provider or External Server If you have a vLLM server already running
  elsewhere (or any inference platform implementing the OpenAI API), you can point
  olmOCR to use it instead of spawning a local instance. Installation for Remote Inference:
  # Lightweight installation - no GPU dependencies needed pip install olmocr Using
  an External Server: # Use external vLLM server instead of local one olmocr ./localworkspace
  --server http://remote-server:8000/v1 --model allenai/olmOCR-2-7B-1025-FP8 --markdown
  --pdfs tests/gnarly_pdfs/*.pdf The served model name in vLLM needs to match the
  value provided in --model. Example vLLM Server Launch: vllm serve allenai/olmOCR-2-7B-1025-FP8
  --max-model-len 16384 Verified External Providers We have tested olmOCR-2-7B-1025-FP8
  on these external model providers and confirmed that they work $/1M Input tokens
  $/1M Output tokens Example Command Cirrascale $0.07 $0.15 olmocr ./workspace --server
  https://ai2endpoints.cirrascale.ai/api --api_key sk-XXXXXXX --workers 1 --max_concurrent_requests
  20 --model olmOCR-2-7B-1025 --pdfs tests/gnarly_pdfs/*.pdf DeepInfra $0.09 $0.19
  olmocr ./workspace --server https://api.deepinfra.com/v1/openai --api_key DfXXXXXXX
  --workers 1 --max_concurrent_requests 20 --model allenai/olmOCR-2-7B-1025 --pdfs
  tests/gnarly_pdfs/*.pdf Parasail $0.10 $0.20 olmocr ./workspace --server https://api.parasail.io/v1
  --api_key psk-XXXXX --workers 1 --max_concurrent_requests 20 --model allenai/olmOCR-2-7B-1025
  --pdfs tests/gnarly_pdfs/*.pdf Notes on arguments --server: Defines the OpenAI-compatible
  endpoint: ex https://api.deepinfra.com/v1/openai --api_key: Your API key, bassed
  in via Authorization Bearer HTTP header --max_concurrent_requests: Max concurrent
  requests that will be in-flight to the inference provider at one time --workers:
  Max number of page groups that will be processed at once. You may want to set this
  to 1 so that you finish one group of stuff before moving on. --pages_per_group:
  You may want a smaller number of pages per group as many external provides have
  lower concurrent request limits --model: The model identifier, ex. allenai/olmOCR-2-7B-1025,
  different providers have different names, and if you run locally, you can use olmocr
  Other arguments work the same as with local inference Multi-node / Cluster Usage
  If you want to convert millions of PDFs using multiple nodes running in parallel,
  olmOCR supports reading PDFs from AWS S3 and coordinating work using an AWS S3 output
  bucket. Start the first worker node: olmocr s3://my_s3_bucket/pdfworkspaces/exampleworkspace
  --pdfs s3://my_s3_bucket/jakep/gnarly_pdfs/*.pdf This sets up a simple work queue
  in your AWS bucket and starts converting PDFs. On subsequent worker nodes: olmocr
  s3://my_s3_bucket/pdfworkspaces/exampleworkspace They will automatically start grabbing
  items from the same workspace queue. Using Beaker for Cluster Execution If you are
  at Ai2 and want to linearize millions of PDFs efficiently using beaker, install
  with Beaker support: pip install olmocr[gpu,beaker] --extra-index-url https://download.pytorch.org/whl/cu128
  Then use the --beaker flag to prepare the workspace locally and launch N GPU workers
  in the cluster: olmocr s3://my_s3_bucket/pdfworkspaces/exampleworkspace --pdfs s3://my_s3_bucket/jakep/gnarly_pdfs/*.pdf
  --beaker --beaker_gpus 4 Using Docker Pull the Docker image (large, includes the
  model, ~30GB): docker pull alleninstituteforai/olmocr:latest-with-model For advanced
  users who want to manage their own model downloads, we also provide a base image
  without the model: docker pull alleninstituteforai/olmocr:latest Quick Start - Process
  PDFs Process a single PDF in your current directory: docker run --gpus all \ -v
  $(pwd):/workspace \ alleninstituteforai/olmocr:latest-with-model \ -c "olmocr /workspace/output
  --markdown --pdfs /workspace/sample.pdf" Process multiple PDFs: docker run --gpus
  all \ -v /path/to/pdfs:/input \ -v /path/to/output:/output \ alleninstituteforai/olmocr:latest-with-model
  \ -c "olmocr /output --markdown --pdfs /input/*.pdf" Interactive Mode Run the container
  interactively for exploration and debugging: docker run -it --gpus all alleninstituteforai/olmocr:latest-with-model
  Visit our Docker repository on Docker Hub for more information. Full Documentation
  To see all available options: olmocr --help usage: pipeline.py [-h] [--pdfs [PDFS
  ...]] [--model MODEL] [--workspace_profile WORKSPACE_PROFILE] [--pdf_profile PDF_PROFILE]
  [--pages_per_group PAGES_PER_GROUP] [--max_page_retries MAX_PAGE_RETRIES] [--max_page_error_rate
  MAX_PAGE_ERROR_RATE] [--workers WORKERS] [--apply_filter] [--stats] [--markdown]
  [--target_longest_image_dim TARGET_LONGEST_IMAGE_DIM] [--target_anchor_text_len
  TARGET_ANCHOR_TEXT_LEN] [--guided_decoding] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION]
  [--max_model_len MAX_MODEL_LEN] [--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--data-parallel-size
  DATA_PARALLEL_SIZE] [--port PORT] [--server SERVER] [--beaker] [--beaker_workspace
  BEAKER_WORKSPACE] [--beaker_cluster BEAKER_CLUSTER] [--beaker_gpus BEAKER_GPUS]
  [--beaker_priority BEAKER_PRIORITY] workspace Manager for running millions of PDFs
  through a batch inference pipeline positional arguments: workspace The filesystem
  path where work will be stored, can be a local folder, or an s3 path if coordinating
  work with many workers, s3://bucket/prefix/ options: -h, --help show this help message
  and exit --pdfs [PDFS ...] Path to add pdfs stored in s3 to the workspace, can be
  a glob path s3://bucket/prefix/*.pdf or path to file containing list of pdf paths
  --model MODEL Path where the model is located, allenai/olmOCR-7B-0725-FP8 is the
  default, can be local, s3, or hugging face. --workspace_profile WORKSPACE_PROFILE
  S3 configuration profile for accessing the workspace --pdf_profile PDF_PROFILE S3
  configuration profile for accessing the raw pdf documents --pages_per_group PAGES_PER_GROUP
  Aiming for this many pdf pages per work item group --max_page_retries MAX_PAGE_RETRIES
  Max number of times we will retry rendering a page --max_page_error_rate MAX_PAGE_ERROR_RATE
  Rate of allowable failed pages in a document, 1/250 by default --workers WORKERS
  Number of workers to run at a time --apply_filter Apply basic filtering to English
  pdfs which are not forms, and not likely seo spam --stats Instead of running any
  job, reports some statistics about the current workspace --markdown Also write natural
  text to markdown files preserving the folder structure of the input pdfs --target_longest_image_dim
  TARGET_LONGEST_IMAGE_DIM Dimension on longest side to use for rendering the pdf
  pages --target_anchor_text_len TARGET_ANCHOR_TEXT_LEN Maximum amount of anchor text
  to use (characters), not used for new models --guided_decoding Enable guided decoding
  for model YAML type outputs VLLM arguments: --gpu-memory-utilization GPU_MEMORY_UTILIZATION
  Fraction of VRAM vLLM may pre-allocate for KV-cache (passed through to vllm serve).
  --max_model_len MAX_MODEL_LEN Upper bound (tokens) vLLM will allocate KV-cache for,
  lower if VLLM won''t start --tensor-parallel-size TENSOR_PARALLEL_SIZE, -tp TENSOR_PARALLEL_SIZE
  Tensor parallel size for vLLM --data-parallel-size DATA_PARALLEL_SIZE, -dp DATA_PARALLEL_SIZE
  Data parallel size for vLLM --port PORT Port to use for the VLLM server --server
  SERVER URL of external vLLM (or other compatible provider) server (e.g., http://hostname:port).
  If provided, skips spawning local vLLM instance beaker/cluster execution: --beaker
  Submit this job to beaker instead of running locally --beaker_workspace BEAKER_WORKSPACE
  Beaker workspace to submit to --beaker_cluster BEAKER_CLUSTER Beaker clusters you
  want to run on --beaker_gpus BEAKER_GPUS Number of gpu replicas to run --beaker_priority
  BEAKER_PRIORITY Beaker priority level for the job Code overview There are some nice
  reusable pieces of the code that may be useful for your own projects: A prompting
  strategy to get really good natural text parsing using ChatGPT 4o - buildsilver.py
  Basic filtering by language and SEO spam removal - filter.py SFT Finetuning code
  for Qwen2.5-VL - train.py GRPO RL Trainer - grpo_train.py Synthetic data generation
  - mine_html_templates.py Processing millions of PDFs through a finetuned model using
  VLLM - pipeline.py Viewing Dolma docs created from PDFs - dolmaviewer.py Team olmOCR
  is developed and maintained by the AllenNLP team, backed by the Allen Institute
  for Artificial Intelligence (AI2). AI2 is a non-profit institute with the mission
  to contribute to humanity through high-impact AI research and engineering. To learn
  more about who specifically contributed to this codebase, see our contributors page.
  License olmOCR is licensed under Apache 2.0. A full copy of the license can be found
  on GitHub. Citing For olmOCR v1 and OlmOCR-bench: @misc{olmocrbench, title={{olmOCR:
  Unlocking Trillions of Tokens in PDFs with Vision Language Models}}, author={Jake
  Poznanski and Jon Borchardt and Jason Dunkelberger and Regan Huff and Daniel Lin
  and Aman Rangapur and Christopher Wilhelm and Kyle Lo and Luca Soldaini}, year={2025},
  eprint={2502.18443}, archivePrefix={arXiv}, primaryClass={cs.CL}, url={https://arxiv.org/abs/2502.18443},
  } For olmOCR v2 Unit Testing Rewards with RL: @misc{olmocr2, title={olmOCR 2: Unit
  Test Rewards for Document OCR}, author={Jake Poznanski and Luca Soldaini and Kyle
  Lo}, year={2025}, eprint={2510.19817}, archivePrefix={arXiv}, primaryClass={cs.CV},
  url={https://arxiv.org/abs/2510.19817}, }'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ae05babd8ff3098f
manifest_dates:
- '2026-07-02'
source_type: community_discussion
tldr: Allen AI 发布了 olmocr 开源工具包，基于 7B 参数视觉语言模型将 PDF 和图像文档转换为干净的 Markdown 文本，支持公式、表格、手写体和多栏布局，每百万页成本低于
  200 美元。
objective_summary: Allen Institute for AI (Allen AI) 在 GitHub 上开源了 olmocr 工具包，这是一个基于
  7B 参数 VLM 的 PDF 与图像文档转文本工具。该工具可将 PDF、PNG、JPEG 文档转换为干净的 Markdown 格式，支持公式、表格、手写体和多栏布局的自然阅读顺序，并自动去除页眉页脚。截至
  2025 年 10 月已发布 v0.4.0 版本，每百万页转换成本低于 200 美元。同时配套发布了 olmOCR-Bench 基准测试套件，覆盖 7000 多个测试用例和
  1400 份文档。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Allen Institute for AI (Allen AI)
  technologies:
  - VLM
  - OCR
  - vLLM
  - sglang
  - FP8
  key_people: []
key_logic_flow:
- Allen AI 发布了 olmocr 工具包，基于 7B 参数视觉语言模型将 PDF 和图像文档转换为干净的 Markdown 纯文本。
- olmocr 支持公式、表格、手写体和复杂格式排版，能自动去除页眉页脚并保持多栏布局的自然阅读顺序。
- 该工具转换效率极高，每百万页成本低于 200 美元，支持本地 GPU 推理、远程推理服务器、Docker 和 Beaker 集群等多种部署方式。
- 截至 2025 年 10 月已迭代至 v0.4.0 版本，通过合成数据和强化学习训练在 olmOCR-Bench 上提升了约 4 个百分点的评分。
- 配套发布了 olmOCR-Bench 基准测试套件，包含 7000 多个测试用例和 1400 份文档，用于衡量各 OCR 系统的性能表现。
- olmOCR v0.4.0 在 olmOCR-Bench 整体得分 82.4，在 ArXiv 数学公式、多栏布局等子项上表现优异。
object_mentions:
- object_type: project
  name: allenai/olmocr
  canonical_name: allenai/olmocr
  url: https://github.com/allenai/olmocr
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - Allen AI 开源的 olmocr 工具包，基于 7B 参数视觉语言模型将 PDF、PNG、JPEG 文档转换为干净的 Markdown 格式。
  - 支持公式、表格、手写体和复杂排版，自动去除页眉页脚并保持多栏布局的自然阅读顺序。
  - 转换效率每百万页成本低于 200 美元，支持本地 GPU、远程推理服务器和 Docker 等多种部署方式。
  article_id: ae05babd8ff3098f
- object_type: project
  name: olmOCR-Bench
  canonical_name: olmOCR-Bench
  url: null
  confidence: high
  article_role: ecosystem_context
  evidence_snippets:
  - olmOCR-Bench 是 Allen AI 配套发布的标准基准测试套件，覆盖 7000 多个测试用例和 1400 份文档。
  - 该基准测试涵盖 ArXiv 论文、数学公式、旧扫描件、表格、多栏布局等多个维度的 OCR 性能评估。
  - olmOCR v0.4.0 在 olmOCR-Bench 上整体得分为 82.4，在 ArXiv 数学、多栏布局等子项上表现优异。
  article_id: ae05babd8ff3098f
extract_result: success
impact_score:
  score: 5.8
  reason: AI2 开源的 olmOCR 是基于 7B VLM 的 PDF 转 Markdown 工具，在自研基准上综合得分 82.4，与现有方案（Chandra
    OCR 83.1、Infinity-Parser 82.5）处于同一梯队。虽然技术路线本身并不颠覆（VLM-based OCR 已有 DeepSeek-OCR、PaddleOCR-VL
    等），但 AI2 的品牌背书、低于 $200/百万页的低成本、以及完善的 Docker/API/S3 部署方案，使其成为实用的开源选择。该领域竞争格局已较为拥挤（Marker、MinerU、DeepSeek-OCR
    等），olmOCR 的加入会推动局部竞争但不会带来范式转移。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 7B VLM 实现的 OCR 准确率能否在实际业务中取代传统的多阶段 OCR 管线
hype_assessment:
  level: low
  reason: 项目文档提供了完整的 v0.1.58 到 v0.4.0 版本迭代日志、与 8 个竞品在 8 个子项上的详细基准对比（含置信区间）、以及明确的系统要求（12GB+
    显存）。没有使用'颠覆'、'革命性'等 PR 话术，技术指标透明可复现，属于实打实的干货。
information_entropy: high
domain_disruption:
  technical_innovation: 基于 7B 视觉语言模型实现 PDF→Markdown 的端到端转换，摒弃了传统 OCR 中版面分析→文字识别→后处理的多阶段管线设计。通过
    RL 训练和合成数据增强，在公式、表格、手写文字、多栏布局等复杂场景表现优异，FP8 推理大幅降低显存需求至 12GB。
  business_model: 开源免费 + 低于 $200/百万页的低成本，配合 Docker 一键部署和多家推理提供商（Cirrascale、DeepInfra、Parasail）的生态对接，可能倒逼商业化
    OCR API（如 Mistral OCR、Nanonets）降价，或将 PDF 结构化处理从按量付费的 API 调用模式推向本地自建的开源范式。
engineering_complexity: production_ready
compound_value:
  score: 6.5
  reason: olmOCR 定位于 PDF→Markdown 这一永久性基础设施需求，基于 7B VLM 的架构使其能受益于 VLM 能力的持续提升（复利效应），且
    <$200/百万页的成本结构极具经济吸引力。但 OCR 赛道竞争激烈（Mistral OCR、Marker、MinerU、PaddleOCR-VL、Chandra
    OCR 等均出现在基准对比中），AI2 作为非营利机构缺乏商业驱动的长期维护承诺，且基准得分并非绝对领先（82.4 vs Chandra OCR 83.1、Infinity-Parser
    82.5），因此长期复利价值存在不确定性。其真正的复利效应在于：随着 VLM 基础模型持续进化，VLM-based OCR 的质量天花板将持续上移，但这一收益并非
    olmOCR 独占。综合来看是有价值的开源基础设施组件，但难以形成商业层面的长期护城河。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- AI2
- vLLM project
- 开源 RAG 生态
competitive_casualty:
- Mistral OCR
- Nanonets
- Adobe Acrobat AI
market_opportunities:
- 企业可基于 olmOCR 搭建大规模文档数字化流水线，以低于每百万页 200 美元的成本将纸质档案、扫描件批量转为结构化 Markdown，直接用于知识库索引与
  RAG 检索增强生成系统
- 开发者可针对法律合同、医学论文、财务报表等垂直领域对 olmOCR 进行微调，打造专业文档解析 API 服务并收取 API 调用费用
- 开源社区可借鉴 olmOCR 的训练代码和基准方法论，开发多语言 OCR 定制模型，填补非英语文档（如中文古籍、阿拉伯语手稿）高精度识别的市场空白
risk_matrix:
  regulatory: 批量提取受版权保护的书籍、论文内容可能引发侵权争议；在 GDPR 或《生成式人工智能服务管理暂行办法》辖区处理含个人信息的文档需严格评估数据合规风险
  technological: OCR/VLM 赛道迭代极快，Infinity-Parser 和 Chandra OCR 已在同基准上超越 olmOCR 得分，存在被快速赶超或替代的风险；7B
    模型需 12GB+ 显存限制了轻量级和端侧部署场景
  competitive: 开源 OCR 工具赛道竞争白热化，Mistral、DeepSeek、PaddleOCR、Marker、MinerU 等已有方案各具优势，olmOCR
    在综合得分上并非绝对领先且缺乏显著的差异化定位
  ethical: 该工具可被用于无差别批量提取个人证件、通信记录等敏感文档内容，存在数据隐私滥用的潜在伦理风险
  additional: []
confidence:
  impact: high
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: allenai/olmocr
  canonical_name: allenai/olmocr
  url: https://github.com/allenai/olmocr
  positioning: Allen AI 开源的基于 7B 参数 VLM 的 PDF 与图像文档转 Markdown 工具包，支持公式、表格、手写体和多栏布局，每百万页转换成本低于
    200 美元。
  technical_signal: 基于 7B 参数视觉语言模型实现 PDF/PNG/JPEG 文档到干净 Markdown 的转换，支持公式、表格、手写体和多栏布局自然阅读顺序输出，并通过合成数据和强化学习训练持续优化模型性能。
  adoption_signal: 截至 2025 年 10 月已迭代至 v0.4.0 版本，配套 olmOCR-Bench 基准测试套件覆盖 7000 多个测试用例和
    1400 份文档，支持本地 GPU、远程推理服务器、Docker 和 Beaker 集群等多种部署方式。
  ecosystem_relevance: 在大模型训练对高质量文本数据需求激增的背景下，olmocr 为学术论文、技术文档等 PDF 资源的规模化清洗与结构化转化提供了低成本、可部署的关键基础设施。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Allen AI 依托机构科研实力持续迭代 olmocr，每百万页低于 200 美元的成本在文档数字化领域具有颠覆性潜力；配套 olmOCR-Bench
    基准测试巩固了生态影响力，值得跟踪其在企业文档处理和 LLM 数据预处理场景中的落地进展。
  risk_notes:
  - olmOCR v0.4.0 在自研基准测试总评分 82.4，略低于 Chandra OCR 0.1.0 的 83.1，尚未实现全面领先。
  - 项目依赖 7B 参数 VLM 和 GPU 推理，在边缘设备和低算力场景下部署受限，轻量级方案可能形成替代威胁。
  - 目前仍处于 v0.4.0 早期迭代阶段，API 与模型稳定性需更广泛社区验证，长期维护路线图尚不明朗。
  score: 8.0
  article_ids:
  - ae05babd8ff3098f
  evidence_snippets:
  - Allen AI 开源的 olmocr 工具包，基于 7B 参数视觉语言模型将 PDF、PNG、JPEG 文档转换为干净的 Markdown 格式。
  - 支持公式、表格、手写体和复杂排版，自动去除页眉页脚并保持多栏布局的自然阅读顺序。
  - 转换效率每百万页成本低于 200 美元，支持本地 GPU、远程推理服务器和 Docker 等多种部署方式。
---

A toolkit for converting PDFs and other image-based document formats into clean, readable, plain text format.

Try the online demo: https://olmocr.allenai.org/

Features:

- Convert PDF, PNG, and JPEG based documents into clean Markdown
- Support for equations, tables, handwriting, and complex formatting
- Automatically removes headers and footers
- Convert into text with a natural reading order, even in the presence of figures, multi-column layouts, and insets
- Efficient, less than $200 USD per million pages converted
- (Based on a 7B parameter VLM, so it requires a GPU)

- October 21, 2025 - v0.4.0 - New model release, boosts olmOCR-bench score by ~4 points using synthetic data and introduces RL training.
- August 13, 2025 - v0.3.0 - New model release, fixes auto-rotation detection, and hallucinations on blank documents.
- July 24, 2025 - v0.2.1 - New model release, scores 3 points higher on olmOCR-Bench, also runs significantly faster because it's default FP8, and needs much fewer retries per document.
- July 23, 2025 - v0.2.0 - New cleaned up trainer code, makes it much simpler to train olmOCR models yourself.
- June 17, 2025 - v0.1.75 - Switch from sglang to vllm based inference pipeline, updated docker image to CUDA 12.8.
- May 23, 2025 - v0.1.70 - Official docker support and images are now available! See Docker usage
- May 19, 2025 - v0.1.68 - olmOCR-Bench launch, scoring 77.4. Launch includes 2 point performance boost in olmOCR pipeline due to bug fixes with prompts.
- Mar 17, 2025 - v0.1.60 - Performance improvements due to better temperature selection in sampling.
- Feb 25, 2025 - v0.1.58 - Initial public launch and demo.

**olmOCR-Bench**:
We also ship a comprehensive benchmark suite covering over 7,000 test cases across 1,400 documents to help measure performance of OCR systems.

| ArXiv | Old scans math |
Tables | Old scans |
Headers & footers |
Multi column |
Long tiny text |
Base | Overall | |
|---|---|---|---|---|---|---|---|---|---|
| Mistral OCR API | 77.2 | 67.5 | 60.6 | 29.3 | 93.6 | 71.3 | 77.1 | 99.4 | 72.0±1.1 |
| Marker 1.10.1 | 83.8 | 66.8 | 72.9 | 33.5 | 86.6 | 80.0 | 85.7 | 99.3 | 76.1±1.1 |
| MinerU 2.5.4* | 76.6 | 54.6 | 84.9 | 33.7 | 96.6 | 78.2 | 83.5 | 93.7 | 75.2±1.1 |
| DeepSeek-OCR | 77.2 | 73.6 | 80.2 | 33.3 | 96.1 | 66.4 | 79.4 | 99.8 | 75.7±1.0 |
| Nanonets-OCR2-3B | 75.4 | 46.1 | 86.8 | 40.9 | 32.1 | 81.9 | 93.0 | 99.6 | 69.5±1.1 |
| PaddleOCR-VL* | 85.7 | 71.0 | 84.1 | 37.8 | 97.0 | 79.9 | 85.7 | 98.5 | 80.0±1.0 |
| Infinity-Parser 7B* | 84.4 | 83.8 | 85.0 | 47.9 | 88.7 | 84.2 | 86.4 | 99.8 | 82.5±? |
| Chandra OCR 0.1.0* | 82.2 | 80.3 | 88.0 | 50.4 | 90.8 | 81.2 | 92.3 | 99.9 | 83.1±0.9 |
olmOCR v0.4.0 |
83.0 | 82.3 | 84.9 | 47.7 | 96.1 | 83.7 | 81.9 | 99.7 | 82.4±1.1 |

You will need to install poppler-utils and additional fonts for rendering PDF images.

Install dependencies (Ubuntu/Debian):

```
sudo apt-get update
sudo apt-get install poppler-utils ttf-mscorefonts-installer msttcorefonts fonts-crosextra-caladea fonts-crosextra-carlito gsfonts lcdf-typetools
```

Set up a conda environment and install olmocr. The requirements for running olmOCR are difficult to install in an existing python environment, so please do make a clean python environment to install into.

```
conda create -n olmocr python=3.11
conda activate olmocr
```

Choose the installation option that matches your use case:

**Option 1: Remote Inference (Lightweight)**

If you plan to use a remote vLLM server with the `--server`

flag, install the base package:

`pip install olmocr`

This avoids installing heavy GPU dependencies like PyTorch (~2GB+).

**Option 2: Local GPU Inference**

Requirements:

- Recent NVIDIA GPU (tested on RTX 4090, L40S, A100, H100) with at least 12 GB of GPU RAM
- 30GB of free disk space

For running inference with your own GPU:

```
pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128
# Recommended: Install flash infer for faster inference on GPU
pip install https://download.pytorch.org/whl/cu128/flashinfer/flashinfer_python-0.2.5%2Bcu128torch2.7-cp38-abi3-linux_x86_64.whl
```

**Option 3: Beaker Cluster Execution**

For submitting jobs to Beaker clusters with the `--beaker`

flag:

`pip install olmocr[beaker]`

**Option 4: Benchmark Suite**

For running the olmOCR benchmark suite:

`pip install olmocr[bench]`

**Combined Installation**

You can combine multiple options:

```
# GPU + Beaker support
pip install olmocr[gpu,beaker] --extra-index-url https://download.pytorch.org/whl/cu128
# GPU + Benchmark support
pip install olmocr[gpu,bench] --extra-index-url https://download.pytorch.org/whl/cu128
```

**Troubleshooting**

If you run into errors about `too many open files`

, update your ulimit:

`ulimit -n 65536`

For quick testing, try the web demo.

**Convert a Single PDF (Local GPU):**

```
# Download a sample PDF
curl -o olmocr-sample.pdf https://olmocr.allenai.org/papers/olmocr_3pg_sample.pdf
# Convert it to markdown
olmocr ./localworkspace --markdown --pdfs olmocr-sample.pdf
```

**Convert an Image file:**

`olmocr ./localworkspace --markdown --pdfs random_page.png`

**Convert Multiple PDFs:**

`olmocr ./localworkspace --markdown --pdfs tests/gnarly_pdfs/*.pdf`

**Use Remote Inference Server:**

`olmocr ./localworkspace --server http://remote-server:8000/v1 --model allenai/olmOCR-2-7B-1025-FP8 --markdown --pdfs *.pdf`

With the `--markdown`

flag, results will be stored as markdown files inside of `./localworkspace/markdown/`

.


Note:You can also use`python -m olmocr.pipeline`

instead of`olmocr`

if you prefer.

The `./localworkspace/`

workspace folder will then have both Dolma and markdown files (if using `--markdown`

).

`cat localworkspace/markdown/olmocr-sample.md `

```
olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models
...
```


If you have a vLLM server already running elsewhere (or any inference platform implementing the OpenAI API), you can point olmOCR to use it instead of spawning a local instance.

**Installation for Remote Inference:**

```
# Lightweight installation - no GPU dependencies needed
pip install olmocr
```

**Using an External Server:**

```
# Use external vLLM server instead of local one
olmocr ./localworkspace --server http://remote-server:8000/v1 --model allenai/olmOCR-2-7B-1025-FP8 --markdown --pdfs tests/gnarly_pdfs/*.pdf
```

The served model name in vLLM needs to match the value provided in `--model`

.

**Example vLLM Server Launch:**

`vllm serve allenai/olmOCR-2-7B-1025-FP8 --max-model-len 16384`

We have tested `olmOCR-2-7B-1025-FP8`

on these external model providers and confirmed that they work

| $/1M Input tokens | $/1M Output tokens | Example Command | |
|---|---|---|---|
| Cirrascale | $0.07 | $0.15 | `olmocr ./workspace --server https://ai2endpoints.cirrascale.ai/api --api_key sk-XXXXXXX --workers 1 --max_concurrent_requests 20 --model olmOCR-2-7B-1025 --pdfs tests/gnarly_pdfs/*.pdf` |
| DeepInfra | $0.09 | $0.19 | `olmocr ./workspace --server https://api.deepinfra.com/v1/openai --api_key DfXXXXXXX --workers 1 --max_concurrent_requests 20 --model allenai/olmOCR-2-7B-1025 --pdfs tests/gnarly_pdfs/*.pdf` |
| Parasail | $0.10 | $0.20 | `olmocr ./workspace --server https://api.parasail.io/v1 --api_key psk-XXXXX --workers 1 --max_concurrent_requests 20 --model allenai/olmOCR-2-7B-1025 --pdfs tests/gnarly_pdfs/*.pdf` |

Notes on arguments

`--server`

: Defines the OpenAI-compatible endpoint: ex`https://api.deepinfra.com/v1/openai`

`--api_key`

: Your API key, bassed in via Authorization Bearer HTTP header`--max_concurrent_requests`

: Max concurrent requests that will be in-flight to the inference provider at one time`--workers`

: Max number of page groups that will be processed at once. You may want to set this to`1`

so that you finish one group of stuff before moving on.`--pages_per_group`

: You may want a smaller number of pages per group as many external provides have lower concurrent request limits`--model`

: The model identifier, ex.`allenai/olmOCR-2-7B-1025`

, different providers have different names, and if you run locally, you can use`olmocr`

- Other arguments work the same as with local inference

If you want to convert millions of PDFs using multiple nodes running in parallel, olmOCR supports reading PDFs from AWS S3 and coordinating work using an AWS S3 output bucket.

**Start the first worker node:**

`olmocr s3://my_s3_bucket/pdfworkspaces/exampleworkspace --pdfs s3://my_s3_bucket/jakep/gnarly_pdfs/*.pdf`

This sets up a simple work queue in your AWS bucket and starts converting PDFs.

**On subsequent worker nodes:**

`olmocr s3://my_s3_bucket/pdfworkspaces/exampleworkspace`

They will automatically start grabbing items from the same workspace queue.

If you are at Ai2 and want to linearize millions of PDFs efficiently using beaker, install with Beaker support:

`pip install olmocr[gpu,beaker] --extra-index-url https://download.pytorch.org/whl/cu128`

Then use the `--beaker`

flag to prepare the workspace locally and launch N GPU workers in the cluster:

`olmocr s3://my_s3_bucket/pdfworkspaces/exampleworkspace --pdfs s3://my_s3_bucket/jakep/gnarly_pdfs/*.pdf --beaker --beaker_gpus 4`

Pull the Docker image (large, includes the model, ~30GB):

`docker pull alleninstituteforai/olmocr:latest-with-model`

For advanced users who want to manage their own model downloads, we also provide a base image without the model:

`docker pull alleninstituteforai/olmocr:latest`

Process a single PDF in your current directory:

```
docker run --gpus all \
-v $(pwd):/workspace \
alleninstituteforai/olmocr:latest-with-model \
-c "olmocr /workspace/output --markdown --pdfs /workspace/sample.pdf"
```

Process multiple PDFs:

```
docker run --gpus all \
-v /path/to/pdfs:/input \
-v /path/to/output:/output \
alleninstituteforai/olmocr:latest-with-model \
-c "olmocr /output --markdown --pdfs /input/*.pdf"
```

Run the container interactively for exploration and debugging:

`docker run -it --gpus all alleninstituteforai/olmocr:latest-with-model`

Visit our Docker repository on Docker Hub for more information.


To see all available options:

```
olmocr --help
usage: pipeline.py [-h] [--pdfs [PDFS ...]] [--model MODEL] [--workspace_profile WORKSPACE_PROFILE] [--pdf_profile PDF_PROFILE] [--pages_per_group PAGES_PER_GROUP] [--max_page_retries MAX_PAGE_RETRIES] [--max_page_error_rate MAX_PAGE_ERROR_RATE] [--workers WORKERS]
[--apply_filter] [--stats] [--markdown] [--target_longest_image_dim TARGET_LONGEST_IMAGE_DIM] [--target_anchor_text_len TARGET_ANCHOR_TEXT_LEN] [--guided_decoding] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--max_model_len MAX_MODEL_LEN]
[--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--data-parallel-size DATA_PARALLEL_SIZE] [--port PORT] [--server SERVER] [--beaker] [--beaker_workspace BEAKER_WORKSPACE] [--beaker_cluster BEAKER_CLUSTER] [--beaker_gpus BEAKER_GPUS] [--beaker_priority BEAKER_PRIORITY]
workspace
Manager for running millions of PDFs through a batch inference pipeline
positional arguments:
workspace The filesystem path where work will be stored, can be a local folder, or an s3 path if coordinating work with many workers, s3://bucket/prefix/
options:
-h, --help show this help message and exit
--pdfs [PDFS ...] Path to add pdfs stored in s3 to the workspace, can be a glob path s3://bucket/prefix/*.pdf or path to file containing list of pdf paths
--model MODEL Path where the model is located, allenai/olmOCR-7B-0725-FP8 is the default, can be local, s3, or hugging face.
--workspace_profile WORKSPACE_PROFILE
S3 configuration profile for accessing the workspace
--pdf_profile PDF_PROFILE
S3 configuration profile for accessing the raw pdf documents
--pages_per_group PAGES_PER_GROUP
Aiming for this many pdf pages per work item group
--max_page_retries MAX_PAGE_RETRIES
Max number of times we will retry rendering a page
--max_page_error_rate MAX_PAGE_ERROR_RATE
Rate of allowable failed pages in a document, 1/250 by default
--workers WORKERS Number of workers to run at a time
--apply_filter Apply basic filtering to English pdfs which are not forms, and not likely seo spam
--stats Instead of running any job, reports some statistics about the current workspace
--markdown Also write natural text to markdown files preserving the folder structure of the input pdfs
--target_longest_image_dim TARGET_LONGEST_IMAGE_DIM
Dimension on longest side to use for rendering the pdf pages
--target_anchor_text_len TARGET_ANCHOR_TEXT_LEN
Maximum amount of anchor text to use (characters), not used for new models
--guided_decoding Enable guided decoding for model YAML type outputs
VLLM arguments:
--gpu-memory-utilization GPU_MEMORY_UTILIZATION
Fraction of VRAM vLLM may pre-allocate for KV-cache (passed through to vllm serve).
--max_model_len MAX_MODEL_LEN
Upper bound (tokens) vLLM will allocate KV-cache for, lower if VLLM won't start
--tensor-parallel-size TENSOR_PARALLEL_SIZE, -tp TENSOR_PARALLEL_SIZE
Tensor parallel size for vLLM
--data-parallel-size DATA_PARALLEL_SIZE, -dp DATA_PARALLEL_SIZE
Data parallel size for vLLM
--port PORT Port to use for the VLLM server
--server SERVER URL of external vLLM (or other compatible provider)
server (e.g., http://hostname:port). If provided,
skips spawning local vLLM instance
beaker/cluster execution:
--beaker Submit this job to beaker instead of running locally
--beaker_workspace BEAKER_WORKSPACE
Beaker workspace to submit to
--beaker_cluster BEAKER_CLUSTER
Beaker clusters you want to run on
--beaker_gpus BEAKER_GPUS
Number of gpu replicas to run
--beaker_priority BEAKER_PRIORITY
Beaker priority level for the job
```

There are some nice reusable pieces of the code that may be useful for your own projects:

- A prompting strategy to get really good natural text parsing using ChatGPT 4o - buildsilver.py
- Basic filtering by language and SEO spam removal - filter.py
- SFT Finetuning code for Qwen2.5-VL - train.py
- GRPO RL Trainer - grpo_train.py
- Synthetic data generation - mine_html_templates.py
- Processing millions of PDFs through a finetuned model using VLLM - pipeline.py
- Viewing Dolma docs created from PDFs - dolmaviewer.py

**olmOCR** is developed and maintained by the AllenNLP team, backed by the Allen Institute for Artificial Intelligence (AI2).
AI2 is a non-profit institute with the mission to contribute to humanity through high-impact AI research and engineering.
To learn more about who specifically contributed to this codebase, see our contributors page.

**olmOCR** is licensed under Apache 2.0.
A full copy of the license can be found on GitHub.

For olmOCR v1 and OlmOCR-bench:

```
@misc{olmocrbench,
title={{olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models}},
author={Jake Poznanski and Jon Borchardt and Jason Dunkelberger and Regan Huff and Daniel Lin and Aman Rangapur and Christopher Wilhelm and Kyle Lo and Luca Soldaini},
year={2025},
eprint={2502.18443},
archivePrefix={arXiv},
primaryClass={cs.CL},
url={https://arxiv.org/abs/2502.18443},
}
```

For olmOCR v2 Unit Testing Rewards with RL:

```
@misc{olmocr2,
title={olmOCR 2: Unit Test Rewards for Document OCR},
author={Jake Poznanski and Luca Soldaini and Kyle Lo},
year={2025},
eprint={2510.19817},
archivePrefix={arXiv},
primaryClass={cs.CV},
url={https://arxiv.org/abs/2510.19817},
}
```