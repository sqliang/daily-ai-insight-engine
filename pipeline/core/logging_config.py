"""
pipeline/core/logging_config.py — 统一日志初始化模块

在 pipeline 启动时一次性配置日志系统：
- 终端输出：brief 格式，级别由 --verbose 控制
- 文件输出：detailed 格式，写入 logs/{date}/{stage}.log，级别始终 DEBUG

使用方式：
    from pipeline.core.logging_config import init_logging
    init_logging(stage="extract", verbose=True)

设计理由：
    将分散在 3 个 stage CLI 中的 basicConfig 调用统一到一个入口，
    日志文件按日期分目录、按 stage 分文件，方便按需查看和定期清理。
"""

import logging
import logging.config
import os
from datetime import date
from pathlib import Path
from typing import Optional

import yaml

from pipeline.utils.file_utils import get_project_root

# ---------------------------------------------------------------------------
# 模块级状态 — 防止重复初始化 + 记录当前 stage
# ---------------------------------------------------------------------------
_initialized: bool = False
_current_stage: str = "pipeline"

# 各 stage 对应的 file handler 名称，用于日志文件命名
STAGE_HANDLER_MAP: dict[str, str] = {
    "scout":       "file_scout",
    "ingest":      "file_ingest",
    "backfill-ids":"file_backfill",
    "extract":     "file_extract",
    "analyze":     "file_analyze",
    "aggregate":   "file_aggregate",
    "synthesize":  "file_synthesize",
}

# 日志文件轮转配置
MAX_BYTES = 10 * 1024 * 1024    # 10 MB 单文件上限
BACKUP_COUNT = 5                 # 每个 stage 最多保留 5 个分片


# ---------------------------------------------------------------------------
# 公共 API
# ---------------------------------------------------------------------------

def init_logging(
    stage: str = "pipeline",
    verbose: bool = False,
    log_dir: Optional[Path] = None,
) -> None:
    """
    初始化日志系统（幂等 — 重复调用只更新 console level 和 file handler）。

    参数：
        stage: 当前运行的 stage 名称（决定日志文件前缀）
        verbose: True 时 console handler 显示 DEBUG 级别
        log_dir: 日志目录（默认 logs/<YYYY-MM-DD>/，可通过环境变量 AI_ENGINE_LOG_DIR 覆盖）
    """
    global _initialized, _current_stage

    # --- 确定日志目录 ---
    if log_dir is None:
        env_dir = os.environ.get("AI_ENGINE_LOG_DIR")
        if env_dir:
            log_dir = Path(env_dir)
        else:
            log_dir = get_project_root() / "logs" / date.today().isoformat()

    os.makedirs(log_dir, exist_ok=True)

    # --- 加载 YAML 配置 ---
    config_path = get_project_root() / "pipeline" / "logging_config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # --- 动态注入 file handler ---
    handler_name = STAGE_HANDLER_MAP.get(stage, "file_pipeline")
    log_file = log_dir / f"{stage}.log"

    config["handlers"][handler_name] = {
        "class": "logging.handlers.RotatingFileHandler",
        "formatter": "detailed",
        "level": "DEBUG",
        "filename": str(log_file),
        "maxBytes": MAX_BYTES,
        "backupCount": BACKUP_COUNT,
        "encoding": "utf-8",
    }

    # --- 调整 console handler 级别 ---
    config["handlers"]["console"]["level"] = "DEBUG" if verbose else "INFO"

    # --- 为 pipeline logger 附加 file handler ---
    pipeline_logger_cfg = config.setdefault("loggers", {}).setdefault("pipeline", {})
    pipeline_logger_cfg["level"] = "DEBUG"
    pipeline_logger_cfg["propagate"] = False
    existing_handlers: list[str] = pipeline_logger_cfg.get("handlers", ["console"])
    if handler_name not in existing_handlers:
        existing_handlers.append(handler_name)
    pipeline_logger_cfg["handlers"] = existing_handlers

    # --- 应用配置 ---
    logging.config.dictConfig(config)

    _initialized = True
    _current_stage = stage

    # 记录初始化信息
    logger = logging.getLogger("pipeline")
    logger.info("日志系统初始化完成 stage=%s verbose=%s file=%s", stage, verbose, log_file)


def get_current_stage() -> str:
    """返回当前 stage 名称，供需要感知上下文的模块查询。"""
    return _current_stage
