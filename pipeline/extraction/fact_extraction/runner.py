"""
pipeline/extraction/fact_extraction/runner.py — Stage 2b: FactExtraction 批量调度

对一批文件并行执行 FactExtraction 提取，通过 asyncio.Semaphore 控制并发。
"""

import asyncio
import logging
from pathlib import Path
from typing import Optional

from ...core.agent import StageResult
from .extractor import extract_fact_extraction

logger = logging.getLogger(__name__)


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

    参数：
        file_paths: 待处理的 .md 文件路径列表（通常指向 data/02_extracted/）
        output_base_dir: 输出根目录
        input_base_dir: 输入根目录（用于计算相对路径）
        semaphore: 并发控制信号量
        model: LLM 模型名称
        skip_existing: 是否跳过已处理的文件

    返回：
        StageResult 列表
    """

    async def process_one(input_path: Path) -> StageResult:
        rel_path = input_path.relative_to(input_base_dir)
        output_path = output_base_dir / rel_path

        async with semaphore:
            return await extract_fact_extraction(
                input_path=input_path,
                output_path=output_path,
                model=model,
                skip_existing=skip_existing,
            )

    tasks = [process_one(p) for p in file_paths]
    results = await asyncio.gather(*tasks, return_exceptions=True)

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
