"""
环境配置模块

负责读取 skill 根目录下的 .env 文件，解析 SCHEMA_FIELDS 配置。

用途：
  - 当用户未在对话中明确指定字段时，skill 可从 .env 读取默认字段配置
  - 配置持久化，用户无需每次对话都重复指定

.env 文件格式：
  SCHEMA_FIELDS=title,tags,domain
  # 注释行会被忽略

优先级：对话指定 > .env 配置 > 全量（schema 目录下所有字段）

依赖：
  - 优先使用 python-dotenv 库（pip install python-dotenv）
  - 无该库时自动回退到手动解析（无外部依赖）
"""

import os
from pathlib import Path
from typing import Optional, Set

try:
    from dotenv import load_dotenv
except ImportError:
    # python-dotenv 未安装时的占位符，运行时会走手动解析分支
    load_dotenv = None  # type: ignore


def load_env_fields(skill_root: str) -> Optional[Set[str]]:
    """
    读取 skill 根目录下 .env 文件中的 SCHEMA_FIELDS 配置。

    SCHEMA_FIELDS 定义了 skill 默认处理的字段范围。
    若用户对话中未指定字段，则 skill 使用此配置。

    返回值语义：
      - None：.env 不存在，或文件中无 SCHEMA_FIELDS 定义（走全量模式）
      - set：配置的字段集合（走部分字段模式）

    解析行为：
      - 空值（如 `SCHEMA_FIELDS=`）视为无配置，返回 None
      - 注释行（以 # 开头）被忽略
      - 重复调用时使用 override=True 确保读取的是当前文件内容，
        而不是上次调用后残留的环境变量值

    Arguments:
        skill_root: skill 根目录的路径字符串（.env 文件所在目录）

    Returns:
        字段名集合，或 None（表示走全量）

    Examples:
        .env 内容为 `SCHEMA_FIELDS=title,tags`
        -> {"title", "tags"}

        .env 内容为空或无 SCHEMA_FIELDS 键
        -> None
    """
    env_path = Path(skill_root) / ".env"

    # .env 文件不存在 → 无配置
    if not env_path.exists():
        return None

    if load_dotenv is not None:
        # 有 python-dotenv：使用库函数加载
        # override=True 确保本次读取的是当前文件内容，覆盖旧的环境变量值
        # 这解决了"第二次调用时 SCHEMA_FIELDS 为空但环境变量仍是旧值"的问题
        load_dotenv(env_path, override=True)
    else:
        # 无 python-dotenv：手动解析 .env 文件
        # 手动清除旧值，保证每次读取都是文件当前内容
        os.environ.pop("SCHEMA_FIELDS", None)
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            # 跳过空行和注释行，只处理包含 = 的行
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            if key.strip() == "SCHEMA_FIELDS":
                # 提取逗号分隔的字段，去空白后转为集合
                fields = {f.strip() for f in val.split(",") if f.strip()}
                # 写回环境变量（供 dotenv 路径的代码路径使用）
                os.environ["SCHEMA_FIELDS"] = val
                # 空值视为无配置（返回 None）
                return fields if fields else None
        # 文件存在但无 SCHEMA_FIELDS 键
        return None

    # 从环境变量读取（python-dotenv 路径）
    fields_val = os.environ.get("SCHEMA_FIELDS", "")
    if not fields_val:
        return None
    return {f.strip() for f in fields_val.split(",") if f.strip()}
