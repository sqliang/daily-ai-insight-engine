---
title: 1jehuang/jcode
source: https://github.com/1jehuang/jcode
author: []
published: ''
created: '2026-06-21'
description: 'Coding Agent Harness jcode The next generation coding agent harness
  to raise the skill ceiling. Built for multi-session workflows, infinite customizability,
  and performance. Features · Install · Quick Start · Further Reading · Contributing
  Installation # macOS & Linux curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh
  | bash Need Windows, Homebrew, source builds, provider setup, or tell your agent
  to set it up for you? Jump to detailed installation. Performance & Resource Efficiency
  jcode is built to be as performant and resource efficient as possible. Every metric
  is optimized to the bone, which is important for scaling multi-session workflows.
  Here we sample a few metrics to show the difference: RAM usage and boot up. RAM
  comparison 1 active session Tool PSS Comparison jcode (local embedding off) 27.8
  MB baseline jcode 167.1 MB 6.0× more RAM pi 144.4 MB 5.2× more RAM Codex CLI 140.0
  MB 5.0× more RAM OpenCode 371.5 MB 13.4× more RAM GitHub Copilot CLI 333.3 MB 12.0×
  more RAM Cursor Agent 214.9 MB 7.7× more RAM Claude Code 386.6 MB 13.9× more RAM
  Antigravity CLI 243.7 MB 8.8× more RAM 10 active sessions Tool PSS Comparison jcode
  (local embedding off) 117.0 MB baseline jcode 260.8 MB 2.2× more RAM pi 833.0 MB
  7.1× more RAM Codex CLI 334.8 MB 2.9× more RAM OpenCode 3237.2 MB 27.7× more RAM
  GitHub Copilot CLI 1756.5 MB 15.0× more RAM Cursor Agent 1632.4 MB 14.0× more RAM
  Claude Code 2300.6 MB 19.7× more RAM Antigravity CLI 1021.2 MB 8.7× more RAM Time
  to first frame Tool Time to first frame Range Comparison jcode 14.0 ms 10.1–19.3
  ms baseline Antigravity CLI 383.5 ms 363.1–415.4 ms 27.4× slower pi 590.7 ms 369.6–934.8
  ms 42.2× slower Codex CLI 882.8 ms 742.3–1640.9 ms 63.1× slower OpenCode 1035.9
  ms 922.5–1104.4 ms 74.0× slower GitHub Copilot CLI 1518.6 ms 1357.4–1826.8 ms 108.5×
  slower Cursor Agent 1949.7 ms 1711.0–2104.8 ms 139.3× slower Claude Code 3436.9
  ms 2032.7–8927.2 ms 245.5× slower Measured on this Linux machine across 10 interactive
  PTY launches. Time to first input (time until typed probe text appears on the rendered
  screen; Antigravity uses its internal input-ready log marker because the sign-in
  screen suppresses probe echo.) Tool Time to first input Range Comparison jcode 48.7
  ms 30.3–62.7 ms baseline Antigravity CLI 383.7 ms 363.4–415.7 ms 7.9× slower pi
  596.4 ms 373.9–955.2 ms 12.2× slower Codex CLI 905.8 ms 760.1–1675.7 ms 18.6× slower
  OpenCode 1047.9 ms 931.1–1116.9 ms 21.5× slower GitHub Copilot CLI 1583.4 ms 1422.8–1880.0
  ms 32.5× slower Cursor Agent 1978.7 ms 1727.3–2130.0 ms 40.6× slower Claude Code
  3512.8 ms 2137.4–9002.0 ms 72.2× slower Measured on this Linux machine across 10
  interactive PTY launches. Antigravity CLI was unauthenticated for this run; its
  sign-in screen rendered normally and emitted an internal CLI ready for user input
  marker, but did not echo the typed probe. Additional clients / memory scaling Tool
  Extra PSS per added session Comparison jcode (local embedding off) ~9.9 MB baseline
  jcode ~10.4 MB 1.1× more RAM pi ~76.5 MB 7.7× more RAM Codex CLI ~21.6 MB 2.2× more
  RAM OpenCode ~318.4 MB 32.2× more RAM GitHub Copilot CLI ~158.1 MB 16.0× more RAM
  Cursor Agent ~157.5 MB 15.9× more RAM Claude Code ~212.7 MB 21.5× more RAM Antigravity
  CLI ~86.4 MB 8.7× more RAM versions tested for this corrected memory rerun: jcode
  v0.9.1888-dev (be386f2) pi 0.62.0 codex-cli 0.120.0 opencode 1.0.203 GitHub Copilot
  CLI 1.0.24 for the 1-session rerun, GitHub Copilot CLI 1.0.27 for the 10-session
  rerun Cursor Agent 2026.04.08-a41fba1 Claude Code 2.1.86 (Claude Code) Antigravity
  CLI 1.0.0 jcode performance demonstration Memory (Agent memory) Jcode embeds each
  turn/response as a semantic vector. Every turn does queries a graph of memories
  to efficiently find related memory entries via a cosine similarity check. The embedding
  hits are fed into the conversation, or optionally uses a memory sideagent which
  verifies the memories are relevant, and potentially does more work for information
  retreival before injecting into the conversation. This results in a human like memory
  system which allows the agent to automatically recall relevant information to the
  conversation without actively calling memory tools or being a token burner. ot To
  have memories which are retrieved, they must also be extracted and stored. Every
  so often (semantic drift, K turns since last extraction, session end, etc), memories
  are extracted via a memory sideagent, and put into the memory graph. The harness
  also provides explicit memory tools to allow the agent to actively search or store
  the memory without relying on a passive background process. The harness also provides
  session search for traditional RAG on previous sessions. Memories are automatically
  consolidated every so often via the ambient mode. This reorganizes, checks for staleness
  and conflicts, etc jcode memory demonstration UI: Side panels, Diagrams, Info Widgets,
  rendering, scrolling, alignment The side panel is a place for auxiliary information.
  Tell your jcode agent to load a file into the side panel and see it update in real
  time, or tell your agent to write directly to the side panel, or use it as a diff
  viewer. The side panel (and chat) is able to render mermaid diagrams inline. To
  make this possible, I created a new mermaid rendering library to render diagrams
  1800x faster. It has no browser or Typescript dependency. See https://github.com/1jehuang/mermaid-rs-renderer
  To show you important information without taking space away from the screen that
  could be used for responses, I developed info widgets. Info widgets will only ever
  take up the negative space on the screen to show you information, and will get out
  of the way if there isn''t any. Jcode can render at over a thousand fps. Your monitor
  will not have the refresh rate to show you, but this means you will not have silly
  flicker problems. The custom scrollback implementation of jcode allows it to do
  much more than a native scrollback. However, it is a terminal-level limitation that
  I cannot have smooth, partial line scrolling with a custom scrollback. To fix this,
  I made my own terminal. Handterm https://github.com/1jehuang/handterm implements
  a native scroll api, and also happens to be very effiecent. This is a work in progress.
  Scrolling is still well implemented for normal terminals. Jcode is left-aligned
  by default. You can switch to centered mode with the Alt+C hotkey, with the /alignment
  command, or in the config. Swarm Spawn two or more agents in the same repo, and
  they will automatically be managed by the server to allow native collaboration.
  When agent A edits a file that agent B has read (code shifting under its feet),
  the server notifies agent B. Agent B can ignore it if it is not relevant, or it
  can check the diff to make sure that it doesn''t conflict. Each agent has messaging
  abilities, capable of DMing just one agent, broadcasting to all other agents hosted
  by the server, or just agents working in that repo. This allows you to spawn multiple
  sessions in the same repo, and have all conflicts automatically resolved. jcode
  swarm demonstration Agents are also able to spawn their own swarms autonomously.
  They have a swarm tool which allows them to spawn in their own teamates to accomplish
  tasks in parallel. Doing so turns the main agent into a coordinator and the spawned
  agents into workers. Groups of agents, their messaging channels, their completion
  statuses, etc are all automatically managed. This can be done headlessly or headed.
  OAuth and Providers jcode works with subscription-backed OAuth flows and many provider
  integrations, so you can use the models you already pay for and still fall back
  to direct API providers when needed. Supported built-in login flows Claude (jcode
  login --provider claude) OpenAI / ChatGPT / Codex (jcode login --provider openai)
  Google Gemini (jcode login --provider gemini) GitHub Copilot (jcode login --provider
  copilot) Azure OpenAI (jcode login --provider azure) Alibaba Cloud Coding Plan (jcode
  login --provider alibaba-coding-plan) Fireworks (jcode login --provider fireworks)
  MiniMax (jcode login --provider minimax) LM Studio (jcode login --provider lmstudio)
  Ollama (jcode login --provider ollama) Custom OpenAI-compatible endpoint (jcode
  login --provider openai-compatible) For custom OpenAI-compatible endpoints, jcode
  now prompts for the API base and supports local localhost servers without requiring
  an API key. Config-file setup for self-hosted endpoints and MCP If you prefer to
  configure things by editing files instead of using the login UI, jcode supports
  both a custom OpenAI-compatible endpoint config and MCP config files. OpenAI-compatible
  providers Many hosted services speak the standard OpenAI /v1/chat/completions API.
  jcode talks to them through one shared OpenAI-compatible provider, so you can use
  almost any such endpoint without waiting for a dedicated integration. There are
  two ways to set one up: Built-in named profiles — jcode ships ready-made profiles
  for several popular OpenAI-compatible services. Log in by id and jcode fills in
  the base URL and key environment variable for you: jcode login --provider <profile-id>
  # for example: jcode login --provider openrouter jcode login --provider deepseek
  jcode login --provider opencode # OpenCode Zen jcode login --provider moonshotai
  Built-in OpenAI-compatible profile ids include: openrouter, deepseek, zai, kimi,
  moonshotai, opencode (OpenCode Zen), opencode-go, 302ai, baseten, cortecs, huggingface,
  nebius, scaleway, stackit, and firmware. Each profile only sets the endpoint and
  key variable; you still pick the model with /model (or --model). Run jcode login
  with no provider to see the interactive list. Any other endpoint — point jcode at
  an arbitrary OpenAI-compatible API (hosted or local) with jcode login --provider
  openai-compatible or the scriptable jcode provider add command described below.
  Useful environment overrides for these endpoints: JCODE_STREAM_IDLE_TIMEOUT_SECS
  — raise the streaming idle timeout (default 180s) for slow reasoning models that
  think silently before emitting tokens. Also settable as [provider] stream_idle_timeout_secs
  in config.toml. Per-model context_window (alias context_limit) in a [[providers.<name>.models]]
  entry — set the context window when the endpoint has no usable /v1/models response,
  so jcode does not fall back to the generic 200k default. extra_body — inject non-standard
  top-level fields into every chat/completions request body for backends that require
  them. See Extra request-body fields below. For details on self-hosting, local runtimes,
  and the exact config file shape, see below. Self-hosted OpenAI-compatible endpoints,
  including vLLM For agents and scripts, the preferred path is the one-shot provider
  profile command. It writes a named profile to ~/.jcode/config.toml, stores secrets
  in jcode''s private app config directory when requested, and prints exact run/validation
  commands: # Secret-safe setup for a hosted OpenAI-compatible API. printf ''%s''
  "$MY_API_KEY" | jcode provider add my-api \ --base-url https://llm.example.com/v1
  \ --model my-model-id \ --api-key-stdin \ --set-default \ --json # Smoke test the
  profile. jcode --provider-profile my-api auth-test --prompt ''Reply exactly JCODE_PROVIDER_SETUP_OK''
  # Use it directly. jcode --provider-profile my-api run ''hello'' For local servers
  that do not require auth: jcode provider add local-vllm \ --base-url http://localhost:8000/v1
  \ --model Qwen/Qwen3-Coder-30B-A3B-Instruct \ --no-api-key \ --set-default Built-in
  local profiles are available for the common desktop/local runtimes: # Ollama: start
  the local server and install a model first. ollama pull llama3.2 jcode login --provider
  ollama jcode --provider ollama --model llama3.2 run ''hello'' # LM Studio: start
  the Local Server, load a chat model, then use the exact # model identifier shown
  by LM Studio or by curl http://localhost:1234/v1/models. jcode login --provider
  lmstudio jcode --provider lmstudio --model ''<model-id>'' run ''hello'' Ollama and
  LM Studio both expose OpenAI-compatible /v1/models and /v1/chat/completions endpoints.
  jcode uses streaming chat completions, function/tool calling, and OpenAI-style image
  content for vision-capable local models. If a local server requires a token, enter
  it during jcode login or create a named profile with --api-key-stdin. Useful flags:
  --api-key-env NAME: reference an existing environment variable instead of storing
  a key. --api-key-stdin: read and store a key without putting it in shell history.
  --context-window TOKENS: persist the model context window for model selection and
  routing. --overwrite: replace an existing profile of the same name. --model-catalog:
  use the endpoint''s /models response in addition to configured models. The generated
  profile can also be edited manually in ~/.jcode/config.toml: [provider] default_provider
  = "my-api" default_model = "my-model-id" [providers.my-api] type = "openai-compatible"
  base_url = "https://llm.example.com/v1" api_key_env = "JCODE_PROVIDER_MY_API_API_KEY"
  env_file = "provider-my-api.env" default_model = "my-model-id" [[providers.my-api.models]]
  id = "my-model-id" context_window = 128000 Extra request-body fields (extra_body)
  Some OpenAI-compatible backends require non-standard top-level request fields. For
  example, NVIDIA NIM DeepSeek-V4 reasoning models (deepseek-ai/deepseek-v4-flash,
  deepseek-ai/deepseek-v4-pro) only enable thinking when the request includes chat_template_kwargs;
  without it they reply without reasoning (or, for some deployments, hang). jcode
  lets you inject arbitrary top-level fields two ways. Per named profile, via extra_body
  in config.toml (a TOML table merged verbatim into the JSON body): [providers.my-nim]
  type = "openai-compatible" base_url = "https://integrate.api.nvidia.com/v1" api_key_env
  = "NVIDIA_API_KEY" default_model = "deepseek-ai/deepseek-v4-flash" [providers.my-nim.extra_body.chat_template_kwargs]
  thinking = true reasoning_effort = "high" For built-in profiles (e.g. nvidia-nim)
  or any endpoint, via the JCODE_OPENAI_EXTRA_BODY environment variable (a JSON object
  string). It can live in the provider''s env file (~/.config/jcode/nvidia-nim.env)
  next to the API key: JCODE_OPENAI_EXTRA_BODY={"chat_template_kwargs":{"thinking":true,"reasoning_effort":"high"}}
  Keys from extra_body are merged last and override any jcode-generated body field
  with the same name (JCODE_OPENAI_EXTRA_BODY wins over the config extra_body on key
  collisions). Invalid values are logged and ignored rather than failing the request.
  The custom OpenAI-compatible provider reads overrides from environment variables
  or from an env file in jcode''s app config directory. On Linux this is usually ~/.config/jcode/,
  so the default file is usually: ~/.config/jcode/openai-compatible.env Example for
  a local or LAN vLLM server: JCODE_OPENAI_COMPAT_API_BASE=http://192.168.1.50:8000/v1
  JCODE_OPENAI_COMPAT_DEFAULT_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct # Optional if
  your server expects auth OPENAI_COMPAT_API_KEY=your-token-here Notes: jcode login
  --provider openai-compatible can create or update this for you. Plain http:// is
  accepted for localhost and private LAN IPs. Public remote HTTP is still rejected.
  HTTPS endpoints work as usual. MCP config files MCP config is separate from config.toml.
  Primary config files: ~/.jcode/mcp.json for global MCP servers .jcode/mcp.json for
  project-local MCP servers Compatibility fallback: .claude/mcp.json Example MCP config:
  { "servers": { "filesystem": { "command": "/path/to/mcp-server", "args": ["--root",
  "/workspace"], "env": {}, "shared": true } } } On first run, jcode also tries to
  import MCP servers from ~/.claude/mcp.json and ~/.codex/config.toml if ~/.jcode/mcp.json
  does not exist yet. For headless or SSH sessions, OAuth-style providers support
  jcode login --provider <provider> --no-browser (alias: --headless) so jcode prints
  the auth URL/QR and falls back to manual code or callback paste instead of trying
  to launch a local browser. For more scriptable remote flows, claude, openai, gemini,
  and antigravity also support a two-step pattern: # Step 1: print a resumable auth
  URL jcode login --provider openai --print-auth-url --json # Step 2: complete later
  with the callback URL or auth code jcode login --provider openai --callback-url
  ''http://localhost:1455/auth/callback?...'' jcode login --provider gemini --auth-code
  ''...'' Additional scriptable cases: # Copilot device flow: print URL + user code,
  then complete later jcode login --provider copilot --print-auth-url --json jcode
  login --provider copilot --complete # Gmail/Google OAuth after credentials are already
  configured jcode login --provider google --print-auth-url --google-access-tier readonly
  jcode login --provider google --callback-url ''http://127.0.0.1:8456?...'' Pending
  scriptable login state is stored under ~/.jcode/pending-login/, automatically expires,
  and stale entries are cleaned up when new scriptable logins start or resume. For
  the built-in OpenAI login flow, jcode opens a local callback on http://localhost:1455/auth/callback
  by default. The above image is the first page of provider logins Supported provider
  Native / first-party style providers: claude, openai, copilot, gemini, azure, alibaba-coding-plan
  Aggregator / compatibility providers: openrouter, openai-compatible Additional provider
  integrations: opencode, opencode-go, zai / kimi, 302ai, baseten, cortecs, deepseek,
  firmware, huggingface, moonshotai, nebius, scaleway, stackit, groq, mistral, perplexity,
  togetherai, deepinfra, fireworks, minimax, xai, lmstudio, ollama, chutes, cerebras,
  cursor, antigravity, google Jcode also supports easy multi-account switching. Ran
  out of tokens on your first ChatGPT Pro subscription? /account and quickly switch
  to your second. Customizability / Self-Dev Jcode is inventing a new form of customizability.
  One that doesn''t limit you to what a plugin or extension can do. Tell your jcode
  agent to enter self dev mode, and it will start modifying its own source code. Jcode
  is optimized to iterate on itself. There is significant infrastructure around self
  developement, which allows it to edit, build, and test its own source code, then
  reload its own binary and continue work in your (potentially many) sessions, fully
  automatically. It is reccomended that you use a frontier model for this. The jcode
  codebase is not a simple one, and weaker models can make subtle, breaking changes.
  GPT 5.5 or the latest available frontier model works well. Misc. The devil is in
  the details. There are many undocumented optimizations and niceties that jcode implements.
  Some examples: Anthropic''s Claude cache goes cold after 5 minutes. If you initiate
  Claude after these 5 minutes, you have a cache miss, potentially costing you lots
  of tokens. The ui warns you when the cache went cold, and notfies you if there was
  an unexpected cache miss. jcode comes with instructions on how to set up Firefox
  Agent Bridge. Ask you agent to set it up, and then you will have browser automation
  in jcode as well. Agent grep is a grep tool I made for the jcode agent. It adds
  file strucuture information (ie the list of functions, their displacement, etc)
  to the grep return, so that the agent can infer more of what the file doesn without
  actually reading the file. It also implements a harness-level integration that adaptively
  truncates returns based on what the agent has already seen. This saves on context
  a lot. Inputs are by default interleaved with the working agent. It sends the input
  as soon as it safely can without breaking the KV cache. Submit with shift enter
  instead, and it will send a queue send, and wait for the agent to fully finish its
  turn before sending. Resume sessions from different harnesses. Claude code broke
  on you? Resume the session from jcode and continue where you left off. Session resume
  is supported for codex, claude code, opencode, and pi. image of /Resume for codex
  sessions Skills are not all loaded on startup. The conversation is embedded as a
  semantic vector, and will automatically inject a skill if there is an embedding
  hit similar to memories. The agent has a skill tool for you to manually activate
  a skill at anytime. You may also activate via slash commands. iOS Application /
  Native OpenClaw A native iOS application version of jcode is coming soon. This will
  allow you to work with jcode on your personal machine''s environment from your phone,
  via Tailscale. Openclaw like features will be bundled with this iOS application.
  Other planned features Agents dont like to commit in dirty git state with active
  changes. Git was clearly not built for multi-agent workflows, and git worktrees
  is not a good solution. Given this, I believe that is an opporunity for a new git
  like primitive to be born. Build speed improvements: An incremental debug cargo
  build with cache enabled takes about 1 minute on my machine. The goal is 5-20 seconds.
  Refactors and crates seams should be able to make this happen. Quick Start # Launch
  the TUI jcode # Run a single command non-interactively jcode run "say hello" # Resume
  a previous session by memorable name jcode --resume fox # Run as a persistent background
  server, then attach more clients jcode serve jcode connect # Send voice input from
  your configured STT command jcode dictate jcode supports interactive TUI use, non-interactive
  runs, persistent server/client workflows, and hotkey-friendly dictation without
  requiring a bundled speech-to-text stack. jcode workflow demonstration Browser Automation
  jcode includes a first-class built-in browser tool for browser control inside agent
  sessions. Current built-in backend: Firefox via Firefox Agent Bridge Current built-in
  tool actions include: status setup open snapshot get_content interactables click
  type fill_form select wait screenshot eval scroll upload press Quick setup: jcode
  browser status jcode browser setup Once setup is complete, the model can use the
  built-in browser tool directly. The UI also summarizes browser tool calls compactly,
  for example opening a URL, clicking a selector, or typing into a field without echoing
  sensitive typed text. Notes: the provider/tool architecture is in place for additional
  backends Firefox is the wired built-in backend today Chrome bridge / remote debugging
  style providers can be added on top of the same browser tool later Further Reading
  Ambient Mode / OpenClaw Browser Provider Protocol Memory Architecture Swarm Architecture
  Server Architecture iOS Client Notes Safety System Windows Notes Wrappers and Shell
  Integration Refactoring Notes Detailed Installation Setup If you want another agent
  to set up jcode for you, give it this prompt: Set up jcode on this machine for me.
  1. Detect the operating system, available package managers, and shell environment,
  then install jcode using the best matching command below instead of referring me
  somewhere else: - macOS with Homebrew available: brew tap 1jehuang/jcode brew install
  jcode - macOS or Linux via install script: curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh
  | bash - Windows PowerShell: irm https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.ps1
  | iex - From source if the above paths are not appropriate: git clone https://github.com/1jehuang/jcode.git
  cd jcode cargo build --release scripts/install_release.sh - For local self-dev /
  refactor work on Linux x86_64, prefer: scripts/dev_cargo.sh build --release -p jcode
  --bin jcode scripts/dev_cargo.sh --print-setup scripts/install_release.sh 2. Verify
  that `jcode` is on my `PATH`. 3. Launch `jcode` once in a new terminal window/session
  to confirm it starts successfully. 4. Before attempting any interactive login flow,
  assess which providers are already available non-interactively and prefer those
  first. Check existing local credentials, config files, CLI sessions, and environment
  variables such as: - Claude: `~/.jcode/auth.json`, `~/.claude/.credentials.json`,
  `~/.local/share/opencode/auth.json`, `ANTHROPIC_API_KEY` - OpenAI: `~/.jcode/openai-auth.json`,
  `~/.codex/auth.json`, `OPENAI_API_KEY` - Gemini: `~/.jcode/gemini_oauth.json`, `~/.gemini/oauth_creds.json`
  - GitHub Copilot: existing auth under `~/.config/github-copilot/` - Azure OpenAI:
  `~/.config/jcode/azure-openai.env`, `AZURE_OPENAI_*`, or an existing `az login`
  - OpenRouter: `OPENROUTER_API_KEY` - Fireworks: `~/.config/jcode/fireworks.env`,
  `FIREWORKS_API_KEY` - MiniMax: `~/.config/jcode/minimax.env`, `MINIMAX_API_KEY`
  - NVIDIA NIM: `~/.config/jcode/nvidia-nim.env`, `NVIDIA_API_KEY` - Alibaba Cloud
  Coding Plan: existing jcode config/env if present 5. Prefer whichever provider is
  already configured and verify it with `jcode auth-test --all-configured` or a provider-specific
  auth test when appropriate. 6. Only if no usable provider is already configured,
  guide me through the minimal manual step needed: - Claude: `jcode login --provider
  claude` - GitHub Copilot: `jcode login --provider copilot` - OpenAI: `jcode login
  --provider openai` - Gemini: `jcode login --provider gemini` - Azure OpenAI: `jcode
  login --provider azure` - Fireworks: `jcode login --provider fireworks` - MiniMax:
  `jcode login --provider minimax` - NVIDIA NIM: `jcode login --provider nvidia-nim`
  - Alibaba Cloud Coding Plan: `jcode login --provider alibaba-coding-plan` - OpenRouter:
  help me set `OPENROUTER_API_KEY` - Anthropic direct API: help me set `ANTHROPIC_API_KEY`
  7. After setup, run a simple smoke test with `jcode run "say hello"` and confirm
  it works. 8. If I want browser automation, also check `jcode browser status`. If
  browser automation is not ready, run `jcode browser setup`, verify the built-in
  `browser` tool works, and explain any remaining manual step. 9. Explain any manual
  step that still needs me, especially browser OAuth, device login, API key entry,
  or browser extension approval. This is intended to be a copy-paste bootstrap prompt
  for jcode itself or any other coding agent. Quick Install # macOS & Linux curl -fsSL
  https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
  On Termux, install the glibc runtime and patchelf first so the installer can patch
  the downloaded Linux binary to Termux''s glibc dynamic linker and create a launcher
  that avoids Termux''s LD_PRELOAD shim: pkg install glibc patchelf curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh
  | bash # Windows (PowerShell) irm https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.ps1
  | iex macOS via Homebrew brew tap 1jehuang/jcode brew install jcode From Source
  (all platforms) git clone https://github.com/1jehuang/jcode.git cd jcode cargo build
  --release For local self-dev / refactor work on Linux x86_64, prefer: scripts/dev_cargo.sh
  build --release -p jcode --bin jcode scripts/dev_cargo.sh --print-setup That wrapper
  automatically uses sccache when available, prefers a fast working local linker setup
  (clang + lld) instead of assuming every machine''s mold configuration is valid,
  and can print the active linker/cache setup via --print-setup so slow-path builds
  are easier to diagnose. Then symlink to your PATH: scripts/install_release.sh Platform
  Support Platform Status Linux x86_64 / aarch64 Fully supported macOS Apple Silicon
  & Intel Supported Windows x86_64 Supported (native + WSL2) Termux aarch64 / x86_64
  Supported with pkg install glibc patchelf'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 2a7f0fddd2dac162
source_type: community_discussion
tldr: jcode 是一个高性能多会话编码代理框架，启动速度比 Claude Code 快 245 倍
objective_summary: 开发者 1jehuang 发布了开源编码代理框架 jcode，通过自定义终端渲染、语义记忆图谱、多代理协作等架构优化，实现了
  14ms 的首帧渲染时间（Claude Code 为 3437ms）和每会话仅 ~10MB 的内存增量（Claude Code 为 ~213MB），支持
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - GitHub
  - OpenAI
  - Google
  - Microsoft
  - Alibaba Cloud
  - Fireworks
  - MiniMax
  - LM Studio
  - Ollama
  technologies:
  - RAG
  - MCP
  - embedding
  - cosine similarity
  key_people:
  - 1jehuang
key_logic_flow:
- jcode 是一个面向多会话工作流的编码代理框架，核心设计目标是极致的性能和资源效率。
- 性能基准测试显示，jcode 首帧渲染中位时间 14ms，比 Claude Code（3437ms）快约 245 倍，每新增会话仅消耗约 10.4MB 内存，远低于同类工具。
- jcode 实现了基于语义向量嵌入和余弦相似度检索的记忆系统，可自动提取、存储和召回相关会话信息，无需代理主动调用记忆工具。
- jcode 支持多代理协作，同一仓库内的多个代理由服务端统一管理，文件变更时自动通知相关代理，代理间可发送私信或广播消息。
- jcode 集成了 Claude、OpenAI、Gemini、GitHub Copilot、Azure、Ollama、LM Studio 等十余种模型提供商，支持
  OpenAI 兼容端点和自定义配置。
- jcode 包含侧面板、Mermaid 图表渲染（自研 Rust 渲染库，速度提升 1800 倍）、自定义终端 Handterm 等辅助功能。
impact_score:
  score: 7.0
  reason: 这是一个在编码代理领域具有实质性技术突破的开源项目。其性能基准测试（首帧渲染14ms vs Claude Code的3437ms，每会话内存增量~10MB
    vs ~213MB）并非空洞的PR话术，而是附带了详细方法论和10次重复测量的数据。该项目通过自研终端渲染引擎、Rust Mermaid渲染库、语义记忆图谱等多层架构创新实现了数量级的性能提升，这对多会话编码代理工作流有根本性的效率改善。虽然项目仍处于v0.9.1888-dev阶段且来自个人开发者，但其技术路径可能推动整个编码代理工具链（Claude
    Code、Cursor、Codex CLI等）的性能竞赛和架构优化，短期影响力预计在开源社区和工具开发者圈子中较为显著。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: 性能基准测试的真实性和日常使用体验能否复现宣称的245倍加速
hype_assessment:
  level: low
  reason: 文章提供了极其详尽的性能基准测试数据，包括10次重复测量的中位数、范围和对比基线，并明确标注了所有被测工具的版本号和测试环境。项目附带了多项自研组件的独立仓库（Handterm终端、Rust
    Mermaid渲染库），这些组件解决了具体工程问题而非包装概念。整篇README以技术细节和架构说明为主，没有任何'颠覆''革命性'等PR滥用词汇，属于实打实的干货输出。
information_entropy: high
domain_disruption:
  technical_innovation: 多项底层架构创新：自研终端渲染引擎将首帧时间压缩到14ms（通过绕过传统终端模拟器瓶颈直接操作PTY）；基于余弦相似度的语义记忆图谱实现被动式上下文检索，无需代理主动调用记忆工具；自研Rust
    Mermaid渲染库摆脱了浏览器依赖并将渲染速度提升1800倍；多会话服务端统一管理架构支持代理间自动通知和协作。这些创新并非特征堆叠，而是系统性地解决了编码代理在性能、记忆和协作三个维度上的核心瓶颈。
  business_model: 作为MIT开源项目，jcode通过支持十余种模型提供商（Claude、OpenAI、Gemini、GitHub Copilot、Azure、Ollama、LM
    Studio等）和OpenAI兼容端点，打破了编码代理工具与特定模型/云厂商的绑定关系。这可能推动编码代理从封闭商业产品向开放平台架构转型，降低团队采用门槛——用户可以选择本地模型降低成本，或混合使用多家云API提高可靠性和灵活性。
engineering_complexity: prototype
compound_value:
  score: 6.5
  reason: jcode 在编码代理框架层面实现了本质性的架构创新：14ms 首帧渲染（比 Claude Code 快 245 倍）、单会话仅 ~10MB 内存增量（Claude
    Code 的 1/21）、自研 Rust Mermaid 渲染库（速度快 1800 倍）、语义记忆图谱实现类人记忆机制、多代理协作原生支持。这些不是增量优化，而是架构级的重写，构成真实的技术护城河。长期复利潜力在于：如果
    jcode 成为开源编码代理的默认基础设施层（类似 LangChain 在 LLM 编排中的地位），社区贡献将形成网络效应，尤其是其多会话架构和多模型提供商支持使其具备平台化基础。但风险同样显著：当前为个人开发者项目，缺乏组织化维护和商业化路径，需面对
    Cursor、Claude Code、GitHub Copilot 等拥有巨量分发渠道和研发预算的竞品。若能在 12-18 个月内建立活跃社区并找到可持续的商业模式（如企业版、托管服务），则有潜力成为该赛道的基石性基础设施。否则，技术优势若被大厂快速复制，复利效应将大打折扣。
value_capture_layer: agent_middleware
moat_impact: democratizes_access
key_beneficiaries:
- 开发者社区
- 小型 AI 编码工具创业公司
- 模型 API 提供商（OpenAI, Anthropic, Google）
competitive_casualty:
- Claude Code
- Cursor Agent
- GitHub Copilot CLI
- OpenCode
- Codex CLI
market_opportunities:
- 开发者可基于 jcode 的极轻量架构和语义记忆图谱，构建面向企业级多会话工作流的编码协作平台，替代传统的单会话 AI 编码工具
- jcode 的多代理协作机制（服务端统一管理 + 文件变更通知）可直接用于自动化 CI/CD 代码评审和持续重构场景，建议开发配套的企业级编排中间件
- jcode 的自研 Rust Mermaid 渲染库（提速 1800 倍）和 Handterm 终端具备独立商业化潜力，可拆解为通用工具 SDK 服务于其他 AI
  编码产品
risk_matrix:
  regulatory: 开源框架本身无直接监管风险，但若企业将其应用于合规敏感领域（如金融、医疗的自动化代码生成），代理自主编码行为的责任归属尚不明确，需关注后续法律框架演进
  technological: 项目处于 v0.9.x-dev 阶段，单维护者模式，长期稳定性存疑；性能基准由作者自行发布，尚未经第三方独立复现；极致的终端渲染优化可能在不同
    OS/终端模拟器上出现兼容性问题
  competitive: Anthropic（Claude Code）、GitHub（Copilot CLI）、Cursor 等巨头生态和资源碾压，可快速复制核心特性；厂商锁定效应（如
    Claude Code 对 Claude 模型的深度优化）可能削弱 jcode 的多模型优势
  ethical: 代理自动记忆和检索对话历史（语义嵌入 + 余弦相似度）可能无意中泄露敏感代码上下文；多代理自动协作可能放大编码缺陷的传播范围，间接引入安全漏洞
  additional:
  - 单维护者项目风险：若核心开发者失去维护动力，社区分支难以维系架构一致性
  - 终端层创新（Handterm）需要用户安装额外软件，增加摩擦，可能限制早期采用速度
confidence:
  impact: high
  compound: medium
  hype: high
actionable_insight: deep_dive
---

The next generation coding agent harness to raise the skill ceiling.

Built for multi-session workflows, infinite customizability, and performance.

Features · Install · Quick Start · Further Reading · Contributing

```
# macOS & Linux
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

Need Windows, Homebrew, source builds, provider setup, or tell your agent to set it up for you? Jump to detailed installation.

jcode is built to be as performant and resource efficient as possible. Every metric is optimized to the bone, which is important for scaling multi-session workflows. Here we sample a few metrics to show the difference: RAM usage and boot up.

1 active session
|
10 active sessions
|

| Tool | Time to first frame | Range | Comparison |
|---|---|---|---|
jcode |
14.0 ms |
10.1–19.3 ms | baseline |
Antigravity CLI |
383.5 ms |
363.1–415.4 ms | 27.4× slower |
pi |
590.7 ms |
369.6–934.8 ms | 42.2× slower |
Codex CLI |
882.8 ms |
742.3–1640.9 ms | 63.1× slower |
OpenCode |
1035.9 ms |
922.5–1104.4 ms | 74.0× slower |
GitHub Copilot CLI |
1518.6 ms |
1357.4–1826.8 ms | 108.5× slower |
Cursor Agent |
1949.7 ms |
1711.0–2104.8 ms | 139.3× slower |
Claude Code |
3436.9 ms |
2032.7–8927.2 ms | 245.5× slower |

Measured on this Linux machine across 10 interactive PTY launches.

(time until typed probe text appears on the rendered screen; Antigravity uses its internal input-ready log marker because the sign-in screen suppresses probe echo.)

| Tool | Time to first input | Range | Comparison |
|---|---|---|---|
jcode |
48.7 ms |
30.3–62.7 ms | baseline |
Antigravity CLI |
383.7 ms |
363.4–415.7 ms | 7.9× slower |
pi |
596.4 ms |
373.9–955.2 ms | 12.2× slower |
Codex CLI |
905.8 ms |
760.1–1675.7 ms | 18.6× slower |
OpenCode |
1047.9 ms |
931.1–1116.9 ms | 21.5× slower |
GitHub Copilot CLI |
1583.4 ms |
1422.8–1880.0 ms | 32.5× slower |
Cursor Agent |
1978.7 ms |
1727.3–2130.0 ms | 40.6× slower |
Claude Code |
3512.8 ms |
2137.4–9002.0 ms | 72.2× slower |

Measured on this Linux machine across 10 interactive PTY launches. Antigravity CLI was unauthenticated for this run; its sign-in screen rendered normally and emitted an internal `CLI ready for user input`

marker, but did not echo the typed probe.

| Tool | Extra PSS per added session | Comparison |
|---|---|---|
jcode (local embedding off) |
~9.9 MB |
baseline |
jcode |
~10.4 MB |
1.1× more RAM |
pi |
~76.5 MB |
7.7× more RAM |
Codex CLI |
~21.6 MB |
2.2× more RAM |
OpenCode |
~318.4 MB |
32.2× more RAM |
GitHub Copilot CLI |
~158.1 MB |
16.0× more RAM |
Cursor Agent |
~157.5 MB |
15.9× more RAM |
Claude Code |
~212.7 MB |
21.5× more RAM |
Antigravity CLI |
~86.4 MB |
8.7× more RAM |

`jcode v0.9.1888-dev (be386f2)`

`pi 0.62.0`

`codex-cli 0.120.0`

`opencode 1.0.203`

`GitHub Copilot CLI 1.0.24`

for the 1-session rerun,`GitHub Copilot CLI 1.0.27`

for the 10-session rerun`Cursor Agent 2026.04.08-a41fba1`

`Claude Code 2.1.86 (Claude Code)`

`Antigravity CLI 1.0.0`


Jcode embeds each turn/response as a semantic vector. Every turn does queries a graph of memories to efficiently find related memory entries via a cosine similarity check. The embedding hits are fed into the conversation, or optionally uses a memory sideagent which verifies the memories are relevant, and potentially does more work for information retreival before injecting into the conversation. This results in a human like memory system which allows the agent to automatically recall relevant information to the conversation without actively calling memory tools or being a token burner. ot To have memories which are retrieved, they must also be extracted and stored. Every so often (semantic drift, K turns since last extraction, session end, etc), memories are extracted via a memory sideagent, and put into the memory graph.

The harness also provides explicit memory tools to allow the agent to actively search or store the memory without relying on a passive background process. The harness also provides session search for traditional RAG on previous sessions.

Memories are automatically consolidated every so often via the ambient mode. This reorganizes, checks for staleness and conflicts, etc

The side panel is a place for auxiliary information. Tell your jcode agent to load a file into the side panel and see it update in real time, or tell your agent to write directly to the side panel, or use it as a diff viewer. The side panel (and chat) is able to render mermaid diagrams inline.

To make this possible, I created a new mermaid rendering library to render diagrams 1800x faster. It has no browser or Typescript dependency. See https://github.com/1jehuang/mermaid-rs-renderer

To show you important information without taking space away from the screen that could be used for responses, I developed info widgets. Info widgets will only ever take up the negative space on the screen to show you information, and will get out of the way if there isn't any.

Jcode can render at over a thousand fps. Your monitor will not have the refresh rate to show you, but this means you will not have silly flicker problems.

The custom scrollback implementation of jcode allows it to do much more than a native scrollback. However, it is a terminal-level limitation that I cannot have smooth, partial line scrolling with a custom scrollback. To fix this, I made my own terminal. Handterm https://github.com/1jehuang/handterm implements a native scroll api, and also happens to be very effiecent. This is a work in progress. Scrolling is still well implemented for normal terminals.

Jcode is left-aligned by default. You can switch to centered mode with the `Alt+C`

hotkey, with the `/alignment`

command, or in the config.

Spawn two or more agents in the same repo, and they will automatically be managed by the server to allow native collaboration. When agent A edits a file that agent B has read (code shifting under its feet), the server notifies agent B. Agent B can ignore it if it is not relevant, or it can check the diff to make sure that it doesn't conflict. Each agent has messaging abilities, capable of DMing just one agent, broadcasting to all other agents hosted by the server, or just agents working in that repo. This allows you to spawn multiple sessions in the same repo, and have all conflicts automatically resolved.

Agents are also able to spawn their own swarms autonomously. They have a swarm tool which allows them to spawn in their own teamates to accomplish tasks in parallel. Doing so turns the main agent into a coordinator and the spawned agents into workers. Groups of agents, their messaging channels, their completion statuses, etc are all automatically managed. This can be done headlessly or headed.

jcode works with subscription-backed OAuth flows and many provider integrations, so you can use the models you already pay for and still fall back to direct API providers when needed.

**Claude**(`jcode login --provider claude`

)**OpenAI / ChatGPT / Codex**(`jcode login --provider openai`

)**Google Gemini**(`jcode login --provider gemini`

)**GitHub Copilot**(`jcode login --provider copilot`

)**Azure OpenAI**(`jcode login --provider azure`

)**Alibaba Cloud Coding Plan**(`jcode login --provider alibaba-coding-plan`

)**Fireworks**(`jcode login --provider fireworks`

)**MiniMax**(`jcode login --provider minimax`

)**LM Studio**(`jcode login --provider lmstudio`

)**Ollama**(`jcode login --provider ollama`

)**Custom OpenAI-compatible endpoint**(`jcode login --provider openai-compatible`

)

For custom OpenAI-compatible endpoints, jcode now prompts for the API base and supports local localhost servers without requiring an API key.

If you prefer to configure things by editing files instead of using the login UI, jcode supports both a custom OpenAI-compatible endpoint config and MCP config files.

Many hosted services speak the standard OpenAI `/v1/chat/completions`

API. jcode talks to them through one shared OpenAI-compatible provider, so you can use almost any such endpoint without waiting for a dedicated integration.

There are two ways to set one up:

-
**Built-in named profiles**— jcode ships ready-made profiles for several popular OpenAI-compatible services. Log in by id and jcode fills in the base URL and key environment variable for you:jcode login --provider <profile-id> # for example: jcode login --provider openrouter jcode login --provider deepseek jcode login --provider opencode # OpenCode Zen jcode login --provider moonshotai

Built-in OpenAI-compatible profile ids include:

`openrouter`

,`deepseek`

,`zai`

,`kimi`

,`moonshotai`

,`opencode`

(OpenCode Zen),`opencode-go`

,`302ai`

,`baseten`

,`cortecs`

,`huggingface`

,`nebius`

,`scaleway`

,`stackit`

, and`firmware`

. Each profile only sets the endpoint and key variable; you still pick the model with`/model`

(or`--model`

). Run`jcode login`

with no provider to see the interactive list. -
**Any other endpoint**— point jcode at an arbitrary OpenAI-compatible API (hosted or local) with`jcode login --provider openai-compatible`

or the scriptable`jcode provider add`

command described below.

Useful environment overrides for these endpoints:

`JCODE_STREAM_IDLE_TIMEOUT_SECS`

— raise the streaming idle timeout (default 180s) for slow reasoning models that think silently before emitting tokens. Also settable as`[provider] stream_idle_timeout_secs`

in`config.toml`

.- Per-model
`context_window`

(alias`context_limit`

) in a`[[providers.<name>.models]]`

entry — set the context window when the endpoint has no usable`/v1/models`

response, so jcode does not fall back to the generic 200k default. `extra_body`

— inject non-standard top-level fields into every chat/completions request body for backends that require them. See Extra request-body fields below.

For details on self-hosting, local runtimes, and the exact config file shape, see below.

For agents and scripts, the preferred path is the one-shot provider profile command. It writes a named profile to `~/.jcode/config.toml`

, stores secrets in jcode's private app config directory when requested, and prints exact run/validation commands:

```
# Secret-safe setup for a hosted OpenAI-compatible API.
printf '%s' "$MY_API_KEY" | jcode provider add my-api \
--base-url https://llm.example.com/v1 \
--model my-model-id \
--api-key-stdin \
--set-default \
--json
# Smoke test the profile.
jcode --provider-profile my-api auth-test --prompt 'Reply exactly JCODE_PROVIDER_SETUP_OK'
# Use it directly.
jcode --provider-profile my-api run 'hello'
```

For local servers that do not require auth:

```
jcode provider add local-vllm \
--base-url http://localhost:8000/v1 \
--model Qwen/Qwen3-Coder-30B-A3B-Instruct \
--no-api-key \
--set-default
```

Built-in local profiles are available for the common desktop/local runtimes:

```
# Ollama: start the local server and install a model first.
ollama pull llama3.2
jcode login --provider ollama
jcode --provider ollama --model llama3.2 run 'hello'
# LM Studio: start the Local Server, load a chat model, then use the exact
# model identifier shown by LM Studio or by curl http://localhost:1234/v1/models.
jcode login --provider lmstudio
jcode --provider lmstudio --model '<model-id>' run 'hello'
```

Ollama and LM Studio both expose OpenAI-compatible `/v1/models`

and `/v1/chat/completions`

endpoints. jcode uses streaming chat completions, function/tool calling, and OpenAI-style image content for vision-capable local models. If a local server requires a token, enter it during `jcode login`

or create a named profile with `--api-key-stdin`

.

Useful flags:

`--api-key-env NAME`

: reference an existing environment variable instead of storing a key.`--api-key-stdin`

: read and store a key without putting it in shell history.`--context-window TOKENS`

: persist the model context window for model selection and routing.`--overwrite`

: replace an existing profile of the same name.`--model-catalog`

: use the endpoint's`/models`

response in addition to configured models.

The generated profile can also be edited manually in `~/.jcode/config.toml`

:

```
[provider]
default_provider = "my-api"
default_model = "my-model-id"
[providers.my-api]
type = "openai-compatible"
base_url = "https://llm.example.com/v1"
api_key_env = "JCODE_PROVIDER_MY_API_API_KEY"
env_file = "provider-my-api.env"
default_model = "my-model-id"
[[providers.my-api.models]]
id = "my-model-id"
context_window = 128000
```

Some OpenAI-compatible backends require non-standard top-level request fields. For example, NVIDIA NIM DeepSeek-V4 reasoning models (`deepseek-ai/deepseek-v4-flash`

, `deepseek-ai/deepseek-v4-pro`

) only enable thinking when the request includes `chat_template_kwargs`

; without it they reply without reasoning (or, for some deployments, hang). jcode lets you inject arbitrary top-level fields two ways.

-
Per named profile, via

`extra_body`

in`config.toml`

(a TOML table merged verbatim into the JSON body):[providers.my-nim] type = "openai-compatible" base_url = "https://integrate.api.nvidia.com/v1" api_key_env = "NVIDIA_API_KEY" default_model = "deepseek-ai/deepseek-v4-flash" [providers.my-nim.extra_body.chat_template_kwargs] thinking = true reasoning_effort = "high"

-
For built-in profiles (e.g.

`nvidia-nim`

) or any endpoint, via the`JCODE_OPENAI_EXTRA_BODY`

environment variable (a JSON object string). It can live in the provider's env file (`~/.config/jcode/nvidia-nim.env`

) next to the API key:JCODE_OPENAI_EXTRA_BODY={"chat_template_kwargs":{"thinking":true,"reasoning_effort":"high"}}


Keys from `extra_body`

are merged last and override any jcode-generated body field with the same name (`JCODE_OPENAI_EXTRA_BODY`

wins over the config `extra_body`

on key collisions). Invalid values are logged and ignored rather than failing the request.

The custom OpenAI-compatible provider reads overrides from environment variables or from an env file in jcode's app config directory. On Linux this is usually `~/.config/jcode/`

, so the default file is usually:

```
~/.config/jcode/openai-compatible.env
```


Example for a local or LAN vLLM server:

```
JCODE_OPENAI_COMPAT_API_BASE=http://192.168.1.50:8000/v1
JCODE_OPENAI_COMPAT_DEFAULT_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct
# Optional if your server expects auth
OPENAI_COMPAT_API_KEY=your-token-here
```

Notes:

`jcode login --provider openai-compatible`

can create or update this for you.- Plain
`http://`

is accepted for`localhost`

and private LAN IPs. Public remote HTTP is still rejected. - HTTPS endpoints work as usual.

MCP config is separate from `config.toml`

.

Primary config files:

`~/.jcode/mcp.json`

for global MCP servers`.jcode/mcp.json`

for project-local MCP servers

Compatibility fallback:

`.claude/mcp.json`


Example MCP config:

```
{
"servers": {
"filesystem": {
"command": "/path/to/mcp-server",
"args": ["--root", "/workspace"],
"env": {},
"shared": true
}
}
}
```

On first run, jcode also tries to import MCP servers from `~/.claude/mcp.json`

and `~/.codex/config.toml`

if `~/.jcode/mcp.json`

does not exist yet.

For headless or SSH sessions, OAuth-style providers support `jcode login --provider <provider> --no-browser`

(alias: `--headless`

) so jcode prints the auth URL/QR and falls back to manual code or callback paste instead of trying to launch a local browser.

For more scriptable remote flows, `claude`

, `openai`

, `gemini`

, and `antigravity`

also support a two-step pattern:

```
# Step 1: print a resumable auth URL
jcode login --provider openai --print-auth-url --json
# Step 2: complete later with the callback URL or auth code
jcode login --provider openai --callback-url 'http://localhost:1455/auth/callback?...'
jcode login --provider gemini --auth-code '...'
```

Additional scriptable cases:

```
# Copilot device flow: print URL + user code, then complete later
jcode login --provider copilot --print-auth-url --json
jcode login --provider copilot --complete
# Gmail/Google OAuth after credentials are already configured
jcode login --provider google --print-auth-url --google-access-tier readonly
jcode login --provider google --callback-url 'http://127.0.0.1:8456?...'
```

Pending scriptable login state is stored under `~/.jcode/pending-login/`

, automatically expires, and stale entries are cleaned up when new scriptable logins start or resume.

For the built-in OpenAI login flow, jcode opens a local callback on
`http://localhost:1455/auth/callback`

by default.

**Native / first-party style providers:**`claude`

,`openai`

,`copilot`

,`gemini`

,`azure`

,`alibaba-coding-plan`

**Aggregator / compatibility providers:**`openrouter`

,`openai-compatible`

**Additional provider integrations:**`opencode`

,`opencode-go`

,`zai`

/`kimi`

,`302ai`

,`baseten`

,`cortecs`

,`deepseek`

,`firmware`

,`huggingface`

,`moonshotai`

,`nebius`

,`scaleway`

,`stackit`

,`groq`

,`mistral`

,`perplexity`

,`togetherai`

,`deepinfra`

,`fireworks`

,`minimax`

,`xai`

,`lmstudio`

,`ollama`

,`chutes`

,`cerebras`

,`cursor`

,`antigravity`

,`google`


Jcode also supports easy multi-account switching. Ran out of tokens on your first ChatGPT Pro subscription? /account and quickly switch to your second.

Jcode is inventing a new form of customizability. One that doesn't limit you to what a plugin or extension can do. Tell your jcode agent to enter self dev mode, and it will start modifying its own source code. Jcode is optimized to iterate on itself. There is significant infrastructure around self developement, which allows it to edit, build, and test its own source code, then reload its own binary and continue work in your (potentially many) sessions, fully automatically.

It is reccomended that you use a frontier model for this. The jcode codebase is not a simple one, and weaker models can make subtle, breaking changes. GPT 5.5 or the latest available frontier model works well.

The devil is in the details. There are many undocumented optimizations and niceties that jcode implements. Some examples:

Anthropic's Claude cache goes cold after 5 minutes. If you initiate Claude after these 5 minutes, you have a cache miss, potentially costing you lots of tokens. The ui warns you when the cache went cold, and notfies you if there was an unexpected cache miss.

jcode comes with instructions on how to set up Firefox Agent Bridge. Ask you agent to set it up, and then you will have browser automation in jcode as well.

Agent grep is a grep tool I made for the jcode agent. It adds file strucuture information (ie the list of functions, their displacement, etc) to the grep return, so that the agent can infer more of what the file doesn without actually reading the file. It also implements a harness-level integration that adaptively truncates returns based on what the agent has already seen. This saves on context a lot.

Inputs are by default interleaved with the working agent. It sends the input as soon as it safely can without breaking the KV cache. Submit with shift enter instead, and it will send a queue send, and wait for the agent to fully finish its turn before sending.

Resume sessions from different harnesses. Claude code broke on you? Resume the session from jcode and continue where you left off. Session resume is supported for codex, claude code, opencode, and pi.

image of /Resume for codex sessionsSkills are not all loaded on startup. The conversation is embedded as a semantic vector, and will automatically inject a skill if there is an embedding hit similar to memories. The agent has a skill tool for you to manually activate a skill at anytime. You may also activate via slash commands.

A native iOS application version of jcode is coming soon. This will allow you to work with jcode on your personal machine's environment from your phone, via Tailscale. Openclaw like features will be bundled with this iOS application.

Agents dont like to commit in dirty git state with active changes. Git was clearly not built for multi-agent workflows, and git worktrees is not a good solution. Given this, I believe that is an opporunity for a new git like primitive to be born.

Build speed improvements: An incremental debug cargo build with cache enabled takes about 1 minute on my machine. The goal is 5-20 seconds. Refactors and crates seams should be able to make this happen.

```
# Launch the TUI
jcode
# Run a single command non-interactively
jcode run "say hello"
# Resume a previous session by memorable name
jcode --resume fox
# Run as a persistent background server, then attach more clients
jcode serve
jcode connect
# Send voice input from your configured STT command
jcode dictate
```

jcode supports interactive TUI use, non-interactive runs, persistent server/client workflows, and hotkey-friendly dictation without requiring a bundled speech-to-text stack.

jcode includes a first-class built-in `browser`

tool for browser control inside agent sessions.

Current built-in backend:

- Firefox via Firefox Agent Bridge

Current built-in tool actions include:

`status`

`setup`

`open`

`snapshot`

`get_content`

`interactables`

`click`

`type`

`fill_form`

`select`

`wait`

`screenshot`

`eval`

`scroll`

`upload`

`press`


Quick setup:

```
jcode browser status
jcode browser setup
```

Once setup is complete, the model can use the built-in `browser`

tool directly. The UI also summarizes browser tool calls compactly, for example opening a URL, clicking a selector, or typing into a field without echoing sensitive typed text.

Notes:

- the provider/tool architecture is in place for additional backends
- Firefox is the wired built-in backend today
- Chrome bridge / remote debugging style providers can be added on top of the same browser tool later

- Ambient Mode / OpenClaw
- Browser Provider Protocol
- Memory Architecture
- Swarm Architecture
- Server Architecture
- iOS Client Notes
- Safety System
- Windows Notes
- Wrappers and Shell Integration
- Refactoring Notes

If you want another agent to set up jcode for you, give it this prompt:

```
Set up jcode on this machine for me.
1. Detect the operating system, available package managers, and shell environment, then install jcode using the best matching command below instead of referring me somewhere else:
- macOS with Homebrew available:
brew tap 1jehuang/jcode
brew install jcode
- macOS or Linux via install script:
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
- Windows PowerShell:
irm https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.ps1 | iex
- From source if the above paths are not appropriate:
git clone https://github.com/1jehuang/jcode.git
cd jcode
cargo build --release
scripts/install_release.sh
- For local self-dev / refactor work on Linux x86_64, prefer:
scripts/dev_cargo.sh build --release -p jcode --bin jcode
scripts/dev_cargo.sh --print-setup
scripts/install_release.sh
2. Verify that `jcode` is on my `PATH`.
3. Launch `jcode` once in a new terminal window/session to confirm it starts successfully.
4. Before attempting any interactive login flow, assess which providers are already available non-interactively and prefer those first. Check existing local credentials, config files, CLI sessions, and environment variables such as:
- Claude: `~/.jcode/auth.json`, `~/.claude/.credentials.json`, `~/.local/share/opencode/auth.json`, `ANTHROPIC_API_KEY`
- OpenAI: `~/.jcode/openai-auth.json`, `~/.codex/auth.json`, `OPENAI_API_KEY`
- Gemini: `~/.jcode/gemini_oauth.json`, `~/.gemini/oauth_creds.json`
- GitHub Copilot: existing auth under `~/.config/github-copilot/`
- Azure OpenAI: `~/.config/jcode/azure-openai.env`, `AZURE_OPENAI_*`, or an existing `az login`
- OpenRouter: `OPENROUTER_API_KEY`
- Fireworks: `~/.config/jcode/fireworks.env`, `FIREWORKS_API_KEY`
- MiniMax: `~/.config/jcode/minimax.env`, `MINIMAX_API_KEY`
- NVIDIA NIM: `~/.config/jcode/nvidia-nim.env`, `NVIDIA_API_KEY`
- Alibaba Cloud Coding Plan: existing jcode config/env if present
5. Prefer whichever provider is already configured and verify it with `jcode auth-test --all-configured` or a provider-specific auth test when appropriate.
6. Only if no usable provider is already configured, guide me through the minimal manual step needed:
- Claude: `jcode login --provider claude`
- GitHub Copilot: `jcode login --provider copilot`
- OpenAI: `jcode login --provider openai`
- Gemini: `jcode login --provider gemini`
- Azure OpenAI: `jcode login --provider azure`
- Fireworks: `jcode login --provider fireworks`
- MiniMax: `jcode login --provider minimax`
- NVIDIA NIM: `jcode login --provider nvidia-nim`
- Alibaba Cloud Coding Plan: `jcode login --provider alibaba-coding-plan`
- OpenRouter: help me set `OPENROUTER_API_KEY`
- Anthropic direct API: help me set `ANTHROPIC_API_KEY`
7. After setup, run a simple smoke test with `jcode run "say hello"` and confirm it works.
8. If I want browser automation, also check `jcode browser status`. If browser automation is not ready, run `jcode browser setup`, verify the built-in `browser` tool works, and explain any remaining manual step.
9. Explain any manual step that still needs me, especially browser OAuth, device login, API key entry, or browser extension approval.
```


This is intended to be a copy-paste bootstrap prompt for jcode itself or any other coding agent.

```
# macOS & Linux
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

On Termux, install the glibc runtime and `patchelf`

first so the installer can
patch the downloaded Linux binary to Termux's glibc dynamic linker and create a
launcher that avoids Termux's `LD_PRELOAD`

shim:

```
pkg install glibc patchelf
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

```
# Windows (PowerShell)
irm https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.ps1 | iex
```

```
brew tap 1jehuang/jcode
brew install jcode
```

```
git clone https://github.com/1jehuang/jcode.git
cd jcode
cargo build --release
```

For local self-dev / refactor work on Linux x86_64, prefer:

```
scripts/dev_cargo.sh build --release -p jcode --bin jcode
scripts/dev_cargo.sh --print-setup
```

That wrapper automatically uses `sccache`

when available, prefers a fast
working local linker setup (`clang + lld`

) instead of assuming every machine's
`mold`

configuration is valid, and can print the active linker/cache setup via
`--print-setup`

so slow-path builds are easier to diagnose.

Then symlink to your PATH:

`scripts/install_release.sh`

| Platform | Status |
|---|---|
Linux x86_64 / aarch64 |
Fully supported |
macOS Apple Silicon & Intel |
Supported |
Windows x86_64 |
Supported (native + WSL2) |
Termux aarch64 / x86_64 |
Supported with `pkg install glibc patchelf` |