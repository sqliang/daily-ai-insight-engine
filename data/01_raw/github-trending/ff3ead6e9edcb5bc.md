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
pipeline_stage: ingested
id: ff3ead6e9edcb5bc
manifest_dates:
- '2026-07-08'
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