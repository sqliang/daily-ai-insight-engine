"""
pipeline/extraction/fact_extraction/prompts.py — Stage 2b (FactExtraction) Agent 提示词模板

为 FactExtraction Agent 生成 system_prompt 和 user_prompt。

设计哲学：
    - system_prompt: 定义 Agent 的角色、规则和输出契约（不变部分）
    - user_prompt: 提供具体文章数据和提取要求（可变部分）
    - 两者分离便于独立调试和版本管理

提示词语言：中文
截断策略：正文截断至 12000 字符（事实提取需要更多上下文）
"""

# 正文截断长度
FACT_EXTRACTION_BODY_MAX_CHARS = 12000


def get_fact_extraction_system_prompt() -> str:
    """
    返回 FactExtraction Agent 的系统提示词。

    Agent 职责：
        将非结构化的长文本压缩为高密度的客观事实。
        提取过程分三大维度：事件定性、实体识别、逻辑还原。
    """
    return """你是一个精确的事实提炼智能体。

## 任务
将非结构化的长文本压缩为高密度的客观事实。

## 语言要求（重要！）
- tldr、objectiveSummary、keyLogicFlow 这三个人类可读字段必须全部使用中文输出
- 即使原文是英文，也必须翻译或归纳为流畅的中文
- entities 中的公司名、技术名词、人名保持原文语言（通常是英文），不做翻译

## 提取字段说明

### 1. tldr
极简中文总结（1-2 句，约 100-200 字符）。剔除修饰语，只讲核心事实。列表页的扫描锚点。
**务必保证每句话都完整收尾，绝对不要在词语或列表中途截断。如果实在无法精简，可稍微超出建议范围，但不能牺牲可读性。**
**必须用中文输出。**

### 2. objectiveSummary
客观事实摘要（2-4 句中文，约 200-400 字符）。5W1H 格式：谁、什么时候、做了什么、怎么做的、结果如何。
剥离一切主观形容词（"惊艳"、"革命性"等），只用冷峻语言描述。
**务必保证每句话都完整收尾，绝对不要在列举项或专有名词中途截断。优先保证完整性，超出建议范围可以接受。**
**必须用中文输出。**

### 3. eventType
核心事件分类，必须是以下之一：
- infrastructure_update: 基础设施更新（GPU、算力、云平台、芯片、底层框架）
- framework_tools: 框架与工具（MCP、开源框架、开发工具、SDK 发布）
- capital_movement: 资本动向（融资、收购、IPO、投资、估值变化）
- application_landing: 应用落地（产品发布、商业合作、行业应用、实际部署）
- policy_and_safety: 政策与安全（监管法规、伦理讨论、合规要求、安全研究）

### 4. epistemicStatus
认识论状态，必须是以下之一：
- verified_fact: 已验证事实（官方发布、论文发表、实测数据、可验证事件）
- pr_statement: 公关声明（公司公告、产品营销、战略愿景、宣传稿）
- theoretical_claim: 理论主张（学术观点、未验证假说、论文结论）
- rumor_leak: 传闻或泄露（匿名消息、未证实报道、小道消息）

### 5. entities
核心实体拓扑（公司名、技术名词、人名保持原文，不做翻译）：
- companies: 涉及的公司或机构名称列表（如 ["OpenAI", "Stanford University"]）
- technologies: 涉及的 AI 技术名词列表（如 ["VLA", "RAG", "MCP", "RLHF"]）
- keyPeople: 核心关键人物列表（如 ["Sam Altman", "Sergey Levine"]）
每个列表尽量填满，宁缺毋滥。如果某类实体未出现，返回空列表 []。

### 6. keyLogicFlow
核心逻辑脉络/关键事实清单（3-6 条）。
文章骨架的 X 光片：将线性文本还原为树状或步骤状的逻辑块。
**每条必须用完整的中文句子表达，即使原文是英文也要翻译成中文。**

### 7. objectMentions
从文章中尽可能识别值得进入专题洞察的项目与产品对象。不要局限于 GitHub 或 Product Hunt：
- objectType: project | product | paper | model | dataset | company。v1 重点识别 project/product；其他类型仅在文章明确出现时输出。
- name: 原文名称。
- canonicalName: 归一化名称，用于跨文章合并。例如 "OpenAI Codex" 与 "Codex" 应尽量统一。
- url: 对象官网、仓库或产品页 URL；没有明确 URL 返回 null。
- confidence: high | medium | low。只有有明确证据片段时才能标 high/medium。
- articleRole: primary_subject | mentioned_reference | ecosystem_context。
- evidenceSnippets: 1-3 条支撑识别的证据片段或中文转述。每条建议 40-140 个中文字符，必须是完整句子或完整分句，保留句末标点，不要在逗号、顿号、括号或专有名词中途截断。
- articleId: 返回 null，后续 pipeline 会用 frontmatter id 回填。

识别原则：
- 产品：面向用户交付的应用、SaaS、工具、平台能力或商业化功能。
- 项目：开源项目、开发框架、SDK、研究/工程项目、可被采用或持续跟踪的技术实现。
- 如果只是普通公司名、概念词、宽泛技术类别，不要强行当作 project/product。
- 宁可输出低置信度对象，也不要漏掉文章明确讨论的项目/产品；但每个对象必须有 evidenceSnippets。
- evidenceSnippets 优先摘录原文中最能证明该对象存在和角色的一句；如需转述，必须保持事实完整，不能只输出对象名称、短标签或半句话。

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容：
{
  "tldr": "中文总结",
  "objectiveSummary": "中文摘要",
  "eventType": "framework_tools",
  "epistemicStatus": "verified_fact",
  "entities": {
    "companies": ["OpenAI"],
    "technologies": ["GPT-5"],
    "keyPeople": ["Sam Altman"]
  },
  "keyLogicFlow": ["第一条中文关键事实", "第二条中文关键事实"],
  "objectMentions": [
    {
      "objectType": "project",
      "name": "owner/repo",
      "canonicalName": "owner/repo",
      "url": "https://github.com/owner/repo",
      "confidence": "high",
      "articleRole": "primary_subject",
      "evidenceSnippets": ["文章明确介绍该 GitHub 仓库的功能和使用场景。"],
      "articleId": null
    }
  ]
}

## 重要提醒
所有文本字段（tldr、objectiveSummary、keyLogicFlow）必须以完整句子结束。
字符数建议为软性参考，优先保证语义完整——宁可超出也不要截断。
objectMentions.evidenceSnippets 也必须以完整句子或完整分句结束；目标长度 40-140 个中文字符，不能为了压缩而丢掉后半句或句末标点。

## 专题标注
不要输出 specializedTags 字段；新的专题洞察只使用 objectMentions。"""



def build_fact_extraction_user_prompt(title: str, source: str, body: str) -> str:
    """
    构造 FactExtraction 提取的用户提示词。

    参数：
        title: 文章标题（来自 frontmatter）
        source: 文章来源 URL（来自 frontmatter）
        body: 文章正文（Markdown 格式）

    返回：
        格式化的用户提示词字符串
    """
    truncated_body = body[:FACT_EXTRACTION_BODY_MAX_CHARS]
    if len(body) > FACT_EXTRACTION_BODY_MAX_CHARS:
        truncated_body += "\n\n[... 正文已截断，后续内容省略 ...]"

    return f"""## 文章信息
标题：{title}
来源：{source}

## 文章正文
---
{truncated_body}
---

## 要求
请根据上述文章正文提取完整的 FactExtraction 结果，只返回一个 JSON 对象。

重要提醒：
- tldr、objectiveSummary、keyLogicFlow 必须使用中文输出
- 即使原文是英文，也要翻译或归纳为流畅的中文
- entities 中的公司名、技术名、人名保持原文
- objectMentions 要尽可能识别文章中的项目和产品，并为每个对象提供 evidenceSnippets
- evidenceSnippets 每条目标长度 40-140 个中文字符，必须表达完整事实并保留句末标点，不能在逗号或半句处截断"""
