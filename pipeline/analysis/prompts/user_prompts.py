"""
Stage 3 Deep Analysis — User 提示词构建器

为 QualitativeAssessment、ValueAssessment、ForesightAndActionability 三个评估维度
构造包含具体文章数据的 user prompt。

每个 builder 接收 Stage 2 提取的结构化事实 + 原始正文，生成完整的 user prompt。
"""

from pipeline.utils.text_utils import truncate_at_natural_break

# 深度分析阶段正文截断长度（比 Stage 2b 的 12000 更短，因为有 Stage 2 事实摘要）
DEEP_ANALYSIS_BODY_MAX_CHARS = 6000


def _format_entities(entities: dict) -> tuple[str, str, str]:
    """格式化实体列表为用户提示文本。"""
    companies = ", ".join(entities.get("companies", [])) if entities.get("companies") else "无"
    technologies = ", ".join(entities.get("technologies", [])) if entities.get("technologies") else "无"
    key_people = ", ".join(entities.get("keyPeople", [])) if entities.get("keyPeople") else "无"
    return companies, technologies, key_people


def _format_logic_flow(key_logic_flow: list) -> str:
    """格式化关键逻辑脉络为用户提示文本。"""
    if key_logic_flow:
        return "\n".join(f"  {i+1}. {item}" for i, item in enumerate(key_logic_flow))
    return "  无"


def _truncate_body(body: str) -> str:
    """截断正文至 DEEP_ANALYSIS_BODY_MAX_CHARS，并在自然断点处截断。"""
    if len(body) <= DEEP_ANALYSIS_BODY_MAX_CHARS:
        return body
    truncated = truncate_at_natural_break(body, DEEP_ANALYSIS_BODY_MAX_CHARS)
    return truncated + "\n\n[... 正文已截断，后续内容省略 ...]"


def _build_context_block(
    title: str,
    source: str,
    source_type: str,
    tldr: str,
    objective_summary: str,
    event_type: str,
    epistemic_status: str,
    entities: dict,
    key_logic_flow: list,
) -> str:
    """构造所有 user prompt 共用的文章信息与事实摘要区块。"""
    companies, technologies, key_people = _format_entities(entities)
    logic_text = _format_logic_flow(key_logic_flow)

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
{logic_text}"""


# =============================================================================
# QualitativeAssessment user prompt
# =============================================================================


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
    """构造 QualitativeAssessment 的用户提示词。"""
    context = _build_context_block(
        title, source, source_type, tldr, objective_summary,
        event_type, epistemic_status, entities, key_logic_flow,
    )
    truncated_body = _truncate_body(body)

    return f"""{context}

## 文章正文
---
{truncated_body}
---

## 要求
请以资深 AI 技术架构师的视角，对以上事件完成 QualitativeAssessment 定性研判分析。
只返回一个 JSON 对象。"""


# =============================================================================
# ValueAssessment user prompt
# =============================================================================


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
    """构造 ValueAssessment 的用户提示词。"""
    context = _build_context_block(
        title, source, source_type, tldr, objective_summary,
        event_type, epistemic_status, entities, key_logic_flow,
    )
    truncated_body = _truncate_body(body)

    return f"""{context}

## 文章正文
---
{truncated_body}
---

## 要求
请以 VC 资本分析师的视角，对以上事件完成 ValueAssessment 价值与格局评估。
只返回一个 JSON 对象。"""


# =============================================================================
# ForesightAndActionability user prompt
# =============================================================================


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
    """构造 ForesightAndActionability 的用户提示词。"""
    context = _build_context_block(
        title, source, source_type, tldr, objective_summary,
        event_type, epistemic_status, entities, key_logic_flow,
    )
    truncated_body = _truncate_body(body)

    return f"""{context}

## 文章正文
---
{truncated_body}
---

## 要求
请以战略风控分析师的视角，对以上事件完成 ForesightAndActionability 前瞻预测与行动转化分析。
只返回一个 JSON 对象。"""


# =============================================================================
# GitHubProjectAnalysis user prompt
# =============================================================================


def build_github_project_user_prompt(
    title: str,
    source: str,
    body: str,
    specialized_tags: dict | None = None,
) -> str:
    """
    构建 GitHub 项目分析 Agent 的用户提示词。

    参数：
        title: 文章标题
        source: 数据源名（应为 "github-trending"）
        body: 文章正文（截断至 6000 字符）
        specialized_tags: Stage 2 提取的 GitHubTags（已包含分类标注）

    返回：
        格式化的用户提示词字符串
    """
    truncated_body = body if body else ""

    tags_str = "无（Stage 2 未提取到标注）"
    if specialized_tags:
        import json as _json
        tags_str = _json.dumps(specialized_tags, ensure_ascii=False, indent=2)

    return f"""## 文章信息

标题：{title}
来源：{source}

## Stage 2 分类标注（已知事实，无需重新判断）

{tags_str}

## 文章正文

{truncated_body}

## 指令

基于以上信息完成 GitHub 开源项目深度分析。注意：
1. projectClassification 中的 domain 和 aiDetail 直接引用 Stage 2 标注结果
2. 专注于需要推理判断的深度分析：技术架构评价、社区健康度、竞品格局、采用建议
3. 所有描述性文本字段用中文输出
"""
