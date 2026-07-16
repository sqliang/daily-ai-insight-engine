"""
pipeline/analysis/run_analysis.py — Stage 3 深度分析管道编排

功能：
    - 从 data/02_extracted/ 读取 Stage 2 输出文件
    - 对每篇文章并行调用 3 个评估 Agent
    - 将结果写入 data/03_analyzed/（保持子目录结构）
    - 分析完成后自动调用 aggregate_frontmatter()，更新 data/04_structured/ 使前端获取最新分析结果
    - 支持 dry-run、部分维度运行、并发控制等 CLI 参数
"""

import asyncio
import logging
from pathlib import Path
from typing import Optional

from ..core.config_loader import get_llm_config, get_stage_config, resolve_data_dir
from pipeline.utils.file_utils import ensure_dir

# ---------------------------------------------------------------------------
# 日志
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)

# Stage 3 回退模型（在 config.yaml 和 CLI 参数均未指定时使用）
DEFAULT_MODEL = "deepseek-v4-flash"



# =============================================================================
# 文件发现与路径计算
# =============================================================================


def discover_files(input_path: Path) -> tuple[list[Path], Path]:
    """
    发现待处理的 .md 文件并确定输入基准目录。

    基准目录统一使用 data/02_extracted/（提取根目录），确保无论传入单个文件
    还是子目录，输出路径都能正确保留 source 子目录结构（如 bensbites/02.md）。

    参数：
        input_path: 输入文件或目录路径

    返回：
        (文件路径列表, 输入基准目录)
    """
    extracted_base = resolve_data_dir("extracted")

    if input_path.is_file():
        # 单个文件：确保它在 data/02_extracted/ 下，基准目录为提取根目录
        try:
            input_path.relative_to(extracted_base)
            return [input_path], extracted_base
        except ValueError:
            # 外部文件：基准目录为其父目录
            return [input_path], input_path.parent
    else:
        files = sorted(input_path.rglob("*.md"))
        # 如果输入目录在 data/02_extracted/ 下，使用提取根目录作为基准
        # 以保留 source 子目录结构（如 bensbites/02.md, arxiv/01.md）
        try:
            input_path.relative_to(extracted_base)
            return files, extracted_base
        except ValueError:
            return files, input_path


def compute_output_base(input_path: Path, input_base_dir: Path, output_base_dir: Path) -> Path:
    """
    计算输出基准目录。

    如果输入在 data/02_extracted/ 下，输出到 data/03_analyzed/ 并保持子目录结构。
    如果输入是外部文件，输出到 data/03_analyzed/ 的根目录。

    参数：
        input_path: 输入文件路径
        input_base_dir: 输入基准目录
        output_base_dir: 默认输出基准目录

    返回：
        适用于该输入文件的输出基准目录
    """
    extracted_base = resolve_data_dir("extracted")
    try:
        input_path.relative_to(extracted_base)
        return output_base_dir
    except ValueError:
        pass
    return output_base_dir


# =============================================================================
# 主编排函数
# =============================================================================


async def run_analysis(
    *,
    input_path: Optional[Path] = None,
    concurrency: Optional[int] = None,
    stages: str = "all",
    skip_existing: bool = True,
    force: bool = False,
    dry_run: bool = False,
    model: Optional[str] = None,
) -> list:
    """
    Stage 3 深度分析管道主入口。

    流程：
        1. 加载配置（模型名、并发数、路径）
        2. 发现文件
        3. Dry run 检查
        4. 创建信号量 + 调用 run_deep_analysis_stage()
        5. 打印汇总

    参数：
        input_path: 输入文件或目录（默认 data/02_extracted/）
        concurrency: 并发文件数（默认从 config 读取，3）
        stages: 要运行的维度（"all" | "qualitative" | "value" | "foresight" | "object"）
        skip_existing: 是否跳过已分析的文件
        force: 强制重新分析（忽略 skip_existing）
        dry_run: 仅列出文件，不实际调用 LLM
        model: LLM 模型名称（默认从 config 读取）
    """
    from .deep_analysis_agent import run_deep_analysis_stage

    # --- 加载配置 ---
    analyze_config = get_stage_config("analyze") or {}
    llm_config = get_llm_config("analyze") or {}

    if model is None:
        model = llm_config.get("name", DEFAULT_MODEL)
    if concurrency is None:
        concurrency = analyze_config.get("concurrency", 3)
    if force:
        skip_existing = False

    # --- 路径解析 ---
    if input_path is None:
        input_path = resolve_data_dir("extracted")
    elif not input_path.is_absolute():
        from pipeline.utils.file_utils import get_project_root
        input_path = get_project_root() / input_path

    output_base_dir = resolve_data_dir("analyzed")

    # --- 发现文件 ---
    files, input_base_dir = discover_files(input_path)
    output_base = compute_output_base(input_path, input_base_dir, output_base_dir)

    total = len(files)
    print(f"\n发现 {total} 个 .md 文件")
    print(f"  输入基准: {input_base_dir}")
    print(f"  输出目录: {output_base}")
    print(f"  模型: {model}")
    print(f"  并发数: {concurrency}")
    print(f"  阶段: {stages}")
    print(f"  跳过已处理: {skip_existing}")

    if dry_run:
        print(f"\n>>> DRY RUN 模式，不会实际调用 LLM <<<")
        for fp in files:
            rel = fp.relative_to(input_base_dir)
            out = output_base / rel
            print(f"  {fp} → {out}")
        return []

    # --- 运行分析 ---
    print(f"\n⏳ Stage 3 (Deep Analysis): 处理 {total} 个文件...")
    ensure_dir(output_base)

    semaphore = asyncio.Semaphore(concurrency)
    results = await run_deep_analysis_stage(
        file_paths=files,
        output_base_dir=output_base,
        input_base_dir=input_base_dir,
        semaphore=semaphore,
        model=model,
        skip_existing=skip_existing,
        stages=stages,
    )

    # --- 自动聚合到 04_structured（前端渐进增强） ---
    if not dry_run and results:
        from ..aggregation.aggregate_frontmatter import aggregate_frontmatter
        synthesize_dir = resolve_data_dir("synthesize_structured")
        agg_config = get_stage_config("aggregate") or {}
        agg_lookback = agg_config.get("lookback_days", 1)
        print(f"\n{'=' * 60}")
        print(f"  自动聚合: 多阶段扫描 → 04_structured (lookback_days={agg_lookback})")
        print(f"{'=' * 60}")
        aggregate_frontmatter(
            output_dir=synthesize_dir,
            dry_run=False,
            lookback_days=agg_lookback,
        )

    # --- 汇总 ---
    _print_summary(results, stages)
    return results


def _print_summary(results: list, stages: str) -> None:
    """打印分析结果汇总。"""
    from ..core.agent import StageResult

    success = [r for r in results if isinstance(r, StageResult) and r.success and not r.skipped]
    skipped = [r for r in results if isinstance(r, StageResult) and r.skipped]
    failed = [r for r in results if isinstance(r, StageResult) and not r.success]

    total_fields = sum(len(r.fields_extracted) for r in success)

    label_map = {"qualitative": "定性研判", "value": "价值评估", "foresight": "前瞻预测", "object": "对象洞察", "all": "Deep Analysis"}
    stage_label = label_map.get(stages, stages)

    print(f"\n{'='*60}")
    print(f"  Stage 3 ({stage_label})")
    print(f"{'='*60}")
    print(f"  成功: {len(success)} 文件")
    print(f"  跳过: {len(skipped)} 文件")
    if failed:
        print(f"  失败: {len(failed)} 文件")
        for r in failed:
            logger.error("Stage 3 文件失败 path=%s error=%s", r.input_path, r.error[:120])
            print(f"    - {r.input_path}: {r.error[:120]}")
    print(f"  共提取 {total_fields} 个字段")
    print(f"\n{'='*60}")
    print(f"  分析完成")
    print(f"{'='*60}")

