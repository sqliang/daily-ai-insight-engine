"""
pipeline/ingestion/repair.py — 自动修复 ingest 失败的文章

扫描 data/01_raw/ 中 extraction_status 为 failed 或 partial 的文章，
使用 BrowserSession 重新抓取原文并更新正文内容。
producthunt 源例外：优先走 fetch_producthunt_article（GraphQL API 优先，
含旧兜底链路），因为整站 Cloudflare challenge 下通用浏览器抓取基本无效。

作为 Stage 1c，在定时任务 scheduled/daily_fetch.sh 中 ingest 之后调用。
"""

import logging
from datetime import date
from pathlib import Path

from pipeline.core.config_loader import resolve_data_dir
from pipeline.core.browser_utils import BrowserSession
from pipeline.core.web_utils import extract_article_content, is_bot_challenge_html
from pipeline.ingestion.ingest.producthunt import fetch_producthunt_article
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter

logger = logging.getLogger(__name__)


def repair_failed_articles(target_date: date | None = None) -> dict:
    """
    扫描 data/01_raw/ 中所有 extraction_status 为 failed 或 partial 的文章，
    使用 BrowserSession 重新抓取并更新正文。

    参数：
        target_date: 只修复 created == target_date 的文章（None = 今天）

    返回：
        dict: {total: 发现数, repaired: 修复成功数, still_failed: 仍失败数, repaired_files: [...]}
    """
    if target_date is None:
        target_date = date.today()

    raw_dir = resolve_data_dir("raw")
    target_date_str = target_date.isoformat()

    # 发现失败文章
    failed_files: list[Path] = []
    for fp in sorted(raw_dir.rglob("*.md")):
        if not fp.is_file():
            continue
        # 跳过不在 source 子目录下的文件
        if fp.parent == raw_dir:
            continue
        try:
            fm, _ = read_frontmatter(fp)
        except Exception:
            continue
        status = fm.get("extraction_status", "")
        created = fm.get("created", "")
        # 兼容 date 对象和字符串
        if isinstance(created, date):
            created_str = created.isoformat()
        else:
            created_str = str(created)[:10]

        if status in ("failed", "partial") and created_str == target_date_str:
            failed_files.append(fp)

    total = len(failed_files)
    if total == 0:
        logger.info("Repair: 未发现需要修复的文章")
        return {"total": 0, "repaired": 0, "still_failed": 0, "repaired_files": []}

    print(f"\n发现 {total} 篇需要修复的文章")

    repaired = 0
    still_failed = 0
    repaired_files: list[str] = []

    with BrowserSession() as session:
        for fp in failed_files:
            try:
                fm, _ = read_frontmatter(fp)
            except Exception:
                still_failed += 1
                continue

            url = fm.get("source", "")
            title = fm.get("title", fp.name)
            if not url:
                still_failed += 1
                logger.warning("Repair: 缺少 source URL: %s", fp)
                continue

            # producthunt 走专用通道（GraphQL API 优先 + 旧兜底链路），
            # 整站 Cloudflare challenge 下通用浏览器抓取基本无效
            if fp.parent.name == "producthunt":
                ph_result = fetch_producthunt_article(
                    {
                        "url": url,
                        "title": title,
                        "summary": str(fm.get("description", "") or ""),
                        "published": str(fm.get("published", "") or ""),
                    },
                    {},
                    session=session,
                )
                if ph_result is not None:
                    fm["extraction_status"] = "success"
                    write_frontmatter(fp, fm, ph_result.content)
                    repaired += 1
                    repaired_files.append(str(fp.relative_to(raw_dir)))
                    print(f"  ✅ {title[:60]}")
                else:
                    print(f"  ❌ 修复失败: {title[:60]}")
                    still_failed += 1
                continue

            # Browser 重试
            html = session.fetch_page_html(
                url, timeout=60000, wait_until="domcontentloaded", wait_ms=5000
            )
            if html and len(html) > 500:
                # 先检查是否为反爬页面，避免把反爬文本当正文
                if is_bot_challenge_html(html):
                    print(f"  ❌ 仍被反爬拦截: {title[:60]}")
                    still_failed += 1
                    continue
                content = extract_article_content(html, url)
                if content and len(content) > 100:
                    # 对提取的正文做二次检查，防止反爬文本被 trafilatura 误提取
                    if is_bot_challenge_html(content):
                        print(f"  ❌ 提取内容仍含反爬文本: {title[:60]}")
                        still_failed += 1
                        continue
                    fm["extraction_status"] = "success"
                    write_frontmatter(fp, fm, content)
                    repaired += 1
                    repaired_files.append(str(fp.relative_to(raw_dir)))
                    print(f"  ✅ {title[:60]}")
                else:
                    fm["extraction_status"] = "partial"
                    write_frontmatter(fp, fm, html[:5000])
                    still_failed += 1
                    print(f"  ⚠️ 部分修复: {title[:60]}")
            else:
                still_failed += 1
                print(f"  ❌ 修复失败: {title[:60]}")

    result = {
        "total": total,
        "repaired": repaired,
        "still_failed": still_failed,
        "repaired_files": repaired_files,
    }
    logger.info(
        "Repair 完成: total=%d repaired=%d still_failed=%d",
        total, repaired, still_failed,
    )
    return result
