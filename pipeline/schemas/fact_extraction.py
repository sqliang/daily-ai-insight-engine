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
    - infrastructure_update: 基建演进（新模型发布、芯片算力更新、训练框架升级）—— 底层能力驱动
    - framework_tools: 框架与工具（新的 Agent 框架、开发者工具开源、API 标准）—— 开发者生态驱动
    - capital_movement: 资本动向（巨额融资、并购、财报、IPO）—— 资本流向驱动
    - application_landing: 应用落地（具体的 ToB/ToC AI 产品发布与迭代）—— 商业价值驱动
    - policy_and_safety: 政策与安全（监管、版权诉讼、安全事故、伦理争议）—— 规则边界驱动
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
    - verified_fact: 已验证事实（如 GitHub 正式开源、财报发布、产品上线、论文被顶会接收）—— 可直接作为推演起点
    - pr_statement: 公关声明（官方发声但包含包装话术、尚未交付的"期货"）—— 需剔除话术水分后采信
    - theoretical_claim: 理论主张（如 arXiv 论文 Benchmark、白皮书设想，尚未经工业界验证）—— 需关注工程落地可行性
    - rumor_leak: 坊间传闻或灰度泄露（如媒体爆料、匿名信源、融资传言）—— 需等待后续确认，聚合时降权
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


# =============================================================================
# 专题标注模型 — Stage 2 来源感知的轻量标注
# =============================================================================


class AiDetail(BaseModel):
    """
    AI 专项标注——仅当 GitHub 项目的 domain == "ai_ml" 时存在。

    为 AI/ML 领域的开源项目提供细粒度子领域分类，
    支撑前端按 AI 子领域筛选和聚合分析。
    """

    primary_categories: List[str] = Field(
        default_factory=list,
        alias="primaryCategories",
        description="AI 一级子分类（可多选）。可选值: agent_framework, llm_infra, "
                    "model_training, model_serving, rag_pipeline, prompt_engineering, "
                    "multimodal, code_gen, ai_testing, ai_observability, ai_security, "
                    "ai_ui_ux, dataset_tooling, other",
    )

    agent_subcategory: Optional[List[str]] = Field(
        default=None,
        alias="agentSubcategory",
        description="Agent 子领域（仅当 primary_categories 包含 agent_framework 时存在）。"
                    "可选值: orchestration, tool_use, memory_management, planning, "
                    "reflection, multi_modal_agent, browser_agent, coding_agent, general_framework",
    )

    tech_tags: List[str] = Field(
        default_factory=list,
        alias="techTags",
        description="AI 关键技术标签（如 RAG, vector-db, function-calling, RLHF, MoE）",
    )

    class Config:
        populate_by_name = True


class GitHubTags(BaseModel):
    """
    GitHub 项目基础标注——Stage 2 从原始文章中提取的结构化元数据。

    两层分类：
        - 第一层 domain + cross_tags：所有项目必填，支持跨领域趋势观察
        - 第二层 ai_detail：仅 domain == "ai_ml" 时存在，AI 生态内精准筛选
    """

    project_name: str = Field(
        ...,
        alias="projectName",
        description="项目名称（GitHub 仓库名，如 'crewAI/crewAI'）",
    )

    project_url: str = Field(
        ...,
        alias="projectUrl",
        description="GitHub 仓库完整 URL",
    )

    primary_language: str = Field(
        ...,
        alias="primaryLanguage",
        description="主要编程语言（如 Python, TypeScript, Rust）",
    )

    license_type: str = Field(
        ...,
        alias="licenseType",
        description="开源协议类型（如 MIT, Apache 2.0, GPLv3, 无）",
    )

    # 第一层：通用领域分类（所有项目）
    domain: str = Field(
        ...,
        description="项目所属技术领域。可选值: ai_ml, web_frontend, web_backend, "
                    "devops_infra, database_storage, programming_languages, developer_tools, "
                    "security, mobile, blockchain, data_engineering, game_development, "
                    "documentation, iot_embedded, other",
    )

    cross_tags: List[str] = Field(
        default_factory=list,
        description="跨领域标签（如 open-source-alternative, devtool, cli-tool, "
                    "api-service, self-hosted, saas）",
    )

    # 第二层：AI 专项（可选）
    ai_detail: Optional[AiDetail] = Field(
        default=None,
        alias="aiDetail",
        description="AI 专项标注。仅当 domain == 'ai_ml' 时存在",
    )

    class Config:
        populate_by_name = True


class ProductTags(BaseModel):
    """产品基础标注——Stage 2 从原始文章中提取的结构化元数据。"""

    product_name: str = Field(..., description="产品名称")
    product_url: str = Field(..., description="产品 URL")
    company_team: Optional[str] = Field(default=None, description="背后的公司/团队")
    launch_context: str = Field(..., description="发布上下文。可选值: new_launch, major_update, pivot, funding_announcement")
    pricing_model: str = Field(..., description="定价模式。可选值: freemium, subscription, usage_based, open_source, free, enterprise, unknown")
    product_category: str = Field(..., description="产品所属品类")
    target_users: List[str] = Field(default_factory=list, description="目标用户画像")


class PaperTags(BaseModel):
    """论文基础标注——Stage 2 从原始文章中提取的结构化元数据。"""

    paper_title: str = Field(..., description="论文标题")
    authors: List[str] = Field(default_factory=list, description="作者列表")
    affiliations: List[str] = Field(default_factory=list, description="作者所属机构")
    venue: Optional[str] = Field(default=None, description="发表会议/期刊")
    code_url: Optional[str] = Field(default=None, description="配套代码仓库 URL")
    dataset_url: Optional[str] = Field(default=None, description="配套数据集 URL")
    research_area: str = Field(..., description="研究领域（如 NLP, CV, RL, Systems）")
    method_type: str = Field(..., description="方法类型（如 transformer, diffusion, RL-based）")


class SpecializedTags(BaseModel):
    """
    按来源类型分派的专题标注——Stage 2 产出，Stage 3 消费。

    设计理由：
        - 来源感知：根据 source 名分派不同的子 schema
        - 降本增效：轻量级分类标注在 Stage 2（temperature 0.1）完成，
          Stage 3 专题分析直接消费标注结果，专注于深度推理
    """

    github: Optional[GitHubTags] = Field(
        default=None,
        description="GitHub 项目标注（仅 source == 'github-trending' 时填充）",
    )

    product: Optional[ProductTags] = Field(
        default=None,
        description="产品标注（仅 source 匹配产品类源时填充）",
    )

    paper: Optional[PaperTags] = Field(
        default=None,
        description="论文标注（仅 source 匹配论文学术源时填充）",
    )
