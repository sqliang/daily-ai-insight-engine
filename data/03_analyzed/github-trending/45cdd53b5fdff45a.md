---
title: AIEraDev/Clypra
source: https://github.com/AIEraDev/Clypra
author: []
published: ''
created: '2026-07-15'
manifest_dates:
- '2026-07-15'
description: 'A modern video editor built with Tauri, React, and TypeScript. Focus
  on building free capabilities of premium capcut functionalitiesClypra Professional
  video editing—free and open source forever. A modern video editor built on Tauri
  v2, React 19, and Rust. Hardware-accelerated processing, cross-platform (desktop
  + mobile), with optional AI-powered features. Features • Architecture • Installation
  • Development • Contributing • Open Core Overview Clypra is a free, open-source
  video editor (MIT License) with professional-grade features. The core editor, effects
  engine, and all UI components are free forever—no watermarks, no feature limits,
  no subscriptions required. Want AI superpowers? Optional Pro features add natural
  language editing, auto-captions, smart reframing, and more. Target Platforms Desktop:
  macOS (Apple Silicon & Intel), Windows, Linux Mobile: iOS (via Capacitor), Android
  (via Capacitor) Features Core Editing Multi-format media import: MP4, MOV, WebM,
  MKV, M4V, AVI (video); MP3, WAV, AAC (audio); JPG, PNG, WebP (image) Frame-accurate
  trimming: Precise timeline control with millisecond accuracy Multi-track timeline:
  Professional timeline interface with ruler and visual feedback Undo/redo system:
  100-level history stack with command pattern architecture Professional Audio High-fidelity
  waveforms: Peak + RMS visualization with mirrored display (technical details) Audio
  synchronization: Frame-accurate AV sync during playback and export Volume control:
  Per-clip volume adjustment with real-time preview Visual Features Filmstrip thumbnails:
  Hardware-accelerated thumbnail generation with adaptive density Text overlays: Custom
  fonts, styles, and animations for titles and captions Preview canvas: Real-time
  compositing with transform controls Performance Hardware acceleration: Native GPU
  decode via FFmpeg (VideoToolbox/D3D11VA/VAAPI) Decoder prewarming: Sub-10ms first-frame
  latency through predictive decoder initialization Parallel processing: Web worker
  pool for thumbnail generation (2-4× faster rendering) Efficient caching: LRU-based
  decoder pool with 20 concurrent decoders Real-time monitoring: 30+ performance metrics
  tracked across video pipeline Project Management Persistent projects: SQLite-backed
  project storage with auto-save Media library: Centralized asset management with
  metadata caching Export pipeline: FFmpeg-based export with codec selection (H.264,
  H.265, ProRes) Architecture Clypra is architected as a native desktop and mobile
  application with clear separation between frontend UI and backend processing. Technology
  Stack Frontend React 19 with TypeScript (strict mode) Zustand for state management
  (separated stores by domain) Vite for build tooling and hot module replacement Backend
  Rust with Tauri v2 for native platform integration FFmpeg (via ffmpeg-next) for
  video/audio processing Hardware acceleration: VideoToolbox (macOS), D3D11VA (Windows),
  VAAPI (Linux) DashMap for concurrent data structures Mobile Capacitor for iOS/Android
  deployment Native bridge for platform-specific features Design Principles Native
  Performance: Rust FFmpeg backend eliminates browser constraints Desktop-First Architecture:
  Optimized for desktop-class workflows, portable to mobile Hardware Acceleration:
  Direct GPU access through native FFmpeg hardware decoders Efficient IPC: Tauri commands
  optimized for minimal serialization overhead Zero Browser Dependencies: No WebCodecs,
  MSE, or web-specific APIs Video Pipeline Architecture ┌─────────────────────────────────────────────────────────────┐
  │ Frontend (React/TS) │ │ ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐
  │ │ │ Timeline UI │ │ Preview Canvas│ │ Filmstrip Cache │ │ │ └──────┬───────┘ └──────┬────────┘
  └────────┬────────┘ │ │ │ │ │ │ │ └─────────────────┴─────────────────────┘ │ │
  │ │ │ Tauri IPC Layer │ │ │ │ └───────────────────────────┼─────────────────────────────────┘
  │ ┌───────────────────────────┼─────────────────────────────────┐ │ Backend (Rust/FFmpeg)
  │ │ ┌─────────────────┴──────────────────┐ │ │ │ Decoder Pool (LRU, size=20) │ │
  │ │ ┌──────────────────────────────┐ │ │ │ │ │ Hardware Decoder Context │ │ │ │
  │ │ (VideoToolbox/D3D11/VAAPI) │ │ │ │ │ └──────────────────────────────┘ │ │ │
  └─────────────┬────────────────────┬─┘ │ │ │ │ │ │ ┌─────────────▼────────┐ ┌────────▼──────────┐
  │ │ │ Frame Decoder │ │ Export Pipeline │ │ │ │ (seek + decode) │ │ (encode + mux)
  │ │ │ └──────────────────────┘ └───────────────────┘ │ └─────────────────────────────────────────────────────────────┘
  Key Optimizations Decoder Prewarming Decoders initialized on project load (eliminates
  50-100ms cold start) Concurrent prewarming (4 decoders at a time) First-frame latency:
  5-10ms (vs 50-100ms without prewarming) Thumbnail Generation Web worker pool (CPU
  cores - 1, max 4) Zero-copy ImageBitmap transfer via Transferable 60% reduction
  in main thread CPU during scroll Batch Processing Atlas-based thumbnail storage
  (reduces IPC overhead by 90%) Streaming decode with channel-based delivery Concurrent
  frame decode (up to 20 videos simultaneously) Sequential Decode Optimization Smart
  seeking: forward decode within GOP boundaries (avoids redundant seeks) Sequential
  hit tracking: detects scrubbing patterns 70% reduction in seek operations during
  timeline navigation For detailed performance metrics and optimization roadmap, see
  PERFORMANCE-DESKTOP-ROADMAP.md. Installation Binary Releases Pre-built binaries
  are available for all supported platforms. Download from the latest release. macOS
  Recommended: Homebrew Installation brew install AIEraDev/tap/clypra This method
  automatically handles Gatekeeper authorization and updates. Alternative: Direct
  Download Download Clypra-universal.dmg from releases Open the DMG and drag Clypra
  to /Applications Right-click the app icon and select "Open" to authorize first launch
  Supported: macOS 11+ (Big Sur and later), both Apple Silicon and Intel Windows Download
  Clypra-x64.msi from releases Run the installer If Windows SmartScreen blocks execution,
  click "More Info" → "Run Anyway" Supported: Windows 10 (version 1809+) and Windows
  11 Linux Download Clypra-x86_64.AppImage from releases Make executable: chmod +x
  Clypra-x86_64.AppImage Run: ./Clypra-x86_64.AppImage Supported: Ubuntu 20.04+, Fedora
  35+, Debian 11+, and derivatives Development Prerequisites Required Node.js 18+
  with npm Rust 1.70+ (install via rustup) FFmpeg 6.0+ with development libraries
  Platform-Specific macOS: Xcode Command Line Tools (xcode-select --install) Windows:
  Visual Studio 2019+ with C++ desktop development tools Linux: Build essentials,
  webkit2gtk, libayatana-appindicator FFmpeg Installation macOS brew install ffmpeg
  Ubuntu/Debian sudo apt install ffmpeg libavcodec-dev libavformat-dev libavutil-dev
  libswscale-dev Windows (Chocolatey) choco install ffmpeg Windows (Manual) Download
  from ffmpeg.org/download.html Extract to C:\ffmpeg Add C:\ffmpeg\bin to system PATH
  Build from Source # Clone repository git clone https://github.com/AIEraDev/clypra.git
  cd clypra # Install dependencies npm install # Configure environment cp .env.example
  .env # Edit .env and add your Clypra API key (required for text effects) # Development
  mode with hot reload npm run tauri dev # Production build npm run build npm run
  tauri build Development Architecture The codebase is organized by domain with clear
  separation of concerns: src/ ├── components/ # React components │ ├── editor/ #
  Core editor UI (Timeline, Preview, Filmstrip) │ ├── screens/ # Full-screen views
  (Launch, Settings) │ └── ui/ # Reusable UI primitives (Modals, Icons, Buttons) ├──
  store/ # Zustand state stores (by domain) │ ├── timelineStore.ts # Timeline structure
  (tracks, clips, gaps) │ ├── playbackStore.ts # Playback state and AV sync │ ├──
  projectStore.ts # Project metadata and media assets │ └── ... # uiStore, settingsStore,
  historyStore ├── core/ # Core engine logic │ ├── runtime/ # ProjectSession and lifecycle
  management │ ├── scheduler/ # Frame scheduler for preview rendering │ ├── resources/
  # PreviewMediaPool (video/audio elements) │ ├── render/ # Canvas rasterization and
  compositing │ └── timeline/ # Timeline calculations and utilities ├── lib/ # Shared
  utilities │ ├── platform/ # Tauri IPC wrappers │ ├── monitoring/ # Performance monitoring
  │ ├── workers/ # Web worker pool │ └── ... # Audio, video, filmstrip utilities ├──
  hooks/ # Custom React hooks ├── types/ # TypeScript type definitions └── App.tsx
  # Application entry point src-tauri/ ├── src/ │ ├── commands/ # Tauri command handlers
  │ │ ├── thumbnail.rs # Video decode commands │ │ ├── export.rs # Export pipeline
  │ │ └── ... │ ├── thumbnail_engine/# FFmpeg decoder pool │ │ ├── decoder.rs # Hardware-accelerated
  decoder │ │ ├── cache.rs # LRU caching │ │ └── ... │ └── lib.rs # Tauri application
  setup └── Cargo.toml # Rust dependencies API Configuration Clypra uses the Clypra
  API for text effects and templates. To enable these features: Copy .env.example
  to .env: cp .env.example .env Add your API key to .env: VITE_CLYPRA_API_KEY=your_api_key_here
  Important: Never commit .env to version control (already in .gitignore) The API
  provides: Text effects library with customizable styles Canvas-based text templates
  with WebM video previews Google Fonts integration Testing # Run all tests npm test
  # Run Rust tests cd src-tauri && cargo test # Run specific test suite npm test --
  src/lib/__tests__/timelineUtils.test.ts # Run with coverage npm test -- --coverage
  Code Quality # TypeScript type checking npx tsc --noEmit # Rust linting cd src-tauri
  && cargo clippy -- -D warnings # Format code npm run format cd src-tauri && cargo
  fmt Project Structure State Management Architecture Clypra uses Zustand with domain-separated
  stores to maintain clear ownership boundaries: timelineStore: Timeline structure
  (tracks, clips, transitions, gaps) playbackStore: Playback state, playhead position,
  AV sync projectStore: Project metadata, media assets, persistence historyStore:
  Undo/redo command stack uiStore: UI state (modals, selections, drag state) settingsStore:
  User preferences and application settings Each store owns its domain and exposes
  actions. Cross-store communication happens through explicit calls, not shared mutable
  state. Video Processing Pipeline Import: FFmpeg probe extracts metadata (duration,
  dimensions, codec) Thumbnail: Rust decoder generates filmstrip tiles (L0-L3 density
  tiers) Preview: HTMLVideoElement (live playback) or Canvas (composited frames) Export:
  Frame scheduler → RGBA frames → FFmpeg encoder → MP4/MOV Performance Monitoring
  The application includes comprehensive performance monitoring: Decoder metrics:
  Cache hits, evictions, decode latency Export metrics: Frame write time, fps, total
  duration Render metrics: Layer rendering time, canvas pool efficiency Cache metrics:
  Filmstrip cache hit rate, memory usage Access metrics in development via window.__performanceMonitor.
  Contributing We welcome contributions! Please see CONTRIBUTING.md for guidelines.
  Development Workflow Fork the repository Create a feature branch (git checkout -b
  feature/amazing-feature) Make your changes with tests Ensure all tests pass (npm
  test && cd src-tauri && cargo test) Commit with conventional commits (feat:, fix:,
  docs:, etc.) Push to your fork and open a Pull Request Code Style TypeScript: Strict
  mode enabled, ESLint + Prettier Rust: cargo fmt + cargo clippy (no warnings) Commits:
  Conventional commits format Documentation: JSDoc for public APIs, inline comments
  for complex logic License This project is licensed under the MIT License - see the
  LICENSE file for details. FFmpeg Licensing Clypra uses FFmpeg for video processing.
  FFmpeg is licensed under: LGPL 2.1+ (default build) GPL 2+ (if built with GPL-only
  components) Binary releases include FFmpeg under LGPL. If you build with GPL components,
  ensure GPL compliance. Acknowledgments Tauri: Cross-platform native application
  framework FFmpeg: Video/audio processing engine React: UI framework shadcn/ui: Component
  library foundation Support Issues: GitHub Issues Discussions: GitHub Discussions
  Documentation: Project Wiki Open Core Model Clypra uses an Open Core business model:
  Free & Open Source (MIT License) ✅ Core Video Editor - Multi-track timeline, frame-accurate
  editing, hardware-accelerated processing ✅ Effects Engine - Professional video effects,
  transitions, filters (via @clypra-studio/engine) ✅ Audio Tools - Waveform visualization,
  volume control, AV sync ✅ Export Pipeline - H.264, H.265, ProRes export with FFmpeg
  ✅ Text Overlays - Custom fonts, styles, and animations ✅ All UI Components - Full
  source code, no proprietary dependencies No watermarks. No feature limits. No subscriptions.
  Forever. Pro Features (AI Layer) 🎯 Natural Language Editing - "Remove all pauses",
  "Add captions", "Make this shorter" 🎯 Auto-Captioning - Transcription with speaker
  detection and customizable styles 🎯 Smart Reframe - Auto-crop for Instagram Stories,
  TikTok, YouTube Shorts 🎯 Scene Detection - AI-powered scene splitting and B-roll
  suggestions 🎯 Audio Enhancement - Noise removal, EQ, compression 🎯 Voice Cloning
  - Match narrator voice across clips (coming soon) 🎯 Multi-language Dubbing - Translate
  and dub with lip sync (coming soon) Pricing: Free tier (100 AI calls/month) • Pro
  ($10/month, unlimited) • Enterprise (custom) Learn more about Pro features → Why
  Open Core? We believe professional video editing should be free and accessible to
  everyone. Open source ensures: Transparency - You can audit every line of code Ownership
  - Your edits, your data, your workflow Community - Contributions from creators worldwide
  Longevity - The editor can''t be shut down or paywalled The Pro AI features fund
  full-time development on the open source core. Everyone wins. Roadmap See PERFORMANCE-DESKTOP-ROADMAP.md
  for upcoming performance improvements. Planned features: Mobile app release (iOS/Android
  via Capacitor) Advanced color grading Multi-camera editing Plugin system for extensions
  GPU-accelerated effects rendering Pro Roadmap (AI features): Natural language commands
  (Q3 2026) Auto-captioning (Q3 2026) Smart reframe (Q4 2026) Voice cloning (Q1 2027)
  Multi-language dubbing (Q2 2027)'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 45cdd53b5fdff45a
source_type: community_discussion
tldr: Clypra 是一个基于 Tauri/React/Rust 的免费开源专业视频编辑器，采用 MIT 协议。
objective_summary: AIEraDev 团队发布了 Clypra，一个基于 Tauri v2、React 19 和 Rust 构建的免费开源视频编辑器。支持
  macOS、Windows、Linux 桌面端及 iOS、Android 移动端，核心功能永久免费，提供可选的 AI 增强 Pro 功能。
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies:
  - AIEraDev
  technologies:
  - Tauri v2
  - React 19
  - Rust
  - FFmpeg
  - Capacitor
  - Zustand
  - VideoToolbox
  - D3D11VA
  - VAAPI
  key_people: []
key_logic_flow:
- Clypra 是一个基于 Tauri v2、React 19 和 Rust 构建的免费开源专业视频编辑器，采用 MIT 协议授权。
- 核心编辑器、特效引擎和所有 UI 组件永久免费，无水印、无功能限制、无订阅要求。
- 可选 Pro 功能提供自然语言编辑、自动字幕、智能重构图等 AI 增强特性。
- 支持桌面端（macOS Apple Silicon 和 Intel、Windows、Linux）和移动端（iOS 和 Android）。
- 硬件加速通过 FFmpeg 原生 GPU 解码器实现，支持 VideoToolbox、D3D11VA 和 VAAPI，可实现亚 10 毫秒首帧延迟。
- 采用 Open Core 商业模式，免费开源核心引擎配合付费高级功能。
specialized_tags:
  github:
    projectName: AIEraDev/Clypra
    projectUrl: https://github.com/AIEraDev/Clypra
    primaryLanguage: Rust
    licenseType: MIT
    domain: other
    crossTags:
    - open-source
    - cross-platform
    - video-editor
    aiDetail: null
extract_result: success
impact_score:
  score: 5.0
  reason: Clypra 是一款架构现代化的开源视频编辑器，采用 Tauri v2 + React 19 + Rust 技术栈并支持跨桌面和移动平台，在开源视频编辑领域具有技术示范意义。MIT
    协议的采用比 GPL 更宽松，可能吸引更多开发者贡献。但视频编辑赛道已有 CapCut、DaVinci Resolve、Shotcut 等成熟竞品，项目刚发布尚未验证用户采纳和生态发展，且可选
    AI Pro 功能并非核心竞争力，短期内对行业竞争格局的冲击有限。评分 5.0——属于重要的产品发布，一定程度改变局部竞争格局。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Rust + Tauri 实现硬件加速视频编辑器的工程可行性及性能优化细节
hype_assessment:
  level: low
  reason: 文章提供了完整的架构图、具体性能指标（亚10ms首帧延迟、70%寻道优化、60%主线程CPU减少）和工程实现细节，技术内容扎实有据。没有使用'颠覆''革命性'等
    PR 话术，整体风格偏向技术文档而非营销宣传，信息可信度较高。
information_entropy: high
domain_disruption:
  technical_innovation: 采用 Tauri v2 + Rust 后端 + React 前端的异构架构实现专业视频编辑器，核心创新包括：基于 FFmpeg
    原生 GPU 解码器（VideoToolbox/D3D11VA/VAAPI）的硬件加速管线、LRU 解码器池（20路并发）、解码器预热（首帧延迟从50-100ms降至5-10ms）、基于
    Web Worker 的缩略图并行生成（2-4倍加速）、以及 Atlas 批处理存储减少90% IPC 开销。整套架构在开源视频编辑器中具有明显技术领先性。
  business_model: Open Core 模式：MIT 协议永久免费开源核心编辑器、特效引擎和 UI 组件（无水印、无功能限制、无订阅），通过可选 AI
    增强 Pro 功能（自然语言编辑、自动字幕、智能重构图）实现商业化。这种模式在视频编辑领域较为罕见，可能推动更多视频工具采用开源核心 + AI 增值的商业路径。
engineering_complexity: production_ready
compound_value:
  score: 4.5
  reason: Clypra 的技术选型（Tauri v2 + Rust + FFmpeg）在性能和跨平台覆盖上是扎实的，支持桌面+移动端且采用 MIT 协议，能有效推动开发者社区采用。但作为视频编辑器赛道的新入场者，其面临的竞争壁垒极高——Adobe
    Premiere Pro、DaVinci Resolve、Final Cut Pro 和 CapCut 均已形成强大的生态锁定（插件体系、用户习惯、云端协作）。MIT
    授权虽然有利于快速扩散，但也意味着核心代码无任何防御性——竞品可以直接 fork 或集成相同能力，导致价值无法有效截留。Open Core 商业模式的核心变现依赖
    AI Pro 功能（自然语言编辑、自动字幕等），但这些功能正在全行业快速商品化（Adobe Firefly、DaVinci Resolve AI、CapCut
    均已布局），差异化的窗口期有限。视频编辑存在典型的高切换成本（工作流依赖、插件生态、项目兼容性），Clypra 要突破这一惯性需要极强的分发能力和产品力，而
    AIEraDev 团队目前尚未建立品牌信任。长期看，Clypra 最大的复利潜力在于成为'视频编辑领域的 Blender'——依托开源社区积累插件生态和模板资产，但
    Blender 走了二十多年且在 3D 工具中竞争格局远不如视频编辑这般集中。综合评估：技术底子好，但价值捕获路径窄，需持续验证用户增长和 Pro 功能的付费转化，因此给予
    4.5 分。
value_capture_layer: end_application
moat_impact: democratizes_access
key_beneficiaries:
- AIEraDev
- 独立视频创作者与 YouTuber
- FFmpeg 生态
competitive_casualty:
- Adobe Premiere Pro
- CapCut
- Clipchamp
market_opportunities:
- Clypra 的 Tauri+React+Rust 架构为开发高性能跨平台桌面应用提供了全新参考范式，创业团队可借鉴此模式低成本构建其他创意工具（如音频工作站、动画制作软件），兼顾
  Web 开发效率与原生性能
- 围绕 Clypra 的 Open Core 模式，可针对其 AI Pro 功能（自然语言编辑、自动字幕、智能重构图）开发垂直行业插件和模板市场，面向自媒体创作者提供
  AI 增强的视频编辑解决方案
- Clypra 硬件加速解码方案（VideoToolbox/D3D11VA/VAAPI）与亚 10ms 首帧延迟技术，对云端视频转码平台和视频处理微服务场景有参考价值，可作为技术栈选型的备选方案
risk_matrix:
  regulatory: 无 — MIT 协议开源合规风险低；AI Pro 功能若接入第三方模型或云服务需关注 API 服务条款与用户数据隐私合规
  technological: 新生项目工程成熟度未经验证；Tauri v2 生态对复杂视频编辑场景的长期稳定性存疑；硬件加速解码在不同 GPU 和驱动版本下可能存在兼容性问题；与
    Shotcut、Kdenlive 等成熟开源编辑器存在功能完整性差距
  competitive: 视频编辑市场竞争白热化：免费市场有 DaVinci Resolve（功能极其完备）、CapCut（AI 功能丰富且用户基数庞大）、Shotcut/Kdenlive（成熟稳定的开源方案）的多重夹击；付费市场有
    Adobe Premiere 和 Final Cut Pro 的生态壁垒；作为新生项目严重缺乏品牌认知与用户社区基础
  ethical: AI 视频编辑功能（自然语言编辑、自动字幕等）存在被用于生成误导性内容的潜在风险，属于行业共性问题
  additional:
  - 开源视频编辑器项目历史上具有较高的停滞与放弃风险（如 Olive 长期开发未正式发布），AIEraDev 团队的持续维护能力和资金可持续性尚未验证
  - 项目当前处于极早期阶段，GitHub 社区活跃度和贡献者生态建设需要长期投入，存在项目夭折的可能性
confidence:
  impact: low
  compound: low
  hype: low
actionable_insight: speculative_watch
---

**Professional video editing—free and open source forever.**

A modern video editor built on Tauri v2, React 19, and Rust. Hardware-accelerated processing, cross-platform (desktop + mobile), with optional AI-powered features.

Features • Architecture • Installation • Development • Contributing • Open Core

Clypra is a **free, open-source video editor** (MIT License) with professional-grade features. The core editor, effects engine, and all UI components are free forever—no watermarks, no feature limits, no subscriptions required.

Want AI superpowers? Optional Pro features add natural language editing, auto-captions, smart reframing, and more.

**Desktop**: macOS (Apple Silicon & Intel), Windows, Linux**Mobile**: iOS (via Capacitor), Android (via Capacitor)

**Multi-format media import**: MP4, MOV, WebM, MKV, M4V, AVI (video); MP3, WAV, AAC (audio); JPG, PNG, WebP (image)**Frame-accurate trimming**: Precise timeline control with millisecond accuracy**Multi-track timeline**: Professional timeline interface with ruler and visual feedback**Undo/redo system**: 100-level history stack with command pattern architecture

**High-fidelity waveforms**: Peak + RMS visualization with mirrored display (technical details)**Audio synchronization**: Frame-accurate AV sync during playback and export**Volume control**: Per-clip volume adjustment with real-time preview

**Filmstrip thumbnails**: Hardware-accelerated thumbnail generation with adaptive density**Text overlays**: Custom fonts, styles, and animations for titles and captions**Preview canvas**: Real-time compositing with transform controls

**Hardware acceleration**: Native GPU decode via FFmpeg (VideoToolbox/D3D11VA/VAAPI)**Decoder prewarming**: Sub-10ms first-frame latency through predictive decoder initialization**Parallel processing**: Web worker pool for thumbnail generation (2-4× faster rendering)**Efficient caching**: LRU-based decoder pool with 20 concurrent decoders**Real-time monitoring**: 30+ performance metrics tracked across video pipeline

**Persistent projects**: SQLite-backed project storage with auto-save**Media library**: Centralized asset management with metadata caching**Export pipeline**: FFmpeg-based export with codec selection (H.264, H.265, ProRes)

Clypra is architected as a **native desktop and mobile application** with clear separation between frontend UI and backend processing.

**Frontend**

- React 19 with TypeScript (strict mode)
- Zustand for state management (separated stores by domain)
- Vite for build tooling and hot module replacement

**Backend**

- Rust with Tauri v2 for native platform integration
- FFmpeg (via ffmpeg-next) for video/audio processing
- Hardware acceleration: VideoToolbox (macOS), D3D11VA (Windows), VAAPI (Linux)
- DashMap for concurrent data structures

**Mobile**

- Capacitor for iOS/Android deployment
- Native bridge for platform-specific features

**Native Performance**: Rust FFmpeg backend eliminates browser constraints**Desktop-First Architecture**: Optimized for desktop-class workflows, portable to mobile**Hardware Acceleration**: Direct GPU access through native FFmpeg hardware decoders**Efficient IPC**: Tauri commands optimized for minimal serialization overhead**Zero Browser Dependencies**: No WebCodecs, MSE, or web-specific APIs

```
┌─────────────────────────────────────────────────────────────┐
│ Frontend (React/TS) │
│ ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐ │
│ │ Timeline UI │ │ Preview Canvas│ │ Filmstrip Cache │ │
│ └──────┬───────┘ └──────┬────────┘ └────────┬────────┘ │
│ │ │ │ │
│ └─────────────────┴─────────────────────┘ │
│ │ │
│ Tauri IPC Layer │
│ │ │
└───────────────────────────┼─────────────────────────────────┘
│
┌───────────────────────────┼─────────────────────────────────┐
│ Backend (Rust/FFmpeg) │
│ ┌─────────────────┴──────────────────┐ │
│ │ Decoder Pool (LRU, size=20) │ │
│ │ ┌──────────────────────────────┐ │ │
│ │ │ Hardware Decoder Context │ │ │
│ │ │ (VideoToolbox/D3D11/VAAPI) │ │ │
│ │ └──────────────────────────────┘ │ │
│ └─────────────┬────────────────────┬─┘ │
│ │ │ │
│ ┌─────────────▼────────┐ ┌────────▼──────────┐ │
│ │ Frame Decoder │ │ Export Pipeline │ │
│ │ (seek + decode) │ │ (encode + mux) │ │
│ └──────────────────────┘ └───────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```


**Decoder Prewarming**

- Decoders initialized on project load (eliminates 50-100ms cold start)
- Concurrent prewarming (4 decoders at a time)
- First-frame latency: 5-10ms (vs 50-100ms without prewarming)

**Thumbnail Generation**

- Web worker pool (CPU cores - 1, max 4)
- Zero-copy ImageBitmap transfer via Transferable
- 60% reduction in main thread CPU during scroll

**Batch Processing**

- Atlas-based thumbnail storage (reduces IPC overhead by 90%)
- Streaming decode with channel-based delivery
- Concurrent frame decode (up to 20 videos simultaneously)

**Sequential Decode Optimization**

- Smart seeking: forward decode within GOP boundaries (avoids redundant seeks)
- Sequential hit tracking: detects scrubbing patterns
- 70% reduction in seek operations during timeline navigation

For detailed performance metrics and optimization roadmap, see PERFORMANCE-DESKTOP-ROADMAP.md.

Pre-built binaries are available for all supported platforms. Download from the latest release.

**Recommended: Homebrew Installation**

`brew install AIEraDev/tap/clypra`

This method automatically handles Gatekeeper authorization and updates.

**Alternative: Direct Download**

- Download
`Clypra-universal.dmg`

from releases - Open the DMG and drag Clypra to
`/Applications`

- Right-click the app icon and select "Open" to authorize first launch

Supported: macOS 11+ (Big Sur and later), both Apple Silicon and Intel

- Download
`Clypra-x64.msi`

from releases - Run the installer
- If Windows SmartScreen blocks execution, click "More Info" → "Run Anyway"

Supported: Windows 10 (version 1809+) and Windows 11

- Download
`Clypra-x86_64.AppImage`

from releases - Make executable:
`chmod +x Clypra-x86_64.AppImage`

- Run:
`./Clypra-x86_64.AppImage`


Supported: Ubuntu 20.04+, Fedora 35+, Debian 11+, and derivatives

**Required**

- Node.js 18+ with npm
- Rust 1.70+ (install via rustup)
- FFmpeg 6.0+ with development libraries

**Platform-Specific**

**macOS**: Xcode Command Line Tools (`xcode-select --install`

)**Windows**: Visual Studio 2019+ with C++ desktop development tools**Linux**: Build essentials, webkit2gtk, libayatana-appindicator

**macOS**

`brew install ffmpeg`

**Ubuntu/Debian**

`sudo apt install ffmpeg libavcodec-dev libavformat-dev libavutil-dev libswscale-dev`

**Windows (Chocolatey)**

`choco install ffmpeg`

**Windows (Manual)**

- Download from ffmpeg.org/download.html
- Extract to
`C:\ffmpeg`

- Add
`C:\ffmpeg\bin`

to system PATH

```
# Clone repository
git clone https://github.com/AIEraDev/clypra.git
cd clypra
# Install dependencies
npm install
# Configure environment
cp .env.example .env
# Edit .env and add your Clypra API key (required for text effects)
# Development mode with hot reload
npm run tauri dev
# Production build
npm run build
npm run tauri build
```

The codebase is organized by domain with clear separation of concerns:

```
src/
├── components/ # React components
│ ├── editor/ # Core editor UI (Timeline, Preview, Filmstrip)
│ ├── screens/ # Full-screen views (Launch, Settings)
│ └── ui/ # Reusable UI primitives (Modals, Icons, Buttons)
├── store/ # Zustand state stores (by domain)
│ ├── timelineStore.ts # Timeline structure (tracks, clips, gaps)
│ ├── playbackStore.ts # Playback state and AV sync
│ ├── projectStore.ts # Project metadata and media assets
│ └── ... # uiStore, settingsStore, historyStore
├── core/ # Core engine logic
│ ├── runtime/ # ProjectSession and lifecycle management
│ ├── scheduler/ # Frame scheduler for preview rendering
│ ├── resources/ # PreviewMediaPool (video/audio elements)
│ ├── render/ # Canvas rasterization and compositing
│ └── timeline/ # Timeline calculations and utilities
├── lib/ # Shared utilities
│ ├── platform/ # Tauri IPC wrappers
│ ├── monitoring/ # Performance monitoring
│ ├── workers/ # Web worker pool
│ └── ... # Audio, video, filmstrip utilities
├── hooks/ # Custom React hooks
├── types/ # TypeScript type definitions
└── App.tsx # Application entry point
src-tauri/
├── src/
│ ├── commands/ # Tauri command handlers
│ │ ├── thumbnail.rs # Video decode commands
│ │ ├── export.rs # Export pipeline
│ │ └── ...
│ ├── thumbnail_engine/# FFmpeg decoder pool
│ │ ├── decoder.rs # Hardware-accelerated decoder
│ │ ├── cache.rs # LRU caching
│ │ └── ...
│ └── lib.rs # Tauri application setup
└── Cargo.toml # Rust dependencies
```


Clypra uses the Clypra API for text effects and templates. To enable these features:

-
Copy

`.env.example`

to`.env`

:cp .env.example .env

-
Add your API key to

`.env`

:`VITE_CLYPRA_API_KEY=your_api_key_here`

-
**Important**: Never commit`.env`

to version control (already in`.gitignore`

)

The API provides:

- Text effects library with customizable styles
- Canvas-based text templates with WebM video previews
- Google Fonts integration

```
# Run all tests
npm test
# Run Rust tests
cd src-tauri && cargo test
# Run specific test suite
npm test -- src/lib/__tests__/timelineUtils.test.ts
# Run with coverage
npm test -- --coverage
```

```
# TypeScript type checking
npx tsc --noEmit
# Rust linting
cd src-tauri && cargo clippy -- -D warnings
# Format code
npm run format
cd src-tauri && cargo fmt
```

Clypra uses Zustand with domain-separated stores to maintain clear ownership boundaries:

**timelineStore**: Timeline structure (tracks, clips, transitions, gaps)**playbackStore**: Playback state, playhead position, AV sync**projectStore**: Project metadata, media assets, persistence**historyStore**: Undo/redo command stack**uiStore**: UI state (modals, selections, drag state)**settingsStore**: User preferences and application settings

Each store owns its domain and exposes actions. Cross-store communication happens through explicit calls, not shared mutable state.

**Import**: FFmpeg probe extracts metadata (duration, dimensions, codec)**Thumbnail**: Rust decoder generates filmstrip tiles (L0-L3 density tiers)**Preview**: HTMLVideoElement (live playback) or Canvas (composited frames)**Export**: Frame scheduler → RGBA frames → FFmpeg encoder → MP4/MOV

The application includes comprehensive performance monitoring:

**Decoder metrics**: Cache hits, evictions, decode latency**Export metrics**: Frame write time, fps, total duration**Render metrics**: Layer rendering time, canvas pool efficiency**Cache metrics**: Filmstrip cache hit rate, memory usage

Access metrics in development via `window.__performanceMonitor`

.

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

- Fork the repository
- Create a feature branch (
`git checkout -b feature/amazing-feature`

) - Make your changes with tests
- Ensure all tests pass (
`npm test && cd src-tauri && cargo test`

) - Commit with conventional commits (
`feat:`

,`fix:`

,`docs:`

, etc.) - Push to your fork and open a Pull Request

**TypeScript**: Strict mode enabled, ESLint + Prettier**Rust**:`cargo fmt`

+`cargo clippy`

(no warnings)**Commits**: Conventional commits format**Documentation**: JSDoc for public APIs, inline comments for complex logic

This project is licensed under the MIT License - see the LICENSE file for details.

Clypra uses FFmpeg for video processing. FFmpeg is licensed under:

- LGPL 2.1+ (default build)
- GPL 2+ (if built with GPL-only components)

Binary releases include FFmpeg under LGPL. If you build with GPL components, ensure GPL compliance.

**Tauri**: Cross-platform native application framework**FFmpeg**: Video/audio processing engine**React**: UI framework**shadcn/ui**: Component library foundation

**Issues**: GitHub Issues**Discussions**: GitHub Discussions**Documentation**: Project Wiki

Clypra uses an **Open Core** business model:

✅ **Core Video Editor** - Multi-track timeline, frame-accurate editing, hardware-accelerated processing

✅ **Effects Engine** - Professional video effects, transitions, filters (via `@clypra-studio/engine`

)

✅ **Audio Tools** - Waveform visualization, volume control, AV sync

✅ **Export Pipeline** - H.264, H.265, ProRes export with FFmpeg

✅ **Text Overlays** - Custom fonts, styles, and animations

✅ **All UI Components** - Full source code, no proprietary dependencies

**No watermarks. No feature limits. No subscriptions. Forever.**

🎯 **Natural Language Editing** - "Remove all pauses", "Add captions", "Make this shorter"

🎯 **Auto-Captioning** - Transcription with speaker detection and customizable styles

🎯 **Smart Reframe** - Auto-crop for Instagram Stories, TikTok, YouTube Shorts

🎯 **Scene Detection** - AI-powered scene splitting and B-roll suggestions

🎯 **Audio Enhancement** - Noise removal, EQ, compression

🎯 **Voice Cloning** - Match narrator voice across clips (coming soon)

🎯 **Multi-language Dubbing** - Translate and dub with lip sync (coming soon)

**Pricing**: Free tier (100 AI calls/month) • Pro ($10/month, unlimited) • Enterprise (custom)

We believe professional video editing should be free and accessible to everyone. Open source ensures:

**Transparency**- You can audit every line of code**Ownership**- Your edits, your data, your workflow**Community**- Contributions from creators worldwide**Longevity**- The editor can't be shut down or paywalled

The Pro AI features fund full-time development on the open source core. Everyone wins.

See PERFORMANCE-DESKTOP-ROADMAP.md for upcoming performance improvements.

Planned features:

- Mobile app release (iOS/Android via Capacitor)
- Advanced color grading
- Multi-camera editing
- Plugin system for extensions
- GPU-accelerated effects rendering

**Pro Roadmap** (AI features):

- Natural language commands (Q3 2026)
- Auto-captioning (Q3 2026)
- Smart reframe (Q4 2026)
- Voice cloning (Q1 2027)
- Multi-language dubbing (Q2 2027)