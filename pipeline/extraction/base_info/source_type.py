"""
pipeline/extraction/base_info/source_type.py — source_type 推断

数据源的 source_type 来自 config.yaml 的 source.type 配置项，
与文件所在目录名（即 source name）一一对应，无需 Agent 调用。

映射关系在模块加载时构建一次，后续所有调用复用。
"""

from pathlib import Path
from typing import Optional

# 目录名 → source_type 映射表（模块加载时填充）
# 如：data/01_raw/arxiv-cs-ai/ → academic_paper
_SOURCE_TYPE_FROM_DIR: dict[str, str] = {}


def _build_source_type_map() -> None:
    """
    从 config.yaml 的数据源配置中提取 name → source.type 映射。

    以文件所在目录名（即 source name）为索引，反查配置中对应数据源的
    type 字段（与 BaseInfo.source_type 枚举值一致）。

    此映射允许 BaseInfo 提取阶段完全跳过 Agent 调用：
    所有 source_type 都可以从文件路径的父目录名推断，零成本、零延迟。
    """
    from ...core.config_loader import get_sources

    for src in get_sources(enabled_only=False):
        name = src.get("name", "")
        src_type = src.get("type", "")
        if name and src_type:
            _SOURCE_TYPE_FROM_DIR[name] = src_type


# 模块加载时构建一次
_build_source_type_map()


def infer_source_type(file_path: Path) -> Optional[str]:
    """
    从文件路径的父目录名推断 source_type。

    查找逻辑：
        1. 取文件所在父目录名（如 data/01_raw/arxiv-cs-ai/01.md → arxiv-cs-ai）
        2. 在映射表中查找对应 config 中的 type 字段
        3. 返回标准枚举值（如 academic_paper）或 None

    参数：
        file_path: 输入 .md 文件路径

    返回：
        标准 source_type 枚举值字符串，无法推断时返回 None
    """
    parent_dir = file_path.parent.name
    return _SOURCE_TYPE_FROM_DIR.get(parent_dir)
