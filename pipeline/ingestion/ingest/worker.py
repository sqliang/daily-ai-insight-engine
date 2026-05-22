"""
pipeline/ingestion/ingest/worker.py — 单篇文章抓取 worker

提供两种 worker 函数：
  - ingest_article():      常规抓取（curl + trafilatura），线程安全，供线程池使用
  - ingest_browser_article(): 浏览器渲染抓取（Playwright），非线程安全，仅从主线程调用

设计理由：
    将文章抓取的完整流程（fetch → extract → truncate → write → mark_seen）
    封装为独立函数，使 orchestrator 只需关心调度逻辑。
"""

import sys
from pathlib import Path
from typing import Optional

from pipeline.ingestion.ingest.truncation import apply_truncation


def ingest_article(
    article: dict,
    source_name: str,
    target_dir: Path,
    state: "IngestState",
) -> Optional[Path]:
    """
    抓取单篇非 browser 策略文章：curl 获取 HTML → trafilatura 提取正文 → 写入 .md。

    无论抓取成功与否都会生成 .md 文件，extraction_status 标记提取质量。
    去重判断由 orchestrator._needs_ingest() 统一处理，worker 不自行检查。

    线程安全：所有 I/O 操作仅访问线程局部或受保护资源，
    可安全地在 ThreadPoolExecutor 中并发执行。

    参数：
        article: manifest 中的文章条目（url, title, id, published, author, summary）
        source_name: 数据源名称（用于查 config）
        target_dir: 输出目录
        state: 线程安全 IngestState

    返回：
        写入的 .md 文件路径，仅 URL 为空时返回 None
    """
    # 延迟导入避免循环依赖
    from pipeline.core.config_loader import get_source_by_name
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.utils.frontmatter import write_frontmatter
    from pipeline.utils.id_utils import generate_id
    from pipeline.core.web_utils import extract_article_content, extract_metadata, fetch_url

    url = article.get("url", "")
    if not url:
        return None

    article_id = article.get("id") or generate_id(url)

    source_config = get_source_by_name(source_name) or {}
    timeout = source_config.get("timeout", 30)

    # curl 获取 HTML（阻塞 I/O，在 worker 线程中安全）
    html = fetch_url(url, timeout=timeout)

    if html:
        # trafilatura 提取元数据和正文（阻塞 I/O，在线程中安全）
        meta = extract_metadata(html, url)
        content = extract_article_content(html, url)

        if content:
            # 正文提取成功
            extraction_status = "success"
            content = apply_truncation(content, source_config)
        else:
            # HTML 拿到了但 trafilatura 无法提取正文，用 manifest summary 兜底
            extraction_status = "partial"
            content = article.get("summary", "")
    else:
        # HTML 获取失败，用 manifest 元数据兜底
        meta = {}
        extraction_status = "failed"
        content = article.get("summary", "")

    # 构建失败/部分提取时的提示语
    if extraction_status == "failed":
        body = f"> **⚠️ 正文抓取失败**：无法获取页面 HTML（可能原因：网络超时、目标服务器拒绝、URL 失效）\n\n{content}".strip()
    elif extraction_status == "partial":
        body = f"> **⚠️ 正文提取不完整**：HTML 获取成功但无法从中提取正文，以下为文章摘要\n\n{content}".strip()
    else:
        body = content

    # 构建 frontmatter 并写入 .md
    fm = build_ingestion_frontmatter(
        title=meta.get("title") or article.get("title", ""),
        url=url,
        published=meta.get("date") or article.get("published", ""),
        author=meta.get("author") or article.get("author", ""),
        description=meta.get("description") or article.get("summary", ""),
        source_name=source_name,
        article_id=article_id,
        extraction_status=extraction_status,
    )

    output_path = target_dir / f"{article_id}.md"
    write_frontmatter(output_path, fm, body)

    # 标记为已处理（线程安全）
    state.mark_seen(article_id)

    return output_path


def ingest_browser_article(
    article: dict,
    source_name: str,
    target_dir: Path,
    state: "IngestState",
    session: "BrowserSession",
) -> Optional[Path]:
    """
    抓取单篇 browser 策略文章：Playwright 渲染 → trafilatura 提取正文 → 写入 .md。

    无论抓取成功与否都会生成 .md 文件，extraction_status 标记提取质量。
    去重判断由 orchestrator._needs_ingest() 统一处理，worker 不自行检查。

    非线程安全！仅从主线程调用（BrowserSession 使用 Playwright 同步 API）。

    参数：
        article: manifest 中的文章条目
        source_name: 数据源名称
        target_dir: 输出目录
        state: 线程安全 IngestState
        session: 已创建的 BrowserSession 实例

    返回：
        写入的 .md 文件路径，仅 URL 为空时返回 None
    """
    from pipeline.core.config_loader import get_source_by_name
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.utils.frontmatter import write_frontmatter
    from pipeline.utils.id_utils import generate_id
    from pipeline.core.web_utils import extract_article_content, extract_metadata

    url = article.get("url", "")
    if not url:
        return None

    article_id = article.get("id") or generate_id(url)

    # 去重检查（线程安全，与线程池中的 ingest_article 共享同一 IngestState）
    if state.is_seen(article_id):
        return None

    source_config = get_source_by_name(source_name) or {}
    timeout = source_config.get("timeout", 30)
    wait_for = source_config.get("wait_for")
    wait_ms = source_config.get("wait_ms", 2000)
    wait_until = source_config.get("wait_until", "domcontentloaded")
    wait_for_fn = source_config.get("wait_for_fn")

    # Playwright 渲染获取 HTML
    html = session.fetch_page_html(
        url, wait_for=wait_for, wait_ms=wait_ms,
        timeout=timeout * 1000, wait_until=wait_until,
        wait_for_fn=wait_for_fn,
    )

    if html:
        # trafilatura 提取
        meta = extract_metadata(html, url)
        content = extract_article_content(html, url)

        if content:
            extraction_status = "success"
            content = apply_truncation(content, source_config)
        else:
            # HTML 拿到了但 trafilatura 无法提取正文，用 manifest summary 兜底
            extraction_status = "partial"
            content = article.get("summary", "")
    else:
        # HTML 获取失败（Playwright 渲染失败或超时），用 manifest 元数据兜底
        meta = {}
        extraction_status = "failed"
        content = article.get("summary", "")

    # 构建失败/部分提取时的提示语
    if extraction_status == "failed":
        body = f"> **⚠️ 正文抓取失败**：Playwright 无法渲染页面（可能原因：页面加载超时、目标站点反爬、网络故障）\n\n{content}".strip()
    elif extraction_status == "partial":
        body = f"> **⚠️ 正文提取不完整**：页面渲染成功但无法提取正文，以下为文章摘要\n\n{content}".strip()
    else:
        body = content

    # 构建 frontmatter 并写入 .md
    fm = build_ingestion_frontmatter(
        title=meta.get("title") or article.get("title", ""),
        url=url,
        published=meta.get("date") or article.get("published", ""),
        author=meta.get("author") or article.get("author", ""),
        description=meta.get("description") or article.get("summary", ""),
        source_name=source_name,
        article_id=article_id,
        extraction_status=extraction_status,
    )

    output_path = target_dir / f"{article_id}.md"
    write_frontmatter(output_path, fm, body)

    # 标记为已处理（线程安全）
    state.mark_seen(article_id)

    return output_path
