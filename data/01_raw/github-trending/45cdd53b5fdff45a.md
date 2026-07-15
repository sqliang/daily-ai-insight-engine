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
pipeline_stage: ingested
id: 45cdd53b5fdff45a
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