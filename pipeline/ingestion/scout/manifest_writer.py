"""
pipeline/ingestion/scout/manifest_writer.py — Markdown 汇总清单生成

负责将当天所有数据源的抓取结果合并为一份 Markdown 汇总文件，输出到
data/00_manifest/{date}-manifest-第{W}周.md。

设计理由：
    - 汇总清单供人类快速浏览当天全部文章来源，独立于 JSON 清单（供机器消费）
    - 对于被跳过的源（今日清单已存在），从已有 JSON 回读数据以确保汇总完整
    - 原子写入（atomic_write）防止生成过程中断导致文件损坏
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from pipeline.utils.file_utils import read_json, atomic_write

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------

SOURCE_TYPE_LABEL: Dict[str, str] = {
    "academic_paper": "学术论文",
    "tech_blog": "技术博客",
    "news_media": "科技媒体",
    "community_discussion": "社区讨论",
}


# ---------------------------------------------------------------------------
# Markdown 清单生成
# ---------------------------------------------------------------------------

def _generate_markdown_manifest(
    all_manifests: Dict[str, List[dict]],
    manifest_dir: Path,
    today_str: str,
    sources: List[dict],
) -> None:
    """
    生成每日汇总 Markdown 清单文件。

    合并逻辑：
        1. 本次 run 新抓取的文章直接使用
        2. 被跳过的源（今日 JSON 已存在）从已有清单文件回读
        3. 合并后按 Tier (A→B→C) 再按 name 排序

    输出文件命名：{date}-manifest-第{W}周.md

    参数：
        all_manifests: 本次 run 新抓取的文章字典 {source_name: [articles]}
        manifest_dir:  data/00_manifest/ 绝对路径
        today_str:     ISO 日期字符串 (YYYY-MM-DD)
        sources:       完整数据源配置列表

    异常：
        无异常抛出 — 所有错误通过 print 警告后继续
    """
    merged: Dict[str, dict] = {}

    for source in sources:
        name = source.get("name", "")
        if name in all_manifests and all_manifests[name]:
            # 本次 run 新抓取的
            merged[name] = {
                "articles": all_manifests[name],
                "source_type": source.get("type", ""),
                "tier": source.get("tier", ""),
                "language": source.get("language", "en"),
            }
        else:
            # 源被跳过 — 尝试从已有 JSON 清单读回
            manifest_path = manifest_dir / f"{name}_{today_str}.json"
            data = read_json(manifest_path)
            if data and data.get("articles"):
                merged[name] = {
                    "articles": data["articles"],
                    "source_type": data.get("source_type", source.get("type", "")),
                    "tier": data.get("tier", source.get("tier", "")),
                    "language": source.get("language", "en"),
                }
            else:
                print(f"  [Markdown] ⚠ {name} — 无清单数据，跳过")

    if not merged:
        print("  [Markdown] ⚠ 没有任何源有文章数据，跳过生成")
        return

    # 按 Tier (A→B→C) 再按 name 排序
    tier_order = {"A": 0, "B": 1, "C": 2}
    sorted_names = sorted(merged.keys(), key=lambda n: (tier_order.get(merged[n]["tier"], 99), n))

    total_sources = len(sorted_names)
    total_articles = sum(len(merged[n]["articles"]) for n in sorted_names)
    iso_week = datetime.now().isocalendar()[1]
    generated_at = datetime.now(timezone.utc).isoformat()

    # 构建 frontmatter + 正文
    lines: List[str] = []
    lines.append("---")
    lines.append(f'date: "{today_str}"')
    lines.append(f"week: {iso_week}")
    lines.append(f"total_sources: {total_sources}")
    lines.append(f"total_articles: {total_articles}")
    lines.append(f'generated_at: "{generated_at}"')
    lines.append("---")
    lines.append("")
    lines.append("# Daily AI Insight — 数据源清单")
    lines.append("")
    lines.append(
        f"**日期**: {today_str} | **第 {iso_week} 周** | "
        f"**{total_sources}** 个源, **{total_articles}** 篇文章"
    )
    lines.append("")

    for name in sorted_names:
        info = merged[name]
        articles: list = info["articles"]
        src_type = info["source_type"]
        tier = info["tier"]
        lang = info["language"]
        src_type_cn = SOURCE_TYPE_LABEL.get(src_type, src_type)
        lang_display = "中文" if lang == "zh" else "EN"
        count = len(articles)

        lines.append("---")
        lines.append("")
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"> Tier {tier} · {src_type_cn} · {lang_display} · {count} 篇")
        lines.append("")

        for article in articles:
            title = article.get("title", "无标题").strip() or "无标题"
            url = article.get("url", "")
            published = article.get("published", "")
            author = article.get("author", "")
            summary = article.get("summary", "").strip()

            # 文章标题行（带链接）
            if url:
                lines.append(f"- **[{title}]({url})**")
            else:
                lines.append(f"- **{title}**")

            # 元信息行
            meta_parts: List[str] = []
            if published:
                meta_parts.append(f"发布: {published}")
            if author:
                meta_parts.append(f"作者: {author}")
            if meta_parts:
                lines.append(f"  - {' | '.join(meta_parts)}")

            # 摘要行
            if summary:
                lines.append(f"  - 摘要: {summary}")
            lines.append("")

    md_content = "\n".join(lines)
    filename = f"{today_str}-manifest-第{iso_week}周.md"
    filepath = manifest_dir / filename
    atomic_write(filepath, md_content)
    print(f"  [Markdown] ✅ 已生成汇总清单: {filename}")
