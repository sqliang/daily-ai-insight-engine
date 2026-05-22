"""
pipeline/extraction/run_extraction.py — Stage 2 编排入口

职责：
    - 文件发现：识别 .md 文件或目录下的所有 .md 文件
    - 编排调度：先执行 Stage 2a (BaseInfo)，全部完成后再执行 Stage 2b (FactExtraction)
    - 结果汇总：打印每个阶段和每个文件的结果摘要
    - CLI 入口：提供 argparse 子命令，支持各种参数组合

并行策略：
    - 阶段间串行（Stage 2a 全部完成 → Stage 2b 开始），避免写冲突
    - 阶段内并行（asyncio.Semaphore 控制并发数），充分利用 API 配额

用法示例：
    # 处理所有文件
    uv run python pipeline/run.py extract

    # 处理单个文件
    uv run python pipeline/run.py extract --input data/01_raw/arxiv/01.md

    # 只运行 BaseInfo
    uv run python pipeline/run.py extract --stage base_info

    # 干跑（列出文件，不调用 LLM）
    uv run python pipeline/run.py extract --dry-run
"""

import logging
import sys
from pathlib import Path
from typing import Optional

import asyncio

from ..core.file_utils import get_project_root, resolve_data_dir, ensure_dir, list_files
from ..core.config_loader import get_llm_config, get_stage_config
from .base_info_agent import run_base_info_stage
from .fact_extraction_agent import run_fact_extraction_stage
from ..core.agent import StageResult

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)


# =============================================================================
# 文件发现
# =============================================================================

def discover_files(input_path: Path) -> tuple[list[Path], Path]:
    """
    发现待处理的 .md 文件。

    处理逻辑：
        - 如果 input_path 是 .md 文件 → 返回 [input_path]
        - 如果 input_path 是目录 → 递归查找所有 .md 文件
        - 基准目录自动判定：若在 data/01_raw/ 下，以 raw 根为基准
          以保留子目录结构 (如 bensbites/01.md → data/02_extracted/bensbites/01.md)
        - 如果 input_path 不存在 → 抛出 FileNotFoundError

    返回:
        (文件路径列表, 输入基准目录)
    """
    if not input_path.exists():
        raise FileNotFoundError(f"输入路径不存在: {input_path}")

    # 获取 raw 基准目录用于路径对齐
    raw_base_dir = resolve_data_dir("raw")

    if input_path.is_file():
        if input_path.suffix != ".md":
            raise ValueError(f"输入文件不是 .md 文件: {input_path}")
        # 单文件模式：尝试确定文件在 raw 目录下的路径结构
        try:
            # 如果文件在 raw 目录下，以 raw 为基准保留子目录
            input_path.relative_to(raw_base_dir)
            base_dir = raw_base_dir
        except ValueError:
            # 文件不在 raw 目录下，基准目录设为文件所在目录
            base_dir = input_path.parent
        return [input_path], base_dir

    # 目录模式：递归查找所有 .md 文件
    files = sorted(input_path.rglob("*.md"))

    # 判定基准目录：如果输入目录在 raw 之下，以 raw 为基准保留子目录结构
    try:
        input_path.relative_to(raw_base_dir)
        base_dir = raw_base_dir
    except ValueError:
        # 输入目录不在 raw 下，沿用 input_path 自身作为基准
        base_dir = input_path

    return files, base_dir


# =============================================================================
# 路径计算
# =============================================================================

def compute_output_base(input_dir: Path, raw_base_dir: Path, extracted_base_dir: Path) -> tuple[Path, Path]:
    """
    计算输出基准目录和输入基准目录。

    当用户指定了非默认输入目录时，保持相对路径结构映射到输出目录。

    参数：
        input_dir: 用户指定的输入目录或文件的父目录
        raw_base_dir: 默认原始数据根目录（data/01_raw/）
        extracted_base_dir: 输出根目录（data/02_extracted/）

    返回：
        (input_base_dir, output_base_dir) 用于路径计算的基准目录对
    """
    # 如果输入目录已经是 extracted_base_dir 的子路径，保持输入基准
    # 否则使用 raw_base_dir 作为输入基准
    try:
        input_dir.relative_to(raw_base_dir)
        input_base = raw_base_dir
    except ValueError:
        # 输入不在 raw_base_dir 下，沿用 input_dir 自身作为基准
        input_base = input_dir

    # 输出基准始终是 extracted_base_dir
    return input_base, extracted_base_dir


# =============================================================================
# 结果汇总
# =============================================================================

def print_stage_summary(stage_name: str, results: list[StageResult]) -> None:
    """
    打印阶段执行结果摘要。

    输出格式：
        === Stage 2a (BaseInfo) ===
          成功: 30 文件
          跳过: 2 文件
          失败: 1 文件
            - data/01_raw/tldrai/05.md: Agent 调用失败

    参数：
        stage_name: 阶段名称（用于标题）
        results: StageResult 列表
    """
    success = [r for r in results if r.success and not r.skipped]
    skipped = [r for r in results if r.skipped]
    failed = [r for r in results if not r.success]

    print(f"\n{'=' * 60}")
    print(f"  Stage {stage_name}")
    print(f"{'=' * 60}")
    print(f"  成功: {len(success)} 文件")
    if skipped:
        print(f"  跳过: {len(skipped)} 文件")
    if failed:
        print(f"  失败: {len(failed)} 文件")
        for r in failed:
            print(f"    - {r.input_path}: {r.error}")

    # 打印成功提取的字段详情（仅在 verbose 模式下或调试时）
    if success:
        total_fields = sum(len(r.fields_extracted) for r in success)
        print(f"  共提取 {total_fields} 个字段")


# =============================================================================
# 主编排函数
# =============================================================================

async def run_extraction(
    *,
    input_path: Optional[Path] = None,
    concurrency: Optional[int] = None,
    stages: str = "all",
    skip_existing: bool = True,
    force: bool = False,
    dry_run: bool = False,
    model: Optional[str] = None,
) -> dict:
    """
    Stage 2 提取流水线主编排函数。

    执行流程：
        1. 加载配置（LLM 模型、并发数、路径）
        2. 发现文件
        3. 如果 dry_run → 只打印文件列表，不执行
        4. Stage 2a: 全部文件并行执行 BaseInfo 提取
        5. 等待 Stage 2a 全部完成
        6. Stage 2b: 在 Stage 2a 输出文件上并行执行 FactExtraction
        7. 打印结果摘要

    参数：
        input_path: 输入文件或目录路径（None 时使用 config.yaml 中的配置）
        concurrency: 并发 Agent 调用数（None 时从 config.yaml 读取）
        stages: 执行的阶段 ("all" | "base_info" | "fact_extraction")
        skip_existing: 是否跳过已有字段的文件
        force: 强制重新提取（忽略 skip_existing）
        dry_run: 只列出文件，不调用 LLM
        model: LLM 模型名称（None 时从 config.yaml 读取）

    返回：
        结果统计字典: {"base_info": [StageResult], "fact_extraction": [StageResult]}
    """
    # --- 加载配置 ---
    project_root = get_project_root()
    llm_config = get_llm_config("extract")
    stage_config = get_stage_config("extract")

    # 模型
    effective_model = model or llm_config.get("name", "claude-sonnet-4-6")

    # 并发数优先级: CLI args > config > 默认 5
    if concurrency is None:
        rate_limit = get_llm_config("extract").get("rate_limit", {})
        # rate_limit 在 config.yaml 的 llm 段下
        from ..core.config_loader import load_config
        full_config = load_config()
        concurrency = full_config.get("llm", {}).get("rate_limit", {}).get("concurrent_requests", 5)

    # 输入路径
    raw_base_dir = resolve_data_dir("raw")
    extracted_base_dir = resolve_data_dir("extracted")

    if input_path is None:
        # 优先从 per-stage config 读取，回退到 data_dirs.raw
        input_dir_str = stage_config.get("input_dir")
        if input_dir_str:
            input_path = project_root / input_dir_str
        else:
            input_path = resolve_data_dir("raw")

    # --- 发现文件 ---
    file_paths, input_base_dir = discover_files(input_path)

    if not file_paths:
        print(f"未找到任何 .md 文件: {input_path}")
        return {}

    # 计算输出基准
    output_base_dir = extracted_base_dir

    print(f"\n发现 {len(file_paths)} 个 .md 文件")
    print(f"  输入基准: {input_base_dir}")
    print(f"  输出目录: {output_base_dir}")
    print(f"  模型: {effective_model}")
    print(f"  并发数: {concurrency}")
    print(f"  阶段: {stages}")
    print(f"  跳过已处理: {skip_existing and not force}")

    # --- Dry run 模式 ---
    if dry_run:
        print("\n将处理的文件:")
        for fp in file_paths:
            rel_path = fp.relative_to(input_base_dir)
            out_path = output_base_dir / rel_path
            print(f"  {fp} → {out_path}")
        return {}

    # --- 执行提取 ---
    semaphore = asyncio.Semaphore(concurrency)
    results: dict[str, list[StageResult]] = {}

    run_2a = stages in ("all", "base_info")
    run_2b = stages in ("all", "fact_extraction")

    # ===== Stage 2a: BaseInfo =====
    if run_2a:
        print(f"\n⏳ Stage 2a (BaseInfo): 处理 {len(file_paths)} 个文件...")
        results_2a = await run_base_info_stage(
            file_paths=file_paths,
            output_base_dir=output_base_dir,
            input_base_dir=input_base_dir,
            semaphore=semaphore,
            model=effective_model,
            skip_existing=not force and skip_existing,
        )
        results["base_info"] = results_2a
        print_stage_summary("2a (BaseInfo)", results_2a)

        # 构建 Stage 2b 的输入文件列表（仅处理成功的文件）
        stage_2b_inputs = [
            output_base_dir / fp.relative_to(input_base_dir)
            for fp, r in zip(file_paths, results_2a)
            if r.success
        ]
        stage_2b_input_base = output_base_dir
    else:
        # 不运行 Stage 2a: Stage 2b 读取 output_base_dir 下的已有文件
        stage_2b_inputs = [
            output_base_dir / fp.relative_to(input_base_dir)
            for fp in file_paths
        ]
        stage_2b_input_base = output_base_dir

    # ===== Stage 2b: FactExtraction =====
    if run_2b:
        print(f"\n⏳ Stage 2b (FactExtraction): 处理 {len(stage_2b_inputs)} 个文件...")
        results_2b = await run_fact_extraction_stage(
            file_paths=stage_2b_inputs,
            output_base_dir=output_base_dir,
            input_base_dir=stage_2b_input_base,
            semaphore=semaphore,
            model=effective_model,
            skip_existing=not force and skip_existing,
        )
        results["fact_extraction"] = results_2b
        print_stage_summary("2b (FactExtraction)", results_2b)

    # --- 最终汇总 ---
    print(f"\n{'=' * 60}")
    print("  提取完成")
    print(f"{'=' * 60}")

    return results


