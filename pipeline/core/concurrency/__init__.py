"""
pipeline/core/concurrency/__init__.py — 通用并发模块公共接口

提供：
  - TaskRunner: 通用并发任务执行器（线程池 / asyncio 双模式）
  - TaskResult: 单个任务的执行结果
  - IngestState: 线程安全的内存去重状态 + 磁盘持久化
"""

from pipeline.core.concurrency.runner import TaskResult, TaskRunner
from pipeline.core.concurrency.state import IngestState

__all__ = ["TaskRunner", "TaskResult", "IngestState"]
