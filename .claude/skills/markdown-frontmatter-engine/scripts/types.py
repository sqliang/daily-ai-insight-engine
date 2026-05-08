"""
类型定义

集中管理全模块共享的数据结构类型，使函数签名更清晰，
同时便于 IDE 进行类型推断和补全。
"""

from typing import TypedDict


class NoteInfo(TypedDict):
    """
    scan 命令返回的单条文件摘要信息。

    Attributes:
        path: 文件的绝对路径
        name: 文件名（不含路径）
        has_frontmatter: 文件开头是否包含 --- 分隔符（即是否有 frontmatter 块）
    """
    path: str
    name: str
    has_frontmatter: bool


class NoteReadResult(TypedDict):
    """
    read 命令返回的单条文件完整信息。

    Attributes:
        path: 文件的绝对路径
        frontmatter: 解析后的 YAML 字典，无 frontmatter 时为空字典
        body: frontmatter 分隔符后的正文内容（不含首行空行）
    """
    path: str
    frontmatter: dict
    body: str


class SchemaEntry(TypedDict):
    """
    scan_schema / schema 命令返回的单条字段定义条目。

    Attributes:
        name: 字段名（从 schema 文件名提取，如 "01.title.md" -> "title"）
        priority: 优先级（数字前缀越小优先级越高，无前缀时为 infinity）
        path: 字段定义文件的绝对路径
    """
    name: str
    priority: float
    path: str


class WriteResultItem(TypedDict):
    """
    write-multi 命令中单条文件的写入结果。

    Attributes:
        path: 文件绝对路径
        status: 写入状态
            - "ok": 成功
            - "not_found": JSON 中指定的路径不存在
            - "failed": 写入时发生其他错误
    """
    path: str
    status: str


class WriteMultiResult(TypedDict):
    """
    write-multi 命令返回的汇总结果。

    Attributes:
        total: 处理的 JSON 条目总数
        results: 每条文件的写入状态列表
    """
    total: int
    results: "list[WriteResultItem]"
