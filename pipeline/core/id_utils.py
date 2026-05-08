"""
pipeline/core/id_utils.py — 共享文章 ID 生成工具

设计目的：
    - 为所有流水线阶段提供统一的 ID 生成函数（单一数据源）
    - 在 00_manifest 阶段即可生成 ID，实现跨源去重
    - 替代 ingest.py 中的 MD5 哈希和 base_info_agent.py 中的重复实现

算法：SHA-256(source_url) → 取前 16 个十六进制字符
    - 确定性：同一 URL 始终产生相同 ID，保证幂等性
    - 零成本：无需 LLM 调用，纯数学运算
    - 足够唯一：64 位哈希空间，碰撞概率极低（约 10^-10 级别）
"""

import hashlib

# 16 hex chars = 64 bits of SHA-256
# 对于 URL 唯一性场景已足够（>10^9 篇文章时碰撞概率仍 <10^-10）
ID_LENGTH = 16


def generate_id(source_url: str) -> str:
    """
    基于 source URL 确定性生成文章唯一标识符。

    算法：SHA-256(source_url) → hexdigest() → 取前 ID_LENGTH 位
    空 URL 返回空字符串（调用方应自行处理）

    参数：
        source_url: 文章原始 URL

    返回：
        16 字符的十六进制 ID 字符串，空 URL 返回 ""
    """
    if not source_url:
        return ""
    return hashlib.sha256(source_url.encode("utf-8")).hexdigest()[:ID_LENGTH]
