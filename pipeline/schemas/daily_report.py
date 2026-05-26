"""
pipeline/schemas/daily_report.py — Stage 4b 日报输出 Pydantic 模型

定义 Editor-in-Chief Agent 产出的日报 JSON 结构。
与前端 src/lib/agent/schema.ts 的 Zod dailyReportSchema 对齐，
共用 pipeline/schemas/ 中已有的 EventType 和 Sentiment 枚举。

包含：
    - DailyReport 及子模型（TopEvent、DeepDive、TrendInsight、Signal、VisualizationData）
    - validate_daily_report(): 两阶段校验（strict → 轻量修复 → re-validate）
      沿袭 fact_extraction/validator.py 与 deep_analysis_agent.py 的既有模式
"""

from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, ValidationError

from .fact_extraction import EventType
from .deep_analysis import Sentiment


# =============================================================================
# 日报专用轻量枚举（Literal 比 Enum 更适合 LLM 输出的容错场景）
# =============================================================================

DimensionLabel = Literal["technology", "application", "policy", "capital"]
SeverityLabel = Literal["low", "medium", "high"]
EntityTypeLabel = Literal["company", "technology", "person", "product", "region"]
LanguageLabel = Literal["zh", "en", "mixed"]


# =============================================================================
# 子模型
# =============================================================================

class DataSourceSummary(BaseModel):
    """数据源概览。描述日报的输入样本构成和信源覆盖范围。"""

    total_articles: int = Field(..., ge=0, alias="totalArticles", description="样本总量")
    sources: list[str] = Field(default_factory=list, description="数据源名称列表")
    languages: list[LanguageLabel] = Field(default_factory=list, description="语言覆盖")
    selection_rationale: str = Field("", alias="selectionRationale", description="信源选择说明")

    class Config:
        populate_by_name = True


class TopEvent(BaseModel):
    """Top 事件。按 impactScore 排名的头条新闻聚合条目。"""

    title: str = Field(..., description="事件标题（中文）")
    article_ids: list[str] = Field(..., alias="articleIds", min_length=1, description="关联文章 ID 列表")
    event_type: EventType = Field(..., alias="eventType", description="事件分类")
    impact_score: float = Field(..., ge=1, le=10, alias="impactScore", description="影响力评分 (1-10)")
    why_it_matters: str = Field(..., alias="whyItMatters", description="为什么重要（中文）")
    evidence: list[str] = Field(..., min_length=1, max_length=6, alias="evidence", description="支撑证据")

    class Config:
        populate_by_name = True


class DeepDive(BaseModel):
    """深度分析。具有战略意义的专题解读，超出原始 impactScore。"""

    title: str = Field(..., description="深度分析标题（中文）")
    background: str = Field(..., description="背景")
    impact: str = Field(..., description="行业影响")
    watch_next: str = Field(..., alias="watchNext", description="后续关注")

    class Config:
        populate_by_name = True


class TrendInsight(BaseModel):
    """趋势判断。按 technology/application/policy/capital 四个维度组织的趋势叙事。"""

    dimension: DimensionLabel = Field(..., description="维度标签")
    judgment: str = Field(..., description="趋势判断（中文）")
    supporting_signals: list[str] = Field(
        ..., min_length=1, max_length=5, alias="supportingSignals", description="支撑信号"
    )

    class Config:
        populate_by_name = True


class Signal(BaseModel):
    """风险或机会信号。"""

    signal: str = Field(..., description="信号描述（中文）")
    severity: SeverityLabel = Field(..., description="严重程度")
    rationale: str = Field(..., description="判断依据（中文）")

    class Config:
        populate_by_name = True


class DistributionItem(BaseModel):
    """可视化分布数据项。"""

    label: str = Field(..., description="分类标签（英文枚举值）")
    count: int = Field(..., ge=0, description="计数")


class ImpactRankingItem(BaseModel):
    """影响力排名数据项。"""

    article_id: str = Field(..., alias="articleId", description="文章 ID")
    title: str = Field(..., description="文章标题")
    score: float = Field(..., ge=1, le=10, description="影响力评分")

    class Config:
        populate_by_name = True


class EntityFrequencyItem(BaseModel):
    """实体频率数据项。"""

    entity: str = Field(..., description="实体名称")
    count: int = Field(..., ge=1, description="出现次数")
    type: EntityTypeLabel = Field(..., description="实体类型")


class VisualizationData(BaseModel):
    """预计算的可视化数据。使前端页面保持纯展示逻辑。"""

    event_type_distribution: list[DistributionItem] = Field(
        default_factory=list, alias="eventTypeDistribution", description="事件类型分布"
    )
    sentiment_distribution: list[DistributionItem] = Field(
        default_factory=list, alias="sentimentDistribution", description="情绪分布"
    )
    impact_ranking: list[ImpactRankingItem] = Field(
        default_factory=list, alias="impactRanking", description="影响力排名"
    )
    entity_frequency: list[EntityFrequencyItem] = Field(
        default_factory=list, alias="entityFrequency", description="实体频率"
    )

    class Config:
        populate_by_name = True


class DailyReport(BaseModel):
    """
    AI 洞察日报顶层模型。

    Editor-in-Chief Agent 的最终输出，包含人类可读的分析文本 + 预计算可视化数据，
    使前端看板页面可完全无状态、纯展示地渲染。
    """

    date: str = Field(..., description="日报日期 (YYYY-MM-DD)")
    generated_at: str = Field(..., alias="generatedAt", description="生成时间 (ISO-8601)")
    report_title: str = Field(..., alias="reportTitle", description="日报标题")
    executive_summary: str = Field(..., alias="executiveSummary", description="执行摘要（中文）")
    data_source_summary: DataSourceSummary = Field(..., alias="dataSourceSummary", description="数据源概览")
    top_events: list[TopEvent] = Field(..., min_length=1, max_length=8, alias="topEvents", description="Top 事件")
    deep_dives: list[DeepDive] = Field(..., min_length=1, max_length=6, alias="deepDives", description="深度分析")
    trend_insights: list[TrendInsight] = Field(..., min_length=1, max_length=6, alias="trendInsights", description="趋势判断")
    risk_signals: list[Signal] = Field(default_factory=list, alias="riskSignals", description="风险信号")
    opportunity_signals: list[Signal] = Field(default_factory=list, alias="opportunitySignals", description="机会信号")
    visualization_data: VisualizationData = Field(..., alias="visualizationData", description="可视化数据")

    class Config:
        populate_by_name = True


# =============================================================================
# 两阶段校验（沿袭 fact_extraction/validator.py 的模式）
# =============================================================================

# 用于 fuzzy 修复的 severity 值映射
_SEVERITY_FUZZY: dict[str, str] = {
    "低": "low", "中": "medium", "高": "high",
    "l": "low", "m": "medium", "h": "high",
    "lo": "low", "med": "medium", "hi": "high",
    "minor": "low", "moderate": "medium", "critical": "high", "severe": "high",
}

_DIMENSION_FUZZY: dict[str, str] = {
    "tech": "technology", "技术": "technology",
    "app": "application", "应用": "application",
    "regulatory": "policy", "regulation": "policy", "政策": "policy", "监管": "policy",
    "capital": "capital", "投资": "capital", "资金": "capital", "资本": "capital",
}


def _fuzzy_repair_report(data: dict) -> dict:
    """对 LLM 输出做轻量修复，使其更可能通过 Pydantic 校验。"""
    repaired = data.copy()

    # 确保列表字段至少为空列表
    for list_key in ("topEvents", "deepDives", "trendInsights", "riskSignals", "opportunitySignals"):
        if list_key not in repaired or not isinstance(repaired.get(list_key), list):
            repaired[list_key] = []

    # 修复 signal 子对象中的 severity
    for signal_key in ("riskSignals", "opportunitySignals"):
        for sig in repaired.get(signal_key, []):
            if isinstance(sig, dict):
                sev = sig.get("severity", "")
                if sev and sev not in ("low", "medium", "high"):
                    match = _SEVERITY_FUZZY.get(str(sev).lower().strip())
                    if match:
                        sig["severity"] = match

    # 修复 trendInsights 中的 dimension
    for trend in repaired.get("trendInsights", []):
        if isinstance(trend, dict):
            dim = trend.get("dimension", "")
            if dim and dim not in ("technology", "application", "policy", "capital"):
                match = _DIMENSION_FUZZY.get(str(dim).lower().strip())
                if match:
                    trend["dimension"] = match

    # 确保 visualizationData 存在
    if "visualizationData" not in repaired or not isinstance(repaired.get("visualizationData"), dict):
        repaired["visualizationData"] = {}

    # 确保 dataSourceSummary 存在
    if "dataSourceSummary" not in repaired or not isinstance(repaired.get("dataSourceSummary"), dict):
        repaired["dataSourceSummary"] = {}

    return repaired


def validate_daily_report(data: dict) -> DailyReport:
    """
    两阶段校验日报 JSON（沿袭 fact_extraction/validator.py 的模式）。

    1. 尝试 strict model_validate
    2. 失败时做轻量 fuzzy 修复后重新校验

    参数：
        data: LLM 输出的日报 dict

    返回：
        通过校验的 DailyReport 实例

    异常：
        ValidationError: 修复后仍然无法通过校验
    """
    try:
        return DailyReport.model_validate(data)
    except ValidationError:
        repaired = _fuzzy_repair_report(data)
        return DailyReport.model_validate(repaired)
