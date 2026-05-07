"""
区块二：事实提炼与浓缩 (Fact Extraction)
=========================================

[核心价值]：滤除修辞、情绪和废话，将非结构化长文本压缩为高密度的客观事实。

字段设计理念：
    - tldr: 极简一句话总结，列表页的扫描单位
    - objectiveSummary: 极简客观事实，详情页的阅读单位，对抗信息过载的"第一道防线"
    - eventType: 核心事件分类，构建宏观趋势大屏的基石
    - epistemicStatus: 认识论状态，区分"确凿事实"与"期货大饼"
    - entities: 核心实体拓扑，从孤立事件走向关系图谱
    - keyLogicFlow: 核心逻辑脉络，"结构化思维还原"
"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class EventType(str, Enum):
    """
    核心事件分类枚举

    将复杂的现实事件进行降维，强制归入最核心的宏观赛道。
    背后的思维维度：构建宏观趋势大屏（如饼图、柱状图）的基石。
    通过这个字段，系统可以统计出"本周资本是在投基建还是在投应用"，
    从而敏锐捕捉行业周期的切换。
    """

    INFRASTRUCTURE_UPDATE = "infrastructure_update"
    FRAMEWORK_TOOLS = "framework_tools"
    CAPITAL_MOVEMENT = "capital_movement"
    APPLICATION_LANDING = "application_landing"
    POLICY_AND_SAFETY = "policy_and_safety"


class EpistemicStatus(str, Enum):
    """
    认识论状态枚举

    这条信息的声明本质是什么？
    物理隔离"确凿事实"与"期货大饼"，聚合时赋予不同可信度权重。
    rumor 即使 impactScore 高也应降权。
    """

    VERIFIED_FACT = "verified_fact"
    PR_STATEMENT = "pr_statement"
    THEORETICAL_CLAIM = "theoretical_claim"
    RUMOR_LEAK = "rumor_leak"


class Entities(BaseModel):
    """
    核心实体拓扑模型

    提取事件中涉及的具象化节点。
    背后的思维维度："从孤立事件走向关系图谱"。
    如果 technologies 中连续三天高频出现 "MCP"，
    系统就能自动在日报中标记其为"爆发趋势词"。
    """

    companies: List[str] = Field(
        default_factory=list,
        description="涉及的核心企业或机构（如 OpenAI, 斯坦福大学）",
    )

    technologies: List[str] = Field(
        default_factory=list,
        description="涉及的核心 AI 技术名词（如 VLA, RAG, MCP, RLHF）",
    )

    key_people: List[str] = Field(
        default_factory=list,
        alias="keyPeople",
        description="核心关键人物（如 Sergey Levine, Sam Altman）",
    )

    class Config:
        populate_by_name = True


class FactExtraction(BaseModel):
    """
    事实提炼与浓缩模型

    滤除修辞、情绪和废话，将非结构化长文本压缩为高密度的客观事实。
    """

    tldr: str = Field(
        ...,
        max_length=80,
        description="极简一句话总结 (TLDR)。剔除所有修饰语，只讲核心事实。列表页的最强锚点。",
    )

    objective_summary: str = Field(
        ...,
        max_length=150,
        alias="objectiveSummary",
        description="极简客观事实。剥离一切主观形容词，只用最冷峻的语言描述 5W1H（谁、什么时候、做了什么、结果如何）。对抗信息过载的'第一道防线'。",
    )

    event_type: EventType = Field(
        ...,
        alias="eventType",
        description="核心事件分类。将复杂的现实事件进行降维，强制归入最核心的宏观赛道。",
    )

    epistemic_status: EpistemicStatus = Field(
        ...,
        alias="epistemicStatus",
        description="认识论状态。标记这条信息的声明本质，区分'确凿事实'与'期货大饼'。",
    )

    entities: Entities = Field(
        ...,
        description="核心实体拓扑。提取事件中涉及的具象化节点，构建词云和知识图谱的底层数据。",
    )

    key_logic_flow: List[str] = Field(
        ...,
        alias="keyLogicFlow",
        description="核心逻辑脉络/关键事实清单 (3-6 条)。文章骨架的 X 光片。'结构化思维还原'，将线性的长文本还原为树状或步骤状的逻辑块。",
    )

    class Config:
        populate_by_name = True
