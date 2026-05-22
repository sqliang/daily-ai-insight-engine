"""
pipeline/synthesis/report_generator.py — JSON 校验 + Markdown 报告生成

功能：
    - validate_report(): 校验 synthesis 输出的 JSON 是否包含所有必要字段
    - generate_markdown(): 将 daily report JSON 转换为人类可读的 Markdown 报告
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from pipeline.utils.file_utils import ensure_dir

# =============================================================================
# 标签映射（与前端 src/lib/report/labels.ts 保持一致）
# =============================================================================

EVENT_TYPE_LABELS = {
    "infrastructure_update": "基建更新",
    "framework_tools": "框架工具",
    "capital_movement": "资本动向",
    "application_landing": "应用落地",
    "policy_and_safety": "政策与安全",
}

SENTIMENT_LABELS = {
    "positive": "正面",
    "neutral": "中立",
    "negative": "负面",
    "mixed": "混合",
}

SEVERITY_LABELS = {
    "low": "低",
    "medium": "中",
    "high": "高",
}

DIMENSION_LABELS = {
    "technology": "技术",
    "application": "应用",
    "policy": "政策",
    "capital": "资本",
}

# =============================================================================
# 必需字段定义
# =============================================================================

_REQUIRED_TOP_KEYS = [
    "date", "generatedAt", "reportTitle", "executiveSummary",
    "dataSourceSummary", "topEvents", "deepDives", "trendInsights",
    "riskSignals", "opportunitySignals", "visualizationData",
]

_REQUIRED_EVENT_KEYS = [
    "title", "articleIds", "eventType", "impactScore", "whyItMatters", "evidence",
]

_REQUIRED_DEEPDIVE_KEYS = ["title", "background", "impact", "watchNext"]

_REQUIRED_TREND_KEYS = ["dimension", "judgment", "supportingSignals"]

_REQUIRED_SIGNAL_KEYS = ["signal", "severity", "rationale"]

_VALID_EVENT_TYPES = set(EVENT_TYPE_LABELS.keys())
_VALID_SEVERITIES = {"low", "medium", "high"}
_VALID_DIMENSIONS = {"technology", "application", "policy", "capital"}


# =============================================================================
# JSON 校验
# =============================================================================


def validate_report(report: dict) -> dict:
    """
    校验 synthesis 输出的 JSON 结构完整性。

    返回: {"valid": bool, "errors": [str], "warnings": [str]}
    """
    errors: list[str] = []
    warnings: list[str] = []

    # 顶层字段
    for key in _REQUIRED_TOP_KEYS:
        if key not in report:
            errors.append(f"缺少顶层字段: {key}")

    ds = report.get("dataSourceSummary", {})
    if isinstance(ds, dict):
        if "totalArticles" not in ds:
            errors.append("dataSourceSummary 缺少 totalArticles")
        if "sources" not in ds:
            warnings.append("dataSourceSummary 缺少 sources")

    # topEvents
    for i, event in enumerate(report.get("topEvents", [])):
        for key in _REQUIRED_EVENT_KEYS:
            if key not in event:
                errors.append(f"topEvents[{i}] 缺少字段: {key}")
        et = event.get("eventType")
        if et and et not in _VALID_EVENT_TYPES:
            errors.append(f"topEvents[{i}] 无效 eventType: {et}")

    # deepDives
    for i, dive in enumerate(report.get("deepDives", [])):
        for key in _REQUIRED_DEEPDIVE_KEYS:
            if key not in dive:
                errors.append(f"deepDives[{i}] 缺少字段: {key}")

    # trendInsights
    for i, trend in enumerate(report.get("trendInsights", [])):
        for key in _REQUIRED_TREND_KEYS:
            if key not in trend:
                errors.append(f"trendInsights[{i}] 缺少字段: {key}")
        dim = trend.get("dimension")
        if dim and dim not in _VALID_DIMENSIONS:
            errors.append(f"trendInsights[{i}] 无效 dimension: {dim}")

    # riskSignals
    for i, sig in enumerate(report.get("riskSignals", [])):
        for key in _REQUIRED_SIGNAL_KEYS:
            if key not in sig:
                errors.append(f"riskSignals[{i}] 缺少字段: {key}")
        sev = sig.get("severity")
        if sev and sev not in _VALID_SEVERITIES:
            errors.append(f"riskSignals[{i}] 无效 severity: {sev}")

    # opportunitySignals
    for i, sig in enumerate(report.get("opportunitySignals", [])):
        for key in _REQUIRED_SIGNAL_KEYS:
            if key not in sig:
                errors.append(f"opportunitySignals[{i}] 缺少字段: {key}")
        sev = sig.get("severity")
        if sev and sev not in _VALID_SEVERITIES:
            errors.append(f"opportunitySignals[{i}] 无效 severity: {sev}")

    # visualizationData
    vis = report.get("visualizationData", {})
    if isinstance(vis, dict):
        if "eventTypeDistribution" not in vis:
            errors.append("visualizationData 缺少 eventTypeDistribution")
        if "sentimentDistribution" not in vis:
            warnings.append("visualizationData 缺少 sentimentDistribution")
        if "entityFrequency" not in vis:
            warnings.append("visualizationData 缺少 entityFrequency")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


# =============================================================================
# Markdown 生成
# =============================================================================


def generate_markdown(report: dict) -> str:
    """
    将 daily report JSON 转换为可读的 Markdown 报告。

    输出结构：
        1. YAML frontmatter（标题、日期）
        2. 执行摘要
        3. 数据概览
        4. 今日 Top 事件（含支撑证据）
        5. 深度分析
        6. 趋势判断
        7. 风险提示（表格）
        8. 机会提示（表格）
        9. 信源说明
    """
    lines: list[str] = []

    # --- YAML frontmatter ---
    lines.append("---")
    lines.append(f'title: "{report.get("reportTitle", "AI 行业情报日报")}"')
    lines.append(f'date: {report.get("date", "")}')
    lines.append(f'generated: {report.get("generatedAt", "")}')
    lines.append("---")
    lines.append("")
    lines.append(f'# {report.get("reportTitle", "AI 行业情报日报")}')
    lines.append("")

    # --- Executive Summary ---
    lines.append("## 执行摘要")
    lines.append("")
    lines.append(report.get("executiveSummary", ""))
    lines.append("")

    # --- Data Overview ---
    ds = report.get("dataSourceSummary", {})
    lines.append("## 数据概览")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    lines.append(f'| 样本总量 | {ds.get("totalArticles", 0)} |')
    sources = ds.get("sources", [])
    lines.append(f'| 信源数 | {len(sources)} ({", ".join(sources)}) |')
    languages = ds.get("languages", [])
    lines.append(f'| 语言覆盖 | {", ".join(languages)} |')
    lines.append("")

    # --- Top Events ---
    lines.append("## 今日 Top 事件")
    lines.append("")
    for i, event in enumerate(report.get("topEvents", []), 1):
        lines.append(f'### #{i} {event.get("title", "")}')
        lines.append("")
        et_label = EVENT_TYPE_LABELS.get(event.get("eventType", ""), event.get("eventType", ""))
        lines.append(f'- **事件类型**: {et_label}')
        lines.append(f'- **影响力评分**: {event.get("impactScore", "?")}/10')
        lines.append(f'- **为什么重要**: {event.get("whyItMatters", "")}')
        lines.append("")
        lines.append("**支撑证据**:")
        lines.append("")
        for e in event.get("evidence", []):
            lines.append(f"- {e}")
        lines.append("")

    # --- Deep Dives ---
    lines.append("## 深度分析")
    lines.append("")
    for dive in report.get("deepDives", []):
        lines.append(f'### {dive.get("title", "")}')
        lines.append("")
        lines.append(f'**背景**: {dive.get("background", "")}')
        lines.append("")
        lines.append(f'**影响**: {dive.get("impact", "")}')
        lines.append("")
        lines.append(f'**后续关注**: {dive.get("watchNext", "")}')
        lines.append("")

    # --- Trend Insights ---
    lines.append("## 趋势判断")
    lines.append("")
    for trend in report.get("trendInsights", []):
        dim_label = DIMENSION_LABELS.get(trend.get("dimension", ""), trend.get("dimension", ""))
        lines.append(f'### {dim_label}')
        lines.append("")
        lines.append(f'**判断**: {trend.get("judgment", "")}')
        lines.append("")
        lines.append("**支撑信号**:")
        lines.append("")
        for s in trend.get("supportingSignals", []):
            lines.append(f"- {s}")
        lines.append("")

    # --- Risk Signals ---
    lines.append("## 风险提示")
    lines.append("")
    lines.append("| 严重程度 | 信号 | 判断依据 |")
    lines.append("|----------|------|----------|")
    for s in report.get("riskSignals", []):
        sev = SEVERITY_LABELS.get(s.get("severity", ""), s.get("severity", ""))
        lines.append(f'| {sev} | {s.get("signal", "")} | {s.get("rationale", "")} |')
    lines.append("")

    # --- Opportunity Signals ---
    lines.append("## 机会提示")
    lines.append("")
    lines.append("| 严重程度 | 信号 | 判断依据 |")
    lines.append("|----------|------|----------|")
    for s in report.get("opportunitySignals", []):
        sev = SEVERITY_LABELS.get(s.get("severity", ""), s.get("severity", ""))
        lines.append(f'| {sev} | {s.get("signal", "")} | {s.get("rationale", "")} |')
    lines.append("")

    # --- Data Source ---
    lines.append("## 信源说明")
    lines.append("")
    lines.append(ds.get("selectionRationale", ""))
    lines.append("")

    return "\n".join(lines)


# =============================================================================
# 文件写入
# =============================================================================


def write_report_files(
    report: dict,
    output_dir: Path,
    *,
    json_filename: str = "daily-report.json",
    md_filename: str = "daily-report.md",
) -> tuple[Path, Path]:
    """
    将 daily report 写入 JSON 和 Markdown 文件。

    参数：
        report: 日报 dict
        output_dir: 输出目录

    返回：
        (json_path, md_path)
    """
    ensure_dir(output_dir)

    json_path = output_dir / json_filename
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    md_content = generate_markdown(report)
    md_path = output_dir / md_filename
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return json_path, md_path
