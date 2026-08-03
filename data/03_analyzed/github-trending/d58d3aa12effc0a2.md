---
title: HKUDS/ViMax
source: https://github.com/HKUDS/ViMax
author: []
published: ''
created: '2026-05-21'
description: '"ViMax: Agentic Video Generation (Director, Screenwriter, Producer,
  and Video Generator All-in-One)" ViMax: Agentic Video Generation 🚨 Current Video
  Generation Limitations: ❌ Limited to Short Clips - Most AI tools generate only seconds
  of footage. ❌ Consistency Chaos - Characters and scenes change unpredictably across
  frames. ❌ Visual-Only Focus - Missing scripts, audio, narrative structure, and storytelling
  depth. 💡 ViMax Solution: 🎬 Director, Screenwriter, Producer, and Video Generator
  All-in-One! We''re exploring a future where AI becomes a complete creative powerhouse.
  💡 Simply input your concept. ViMax autonomously handles the rest. It orchestrates
  scriptwriting, storyboarding, character creation, and final video generation—all
  end-to-end. 🚀 https://github.com/user-attachments/assets/5bad46b2-8276-4e1d-9480-3522640744b2
  📑 Table of Contents 💡 Key Features 🔮 Demos 🏗️ Architecture 🚀 Quick Start 💡Key Features
  🌟 Idea2Video From Spark to Screen Transform raw ideas into complete video stories
  through intelligent multi-agent workflows automating storytelling, character design,
  and production . 🎨 Novel2Video Smart Literary Adaptation Engine Transform complete
  novels into episodic video content with intelligent narrative compression, character
  tracking, and scene-by-scene visual adaptation ⚙️ Script2Video Unlimited Screenplay
  Video Creation Unleash your creativity by writing any screenplay from personal stories
  to epic adventures, giving you complete control over every aspect of your visual
  storytelling. 🤳 AutoCameo Generate Video from Your Photo Create your own cameo video,
  transforming yourself/pet into a guest star who appears across limitless creative
  scripts, cinematic sequences, and interactive storylines. 🔮Video Demos Generated
  from Scratch 🎯 End-to-End Video Creation Engine The Challenges: 🌅 Reference Images:
  Time-consuming acquisition, organization, and alignment of reference frames that
  accurately capture characters, objects, positions, and environments. 🫠 Consistency
  Check: Sometimes, the image generator may generate unusable images even if it is
  given the correct characters, position, environment reference image and prompts.
  📄 Scripts Generation: Professional and high-quality videos need to have rich information
  density and structured design. 📝 Storyboard Design: Converting stories into visual
  narratives requires expertise in cinematography, scene composition, and visual storytelling
  that most creators lack. 🎬 Shot Design: Creating coherent camera sequences with
  proper angles, transitions, and pacing while maintaining narrative flow across complex
  scenes. 🎨 Development Delays: Ensuring character appearances, environments, and
  artistic style remain consistent across hundreds of shots in long-form content.
  ⏱️ Production Efficiency: Traditional video creation involves multiple specialists
  and lengthy workflows, creating barriers for independent creators and rapid prototyping.
  🎥 Scaling AI Generated Video: AI-generated videos are usually only a few seconds
  long, high-quality long videos at the minute or even hour level require complex
  cross-scene continuity and multi-storyboards design and processing capabilities.
  ViMAX: eliminates these production bottlenecks by automating the entire video creation
  pipeline from narrative input to final video output. 🔥 Why ViMax? 🧠 Effortless Production
  🚀 Complete Creative Freedom 🔊 Audio and Video Binding 🎨 Professional Quality 🤩 Interactive
  Video One-Prompt to Finished Video From Any Narrative to Reality Synchronized Storytelling
  Movie-Grade Output Make Your Own Cameo Video Skip the technical complexity—just
  describe your vision and let ViMax handle script generation, storyboarding, shot
  design, reference management, and consistency validation No creative limits—whether
  it''s a trailer, short story, novel chapter, or original concept, ViMax intelligently
  structures narratives and designs cinematography to bring any idea to life Seamlessly
  integrate character voice, and sound effects with visual content to create immersive
  experiences where audio and video work in perfect harmony Automated quality control
  ensures character consistency, proper scene composition, and professional visual
  standards across every frame of your video Interact in your own short stories by
  uploading your photo—ViMax intelligently integrates you as a character with consistent
  appearance and natural interactions throughout the entire video ☄️ Coming Soon 👨‍💻
  Google AI Studio API config✅ 📹 Dev mode branch 🤳 AutoCameo integrate 📺 More demos
  🎞️ Shot planning 🤖 New features 🏗️ Architecture 📊 System Overview ViMax is a multi-agent
  video framework that enables automated multi-shot video generation while ensuring
  character and scene consistency. Our system seamlessly translates your ideas into
  corresponding videos, allowing you to focus on storytelling rather than technical
  implementation. 🎯 Technical Capabilities: 🧬 Intelligent Long Script Generation RAG-based
  long script design engine that intelligently analyzes lengthy, novel-like stories
  and automatically segments them into a multi-scene script format. The process meticulously
  ensures that all key plot developments and character dialogues are accurately retained
  within the new structure. 🪄 Expressive Storyboard Design Shot-level storyboard design
  system that create expressive storyboards through cinematography language based
  on user requirements and target audiences, which establishs the narrative rhythm
  for subsequent video generation. 🔮 Multi-camera Filming Simulation Simulates multi-camera
  filming to deliver an immersive viewing experience while maintaining consistent
  character positioning and backgrounds within the same scene. 🧸 Intelligent Reference
  Images Selection Intelligently select the reference image required for the first
  frame of the current video, including the storyboards that occurred in the previous
  timeline, to ensure the accuracy of multiple characters and environmental elements
  as the video becomes longer. ⚙️ Automated Images Generation Based on the selected
  reference image and the visual logical order on the previous timeline, the prompt
  of the image generator is automatically generated to reasonably arrange the spatial
  interaction position between the character and the environment. ✅ Automated Image
  Generation Consistency Check Generate multiple images in parallel and select the
  best consistent image as the first frame through MLLM/VLM to imitate the workflow
  of human creators. ⚡ High-efficiency Parallel Shot Generation Parallel processing
  for sequential shots captured from the same camera enables highly efficient video
  production. 🤖 Multi-Agent Video Generation Pipeline 🧠 INPUT LAYER 📝 Idea & Scripts
  & Novels • 💭 Natural Language Prompts • 🖼️ Reference Images • 🎨 Style Directives
  • 🧩 Configs 🧭 CENTRAL ORCHESTRATION Agent Scheduling • Stage Transitions • Resource
  Management • Retry/Fallback Logic 🧾 SCRIPT UNDERSTANDING Character/Environment Extraction
  • Scene Boundaries • Style Intent 🎥 SCENE & SHOT PLANNING Storyboard Steps • Shot
  List • Key Frames & Beats 🧪 VISUAL ASSET PLANNING Reference Image Selection • Look/Style
  Guidance • Prompt Conditioning 🗂️ ASSET INDEXING Frames/Refs Catalog • Embeddings
  • Retrieval for Reuse ♻️ CONSISTENCY & CONTINUITY Character/Environment Tracking
  • Ref Matching • Temporal Coherence ✂️ VISUAL SYNTHESIS & ASSEMBLY Image Generation
  • Best-Frame Selection • First/Last-Frame→Video • Cut & Timeline Assembly 🚀 OUTPUT
  LAYER 🖼️ Frames • 🎞️ Clips & Final Videos • 📜 Logs • 📦 Working Directory Artifacts
  🚀Quick Start 🖥️ Environment OS: Linux, Windows 📥 Clone and Install We use uv to
  manage the environment. For uv installation, please refer to the https://docs.astral.sh/uv/getting-started/installation/.
  git clone https://github.com/HKUDS/ViMax.git cd ViMax uv sync 🎯 Usage main_idea2video.py
  is used to convert your ideas into videos. You need to configure the model and API
  key information in the configs/idea2video.yaml file, including three parts—the chat
  model, the image generator, and the video generator, as shown below chat_model:
  init_args: model: google/gemini-2.5-flash-lite-preview-09-2025 model_provider: openai
  api_key: <YOUR_API_KEY> base_url: https://openrouter.ai/api/v1 image_generator:
  class_path: tools.ImageGeneratorNanobananaGoogleAPI init_args: api_key: <YOUR_API_KEY>
  video_generator: class_path: tools.VideoGeneratorVeoGoogleAPI init_args: api_key:
  <YOUR_API_KEY> working_dir: .working_dir/idea2video Then, provide a simple yet thoughtful
  idea and the corresponding creative requirements in main_idea2video.py. idea = \
  """ If a cat and a dog are best friends, what would happen when they meet a new
  cat? """ user_requirement = \ """ For children, do not exceed 3 scenes. """ style
  = "Cartoon" Using MiniMax as Chat Model Provider MiniMax models can be used as an
  alternative chat model provider. MiniMax offers OpenAI-compatible API access to
  models such as MiniMax-M2.7 (1M context window) and MiniMax-M2.5 (204K context).
  Simply set model_provider: minimax in your config — the base URL is resolved automatically:
  chat_model: init_args: model: MiniMax-M2.7 model_provider: minimax api_key: <YOUR_MINIMAX_API_KEY>
  Or export the API key as an environment variable and leave api_key empty: export
  MINIMAX_API_KEY=<YOUR_KEY> See configs/idea2video_minimax.yaml and configs/script2video_minimax.yaml
  for complete examples. Model Context Note MiniMax-M2.7 1M tokens Latest, recommended
  MiniMax-M2.7-highspeed 1M tokens Fast variant MiniMax-M2.5 204K tokens Stable MiniMax-M2.5-highspeed
  204K tokens Fast variant main_script2video.py generates a video based on a specific
  script. You similarly need to set up the API configuration in configs/script2video.yaml
  file. Then, provide a scene script and the corresponding creative requirements in
  main_script2video.py, as shown below. script = \ """ EXT. SCHOOL GYM - DAY A group
  of students are practicing basketball in the gym. The gym is large and open, with
  a basketball hoop at one end and a large crowd of spectators at the other end. John
  (18, male, tall, athletic) is the star player, and he is practicing his dribble
  and shot. Jane (17, female, short, athletic) is the assistant coach, and she is
  helping John with his practice. The other students are watching the practice and
  cheering for John. John: (dribbling the ball) I''m going to score a basket! Jane:
  (smiling) Good job, John! John: (shooting the ball) Yes! ... """ user_requirement
  = \ """ Fast-paced with no more than 20 shots. """ style = "Animate Style" 🌟 If
  this project helps you, please give us a Star! ❤️ Thanks for visiting ✨ ViMax!'
tags:
- clippings
extraction_status: success
id: d58d3aa12effc0a2
source_type: community_discussion
tldr: HKUDS 团队发布 ViMax v1.2.0，一个开源的智能体视频生成框架，将导演、编剧、制片人和视频生成器整合为一体化工作流。用户只需输入创意概念，ViMax
  即可自动完成脚本撰写、分镜设计、角色创建和最终视频生成，支持 Google AI Studio 和 MiniMax 等多种模型后端。
objective_summary: 香港大学数据科学实验室（HKUDS）于 2026 年 7 月 20 日发布 ViMax v1.2.0（Web Workspace），这是一个基于智能体的多镜头视频生成框架。ViMax
  采用多智能体编排架构，自动处理长脚本生成（基于 RAG 的场景分割）、表现性分镜设计、多机位拍摄模拟、参考图像智能选择、图像生成一致性检查以及高效并行镜头生成。该框架支持
  Idea2Video 和 Script2Video 两种工作流，并新增 Web UI 实现项目管理和代理对话。用户需自行配置聊天模型、图像生成器和视频生成器的
  API 密钥（支持 Google Gemini、MiniMax 等）。项目在 GitHub 获 11.2k Stars 和 1.7k Forks，采用 MIT
  许可证。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - HKUDS
  - Google
  - MiniMax
  - OpenRouter
  technologies:
  - RAG
  - MLLM
  - VLM
  - Gemini
  - Veo
  key_people: []
key_logic_flow:
- ViMax 是一个多智能体视频框架，将导演、编剧、制片人和视频生成器整合为一体化系统，用户只需输入概念即可全自动完成视频创作。
- 框架采用中央编排层调度多个智能体，涵盖脚本理解、场景与镜头规划、视觉资产规划、资产索引、一致性与连续性检查、视觉合成与组装等完整管线。
- ViMax 支持两种主要工作流：Idea2Video（从创意想法生成视频）和 Script2Video（基于剧本或分场脚本生成视频），以及新增的 Agent Loop
  + TUI 交互式工作流。
- 技术能力包括基于 RAG 的长脚本生成、通过镜头语言创建表现性分镜、多机位拍摄模拟、智能选择参考图像确保多角色和环境一致性，以及利用 MLLM/VLM 进行图像生成一致性校验。
- v1.2.0 版本新增 Web UI 界面，支持命名项目管理、代理对话、工件与分镜预览、渲染检查点、文件上传、提供商设置和暗色模式。
- 项目已发表 arXiv 论文（2606.07649），使用 uv 管理环境，配置支持 Google Gemini API、MiniMax 等模型后端。
pipeline_stage: fact_extracted
extract_result: success
object_mentions:
- object_type: project
  name: HKUDS/ViMax
  canonical_name: HKUDS/ViMax
  url: https://github.com/HKUDS/ViMax
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - ViMax 是一个多智能体视频框架，能够实现自动化多镜头视频生成，同时确保角色和场景的一致性。
  - ViMax 将导演、编剧、制片人和视频生成器整合为一体化系统，用户只需输入概念即可自动完成脚本撰写、分镜设计和最终视频生成。
  - 该项目在 GitHub 获 11.2k Stars 和 1.7k Forks，最新 v1.2.0 版本于 2026 年 7 月 20 日发布。
  article_id: d58d3aa12effc0a2
- object_type: paper
  name: ViMax arXiv Paper
  canonical_name: ViMax arXiv Paper
  url: https://arxiv.org/abs/2606.07649
  confidence: high
  article_role: mentioned_reference
  evidence_snippets:
  - 项目已发表 arXiv 论文，编号为 2606.07649，可作为学术引用参考。
  article_id: d58d3aa12effc0a2
- object_type: product
  name: Google AI Studio API
  canonical_name: Google AI Studio
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ViMax 支持通过 Google AI Studio API 配置聊天模型、图像生成器和视频生成器。
  - ViMax 的视频生成器工具支持 Google Veo API，图像生成器支持 Google 提供的 API。
  article_id: d58d3aa12effc0a2
- object_type: product
  name: MiniMax API
  canonical_name: MiniMax
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - ViMax 支持 MiniMax 作为备选聊天模型提供商，兼容 OpenAI 的 API 格式。
  - MiniMax-M2.7 提供 100 万 token 上下文窗口，是 ViMax 推荐使用的聊天模型。
  article_id: d58d3aa12effc0a2
impact_score:
  score: 5.5
  reason: ViMax是一个多智能体视频生成编排框架，核心价值在于将脚本生成、分镜设计、角色一致性校验、视频合成等环节通过中央编排调度串联成端到端流水线，而非底层生成模型的突破。该工作降低了AI视频创作的技术门槛，对独立创作者和快速原型场景有实际价值，但本质是对Gemini、MiniMax、Veo等现有模型的工程集成与工作流优化。考虑到视频生成领域正处于快速上升期且多智能体架构是当前热点，该框架具有中等偏上的短期冲击力——它不会改变行业范式，但为开源社区提供了一个可复用的视频制作管线参考实现，评分5.5分。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 多智能体编排架构的实际视频生成质量与角色/场景跨镜头一致性表现
hype_assessment:
  level: medium
  reason: README中使用了'Complete Creative Freedom'（完全创作自由）、'Movie-Grade Output'（电影级产出）、'Effortless
    Production'（毫不费力的制作）等营销话术，存在一定包装成分。项目虽提供了架构图和演示视频，但缺乏系统性的定量评估指标（如一致性分数、用户满意度对比、生成成功率等），也未与现有方案做横向消融实验。不过该项目确实提供了可运行的代码和多段demo视频，并非纯概念炒作，因此判定为中等水分。
information_entropy: medium
domain_disruption:
  technical_innovation: 核心技术创新在于将RAG引擎用于长文本脚本的自动分段与关键情节保留，以及通过MLLM/VLM对生成图像进行并行候选筛选和一致性校验——模拟人类创作者的筛选工作流。六大模块（脚本理解、场景镜头规划、视觉资产规划、资产索引、一致性校验、视觉合成组装）的中央编排调度设计是工程实现的本质突破，同一机位连续镜头的并行处理也提升了长视频制作效率。但底层生成能力仍依赖第三方模型API。
  business_model: 该框架以开源形式发布，短期商业影响主要体现在降低AI视频制作工具的开发门槛，可能催生一批基于ViMax架构的二次开发或SaaS化视频创作平台。长期看，此类多智能体编排框架可能推动视频制作从'人工精修'向'AI自动化流水线'转型，对短视频MCN、独立创作者经济、教育内容生产等领域有重塑潜力。但目前仍处于研究原型阶段，距离商业化产品尚有距离。
engineering_complexity: prototype
compound_value:
  score: 5.5
  reason: 多智能体视频生成框架代表了AI视频制作从单次推理到编排式工作流的范式演进，这一方向具有结构性的技术价值。但作为高校实验室开源项目，其长期复利效应受到三重约束：（1）商业化路径不明确——HKUDS是学术机构而非商业实体，缺乏go-to-market能力和持续运营团队，代码仓库可能面临维护断层；（2）价值捕获薄弱——框架位于编排层，对底层模型（Gemini、MiniMax）高度依赖，视频质量的提升受制于模型能力的线性进步而非框架本身的非线性改进；（3）赛道竞争激烈——Runway、Pika、Kling等商业产品正在快速内化类似的多镜头一致性能力，开源框架的先发优势窗口正在收窄。若该项目能孵化独立公司并建立开发者生态，score有上调至7-7.5的空间；若仅停留为学术Demo，3-5年后大概率被商业产品吸收或替代。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- Google
- MiniMax
- OpenRouter
- HKUDS
- 独立视频创作者与小型工作室
competitive_casualty:
- Runway
- Pika Labs
- 传统视频后期制作工具厂商
- 闭源AI视频SaaS平台
market_opportunities:
- 独立开发者和创业团队可基于ViMax开源框架封装SaaS产品，瞄准短剧出海、跨境电商广告视频、企业培训课件等垂直场景，提供低门槛的一键视频生成服务，差异化竞争点在于中文剧本理解与本土化叙事风格适配
- 视频制作工具厂商可在现有剪辑工具中集成「AI多智能体导演」模块，将ViMax的分镜设计+一致性校验能力嵌入专业工作流，定位为「AI副导演」辅助人类创作者而非完全替代，降低专业用户的使用心理门槛
- AI工程师和产品经理建议深入研究该框架的多智能体编排模式（中央调度→六大模块流水线），这一架构范式可迁移至AI音乐制作、AI游戏关卡设计、AI互动小说等需要跨模块协作的创意生成领域
risk_matrix:
  regulatory: AI生成视频面临日益收紧的监管环境：中国《生成式人工智能服务管理暂行办法》要求AI生成内容显著标识，欧盟AI Act将深度伪造列为高风险应用，美国多州推进AI生成内容水印立法。ViMax的Cameo换脸功能若商业化部署，可能触发肖像权侵权与深度伪造相关法规，需密切关注各国对AI视频生成工具的合规要求演变
  technological: 框架强依赖底层模型（Gemini-2.5-Flash-Lite、MiniMax-M2.7等）的API稳定性与定价策略，若Google或MiniMax调整API政策、提价或下线模型，框架核心能力将受重大冲击。当前AI视频生成仍以秒级短片为主，距离分钟级甚至小时级长视频的质量与一致性仍有显著技术鸿沟，论文级声明与工程实际效果之间可能存在落差。此外，开源仓库目前仅有README，实际代码尚未充分公开验证
  competitive: 赛道高度拥挤且巨头密集布局：OpenAI Sora已开放使用，Google Veo深度整合Vertex AI生态，快手可灵(Kling)在国内市场占据先发优势，Runway、Pika等创业公司持续迭代。ViMax作为高校开源项目，在工程化程度、模型自研能力、资金与算力资源上与上述玩家存在数量级差距，存在被巨头生态整合吸收或边缘化的风险
  ethical: ViMax的Cameo功能允许用户上传照片自动换脸为视频角色，极易被滥用生成虚假名人代言、政治误导视频或未经同意的色情内容。全自动化视频生成流水线大幅降低了深度伪造的技术门槛，可能加剧虚假信息传播、身份盗用和隐私侵犯。此外，从编剧、分镜师到后期制作的全链条自动化对影视行业从业者构成结构性就业冲击
  additional:
  - 开源治理风险：HKUDS实验室若后续缺乏持续维护资源，框架可能沦为 abandonware，依赖该框架的商业项目将面临技术债务
  - 地缘政治风险：框架同时支持Google(美国)和MiniMax(中国)模型，在中美AI技术脱钩背景下，跨国部署可能面临出口管制或数据跨境合规障碍
  - 质量声誉风险：若早期用户基于框架生成低质量视频并广泛传播，可能导致ViMax品牌与「粗糙AI视频」绑定，损害长期生态建设
confidence:
  impact: medium
  compound: medium
  hype: high
actionable_insight: strategic_invest
object_insights:
- object_type: project
  name: HKUDS/ViMax
  canonical_name: HKUDS/ViMax
  url: https://github.com/HKUDS/ViMax
  positioning: ViMax 是一个基于多智能体编排的开源视频生成框架，将导演、编剧、制片人和视频生成器整合为一体化系统，实现从创意概念到最终视频的全自动端到端生成。
  technical_signal: 采用多智能体中央编排架构，集成 RAG 长脚本生成、镜头语言分镜设计、多机位拍摄模拟、MLLM/VLM 图像一致性校验及高效并行镜头生成等模块化技术能力。
  adoption_signal: 在 GitHub 获 11.2k Stars 和 1.7k Forks，采用 MIT 许可证，v1.2.0 新增 Web UI
    工作空间，表明社区关注度和项目活跃度持续提升。
  ecosystem_relevance: 支持 Google Gemini API 和 MiniMax 等多种模型后端，与 AI 视频生成生态中的基础模型提供商形成互补关系，降低创作者使用门槛。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: ViMax 代表 AI 视频生成从单镜头片段向多镜头长视频叙事演进的重要方向，其多智能体编排和一致性保持技术具有显著创新性，开源模式有望加速视频创作民主化进程。
  risk_notes:
  - 当前 AI 视频生成质量仍受限于单镜头时长和一致性，长视频跨场景叙事面临技术挑战。
  - 高度依赖第三方模型 API（如 Google Gemini、MiniMax），存在供应链中断和服务可用性风险。
  - 用户需自行配置多个 API 密钥并管理提供商设置，较高的技术门槛可能限制非技术用户采用。
  score: 8.0
  article_ids:
  - d58d3aa12effc0a2
  evidence_snippets:
  - ViMax 是一个多智能体视频框架，能够实现自动化多镜头视频生成，同时确保角色和场景的一致性。
  - ViMax 将导演、编剧、制片人和视频生成器整合为一体化系统，用户只需输入概念即可自动完成脚本撰写、分镜设计和最终视频生成。
  - 该项目在 GitHub 获 11.2k Stars 和 1.7k Forks，最新 v1.2.0 版本于 2026 年 7 月 20 日发布。
---

- ❌
**Limited to Short Clips**- Most AI tools generate only seconds of footage. - ❌
**Consistency Chaos**- Characters and scenes change unpredictably across frames. - ❌
**Visual-Only Focus**- Missing scripts, audio, narrative structure, and storytelling depth.

🎬 **Director**, **Screenwriter**, **Producer**, and **Video Generator** **All-in-One**! We're exploring a future where AI becomes a complete creative powerhouse. 💡 Simply input your concept. ViMax autonomously handles the rest. It orchestrates scriptwriting, storyboarding, character creation, and final video generation—all end-to-end. 🚀

## vimax_demo.mp4

|
Transform |
Transform |
Unleash your creativity by writing |
|

## f1.mp4 |
## underwater.mp4 |
## otter.mp4 |
## carrier.mp4 |
## vampire.mp4 |
## skydiving.mp4 |
## tree.mp4 |
## cameo_skycastle.mp4 |
## cameo_cat.mp4 |

**The Challenges**:

-
🌅

**Reference Images**: Time-consuming acquisition, organization, and alignment of reference frames that accurately capture characters, objects, positions, and environments. -
🫠

**Consistency Check**: Sometimes, the image generator may generate unusable images even if it is given the correct characters, position, environment reference image and prompts. -
📄

**Scripts Generation**: Professional and high-quality videos need to have rich information density and structured design. -
📝

**Storyboard Design**: Converting stories into visual narratives requires expertise in cinematography, scene composition, and visual storytelling that most creators lack. -
🎬

**Shot Design**: Creating coherent camera sequences with proper angles, transitions, and pacing while maintaining narrative flow across complex scenes. -
🎨

**Development Delays**: Ensuring character appearances, environments, and artistic style remain consistent across hundreds of shots in long-form content. -
⏱️

**Production Efficiency**: Traditional video creation involves multiple specialists and lengthy workflows, creating barriers for independent creators and rapid prototyping. -
🎥

**Scaling AI Generated Video**: AI-generated videos are usually only a few seconds long, high-quality long videos at the minute or even hour level require complex cross-scene continuity and multi-storyboards design and processing capabilities.

**ViMAX**: eliminates these production bottlenecks by automating the entire video creation pipeline from narrative input to final video output.

🧠 Effortless Production |
🚀 Complete Creative Freedom |
🔊 Audio and Video Binding |
🎨 Professional Quality |
🤩 Interactive Video |
|---|---|---|---|---|
| One-Prompt to Finished Video | From Any Narrative to Reality | Synchronized Storytelling | Movie-Grade Output | Make Your Own Cameo Video |
| Skip the technical complexity—just describe your vision and let ViMax handle script generation, storyboarding, shot design, reference management, and consistency validation | No creative limits—whether it's a trailer, short story, novel chapter, or original concept, ViMax intelligently structures narratives and designs cinematography to bring any idea to life | Seamlessly integrate character voice, and sound effects with visual content to create immersive experiences where audio and video work in perfect harmony | Automated quality control ensures character consistency, proper scene composition, and professional visual standards across every frame of your video | Interact in your own short stories by uploading your photo—ViMax intelligently integrates you as a character with consistent appearance and natural interactions throughout the entire video |

- 👨💻
**Google AI Studio API config✅** - 📹
**Dev mode branch** - 🤳
**AutoCameo integrate** - 📺
**More demos** - 🎞️
**Shot planning** - 🤖
**New features**

**ViMax** is a multi-agent video framework that enables automated multi-shot video generation while ensuring character and scene consistency. Our system seamlessly translates your ideas into corresponding videos, allowing you to focus on storytelling rather than technical implementation.

🎯 **Technical Capabilities**:

🧬 **Intelligent Long Script Generation**

RAG-based long script design engine that intelligently analyzes lengthy, novel-like stories and automatically segments them into a multi-scene script format. The process meticulously ensures that all key plot developments and character dialogues are accurately retained within the new structure.

🪄 **Expressive Storyboard Design**

Shot-level storyboard design system that create expressive storyboards through cinematography language based on user requirements and target audiences, which establishs the narrative rhythm for subsequent video generation.

🔮 **Multi-camera Filming Simulation**

Simulates multi-camera filming to deliver an immersive viewing experience while maintaining consistent character positioning and backgrounds within the same scene.

🧸 **Intelligent Reference Images Selection**

Intelligently select the reference image required for the first frame of the current video, including the storyboards that occurred in the previous timeline, to ensure the accuracy of multiple characters and environmental elements as the video becomes longer.

⚙️ **Automated Images Generation**

Based on the selected reference image and the visual logical order on the previous timeline, the prompt of the image generator is automatically generated to reasonably arrange the spatial interaction position between the character and the environment.

✅ **Automated Image Generation Consistency Check**

Generate multiple images in parallel and select the best consistent image as the first frame through MLLM/VLM to imitate the workflow of human creators.

⚡ **High-efficiency Parallel Shot Generation**

Parallel processing for sequential shots captured from the same camera enables highly efficient video production.

🧠 INPUT LAYER📝 Idea & Scripts & Novels • 💭 Natural Language Prompts • 🖼️ Reference Images • 🎨 Style Directives • 🧩 Configs |
||
🧭 CENTRAL ORCHESTRATIONAgent Scheduling • Stage Transitions • Resource Management • Retry/Fallback Logic |
||
🧾 SCRIPT UNDERSTANDINGCharacter/Environment Extraction • Scene Boundaries • Style Intent |
🎥 SCENE & SHOT PLANNINGStoryboard Steps • Shot List • Key Frames & Beats |
|
🧪 VISUAL ASSET PLANNINGReference Image Selection • Look/Style Guidance • Prompt Conditioning |
||
🗂️ ASSET INDEXINGFrames/Refs Catalog • Embeddings • Retrieval for Reuse |
♻️ CONSISTENCY & CONTINUITYCharacter/Environment Tracking • Ref Matching • Temporal Coherence |
|
✂️ VISUAL SYNTHESIS & ASSEMBLYImage Generation • Best-Frame Selection • First/Last-Frame→Video • Cut & Timeline Assembly |
||
🚀 OUTPUT LAYER🖼️ Frames • 🎞️ Clips & Final Videos • 📜 Logs • 📦 Working Directory Artifacts |

```
OS: Linux, Windows
```


We use uv to manage the environment. For uv installation, please refer to the https://docs.astral.sh/uv/getting-started/installation/.

```
git clone https://github.com/HKUDS/ViMax.git
cd ViMax
uv sync
```

main_idea2video.py is used to convert your ideas into videos. You need to configure the model and API key information in the configs/idea2video.yaml file, including three parts—the chat model, the image generator, and the video generator, as shown below

```
chat_model:
init_args:
model: google/gemini-2.5-flash-lite-preview-09-2025
model_provider: openai
api_key: <YOUR_API_KEY>
base_url: https://openrouter.ai/api/v1
image_generator:
class_path: tools.ImageGeneratorNanobananaGoogleAPI
init_args:
api_key: <YOUR_API_KEY>
video_generator:
class_path: tools.VideoGeneratorVeoGoogleAPI
init_args:
api_key: <YOUR_API_KEY>
working_dir: .working_dir/idea2video
```

Then, provide a simple yet thoughtful idea and the corresponding creative requirements in main_idea2video.py.

```
idea = \
"""
If a cat and a dog are best friends, what would happen when they meet a new cat?
"""
user_requirement = \
"""
For children, do not exceed 3 scenes.
"""
style = "Cartoon"
```

MiniMax models can be used as an alternative chat model provider. MiniMax offers OpenAI-compatible API access to models such as **MiniMax-M2.7** (1M context window) and **MiniMax-M2.5** (204K context).

Simply set `model_provider: minimax`

in your config — the base URL is resolved automatically:

```
chat_model:
init_args:
model: MiniMax-M2.7
model_provider: minimax
api_key: <YOUR_MINIMAX_API_KEY>
```

Or export the API key as an environment variable and leave `api_key`

empty:

`export MINIMAX_API_KEY=<YOUR_KEY>`

See `configs/idea2video_minimax.yaml`

and `configs/script2video_minimax.yaml`

for complete examples.

| Model | Context | Note |
|---|---|---|
| MiniMax-M2.7 | 1M tokens | Latest, recommended |
| MiniMax-M2.7-highspeed | 1M tokens | Fast variant |
| MiniMax-M2.5 | 204K tokens | Stable |
| MiniMax-M2.5-highspeed | 204K tokens | Fast variant |

main_script2video.py generates a video based on a specific script. You similarly need to set up the API configuration in configs/script2video.yaml file. Then, provide a scene script and the corresponding creative requirements in main_script2video.py, as shown below.

```
script = \
"""
EXT. SCHOOL GYM - DAY
A group of students are practicing basketball in the gym. The gym is large and open, with a basketball hoop at one end and a large crowd of spectators at the other end. John (18, male, tall, athletic) is the star player, and he is practicing his dribble and shot. Jane (17, female, short, athletic) is the assistant coach, and she is helping John with his practice. The other students are watching the practice and cheering for John.
John: (dribbling the ball) I'm going to score a basket!
Jane: (smiling) Good job, John!
John: (shooting the ball) Yes!
...
"""
user_requirement = \
"""
Fast-paced with no more than 20 shots.
"""
style = "Animate Style"
```

**🌟 If this project helps you, please give us a Star!**

* ❤️ Thanks for visiting ✨ ViMax!*