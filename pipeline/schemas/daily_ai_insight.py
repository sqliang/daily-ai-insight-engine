"""
顶层结构：DailyAIInsight
=========================

设计流程：
    Phase 1 → 提取 baseInfo + factExtraction（基础元信息 + 事实浓缩）
    Phase 2 → 并行深度分析，三维度平铺（定性研判 / 价值评估 / 前瞻行动），汇总聚合

[核心价值]:
    - 摒弃传统 RSS 的"表面事实罗列"
    - 采用"领域驱动设计 (DDD)"与"价值投资视角"
    - 将非结构化的嘈杂新闻，降维解构为：信息论状态、生态博弈、技术基元与商业护城河

适用场景：
    - 构建自动化 AI 行业雷达
    - 前端可视化大屏
    - 后续多 Agent 协同调度的核心数据契约
"""

from pydantic import BaseModel, Field

from .base_info import BaseInfo
from .fact_extraction import FactExtraction
from .deep_analysis import (
    QualitativeAssessment,
    ValueAssessment,
    ForesightAndActionability,
)


class DailyAIInsight(BaseModel):
    """
    AI 舆情分析日报核心认知模型

    顶层结构，包含两个阶段的数据提取：
        - Phase 1: 基础元信息 (baseInfo) + 事实提炼 (factExtraction)
        - Phase 2: 深度分析，三组字段平铺并行处理
            - 定性研判 (qualitativeAssessment): 当下 —— 事件本身是什么，有多重要？
            - 价值评估 (valueAssessment): 中长期 —— 价值流向哪里，格局如何重塑？
            - 前瞻行动 (foresightAndActionability): 未来 —— 有什么风险，该做什么？
    """

    base_info: BaseInfo = Field(
        ...,
        alias="baseInfo",
        description="Phase 1：基础元信息。物理溯源，支撑基础的数据查询与展示。",
    )

    fact_extraction: FactExtraction = Field(
        ...,
        alias="factExtraction",
        description="Phase 1：事实提炼与浓缩。滤除修辞、情绪和废话，将非结构化长文本压缩为高密度的客观事实。",
    )

    qualitative_assessment: QualitativeAssessment = Field(
        ...,
        alias="qualitativeAssessment",
        description="Phase 2：定性研判。当下 —— 事件本身是什么，有多重要？",
    )

    value_assessment: ValueAssessment = Field(
        ...,
        alias="valueAssessment",
        description="Phase 2：价值评估。中长期 —— 价值流向哪里，格局如何重塑？",
    )

    foresight_and_actionability: ForesightAndActionability = Field(
        ...,
        alias="foresightAndActionability",
        description="Phase 2：前瞻行动。未来 —— 有什么风险，该做什么？",
    )

    class Config:
        populate_by_name = True
