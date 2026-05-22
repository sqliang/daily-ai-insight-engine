"""
区块零：基础元信息 (Base Information)
=====================================

[核心价值]：物理溯源，支撑基础的数据查询与展示。

字段设计理念：
    - id: 原文的唯一标识符或 URL Hash，确保每条资讯可精确检索、去重和关联
    - title: 资讯或文章的原始标题，作为前端列表展示的绝对锚点
    - sourceUrl: 原始链接 URL，数据可追溯性的根本保障
    - publishedAt: 发布时间，用于构建时间轴（Timeline）和判断时效性
    - sourceType: 信息源类型，"信源决定信噪比"
"""

from enum import Enum
from pydantic import BaseModel, Field


class SourceType(str, Enum):
    """
    信息源类型枚举

    标识该信息的发源地生态。
    背后的思维维度："信源决定信噪比"。
        - academic_paper: 学术论文（如 arXiv），代表技术前沿但缺乏商业落地
        - tech_blog: 技术博客/官方发布，权威但可能有商业目的
        - news_media: 科技媒体/公关稿，商业意图强但存在技术水分
        - community_discussion: 社区讨论/社交媒体，代表最真实的开发者情绪
        - newsletter_rss: 邮件通讯/RSS 摘要，精选聚合但缺乏深度分析
    """

    ACADEMIC_PAPER = "academic_paper"
    TECH_BLOG = "tech_blog"
    NEWS_MEDIA = "news_media"
    COMMUNITY_DISCUSSION = "community_discussion"
    NEWSLETTER_RSS = "newsletter_rss"


class BaseInfo(BaseModel):
    """
    基础元信息模型

    物理溯源，支撑基础的数据查询与展示。
    """

    id: str = Field(
        ...,
        description="原文的唯一标识符或 URL Hash。兜底追踪：确保每条资讯可精确检索、去重和关联。",
    )

    title: str = Field(
        ...,
        description="资讯或文章的原始标题。标注什么：未经加工的原始语境。为什么用：作为前端列表展示的绝对锚点。",
    )

    source: str = Field(
        ...,
        description="原始链接 URL。数据可追溯性的根本保障，防止大模型凭空捏造（幻觉）事件。",
    )

    published: str = Field(
        ...,
        description="发布时间。用于构建大屏的时间轴（Timeline）和判断时效性。",
    )

    created: str = Field(
        ...,
        description="创建时间。用于记录数据获取的时间点，作为时间戳。",
    )

    source_type: SourceType = Field(
        ...,
        alias="sourceType",
        description="信息源类型。标识该信息的发源地生态，决定内容的可信度权重。",
    )

    class Config:
        populate_by_name = True
