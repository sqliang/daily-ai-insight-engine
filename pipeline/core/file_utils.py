"""
文件操作工具库

提供：项目根目录解析、目录创建、原子写入、JSON 读写等通用文件操作。
原子写入模式参考 knowledge-scout 项目，用于防止写入中断导致文件损坏。
"""

import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

# 缓存从 config.yaml 解析的数据目录映射，避免每次调用 resolve_data_dir 都重新加载
_data_dir_mapping_cache: Optional[Dict[str, Path]] = None

def get_project_root() -> Path:
    """从当前文件位置向上推导项目根目录 (daily-ai-insight-engine/)。"""
    return Path(__file__).resolve().parent.parent.parent


def ensure_dir(path: Path) -> Path:
    """递归创建目录 (等效于 mkdir -p)，返回创建的路径。"""
    path.mkdir(parents=True, exist_ok=True)
    return path


def atomic_write(filepath: Path, content: str) -> None:
    """
    原子写入文件：先写临时文件，再 rename 到目标路径。
    防止写入过程中进程崩溃导致目标文件损坏。
    """
    ensure_dir(filepath.parent)
    fd, tmp_path = tempfile.mkstemp(
        suffix=".tmp", prefix=filepath.name + ".", dir=filepath.parent
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        shutil.move(tmp_path, filepath)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


def read_json(filepath: Path) -> Any:
    """读取 JSON 文件，返回解析后的对象。文件不存在时返回 None。"""
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filepath: Path, data: Any, indent: int = 2) -> None:
    """将数据写入 JSON 文件 (非原子写入，适用于轻量级数据文件)。"""
    ensure_dir(filepath.parent)
    content = json.dumps(data, ensure_ascii=False, indent=indent)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def list_files(directory: Path, pattern: str = "*") -> List[Path]:
    """列出目录下匹配 glob 模式的文件路径列表。"""
    if not directory.exists():
        return []
    return sorted(directory.glob(pattern))


def get_next_sequence_number(target_dir: Path) -> int:
    """获取目标目录下已有文件的最大序号 + 1，用于生成连续文件名如 01.md, 02.md。"""
    existing = list_files(target_dir, "*.md")
    max_num = 0
    for p in existing:
        try:
            num = int(p.stem)
            if num > max_num:
                max_num = num
        except ValueError:
            continue
    return max_num + 1


def _build_data_dir_mapping(project: Path) -> Dict[str, Path]:
    """
    构建 stage_key → Path 映射。

    优先从 config.yaml 的 pipeline.data_dirs 读取路径配置，
    缺失的键回退到硬编码默认值。使用延迟导入避免与 config_loader 的循环导入。

    设计理由：
        config_loader.py 模块级导入了本模块的 get_project_root，
        因此本模块不能在模块级导入 config_loader，只能在函数体内延迟导入。
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
        from pipeline.core.config_loader import load_config

        config = load_config()
        data_dirs = config.get("pipeline", {}).get("data_dirs", {})
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
        from pipeline.core.config_loader import load_config

        config = load_config()
        state_rel = config.get("pipeline", {}).get("state_file", "data/state.json")
        path = project / state_rel.strip("/")
        ensure_dir(path.parent)
        return path
    except Exception:
        return project / "data" / "state.json"
