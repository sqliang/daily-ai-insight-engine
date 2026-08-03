---
title: anthropics/skills
source: https://github.com/anthropics/skills
author: []
published: ''
created: '2026-06-01'
description: 'Public repository for Agent Skills Note: This repository contains Anthropic''s
  implementation of skills for Claude. For information about the Agent Skills standard,
  see agentskills.io. Skills Skills are folders of instructions, scripts, and resources
  that Claude loads dynamically to improve performance on specialized tasks. Skills
  teach Claude how to complete specific tasks in a repeatable way, whether that''s
  creating documents with your company''s brand guidelines, analyzing data using your
  organization''s specific workflows, or automating personal tasks. For more information,
  check out: What are skills? Using skills in Claude How to create custom skills Equipping
  agents for the real world with Agent Skills About This Repository This repository
  contains skills that demonstrate what''s possible with Claude''s skills system.
  These skills range from creative applications (art, music, design) to technical
  tasks (testing web apps, MCP server generation) to enterprise workflows (communications,
  branding, etc.). Each skill is self-contained in its own folder with a SKILL.md
  file containing the instructions and metadata that Claude uses. Browse through these
  skills to get inspiration for your own skills or to understand different patterns
  and approaches. Many skills in this repo are open source (Apache 2.0). We''ve also
  included the document creation & editing skills that power Claude''s document capabilities
  under the hood in the skills/docx, skills/pdf, skills/pptx, and skills/xlsx subfolders.
  These are source-available, not open source, but we wanted to share these with developers
  as a reference for more complex skills that are actively used in a production AI
  application. Disclaimer These skills are provided for demonstration and educational
  purposes only. While some of these capabilities may be available in Claude, the
  implementations and behaviors you receive from Claude may differ from what is shown
  in these skills. These skills are meant to illustrate patterns and possibilities.
  Always test skills thoroughly in your own environment before relying on them for
  critical tasks. Skill Sets ./skills: Skill examples for Creative & Design, Development
  & Technical, Enterprise & Communication, and Document Skills ./spec: The Agent Skills
  specification ./template: Skill template Try in Claude Code, Claude.ai, and the
  API Claude Code You can register this repository as a Claude Code Plugin marketplace
  by running the following command in Claude Code: /plugin marketplace add anthropics/skills
  Then, to install a specific set of skills: Select Browse and install plugins Select
  anthropic-agent-skills Select document-skills or example-skills Select Install now
  Alternatively, directly install either Plugin via: /plugin install document-skills@anthropic-agent-skills
  /plugin install example-skills@anthropic-agent-skills After installing the plugin,
  you can use the skill by just mentioning it. For instance, if you install the document-skills
  plugin from the marketplace, you can ask Claude Code to do something like: "Use
  the PDF skill to extract the form fields from path/to/some-file.pdf" Claude.ai These
  example skills are all already available to paid plans in Claude.ai. To use any
  skill from this repository or upload custom skills, follow the instructions in Using
  skills in Claude. Claude API You can use Anthropic''s pre-built skills, and upload
  custom skills, via the Claude API. See the Skills API Quickstart for more. Creating
  a Basic Skill Skills are simple to create - just a folder with a SKILL.md file containing
  YAML frontmatter and instructions. You can use the template-skill in this repository
  as a starting point: --- name: my-skill-name description: A clear description of
  what this skill does and when to use it --- # My Skill Name [Add your instructions
  here that Claude will follow when this skill is active] ## Examples - Example usage
  1 - Example usage 2 ## Guidelines - Guideline 1 - Guideline 2 The frontmatter requires
  only two fields: name - A unique identifier for your skill (lowercase, hyphens for
  spaces) description - A complete description of what the skill does and when to
  use it The markdown content below contains the instructions, examples, and guidelines
  that Claude will follow. For more details, see How to create custom skills. Partner
  Skills Skills are a great way to teach Claude how to get better at using specific
  pieces of software. As we see awesome example skills from partners, we may highlight
  some of them here: Notion - Notion Skills for Claude'
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: 82a901da1b9bedec
source_type: community_discussion
tldr: Anthropic 开源了 skills 仓库，包含 Claude 技能实现集合（SKILL.md 指令文件加附属资源），覆盖创意设计、开发技术、企业通信和文档处理四大类别，支持通过
  Claude Code Plugin 市场安装或通过 API 上传自定义技能。
objective_summary: Anthropic 在 GitHub 上发布了 anthropics/skills 开源仓库，该仓库是 Claude 技能系统的官方实现集合。仓库包含
  Agent Skills 规范（./spec）、技能模板（./template）以及四大类示例技能：创意设计、开发技术、企业通信和文档处理。用户可通过 Claude
  Code 的 /plugin marketplace add 或 /plugin install 命令安装文档技能和示例技能两个插件，也可通过 Claude API
  上传自定义技能。大部分技能以 Apache 2.0 开源协议发布，文档技能（docx/pdf/pptx/xlsx）以 source-available 许可提供。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  technologies:
  - Agent Skills
  - Claude Code Plugin
  key_people: []
key_logic_flow:
- Anthropic 在 GitHub 上发布了 anthropics/skills 开源仓库，该仓库包含 Claude 技能系统的完整实现和示例集合，并定义了
  Agent Skills 规范。
- Skills 是以 SKILL.md 指令文件为核心的文件夹结构，包含 YAML 前端元数据和 Markdown 指令，用于指导 Claude 以可重复的方式完成特定领域的专业任务。
- 仓库中的示例技能覆盖创意设计、开发技术、企业通信和文档处理四大类别，大部分以 Apache 2.0 开源协议发布。
- 文档处理技能（docx、pdf、pptx、xlsx）以 source-available 许可提供，它们是驱动 Claude 文档能力底层的生产级实现。
- 用户可通过 Claude Code 的 /plugin marketplace add 或 /plugin install 命令安装文档技能和示例技能两个插件，也可通过
  Claude API 上传自定义技能。
- 创建自定义技能只需创建一个包含 name 和 description 字段的 SKILL.md 文件，使用仓库中的 template-skill 作为起始模板即可快速上手。
extract_result: success
object_mentions:
- object_type: project
  name: anthropics/skills
  canonical_name: anthropics/skills
  url: https://github.com/anthropics/skills
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - 该仓库是 Anthropic 在 GitHub 上发布的 Claude 技能官方实现，包含 SKILL.md 指令文件、Agent Skills 规范和技能模板。
  - 仓库中的示例技能覆盖创意设计、开发技术、企业通信和文档处理四大类别，大部分以 Apache 2.0 开源协议发布。
  - 用户可通过 Claude Code 的 /plugin marketplace add anthropics/skills 命令将本仓库注册为插件市场。
  article_id: 82a901da1b9bedec
- object_type: project
  name: Agent Skills
  canonical_name: Agent Skills
  url: https://agentskills.io
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - Agent Skills 是定义 Claude 技能加载和行为的标准规范，其规范文档位于该仓库的 ./spec 子目录中。
  - 关于 Agent Skills 标准的更多信息可在 agentskills.io 网站上查阅。
  article_id: 82a901da1b9bedec
- object_type: product
  name: document-skills
  canonical_name: document-skills
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 文档技能插件包含驱动 Claude 文档处理能力的 docx、pdf、pptx 和 xlsx 子技能，采用 source-available 许可。
  - 用户可通过 /plugin install document-skills@anthropic-agent-skills 命令在 Claude Code 中安装文档技能插件。
  article_id: 82a901da1b9bedec
- object_type: product
  name: example-skills
  canonical_name: example-skills
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 示例技能插件包含仓库中创意、开发和企业通信等类别的所有示例技能，可供学习和参考。
  - 用户可通过 /plugin install example-skills@anthropic-agent-skills 命令安装示例技能插件。
  article_id: 82a901da1b9bedec
- object_type: project
  name: template-skill
  canonical_name: template-skill
  url: null
  confidence: medium
  article_role: mentioned_reference
  evidence_snippets:
  - 模板技能是创建自定义技能的起始模板，只需填充 name 和 description 字段以及 Markdown 指令即可完成定义。
  - 模板技能位于仓库的 ./template 子目录中，展示了 SKILL.md 文件的最小必需结构和编写规范。
  article_id: 82a901da1b9bedec
impact_score:
  score: 7.0
  reason: Anthropic 开源 Skills 仓库是 AI Agent 生态建设的关键一步。它定义了一套标准化的技能描述规范（SKILL.md + YAML
    frontmatter），并提供了从创意设计到企业文档处理的全套可运行示例。更重要的是，文档技能（docx/pdf/pptx/xlsx）以源码可用形式发布，展示了生产级
    Agent 技能的工程实现方式。这虽然不是 GPT-3 级别的范式转移，但可能催生类似 VS Code 插件生态的 Claude 技能生态，改变 AI Agent
    定制化和可扩展性的竞争格局。短期冲击力较高，因为开发者可以立即通过 Claude Code 插件市场安装使用。
sentiment: positive
developer_sentiment:
  tone: excited
  primary_focus: Agent Skills 标准化规范和可自定义的技能模板，以及如何通过插件市场分发技能
hype_assessment:
  level: low
  reason: Anthropic 没有使用'颠覆性'、'革命性'等夸张 PR 词汇，而是提供了完整的仓库、规范文档、示例代码和安装指南。仓库明确标注'这些技能仅供演示和教育目的'，并提示生产环境需自行充分测试，态度务实。Apache
    2.0 开源协议和 agentskills.io 标准规范进一步增强了可信度。
information_entropy: high
domain_disruption:
  technical_innovation: 定义了 Agent Skills 标准化规范（agentskills.io），以 SKILL.md + YAML frontmatter
    作为技能描述元格式，支持动态加载和运行时注入。文档技能以源码形式揭示了生产级 AI 应用（Claude 文档能力）的底层实现架构，包括 docx/pdf/pptx/xlsx
    等复杂格式的处理模式。
  business_model: 可能催生围绕 Claude 的技能插件市场生态，类似 Slack App Directory 或 VS Code Marketplace
    的分发与变现模式。Anthropic 通过标准化规范锁定平台网络效应，第三方开发者可创建和分发专有技能，企业可构建内部技能库，形成多层次的商业模式闭环。
engineering_complexity: production_ready
compound_value:
  score: 8.5
  reason: Anthropic 开源 Skills 是一次典型的'标准即护城河'战略布局。从 VC 视角看，其复利价值体现在三层递进逻辑：第一层，通过 agentskills.io
    标准化规范和 Apache 2.0 开源许可证，Anthropic 试图建立 AI Agent 技能的事实标准——这与 MCP 协议形成互补（MCP 管工具接入，Skills
    管任务编排），一旦开发者社区习惯用 SKILL.md + YAML frontmatter 定义技能，迁移成本会指数级上升。第二层，技能市场的网络效应：技能越多→Claude
    越强大→用户越多→更多开发者来建技能，这是一个典型的双边平台飞轮，与 OpenAI 封闭的 GPTs 商店形成直接竞争。第三层，文档技能（docx/pdf/pptx/xlsx）以源码可用形式开源，说明
    Anthropic 有意让企业级用户信任其底层实现，同时保留商业控制权，这是企业级变现的关键入口。风险点：标准仍在早期，需要观察开发者 adoption rate
    和与 MCP 生态的融合程度；如果 OpenAI 也推出类似的开放技能标准，可能会分化生态。综合评分 8.5：3-5 年后 Skill 生态大概率是 Claude
    平台的核心壁垒。
value_capture_layer: agent_middleware
moat_impact: creates_new_moat
key_beneficiaries:
- Anthropic
- 开发者社区（Skill 创作者）
- Notion
- Claude Code 用户
competitive_casualty:
- OpenAI（GPTs 封闭生态）
- LangChain（Agent 编排层被替代风险）
- 传统 RPA/宏工具厂商
market_opportunities:
- 企业和咨询公司可围绕 Agent Skills 标准提供定制化技能开发服务，帮助组织将品牌规范、合规流程、数据分析等工作流封装为可复用的 Claude 技能，抢占企业级
  AI 定制化落地的蓝海市场
- 开发者可基于开源技能模板构建垂直行业技能包（如法律文书处理、医疗记录分析、金融报告生成），通过 Claude Code 插件市场分发，形成技能即服务（Skills-as-a-Service）的新型
  SaaS 商业模式
- MCP 服务器生成技能和文档处理技能降低了 AI Agent 开发门槛，技术团队可借此快速构建内部自动化工具链，从文档生成到代码审查全链路提效
risk_matrix:
  regulatory: 技能生成的文档和通信内容可能涉及行业合规要求（如金融报告需符合 SEC 规定、医疗文档需遵循 HIPAA），技能创建者需自行确保输出合规；仓库中文档技能仅以源码可用形式提供而非完全开源，存在许可证理解和合规混淆的风险
  technological: Skills 系统深度绑定 Claude/Anthropic 生态，存在供应商锁定风险；OpenAI 的 GPTs 和 Google
    的定制 Agent 是直接竞争方案，若生态未能形成网络效应，当前技能模式可能被快速替代
  competitive: OpenAI 已通过 GPTs 和自定义 Actions 建立了类似生态，开发者技能创作的注意力竞争激烈；大型云厂商可凭借平台优势提供更深度集成的
    Agent 自定义方案，挤压独立技能生态的生存空间
  ethical: 技能可被滥用于大规模生成深度伪造文档、误导性企业通信或钓鱼内容；技能质量参差不齐，嵌入创作者偏见的技能可能被不加审查地广泛使用，放大算法偏见风险
  additional:
  - 恶意技能的分发和供应链攻击风险——开源技能仓库若缺乏安全审核机制，可能被植入后门或恶意指令
  - 技能市场中的知识产权争议——技能可能无意中复制了受版权保护的流程模板或设计模式
confidence:
  impact: medium
  compound: medium
  hype: low
actionable_insight: deep_dive
object_insights:
- object_type: project
  name: anthropics/skills
  canonical_name: anthropics/skills
  url: https://github.com/anthropics/skills
  positioning: Anthropic 开源的 Claude 技能官方集合，提供 Agent Skills 规范、技能模板和四大类示例技能，是 Claude
    技能生态的基础平台。
  technical_signal: 定义了基于 SKILL.md 指令文件加 YAML 前端元数据的技能规范，支持通过 Claude Code 插件市场和 Claude
    API 两种方式加载与安装技能。
  adoption_signal: 仓库以 Apache 2.0 开源协议发布，用户可通过 /plugin marketplace add 命令直接注册为插件市场，大幅降低了技能开发和分享的门槛。
  ecosystem_relevance: 作为官方技能仓库为 Claude 生态提供标准化技能模板和参考实现，有助于吸引开发者共建技能生态，增强 Claude
    在 Agent 领域的平台竞争力。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: Anthropic 开源技能仓库标志着 Claude 技能生态系统的正式开放，仓库的社区贡献活跃度、技能数量和覆盖领域的扩展速度，将直接影响
    Claude 在 AI Agent 平台竞争中的地位。
  risk_notes:
  - 文档处理技能以 source-available 而非完全开源许可发布，可能限制社区对其核心实现的复用和改进。
  - 技能生态的活跃度依赖于社区贡献意愿，若缺乏足够的第三方技能贡献，仓库可能沦为官方样板而缺乏生态活力。
  score: 9.0
  article_ids:
  - 82a901da1b9bedec
  evidence_snippets:
  - 该仓库是 Anthropic 在 GitHub 上发布的 Claude 技能官方实现，包含 SKILL.md 指令文件、Agent Skills 规范和技能模板。
  - 仓库中的示例技能覆盖创意设计、开发技术、企业通信和文档处理四大类别，大部分以 Apache 2.0 开源协议发布。
  - 用户可通过 Claude Code 的 /plugin marketplace add anthropics/skills 命令将本仓库注册为插件市场。
- object_type: product
  name: document-skills
  canonical_name: document-skills
  url: null
  positioning: Anthropic 以 source-available 许可发布的文档处理技能集合，包含 docx、pdf、pptx 和 xlsx
    子技能，是驱动 Claude 文档能力的生产级实现。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Claude 开发者
  - 需要 AI 文档处理能力的企业用户
  - Claude Code 用户
  product_signal: 包含 docx、pdf、pptx 和 xlsx 四种文档格式的生产级处理实现，可通过 /plugin install 命令直接在
    Claude Code 中安装使用。
  market_signal: 以 source-available 而非完全开源许可发布，表明 Anthropic 在开放技能生态与保护核心能力之间采取了折中策略。
  differentiation: 作为 Claude 文档能力的底层实现，与普通第三方文档处理技能相比具有更高的官方保证和与 Claude 平台的原生集成度。
  watch_reason: 文档处理是 AI 在企业场景的核心能力，document-skills 的许可策略演变和功能迭代将直接反映 Anthropic 对企业市场的战略定位与开放程度。
  risk_notes:
  - source-available 许可限制了社区复用的自由度，企业用户在生产环境使用前需仔细审视许可条款的具体限制。
  - 作为 Claude 底层能力的公开参考实现，可能与实际 Claude 服务中的行为存在差异，不应将其视为官方行为的承诺。
  score: 7.0
  article_ids:
  - 82a901da1b9bedec
  evidence_snippets:
  - 文档技能插件包含驱动 Claude 文档处理能力的 docx、pdf、pptx 和 xlsx 子技能，采用 source-available 许可。
  - 用户可通过 /plugin install document-skills@anthropic-agent-skills 命令在 Claude Code 中安装文档技能插件。
- object_type: product
  name: example-skills
  canonical_name: example-skills
  url: null
  positioning: Anthropic 提供的 Claude 技能示例集合，覆盖创意设计、开发技术和企业通信三大类别，供用户学习和参考技能编写模式。
  technical_signal: null
  adoption_signal: null
  ecosystem_relevance: null
  target_users:
  - Claude 技能开发者
  - 希望了解 Claude 技能系统的用户
  - AI 应用开发者
  product_signal: 包含创意设计、开发技术和企业通信三大类别示例技能，可通过 /plugin install example-skills@anthropic-agent-skills
    命令一键安装。
  market_signal: 作为官方示例集向开发者展示技能系统的能力边界，有助于降低学习曲线并吸引更多开发者创建和分享自定义技能。
  differentiation: 与 document-skills 的生产级实现不同，example-skills 专注于教育目的，以 Apache 2.0
    完全开源许可发布，更适合学习和二次开发。
  watch_reason: 示例技能的覆盖范围和复杂度演进反映了 Anthropic 对 Claude 技能能力边界的定义，是判断技能生态发展方向和平台策略的重要晴雨表。
  risk_notes:
  - 示例技能仅供演示和教育目的，实际 Claude 服务中的行为可能与示例实现存在差异，不应直接依赖。
  - 仓库可能缺乏持续更新维护，导致部分示例技能在 Claude 系统升级后失效。
  score: 5.0
  article_ids:
  - 82a901da1b9bedec
  evidence_snippets:
  - 示例技能插件包含仓库中创意、开发和企业通信等类别的所有示例技能，可供学习和参考。
  - 用户可通过 /plugin install example-skills@anthropic-agent-skills 命令安装示例技能插件。
- object_type: project
  name: template-skill
  canonical_name: template-skill
  url: null
  positioning: 创建自定义 Claude 技能的起始模板，展示 SKILL.md 文件的最小必需结构和编写规范，帮助开发者快速上手技能开发。
  technical_signal: 模板仅要求 name 和 description 两个 YAML 前端元数据字段加 Markdown 指令体，这种极简设计大幅降低了技能创建的技术门槛。
  adoption_signal: 位于开源仓库的 ./template 目录中，任何开发者都可直接复制使用，与官方技能采用完全一致的结构标准。
  ecosystem_relevance: 作为官方模板为技能生态提供统一的创作起点，确保社区贡献的技能在结构上兼容官方规范，降低生态碎片化风险。
  target_users: []
  product_signal: null
  market_signal: null
  differentiation: null
  watch_reason: 技能模板的演进方向反映了 Anthropic 对开发者体验的持续优化策略，是衡量 Claude 技能生态开发者友好度和准入门槛的重要指标。
  risk_notes:
  - 模板过于简化可能导致社区技能风格和质量参差不齐，缺乏最佳实践引导。
  - 若模板更新滞后于技能规范变化，基于旧模板开发的技能可能在新版本中出现兼容性问题。
  score: 4.0
  article_ids:
  - 82a901da1b9bedec
  evidence_snippets:
  - 模板技能是创建自定义技能的起始模板，只需填充 name 和 description 字段以及 Markdown 指令即可完成定义。
  - 模板技能位于仓库的 ./template 子目录中，展示了 SKILL.md 文件的最小必需结构和编写规范。
---

Note:This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see agentskills.io.

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:

- What are skills?
- Using skills in Claude
- How to create custom skills
- Equipping agents for the real world with Agent Skills

This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md`

file containing the instructions and metadata that Claude uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power Claude's document capabilities under the hood in the `skills/docx`

, `skills/pdf`

, `skills/pptx`

, and `skills/xlsx`

subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

- ./skills: Skill examples for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- ./spec: The Agent Skills specification
- ./template: Skill template

You can register this repository as a Claude Code Plugin marketplace by running the following command in Claude Code:

```
/plugin marketplace add anthropics/skills
```


Then, to install a specific set of skills:

- Select
`Browse and install plugins`

- Select
`anthropic-agent-skills`

- Select
`document-skills`

or`example-skills`

- Select
`Install now`


Alternatively, directly install either Plugin via:

```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```


After installing the plugin, you can use the skill by just mentioning it. For instance, if you install the `document-skills`

plugin from the marketplace, you can ask Claude Code to do something like: "Use the PDF skill to extract the form fields from `path/to/some-file.pdf`

"

These example skills are all already available to paid plans in Claude.ai.

To use any skill from this repository or upload custom skills, follow the instructions in Using skills in Claude.

You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the Skills API Quickstart for more.

Skills are simple to create - just a folder with a `SKILL.md`

file containing YAML frontmatter and instructions. You can use the **template-skill** in this repository as a starting point:

```
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
# My Skill Name
[Add your instructions here that Claude will follow when this skill is active]
## Examples
- Example usage 1
- Example usage 2
## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:

`name`

- A unique identifier for your skill (lowercase, hyphens for spaces)`description`

- A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see How to create custom skills.

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

**Notion**- Notion Skills for Claude