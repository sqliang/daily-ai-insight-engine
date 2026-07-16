"""
pipeline/schemas/daily_report.py — Stage 4b 日报输出 Pydantic 模型

定义 Editor-in-Chief Agent 产出的日报 JSON 结构。
与前端 src/lib/agent/schema.ts 的 Zod dailyReportSchema 对齐，
共用 pipeline/schemas/ 中已有的 EventType 和 Sentiment 枚举。

包含：
    - DailyReport 及子模型（TopEvent、DeepDive、TrendInsight、Signal、VisualizationData）
    - SpecializedBrief 及子模型（GithubBrief、ProductBrief、PaperBrief、
      ObjectInsightBrief、SpecializedInsightItem、SpecializedSource）
    - validate_daily_report(): 两阶段校验（strict → 轻量修复 → re-validate）
      沿袭 fact_extraction/validator.py 与 deep_analysis_agent.py 的既有模式
"""

from __future__ import annotations

from enum import Enum
from typing import Literal, Optional

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


class EvidenceSource(BaseModel):
    """证据来源的可解析结构。从 articleIds 解析 URL，供前端渲染可点击来源链接。"""

    source_dir: str = Field(..., alias="sourceDir", description="信源目录名（如 theverge）")
    title: str = Field(..., description="文章标题")
    url: str = Field(..., description="原文 URL")

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
    evidence_article_ids: list[list[str]] = Field(
        default_factory=list, alias="evidenceArticleIds",
        description="每条 evidence 对应的 articleId 列表，长度与 evidence 一致，由 LLM 输出",
    )
    evidence_sources: list[EvidenceSource] = Field(
        default_factory=list, alias="evidenceSources",
        description="证据来源的可解析结构，由 pipeline 后处理从 articleIds 解析",
    )

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
    AI 洞察报告顶层模型。

    Editor-in-Chief Agent 的最终输出，包含：
        - 人类可读的分析文本（执行摘要、Top 事件、深度分析、趋势判断、风险/机会信号）
        - 预计算可视化数据（visualizationData），使前端看板可完全无状态渲染
        - 专题洞察（specializedBrief）：GitHub / 论文 / 产品三类垂直简报，
          供 /specialized/* 页面和 /dashboard/{date} 顶部入口消费

    设计理由：
        把日报生成阶段能做的所有判断和聚合都做完，前端只负责展示。这样 Next.js 可以
        通过 Server Component 直接 readFile 读取 JSON，无需 API 层或数据库。
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
    specialized_brief: Optional["SpecializedBrief"] = Field(
        default=None,
        alias="specializedBrief",
        description="专题洞察（GitHub/论文/产品）。由主编 Agent 在 Stage 4b 生成，仅当有专题文章时存在。",
    )

    class Config:
        populate_by_name = True


# =============================================================================
# 专题简报 — Stage 4b 日报中的轻量专题摘要
# =============================================================================


class GithubBrief(BaseModel):
    """
    项目洞察简报——日报中的轻量摘要（Phase 1 早期格式）。

    设计理由：
        新版专题洞察已演进为 ObjectInsightBrief（projectInsights），包含完整项目条目、
        来源引用与关键判断。保留 GithubBrief 是为了兼容历史日报 JSON，前端可在两者间
        平滑降级。
    """

    summary: str = Field(
        ...,
        description="一句话总结今日 GitHub Trending 项目趋势（中文）",
    )

    top_projects: list[str] = Field(
        default_factory=list,
        alias="topProjects",
        description="值得关注的项目名列表（Top 3-5）",
    )

    domain_distribution: dict = Field(
        default_factory=dict,
        alias="domainDistribution",
        description="通用领域分布（如 {'ai_ml': 3, 'devops_infra': 2}）",
    )

    ai_category_distribution: Optional[dict] = Field(
        default=None,
        alias="aiCategoryDistribution",
        description="AI 子领域分布（仅当有 AI 项目时，如 {'agent_framework': 2}）",
    )

    article_count: int = Field(
        ...,
        alias="articleCount",
        description="当日 github-trending 文章总数",
    )

    class Config:
        populate_by_name = True


class ProductBrief(BaseModel):
    """
    产品洞察简报——日报中的轻量摘要（Phase 2 早期格式）。

    与 GithubBrief 类似，新版使用 ObjectInsightBrief（productInsights）承载完整产品洞察。
    保留本模型以兼容历史日报 JSON。
    """

    summary: str = Field(
        default="",
        description="一句话总结今日产品趋势（中文）",
    )

    notable_products: list[str] = Field(
        default_factory=list,
        alias="notableProducts",
        description="值得关注的产品名列表",
    )

    launch_context_distribution: dict = Field(
        default_factory=dict,
        alias="launchContextDistribution",
        description="产品发布上下文分布（如 {'new_launch': 2, 'major_update': 1}）",
    )

    article_count: int = Field(
        default=0,
        alias="articleCount",
        description="当日产品类文章总数",
    )

    class Config:
        populate_by_name = True


class PaperBrief(BaseModel):
    """
    论文洞察简报——日报中的轻量摘要（Phase 2 实现）。

    目前论文洞察仍以摘要形式呈现，未来可像项目 / 产品一样演进为
    ObjectInsightBrief 以支撑更细粒度的论文条目分析。
    """

    summary: str = Field(
        default="",
        description="一句话总结今日论文趋势（中文）",
    )

    key_papers: list[str] = Field(
        default_factory=list,
        alias="keyPapers",
        description="关键论文标题列表",
    )

    research_areas: list[str] = Field(
        default_factory=list,
        alias="researchAreas",
        description="涉及的研究领域列表",
    )

    article_count: int = Field(
        default=0,
        alias="articleCount",
        description="当日论文类文章总数",
    )

    class Config:
        populate_by_name = True


class SpecializedSource(BaseModel):
    """
    专题洞察对象的文章来源引用。

    设计理由：
        LLM 输出洞察时只需给出 articleIds，pipeline 在 _enrich_specialized_sources()
        中将其解析为可点击的来源对象。这样来源解析是确定性的，不依赖模型稳定输出
        标题和 URL，同时让前端能稳定展示“证据链”。
    """

    article_id: str = Field(..., alias="articleId", description="文章 ID")
    title: str = Field(..., description="文章标题")
    source_dir: str = Field(..., alias="sourceDir", description="信源目录名")
    url: str = Field("", description="原文 URL")

    class Config:
        populate_by_name = True


class SpecializedInsightItem(BaseModel):
    """
    项目/产品洞察对象条目。

    一个条目对应一个具体的开源项目或产品，包含：
        - 定位与价值判断（oneLine / whyItMatters）
        - 机会信号与风险（signals / risks）
        - 可追溯到原文的证据链（articleIds / sources / evidenceSnippets）
        - 关注评分（score）

    设计理由：
        把“项目/产品是否值得看”的决策所需信息压缩到一个对象里，避免读者在多个来源间
        来回切换。所有文本字段都经过 _normalize_specialized_sentence() 规整，确保
        前端展示时句子完整、长度可控。
    """

    name: str = Field(..., description="对象名称")
    canonical_name: str = Field(..., alias="canonicalName", description="归一化名称，用于跨天去重和展示")
    url: Optional[str] = Field(default=None, description="对象 URL（如 GitHub 仓库地址、产品官网）")
    one_line: str = Field(..., alias="oneLine", description="一句话定位，建议 30-90 个中文字符，需完整收尾。")
    why_it_matters: str = Field(..., alias="whyItMatters", description="为什么值得关注，建议 80-220 个中文字符，需完整收尾。")
    signals: list[str] = Field(default_factory=list, description="机会、技术、采用或市场信号。每条建议 25-90 个中文字符，需完整收尾。")
    risks: list[str] = Field(default_factory=list, description="风险或不确定性。每条建议 25-90 个中文字符，需完整收尾。")
    score: float = Field(..., ge=1, le=10, description="专题关注评分 1-10")
    article_ids: list[str] = Field(default_factory=list, alias="articleIds", description="支撑该对象的文章 ID 列表")
    sources: list[SpecializedSource] = Field(default_factory=list, description="解析后的支撑来源文章列表，供前端展示可点击链接")
    evidence_snippets: list[str] = Field(
        default_factory=list,
        alias="evidenceSnippets",
        description="证据片段。每条建议 40-140 个中文字符，需表达完整事实并保留句末标点。",
    )

    class Config:
        populate_by_name = True


class ObjectInsightBrief(BaseModel):
    """
    项目/产品洞察聚合简报。

    这是新版专题洞察的核心结构，把多个 SpecializedInsightItem 聚合为一份完整简报：
        - summary / keyJudgment：主编 Agent 对当日专题的整体判断
        - watchSignals：读者后续应关注的关键信号
        - items：具体项目/产品条目
        - distribution：领域/类别分布统计
        - sourceCoverage：本次简报覆盖的信源目录
    """

    summary: str = Field(default="", description="专题摘要")
    key_judgment: str = Field(default="", alias="keyJudgment", description="关键判断，建议 80-220 个中文字符，需完整收尾。")
    watch_signals: list[str] = Field(default_factory=list, alias="watchSignals", description="后续关注信号。每条建议 25-90 个中文字符，需完整收尾。")
    items: list[SpecializedInsightItem] = Field(default_factory=list, description="对象洞察列表")
    distribution: dict = Field(default_factory=dict, description="对象分布统计（如领域、AI 子类别、发布上下文）")
    source_coverage: list[str] = Field(default_factory=list, alias="sourceCoverage", description="覆盖信源目录列表")

    class Config:
        populate_by_name = True


class SpecializedBrief(BaseModel):
    """
    日报中的专题简报——轻量摘要 + 深度洞察 + 入口引导。

    设计理由：
        不同读者关注不同维度：开发者关心 GitHub 项目、研究者关心论文、产品经理关心
        新产品。SpecializedBrief 把这三类内容从综合日报中独立出来，既能在
        /dashboard/{date} 顶部作为入口卡片呈现，也能在 /specialized/* 页面展开为
        完整的垂直洞察。

    字段说明：
        - githubHighlights / productHighlights / paperHighlights：Phase 1/2 早期轻量格式，
          保留以兼容历史日报。
        - projectInsights / productInsights：新版完整洞察结构，优先被前端读取。

    每个子块仅在当天有匹配文章时存在，无匹配时整个子块为 null。
    """

    github_highlights: Optional[GithubBrief] = Field(
        default=None,
        alias="githubHighlights",
        description="今日项目亮点（仅当有项目类文章时，旧版轻量格式）",
    )

    product_highlights: Optional[ProductBrief] = Field(
        default=None,
        alias="productHighlights",
        description="今日产品亮点（仅当有产品类文章时，旧版轻量格式）",
    )

    paper_highlights: Optional[PaperBrief] = Field(
        default=None,
        alias="paperHighlights",
        description="今日论文亮点（仅当有论文类文章时）",
    )

    project_insights: Optional[ObjectInsightBrief] = Field(
        default=None,
        alias="projectInsights",
        description="新版项目洞察（含完整条目、来源引用、分布统计）",
    )

    product_insights: Optional[ObjectInsightBrief] = Field(
        default=None,
        alias="productInsights",
        description="新版产品洞察（含完整条目、来源引用、分布统计）",
    )

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
