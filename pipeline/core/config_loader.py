"""
配置加载工具

加载 pipeline/config.yaml 并提供按 tier、enabled 等条件过滤数据源的便捷方法。
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from .file_utils import get_project_root


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
