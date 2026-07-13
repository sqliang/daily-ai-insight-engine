"""
pipeline/schemas/specialized_analysis.py — 专题分析 Pydantic 模型

包含 GitHub 开源项目分析、产品分析、论文分析的输出 Schema。
每个专题分析对应一个 Stage 3 Agent persona，按 source 类型自动匹配。

Phase 1 实现 GitHubProjectAnalysis，Phase 2/3 追加 ProductAnalysis 和 PaperAnalysis。
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

from .fact_extraction import AiDetail


# =============================================================================
# GitHubProjectAnalysis 嵌套模型
# =============================================================================


class ProjectProfile(BaseModel):
    """项目画像——基础识别信息。"""

    name: str = Field(..., description="项目名称")
    url: str = Field(..., description="GitHub 仓库 URL")
    primary_language: str = Field(..., alias="primaryLanguage", description="主要编程语言")
    license: str = Field(..., description="开源协议类型")
    description: str = Field(..., description="一句话项目定位")
    created_date: Optional[str] = Field(default=None, alias="createdDate", description="项目首次创建日期")

    class Config:
        populate_by_name = True


class ProjectClassification(BaseModel):
    """
    项目分类标注——两层体系。

    第一层 domain + cross_tags：所有项目必填
    第二层 ai_detail：仅 domain == "ai_ml" 时存在
    """

    domain: str = Field(
        ...,
        description="通用技术领域。可选值见 GitHubTags.domain 注释",
    )
    cross_tags: List[str] = Field(
        default_factory=list,
        alias="crossTags",
        description="跨领域标签",
    )
    ai_detail: Optional[AiDetail] = Field(
        default=None,
        alias="aiDetail",
        description="AI 专项标注（仅 AI/ML 项目）",
    )

    class Config:
        populate_by_name = True


class CodeQualityIndicators(BaseModel):
    """代码质量信号——从仓库元数据推断。"""

    has_tests: bool = Field(..., alias="hasTests", description="是否包含测试")
    has_ci_cd: bool = Field(..., alias="hasCiCd", description="是否配置 CI/CD")
    documentation_level: str = Field(
        ...,
        alias="documentationLevel",
        description="文档质量。可选值: comprehensive, adequate, minimal, none",
    )

    class Config:
        populate_by_name = True


class TechAssessment(BaseModel):
    """技术架构评价。"""

    architecture_highlights: str = Field(
        ...,
        alias="architectureHighlights",
        description="架构亮点（如 '基于 DAG 的异步任务编排'）",
    )
    tech_stack_quality: str = Field(
        ...,
        alias="techStackQuality",
        description="技术栈质量。可选值: production_grade, promising, experimental, toy",
    )
    code_quality_indicators: CodeQualityIndicators = Field(
        ...,
        alias="codeQualityIndicators",
        description="代码质量信号",
    )
    dependencies_analysis: str = Field(
        ...,
        alias="dependenciesAnalysis",
        description="关键依赖分析",
    )

    class Config:
        populate_by_name = True


class CommunityHealth(BaseModel):
    """社区与活跃度。"""

    stars_trend: str = Field(
        ...,
        alias="starsTrend",
        description="Star 增长趋势（如 '近 30 天日均 +50'）",
    )
    contributor_activity: str = Field(
        ...,
        alias="contributorActivity",
        description="贡献者活跃度。可选值: very_active, active, moderate, low, stagnant",
    )
    issue_response_time: str = Field(
        ...,
        alias="issueResponseTime",
        description="Issue 响应速度。可选值: fast, normal, slow",
    )
    pr_merge_velocity: str = Field(
        ...,
        alias="prMergeVelocity",
        description="PR 合并速度。可选值: high, medium, low",
    )
    bus_factor_assessment: str = Field(
        ...,
        alias="busFactorAssessment",
        description="核心贡献者集中度风险",
    )

    class Config:
        populate_by_name = True


class CompetitiveLandscape(BaseModel):
    """竞品对比。"""

    direct_alternatives: List[str] = Field(
        default_factory=list,
        alias="directAlternatives",
        description="直接竞品项目名列表",
    )
    differentiation: str = Field(
        ...,
        description="与竞品的核心差异",
    )
    moat_analysis: str = Field(
        ...,
        alias="moatAnalysis",
        description="护城河分析",
    )

    class Config:
        populate_by_name = True


class AdoptionGuidance(BaseModel):
    """采用建议。"""

    maturity_score: float = Field(
        ...,
        ge=1,
        le=10,
        alias="maturityScore",
        description="综合成熟度评分 (1-10)",
    )
    recommended_for: List[str] = Field(
        default_factory=list,
        alias="recommendedFor",
        description="适用场景",
    )
    caution_for: List[str] = Field(
        default_factory=list,
        alias="cautionFor",
        description="不适用/需谨慎的场景",
    )
    time_to_production: str = Field(
        ...,
        alias="timeToProduction",
        description="生产就绪时间评估。可选值: ready_now, needs_1_3_months, needs_6_plus_months, not_recommended",
    )

    class Config:
        populate_by_name = True


class GitHubProjectAnalysis(BaseModel):
    """
    GitHub 开源项目深度分析——Stage 3 专题分析产出。

    设计理念：
        技术尽职调查——帮助决策者判断项目是否值得采用、贡献或关注。
    """

    project_profile: ProjectProfile = Field(
        ...,
        alias="projectProfile",
        description="项目画像",
    )

    project_classification: ProjectClassification = Field(
        ...,
        alias="projectClassification",
        description="项目分类标注（两层体系）",
    )

    tech_assessment: TechAssessment = Field(
        ...,
        alias="techAssessment",
        description="技术架构评价",
    )

    community_health: CommunityHealth = Field(
        ...,
        alias="communityHealth",
        description="社区与活跃度",
    )

    competitive_landscape: CompetitiveLandscape = Field(
        ...,
        alias="competitiveLandscape",
        description="竞品对比",
    )

    adoption_guidance: AdoptionGuidance = Field(
        ...,
        alias="adoptionGuidance",
        description="采用建议",
    )

    class Config:
        populate_by_name = True


# =============================================================================
# 共享枚举（PaperAnalysis 使用）
# =============================================================================


class TechnicalDepth(str, Enum):
    """技术深度枚举。"""
    DEEPLY_TECHNICAL = "deeply_technical"
    MODERATE = "moderate"
    ACCESSIBLE = "accessible"


class NoveltyType(str, Enum):
    """方法创新类型枚举。"""
    ARCHITECTURAL = "architectural"
    ALGORITHMIC = "algorithmic"
    TRAINING_METHOD = "training_method"
    DATA_CENTRIC = "data_centric"
    THEORETICAL = "theoretical"
    BENCHMARK = "benchmark"


class Significance(str, Enum):
    """研究意义枚举。"""
    FUNDAMENTAL = "fundamental"
    PRACTICAL = "practical"
    INCREMENTAL = "incremental"
    NICHE = "niche"


class BaselineComparison(str, Enum):
    """基线对比质量枚举。"""
    COMPREHENSIVE = "comprehensive"
    ADEQUATE = "adequate"
    SELECTIVE = "selective"
    WEAK = "weak"


class AblationQuality(str, Enum):
    """消融实验质量枚举。"""
    THOROUGH = "thorough"
    ADEQUATE = "adequate"
    MINIMAL = "minimal"
    ABSENT = "absent"


class ReproducibilityLevel(str, Enum):
    """可复现性枚举。"""
    FULLY = "fully_reproducible"
    MOSTLY = "mostly_reproducible"
    PARTIALLY = "partially"
    NOT = "not_reproducible"


class OverclaimingAssessment(str, Enum):
    """过度宣称评估枚举。"""
    HONEST = "honest"
    MILD = "mild_overclaim"
    SIGNIFICANT = "significant_overclaim"


class ComputeRequirements(str, Enum):
    """算力需求枚举。"""
    COMMODITY = "commodity"
    DATACENTER = "datacenter"
    SUPERCOMPUTER = "supercomputer"
    PROHIBITIVE = "prohibitive"


class IntegrationReadiness(str, Enum):
    """集成就绪度枚举。"""
    READY = "ready_to_integrate"
    NEEDS_ENGINEERING = "needs_engineering"
    NEEDS_RESEARCH = "needs_research"
    DISTANT = "distant"


# =============================================================================
# PaperAnalysis 嵌套模型
# =============================================================================


class PaperMetadata(BaseModel):
    """论文元信息。"""

    title: str = Field(..., alias="title", description="论文标题")
    authors: List[str] = Field(default_factory=list, description="作者列表")
    affiliations: List[str] = Field(default_factory=list, description="作者所属机构")
    venue: Optional[str] = Field(default=None, description="发表会议/期刊（如 NeurIPS 2025, arXiv preprint）")
    paper_url: str = Field(..., alias="paperUrl", description="论文 URL")
    code_url: Optional[str] = Field(default=None, alias="codeUrl", description="配套代码仓库 URL")
    dataset_url: Optional[str] = Field(default=None, alias="datasetUrl", description="配套数据集 URL")

    class Config:
        populate_by_name = True


class ResearchProblem(BaseModel):
    """研究问题与动机。"""

    core_question: str = Field(..., alias="coreQuestion", description="核心研究问题（一句话）")
    motivation: str = Field(..., description="研究动机与背景")
    significance: str = Field(..., description="研究意义。可选值: fundamental, practical, incremental, niche")
    gap_addressed: str = Field(..., alias="gapAddressed", description="填补了什么研究空白")

    class Config:
        populate_by_name = True


class Methodology(BaseModel):
    """方法创新。"""

    approach_summary: str = Field(..., alias="approachSummary", description="方法概述（200 字以内）")
    novelty_type: str = Field(..., alias="noveltyType", description="创新类型。可选值: architectural, algorithmic, training_method, data_centric, theoretical, benchmark")
    key_innovations: List[str] = Field(default_factory=list, alias="keyInnovations", description="关键创新点（2-4 条）")
    inspiration_sources: List[str] = Field(default_factory=list, alias="inspirationSources", description="方法的启发来源")
    technical_depth: str = Field(..., alias="technicalDepth", description="技术深度。可选值: deeply_technical, moderate, accessible")

    class Config:
        populate_by_name = True


class ExperimentalRigor(BaseModel):
    """实验与验证。"""

    benchmark_coverage: str = Field(..., alias="benchmarkCoverage", description="评测基准覆盖描述")
    baseline_comparison: str = Field(..., alias="baselineComparison", description="基线对比质量。可选值: comprehensive, adequate, selective, weak")
    ablation_quality: str = Field(..., alias="ablationQuality", description="消融实验质量。可选值: thorough, adequate, minimal, absent")
    reproducibility_level: str = Field(..., alias="reproducibilityLevel", description="可复现性。可选值: fully_reproducible, mostly_reproducible, partially, not_reproducible")
    claimed_improvement: str = Field(..., alias="claimedImprovement", description="论文声称的提升")

    class Config:
        populate_by_name = True


class LimitationsAndHonesty(BaseModel):
    """局限性与诚实度。"""

    stated_limitations: List[str] = Field(default_factory=list, alias="statedLimitations", description="论文自身承认的局限性")
    reviewer_concerns: List[str] = Field(default_factory=list, alias="reviewerConcerns", description="审稿人会提出的担忧")
    overclaiming_assessment: str = Field(..., alias="overclaimingAssessment", description="过度宣称评估。可选值: honest, mild_overclaim, significant_overclaim")
    generalization_concern: str = Field(..., alias="generalizationConcern", description="泛化性担忧")

    class Config:
        populate_by_name = True


class IndustrialRelevance(BaseModel):
    """工业落地潜力。"""

    applicable_domains: List[str] = Field(default_factory=list, alias="applicableDomains", description="可应用领域")
    compute_requirements: str = Field(..., alias="computeRequirements", description="算力需求。可选值: commodity, datacenter, supercomputer, prohibitive")
    integration_readiness: str = Field(..., alias="integrationReadiness", description="集成就绪度。可选值: ready_to_integrate, needs_engineering, needs_research, distant")
    cost_efficiency_analysis: str = Field(..., alias="costEfficiencyAnalysis", description="成本效益分析")

    class Config:
        populate_by_name = True


class RelatedWorkContext(BaseModel):
    """与相关工作的关系。"""

    closest_prior_works: List[str] = Field(default_factory=list, alias="closestPriorWorks", description="最接近的先前工作")
    advancement_over_prior: str = Field(..., alias="advancementOverPrior", description="相比之前工作的实质进步")
    opens_new_direction: bool = Field(..., alias="opensNewDirection", description="是否开辟了新方向")
    potential_follow_ups: List[str] = Field(default_factory=list, alias="potentialFollowUps", description="可能的后续研究方向")

    class Config:
        populate_by_name = True


class PaperAnalysis(BaseModel):
    """
    论文深度分析——Stage 3 专题分析产出。

    设计理念：
        学术研究评估——帮助技术团队判断论文的学术价值、技术可行性与工业落地潜力。
    """

    paper_metadata: PaperMetadata = Field(
        ...,
        alias="paperMetadata",
        description="论文元信息",
    )
    research_problem: ResearchProblem = Field(
        ...,
        alias="researchProblem",
        description="研究问题与动机",
    )
    methodology: Methodology = Field(
        ...,
        description="方法创新",
    )
    experimental_rigor: ExperimentalRigor = Field(
        ...,
        alias="experimentalRigor",
        description="实验与验证",
    )
    limitations_and_honesty: LimitationsAndHonesty = Field(
        ...,
        alias="limitationsAndHonesty",
        description="局限性与诚实度",
    )
    industrial_relevance: IndustrialRelevance = Field(
        ...,
        alias="industrialRelevance",
        description="工业落地潜力",
    )
    related_work_context: RelatedWorkContext = Field(
        ...,
        alias="relatedWorkContext",
        description="与相关工作的关系",
    )

    class Config:
        populate_by_name = True


# Phase 3 占位：ProductAnalysis 后续追加
