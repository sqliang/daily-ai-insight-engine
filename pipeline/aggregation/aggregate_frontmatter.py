"""
pipeline/aggregation/aggregate_frontmatter.py — Stage 4a: Frontmatter 聚合

功能：
    - 默认扫描 data/01_raw/ + data/02_extracted/ + data/03_analyzed/ 下所有 .md 文件
    - 按 (source, article_id) 去重，保留最完整版本（03 > 02 > 01 优先级）
    - 提取 YAML frontmatter（不含正文 body）
    - 按 lookback_days 过滤旧文章（基于 frontmatter.created 字段）
    - 按 source 子目录分组
    - 输出：
        data/04_structured/{source}.json  — 每个数据源一个 JSON 数组
        data/04_structured/all_articles.json  — 所有文章的合并文件（含统计摘要）

设计原则：
    - 纯机械操作，零 LLM 调用，< 1 秒完成
    - 保留所有 frontmatter 字段（camelCase 键名）
    - 嵌套结构保持原样（如 impact_score: {score, reason}）
    - 跳过空正文文件和 frontmatter 解析失败的文件
    - per-source JSON 仅保留最近 hot_days 天热数据（默认 7 天），供前端快速读取
    - 冷数据按 created 日期分片写入 archive/{source}/{source}_{date}.json
    - all_articles.json 按 lookback_days 过滤（仅时间窗口内文章，作为日报输入）
    - 时间切片基于 frontmatter.created 字段，兼容 YAML 解析出的 date 对象和字符串
    - 显式传 input_dir 时保持单目录行为（向后兼容）
    - archive 分片每次 aggregate 覆盖写（文章可能被后续阶段更新）
"""

import json
import logging
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from pydantic import ValidationError

from ..core.config_loader import get_stage_config, resolve_data_dir
from pipeline.utils.file_utils import ensure_dir
from pipeline.utils.frontmatter import read_frontmatter
from pipeline.utils.schema_utils import flat_frontmatter_to_nested
from pipeline.schemas.daily_ai_insight import DailyAIInsight

logger = logging.getLogger(__name__)


def _serialize_value(obj):
    """将 Python 对象递归转换为 JSON 可序列化格式，过滤 None 值。"""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, list):
        return [v for v in (_serialize_value(x) for x in obj) if v is not None]
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            sv = _serialize_value(v)
            if sv is not None:
                result[k] = sv
        return result
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)


def _validate_article_fm(fm: dict, filepath: Path) -> int:
    """
    对单篇文章的扁平 frontmatter 做逐子模型 Pydantic 校验。

    将扁平字段路由到 DailyAIInsight 的 5 个子模型槽位，
    对有数据的子模型分别执行 model_validate()。
    校验失败仅记录 warning，不阻断数据流。
    未处理阶段（无数据的子模型）静默跳过。

    返回：
        校验失败的子模型数量
    """
    nested = flat_frontmatter_to_nested(fm)
    article_id = fm.get("id", "?")
    failed = 0

    for parent_key, sub_fields in nested.items():
        if not sub_fields:
            continue  # 该子模型无数据（文章尚未完成对应阶段），跳过
        sub_model_cls = DailyAIInsight.model_fields[parent_key].annotation
        try:
            sub_model_cls.model_validate(sub_fields)
        except ValidationError as exc:
            failed += 1
            error_count = len(exc.errors())
            logger.warning(
                "DailyAIInsight 校验失败 [%s] %s 子模型 (%d 个错误): %s — %s",
                parent_key,
                article_id,
                error_count,
                filepath,
                exc.errors(),
            )

    return failed


def _is_outside_window(record: dict, lookback_cutoff: Optional[date]) -> bool:
    """
    检查文章的 created 字段是否早于 lookback_cutoff（即不在时间窗口内）。

    YAML 解析器会将日期字符串反序列化为 date 对象，需兼容两种类型。
    """
    if lookback_cutoff is None:
        return False
    created_val = record.get("created", "")
    if not created_val:
        return False
    try:
        if isinstance(created_val, date):
            return created_val < lookback_cutoff
        return date.fromisoformat(str(created_val)) < lookback_cutoff
    except (ValueError, TypeError):
        return False  # created 字段异常时保守保留


def _cleanup_expired_archives(archive_dir: Path, source: str, max_history_days: Optional[int]) -> int:
    """
    清理 source 目录下超出 max_history_days 的归档分片。

    分片文件名格式：{source}_{YYYY-MM-DD}.json，从文件名提取日期并比较。

    参数：
        archive_dir: archive 根目录（data/04_structured/archive/）
        source: source 名称
        max_history_days: 最大保留天数（None 或 0 = 不限，不清理）

    返回：
        删除的分片数量
    """
    if not max_history_days or max_history_days <= 0:
        return 0
    source_dir = archive_dir / source
    if not source_dir.is_dir():
        return 0
    expire_date = date.today() - timedelta(days=max_history_days)
    removed = 0
    prefix = f"{source}_"
    for shard_path in sorted(source_dir.iterdir()):
        if not shard_path.name.startswith(prefix) or not shard_path.suffix == ".json":
            continue
        date_part = shard_path.stem[len(prefix):]  # YYYY-MM-DD
        try:
            shard_date = date.fromisoformat(date_part)
            if shard_date < expire_date:
                shard_path.unlink()
                removed += 1
        except (ValueError, IndexError):
            pass  # 文件名格式异常，跳过
    return removed


# 多阶段扫描目录，按优先级排序（先扫描的优先 — 即最完整版本）
_AGGREGATE_STAGE_DIRS = ("analyzed", "extracted", "raw")


def _discover_all_stages() -> tuple[list[Path], list[str]]:
    """
    扫描所有 pipeline 阶段目录中的 .md 文件，按 (source, article_id) 去重。

    优先级：analyzed > extracted > raw — 先扫描的胜出，
    自然保留最完整的文章版本。

    返回：
        (去重后的文件路径列表, 实际扫描的阶段 key 列表)
    """
    seen: dict[tuple[str, str], Path] = {}  # (source, article_id) -> filepath
    active_stages: list[str] = []

    for stage_key in _AGGREGATE_STAGE_DIRS:
        try:
            stage_dir = resolve_data_dir(stage_key)
        except (ValueError, KeyError):
            continue

        if not stage_dir.exists():
            continue

        active_stages.append(stage_key)

        for fp in sorted(stage_dir.rglob("*.md")):
            if not fp.is_file():
                continue
            source = fp.parent.name
            # 跳过直接在阶段根目录下的文件（不属于任何 source）
            if source == stage_dir.name:
                continue
            article_id = fp.stem
            key = (source, article_id)
            if key not in seen:
                seen[key] = fp

    return sorted(seen.values()), active_stages


def _group_by_source(file_paths: list[Path]) -> dict[str, list[Path]]:
    """按父目录名（source）分组文件路径。"""
    groups: dict[str, list[Path]] = {}
    for fp in file_paths:
        source = fp.parent.name
        groups.setdefault(source, []).append(fp)
    return groups


def _extract_article(filepath: Path, source_dir: str) -> tuple[Optional[dict], int]:
    """
    从单个 .md 文件提取 frontmatter 并构造文章记录。

    跳过条件：
        - frontmatter 为空
        - 缺少 id 或 title 字段
        - 正文为空（死文件）

    时间窗口过滤由调用方通过 _is_outside_window() 执行，
    确保 per-source JSON 保留全量数据供前端 enrichment 使用。

    返回：
        (文章记录 dict 或 None, 校验失败的子模型数)
    """
    try:
        fm, body = read_frontmatter(filepath)
    except Exception as exc:
        logger.warning("跳过（解析失败）: %s — %s", filepath, exc)
        return None, 0

    if not fm:
        logger.debug("跳过（无 frontmatter）: %s", filepath)
        return None, 0

    if not fm.get("id") or not fm.get("title"):
        logger.debug("跳过（缺少 id/title）: %s", filepath)
        return None, 0

    body_stripped = body.strip() if body else ""
    if not body_stripped:
        logger.debug("跳过（正文为空）: %s", filepath)
        return None, 0

    # 逐子模型校验 frontmatter 数据完整性（非阻塞质量门）
    validation_failures = _validate_article_fm(fm, filepath)

    record = {"source_dir": source_dir}
    record.update(fm)
    return _serialize_value(record), validation_failures


def aggregate_frontmatter(
    *,
    input_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    dry_run: bool = False,
    lookback_days: Optional[int] = None,
    hot_days: Optional[int] = None,
    max_history_days: Optional[int] = None,
) -> dict:
    """
    Stage 4a 主函数：聚合所有 pipeline 阶段的 .md 文件 frontmatter。

    默认扫描 data/01_raw/ + data/02_extracted/ + data/03_analyzed/，
    按 (source, article_id) 去重，保留最完整版本（03 > 02 > 01）。
    显式传 input_dir 时保持单目录行为（向后兼容）。

    热冷分离：
        - {source}.json：仅保留最近 hot_days 天的文章（热数据）
        - archive/{source}/{source}_{date}.json：冷数据按 created 日期分片
        - all_articles.json：由 lookback_days 控制时间窗口

    参数：
        input_dir: 输入目录（None = 多阶段扫描；显式 Path = 单目录）
        output_dir: 输出目录（默认 data/04_structured/）
        dry_run: 仅列出文件，不实际写入
        lookback_days: all_articles.json 时间窗口（天）。None 时从 config 读取
        hot_days: per-source JSON 热数据窗口（天）。None 时从 config 读取，默认 7
        max_history_days: archive 最大保留天数。None 时从 config 读取，默认 365（0 = 不限）

    返回：
        汇总 dict：{total_articles, sources: {name: count}, errors, skipped_old,
                   aggregated_stages, hot_days, archived_articles}
    """
    if output_dir is None:
        output_dir = resolve_data_dir("synthesize_structured")

    # --- 解析配置 ---
    agg_config = get_stage_config("aggregate") or {}
    if lookback_days is None:
        lookback_days = agg_config.get("lookback_days", 1)
    if hot_days is None:
        hot_days = agg_config.get("hot_days", 7)
    if max_history_days is None:
        max_history_days = agg_config.get("max_history_days", 365)

    lookback_cutoff: Optional[date] = None
    if lookback_days is not None and lookback_days > 0:
        lookback_cutoff = date.today() - timedelta(days=lookback_days)

    hot_cutoff: Optional[date] = None
    if hot_days is not None and hot_days > 0:
        hot_cutoff = date.today() - timedelta(days=hot_days)

    # --- 文件发现 ---
    if input_dir is not None:
        # 显式指定目录：单目录行为（向后兼容）
        all_files = sorted(input_dir.rglob("*.md"))
        source_groups = _group_by_source(all_files)
        aggregated_stages = [str(input_dir)]
    else:
        # 默认：多阶段扫描
        all_files, aggregated_stages = _discover_all_stages()
        source_groups = _group_by_source(all_files)

    stage_label = " > ".join(aggregated_stages)
    print(f"\n发现 {len(all_files)} 个 .md 文件，来自 {len(source_groups)} 个数据源")
    print(f"  扫描阶段: {stage_label}")
    if lookback_cutoff:
        print(f"  日报窗口: 仅保留 created >= {lookback_cutoff.isoformat()} (lookback_days={lookback_days})")
    if hot_cutoff:
        print(f"  热数据窗口: 仅保留 created >= {hot_cutoff.isoformat()} (hot_days={hot_days})")
    print()

    if dry_run:
        for source, files in sorted(source_groups.items()):
            print(f"  {source}: {len(files)} 个文件 → {output_dir / f'{source}.json'}")
        print(f"\n  合并文件: {output_dir / 'all_articles.json'}")
        print(f"  归档目录: {output_dir / 'archive'}/")
        return {
            "total_articles": len(all_files),
            "sources": {s: len(f) for s, f in source_groups.items()},
            "errors": 0,
            "skipped_old": 0,
            "aggregated_stages": aggregated_stages,
            "archived_articles": 0,
        }

    # 提取文章记录
    all_articles: list[dict] = []
    errors = 0
    skipped_old = 0
    validation_warnings = 0
    source_counts: dict[str, int] = {}
    total_archived = 0
    archive_dir = output_dir / "archive"

    for source, files in sorted(source_groups.items()):
        all_source_articles = []
        in_window_articles = []
        for fp in files:
            record, vf = _extract_article(fp, source)
            validation_warnings += vf
            if record is None:
                errors += 1
                continue
            all_source_articles.append(record)
            if not _is_outside_window(record, lookback_cutoff):
                in_window_articles.append(record)
            else:
                skipped_old += 1

        source_counts[source] = len(in_window_articles)
        all_articles.extend(in_window_articles)

        # 热冷分离：按 created 日期分流
        hot_articles: list[dict] = []
        cold_by_date: dict[str, list[dict]] = {}
        for record in all_source_articles:
            if _is_outside_window(record, hot_cutoff):
                # 冷数据：归入对应日期分片
                created_val = record.get("created", "")
                if isinstance(created_val, date):
                    date_str = created_val.isoformat()
                elif isinstance(created_val, str) and created_val:
                    date_str = created_val[:10]
                else:
                    date_str = "unknown"
                cold_by_date.setdefault(date_str, []).append(record)
            else:
                hot_articles.append(record)

        # 写入热数据 per-source JSON
        output_path = ensure_dir(output_dir) / f"{source}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(hot_articles, f, ensure_ascii=False, indent=2)
        cold_count = sum(len(v) for v in cold_by_date.values())
        print(f"  [{source}] {len(hot_articles)} 热数据（{cold_count} 归档） → {output_path}")

        # 写入冷数据归档分片
        if cold_by_date:
            source_archive_dir = ensure_dir(archive_dir / source)
            for date_str, batch in cold_by_date.items():
                shard_path = source_archive_dir / f"{source}_{date_str}.json"
                with open(shard_path, "w", encoding="utf-8") as f:
                    json.dump(batch, f, ensure_ascii=False, indent=2)
            total_archived += cold_count

        # 清理过期归档分片
        _cleanup_expired_archives(archive_dir, source, max_history_days)

    # 构建统计摘要（基于时间窗口内的文章）
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

    # 计算文章时间覆盖范围
    created_dates: list[date] = []
    for a in all_articles:
        created_val = a.get("created", "")
        if created_val:
            try:
                if isinstance(created_val, date):
                    created_dates.append(created_val)
                else:
                    created_dates.append(date.fromisoformat(str(created_val)))
            except (ValueError, TypeError):
                pass

    coverage_period = {}
    if created_dates:
        coverage_period = {
            "earliest": min(created_dates).isoformat(),
            "latest": max(created_dates).isoformat(),
        }

    combined = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "aggregated_stages": aggregated_stages,
        "lookback_days": lookback_days,
        "total_articles": len(all_articles),
        "skipped_old": skipped_old,
        "sources": sources_summary,
        "articles": all_articles,
    }
    if coverage_period:
        combined["coverage_period"] = coverage_period

    # 写入合并 JSON
    combined_path = ensure_dir(output_dir) / "all_articles.json"
    with open(combined_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)
    print(f"\n  合并: {len(all_articles)} 篇文章 → {combined_path}")
    if skipped_old > 0:
        print(f"  因时效跳过（日报窗口）: {skipped_old} 篇旧文章")
    if total_archived > 0:
        print(f"  热冷分离: {total_archived} 篇归档至 {archive_dir}/")
    if validation_warnings > 0:
        print(f"  DailyAIInsight 校验警告: {validation_warnings} 个子模型校验失败（文章仍正常输出）")

    return {
        "total_articles": len(all_articles),
        "sources": source_counts,
        "errors": errors,
        "skipped_old": skipped_old,
        "validation_warnings": validation_warnings,
        "aggregated_stages": aggregated_stages,
        "archived_articles": total_archived,
    }




