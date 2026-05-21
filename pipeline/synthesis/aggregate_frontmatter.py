"""
pipeline/synthesis/aggregate_frontmatter.py — Stage 4a: Frontmatter 聚合

功能：
    - 递归扫描 data/03_analyzed/ 下所有 .md 文件
    - 提取 YAML frontmatter（不含正文 body）
    - 按 source 子目录分组
    - 输出：
        data/04_structured/{source}.json  — 每个数据源一个 JSON 数组
        data/04_structured/all_articles.json  — 所有文章的合并文件（含统计摘要）

设计原则：
    - 纯机械操作，零 LLM 调用，< 1 秒完成
    - 保留所有 frontmatter 字段（camelCase 键名）
    - 嵌套结构保持原样（如 impact_score: {score, reason}）
    - 跳过空正文文件和 frontmatter 解析失败的文件
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from ..core.file_utils import ensure_dir, resolve_data_dir
from ..core.frontmatter_utils import read_frontmatter

logger = logging.getLogger(__name__)


def _serialize_value(obj):
    """将 Python 对象递归转换为 JSON 可序列化格式。"""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, list):
        return [_serialize_value(v) for v in obj]
    if isinstance(obj, dict):
        return {k: _serialize_value(v) for k, v in obj.items()}
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)


def _extract_article(filepath: Path, source_dir: str) -> Optional[dict]:
    """
    从单个 .md 文件提取 frontmatter 并构造文章记录。

    跳过条件：
        - frontmatter 为空
        - 缺少 id 或 title 字段
        - 正文为空（死文件）

    返回：
        包含 source_dir 和所有 frontmatter 字段的扁平 dict，或 None
    """
    try:
        fm, body = read_frontmatter(filepath)
    except Exception as exc:
        logger.warning("跳过（解析失败）: %s — %s", filepath, exc)
        return None

    if not fm:
        logger.debug("跳过（无 frontmatter）: %s", filepath)
        return None

    if not fm.get("id") or not fm.get("title"):
        logger.debug("跳过（缺少 id/title）: %s", filepath)
        return None

    body_stripped = body.strip() if body else ""
    if not body_stripped:
        logger.debug("跳过（正文为空）: %s", filepath)
        return None

    record = {"source_dir": source_dir}
    record.update(fm)
    return _serialize_value(record)


def aggregate_frontmatter(
    *,
    input_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    dry_run: bool = False,
) -> dict:
    """
    Stage 4a 主函数：聚合所有 analyzed .md 文件的 frontmatter。

    流程：
        1. 递归 glob 所有 .md 文件
        2. 按父目录名（source）分组
        3. 提取每篇文章的 frontmatter
        4. 写入 {source}.json 和 all_articles.json

    参数：
        input_dir: 输入目录（默认 data/03_analyzed/）
        output_dir: 输出目录（默认 data/04_structured/）
        dry_run: 仅列出文件，不实际写入

    返回：
        汇总 dict：{total_articles, sources: {name: count}, errors: int}
    """
    if input_dir is None:
        input_dir = resolve_data_dir("analyzed")
    if output_dir is None:
        output_dir = resolve_data_dir("synthesize_structured")

    # 递归发现 .md 文件并分组
    all_files = sorted(input_dir.rglob("*.md"))
    source_groups: dict[str, list[Path]] = {}
    for fp in all_files:
        source = fp.parent.name
        source_groups.setdefault(source, []).append(fp)

    print(f"\n发现 {len(all_files)} 个 .md 文件，来自 {len(source_groups)} 个数据源\n")

    if dry_run:
        for source, files in sorted(source_groups.items()):
            print(f"  {source}: {len(files)} 个文件 → {output_dir / f'{source}.json'}")
        print(f"\n  合并文件: {output_dir / 'all_articles.json'}")
        return {
            "total_articles": len(all_files),
            "sources": {s: len(f) for s, f in source_groups.items()},
            "errors": 0,
        }

    # 提取文章记录
    all_articles: list[dict] = []
    errors = 0
    source_counts: dict[str, int] = {}

    for source, files in sorted(source_groups.items()):
        articles = []
        for fp in files:
            record = _extract_article(fp, source)
            if record is None:
                errors += 1
                continue
            articles.append(record)

        source_counts[source] = len(articles)
        all_articles.extend(articles)

        # 写入单数据源 JSON
        output_path = ensure_dir(output_dir) / f"{source}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        print(f"  [{source}] {len(articles)}/{len(files)} 篇 → {output_path}")

    # 构建统计摘要
    sources_summary = {}
    for source, files in sorted(source_groups.items()):
        articles_in_source = [a for a in all_articles if a.get("source_dir") == source]
        impact_scores = [
            a.get("impact_score", {}).get("score", 0)
            if isinstance(a.get("impact_score"), dict)
            else a.get("impact_score", 0)
            for a in articles_in_source
        ]
        avg_impact = round(sum(impact_scores) / len(impact_scores), 1) if impact_scores else 0
        sources_summary[source] = {
            "count": len(articles_in_source),
            "avg_impact": avg_impact,
        }

    combined = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(input_dir),
        "total_articles": len(all_articles),
        "sources": sources_summary,
        "articles": all_articles,
    }

    # 写入合并 JSON
    combined_path = ensure_dir(output_dir) / "all_articles.json"
    with open(combined_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"\n  合并: {len(all_articles)} 篇文章 → {combined_path}")

    return {
        "total_articles": len(all_articles),
        "sources": source_counts,
        "errors": errors,
    }




