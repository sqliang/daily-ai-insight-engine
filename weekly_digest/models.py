"""
weekly_digest/models.py — 周报数据模型

定义周报的结构化 schema（Pydantic v2），是收集逻辑（collector）与渲染逻辑（render）
之间的唯一契约。每次运行除 Markdown 外还会输出同名 JSON（该模型的序列化结果），
作为未来 web 站点周报功能的数据源——届时可直接读取 JSON，或 upsert 到 PostgreSQL
后由前端查询，schema 保持稳定。
"""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class DigestItem(BaseModel):
    """周报中的单个条目（一个项目 / 产品 / 文章）。

    字段按"渲染所需的最小集合"设计：中文摘要缺失时由 collector 走降级链
    填充英文原文，渲染层不再判断数据完整度。
    """

    article_id: str = Field(
        ...,
        description="文章 ID（源 URL 的 SHA-256），与 pipeline 数据目录中的文件名一致，可用于溯源",
    )
    title: str = Field(..., description="条目标题（GitHub 为 owner/repo，Product Hunt 为产品名）")
    url: str = Field(..., description="原始链接（frontmatter.source）")
    created: date = Field(..., description="pipeline 抓取日期，周报按此字段分组")
    published: Optional[date] = Field(
        None,
        description="原始发布日期（Product Hunt 有效；GitHub Trending 通常为空）",
    )
    summary_zh: Optional[str] = Field(
        None,
        description="中文摘要（Stage 2 tldr）。为 None 表示文章未执行 extraction，渲染层展示英文原文降级",
    )
    detail_zh: Optional[str] = Field(
        None,
        description="中文详细说明（Stage 2 objective_summary），未提取时为 None",
    )
    description_en: Optional[str] = Field(
        None,
        description="英文原始描述（frontmatter.description 截断版），中英文对照的英文侧",
    )
    trending_days: List[date] = Field(
        default_factory=list,
        description="本周内出现在 manifest 的日期列表（GitHub Trending 连续上榜天数统计用）",
    )


class DigestStats(BaseModel):
    """周报头部统计信息。"""

    total: int = Field(..., description="本周收录条目总数")
    extracted: int = Field(..., description="已完成 Stage 2 提取（有中文摘要）的条目数")
    days_covered: int = Field(..., description="本周内有数据的日期数")


class WeeklyDigest(BaseModel):
    """一份周报（单信源 × 单 ISO 周）。

    渲染层输入，也是 JSON 输出文件的顶层结构。未来 web 站点直接消费此模型。
    """

    source: str = Field(..., description="信源目录名，如 github-trending / producthunt")
    source_label: str = Field(..., description="信源展示名，如 GitHub Trending / Product Hunt")
    iso_week: str = Field(..., description="ISO 周标识，如 2026-W41")
    week_start: date = Field(..., description="周起始日（周一）")
    week_end: date = Field(..., description="周结束日（周日）")
    generated_at: date = Field(..., description="报告生成日期")
    stats: DigestStats = Field(..., description="统计信息")
    items: List[DigestItem] = Field(
        default_factory=list,
        description="本周条目，渲染层按 created 倒序分组展示",
    )
