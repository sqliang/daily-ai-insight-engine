"""
pipeline/extraction/base_info/prompts.py — Stage 2a (BaseInfo) Agent 提示词模板

为 BaseInfo Agent 生成 system_prompt 和 user_prompt。
仅在 source_type 无法从目录名推断时作为兜底使用。
"""

# Stage 2a: BaseInfo 提示词
# ---------------------------------------------------------------------------
# source_type 分类体系
# ---------------------------------------------------------------------------

_BASE_INFO_SOURCE_TYPE_DESC = """你需要判断文章的信息源类型 (sourceType)，从以下 5 种中选择其一：

- academic_paper: 学术论文、预印本（如 arXiv），强调研究方法、实验数据和同行评议
- tech_blog: 技术博客、工程实践分享（如 OpenAI Blog、Anthropic Blog），强调技术实现细节
- news_media: 科技新闻媒体报道（如 TechCrunch、VentureBeat），强调事件报道和行业动态
- community_discussion: 社区讨论、论坛帖子（如 Hacker News、Reddit），强调多人观点和交流
- newsletter_rss: 邮件通讯 RSS 摘要（如 TLDR AI），强调信息聚合和快速摘要
"""

_BASE_INFO_SYSTEM_PROMPT = f"""你是一个精准的元数据提取 Agent。

{_BASE_INFO_SOURCE_TYPE_DESC}

你的任务是根据给定文章的正文内容，判断该文章的 sourceType。
只返回一个 JSON 对象，不要有任何额外文字。"""


def get_base_info_system_prompt() -> str:
    """
    返回 BaseInfo Agent 的系统提示词。

    定义 Agent 角色为精准元数据提取器，说明 sourceType 分类标准，
    并要求只输出 JSON。
    """
    return _BASE_INFO_SYSTEM_PROMPT


def build_base_info_user_prompt(missing_fields: list[str], body: str) -> str:
    """
    构造 BaseInfo 提取的用户提示词。

    参数：
        missing_fields: 需要提取的字段名列表
        body: 文章正文（已截断至 8000 字符）

    返回：
        完整的用户提示词字符串
    """
    # 正文截断至 8000 字符（信息源类型判断不需要全文）
    truncated_body = body[:8000]

    fields_str = "、".join(missing_fields)
    prompt = f"""请根据以下文章内容，判断其信息源类型 (sourceType)。

缺失字段：{fields_str}

---
{truncated_body}
---

请返回一个 JSON 对象，格式如下：
{{"sourceType": "选择的类型"}}"""

    return prompt
