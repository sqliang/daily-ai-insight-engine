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
from typing import Any, List, Optional


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


def resolve_data_dir(stage_key: str) -> Path:
    """
    解析数据目录路径。
    stage_key 可选: raw, processed, structured, reports, manifest
    """
    project = get_project_root()
    key_to_path = {
        "manifest": project / "data" / "00_manifest",
        "raw": project / "data" / "01_raw",
        "processed": project / "data" / "02_processed",
        "extracted": project / "data" / "02_extracted",
        "structured": project / "data" / "03_structured",
        "reports": project / "data" / "04_reports",
    }
    path = key_to_path.get(stage_key)
    if path is None:
        raise ValueError(f"未知数据层: {stage_key}，可选值: {list(key_to_path.keys())}")
    ensure_dir(path)
    return path
