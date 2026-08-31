"""
pipeline/publish/publishers.py — Stage 5 数据收集、字段映射与 upsert

数据流：
    data/05_reports/daily-report-*.json|.md  → daily_reports 表
    data/00_manifest/{source}_{date}.json    → manifests 表
    data/04_structured/{source}.json（热）+ archive/{source}/{source}_{date}.json（冷）→ articles 表

设计要点：
    - map_* / parse_* / clean_* 均为纯函数（无 I/O、无 DB），供单测直接覆盖字段映射。
    - collect_* 负责文件扫描 + 纯函数映射；upsert_* 只负责批量 SQL 写入。
    - 文章冷热合并复刻前端语义（src/lib/data/sources/structured-data.ts:loadStructuredData）：
      同一 source 内热数据优先，冷数据中 normalize 后相同 URL 的跳过。
    - 全部 INSERT ... ON CONFLICT (主键) DO UPDATE，天然幂等。
"""

import json
import logging
import re
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

import psycopg
from psycopg.types.json import Jsonb

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 通用解析工具（纯函数）
# ---------------------------------------------------------------------------

def normalize_url(url: str) -> str:
    """
    规范化 URL 用于去重比较（复刻前端 normalizeUrl 语义）。

    去除首尾空白与尾部斜杠，统一协议前缀小写。
    """
    url = url.strip()
    url = re.sub(r"/+$", "", url)
    url = re.sub(r"^http://", "http://", url, flags=re.IGNORECASE)
    url = re.sub(r"^https://", "https://", url, flags=re.IGNORECASE)
    return url


def parse_iso_date(value) -> Optional[date]:
    """
    将 frontmatter 中的日期字段解析为 date。

    兼容 "YYYY-MM-DD" 与完整 ISO 时间戳（截断为日期）；非字符串强转 str。
    解析失败返回 None（调用方据此跳过并记 warning）。
    """
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    # 纯日期直通；带时间的交给 fromisoformat 再取日期部分
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
            return date.fromisoformat(s)
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt.date()
    except ValueError:
        return None


def parse_iso_datetime(value) -> Optional[datetime]:
    """
    将 ISO 字符串解析为带时区的 datetime（用于 generated_at 列）。

    解析失败返回 None；无时区信息时按 UTC 处理，避免 timestamptz 列写入歧义。
    """
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def clean_author(value) -> Optional[str]:
    """
    清洗作者字段。

    frontmatter 中 author 可能是列表（如 ["[[Name]]"]），取第一个元素并
    剥掉 Obsidian wiki-link 风格的 [[ ]] 包裹；非字符串强转 str。
    """
    if isinstance(value, list):
        value = value[0] if value else None
    if value is None:
        return None
    s = str(value).strip()
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2].strip()
    return s or None


def parse_impact_score(value) -> Optional[float]:
    """
    解析 impact_score 字段为数值。

    Stage 3 产出为 dict（{"score": 2.5, "reason": ...}），取 score 键；
    也可能直接是数值或数字字符串。无法解析为数值时返回 None。
    """
    if isinstance(value, dict):
        value = value.get("score")
    if isinstance(value, bool):
        # bool 是 int 子类，但语义上不是分数，防御性排除
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.strip())
        except ValueError:
            return None
    return None


def strip_frontmatter(text: str) -> str:
    """
    剥离 Markdown 开头的 YAML frontmatter 块（---\\n...\\n---）。

    日报 .md 可能带 frontmatter，入库的 report_md 只保留正文。
    无 frontmatter 时原样返回。
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[i + 1:]).lstrip("\n")
    # 只有起始 --- 没有闭合 ---：视为无有效 frontmatter，原样返回
    return text


# ---------------------------------------------------------------------------
# 字段映射（纯函数，dict → 表行 dict）
# ---------------------------------------------------------------------------

# 文件名兜底解析：{source}_{YYYY-MM-DD}（source 本身可能含连字符，从右侧切一次）
_MANIFEST_STEM_RE = re.compile(r"^(?P<source>.+)_(?P<date>\d{4}-\d{2}-\d{2})$")
# 日报文件名：daily-report-YYYY-MM-DD.json（无日期的 daily-report.json 天然不匹配）
_REPORT_NAME_RE = re.compile(r"^daily-report-(?P<date>\d{4}-\d{2}-\d{2})\.json$")


def parse_manifest_filename(stem: str) -> Optional[tuple[str, str]]:
    """
    从 manifest 文件名（不含扩展名）解析 (source, date)。

    仅在 JSON 内 source/date 字段缺失时作为兜底使用。
    """
    m = _MANIFEST_STEM_RE.match(stem)
    if not m:
        return None
    return m.group("source"), m.group("date")


def map_manifest(path_stem: str, data: dict) -> Optional[dict]:
    """
    将 manifest JSON 映射为 manifests 表行。

    参数：
        path_stem: 文件名（不含 .json），用于字段缺失时的兜底解析
        data:      manifest JSON 反序列化后的 dict

    返回：
        表行 dict；source/date 均无法确定时返回 None（调用方记 warning 跳过）
    """
    source = data.get("source")
    mdate = data.get("date")
    if not source or not mdate:
        fallback = parse_manifest_filename(path_stem)
        if fallback is None:
            return None
        f_source, f_date = fallback
        source = source or f_source
        mdate = mdate or f_date
    return {
        "source": str(source),
        "date": str(mdate),
        "generated_at": parse_iso_datetime(data.get("generated_at")),
        "payload": data,
    }


def map_report(path: Path, data: dict) -> Optional[dict]:
    """
    将日报 JSON 映射为 daily_reports 表行。

    参数：
        path: 日报 JSON 文件路径（日期从文件名提取，mtime 作为 generated_at 兜底）
        data: 日报 JSON 反序列化后的 dict

    返回：
        表行 dict；文件名不含日期时返回 None
    """
    m = _REPORT_NAME_RE.match(path.name)
    if not m:
        return None
    # generated_at 优先取 JSON 内的 generatedAt，缺失时用文件 mtime 兜底
    generated_at = parse_iso_datetime(data.get("generatedAt"))
    if generated_at is None:
        generated_at = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    # 同名 .md 存在则读入正文（剥离 frontmatter）
    md_path = path.with_suffix(".md")
    report_md = None
    if md_path.exists():
        report_md = strip_frontmatter(md_path.read_text(encoding="utf-8"))
    return {
        "date": m.group("date"),
        "report": data,
        "report_md": report_md,
        "generated_at": generated_at,
    }


def map_article(entry: dict) -> Optional[dict]:
    """
    将 04_structured 中的扁平 frontmatter dict 映射为 articles 表行。

    参数：
        entry: 结构化 JSON 数组元素（含 source_dir 键的扁平 frontmatter）

    返回：
        表行 dict；id 或 created 缺失/非法时返回 None（调用方记 warning 跳过）。
        payload 整存整个扁平 dict，保证入库数据与磁盘数据一一对应。
    """
    article_id = entry.get("id")
    if not article_id:
        return None
    created = parse_iso_date(entry.get("created"))
    if created is None:
        return None
    published = entry.get("published")
    return {
        "id": str(article_id),
        "source_dir": str(entry.get("source_dir") or ""),
        "created": created,
        # frontmatter 里原文 URL 的字段名是 source
        "url": str(entry.get("source")) if entry.get("source") else None,
        "title": str(entry.get("title")) if entry.get("title") else None,
        "author": clean_author(entry.get("author")),
        "description": str(entry.get("description")) if entry.get("description") else None,
        "tldr": str(entry.get("tldr")) if entry.get("tldr") else None,
        "objective_summary": str(entry.get("objective_summary")) if entry.get("objective_summary") else None,
        "event_type": str(entry.get("event_type")) if entry.get("event_type") else None,
        "sentiment": str(entry.get("sentiment")) if entry.get("sentiment") else None,
        "published": str(published) if published is not None else None,
        "impact_score": parse_impact_score(entry.get("impact_score")),
        "payload": entry,
    }


# ---------------------------------------------------------------------------
# 文件扫描与收集（filesystem → 表行列表）
# ---------------------------------------------------------------------------

def collect_report_rows(reports_dir: Path, target_date: Optional[str] = None) -> list[dict]:
    """
    扫描 data/05_reports/ 收集 daily_reports 表行。

    只处理 daily-report-YYYY-MM-DD.json（排除无日期的 daily-report.json）。
    target_date 非空时只收集该日期的日报。
    """
    rows: list[dict] = []
    if not reports_dir.is_dir():
        return rows
    for path in sorted(reports_dir.glob("daily-report-*.json")):
        m = _REPORT_NAME_RE.match(path.name)
        if not m:
            continue
        if target_date and m.group("date") != target_date:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("日报文件读取失败，跳过: %s (%s)", path, exc)
            continue
        row = map_report(path, data)
        if row:
            rows.append(row)
    return rows


def collect_manifest_rows(manifest_dir: Path, target_date: Optional[str] = None) -> list[dict]:
    """
    扫描 data/00_manifest/ 收集 manifests 表行。

    目录下还有人类可读的 .md 汇总文件，glob 只取 .json 天然跳过。
    target_date 非空时只收集该日期的 manifest（先按文件名粗筛，减少 JSON 解析量）。
    """
    rows: list[dict] = []
    if not manifest_dir.is_dir():
        return rows
    for path in sorted(manifest_dir.glob("*.json")):
        if target_date and not path.stem.endswith(f"_{target_date}"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("manifest 文件读取失败，跳过: %s (%s)", path, exc)
            continue
        row = map_manifest(path.stem, data)
        if row is None:
            logger.warning("manifest 缺少 source/date 且文件名无法解析，跳过: %s", path)
            continue
        if target_date and row["date"] != target_date:
            continue
        rows.append(row)
    return rows


def collect_article_rows(
    structured_dir: Path,
    target_date: Optional[str] = None,
    include_archive: bool = True,
) -> list[dict]:
    """
    扫描 data/04_structured/ 收集 articles 表行（热数据 + 可选冷数据）。

    合并规则复刻前端 loadStructuredData 语义：同一 source 内热数据优先，
    冷数据中 normalize 后相同 URL 的跳过。
    跨 source 不去重：不同 source 可能收录同一 URL，articles 表主键是 id，
    且 source_dir 不同属于不同记录。

    参数：
        structured_dir:  data/04_structured/ 目录
        target_date:     非空时只收集 created == 该日期的文章
        include_archive: 是否扫描 archive 冷数据分片（--force 全量 backfill 时为 True）

    返回：
        表行 dict 列表
    """
    rows: list[dict] = []
    if not structured_dir.is_dir():
        return rows

    def _load_array(path: Path) -> list:
        """读取 JSON 数组文件；非数组（如 all_articles.json 的 dict）返回空列表。"""
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning("结构化文件读取失败，跳过: %s (%s)", path, exc)
            return []
        return data if isinstance(data, list) else []

    def _append(entries: list, seen_urls: set, source_name: str) -> None:
        """映射并追加表行，按 normalize 后的 URL 去重（先出现者优先）。"""
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            url = entry.get("source")
            if url:
                key = normalize_url(str(url))
                if key in seen_urls:
                    continue
                seen_urls.add(key)
            row = map_article(entry)
            if row is None:
                logger.warning("文章缺少 id/created 或 created 非法，跳过: source=%s url=%s",
                               source_name, url)
                continue
            if target_date and row["created"].isoformat() != target_date:
                continue
            rows.append(row)

    # 热数据：{source}.json（all_articles.json 是 dict，_load_array 自动排除）
    hot_files = [p for p in sorted(structured_dir.glob("*.json")) if p.stem != "all_articles"]
    for hot_path in hot_files:
        source_name = hot_path.stem
        seen_urls: set = set()
        _append(_load_array(hot_path), seen_urls, source_name)

        if not include_archive:
            continue
        # 冷数据：archive/{source}/{source}_{date}.json
        archive_dir = structured_dir / "archive" / source_name
        if not archive_dir.is_dir():
            continue
        for shard in sorted(archive_dir.glob("*.json")):
            # 文件名日期粗筛：不匹配目标日期的分片不读内容
            if target_date and not shard.stem.endswith(f"_{target_date}"):
                continue
            _append(_load_array(shard), seen_urls, f"{source_name}(archive)")

    return rows


# ---------------------------------------------------------------------------
# upsert（表行列表 → PostgreSQL）
# ---------------------------------------------------------------------------

_UPSERT_REPORTS_SQL = """
INSERT INTO daily_reports (date, report, report_md, generated_at)
VALUES (%(date)s, %(report)s, %(report_md)s, %(generated_at)s)
ON CONFLICT (date) DO UPDATE SET
    report = EXCLUDED.report,
    report_md = EXCLUDED.report_md,
    generated_at = EXCLUDED.generated_at
"""

_UPSERT_MANIFESTS_SQL = """
INSERT INTO manifests (source, date, generated_at, payload)
VALUES (%(source)s, %(date)s, %(generated_at)s, %(payload)s)
ON CONFLICT (source, date) DO UPDATE SET
    generated_at = EXCLUDED.generated_at,
    payload = EXCLUDED.payload
"""

_UPSERT_ARTICLES_SQL = """
INSERT INTO articles (id, source_dir, created, published, url, title, author,
                      description, tldr, objective_summary, event_type, sentiment,
                      impact_score, payload, updated_at)
VALUES (%(id)s, %(source_dir)s, %(created)s, %(published)s, %(url)s, %(title)s,
        %(author)s, %(description)s, %(tldr)s, %(objective_summary)s,
        %(event_type)s, %(sentiment)s, %(impact_score)s, %(payload)s, now())
ON CONFLICT (id) DO UPDATE SET
    source_dir = EXCLUDED.source_dir,
    created = EXCLUDED.created,
    published = EXCLUDED.published,
    url = EXCLUDED.url,
    title = EXCLUDED.title,
    author = EXCLUDED.author,
    description = EXCLUDED.description,
    tldr = EXCLUDED.tldr,
    objective_summary = EXCLUDED.objective_summary,
    event_type = EXCLUDED.event_type,
    sentiment = EXCLUDED.sentiment,
    impact_score = EXCLUDED.impact_score,
    payload = EXCLUDED.payload,
    updated_at = now()
"""


def upsert_reports(conn: "psycopg.Connection", rows: list[dict]) -> int:
    """批量 upsert daily_reports 行，返回写入行数。"""
    if not rows:
        return 0
    params = [{**r, "report": Jsonb(r["report"])} for r in rows]
    with conn.cursor() as cur:
        cur.executemany(_UPSERT_REPORTS_SQL, params)
    return len(rows)


def upsert_manifests(conn: "psycopg.Connection", rows: list[dict]) -> int:
    """批量 upsert manifests 行，返回写入行数。"""
    if not rows:
        return 0
    params = [{**r, "payload": Jsonb(r["payload"])} for r in rows]
    with conn.cursor() as cur:
        cur.executemany(_UPSERT_MANIFESTS_SQL, params)
    return len(rows)


def upsert_articles(conn: "psycopg.Connection", rows: list[dict]) -> int:
    """批量 upsert articles 行，返回写入行数。"""
    if not rows:
        return 0
    params = [{**r, "payload": Jsonb(r["payload"])} for r in rows]
    with conn.cursor() as cur:
        cur.executemany(_UPSERT_ARTICLES_SQL, params)
    return len(rows)


# ---------------------------------------------------------------------------
# 编排入口
# ---------------------------------------------------------------------------

def publish_all(
    *,
    conn: Optional["psycopg.Connection"] = None,
    target_date: Optional[str] = None,
    include_archive: bool = True,
) -> dict:
    """
    Stage 5 主编排：收集三组数据并 upsert 到 PostgreSQL。

    参数：
        conn:            已建立的连接（None 时通过 db.get_connection() 自建，
                         便于测试注入 mock 连接）
        target_date:     非空时只发布该日期（created/日期字段匹配）的数据
        include_archive: 是否包含 archive 冷数据文章（--force 全量 backfill）

    返回：
        统计 dict：{"reports": n, "manifests": n, "articles": n}

    设计理由：
        三组 upsert 放在一个事务里——任一组失败整体回滚，避免 DB 出现
        "报告已更新但文章是旧版" 的半一致状态。
    """
    from ..core.config_loader import resolve_data_dir
    from .db import get_connection

    reports_dir = resolve_data_dir("reports")
    manifest_dir = resolve_data_dir("manifest")
    structured_dir = resolve_data_dir("synthesize_structured")

    report_rows = collect_report_rows(reports_dir, target_date)
    manifest_rows = collect_manifest_rows(manifest_dir, target_date)
    article_rows = collect_article_rows(structured_dir, target_date, include_archive)

    own_conn = conn is None
    if own_conn:
        conn = get_connection()
    try:
        with conn.transaction():
            stats = {
                "reports": upsert_reports(conn, report_rows),
                "manifests": upsert_manifests(conn, manifest_rows),
                "articles": upsert_articles(conn, article_rows),
            }
    finally:
        if own_conn:
            conn.close()

    logger.info(
        "publish 完成 target_date=%s include_archive=%s reports=%d manifests=%d articles=%d",
        target_date, include_archive,
        stats["reports"], stats["manifests"], stats["articles"],
    )
    return stats
