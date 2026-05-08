"""
区块三：深度研判与量化分析 (Deep Analysis & Scoring)
====================================================

[核心价值]：利用 AI 的推理能力，对事件进行多维度的"价值审判"。
三维度平铺于 DailyAIInsight，Phase 2 并行处理后汇总聚合。

包含：
    - QualitativeAssessment: 定性研判（回答"这是什么事件，当下有多重要？"）
    - ValueAssessment: 价值与格局评估（回答"长期价值沉淀在哪里，竞争格局如何重塑？"）
    - ForesightAndActionability: 前瞻预测与行动转化（回答"有什么风险，我该做什么？"）
"""

from enum import Enum
from typing import List
from pydantic import BaseModel, Field


class Sentiment(str, Enum):
    """
    行业情绪倾向枚举

    与 impactScore 正交：高冲击力可以是坏消息，低冲击力可以是好消息。

    - positive: 利好 AI 行业（如技术突破、开源发布、政策松绑）
    - negative: 利空 AI 行业（如安全事故、监管收紧、关键人才流失）
    - neutral: 中性信息（如例行财报、人事变动）
    - mixed: 影响复杂 / 多空交织（如大厂开源挤压小厂但利好生态）
    """

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"


class DeveloperTone(str, Enum):
    """
    开发者情绪语气枚举

    用脚投票的开发者群体的真实反馈，而非大众媒体的表层叙事。
    开发者情绪是技术落地阻力/推力的最前置指标——
    大众觉得牛逼，但开发者可能觉得 API 太贵或协议流氓。

    - excited: 兴奋期待（对新技术/新工具的正面反应）
    - skeptical: 怀疑质疑（对宣传话术或性能声明的合理怀疑）
    - frustrated: 沮丧不满（对 API 变更、定价策略或生态锁定的抗拒）
    - neutral: 中性观望（尚无明确情绪倾向）
    """

    EXCITED = "excited"
    SKEPTICAL = "skeptical"
    FRUSTRATED = "frustrated"
    NEUTRAL = "neutral"


class HypeLevel(str, Enum):
    """
    炒作指数/水分预警枚举

    - low: 实打实的干货
    - medium: 存在一定包装
    - high: 严重的概念炒作，大屏上将打上红色预警标签
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class InformationEntropy(str, Enum):
    """
    信息熵/干货浓度枚举

    与 hypeAssessment 正交：低水分文章也可能是旧闻重发（低熵），
    高水分文章也可能有真实突破（高熵）。

    - high: 高密度新知（开创性理念、颠覆性架构、独家爆料），值得逐字精读
    - medium: 常规迭代（版本更新、功能补齐、行业研报），可快速扫读
    - low: 陈旧信息（重复解读、情绪宣泄、无实质内容），可跳过
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class EngineeringComplexity(str, Enum):
    """
    工程落地复杂度/技术成熟度枚举

    防忽悠机制。矫正市场对短期技术落地速度的盲目乐观。

    - conceptual: 概念验证阶段（白皮书、博客设想，无可用代码）
    - prototype: 实验室原型/论文代码（跑通了，但不可靠，无生产级保障）
    - production_ready: 生产级可用（SLA 有保障，可直接接入业务系统）
    - infrastructure: 泛用型基建（已成为行业标准，如 Transformer、Kubernetes）
    """

    CONCEPTUAL = "conceptual"
    PROTOTYPE = "prototype"
    PRODUCTION_READY = "production_ready"
    INFRASTRUCTURE = "infrastructure"


class ValueCaptureLayer(str, Enum):
    """
    价值捕获层枚举

    此次事件的红利最终沉淀在科技栈的哪一层？
    从底层硬件到终端应用，不同层级的利润率、壁垒高度和规模效应截然不同。

    - hardware_compute: 硬件与算力层（GPU、芯片、数据中心）—— 重资产、高壁垒
    - cloud_platform: 云平台层（AWS、Azure、GCP 等）—— 规模效应极强
    - foundation_model: 基础模型层（GPT、Claude、Llama 等）—— 技术壁垒高但开源冲击大
    - agent_middleware: 智能体与中间件层（MCP、Agent 框架、工具链）—— 生态位竞争激烈
    - end_application: 终端应用层（ChatGPT、Copilot、行业 SaaS）—— 离用户最近但护城河最浅
    """

    HARDWARE_COMPUTE = "hardware_compute"
    CLOUD_PLATFORM = "cloud_platform"
    FOUNDATION_MODEL = "foundation_model"
    AGENT_MIDDLEWARE = "agent_middleware"
    END_APPLICATION = "end_application"


class MoatImpact(str, Enum):
    """
    护城河影响枚举

    事件对行业竞争格局的重塑方向。

    - strengthens_monopoly: 加强垄断（巨头受益，小玩家被挤出——如大厂发布免费原生功能）
    - democratizes_access: 民主化（降低门槛，更多玩家入场——如高质量开源模型发布）
    - creates_new_moat: 创造新护城河（新的竞争壁垒正在形成——如新的数据飞轮或分发渠道）
    - neutral: 无明显影响（事件对竞争格局不产生实质性改变）
    """

    STRENGTHENS_MONOPOLY = "strengthens_monopoly"
    DEMOCRATIZES_ACCESS = "democratizes_access"
    CREATES_NEW_MOAT = "creates_new_moat"
    NEUTRAL = "neutral"


class ConfidenceLevel(str, Enum):
    """
    AI 研判置信度等级枚举

    标记 LLM 对自身判断的确定程度，避免"所有结论同样可信"的错觉。
    - high: 高置信度（信息源可靠、证据链完整、推理链条稳固），可直接作为决策参考
    - medium: 中等置信度（信息源基本可信但存在部分推断或信息缺口），需交叉验证后采信
    - low: 低置信度（信息源模糊、推断链路长、或领域超出 LLM 知识边界），仅作参考不可作为行动依据
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ActionableInsight(str, Enum):
    """
    可执行建议枚举

    分析做完后，读者应该做什么。此字段为分类标签，具体战略陈述见 ForesightAndActionability.marketOpportunities。
    - deep_dive: 值得深入阅读原文（高熵高冲击事件，原文有不可替代的细节和上下文）
    - monitor: 持续跟踪后续进展（事件重要但尚未尘埃落定，如早期产品发布、政策草案征求意见）
    - strategic_invest: 具备战略投资/研究方向价值（有明确的赛道机会或技能学习路径）—— 配合 marketOpportunities 使用
    - speculative_watch: 投机性关注，不确定性高（概念阶段、尚无落地路径、或炒作水分大）
    - ignore: 噪音，可跳过（无实质内容的 PR 通稿、旧闻重发、低熵低冲击）
    """

    DEEP_DIVE = "deep_dive"
    MONITOR = "monitor"
    STRATEGIC_INVEST = "strategic_invest"
    SPECULATIVE_WATCH = "speculative_watch"
    IGNORE = "ignore"


class ImpactScore(BaseModel):
    """
    短期行业冲击力评分模型

    1-3分：日常更新，小圈子自嗨
    4-7分：重要产品发布或高额融资，改变局部竞争格局
    8-10分：行业范式转移（如 ChatGPT 发布、Transformer 论文发表）
    日报 Top 5 榜单的核心排序指标。
    """

    score: float = Field(
        ...,
        ge=1,
        le=10,
        description="短期行业冲击力评分 (1-10)",
    )

    reason: str = Field(
        ...,
        description="强制 CoT：先给出评分依据，再给出评分",
    )


class DeveloperSentiment(BaseModel):
    """
    开发者/核心圈情绪反应模型

    标注什么：用脚投票的开发者群体的真实反馈，而非大众媒体的表层叙事。
    为什么用：开发者情绪是技术落地阻力/推力的最前置指标。
    与 sentiment 的区分：sentiment 判断事件对行业的客观影响方向，
    developerSentiment 捕捉核心圈的主观情绪温度。
    """

    tone: DeveloperTone = Field(
        ...,
        description="开发者情绪语气",
    )

    primary_focus: str = Field(
        ...,
        alias="primaryFocus",
        description="开发者关注或争议的焦点（如'API 定价'、'开源协议'、'性能水分'）",
    )

    class Config:
        populate_by_name = True


class HypeAssessment(BaseModel):
    """
    炒作指数/水分预警模型

    - low: 实打实的干货
    - medium: 存在一定包装
    - high: 严重的概念炒作，大屏上将打上红色预警标签
    """

    level: HypeLevel = Field(
        ...,
        description="炒作等级",
    )

    reason: str = Field(
        ...,
        description="强制 CoT：识别'颠覆'、'革命性'等 PR 滥用词汇，给出判定依据",
    )


class DomainDisruption(BaseModel):
    """
    领域破局点解析模型

    强制跨域思考，将技术"硬实力"与商业"软实力"解耦分析。
    - 即使是纯商业新闻，也需反推其背后的技术驱动力
    - 即使是纯学术论文，也需推演其潜在的商业化路径
    """

    technical_innovation: str = Field(
        ...,
        alias="technicalInnovation",
        description="技术架构或工程实现的本质突破。若是纯商业新闻，简述其背后的技术驱动力；若确实无关则填'无'",
    )

    business_model: str = Field(
        ...,
        alias="businessModel",
        description="对商业模式或 SaaS 生态的重塑力。若是纯学术论文，推演其潜在商业化路径；若确实无关则填'无'",
    )

    class Config:
        populate_by_name = True


class CompoundValue(BaseModel):
    """
    长期复利价值评分模型

    1-3分：昙花一现，无长期积累效应
    4-7分：有潜力成为细分赛道基础设施，但需持续验证
    8-10分：极强复利效应，3-5 年后大概率仍是行业基石
    设计理念：引入"价值投资"思维，打捞当前不显山露水但具备底层创新的事件。
    """

    score: float = Field(
        ...,
        ge=1,
        le=10,
        description="长期复利价值评分 (1-10)",
    )

    reason: str = Field(
        ...,
        description="强制 CoT：拒绝拍脑袋打分",
    )


class RiskMatrix(BaseModel):
    """
    风险矩阵模型

    强制 AI 从四个维度审视潜在下行风险。
    结构性维度确保不遗漏，additional 作为自由补充的安全阀。
    监管与伦理拆分：regulatory 聚焦合规与法律风险，ethical 聚焦数据伦理与社会影响。
    """

    regulatory: str = Field(
        ...,
        description="监管与合规风险（如 AI Act、出口管制、版权诉讼）",
    )

    technological: str = Field(
        ...,
        description="技术替代风险（如架构过时、论文撤回、开源替代）",
    )

    competitive: str = Field(
        ...,
        description="竞争格局风险（如巨头入场、价格战、生态挤压）",
    )

    ethical: str = Field(
        ...,
        description="数据伦理与社会影响（如偏见歧视、深度伪造、数据投毒、隐私侵犯、就业冲击）",
    )

    additional: List[str] = Field(
        default_factory=list,
        description="补充风险：非上述四类的额外风险（可选，为空数组表示无额外风险）",
    )


class Confidence(BaseModel):
    """
    AI 研判置信度模型

    标记 LLM 对自身判断的确定程度，避免"所有结论同样可信"的错觉。
    """

    impact: ConfidenceLevel = Field(
        ...,
        description="短期冲击力判断的置信度",
    )

    compound: ConfidenceLevel = Field(
        ...,
        description="长期复利判断的置信度（通常低于短期）",
    )

    hype: ConfidenceLevel = Field(
        ...,
        description="炒作判定的置信度",
    )


class QualitativeAssessment(BaseModel):
    """
    定性研判模型

    回答："这是什么事件，当下有多重要？"
    """

    impact_score: ImpactScore = Field(
        ...,
        alias="impactScore",
        description="短期行业冲击力 (1-3 个月)。日报 Top 5 榜单的核心排序指标。",
    )

    sentiment: Sentiment = Field(
        ...,
        description="行业情绪倾向。与 impactScore 正交。",
    )

    developer_sentiment: DeveloperSentiment = Field(
        ...,
        alias="developerSentiment",
        description="开发者/核心圈情绪反应。技术落地阻力/推力的最前置指标。",
    )

    hype_assessment: HypeAssessment = Field(
        ...,
        alias="hypeAssessment",
        description="炒作指数/水分预警。大屏上将打上红色预警标签。",
    )

    information_entropy: InformationEntropy = Field(
        ...,
        alias="informationEntropy",
        description="信息熵/干货浓度。与 hypeAssessment 正交。",
    )

    domain_disruption: DomainDisruption = Field(
        ...,
        alias="domainDisruption",
        description="领域破局点解析。强制跨域思考，将技术'硬实力'与商业'软实力'解耦分析。",
    )

    engineering_complexity: EngineeringComplexity = Field(
        ...,
        alias="engineeringComplexity",
        description="工程落地复杂度/技术成熟度。防忽悠机制。",
    )

    class Config:
        populate_by_name = True


class ValueAssessment(BaseModel):
    """
    价值与格局评估模型

    回答："长期价值沉淀在哪里，竞争格局如何重塑？"
    """

    compound_value: CompoundValue = Field(
        ...,
        alias="compoundValue",
        description="长期复利价值 (3-5 年)。引入'价值投资'思维。",
    )

    value_capture_layer: ValueCaptureLayer = Field(
        ...,
        alias="valueCaptureLayer",
        description="价值捕获层：此次事件的红利最终沉淀在科技栈的哪一层？",
    )

    moat_impact: MoatImpact = Field(
        ...,
        alias="moatImpact",
        description="护城河影响：事件对行业竞争格局的重塑。",
    )

    key_beneficiaries: List[str] = Field(
        ...,
        alias="keyBeneficiaries",
        description="关键受益方：此次事件中可能获益的具体公司或项目。聚焦中长期价值流动的最终受益者。",
    )

    competitive_casualty: List[str] = Field(
        ...,
        alias="competitiveCasualty",
        description="竞争波及方/受损者。风险预警的关键指标。与 keyBeneficiaries 互补：一个看赢家，一个看输家。",
    )

    class Config:
        populate_by_name = True


class ForesightAndActionability(BaseModel):
    """
    前瞻预测与行动转化模型

    回答："有什么风险，我该做什么？"
    [核心价值]：从"理解过去"转向"指导未来"，输出具有实操意义的指南。
    """

    market_opportunities: List[str] = Field(
        ...,
        alias="marketOpportunities",
        description="赛道机会与落地启发。基于该事件推演的 1-3 个具体商业变现、产品迭代或个人技能提升方向。",
    )

    risk_matrix: RiskMatrix = Field(
        ...,
        alias="riskMatrix",
        description="风险矩阵：强制从四个维度审视潜在下行风险。",
    )

    confidence: Confidence = Field(
        ...,
        description="AI 研判置信度：标记 LLM 对自身判断的确定程度。",
    )

    actionable_insight: ActionableInsight = Field(
        ...,
        alias="actionableInsight",
        description="可执行建议：分析做完后，读者应该做什么。",
    )

    class Config:
        populate_by_name = True
