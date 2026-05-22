"""
pipeline/core/concurrency/runner.py — 通用并发任务执行器

TaskRunner 提供两种并发模式：
  - mode="thread":  使用 ThreadPoolExecutor 执行阻塞式 I/O 任务（curl、trafilatura）
  - mode="async":   使用 asyncio.Semaphore + asyncio.gather 执行异步任务（LLM SDK）

设计理由：
    将并发调度逻辑从业务代码中分离，让各 pipeline 阶段只需关注 worker 函数本身。
    Stage 2/3 已有的 ad-hoc asyncio.Semaphore 模式后续可逐步迁移至此。
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, List, Literal, Optional


@dataclass
class TaskResult:
    """单个任务的执行结果。"""
    success: bool
    result: Any = None
    error: Optional[Exception] = None
    task_index: int = -1


class TaskRunner:
    """
    通用并发任务执行器。

    使用方式：
        # 线程池模式（阻塞 I/O）
        runner = TaskRunner(concurrency=5, mode="thread")
        results = runner.run_sync(tasks, on_progress=my_callback)

        # 异步模式（async-native I/O）
        runner = TaskRunner(concurrency=3, mode="async")
        results = await runner.run_async(tasks)
    """

    def __init__(
        self,
        concurrency: int = 5,
        mode: Literal["thread", "async"] = "thread",
    ):
        self.concurrency = max(1, concurrency)
        self.mode = mode

    # ------------------------------------------------------------------
    # 同步路径（ThreadPoolExecutor）
    # ------------------------------------------------------------------

    def run_sync(
        self,
        tasks: Iterable[Callable[[], Any]],
        *,
        on_progress: Optional[Callable[[int, int, "TaskResult"], None]] = None,
    ) -> List[TaskResult]:
        """
        通过 ThreadPoolExecutor 并发执行一组可调用对象。

        参数：
            tasks: 零参数可调用对象列表（用 functools.partial 绑定参数）
            on_progress: 进度回调，签名为 (done: int, total: int, latest: TaskResult)

        返回：
            List[TaskResult]: 与输入顺序一致的结果列表

        异常处理：
            单个任务抛出异常时记录到 TaskResult.error，不影响其他任务继续执行。
        """
        task_list = list(tasks)
        if not task_list:
            return []

        results: List[Optional[TaskResult]] = [None] * len(task_list)

        with ThreadPoolExecutor(max_workers=self.concurrency) as executor:
            future_to_idx = {
                executor.submit(fn): idx
                for idx, fn in enumerate(task_list)
            }
            done_count = 0
            total = len(task_list)

            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    value = future.result()
                    results[idx] = TaskResult(success=True, result=value, task_index=idx)
                except Exception as exc:
                    results[idx] = TaskResult(success=False, error=exc, task_index=idx)

                done_count += 1
                if on_progress:
                    on_progress(done_count, total, results[idx])

        return [r for r in results if r is not None]

    # ------------------------------------------------------------------
    # 异步路径（asyncio.Semaphore）
    # ------------------------------------------------------------------

    async def run_async(
        self,
        tasks: Iterable[Callable[[], Any]],
        *,
        on_progress: Optional[Callable[[int, int, "TaskResult"], None]] = None,
    ) -> List[TaskResult]:
        """
        通过 asyncio.Semaphore 并发执行一组 async 可调用对象。

        参数：
            tasks: 零参数 async 可调用对象列表
            on_progress: 进度回调

        返回：
            List[TaskResult]: 与输入顺序一致的结果列表

        异常处理：
            单个任务抛出异常时记录到 TaskResult.error，不影响其他任务。
        """
        task_list = list(tasks)
        if not task_list:
            return []

        sem = asyncio.Semaphore(self.concurrency)
        results: List[Optional[TaskResult]] = [None] * len(task_list)
        completed = 0
        total = len(task_list)

        async def _run_one(idx: int, fn: Callable):
            nonlocal completed
            async with sem:
                try:
                    value = await fn()
                    results[idx] = TaskResult(success=True, result=value, task_index=idx)
                except Exception as exc:
                    results[idx] = TaskResult(success=False, error=exc, task_index=idx)
                completed += 1
                if on_progress:
                    on_progress(completed, total, results[idx])

        await asyncio.gather(*(_run_one(i, fn) for i, fn in enumerate(task_list)))
        return [r for r in results if r is not None]
