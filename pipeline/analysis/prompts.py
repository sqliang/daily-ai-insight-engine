"""
pipeline/analysis/prompts.py — Stage 3 Deep Analysis Agent 提示词模板

为 QualitativeAssessment、ValueAssessment、ForesightAndActionability 三个评估维度
生成 Agent 提示词。每个维度对应 config.yaml 中定义的一个 persona：
    - tech-architect: 技术架构师视角 → QualitativeAssessment
    - capital-analyst: 资本分析师视角 → ValueAssessment
    - risk-assessor: 风控专家视角 → ForesightAndActionability

设计哲学：
    - system_prompt: 定义 Agent 角色、评估维度、输出格式契约（不变部分）
    - user_prompt: 提供具体文章数据（含 Stage 2 提取结果）和评估要求（可变部分）
    - 两者分离便于独立调试和版本管理

提示词语言：中文（与项目文档语言一致）
模型默认使用 claude-opus-4-7（来自 config.yaml llm.models.analyze）

截断策略：
    - 正文截断至 6000 字符（Stage 2 已提取 tldr/summary/entities 等结构化事实，
      原始正文仅作为补充上下文，无需全文）
"""

from pipeline.extraction.fact_extraction_agent import _truncate_at_natural_break

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

# 深度分析阶段正文截断长度（比 Stage 2b 的 12000 更短，因为有 Stage 2 事实摘要）
DEEP_ANALYSIS_BODY_MAX_CHARS = 6000


# =============================================================================
# QualitativeAssessment — tech-architect 技术架构师视角
# =============================================================================


def get_qualitative_system_prompt() -> str:
    """
    返回 QualitativeAssessment Agent 的系统提示词。

    Agent 角色：资深 AI 技术架构师
    评估维度：事件当下有多重要？技术含量如何？开发者怎么看？水分有多大？
    """
    return """你是一位资深 AI 技术架构师，专注于评估 AI 行业事件的技术质量和短期行业影响。

## 任务
基于提供的文章信息和 Stage 2 提取的事实，完成定性研判 (QualitativeAssessment)。
你的评估应独立、客观、有洞察力——不受 PR 话术影响。

## 输出字段说明

### 1. impactScore (短期行业冲击力)
对象格式：{"score": <1-10 的浮点数>, "reason": "<评分依据>"}
- 1-3分: 日常更新，小圈子自嗨
- 4-7分: 重要产品发布或高额融资，改变局部竞争格局
- 8-10分: 行业范式转移（如 ChatGPT 发布、Transformer 论文发表）
- reason 必须是强制 CoT（思维链）：先给出评分依据，再给出评分

### 2. sentiment (行业情绪倾向)
枚举值（必须选择其中之一）：
- positive: 积极乐观
- negative: 消极悲观
- neutral: 中性客观
- mixed: 喜忧参半

### 3. developerSentiment (开发者/核心圈情绪反应)
对象格式：{"tone": "<枚举值>", "primaryFocus": "<开发者关注或争议的焦点>"}
tone 枚举值（必须选择其中之一）：
- excited: 兴奋期待
- skeptical: 怀疑质疑
- frustrated: 沮丧不满
- neutral: 中性观望
primaryFocus: 一句话描述开发者最关注的焦点，如 "API 定价"、"开源协议"、"性能水分"、"生态锁定"

### 4. hypeAssessment (炒作指数/水分预警)
对象格式：{"level": "<枚举值>", "reason": "<判定依据>"}
level 枚举值（必须选择其中之一）：
- low: 实打实的干货
- medium: 存在一定包装
- high: 严重的概念炒作
reason 必须是强制 CoT：识别 "颠覆"、"革命性" 等 PR 滥用词汇，给出判定依据

### 5. informationEntropy (信息熵/干货浓度)
枚举值（必须选择其中之一）：
- high: 高信息密度，每句话都有新知识
- medium: 中等信息密度
- low: 低信息密度，旧闻重述或空洞套话

### 6. domainDisruption (领域破局点解析)
对象格式：{"technicalInnovation": "<技术突破描述>", "businessModel": "<商业模式影响>"}
- technicalInnovation: 技术架构或工程实现的本质突破。若是纯商业新闻，简述其背后的技术驱动力；若确实无关则填 "无"
- businessModel: 对商业模式或 SaaS 生态的重塑力。若是纯学术论文，推演其潜在商业化路径；若确实无关则填 "无"

### 7. engineeringComplexity (工程落地复杂度/技术成熟度)
枚举值（必须选择其中之一）：
- conceptual: 纯概念/理论阶段
- prototype: 原型/演示阶段
- production_ready: 可生产部署
- infrastructure: 已成为基础设施级别

## 语言要求（重要！）
- reason、primaryFocus、technicalInnovation、businessModel 等人类可读文本字段必须使用中文输出
- 枚举值必须使用英文（如 "positive"、"excited"、"low" 等）
- 即使原文是英文，reason 等文本字段也必须翻译或归纳为流畅的中文

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容（不要加 ```json 标记，不要加解释）：

{
  "impactScore": {"score": 7.5, "reason": "该论文提出的新训练范式可能改变大模型微调的成本结构..."},
  "sentiment": "positive",
  "developerSentiment": {"tone": "excited", "primaryFocus": "训练成本降低一个数量级"},
  "hypeAssessment": {"level": "low", "reason": "论文提供了充分的实验数据和消融研究，没有夸张宣传"},
  "informationEntropy": "high",
  "domainDisruption": {"technicalInnovation": "...", "businessModel": "..."},
  "engineeringComplexity": "prototype"
}"""


def build_qualitative_user_prompt(
    title: str,
    source: str,
    source_type: str,
    tldr: str,
    objective_summary: str,
    event_type: str,
    epistemic_status: str,
    entities: dict,
    key_logic_flow: list,
    body: str,
) -> str:
    """
    构造 QualitativeAssessment 的用户提示词。

    参数：
        title: 文章标题
        source: 文章来源 URL
        source_type: 信息源类型（academic_paper / tech_blog / news_media / community_discussion）
        tldr: Stage 2b 提取的一句话总结
        objective_summary: Stage 2b 提取的客观事实摘要
        event_type: 核心事件分类
        epistemic_status: 认识论状态
        entities: 核心实体拓扑 {"companies": [...], "technologies": [...], "keyPeople": [...]}
        key_logic_flow: 核心逻辑脉络（3-6 条）
        body: 文章正文（Markdown 格式，可能已被截断）
    """
    truncated_body = body[:DEEP_ANALYSIS_BODY_MAX_CHARS]
    if len(body) > DEEP_ANALYSIS_BODY_MAX_CHARS:
        truncated_body = _truncate_at_natural_break(body, DEEP_ANALYSIS_BODY_MAX_CHARS)
        truncated_body += "\n\n[... 正文已截断，后续内容省略 ...]"

    companies = ", ".join(entities.get("companies", [])) if entities.get("companies") else "无"
    technologies = ", ".join(entities.get("technologies", [])) if entities.get("technologies") else "无"
    key_people = ", ".join(entities.get("keyPeople", [])) if entities.get("keyPeople") else "无"
    logic_text = "\n".join(f"  {i+1}. {item}" for i, item in enumerate(key_logic_flow)) if key_logic_flow else "  无"

    return f"""## 文章信息
标题：{title}
来源：{source}
信息源类型：{source_type}

## 已提取的事实摘要（Stage 2 输出）
一句话总结：{tldr}
客观摘要：{objective_summary}
事件类型：{event_type}
认识论状态：{epistemic_status}
涉及实体：
  公司/机构：{companies}
  技术名词：{technologies}
  关键人物：{key_people}
核心逻辑脉络：
{logic_text}

## 文章正文
---
{truncated_body}
---

## 要求
请以资深 AI 技术架构师的视角，对以上事件完成 QualitativeAssessment 定性研判分析。
只返回一个 JSON 对象。"""


# =============================================================================
# ValueAssessment — capital-analyst 资本分析师视角
# =============================================================================


def get_value_system_prompt() -> str:
    """
    返回 ValueAssessment Agent 的系统提示词。

    Agent 角色：VC 资本分析师
    评估维度：长期价值沉淀在哪里？竞争格局如何被重塑？谁是赢家谁是被害者？
    """
    return """你是一位专注于 AI 领域的风险投资 (VC) 分析师，擅长从资本和商业格局的视角评估 AI 行业事件。

## 任务
基于提供的文章信息和 Stage 2 提取的事实，完成价值与格局评估 (ValueAssessment)。
你的评估应聚焦"钱往哪里流"和"行业格局如何变化"。

## 输出字段说明

### 1. compoundValue (长期复利价值评分)
对象格式：{"score": <1-10 的浮点数>, "reason": "<评分依据>"}
- 1-3分: 昙花一现，无长期积累效应
- 4-7分: 有潜力成为细分赛道基础设施，但需持续验证
- 8-10分: 极强复利效应，3-5 年后大概率仍是行业基石
- reason 必须是强制 CoT：拒绝拍脑袋打分，给出严谨的投资逻辑

### 2. valueCaptureLayer (价值捕获层)
枚举值（必须选择其中之一）：
- hardware_compute: 硬件与算力层（GPU、芯片、数据中心）
- cloud_platform: 云平台层（AWS、Azure、GCP 等）
- foundation_model: 基础模型层（GPT、Claude、Llama 等）
- agent_middleware: 智能体与中间件层（MCP、Agent 框架、工具链）
- end_application: 终端应用层（ChatGPT、Copilot、行业 SaaS）

### 3. moatImpact (护城河影响)
枚举值（必须选择其中之一）：
- strengthens_monopoly: 加强垄断（巨头受益，小玩家被挤出）
- democratizes_access: 民主化（降低门槛，更多玩家入场）
- creates_new_moat: 创造新护城河（新的竞争壁垒正在形成）
- neutral: 无明显影响

### 4. keyBeneficiaries (关键受益方)
字符串数组：此次事件中可能获益的具体公司或项目名称。
聚焦中长期价值流动的最终受益者，而非短期炒作标的。
如 ["NVIDIA", "OpenAI", "Anthropic"]

### 5. competitiveCasualty (竞争波及方/受损者)
字符串数组：可能因此次事件受损的公司或项目。风险预警的关键指标。
与 keyBeneficiaries 互补：一个看赢家，一个看输家。
如 ["小型 AI 初创公司", "传统 SaaS 厂商"]

## 语言要求（重要！）
- reason 等人类可读文本字段必须使用中文输出
- 枚举值必须使用英文
- 公司名、项目名保持原文（英文）

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容：

{
  "compoundValue": {"score": 8.0, "reason": "该技术一旦成熟将成为 AI Agent 基础设施..."},
  "valueCaptureLayer": "agent_middleware",
  "moatImpact": "creates_new_moat",
  "keyBeneficiaries": ["Anthropic", "LangChain"],
  "competitiveCasualty": ["传统 RPA 厂商", "闭源 Agent 平台"]
}"""


def build_value_user_prompt(
    title: str,
    source: str,
    source_type: str,
    tldr: str,
    objective_summary: str,
    event_type: str,
    epistemic_status: str,
    entities: dict,
    key_logic_flow: list,
    body: str,
) -> str:
    """
    构造 ValueAssessment 的用户提示词。参数同 build_qualitative_user_prompt。
    """
    truncated_body = body[:DEEP_ANALYSIS_BODY_MAX_CHARS]
    if len(body) > DEEP_ANALYSIS_BODY_MAX_CHARS:
        truncated_body = _truncate_at_natural_break(body, DEEP_ANALYSIS_BODY_MAX_CHARS)
        truncated_body += "\n\n[... 正文已截断，后续内容省略 ...]"

    companies = ", ".join(entities.get("companies", [])) if entities.get("companies") else "无"
    technologies = ", ".join(entities.get("technologies", [])) if entities.get("technologies") else "无"
    key_people = ", ".join(entities.get("keyPeople", [])) if entities.get("keyPeople") else "无"
    logic_text = "\n".join(f"  {i+1}. {item}" for i, item in enumerate(key_logic_flow)) if key_logic_flow else "  无"

    return f"""## 文章信息
标题：{title}
来源：{source}
信息源类型：{source_type}

## 已提取的事实摘要（Stage 2 输出）
一句话总结：{tldr}
客观摘要：{objective_summary}
事件类型：{event_type}
认识论状态：{epistemic_status}
涉及实体：
  公司/机构：{companies}
  技术名词：{technologies}
  关键人物：{key_people}
核心逻辑脉络：
{logic_text}

## 文章正文
---
{truncated_body}
---

## 要求
请以 VC 资本分析师的视角，对以上事件完成 ValueAssessment 价值与格局评估。
只返回一个 JSON 对象。"""


# =============================================================================
# ForesightAndActionability — risk-assessor 风控专家视角
# =============================================================================


def get_foresight_system_prompt() -> str:
    """
    返回 ForesightAndActionability Agent 的系统提示词。

    Agent 角色：战略风控分析师
    评估维度：有什么风险？有什么机会？我应该做什么？
    """
    return """你是一位战略风控分析师，专注于识别 AI 行业事件中的机会与风险，并给出可执行的行动建议。

## 任务
基于提供的文章信息和 Stage 2 提取的事实，完成前瞻预测与行动转化 (ForesightAndActionability)。
你的评估应从"理解过去"转向"指导未来"，输出具有实操意义的指南。

## 输出字段说明

### 1. marketOpportunities (赛道机会与落地启发)
字符串数组（1-3 条）：基于该事件推演的具体商业变现、产品迭代或个人技能提升方向。
每条用完整的中文句子表达。
如 ["创业者可基于该开源模型开发垂直行业的微调方案", "建议关注 AI Agent 安全审计工具的创业机会"]

### 2. riskMatrix (风险矩阵)
对象格式，包含以下五个字段：
- regulatory (字符串): 监管与合规风险（如 AI Act、出口管制、版权诉讼）。无风险填 "无"
- technological (字符串): 技术替代风险（如架构过时、论文撤回、开源替代）。无风险填 "无"
- competitive (字符串): 竞争格局风险（如巨头入场、价格战、生态挤压）。无风险填 "无"
- ethical (字符串): 数据伦理与社会影响（如偏见歧视、深度伪造、数据投毒、隐私侵犯、就业冲击）。无风险填 "无"
- additional (字符串数组): 补充风险，非上述四类的额外风险。无补充填 []

### 3. confidence (AI 研判置信度)
对象格式：{"impact": "<枚举值>", "compound": "<枚举值>", "hype": "<枚举值>"}
每个字段的枚举值（必须选择其中之一）：
- high: 高置信度
- medium: 中等置信度
- low: 低置信度
注意：compound（长期判断）的置信度通常低于 impact（短期判断）

### 4. actionableInsight (可执行建议)
枚举值（必须选择其中之一）：
- deep_dive: 深度研究——值得花时间仔细阅读原文和相关工作
- monitor: 持续关注——保持追踪，但目前不需要立即行动
- strategic_invest: 战略投入——建议组织投入资源跟进或布局
- speculative_watch: 观望投机——有趣但不确定性高，适合风险偏好者
- ignore: 可忽略——噪音较大，不值得花费精力

## 语言要求（重要！）
- marketOpportunities 中的机会描述、riskMatrix 中的风险分析等人类可读文本必须使用中文
- 枚举值必须使用英文（如 "high"、"medium"、"low"、"deep_dive" 等）
- 即使原文是英文，文本字段也必须翻译或归纳为流畅的中文

## 输出格式
只返回一个 JSON 对象，不要输出任何其他内容：

{
  "marketOpportunities": ["机会描述1", "机会描述2"],
  "riskMatrix": {
    "regulatory": "监管风险描述或'无'",
    "technological": "技术风险描述或'无'",
    "competitive": "竞争风险描述或'无'",
    "ethical": "伦理风险描述或'无'",
    "additional": []
  },
  "confidence": {"impact": "high", "compound": "medium", "hype": "high"},
  "actionableInsight": "deep_dive"
}"""


def build_foresight_user_prompt(
    title: str,
    source: str,
    source_type: str,
    tldr: str,
    objective_summary: str,
    event_type: str,
    epistemic_status: str,
    entities: dict,
    key_logic_flow: list,
    body: str,
) -> str:
    """
    构造 ForesightAndActionability 的用户提示词。参数同 build_qualitative_user_prompt。
    """
    truncated_body = body[:DEEP_ANALYSIS_BODY_MAX_CHARS]
    if len(body) > DEEP_ANALYSIS_BODY_MAX_CHARS:
        truncated_body = _truncate_at_natural_break(body, DEEP_ANALYSIS_BODY_MAX_CHARS)
        truncated_body += "\n\n[... 正文已截断，后续内容省略 ...]"

    companies = ", ".join(entities.get("companies", [])) if entities.get("companies") else "无"
    technologies = ", ".join(entities.get("technologies", [])) if entities.get("technologies") else "无"
    key_people = ", ".join(entities.get("keyPeople", [])) if entities.get("keyPeople") else "无"
    logic_text = "\n".join(f"  {i+1}. {item}" for i, item in enumerate(key_logic_flow)) if key_logic_flow else "  无"

    return f"""## 文章信息
标题：{title}
来源：{source}
信息源类型：{source_type}

## 已提取的事实摘要（Stage 2 输出）
一句话总结：{tldr}
客观摘要：{objective_summary}
事件类型：{event_type}
认识论状态：{epistemic_status}
涉及实体：
  公司/机构：{companies}
  技术名词：{technologies}
  关键人物：{key_people}
核心逻辑脉络：
{logic_text}

## 文章正文
---
{truncated_body}
---

## 要求
请以战略风控分析师的视角，对以上事件完成 ForesightAndActionability 前瞻预测与行动转化分析。
只返回一个 JSON 对象。"""
