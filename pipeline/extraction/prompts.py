"""
pipeline/extraction/prompts.py — Agent 提示词模板

为 Stage 2a (BaseInfo) 和 Stage 2b (FactExtraction) 生成 Agent 提示词。

设计哲学：
    - system_prompt: 定义 Agent 的角色、规则和输出契约（不变部分）
    - user_prompt: 提供具体文章数据和提取要求（可变部分）
    - 两者分离便于独立调试和版本管理

提示词语言：中文（与项目文档语言一致）
模型默认使用 claude-sonnet-4-6（来自 config.yaml llm.models.extract）

截断策略：
    - BaseInfo 提取：正文截断至 8000 字符（信息源类型判断不需要全文）
    - FactExtraction 提取：正文截断至 12000 字符（事实提取需要更多上下文）
"""

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

# 正文截断长度
BASE_INFO_BODY_MAX_CHARS = 8000
FACT_EXTRACTION_BODY_MAX_CHARS = 12000


# =============================================================================
# Stage 2a: BaseInfo 提示词
# =============================================================================

def get_base_info_system_prompt() -> str:
    """
    返回 BaseInfo Agent 的系统提示词。

    Agent 职责：
        根据文章正文判断信息源类型 (source_type)。
        这是一个分类任务——只需判断文章来源的生态属性。

    分类依据：
        - academic_paper: 学术论文（从 arXiv、学术会议等处抓取）
            → 特征：摘要格式、实验数据、引用文献、学术语言
        - tech_blog: 技术博客或官方技术发布
            → 特征：第一人称、技术深度、官方产品公告、教程风格
        - news_media: 科技媒体新闻报道
            → 特征：第三方报道口吻、引用多方观点、商业角度
        - community_discussion: 社区讨论或个人博客/Newsletter
            → 特征：个人观点、讨论语气、社区链接（Hacker News 等）
    """
    return """你是一个精确的元信息提取智能体。

## 任务
根据文章正文，判断文章的信息源类型 (source_type)。

## 分类标准

source_type 必须从以下四个值中选择：

1. academic_paper — 学术论文
   特征：摘要格式、实验数据、引用文献、学术语言、arXiv 等学术平台来源

2. tech_blog — 技术博客或官方技术发布
   特征：第一人称技术文章、官方产品公告、技术教程、公司在自有域名发布

3. news_media — 科技媒体新闻报道
   特征：第三方报道口吻、引用多方观点、商业角度、记者署名

4. community_discussion — 社区讨论或个人博客/Newsletter
   特征：个人观点、论坛讨论语气、Newsletter 摘要风格、社区平台来源

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容（不要加 ```json 标记，不要加解释）：
{"source_type": "选择的类型"}

## 示例
{"source_type": "academic_paper"}
{"source_type": "news_media"}"""


def build_base_info_user_prompt(missing_fields: list[str], body: str) -> str:
    """
    构造 BaseInfo 提取的用户提示词。

    参数：
        missing_fields: 需要提取的字段名列表（如 ["source_type"]）
        body: 文章正文（Markdown 格式）

    返回：
        格式化的用户提示词字符串
    """
    # 截断正文以控制 token 消耗
    truncated_body = body[:BASE_INFO_BODY_MAX_CHARS]
    if len(body) > BASE_INFO_BODY_MAX_CHARS:
        truncated_body += "\n\n[... 正文已截断，后续内容省略 ...]"

    fields_str = "、".join(missing_fields)
    return f"""## 需要提取的字段
{fields_str}

## 文章正文
---
{truncated_body}
---

## 要求
请根据上述文章正文判断 source_type，只返回一个 JSON 对象。"""


# =============================================================================
# Stage 2b: FactExtraction 提示词
# =============================================================================

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
极简一句话总结（最多 80 中文/英文字符）。剔除所有修饰语，只讲核心事实。列表页的扫描锚点。
**必须用中文输出。**

### 2. objectiveSummary
客观事实摘要（最多 150 个中文字符）。5W1H 格式：谁、什么时候、做了什么、怎么做的、结果如何。
剥离一切主观形容词（"惊艳"、"革命性"等），只用冷峻语言描述。
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
  "keyLogicFlow": ["第一条中文关键事实", "第二条中文关键事实"]
}"""


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
    # 截断正文以控制 token 消耗
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
- entities 中的公司名、技术名、人名保持原文"""
