"""
pipeline/ingestion/ingest/orchestrator.py — Stage 1b 正文抓取业务逻辑

负责从 manifest 清单读取文章 URL，分类后通过 ExitStack 并行调度：
  - 常规文章（rss/scrape 策略）→ ThreadPoolExecutor 线程池并发
  - Browser 文章（Playwright 策略）→ 主线程串行（与线程池并行执行）

提供 run_ingest() 主编排函数，被 cli.py 消费。

设计理由：
    将业务逻辑与 CLI 契约分离，worker 函数拆分到 worker.py，
    截断逻辑拆分到 truncation.py，状态管理委托给 core/concurrency/state.py。
"""

import sys
from contextlib import ExitStack
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# 确保项目根目录在 sys.path 中，支持从任意目录运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.core.concurrency.state import IngestState
from pipeline.core.config_loader import get_source_by_name
from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.file_utils import ensure_dir, read_json
from pipeline.ingestion.ingest.worker import ingest_article, ingest_browser_article


def _needs_ingest(article: Dict[str, Any], target_dir: Path, state: IngestState) -> bool:
    """
    判断文章是否需要抓取：未见过，或 state 认为已处理但 .md 文件已不存于磁盘。

    仅靠 state.is_seen() 会因 state 与磁盘不一致而永久跳过文章，
    需要文件存在性作为二级验证。
    """
    from pipeline.utils.id_utils import generate_id

    article_id = article.get("id") or generate_id(article.get("url", ""))
    if not state.is_seen(article_id):
        return True
    md_path = target_dir / f"{article_id}.md"
    if not md_path.exists():
        return True
    return False


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
        manifest_paths = sorted(manifest_dir.glob(f"*_{today_str}.json"))

    if not manifest_paths:
        print("未找到清单文件，请先运行 scout")
        return []

    # ------------------------------------------------------------------
    # 2. 初始化去重状态
    # ------------------------------------------------------------------
    state = IngestState(force=force)

    # ------------------------------------------------------------------
    # 3. 分类文章：常规 vs browser
    # ------------------------------------------------------------------
    regular_items: List[Tuple[Dict[str, Any], str, Path]] = []
    browser_items: List[Tuple[Dict[str, Any], str, Path]] = []

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

        for article in articles:
            item = (article, source_name, target_dir)
            if strategy == "browser":
                browser_items.append(item)
            else:
                regular_items.append(item)

    # ------------------------------------------------------------------
    # 4. 预扫描去重（提前剔除已处理文章，减少无用任务提交）
    # ------------------------------------------------------------------
    regular_items = [
        item for item in regular_items
        if _needs_ingest(item[0], item[2], state)
    ]
    browser_items = [
        item for item in browser_items
        if _needs_ingest(item[0], item[2], state)
    ]

    total_articles = len(regular_items) + len(browser_items)
    if total_articles == 0:
        print("所有文章已处理，无新增")
        return []

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
        for article, source_name, target_dir in regular_items:
            future = executor.submit(
                ingest_article, article, source_name, target_dir, state
            )
            future_to_info[future] = (article, source_name)

        # --- 主线程同时处理 browser 文章（与线程池并行） ---
        if browser_items and browser_session:
            print(f"\n[browser] 开始处理 {len(browser_items)} 篇...")
            for article, source_name, target_dir in browser_items:
                url = article.get("url", "")
                title = article.get("title", url)[:60]
                print(f"  [browser] {title}...")
                result = ingest_browser_article(
                    article, source_name, target_dir, state, browser_session
                )
                if result:
                    output_files.append(result)
                else:
                    print(f"         跳过: URL 缺失")

        # --- 等待线程池完成 ---
        if future_to_info:
            print(f"\n[thread] 等待 {len(future_to_info)} 篇常规文章完成...")
            for future in as_completed(future_to_info):
                article, source_name = future_to_info[future]
                url = article.get("url", "")
                title = article.get("title", url)[:60]
                try:
                    result = future.result()
                    if result:
                        output_files.append(result)
                        print(f"  [ok] {title}")
                    else:
                        print(f"  [跳过] {title}: URL 缺失")
                except Exception as exc:
                    print(f"  [异常] {title}: {exc}")

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

    skipped = state.seen_count - len(output_files)

    print(f"\n=== 完成: 总计 {len(output_files)} 篇 "
          f"(success: {status_counts['success']}, "
          f"partial: {status_counts['partial']}, "
          f"failed: {status_counts['failed']}), "
          f"跳过 {skipped} 篇（历史去重） ===")
    return output_files
