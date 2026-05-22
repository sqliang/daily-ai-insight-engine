"""
配置加载工具

加载 pipeline/config.yaml 并提供按 tier、enabled 等条件过滤数据源的便捷方法。
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from pipeline.utils.file_utils import ensure_dir, get_project_root


# 缓存已加载的配置，避免重复 I/O
_config_cache: Optional[Dict[str, Any]] = None


def load_config(force_reload: bool = False) -> Dict[str, Any]:
    """加载 pipeline/config.yaml，结果缓存于内存中。"""
    global _config_cache
    if _config_cache is not None and not force_reload:
        return _config_cache

    config_path = get_project_root() / "pipeline" / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        _config_cache = yaml.safe_load(f)
    return _config_cache


def get_pipeline_config() -> Dict[str, Any]:
    """获取 pipeline 全局配置段 (name, version, data_dirs)。"""
    return load_config().get("pipeline", {})


def get_data_dirs() -> Dict[str, str]:
    """返回 pipeline.data_dirs 配置字典 (key → 相对路径字符串)。"""
    return get_pipeline_config().get("data_dirs", {})


def get_state_file_path() -> str:
    """返回 state.json 文件的相对路径（自项目根目录）。"""
    return get_pipeline_config().get("state_file", "data/state.json")


def get_sources(tier: Optional[str] = None, enabled_only: bool = True) -> List[Dict[str, Any]]:
    """
    获取数据源列表。
    tier: 可选过滤 A/B/C
    enabled_only: 是否只返回 enabled=true 的源 (默认 True)
    """
    sources = load_config().get("sources", [])
    result = []
    for s in sources:
        if enabled_only and not s.get("enabled", True):
            continue
        if tier and s.get("tier") != tier:
            continue
        result.append(s)
    return result


def get_source_by_name(name: str) -> Optional[Dict[str, Any]]:
    """按 name 精确查找单个数据源配置。"""
    for s in load_config().get("sources", []):
        if s.get("name") == name:
            return s
    return None


def get_llm_config(stage: str) -> Dict[str, Any]:
    """获取指定阶段的 LLM 配置 (extract / analyze / synthesize)。"""
    llm = load_config().get("llm", {})
    return llm.get("models", {}).get(stage, {})


def get_stage_config(stage: str) -> Dict[str, Any]:
    """获取指定阶段的参数配置 (ingest / extract / analyze / synthesize)。"""
    return load_config().get("stages", {}).get(stage, {})


def get_quotas() -> Dict[str, int]:
    """获取配额配置。"""
    return load_config().get("quotas", {})


def reload_config() -> Dict[str, Any]:
    """强制重新加载配置，清除缓存。"""
    return load_config(force_reload=True)


# ---------------------------------------------------------------------------
# 数据目录解析 — 依赖 config.yaml 的 pipeline.data_dirs
# ---------------------------------------------------------------------------

# 缓存从 config.yaml 解析的数据目录映射，避免每次调用 resolve_data_dir 都重新加载
_data_dir_mapping_cache: Optional[Dict[str, Path]] = None


def _build_data_dir_mapping(project: Path) -> Dict[str, Path]:
    """
    构建 stage_key → Path 映射。

    优先从 config.yaml 的 pipeline.data_dirs 读取路径配置，
    缺失的键回退到硬编码默认值。
    """
    # 硬编码默认值 — 当 config.yaml 不可用时作为兜底
    defaults: Dict[str, Path] = {
        "manifest":               project / "data" / "00_manifest",
        "raw":                    project / "data" / "01_raw",
        "processed":              project / "data" / "02_processed",
        "extracted":              project / "data" / "02_extracted",
        "structured":             project / "data" / "03_structured",
        "analyzed":               project / "data" / "03_analyzed",
        "synthesize_structured":  project / "data" / "04_structured",
        "reports":                project / "data" / "05_reports",
    }

    try:
        data_dirs = load_config().get("pipeline", {}).get("data_dirs", {})
        if not data_dirs:
            return defaults

        # 以 config 为准，config 中缺失的键用默认值补齐
        merged: Dict[str, Path] = {}
        for key in defaults:
            cfg_path = data_dirs.get(key)
            if cfg_path is not None:
                merged[key] = project / cfg_path.strip("/")
            else:
                merged[key] = defaults[key]
        return merged
    except Exception:
        # config.yaml 缺失或格式错误时，回退到硬编码默认值
        return defaults


def resolve_data_dir(stage_key: str) -> Path:
    """
    解析数据目录路径（从 config.yaml 的 pipeline.data_dirs 读取）。

    stage_key 可选: manifest, raw, processed, extracted, structured,
                    analyzed, synthesize_structured, reports

    返回的目录路径保证存在（不存在则自动创建）。
    """
    global _data_dir_mapping_cache
    project = get_project_root()

    if _data_dir_mapping_cache is None:
        _data_dir_mapping_cache = _build_data_dir_mapping(project)

    path = _data_dir_mapping_cache.get(stage_key)
    if path is None:
        raise ValueError(
            f"未知数据层: {stage_key}，可选值: {list(_data_dir_mapping_cache.keys())}"
        )
    ensure_dir(path)
    return path


def resolve_state_file() -> Path:
    """
    解析去重状态文件路径（从 config.yaml 的 pipeline.state_file 读取）。

    返回的父目录路径保证存在（不存在则自动创建）。

    设计理由：
        独立于 resolve_data_dir() 是因为 state.json 是一个文件而非目录，
        路径需要不同的处理逻辑（确保父目录存在而非目录本身）。
    """
    project = get_project_root()

    try:
        state_rel = load_config().get("pipeline", {}).get("state_file", "data/state.json")
        path = project / state_rel.strip("/")
        ensure_dir(path.parent)
        return path
    except Exception:
        return project / "data" / "state.json"
