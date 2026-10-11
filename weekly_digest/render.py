"""
weekly_digest/render.py — 周报 Markdown 渲染

将 WeeklyDigest 渲染为中英文对照的 Markdown 文档：头部统计 + 按日期倒序分组。
渲染层不判断数据完整度——collector 已按降级链组装好字段，这里只做展示分支：
有中文摘要走"中文摘要 + 详细说明 + English 原文"三段式；无中文摘要时英文原文
升格为主体并标注"未提取"，避免同一段英文重复出现两次。
"""

from datetime import date
from itertools import groupby
from typing import List

from weekly_digest.models import DigestItem, WeeklyDigest

# 日期分组标题中的中文星期名（date.weekday() 周一为 0）
_WEEKDAY_NAMES = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


# ---------------------------------------------------------------------------
# 条目渲染
# ---------------------------------------------------------------------------

def _render_item(index: int, item: DigestItem, show_trending: bool) -> str:
    """
    渲染单个条目为 Markdown 片段。

    参数：
        index: 条目在当日分组内的序号（从 1 开始）
        item: 周报条目
        show_trending: 是否展示"上榜天数"行（仅 GitHub Trending 有意义；
            Product Hunt 等榜单源改为展示发布日期）
    """
    lines: List[str] = [f"### {index}. [{item.title}]({item.url})", ""]

    if item.summary_zh:
        lines.append(f"- **中文摘要**：{item.summary_zh}")
        if item.detail_zh:
            lines.append(f"- **详细说明**：{item.detail_zh}")
        if item.description_en:
            lines.append(f"- **English**: {item.description_en}")
    else:
        # 降级分支：未执行 extraction，英文原文升格为主体展示
        lines.append("- **状态**：本条未提取中文摘要，以下为英文原文")
        if item.description_en:
            lines.append(f"- **English**: {item.description_en}")

    if show_trending and item.trending_days:
        days = ", ".join(d.strftime("%m-%d") for d in item.trending_days)
        lines.append(f"- **上榜**：{len(item.trending_days)} 天（{days}）")
    if not show_trending and item.published:
        lines.append(f"- **发布日期**：{item.published.isoformat()}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 文档渲染
# ---------------------------------------------------------------------------

def render_markdown(digest: WeeklyDigest) -> str:
    """
    将周报渲染为完整 Markdown 文档。

    参数：
        digest: collector 产出的周报模型

    返回：
        str: Markdown 全文（末尾带换行）
    """
    # GitHub Trending 的"上榜天数"语义来自 manifest_dates；其他源展示发布日期
    show_trending = digest.source == "github-trending"

    stats_line = (
        f"> 本周共收录 {digest.stats.total} 条，其中 {digest.stats.extracted} 条已完成中文摘要提取，"
        f"覆盖 {digest.stats.days_covered} 天。数据来自本地 pipeline 抓取，"
        f"生成于 {digest.generated_at.isoformat()}。"
    )
    # 周未结束时生成的是快照：标注清楚，避免读者误以为这是完整周报；
    # 下次运行会全量重生成（新文章补入、已提取文章升级为中文摘要）
    if digest.week_end > digest.generated_at:
        stats_line += " ⚠️ 本周尚未结束，本报告为进行中快照（数据截至生成时），后续运行会自动补全并升级中文摘要。"

    parts: List[str] = [
        f"# {digest.source_label} 周报 · {digest.iso_week}"
        f"（{digest.week_start.isoformat()} ~ {digest.week_end.isoformat()}）",
        "",
        stats_line,
        "",
    ]

    if not digest.items:
        parts.append("本周无收录条目。")
        parts.append("")
        return "\n".join(parts)

    # items 已按 created 倒序排好（collector 保证），groupby 直接按日期分组
    for day, group in groupby(digest.items, key=lambda it: it.created):
        day_items = list(group)
        weekday = _WEEKDAY_NAMES[day.weekday()]
        parts.append(f"## {day.isoformat()} · {weekday}（{len(day_items)} 条）")
        parts.append("")
        for i, item in enumerate(day_items, start=1):
            parts.append(_render_item(i, item, show_trending))
            parts.append("")

    return "\n".join(parts)
