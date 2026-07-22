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