"""
pipeline/synthesis/run_synthesis.py — Stage 4b CLI 入口

用法:
    uv run python pipeline/run.py synthesize                    运行完整合成流程
    uv run python pipeline/run.py synthesize --dry-run          显示 prompt 预估信息
    uv run python pipeline/run.py synthesize --model claude-opus-4-7  指定模型
    uv run python pipeline/run.py synthesize --max-detail 20    限制详细展示文章数

流程:
    1. 读取 data/04_structured/all_articles.json
    2. 调用 Editor-in-Chief Agent 生成日报 JSON
    3. 校验 JSON 结构
    4. 写入 daily-report.json + daily-report.md
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from .editor_in_chief_agent import run_editor_in_chief_sync
from .report_generator import validate_report, write_report_files
from ..core.file_utils import resolve_data_dir, read_json, ensure_dir

logger = logging.getLogger(__name__)


def synthesize_report(
    *,
    input_path: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    model: Optional[str] = None,
    max_detail: int = 30,
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    """
    Stage 4b 主函数：从 all_articles.json 生成日报。

    参数：
        input_path: all_articles.json 路径（默认 data/04_structured/all_articles.json）
        output_dir: 输出目录（默认 data/05_reports/）
        model: LLM 模型名称
        max_detail: user prompt 中完整展示的文章数
        dry_run: True 时仅显示 prompt 预估，不调用 LLM
        verbose: 显示详细信息

    返回：
        日报 dict
    """
    if input_path is None:
        input_path = resolve_data_dir("synthesize_structured") / "all_articles.json"
    if output_dir is None:
        output_dir = resolve_data_dir("reports")

    if not input_path.exists():
        print(f"错误: 输入文件不存在: {input_path}")
        print("请先运行 'uv run python pipeline/run.py aggregate' 生成 all_articles.json")
        sys.exit(1)

    # 预读数据
    data = read_json(input_path)
    articles = data.get("articles", [])
    total = len(articles)
    sources = data.get("sources", {})

    print(f"\n=== Stage 4b: Editor-in-Chief 合成 ===")
    print(f"  输入: {input_path}")
    print(f"  文章总数: {total}")
    print(f"  数据源: {list(sources.keys())}")
    print(f"  完整展示: 前 {min(max_detail, total)} 篇")

    if dry_run:
        from .prompts.user_prompt import build_user_prompt
        from .prompts.system_prompt import EDITOR_IN_CHIEF_SYSTEM_PROMPT

        user_prompt = build_user_prompt(articles, max_detail=max_detail)
        print(f"\n  >>> DRY RUN — 不调用 LLM <<<")
        print(f"  System prompt:  {len(EDITOR_IN_CHIEF_SYSTEM_PROMPT)} chars")
        print(f"  User prompt:    {len(user_prompt)} chars")
        print(f"  估算 tokens:    ~{len(user_prompt) // 3} tokens (rough estimate)")
        print(f"  输出目录:       {output_dir}")
        return {}

    print(f"  模型: {model or 'claude-opus-4-7 (默认)'}")
    print(f"\n  调用 Editor-in-Chief Agent...")

    report = run_editor_in_chief_sync(
        input_path,
        model=model,
        max_detail=max_detail,
    )

    # 校验
    validation = validate_report(report)
    print(f"\n  校验结果: {'通过' if validation['valid'] else '存在问题'}")
    for err in validation.get("errors", []):
        print(f"    ❌ {err}")
    for warn in validation.get("warnings", []):
        print(f"    ⚠️  {warn}")

    # 写入文件
    json_path, md_path = write_report_files(report, output_dir)
    print(f"\n  日报 JSON:  {json_path}")
    print(f"  日报 MD:    {md_path}")

    # 简易统计
    print(f"\n=== 日报摘要 ===")
    print(f"  Top 事件:   {len(report.get('topEvents', []))}")
    print(f"  深度分析:   {len(report.get('deepDives', []))}")
    print(f"  趋势判断:   {len(report.get('trendInsights', []))}")
    print(f"  风险信号:   {len(report.get('riskSignals', []))}")
    print(f"  机会信号:   {len(report.get('opportunitySignals', []))}")

    return report



