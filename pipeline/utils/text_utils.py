"""
pipeline/utils/text_utils.py — 通用文本处理工具

提供中英文文本的自然断句截断功能，被 extraction 和 analysis 两个 stage 共用。
"""

import re

# ---------------------------------------------------------------------------
# 中英文混排间距规范化
# ---------------------------------------------------------------------------

# CJK 字符集：覆盖中日韩统一表意文字 + 标点
_CJK_RANGE = (
    r'一-鿿'     # CJK Unified Ideographs
    r'㐀-䶿'     # CJK Unified Ideographs Extension A
    r'豈-﫿'     # CJK Compatibility Ideographs
)

_CJK_RE = re.compile(
    rf'([{_CJK_RANGE}])([a-zA-Z0-9])'
)
_CJK_RE_REV = re.compile(
    rf'([a-zA-Z0-9])([{_CJK_RANGE}])'
)


def insert_cjk_spacing(text: str) -> str:
    """
    在中英文混排文本中自动插入规范间距。

    规则：
        - 中文字符后紧跟英文字母/数字 → 插入空格
        - 英文字母/数字后紧跟中文字符 → 插入空格
        - 已存在的空格不会被重复插入

    被 synthesis stage 调用，对 LLM 生成的日报文本字段做后处理。
    """
    # 先处理 CJK→Latin 方向，再处理 Latin→CJK 方向
    text = _CJK_RE.sub(r'\1 \2', text)
    text = _CJK_RE_REV.sub(r'\1 \2', text)
    return text


# ---------------------------------------------------------------------------
# 自然断句截断
# ---------------------------------------------------------------------------


def truncate_at_natural_break(text: str, max_len: int) -> str:
    """
    在自然断句处截断文本，避免中英文句子被拦腰截断。

    三级回退策略：
        1. 强断句（。！？.!?\n）— 在 max_len 往前 30 字符范围内搜索
        2. 弱断句（；，,; ）— 在 max_len 往前 20 字符范围内搜索
        3. 硬截断 — 在 max_len 处直接截断，去掉末尾不完整的字符

    参数：
        text: 待截断的原始文本
        max_len: 目标最大字符数

    返回：
        截断后的文本（已去除首尾空白）
    """
    if len(text) <= max_len:
        return text.strip()

    truncated = text[:max_len]

    # 策略 1: 强断句 — 搜索 。！？.!?\n
    search_start = max(max_len - 30, 0)
    for cut_pos in range(max_len, search_start, -1):
        if truncated[cut_pos - 1] in "。！？.!?\n":
            return truncated[:cut_pos].strip()

    # 策略 2: 弱断句 — 搜索 ；，,;
    search_start = max(max_len - 20, 0)
    for cut_pos in range(max_len, search_start, -1):
        if truncated[cut_pos - 1] in "；，,; ":
            return truncated[:cut_pos].strip()

    # 策略 3: 硬截断
    return truncated.strip()
