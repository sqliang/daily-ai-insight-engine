"""
pipeline/schemas/specialized_analysis.py — 专题分析 Pydantic 模型

包含 GitHub 开源项目分析、产品分析、论文分析的输出 Schema。
每个专题分析对应一个 Stage 3 Agent persona，按 source 类型自动匹配。

Phase 1 实现 GitHubProjectAnalysis，Phase 2/3 追加 ProductAnalysis 和 PaperAnalysis。
"""

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
    primary_language: str = Field(..., description="主要编程语言")
    license: str = Field(..., description="开源协议类型")
    description: str = Field(..., description="一句话项目定位")
    created_date: Optional[str] = Field(default=None, description="项目首次创建日期")


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
        description="跨领域标签",
    )
    ai_detail: Optional[AiDetail] = Field(
        default=None,
        description="AI 专项标注（仅 AI/ML 项目）",
    )


class CodeQualityIndicators(BaseModel):
    """代码质量信号——从仓库元数据推断。"""

    has_tests: bool = Field(..., description="是否包含测试")
    has_ci_cd: bool = Field(..., description="是否配置 CI/CD")
    documentation_level: str = Field(
        ...,
        description="文档质量。可选值: comprehensive, adequate, minimal, none",
    )


class TechAssessment(BaseModel):
    """技术架构评价。"""

    architecture_highlights: str = Field(
        ...,
        description="架构亮点（如 '基于 DAG 的异步任务编排'）",
    )
    tech_stack_quality: str = Field(
        ...,
        description="技术栈质量。可选值: production_grade, promising, experimental, toy",
    )
    code_quality_indicators: CodeQualityIndicators = Field(
        ...,
        description="代码质量信号",
    )
    dependencies_analysis: str = Field(
        ...,
        description="关键依赖分析",
    )


class CommunityHealth(BaseModel):
    """社区与活跃度。"""

    stars_trend: str = Field(
        ...,
        description="Star 增长趋势（如 '近 30 天日均 +50'）",
    )
    contributor_activity: str = Field(
        ...,
        description="贡献者活跃度。可选值: very_active, active, moderate, low, stagnant",
    )
    issue_response_time: str = Field(
        ...,
        description="Issue 响应速度。可选值: fast, normal, slow",
    )
    pr_merge_velocity: str = Field(
        ...,
        description="PR 合并速度。可选值: high, medium, low",
    )
    bus_factor_assessment: str = Field(
        ...,
        description="核心贡献者集中度风险",
    )


class CompetitiveLandscape(BaseModel):
    """竞品对比。"""

    direct_alternatives: List[str] = Field(
        default_factory=list,
        description="直接竞品项目名列表",
    )
    differentiation: str = Field(
        ...,
        description="与竞品的核心差异",
    )
    moat_analysis: str = Field(
        ...,
        description="护城河分析",
    )


class AdoptionGuidance(BaseModel):
    """采用建议。"""

    maturity_score: float = Field(
        ...,
        ge=1,
        le=10,
        description="综合成熟度评分 (1-10)",
    )
    recommended_for: List[str] = Field(
        default_factory=list,
        description="适用场景",
    )
    caution_for: List[str] = Field(
        default_factory=list,
        description="不适用/需谨慎的场景",
    )
    time_to_production: str = Field(
        ...,
        description="生产就绪时间评估。可选值: ready_now, needs_1_3_months, needs_6_plus_months, not_recommended",
    )


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


# Phase 2/3 占位：ProductAnalysis, PaperAnalysis 后续追加
