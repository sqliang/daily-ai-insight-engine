"""
pipeline/extraction/fact_extraction_agent.py — Stage 2b: 事实提取与浓缩

功能：
    - extract_fact_extraction(): 单文件处理——读取、调用 Agent、校验、合并、写入
    - run_fact_extraction_stage(): 批量并行调度入口
    - _validate_fact_extraction(): Pydantic 模型校验 + 模糊枚举匹配回退

设计决策：
    - 所有 FactExtraction 字段都是新字段（Stage 1 不会产生这些字段）
    - 输入来自 data/02_extracted/（已由 Stage 2a 丰富了 BaseInfo），
      因此可以读到 source、title 等元信息辅助提取
    - Pydantic 校验失败时尝试模糊匹配枚举值（如 "infrastructure" → "infrastructure_update"）
    - 正文空时跳过 Agent 调用
"""

import logging
from pathlib import Path
from typing import Optional

import asyncio

from ..core.frontmatter_utils import read_frontmatter, write_frontmatter
from ..schemas.fact_extraction import (
    FactExtraction,
    EventType,
    EpistemicStatus,
    Entities,
)
from .agent import (
    AgentCallError,
    StageResult,
    call_agent_with_retry,
    parse_json_response,
)
from .prompts import (
    get_fact_extraction_system_prompt,
    build_fact_extraction_user_prompt,
)

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)


# =============================================================================
# 所有 FactExtraction 字段名（用于 skip_existing 检查）
# =============================================================================

# Pydantic 字段名列表
_FACT_EXTRACTION_FIELDS: set[str] = set(FactExtraction.model_fields.keys())


# =============================================================================
# 模糊枚举匹配
# =============================================================================

# 枚举值模糊匹配映射表
# key 为 Agent 可能返回的常见变体，value 为标准枚举值
_EVENT_TYPE_FUZZY: dict[str, str] = {
    # 基础设施变体
    "infrastructure": "infrastructure_update",
    "infra": "infrastructure_update",
    "infra_update": "infrastructure_update",
    "hardware": "infrastructure_update",
    # 框架工具变体
    "framework": "framework_tools",
    "tools": "framework_tools",
    "tool": "framework_tools",
    "oss": "framework_tools",
    "open_source": "framework_tools",
    # 资本动向变体
    "capital": "capital_movement",
    "funding": "capital_movement",
    "investment": "capital_movement",
    "acquisition": "capital_movement",
    "ipo": "capital_movement",
    # 应用落地变体
    "application": "application_landing",
    "product": "application_landing",
    "launch": "application_landing",
    "deployment": "application_landing",
    # 政策安全变体
    "policy": "policy_and_safety",
    "regulation": "policy_and_safety",
    "safety": "policy_and_safety",
    "security": "policy_and_safety",
    "governance": "policy_and_safety",
}

_EPISTEMIC_FUZZY: dict[str, str] = {
    # 已验证事实变体
    "fact": "verified_fact",
    "verified": "verified_fact",
    "confirmed": "verified_fact",
    # 公关声明变体
    "pr": "pr_statement",
    "announcement": "pr_statement",
    "press_release": "pr_statement",
    "marketing": "pr_statement",
    # 理论主张变体
    "claim": "theoretical_claim",
    "theory": "theoretical_claim",
    "hypothesis": "theoretical_claim",
    "research": "theoretical_claim",
    # 传闻变体
    "rumor": "rumor_leak",
    "leak": "rumor_leak",
    "unconfirmed": "rumor_leak",
    "speculation": "rumor_leak",
}


def _fuzzy_match_enum(value: str, mapping: dict[str, str], enum_name: str) -> Optional[str]:
    """
    模糊匹配枚举值。

    匹配策略：
        1. 直接查找映射表（小写归一化）
        2. 尝试在映射表中做子串包含匹配

    参数：
        value: Agent 返回的原始值
        mapping: 模糊匹配映射表
        enum_name: 枚举类名（仅用于日志）

    返回：
        匹配到的标准枚举值，未匹配返回 None
    """
    key = value.lower().strip()

    # 直接匹配
    if key in mapping:
        return mapping[key]

    # 子串包含匹配：检查 key 是否包含映射键或被映射键包含
    for k, v in mapping.items():
        if k in key or key in k:
            logger.info("模糊匹配 %s: '%s' → '%s' (匹配键 '%s')", enum_name, value, v, k)
            return v

    return None


# =============================================================================
# 文本截断工具
# =============================================================================

def _truncate_at_natural_break(text: str, max_len: int) -> str:
    """
    在自然断句处截断文本，避免中文句子被拦腰截断。

    三级回退策略：
        1. 强断句（。！？.!?\n）— 在 max_len 往前 30 字符范围内搜索
        2. 弱断句（；，,; ）— 在 max_len 往前 20 字符范围内搜索
        3. 硬截断 — 在 max_len 处直接截断，去掉末尾不完整的字符

    参数：
        text: 待截断的原始文本
        max_len: 目标最大字符数

    返回：
        截断后的文本（已去除首尾空白）
    """
    if len(text) <= max_len:
        return text.strip()

    truncated = text[:max_len]

    # 策略 1: 强断句 — 搜索 。！？.!?\n
    search_start = max(max_len - 30, 0)
    for cut_pos in range(max_len, search_start, -1):
        if truncated[cut_pos - 1] in "。！？.!?\n":
            return truncated[:cut_pos].strip()

    # 策略 2: 弱断句 — 搜索 ；，,;
    search_start = max(max_len - 20, 0)
    for cut_pos in range(max_len, search_start, -1):
        if truncated[cut_pos - 1] in "；，,; ":
            return truncated[:cut_pos].strip()

    # 策略 3: 硬截断
    return truncated.strip()


# =============================================================================
# 校验函数
# =============================================================================

def _validate_fact_extraction(data: dict) -> FactExtraction:
    """
    验证并构造 FactExtraction 实例。

    处理流程：
        1. 先用 Pydantic 严格校验（FactExtraction.model_validate）
        2. 如果枚举值校验失败 → 尝试模糊匹配
        3. 如果实体字段缺失 → 用空 Entities 回退
        4. 如果 keyLogicFlow 缺失 → 用空列表回退

    参数：
        data: Agent 返回的原始 JSON 字典

    返回：
        验证通过的 FactExtraction 实例

    异常：
        ValueError: 模糊匹配也失败时抛出，包含详细错误信息
    """
    from pydantic import ValidationError
    from ..schemas.fact_extraction import FactExtraction

    # --- 尝试严格校验 ---
    try:
        return FactExtraction.model_validate(data)
    except ValidationError as pydantic_err:
        # 收集校验错误
        errors = pydantic_err.errors()
        logger.warning("FactExtraction 严格校验失败: %s", errors)

        # --- 尝试修复枚举值 ---
        repaired = dict(data)  # 浅拷贝以便修改
        _already_swapped = False  # 防止重复执行交叉互换

        for error in errors:
            loc = error.get("loc", [])
            if not loc:
                continue

            field_name = loc[0]
            raw_value = data.get(field_name)

            # 修复 eventType
            if field_name in ("eventType", "event_type") and isinstance(raw_value, str):
                matched = _fuzzy_match_enum(raw_value, _EVENT_TYPE_FUZZY, "eventType")
                if matched:
                    repaired[field_name] = matched
                    logger.info("eventType 修复: '%s' → '%s'", raw_value, matched)

            # 修复 epistemicStatus
            if field_name in ("epistemicStatus", "epistemic_status") and isinstance(raw_value, str):
                matched = _fuzzy_match_enum(raw_value, _EPISTEMIC_FUZZY, "epistemicStatus")
                if matched:
                    repaired[field_name] = matched
                    logger.info("epistemicStatus 修复: '%s' → '%s'", raw_value, matched)

        # --- 检测 enum 交叉互换 (cross-enum swap) ---
        # 现象：Agent 将 eventType 和 epistemicStatus 的值填反
        # 例如 eventType="theoretical_claim"（应为 epistemicStatus 值）
        # 同时 epistemicStatus="infrastructure_update"（应为 eventType 值）
        # 此时两个值都无法通过各自枚举的模糊匹配 → 直接交换它们
        if not _already_swapped:
            evt_raw = repaired.get("eventType") or repaired.get("event_type")
            eps_raw = repaired.get("epistemicStatus") or repaired.get("epistemic_status")

            if isinstance(evt_raw, str) and isinstance(eps_raw, str):
                # 检查 evt_raw 是否更像是 epistemicStatus 值，且 eps_raw 是否更像是 eventType 值
                evt_is_eps = (
                    evt_raw in _EPISTEMIC_FUZZY
                    or _fuzzy_match_enum(evt_raw, _EPISTEMIC_FUZZY, "eventType→epistemicStatus") is not None
                    or evt_raw in EpistemicStatus.__members__
                )
                eps_is_evt = (
                    eps_raw in _EVENT_TYPE_FUZZY
                    or _fuzzy_match_enum(eps_raw, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType") is not None
                    or eps_raw in EventType.__members__
                )

                if evt_is_eps and eps_is_evt:
                    # 交叉互换：swap 两个字段的值
                    evt_matched = (
                        _fuzzy_match_enum(eps_raw, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType")
                        or eps_raw
                    )
                    eps_matched = (
                        _fuzzy_match_enum(evt_raw, _EPISTEMIC_FUZZY, "eventType→epistemicStatus")
                        or evt_raw
                    )
                    evt_key = "eventType" if "eventType" in repaired else "event_type"
                    eps_key = "epistemicStatus" if "epistemicStatus" in repaired else "epistemic_status"
                    repaired[evt_key] = evt_matched
                    repaired[eps_key] = eps_matched
                    _already_swapped = True
                    logger.info(
                        "检测到 enum 交叉互换: eventType('%s') ↔ epistemicStatus('%s') → 已交换",
                        evt_raw, eps_raw,
                    )

        # --- 单向 enum 修复 ---
        # 交叉互换检测未触发时，仍可能出现 eventType 被填成 EpistemicStatus 值
        # （如 eventType="theoretical_claim" 而 epistemicStatus 本身是合法的 EpistemicStatus 值）
        # 此时将 eventType 的值单向移动到 epistemicStatus，eventType 使用最通用的回退值
        # 注意：仅在 eventType 绝对无法匹配为 EventType 时才回退，避免误判
        if not _already_swapped:
            evt_key = "eventType" if "eventType" in repaired else "event_type"
            eps_key = "epistemicStatus" if "epistemicStatus" in repaired else "epistemic_status"

            evt_val = repaired.get(evt_key)
            eps_val = repaired.get(eps_key)

            if isinstance(evt_val, str) and isinstance(eps_val, str):
                # 检查 eventType 值是否可以匹配为 EpistemicStatus
                evt_as_eps = _fuzzy_match_enum(evt_val, _EPISTEMIC_FUZZY, "eventType→epistemicStatus")
                # 检查 eventType 值是否可以匹配为 EventType（包括严格枚举值）
                evt_as_evt = _fuzzy_match_enum(evt_val, _EVENT_TYPE_FUZZY, "eventType")
                evt_is_valid_event = (
                    evt_as_evt is not None
                    or evt_val in EventType.__members__
                )
                # 检查 epistemicStatus 值是否已经合法
                eps_as_eps = _fuzzy_match_enum(eps_val, _EPISTEMIC_FUZZY, "epistemicStatus")
                eps_is_valid_eps = (
                    eps_as_eps is not None
                    or eps_val in EpistemicStatus.__members__
                )

                # 条件：eventType 能匹配为 EpistemicStatus，但不能匹配为 EventType
                # 说明 Agent 将 epistemicStatus 值填入了 eventType 字段
                if evt_as_eps is not None and not evt_is_valid_event:
                    # 将 eventType 的值移动到 epistemicStatus
                    repaired[eps_key] = evt_as_eps
                    # eventType 回退为最通用的默认值（通常适用于学术论文）
                    repaired[evt_key] = "framework_tools"
                    logger.info(
                        "单向修复 eventType: '%s' → epistemicStatus, eventType 回退为 framework_tools",
                        evt_val,
                    )
                # 反之：epistemicStatus 能匹配为 EventType，但不能匹配为 EpistemicStatus
                elif eps_as_eps is None and not eps_is_valid_eps:
                    eps_as_evt = _fuzzy_match_enum(eps_val, _EVENT_TYPE_FUZZY, "epistemicStatus→eventType")
                    if eps_as_evt is not None:
                        repaired[evt_key] = eps_as_evt
                        repaired[eps_key] = "verified_fact"
                        logger.info(
                            "单向修复 epistemicStatus: '%s' → eventType, epistemicStatus 回退为 verified_fact",
                            eps_val,
                        )

        # --- 确保 entities 字段存在 ---
        if "entities" not in repaired or not isinstance(repaired.get("entities"), dict):
            repaired["entities"] = {"companies": [], "technologies": [], "keyPeople": []}

        # --- 确保 keyLogicFlow 存在 ---
        if "keyLogicFlow" not in repaired:
            repaired["keyLogicFlow"] = []

        # --- 截断超长文本字段（中文字符数可能超过 Pydantic max_length） ---
        # tldr: 最多 80 字符，objectiveSummary: 最多 150 字符
        # 三级回退断句策略：强断句（。！？.!?\n）→ 弱断句（；，,; ）→ 硬截断
        if "tldr" in repaired and isinstance(repaired["tldr"], str):
            if len(repaired["tldr"]) > 80:
                truncated = _truncate_at_natural_break(repaired["tldr"], 80)
                repaired["tldr"] = truncated
                logger.info("tldr 截断: %d → %d 字符",
                           len(data.get("tldr", "")), len(repaired["tldr"]))

        if "objectiveSummary" in repaired and isinstance(repaired["objectiveSummary"], str):
            if len(repaired["objectiveSummary"]) > 150:
                truncated = _truncate_at_natural_break(repaired["objectiveSummary"], 150)
                repaired["objectiveSummary"] = truncated
                logger.info("objectiveSummary 截断: %d → %d 字符",
                           len(data.get("objectiveSummary", "")), len(repaired["objectiveSummary"]))

        # --- 修复后重新校验 ---
        try:
            return FactExtraction.model_validate(repaired)
        except ValidationError as second_err:
            raise ValueError(
                f"FactExtraction 校验失败（模糊匹配后仍失败）: {second_err}"
            ) from second_err


# =============================================================================
# 单文件处理
# =============================================================================

async def extract_fact_extraction(
    input_path: Path,
    output_path: Path,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
) -> StageResult:
    """
    对单个 .md 文件执行 FactExtraction 提取。

    处理流程：
        1. read_frontmatter(input_path) → (existing_fm, body)
        2. skip_existing 检查：输出文件已存在且包含所有 FactExtraction 字段 → 跳过
        3. body 为空 → 跳过 Agent 调用
        4. 构建 prompt（包含 title、source、body）
        5. 调用 Agent → 解析 JSON → Pydantic 校验
        6. 将 FactExtraction 字段合并到 existing_fm
        7. write_frontmatter(output_path, merged_fm, body)

    参数：
        input_path: 输入 .md 文件路径（通常来自 data/02_extracted/）
        output_path: 输出 .md 文件路径（通常与 input_path 相同，原位更新）
        model: LLM 模型名称
        skip_existing: 是否跳过已提取的文件

    返回：
        StageResult 记录提取结果
    """
    input_str = str(input_path)
    output_str = str(output_path)

    # --- 读取 frontmatter ---
    try:
        existing_fm, body = read_frontmatter(input_path)
    except Exception as exc:
        logger.error("读取文件失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"读取文件失败: {exc}",
        )

    # --- 检查是否需要跳过 ---
    # id 必须存在（表明文件已通过 Stage 2a 处理），+ 所有 FactExtraction 字段完整
    if skip_existing and output_path.exists():
        try:
            out_fm, _ = read_frontmatter(output_path)
            if out_fm.get("id") and _FACT_EXTRACTION_FIELDS.issubset(set(out_fm.keys())):
                logger.info("跳过（id=%s 已提取）: %s", out_fm.get("id"), input_str)
                return StageResult(
                    input_path=input_str,
                    output_path=output_str,
                    success=True,
                    fields_extracted=[],
                    skipped=True,
                )
        except Exception:
            pass  # 输出文件损坏，继续处理

    # --- 空 body 处理 ---
    if not body.strip():
        logger.warning("正文为空，跳过 FactExtraction: %s", input_str)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=True,
            fields_extracted=[],
            skipped=True,
        )

    # --- 调用 Agent 提取 ---
    title = existing_fm.get("title", "")
    source = existing_fm.get("source", "")

    logger.info("提取 FactExtraction: %s", input_str)

    try:
        # 构建提示词
        system_prompt = get_fact_extraction_system_prompt()
        user_prompt = build_fact_extraction_user_prompt(
            title=title,
            source=source,
            body=body,
        )

        # 调用 Agent（带重试）
        response_text = await call_agent_with_retry(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_turns=3,
        )

        # 解析 JSON
        extracted_data = parse_json_response(response_text)

        # 校验并构造 FactExtraction
        fact_extraction = _validate_fact_extraction(extracted_data)

    except AgentCallError as exc:
        logger.error("Agent 调用失败 %s: %s", input_str, exc.message)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=exc.message,
        )
    except ValueError as exc:
        logger.error("解析/校验失败 %s: %s", input_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"解析/校验失败: {exc}",
        )

    # --- 合并 FactExtraction 字段到 frontmatter ---
    # 使用 alias-aware 导出，保持与 schema 一致的字段名
    fields_written: list[str] = []

    # 使用 model_dump(mode="json") 确保枚举值转为字符串，避免 PyYAML 序列化为 Python 对象
    fe_dict = fact_extraction.model_dump(mode="json", by_alias=False)

    for field_name, value in fe_dict.items():
        existing_fm[field_name] = value
        fields_written.append(field_name)

    # --- 写入输出文件 ---
    try:
        write_frontmatter(output_path, existing_fm, body)
    except Exception as exc:
        logger.error("写入输出文件失败 %s: %s", output_str, exc)
        return StageResult(
            input_path=input_str,
            output_path=output_str,
            success=False,
            error=f"写入文件失败: {exc}",
        )

    logger.info(
        "FactExtraction 提取完成: %s → %s (字段: %s)",
        input_str,
        output_str,
        ", ".join(fields_written),
    )
    return StageResult(
        input_path=input_str,
        output_path=output_str,
        success=True,
        fields_extracted=fields_written,
    )


# =============================================================================
# 批量并行调度
# =============================================================================

async def run_fact_extraction_stage(
    file_paths: list[Path],
    output_base_dir: Path,
    input_base_dir: Path,
    semaphore: asyncio.Semaphore,
    *,
    model: Optional[str] = None,
    skip_existing: bool = True,
) -> list[StageResult]:
    """
    为一批文件并行执行 FactExtraction 提取。

    并行控制：
        - 使用 asyncio.Semaphore 限制并发 Agent 调用数量
        - asyncio.gather(return_exceptions=True) 保证单个文件失败不影响其他

    注意：
        - file_paths 通常指向 data/02_extracted/ 下的文件（Stage 2a 输出）
        - 输出路径与输入路径相同（原位更新 frontmatter）

    参数：
        file_paths: 待处理的 .md 文件路径列表
        output_base_dir: 输出根目录
        input_base_dir: 输入根目录（用于计算相对路径）
        semaphore: 并发控制信号量
        model: LLM 模型名称
        skip_existing: 是否跳过已处理的文件

    返回：
        StageResult 列表
    """

    async def process_one(input_path: Path) -> StageResult:
        """处理单个文件，在 semaphore 保护下调用 Agent。"""
        # 计算输出路径：保持子目录结构
        rel_path = input_path.relative_to(input_base_dir)
        output_path = output_base_dir / rel_path

        # semaphore 控制并发数
        async with semaphore:
            return await extract_fact_extraction(
                input_path=input_path,
                output_path=output_path,
                model=model,
                skip_existing=skip_existing,
            )

    # 创建所有并发任务
    tasks = [process_one(p) for p in file_paths]

    # return_exceptions=True: 单个文件异常不中断其他文件的处理
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # 将意外异常转为 StageResult
    wrapped: list[StageResult] = []
    for i, result in enumerate(results):
        if isinstance(result, StageResult):
            wrapped.append(result)
        elif isinstance(result, BaseException):
            wrapped.append(
                StageResult(
                    input_path=str(file_paths[i]),
                    output_path="",
                    success=False,
                    error=f"未处理的异常: {result}",
                )
            )
        else:
            wrapped.append(
                StageResult(
                    input_path=str(file_paths[i]),
                    output_path="",
                    success=False,
                    error=f"未知返回类型: {type(result)}",
                )
            )

    return wrapped
