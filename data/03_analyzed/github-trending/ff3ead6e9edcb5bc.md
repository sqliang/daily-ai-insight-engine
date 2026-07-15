---
title: kyutai-labs/pocket-tts
source: https://github.com/kyutai-labs/pocket-tts
author: []
published: ''
created: '2026-07-08'
description: 'A TTS that fits in your CPU (and pocket)Pocket TTS A lightweight text-to-speech
  (TTS) application designed to run efficiently on CPUs. Forget about the hassle of
  using GPUs and web APIs serving TTS models. With Kyutai''s Pocket TTS, generating
  audio is just a pip install and a function call away. Supports Python 3.10, 3.11,
  3.12, 3.13 and 3.14. Requires PyTorch 2.5+. Does not require the gpu version of
  PyTorch. 🔊 Demo | 🐱‍💻GitHub Repository | 🤗 Hugging Face Model Card | ⚙️ Tech report
  | 📄 Paper | 📚 Documentation Main takeaways Runs on CPU Small model size, 100M parameters
  Audio streaming Low latency, ~200ms to get the first audio chunk Faster than real-time,
  ~6x real-time on a CPU of MacBook Air M4 Uses only 2 CPU cores Python API and CLI
  Voice cloning Multi-language support: english, french, german, portuguese, italian,
  spanish Can handle infinitely long text inputs Can run on client-side in the browser
  Additional languages may be added in the future. Trying it from the website, without
  installing anything Navigate to the Kyutai website to try it out directly in your
  browser. You can input text, select different voices, and generate speech without
  any installation. Trying it with the CLI The generate command You can use pocket-tts
  directly from the command line. We recommend using uv as it installs any dependencies
  on the fly in an isolated environment (uv installation instructions here). You can
  also use pip install pocket-tts to install it manually. This will generate a wav
  file ./tts_output.wav saying the default text with the default voice, and display
  some speed statistics. uvx pocket-tts generate # or if you installed it manually
  with pip: pocket-tts generate Modify the voice with --voice and the text with --text.
  We provide a small catalog of voices. Choose a pretrained language model with --language
  when running generate, export-voice, or serve (default: english). Non-english languages
  have also biggers 24 layers variants that are higher quality but slower. You can
  select them by using for example --language italian_24l. The --config option accepts
  only a local YAML path for custom weights. You can take a look at this page which
  details the licenses for each voice. alba (en) giovanni (it) lola (es) juergen (de)
  rafael (pt) estelle (fr) anna (en) azelma (en) bill_boerst (en) caro_davy (en) charles
  (en) cosette (en) eponine (en) eve (en) fantine (en) george (en) jane (en) jean
  (en) javert (en) marius (en) mary (en) michael (en) paul (en) peter_yearsley (en)
  stuart_bell (en) vera (en) The --voice argument can also take a plain wav file as
  input for voice cloning. You can use your own or check out our voice repository.
  We recommend cleaning the sample before using it with Pocket TTS, because the audio
  quality of the sample is also reproduced. Feel free to check out the generate documentation
  for more details and examples. For trying multiple voices and prompts quickly, prefer
  using the serve command. The serve command You can also run a local server to generate
  audio via HTTP requests. uvx pocket-tts serve # or if you installed it manually
  with pip: pocket-tts serve Navigate to http://localhost:8000 to try the web interface,
  it''s faster than the command line as the model is kept in memory between requests.
  You can check out the serve documentation for more details and examples. The export-voice
  command Processing an audio file (e.g., a .wav or .mp3) for voice cloning is relatively
  slow, but loading a safetensors file -- a voice embedding converted from an audio
  file -- is very fast. You can use the export-voice command to do this conversion.
  See the export-voice documentation for more details and examples. Using it as a
  Python library You can try out the Python library on Colab here. Install the package
  with pip install pocket-tts # or uv add pocket-tts You can use this package as a
  simple Python library to generate audio from text. from pocket_tts import TTSModel
  import scipy.io.wavfile tts_model = TTSModel.load_model() voice_state = tts_model.get_state_for_audio_prompt(
  "alba" # One of the pre-made voices, see above # You can also use any voice file
  you have locally or from Hugging Face: # "./some_audio.wav" # or "hf://kyutai/tts-voices/expresso/ex01-ex02_default_001_channel2_198s.wav"
  ) audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")
  # Audio is a 1D torch tensor containing PCM data. scipy.io.wavfile.write("output.wav",
  tts_model.sample_rate, audio.numpy()) You can have multiple voice states around
  if you have multiple voices you want to use. load_model() and get_state_for_audio_prompt()
  are relatively slow operations, so we recommend to keep the model and voice states
  in memory if you can. For faster voice loading, you can export voice states to safetensors
  files: from pocket_tts import TTSModel, export_model_state model = TTSModel.load_model()
  # Export a voice state for fast loading later model_state = model.get_state_for_audio_prompt("some_voice.wav")
  export_model_state(model_state, "./some_voice.safetensors") # Later, load it quickly,
  this is quite fast as it''s just reading the kvcache # from disk and doesn''t do
  any others computations. model_state_copy = model.get_state_for_audio_prompt("./some_voice.safetensors")
  audio = model.generate_audio(model_state_copy, "Hello world!") You can check out
  the Python API documentation for more details and examples. Unsupported features
  At the moment, we do not support (but would love pull requests adding): Adding silence
  in the text input to generate pauses. We tried running this TTS model on the GPU
  but did not observe a speedup compared to CPU execution, notably because we use
  a batch size of 1 and a very small model. Development and local setup We accept
  contributions! Feel free to open issues or pull requests on GitHub. You can find
  development instructions in the CONTRIBUTING.md file. You''ll also find there how
  to have an editable install of the package for local development. In-browser implementations
  Pocket TTS is small enough to run directly in your browser in WebAssembly/JavaScript.
  We don''t have official support for this yet, but you can try out one of these community
  implementations: wasm-pocket-tts by @LaurentMazare: Rust port of pocket TTS with
  XN. Demo here pocket-tts-onnx-export by @KevinAHM: Model exported to .onnx and run
  using ONNX Runtime Web. Demo here pocket-tts by @babybirdprd: Candle version (Rust)
  with WebAssembly and PyO3 bindings, meaning it can run on the web too. jax-js by
  @ekzhang: Using jax-js, a ML library for the web. Demo here Alterative implementations
  pocket-tts-mlx by @jishnuvenugopal - MLX backend optimized for Apple Silicon pocket-tts-xn
  by @LaurentMazare - A Rust port of Pocket TTS implemented with XN. pocket-tts-candle
  by @babybirdprd - Candle version (Rust) with WebAssembly and PyO3 bindings. PocketTTS.cpp
  by @VolgaGerm - Single-file C++ runtime using ONNX Runtime, with CLI, HTTP server,
  and FFI C API. sherpa-onnx by @csukuangfj - Run PocketTTS on Windows, macOS, Linux,
  and embedded boards (Raspberry Pi, Jetson, RK3588, etc.) with bindings for 12 programming
  languages: C++, C, Python, JavaScript, Java, C#, Kotlin, Swift, Go, Dart, Rust,
  Pascal, plus WebAssembly. pocket-tts-csharp by @TheAjaykrishnanR - A C# port of
  Pocket TTS implemented using TorchSharp and TorchSharp.PyBridge for ease of use
  as a library in .NET projects. Projects using Pocket TTS pocket-reader by @lukasmwerner-
  Browser screen reader pocket-tts-wyoming by @ikidd - Docker container for pocket-tts
  using Wyoming protocol, ready for Home Assistant Voice use. Sonorus by @KevinAHM
  - Talk to any named character in Hogwarts Legacy with their original voice. Native
  macOS App by @slaughters85j - Native macOS app, Python-free. Runs Pocket-TTS via
  Core ML, fully on-device. Includes signed and notarized .app releases. Electron
  macOS App by @slaughters85j - Electron Mac Desktop App + macOS Quick Action pocket-tts-openai_streaming_server
  by @teddybear082 - OpenAI-compatible streaming server, dockerized and with an .exe
  release pocket-tts-unity by @lookbe - A Unity 6 integration for Pocket-TTS. ComfyUI-Pocket-TTS
  by @ai-joe-git Lightweight CPU-based Text-to-Speech for ComfyUI pocket-tts-server
  by @ai-joe-git A lightweight, real-time voice cloning and chat server with OpenAI-compatible
  API. Clone any voice with just 20 seconds of audio and chat with AI using that voice
  instantly. discord-tts by @alkmei - Multivoice Discord text-to-speech bot that uses
  Pocket TTS. cursed-codex by @dooart - AI coding agent with unhinged live football
  commentary pocket-tts-deno Port of pocket-tts-server as a wasm + onnx deno server
  with voice TTS API. FrontPocket by @markd89 - Front-end for Pocket-TTS to speak
  text from clipboard, file, CLI (hotkeys) & GUI toolbar. Change playback speed, voice,
  and move forward/backward between sentences instantaneously. openclaw-pockettts
  by @dodgyrabbit - A Docker container with the Python implementation but exposed
  as an OpenAI TTS API for easy integration with OpenClaw. openclaw-pocketts.cpp by
  @dodgyrabbit - A Docker container with the PocketTTS.cpp version, packaged for easy
  integration with OpenClaw. tts-audiobook-tool by @zeropointnine - Multi-model audiobook
  generator with automatic error detection, 48khz upscaling, synced browser reader,
  stand-alone server-mode. seshat-tts by @scriptriva - Accessibility tool that provides
  real-time audio synthesis for games and apps. It also features a voice manager capable
  of cloning voices based on user presets. LocalVocal.ai by @joshwhiton - Fully local
  conversational voice-harness for Macs with Apple Silicon. Includes voice-activity
  & turn detection, dictation, voice cloning, CLI to talk to Claude, Codex... and
  more. Prohibited use Use of our model must comply with all applicable laws and regulations
  and must not result in, involve, or facilitate any illegal, harmful, deceptive,
  fraudulent, or unauthorized activity. Prohibited uses include, without limitation,
  voice impersonation or cloning without explicit and lawful consent; misinformation,
  disinformation, or deception (including fake news, fraudulent calls, or presenting
  generated content as genuine recordings of real people or events); and the generation
  of unlawful, harmful, libelous, abusive, harassing, discriminatory, hateful, or
  privacy-invasive content. We disclaim all liability for any non-compliant use. Authors
  Manu Orsini*, Simon Rouard*, Gabriel De Marmiesse*, Václav Volhejn, Neil Zeghidour,
  Alexandre Défossez *equal contribution'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: ff3ead6e9edcb5bc
manifest_dates:
- '2026-07-08'
source_type: community_discussion
tldr: Kyutai 发布轻量级 CPU 端文本转语音工具 Pocket TTS
objective_summary: Kyutai 实验室发布了 Pocket TTS，一款专为 CPU 设计的轻量级文本转语音应用，仅 1 亿参数、支持 6 种语言、语音克隆和流式生成。在
  MacBook Air M4 上达到约 200ms 首音延迟和 6 倍实时速度，可通过 pip 安装或直接命令行使用。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Kyutai
  technologies:
  - TTS
  - PyTorch
  - safetensors
  - ONNX
  - WebAssembly
  key_people:
  - Manu Orsini
  - Simon Rouard
  - Gabriel De Marmiesse
  - Václav Volhejn
  - Neil Zeghidour
  - Alexandre Défossez
key_logic_flow:
- Kyutai 实验室发布了 Pocket TTS，一个仅 1 亿参数的轻量级文本转语音应用，专为 CPU 运行设计，无需 GPU。
- Pocket TTS 支持英语、法语、德语、葡萄牙语、意大利语和西班牙语共 6 种语言，提供 26 种预设语音。
- 该工具在 MacBook Air M4 上实现约 200ms 首音延迟和 6 倍实时速度，仅使用 2 个 CPU 核心。
- 支持语音克隆功能，可通过音频文件或 safetensors 嵌入快速加载自定义音色。
- 提供 Python API、CLI 和 HTTP 服务器三种使用方式，支持无限长文本输入和流式音频生成。
- 社区已贡献多种移植版本，包括 WebAssembly/JavaScript、Rust、ONNX Runtime、C#、Unity 等平台实现。
specialized_tags:
  github:
    projectName: kyutai-labs/pocket-tts
    projectUrl: https://github.com/kyutai-labs/pocket-tts
    primaryLanguage: Python
    licenseType: null
    domain: ai_ml
    crossTags:
    - open-source
    - cpu-inference
    - on-device
    aiDetail:
      primaryCategories:
      - multimodal
      - model_serving
      agentSubcategory: null
      techTags:
      - TTS
      - voice-cloning
      - speech-synthesis
      - streaming-inference
extract_result: success
impact_score:
  score: 6.5
  reason: 该事件并非范式转移级别的突破（非 8-10 分），但远超日常小迭代（非 1-3 分）。评分为 6.5 的依据：Pocket TTS 以 1 亿参数在
    CPU 上实现约 200ms 首音延迟和 6 倍实时速度，支持 6 种语言和语音克隆，通过 pip 一键安装即可使用，大幅降低了高质量 TTS 的部署门槛。其意义类似于
    Whisper 对语音识别的冲击——让 TTS 从 GPU/云端依赖走向人人可用的本地工具。社区已涌现 WASM、Rust、ONNX、C#、Unity 等多平台移植，表明生态影响正在扩散。但架构基于现有
    Transformer 范式，并非全新技术路线，且非英语语言质量仍有提升空间，因此评分为 6.5。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: CPU 端即刻可用的高质量 TTS，pip install 即开即用且支持语音克隆
hype_assessment:
  level: low
  reason: 项目的宣传基调务实克制，没有使用'颠覆''革命性'等 PR 滥用语。所有性能指标（200ms 延迟、6 倍实时、2 个 CPU 核心）均为具体且可复现的基准测试数据。项目同时坦诚说明了局限性：GPU
    无加速效果、非英语有 24 层大模型变体但质量/速度有 trade-off、语音克隆依赖清洁音频样本。提供详细技术报告和论文链接以供验证，信息透明度高，炒作嫌疑极低。
information_entropy: high
domain_disruption:
  technical_innovation: 在 CPU 端实现百毫秒级首音延迟和 6 倍实时速度的轻量级 TTS，通过仅 1 亿参数的小模型设计和单样本批处理策略，完全规避了
    GPU 依赖，使高质量语音合成可部署到任意消费级硬件。引入 safetensors 格式的语音嵌入缓存机制，实现了语音克隆状态的接近零成本切换，大幅提升了多音色场景下的实用效率。
  business_model: 以完全开源方式挑战现有商业 TTS API（如 ElevenLabs、OpenAI TTS）的按量计费模式。类似 Whisper
    对语音识别行业的冲击，Pocket TTS 可能催生大量基于本地 TTS 的应用生态——从内容创作工具到无障碍辅助、从游戏语音到物联网设备——推动 TTS
    从 API 订阅制向本地免费可用的商业模式转变。社区已自发移植到多种平台，印证了这一趋势。
engineering_complexity: production_ready
compound_value:
  score: 7.0
  reason: Pocket TTS 的核心价值在于将 TTS 从 GPU/云端依赖中解放，实现纯 CPU 本地运行。100M 参数量级、MIT 开源协议、~200ms
    首音延迟、6 倍实时速度、支持语音克隆，这些特性使其具备成为本地 TTS 基础设施层的潜力。社区生态正快速形成——WASM/JavaScript、Rust、ONNX
    Runtime、Unity 等多平台移植表明开发者粘性较强。长期复利的关键在于：如果 Pocket TTS 成为类似 SentencePiece 或 Whisper
    那样的行业标准组件，嵌入各类应用（浏览器、桌面、移动端、嵌入式），其价值将随时间指数增长。但风险同样显著：Kyutai 是非营利研究实验室，长期维护和持续迭代的不确定性高于商业公司；100M
    参数规模在语音自然度、情感表现力上存在天花板，难以完全替代 ElevenLabs 或 OpenAI TTS 的高端场景；TTS 赛道竞争激烈，可能有更强模型后来居上。综合来看，有潜力成为细分赛道基础设施，但需持续观察生态发展和维护持续性。
value_capture_layer: foundation_model
moat_impact: democratizes_access
key_beneficiaries:
- Kyutai
- Hugging Face
- Apple
- 本地 AI 应用开发者
competitive_casualty:
- ElevenLabs
- OpenAI (TTS API)
- Google Cloud TTS
- AWS Polly
market_opportunities:
- 开发者可基于 Pocket TTS 的 1 亿参数 CPU 级模型，为边缘设备、IoT 和离线场景构建语音交互产品，无需 GPU 即可实现实时语音合成
- 语音克隆功能可直接应用于无障碍辅助工具、有声书制作、多语言配音等场景，降低高质量 TTS 的部署门槛和技术成本
- WebAssembly/JavaScript 社区移植版本预示着浏览器端语音合成的可能性，前端开发者可探索零部署的在线语音产品形态
risk_matrix:
  regulatory: 语音克隆功能可能触发各国对 AI 合成语音的监管要求，如欧盟 AI Act 对高风险 AI 系统的透明度义务、美国各州深度伪造法案对未经同意的声音模仿的禁令，以及
    GDPR 下生物特征数据的处理限制
  technological: 模型仅 1 亿参数且面向 CPU，在多语言音质、情感表达和噪音鲁棒性上可能逊于更大规模的 TTS 模型（如 ElevenLabs、VALL-E），面临被后续更优架构替代的风险
  competitive: TTS 赛道竞争激烈，商业层面有 ElevenLabs、Play.ht、Azure Speech 等，开源层面有 Coqui AI、Bark、XTTS
    等竞品，Pocket TTS 的 CPU 优势可能被后续开源模型快速追赶
  ethical: 语音克隆功能若被滥用可导致深度伪造音频、冒充他人声音实施诈骗或虚假信息传播，且预设音色库中的说话人是否获得明确授权许可需重点关注
  additional: []
confidence:
  impact: high
  compound: medium
  hype: medium
actionable_insight: deep_dive
---

A lightweight text-to-speech (TTS) application designed to run efficiently on CPUs. Forget about the hassle of using GPUs and web APIs serving TTS models. With Kyutai's Pocket TTS, generating audio is just a pip install and a function call away.

Supports Python 3.10, 3.11, 3.12, 3.13 and 3.14. Requires PyTorch 2.5+. Does not require the gpu version of PyTorch.

🔊 Demo | 🐱💻GitHub Repository | 🤗 Hugging Face Model Card | ⚙️ Tech report | 📄 Paper | 📚 Documentation

- Runs on CPU
- Small model size, 100M parameters
- Audio streaming
- Low latency, ~200ms to get the first audio chunk
- Faster than real-time, ~6x real-time on a CPU of MacBook Air M4
- Uses only 2 CPU cores
- Python API and CLI
- Voice cloning
- Multi-language support: english, french, german, portuguese, italian, spanish
- Can handle infinitely long text inputs
- Can run on client-side in the browser

Additional languages may be added in the future.

Navigate to the Kyutai website to try it out directly in your browser. You can input text, select different voices, and generate speech without any installation.

You can use pocket-tts directly from the command line. We recommend using
`uv`

as it installs any dependencies on the fly in an isolated environment (uv installation instructions here).
You can also use `pip install pocket-tts`

to install it manually.

This will generate a wav file `./tts_output.wav`

saying the default text with the default voice, and display some speed statistics.

```
uvx pocket-tts generate
# or if you installed it manually with pip:
pocket-tts generate
```

Modify the voice with `--voice`

and the text with `--text`

. We provide a small catalog of voices.
Choose a pretrained language model with `--language`

when running `generate`

, `export-voice`

, or `serve`

(default: `english`

). Non-english languages have also biggers 24 layers variants that are higher quality but slower. You can select them by using for example `--language italian_24l`

.
The `--config`

option accepts only a local YAML path for custom weights.

You can take a look at this page which details the licenses for each voice.

- alba (en)
- giovanni (it)
- lola (es)
- juergen (de)
- rafael (pt)
- estelle (fr)
- anna (en)
- azelma (en)
- bill_boerst (en)
- caro_davy (en)
- charles (en)
- cosette (en)
- eponine (en)
- eve (en)
- fantine (en)
- george (en)
- jane (en)
- jean (en)
- javert (en)
- marius (en)
- mary (en)
- michael (en)
- paul (en)
- peter_yearsley (en)
- stuart_bell (en)
- vera (en)

The `--voice`

argument can also take a plain wav file as input for voice cloning.
You can use your own or check out our voice repository.
We recommend cleaning the sample before using it with Pocket TTS, because the audio quality of the sample is also reproduced.

Feel free to check out the generate documentation for more details and examples.
For trying multiple voices and prompts quickly, prefer using the `serve`

command.

You can also run a local server to generate audio via HTTP requests.

```
uvx pocket-tts serve
# or if you installed it manually with pip:
pocket-tts serve
```

Navigate to `http://localhost:8000`

to try the web interface, it's faster than the command line as the model is kept in memory between requests.

You can check out the serve documentation for more details and examples.

Processing an audio file (e.g., a .wav or .mp3) for voice cloning is relatively slow, but loading a safetensors file -- a voice embedding converted from an audio file -- is very fast. You can use the `export-voice`

command to do this conversion. See the export-voice documentation for more details and examples.

You can try out the Python library on Colab here.

Install the package with

```
pip install pocket-tts
# or
uv add pocket-tts
```

You can use this package as a simple Python library to generate audio from text.

```
from pocket_tts import TTSModel
import scipy.io.wavfile
tts_model = TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt(
"alba" # One of the pre-made voices, see above
# You can also use any voice file you have locally or from Hugging Face:
# "./some_audio.wav"
# or "hf://kyutai/tts-voices/expresso/ex01-ex02_default_001_channel2_198s.wav"
)
audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")
# Audio is a 1D torch tensor containing PCM data.
scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())
```

You can have multiple voice states around if
you have multiple voices you want to use. `load_model()`

and `get_state_for_audio_prompt()`

are relatively slow operations,
so we recommend to keep the model and voice states in memory if you can.

For faster voice loading, you can export voice states to safetensors files:

```
from pocket_tts import TTSModel, export_model_state
model = TTSModel.load_model()
# Export a voice state for fast loading later
model_state = model.get_state_for_audio_prompt("some_voice.wav")
export_model_state(model_state, "./some_voice.safetensors")
# Later, load it quickly, this is quite fast as it's just reading the kvcache
# from disk and doesn't do any others computations.
model_state_copy = model.get_state_for_audio_prompt("./some_voice.safetensors")
audio = model.generate_audio(model_state_copy, "Hello world!")
```

You can check out the Python API documentation for more details and examples.

At the moment, we do not support (but would love pull requests adding):

We tried running this TTS model on the GPU but did not observe a speedup compared to CPU execution, notably because we use a batch size of 1 and a very small model.

We accept contributions! Feel free to open issues or pull requests on GitHub.

You can find development instructions in the CONTRIBUTING.md file. You'll also find there how to have an editable install of the package for local development.

Pocket TTS is small enough to run directly in your browser in WebAssembly/JavaScript. We don't have official support for this yet, but you can try out one of these community implementations:

- wasm-pocket-tts by @LaurentMazare: Rust port of pocket TTS with XN. Demo here
- pocket-tts-onnx-export by @KevinAHM: Model exported to .onnx and run using ONNX Runtime Web. Demo here
- pocket-tts by @babybirdprd: Candle version (Rust) with WebAssembly and PyO3 bindings, meaning it can run on the web too.
- jax-js by @ekzhang: Using jax-js, a ML library for the web. Demo here

- pocket-tts-mlx by @jishnuvenugopal - MLX backend optimized for Apple Silicon
- pocket-tts-xn by @LaurentMazare - A Rust port of Pocket TTS implemented with XN.
- pocket-tts-candle by @babybirdprd - Candle version (Rust) with WebAssembly and PyO3 bindings.
- PocketTTS.cpp by @VolgaGerm - Single-file C++ runtime using ONNX Runtime, with CLI, HTTP server, and FFI C API.
- sherpa-onnx by @csukuangfj - Run PocketTTS on
**Windows, macOS, Linux**, and embedded boards (Raspberry Pi, Jetson, RK3588, etc.) with bindings for 12 programming languages:**C++, C, Python, JavaScript, Java, C#, Kotlin, Swift, Go, Dart, Rust, Pascal**, plus WebAssembly. - pocket-tts-csharp by @TheAjaykrishnanR - A C# port of Pocket TTS implemented using TorchSharp and TorchSharp.PyBridge for ease of use as a library in .NET projects.

- pocket-reader by @lukasmwerner- Browser screen reader
- pocket-tts-wyoming by @ikidd - Docker container for pocket-tts using Wyoming protocol, ready for Home Assistant Voice use.
- Sonorus by @KevinAHM - Talk to any named character in Hogwarts Legacy with their original voice.
- Native macOS App by @slaughters85j - Native macOS app, Python-free. Runs Pocket-TTS via Core ML, fully on-device. Includes signed and notarized .app releases.
- Electron macOS App by @slaughters85j - Electron Mac Desktop App + macOS Quick Action
- pocket-tts-openai_streaming_server by @teddybear082 - OpenAI-compatible streaming server, dockerized and with an
`.exe`

release - pocket-tts-unity by @lookbe - A Unity 6 integration for Pocket-TTS.
- ComfyUI-Pocket-TTS by @ai-joe-git Lightweight CPU-based Text-to-Speech for ComfyUI
- pocket-tts-server by @ai-joe-git A lightweight, real-time voice cloning and chat server with OpenAI-compatible API. Clone any voice with just 20 seconds of audio and chat with AI using that voice instantly.
- discord-tts by @alkmei - Multivoice Discord text-to-speech bot that uses Pocket TTS.
- cursed-codex by @dooart - AI coding agent with unhinged live football commentary
- pocket-tts-deno Port of pocket-tts-server as a wasm + onnx deno server with voice TTS API.
- FrontPocket by @markd89 - Front-end for Pocket-TTS to speak text from clipboard, file, CLI (hotkeys) & GUI toolbar. Change playback speed, voice, and move forward/backward between sentences instantaneously.
- openclaw-pockettts by @dodgyrabbit - A Docker container with the Python implementation but exposed as an OpenAI TTS API for easy integration with OpenClaw.
- openclaw-pocketts.cpp by @dodgyrabbit - A Docker container with the PocketTTS.cpp version, packaged for easy integration with OpenClaw.
- tts-audiobook-tool by @zeropointnine - Multi-model audiobook generator with automatic error detection, 48khz upscaling, synced browser reader, stand-alone server-mode.
- seshat-tts by @scriptriva - Accessibility tool that provides real-time audio synthesis for games and apps. It also features a voice manager capable of cloning voices based on user presets.
- LocalVocal.ai by @joshwhiton - Fully local conversational voice-harness for Macs with Apple Silicon. Includes voice-activity & turn detection, dictation, voice cloning, CLI to talk to Claude, Codex... and more.

Use of our model must comply with all applicable laws and regulations and must not result in, involve, or facilitate any illegal, harmful, deceptive, fraudulent, or unauthorized activity. Prohibited uses include, without limitation, voice impersonation or cloning without explicit and lawful consent; misinformation, disinformation, or deception (including fake news, fraudulent calls, or presenting generated content as genuine recordings of real people or events); and the generation of unlawful, harmful, libelous, abusive, harassing, discriminatory, hateful, or privacy-invasive content. We disclaim all liability for any non-compliant use.

Manu Orsini*, Simon Rouard*, Gabriel De Marmiesse*, Václav Volhejn, Neil Zeghidour, Alexandre Défossez

*equal contribution