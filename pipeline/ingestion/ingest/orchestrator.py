"""
pipeline/ingestion/ingest/orchestrator.py — Stage 1b 正文抓取业务逻辑

负责从 manifest 清单读取文章 URL，分类后通过 ExitStack 并行调度：
  - 常规文章（rss/scrape 策略）→ ThreadPoolExecutor 线程池并发
  - Browser 文章（Playwright 策略）→ 主线程串行（与线程池并行执行）

浏览器回退机制（v2）：
  常规文章 curl 抓取时如检测到反爬拦截（Cloudflare / JS challenge），
  不直接写入 partial 兜底文件，而是收集到 bot_blocked_queue，
  线程池结束后统一用 Playwright 重试。重试失败时调用 _write_fallback_md()
  写入 failed 兜底文件，防止下次运行反复重试同一篇注定失败的文章。

提供 run_ingest() 主编排函数，被 cli.py 消费。

设计理由：
    将业务逻辑与 CLI 契约分离，worker 函数拆分到 worker.py，
    截断逻辑拆分到 truncation.py，状态管理委托给 core/concurrency/state.py。
"""

import logging
import re
import sys
from contextlib import ExitStack
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


# 确保项目根目录在 sys.path 中，支持从任意目录运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.core.concurrency.state import IngestState
from pipeline.core.config_loader import get_source_by_name
from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.file_utils import ensure_dir, read_json
from pipeline.ingestion.ingest.worker import ingest_article, ingest_browser_article, BOT_BLOCKED


def _needs_ingest(article: Dict[str, Any], target_dir: Path, state: IngestState) -> bool:
    """
    判断文章是否需要抓取：force 模式或磁盘 raw 文件不存在。

    设计理由：
        raw 文件是 ingest 阶段的事实来源。state 只是加速去重的缓存，可能因为
        历史迁移、手动修复或清理而缺失记录。非 force 模式下只要 .md 已存在，
        就不能重抓覆盖 created；否则会破坏“首次入库日期”的日报口径。
    """
    from pipeline.utils.id_utils import generate_id

    article_id = article.get("id") or generate_id(article.get("url", ""))
    md_path = target_dir / f"{article_id}.md"
    if md_path.exists() and not state.force_enabled:
        return False
    if state.is_seen(article_id):
        return False
    if not md_path.exists():
        return True
    return True


def _record_manifest_date_for_existing(
    article: Dict[str, Any],
    target_dir: Path,
    manifest_date: Optional[str],
) -> None:
    """
    为已存在且跳过抓取的 raw 文件补记 manifest 日期。

    同一篇文章可能连续多天出现在不同日期的 manifest 中。正文只需抓取一次，
    manifest_dates 只作为审计和后续专题分析线索；默认日报仍按 created 选择
    新增文章。因此跳过下载时只补记 manifest_dates，不覆盖 created。
    """
    if not manifest_date:
        return

    from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter
    from pipeline.utils.id_utils import generate_id

    article_id = article.get("id") or generate_id(article.get("url", ""))
    if not article_id:
        return

    md_path = target_dir / f"{article_id}.md"
    if not md_path.exists():
        return

    try:
        fm, body = read_frontmatter(md_path)
        existing_dates = fm.get("manifest_dates", [])
        if isinstance(existing_dates, str):
            existing_dates = [existing_dates]
        elif not isinstance(existing_dates, list):
            existing_dates = []

        created = fm.get("created")
        if created:
            existing_dates.append(str(created)[:10])
        existing_dates.append(str(manifest_date)[:10])

        normalized = sorted({d for d in existing_dates if d})
        if normalized != fm.get("manifest_dates"):
            fm["manifest_dates"] = normalized
            write_frontmatter(md_path, fm, body)
    except Exception as exc:
        logger.warning("补记 manifest 日期失败 path=%s date=%s error=%s", md_path, manifest_date, exc)


def _write_fallback_md(
    article: Dict[str, Any],
    source_name: str,
    target_dir: Path,
    state: IngestState,
    reason: str = "",
    created: Optional[str] = None,
) -> Optional[Path]:
    """
    为抓取完全失败的文章写入兜底 .md 文件，确保 downstream 阶段可见。

    当浏览器重试也无法获取正文时调用，写入 extraction_status: failed，
    防止下次 ingest 运行重复尝试同一篇注定失败的文章。

    created: manifest 日期。历史清单重跑时用于保留原批次日期。
    """
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.utils.frontmatter import write_frontmatter
    from pipeline.utils.id_utils import generate_id

    url = article.get("url", "")
    article_id = article.get("id") or generate_id(url)

    fm = build_ingestion_frontmatter(
        title=article.get("title", ""),
        url=url,
        published=article.get("published", ""),
        author=article.get("author", ""),
        description=article.get("summary", ""),
        source_name=source_name,
        article_id=article_id,
        extraction_status="failed",
        created=created,
    )

    reason_line = f"\n原因：{reason}" if reason else ""
    body = (
        f"> **⚠️ 正文抓取失败**：curl + Playwright 均无法获取页面正文{reason_line}\n\n"
        f"{article.get('summary', '')}"
    ).strip()

    output_path = target_dir / f"{article_id}.md"
    write_frontmatter(output_path, fm, body)
    state.mark_seen(article_id)

    return output_path


def _discover_manifests(manifest_dir: Path, today_str: str) -> list[Path]:
    """
    发现今日 manifest；若不存在则回退到目录中最新的日期。

    设计理由：
        scout 和 ingest 独立计算 date.today()，跨天运行时 ingest
        找不到今日 manifest 会直接空跑。回退到最近日期可避免断点断裂。
    """
    paths = sorted(manifest_dir.glob(f"*_{today_str}.json"))
    if paths:
        return paths

    # 回退：找到目录中最新的日期
    all_manifests = sorted(manifest_dir.glob("*.json"))
    if not all_manifests:
        return []

    dates: set[str] = set()
    for mf in all_manifests:
        match = re.match(r".*_(\d{4}-\d{2}-\d{2})\.json$", mf.name)
        if match:
            dates.add(match.group(1))

    if not dates:
        return []

    latest = max(dates)
    logger.warning("今日 (%s) 无 manifest，回退到最近日期: %s", today_str, latest)
    return sorted(manifest_dir.glob(f"*_{latest}.json"))


def run_ingest(
    manifest_name: Optional[str] = None,
    force: bool = False,
    concurrency: int = 5,
) -> List[Path]:
    """
    主入口：读取清单文件，并发抓取正文，生成 .md 文件。

    参数：
        manifest_name: 指定清单文件名 (不含路径)，为 None 时处理今日所有清单。
        force: 忽略去重状态，强制重新抓取。
        concurrency: 线程池并发数（默认 5）。

    返回：
        生成的文件路径列表。
    """
    today_str = date.today().isoformat()
    manifest_dir = resolve_data_dir("manifest")
    raw_dir = resolve_data_dir("raw")

    # ------------------------------------------------------------------
    # 1. 选择清单文件
    # ------------------------------------------------------------------
    if manifest_name:
        manifest_paths = [manifest_dir / manifest_name]
    else:
        manifest_paths = _discover_manifests(manifest_dir, today_str)

    if not manifest_paths:
        logger.warning("未找到清单文件 today=%s", today_str)
        print("未找到清单文件，请先运行 scout")
        return []

    # ------------------------------------------------------------------
    # 2. 初始化去重状态
    # ------------------------------------------------------------------
    state = IngestState(force=force)

    # ------------------------------------------------------------------
    # 3. 分类文章：常规 vs browser
    # ------------------------------------------------------------------
    regular_items: List[Tuple[Dict[str, Any], str, Path, Optional[str]]] = []
    browser_items: List[Tuple[Dict[str, Any], str, Path, Optional[str]]] = []

    for manifest_path in manifest_paths:
        manifest = read_json(manifest_path)
        if not manifest:
            continue

        source_name = manifest.get("source", "")
        source_config = get_source_by_name(source_name) or {}
        target_dir = raw_dir / source_name
        ensure_dir(target_dir)

        strategy = source_config.get("fetch_strategy", "rss")
        articles = manifest.get("articles", [])
        manifest_date = manifest.get("date")

        for article in articles:
            item = (article, source_name, target_dir, manifest_date)
            if strategy == "browser":
                browser_items.append(item)
            else:
                regular_items.append(item)

    # ------------------------------------------------------------------
    # 4. 预扫描去重（提前剔除已处理文章，减少无用任务提交）
    # ------------------------------------------------------------------
    total_in_manifests = len(regular_items) + len(browser_items)

    pending_regular: List[Tuple[Dict[str, Any], str, Path, Optional[str]]] = []
    for item in regular_items:
        if _needs_ingest(item[0], item[2], state):
            pending_regular.append(item)
        else:
            _record_manifest_date_for_existing(item[0], item[2], item[3])
    regular_items = pending_regular

    pending_browser: List[Tuple[Dict[str, Any], str, Path, Optional[str]]] = []
    for item in browser_items:
        if _needs_ingest(item[0], item[2], state):
            pending_browser.append(item)
        else:
            _record_manifest_date_for_existing(item[0], item[2], item[3])
    browser_items = pending_browser

    total_articles = len(regular_items) + len(browser_items)
    if total_articles == 0:
        logger.info("所有文章已处理，无新增")
        print("所有文章已处理，无新增")
        return []

    logger.info("Ingest 开始 regular=%d browser=%d concurrency=%d",
                len(regular_items), len(browser_items), concurrency)
    print(f"待处理: {len(regular_items)} 篇常规 + {len(browser_items)} 篇 browser")

    # ------------------------------------------------------------------
    # 5. ExitStack 并行调度：线程池 + browser session 同时运行
    # ------------------------------------------------------------------
    output_files: List[Path] = []

    with ExitStack() as stack:
        executor = stack.enter_context(
            ThreadPoolExecutor(max_workers=concurrency)
        )

        # 初始化 browser session（仅在存在 browser 文章时）
        browser_session = None
        if browser_items:
            from pipeline.core.browser_utils import BrowserSession
            browser_session = stack.enter_context(BrowserSession())

        # --- 提交常规文章到线程池（立即开始执行） ---
        future_to_info: dict = {}
        for article, source_name, target_dir, manifest_date in regular_items:
            future = executor.submit(
                ingest_article, article, source_name, target_dir, state, manifest_date
            )
            future_to_info[future] = (article, source_name, target_dir, manifest_date)

        # --- 主线程同时处理 browser 文章（与线程池并行） ---
        if browser_items and browser_session:
            print(f"\n[browser] 开始处理 {len(browser_items)} 篇...")
            for article, source_name, target_dir, manifest_date in browser_items:
                url = article.get("url", "")
                title = article.get("title", url)[:60]
                print(f"  [browser] {title}...")
                result = ingest_browser_article(
                    article, source_name, target_dir, state, browser_session,
                    created=manifest_date,
                )
                if result:
                    output_files.append(result)
                else:
                    print(f"         跳过: URL 缺失")

        # --- 等待线程池完成 ---
        bot_blocked_queue: list = []  # 被反爬拦截的文章，稍后用浏览器重试

        if future_to_info:
            print(f"\n[thread] 等待 {len(future_to_info)} 篇常规文章完成...")
            for future in as_completed(future_to_info):
                article, source_name, target_dir, manifest_date = future_to_info[future]
                url = article.get("url", "")
                title = article.get("title", url)[:60]
                try:
                    result = future.result()
                    if result is BOT_BLOCKED:
                        # 反爬页面：不写 .md 文件，加入浏览器重试队列
                        bot_blocked_queue.append((article, source_name, target_dir, manifest_date))
                        print(f"  [反爬] {title} → 加入浏览器重试队列")
                    elif result:
                        output_files.append(result)
                        print(f"  [ok] {title}")
                    else:
                        print(f"  [跳过] {title}: URL 缺失")
                except Exception as exc:
                    logger.error("Worker 异常 source=%s title=%s url=%s: %s",
                                 source_name, title, url, exc)
                    print(f"  [异常] {title}: {exc}")

        # --- 浏览器重试：处理被反爬拦截的文章 ---
        if bot_blocked_queue:
            print(f"\n[browser-retry] 对 {len(bot_blocked_queue)} 篇反爬文章使用浏览器重试...")
            # 如果还没有 browser session，创建一个
            if browser_session is None:
                from pipeline.core.browser_utils import BrowserSession
                browser_session = stack.enter_context(BrowserSession())

            for article, source_name, target_dir, manifest_date in bot_blocked_queue:
                url = article.get("url", "")
                title = article.get("title", url)[:60]
                print(f"  [browser-retry] {title}...")
                try:
                    result = ingest_browser_article(
                        article, source_name, target_dir, state, browser_session,
                        created=manifest_date,
                    )
                    if result:
                        output_files.append(result)
                        print(f"    [ok] browser 重试成功")
                    else:
                        # URL 为空：写 failed 兜底文件，确保下游阶段能看到这篇文章
                        result = _write_fallback_md(
                            article, source_name, target_dir, state,
                            reason="URL 缺失，无法进行浏览器重试",
                            created=manifest_date,
                        )
                        if result:
                            output_files.append(result)
                        print(f"    [跳过] URL 缺失，已写兜底文件")
                except Exception as exc:
                    logger.error("Browser 重试异常 source=%s title=%s url=%s: %s",
                                 source_name, title, url, exc)
                    # 写 failed 兜底文件，防止下次运行反复重试同一篇文章
                    result = _write_fallback_md(
                        article, source_name, target_dir, state,
                        reason=f"浏览器重试异常: {exc}",
                        created=manifest_date,
                    )
                    if result:
                        output_files.append(result)
                    print(f"    [异常] browser 重试失败: {exc}，已写兜底文件")

    # ------------------------------------------------------------------
    # 6. 持久化去重状态
    # ------------------------------------------------------------------
    state.flush_to_disk()

    # ------------------------------------------------------------------
    # 7. 统计提取状态分布（success / partial / failed）
    # ------------------------------------------------------------------
    from pipeline.utils.frontmatter import read_frontmatter

    status_counts = {"success": 0, "partial": 0, "failed": 0}
    for f in output_files:
        fm, _ = read_frontmatter(f)
        status = fm.get("extraction_status", "success")
        status_counts[status] = status_counts.get(status, 0) + 1

    # skipped 基于预扫描实际剔除数量，而非 seen_count 估算（seen_count 含历史，不准确）
    skipped = total_in_manifests - total_articles

    logger.info("Ingest 完成 total=%d success=%d partial=%d failed=%d skipped=%d",
                len(output_files), status_counts["success"], status_counts["partial"],
                status_counts["failed"], skipped)
    print(f"\n=== 完成: 总计 {len(output_files)} 篇 "
          f"(success: {status_counts['success']}, "
          f"partial: {status_counts['partial']}, "
          f"failed: {status_counts['failed']}), "
          f"跳过 {skipped} 篇（历史去重） ===")
    return output_files
