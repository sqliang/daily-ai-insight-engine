"""
pipeline/extraction/agent/prompts/base_info.py — Stage 2a (BaseInfo) Agent 提示词模板

为 BaseInfo Agent 生成 system_prompt 和 user_prompt。

设计哲学：
    - system_prompt: 定义 Agent 的角色、规则和输出契约（不变部分）
    - user_prompt: 提供具体文章数据和提取要求（可变部分）
    - 两者分离便于独立调试和版本管理

提示词语言：中文（与项目文档语言一致）
模型默认使用 claude-sonnet-4-6（来自 config.yaml llm.models.extract）

截断策略：
    - BaseInfo 提取：正文截断至 8000 字符（信息源类型判断不需要全文）
"""

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

# 正文截断长度
BASE_INFO_BODY_MAX_CHARS = 8000


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
