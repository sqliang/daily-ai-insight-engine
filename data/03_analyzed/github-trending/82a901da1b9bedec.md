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
tldr: Anthropic 开源了 Claude 的 Skills 系统仓库，包含示例技能和规范文档
objective_summary: Anthropic 于 GitHub 发布 skills 开源仓库，包含 Claude AI 的技能指令集、Agent Skills
  规范、技能模板及四大类示例技能（创意设计、开发技术、企业通讯、文档处理），开发者可自由使用或自定义技能。
event_type: framework_tools
epistemic_status: verified_fact
entities:
  companies:
  - Anthropic
  - GitHub
  - Notion
  technologies:
  - Agent Skills
  - YAML frontmatter
  - SKILL.md
  - MCP
  - Claude API
  key_people: []
key_logic_flow:
- Anthropic 在 GitHub 上开源了 skills 仓库，包含 Claude 的技能系统实现，遵循 Agent Skills 标准（agentskills.io）。
- 每个 skill 是一个包含 SKILL.md 文件的独立文件夹，通过 YAML 前置元数据（name、description）和 Markdown 指令定义
  Claude 的行为。
- 仓库包含四大类示例技能：创意与设计、开发与技术、企业与通讯、文档处理技能（docx/pdf/pptx/xlsx 以源码可用形式提供）。
- 用户可通过 Claude Code 插件市场或 /plugin install 命令直接安装 document-skills 和 example-skills
  插件。
- 开发者可通过 Claude API 调用预置技能或上传自定义技能，并可基于仓库中的 template-skill 创建新技能。
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