"""
Frontmatter 解析与序列化模块

负责 Markdown 文件中 YAML frontmatter 块的双向转换：
  - 解析（parse_frontmatter）：将字符串内容拆分为元数据字典 + 正文
  - 序列化（build_frontmatter）：将元数据字典 + 正文组装为符合 FORMAT.md 规范的字符串

格式规范（FORMAT.md）：
  1. 字段与字段之间空一行（每个字段视为一个 group）
  2. 列表项使用 2 空格缩进
  3. 闭合 --- 后空一行再接正文
  4. tags 和 aliases 为合并模式（去重追加），其他字段为覆盖模式
  5. 不在 field_order 中的字段按字母顺序排在最后
"""

from typing import Any, List, Dict, Optional, Tuple


# ============================================================================
# 解析：从字符串到 Python 对象
# ============================================================================


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """
    将 Markdown 文件内容拆分为 frontmatter 字典和正文。

    Frontmatter 是 YAML 格式的元数据块，位于文件开头的两行 --- 之间。
    不使用完整的 YAML 解析器（pyyaml），而是手写解析器以避免：
      - 外部依赖
      - YAML 的复杂类型推断（如自动转换日期字符串）
      - YAML 的多文档支持（--- 分隔符在一篇笔记中只用于 frontmatter）

    解析逻辑基于状态机：
      - 状态 A（scalar 行）：`key: value`   -> 设置标量字段
      - 状态 B（list header）：`key:`       -> 开始收集列表项
      - 状态 C（list item）：`- item`       -> 向当前列表追加项

    Arguments:
        content: Markdown 文件的完整文本内容

    Returns:
        (frontmatter_dict, body_content)
            - frontmatter_dict: 解析出的 YAML 字段，无 frontmatter 时为空 {}
            - body_content: --- 块之后的所有内容（不含闭合 --- 行）

    Examples:
        content = "---\\ntitle: Hello\\ntags:\\n  - python\\n---\\n\\n正文"
        -> ({'title': 'Hello', 'tags': ['python']}, '\\n正文')
    """
    # 快速路径：文件不以 --- 开头，说明没有 frontmatter
    if not content.startswith("---"):
        return {}, content

    lines = content.split("\n")

    # Frontmatter 块至少需要 3 行：---, 内容, ---（不含空行）
    if len(lines) < 3:
        return {}, content

    # 找到第二个 --- 分隔符，确定 frontmatter 块的边界
    # end_idx 初始为 1（跳过第一行的 ---）
    end_idx = 1
    while end_idx < len(lines) and lines[end_idx].strip() != "---":
        end_idx += 1

    # frontmatter 内容行（不包含两端的 --- 分隔符）
    fm_lines = lines[1:end_idx]
    # 正文：从第二个 --- 之后的第一行开始（跳过闭合行本身）
    body = "\n".join(lines[end_idx + 1:])

    fm: dict = {}
    # pending_list_key 记录当前正在收集的列表字段名。
    # 状态机设计：
    #   - 遇到 `key: value`（val 非空）→ 切换到标量模式，重置 pending_list_key
    #   - 遇到 `key:`（val 为空）      → 切换到列表模式，记录 key，开始收集
    #   - 遇到 `- item`                 → 向当前 pending_list_key 追加
    pending_list_key: Optional[str] = None

    for line in fm_lines:
        stripped = line.strip()

        # 跳过空行和注释行
        if not stripped or stripped.startswith("#"):
            continue

        if ":" in stripped:
            # 找到 key:value 对，拆分为键和值
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val:
                # 情况 1：标量字段（`title: Hello`）
                # 关闭列表收集状态（如果之前在收集列表）
                pending_list_key = None
                fm[key] = val
            else:
                # 情况 2：列表头（`tags:` 或 `aliases:` 后面跟多项）
                # 开启列表收集状态，初始化空列表
                pending_list_key = key
                fm[key] = []
        elif stripped.startswith("-"):
            # 情况 3：列表项（`- python`）
            # 仅在有活动的列表头时才追加，避免 `- item` 出现在错误位置时污染数据
            item = stripped[1:].strip()
            if pending_list_key and item:
                fm[pending_list_key].append(item)

    return fm, body


# ============================================================================
# 序列化：从 Python 对象到 YAML 字符串
# ============================================================================


def _format_scalar(value: Any) -> str:
    """
    将 Python 值格式化为 YAML 标量字符串。

    处理 bool 值（YAML 规范要求小写 true/false），
    以及 int/float 值的字符串转换。
    字符串值直接转为 str（不加引号，保持 YAML 可读性）。

    Arguments:
        value: Python 对象

    Returns:
        YAML 标量字符串表示
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def _format_field(key: str, value: Any, indent: str = "  ") -> List[str]:
    """
    将单个 frontmatter 字段格式化为多行 YAML 行列表。

    标量字段输出为单行：`key: value`
    空列表输出为单行：`key: []`
    非空列表输出为：
        key:
          - item1
          - item2

    Arguments:
        key: 字段名
        value: 字段值（标量或列表）
        indent: 列表项缩进字符，默认 2 空格

    Returns:
        格式化后的行列表（不含前导缩进）
    """
    if isinstance(value, list):
        # 空列表特殊处理：输出为 `key: []`（单行），避免后续 enumerate 出问题
        if not value:
            return [f"{key}: []"]
        lines = [f"{key}:"]
        for item in value:
            lines.append(f"{indent}- {_format_scalar(item)}")
        return lines
    else:
        return [f"{key}: {_format_scalar(value)}"]


def build_frontmatter(
    fields: dict,
    existing_fm: dict,
    field_order: List[str],
) -> str:
    """
    将新的 frontmatter 字段与现有字段合并，组装为符合 FORMAT.md 规范的字符串。

    合并策略（两种模式）：
      - 合并模式（tags, aliases）：新旧值去重后追加，保留历史数据
      - 覆盖模式（其他字段）：新值覆盖旧值

    字段输出顺序：
      1. field_order 中的字段（按 schema 优先级顺序）
      2. field_order 之外的字段（按字母顺序，视为扩展字段）

    FORMAT.md 规范：每个字段块之间空一行。

    Arguments:
        fields: 本次要写入的新字段（可能只包含部分字段）
        existing_fm: 文件中已有的 frontmatter 字典
        field_order: 字段输出的优先顺序（从 schema 扫描得到）

    Returns:
        完整的 frontmatter 块字符串，包含前后 --- 分隔符和末尾空行

    Examples:
        build_frontmatter(
            fields={"title": "New Title", "tags": ["python"]},
            existing_fm={"title": "Old", "tags": ["javascript"], "custom": "keep"},
            field_order=["title", "tags", "domain"]
        )
        # 返回:
        # ---
        # title: New Title
        #
        # tags:
        #   - javascript
        #   - python
        #
        # custom: keep
        # ---
        #
    """
    # 合并模式字段：多次写入时去重追加，而不是覆盖
    merge_fields = {"tags", "aliases"}

    final_fields: Dict[str, Any] = {}
    already_written_keys: set = set()

    # 阶段 1：按 field_order 顺序处理所有字段
    for key in field_order:
        # 只有当字段在本次新值或历史值中存在时才处理
        if key not in fields and key not in existing_fm:
            continue

        if key in merge_fields:
            # ---- 合并模式 ----
            # 获取历史值（可能是字符串或列表，统一转为列表）
            existing = existing_fm.get(key, [])
            if isinstance(existing, str):
                existing = [existing]
            # 获取新值
            new = fields.get(key, [])
            if isinstance(new, str):
                new = [new]
            # 去重追加：dict.fromkeys 保留顺序下去重
            combined = list(dict.fromkeys(existing + new))
            if combined:  # 忽略空列表
                final_fields[key] = combined
                already_written_keys.add(key)
        else:
            # ---- 覆盖模式 ----
            if key in fields:
                final_fields[key] = fields[key]
                already_written_keys.add(key)

    # 阶段 2：将 existing_fm 中不在 field_order 且不在新值中的字段追加进来
    # 这些是"扩展字段"（不在 schema 中定义），保留原样
    for key, val in existing_fm.items():
        if key not in already_written_keys:
            final_fields[key] = val
            already_written_keys.add(key)

    # 阶段 3：构建输出行
    # 使用 pending_blank 机制：在每个字段前插入空行（FORMAT.md 规范）
    output_lines: List[str] = []
    pending_blank = False

    def emit_field(key: str, value: Any) -> None:
        """
        将单个字段追加到 output_lines，并在字段前插入空行。
        pending_blank 保证了：第一个字段前不空行，之后每个字段前都空一行。
        """
        nonlocal pending_blank
        lines = _format_field(key, value)
        if pending_blank and output_lines:
            output_lines.append("")  # 字段间空行
        for line in lines:
            output_lines.append(line)
        pending_blank = True

    # 阶段 3a：按 field_order 输出（schema 定义的核心字段）
    for key in field_order:
        if key in final_fields:
            emit_field(key, final_fields[key])

    # 阶段 3b：按字母顺序输出扩展字段（不在 schema 中的历史字段）
    other_keys = sorted(
        k for k in final_fields.keys()
        if k not in field_order
    )
    for key in other_keys:
        emit_field(key, final_fields[key])

    # 组装最终字符串：--- + 内容 + --- + 空行
    return "---\n" + "\n".join(output_lines) + "\n---\n\n"
