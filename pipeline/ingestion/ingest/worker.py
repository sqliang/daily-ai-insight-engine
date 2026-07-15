"""
pipeline/ingestion/ingest/worker.py — 单篇文章抓取 worker

提供两种 worker 函数：
  - ingest_article():      常规抓取（curl + trafilatura），线程安全，供线程池使用
  - ingest_browser_article(): 浏览器渲染抓取（Playwright），非线程安全，仅从主线程调用

设计理由：
    将文章抓取的完整流程（fetch → extract → truncate → write → mark_seen）
    封装为独立函数，使 orchestrator 只需关心调度逻辑。
"""

import logging
import re
import sys
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from pipeline.ingestion.ingest.truncation import apply_truncation

logger = logging.getLogger(__name__)

# 特殊返回值：标记文章被反爬机制拦截，需用浏览器重试
# orchestrator 检查到此标记后收集对应文章，线程池结束后统一用 Playwright 重试
BOT_BLOCKED = object()


def ingest_article(
    article: dict,
    source_name: str,
    target_dir: Path,
    state: "IngestState",
    created: Optional[str] = None,
) -> Optional[Path]:
    """
    抓取单篇非 browser 策略文章：curl 获取 HTML → trafilatura 提取正文 → 写入 .md。

    无论抓取成功与否都会生成 .md 文件，extraction_status 标记提取质量。
    去重判断由 orchestrator._needs_ingest() 统一处理，worker 不自行检查。

    反爬检测：curl 获取 HTML 后先检查 is_bot_challenge_html()，
    若检测到 Cloudflare / JS challenge 页面，返回 BOT_BLOCKED 标记
    让 orchestrator 改用 Playwright 重试，避免写入无意义的 partial 文件。

    线程安全：所有 I/O 操作仅访问线程局部或受保护资源，
    可安全地在 ThreadPoolExecutor 中并发执行。

    参数：
        article: manifest 中的文章条目（url, title, id, published, author, summary）
        source_name: 数据源名称（用于查 config）
        target_dir: 输出目录
        state: 线程安全 IngestState
        created: manifest 日期。历史清单重跑时用于保留原批次日期

    返回：
        Path          — 写入的 .md 文件路径
        BOT_BLOCKED   — 检测到反爬页面，需浏览器重试（不写文件，不标记 seen）
        None          — URL 为空
    """
    # 延迟导入避免循环依赖
    from pipeline.core.config_loader import get_source_by_name
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.utils.frontmatter import write_frontmatter
    from pipeline.utils.id_utils import generate_id
    from pipeline.core.web_utils import extract_article_content, extract_metadata, fetch_url, fetch_via_jina, is_bot_challenge_html

    url = article.get("url", "")
    if not url:
        return None

    article_id = article.get("id") or generate_id(url)

    source_config = get_source_by_name(source_name) or {}
    timeout = source_config.get("timeout", 30)

    if source_name == "producthunt":
        producthunt_path = _try_producthunt_ingest(
            article=article,
            source_name=source_name,
            target_dir=target_dir,
            state=state,
            source_config=source_config,
            article_id=article_id,
            created=created,
        )
        if producthunt_path:
            return producthunt_path

    if source_name == "hackernews":
        hackernews_path = _try_hackernews_ingest(
            article=article,
            source_name=source_name,
            target_dir=target_dir,
            state=state,
            source_config=source_config,
            article_id=article_id,
            created=created,
        )
        if hackernews_path:
            return hackernews_path

    # curl 获取 HTML（阻塞 I/O，在 worker 线程中安全）
    html = fetch_url(url, timeout=timeout)

    # 检测反爬页面：HTML 获取成功但内容是 Cloudflare / JS challenge
    # 先尝试 Jina AI Reader 兜底，失败后再返回 BOT_BLOCKED 让 Playwright 重试
    if html and is_bot_challenge_html(html):
        logger.info("检测到反爬页面，尝试 Jina AI Reader 兜底 source=%s url=%s", source_name, url)
        jina_body = fetch_via_jina(url)
        if jina_body:
            # Jina 成功获取真实内容，直接写入文件（无需 Playwright）
            meta = extract_metadata(html, url)  # 元数据从原始 HTML 提取（标题等）
            fm = build_ingestion_frontmatter(
                title=meta.get("title") or article.get("title", ""),
                url=url,
                published=meta.get("date") or article.get("published", ""),
                author=meta.get("author") or article.get("author", ""),
                description=meta.get("description") or article.get("summary", ""),
                source_name=source_name,
                article_id=article_id,
                extraction_status="success",
                created=created,
            )
            output_path = target_dir / f"{article_id}.md"
            write_frontmatter(output_path, fm, apply_truncation(jina_body, source_config))
            state.mark_seen(article_id)
            logger.info("Jina AI Reader 兜底成功 source=%s url=%s", source_name, url)
            return output_path
        # Jina 也失败，走现有兜底链：BOT_BLOCKED → Playwright → failed
        logger.info("Jina AI Reader 兜底失败，标记为浏览器重试 source=%s url=%s", source_name, url)
        return BOT_BLOCKED

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
        # curl 获取失败（含重试后仍失败），返回 BOT_BLOCKED 触发浏览器兜底
        # 设计理由：瞬时网络故障不应直接判定为永久失败，给 Playwright 一次机会
        # orchestrator 的 browser-retry 循环会自动处理，Playwright 也失败时才写 failed
        logger.info("curl 获取失败，标记为浏览器重试 source=%s url=%s", source_name, url)
        return BOT_BLOCKED

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
        created=created,
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
    created: Optional[str] = None,
) -> Optional[Path]:
    """
    抓取单篇 browser 策略文章：Playwright 渲染 → trafilatura 提取正文 → 写入 .md。

    无论抓取成功与否都会生成 .md 文件，extraction_status 标记提取质量。

    去重检查：内部有独立的 is_seen + 文件存在性双重验证，
    与 orchestrator._needs_ingest() 逻辑一致，防止 state 与磁盘不一致时
    永久跳过需重抓的文章。

    反爬检测（两阶段）：Playwright 渲染后先检查 is_bot_challenge_html()，
    若检测到反爬标记，仍让 trafilatura 尝试提取。仅当 trafilatura 也失败时
    才确认为真正的反爬拦截（extraction_status=failed），避免残留 JS 标记误报。

    非线程安全！仅从主线程调用（BrowserSession 使用 Playwright 同步 API）。

    参数：
        article:    manifest 中的文章条目
        source_name: 数据源名称
        target_dir:  输出目录
        state:       线程安全 IngestState
        session:     已创建的 BrowserSession 实例
        created:     manifest 日期。历史清单重跑时用于保留原批次日期

    返回：
        Path  — 写入的 .md 文件路径
        None  — URL 为空，或已去重（seen + 文件存在）
    """
    from pipeline.core.config_loader import get_source_by_name
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.utils.frontmatter import write_frontmatter
    from pipeline.utils.id_utils import generate_id
    from pipeline.core.web_utils import extract_article_content, extract_metadata, is_bot_challenge_html

    url = article.get("url", "")
    if not url:
        return None

    article_id = article.get("id") or generate_id(url)

    # 去重检查（线程安全，与线程池中的 ingest_article 共享同一 IngestState）
    # 仅当 state 已标记 AND .md 文件仍存在时才跳过，防止 state 与磁盘不一致
    if state.is_seen(article_id):
        md_path = target_dir / f"{article_id}.md"
        if md_path.exists():
            return None

    source_config = get_source_by_name(source_name) or {}
    timeout = source_config.get("timeout", 30)
    wait_for = source_config.get("wait_for")
    wait_ms = source_config.get("wait_ms", 2000)
    wait_until = source_config.get("wait_until", "domcontentloaded")
    wait_for_fn = source_config.get("wait_for_fn")

    if source_name == "producthunt":
        producthunt_path = _try_producthunt_ingest(
            article=article,
            source_name=source_name,
            target_dir=target_dir,
            state=state,
            source_config=source_config,
            article_id=article_id,
            created=created,
            session=session,
        )
        if producthunt_path:
            return producthunt_path

    # Playwright 渲染获取 HTML
    html = session.fetch_page_html(
        url, wait_for=wait_for, wait_ms=wait_ms,
        timeout=timeout * 1000, wait_until=wait_until,
        wait_for_fn=wait_for_fn,
    )

    # 检测反爬页面：Playwright 也可能被激进反爬系统拦截
    # 若检测到反爬页面，视为 failed 而非 partial，便于区分根本原因
    #
    # 注意：中文反爬页面（如 ProductHunt 的 "安全验证" 页面）本身就是纯文本内容，
    # trafilatura 会将其当正文提取。因此 bot_blocked + content 非空 ≠ 正文正常，
    # 需对提取内容做二次检查，防止反爬文本混入管线。
    bot_blocked = False
    if html and is_bot_challenge_html(html):
        logger.debug("Playwright 渲染后检测到反爬标记 source=%s url=%s", source_name, url)
        bot_blocked = True

    if html:
        # trafilatura 提取（先提取，再根据结果和反爬信号综合判断）
        meta = extract_metadata(html, url)
        content = extract_article_content(html, url)

        if content:
            if bot_blocked:
                # 反爬页面被 trafilatura 误提取（如中文 "安全验证" 页面的纯文本）
                # 对提取内容做二次关键词检查，防反爬文本混入管线
                if is_bot_challenge_html(content):
                    extraction_status = "failed"
                    content = article.get("summary", "")
                else:
                    # 残余 Cloudflare 标记不影响正文质量，以 trafilatura 结果为准
                    extraction_status = "success"
                    content = apply_truncation(content, source_config)
            else:
                # 正文提取成功且无反爬标记，正常成功路径
                extraction_status = "success"
                content = apply_truncation(content, source_config)
        elif bot_blocked:
            # 反爬页面 + trafilatura 确认失败 → 标记为 failed（非 partial）
            # 区别于 "内容提取失败"，明确根因是反爬拦截
            extraction_status = "failed"
            content = article.get("summary", "")
        else:
            # HTML 拿到了但 trafilatura 无法提取正文（非反爬原因），用 manifest summary 兜底
            extraction_status = "partial"
            content = article.get("summary", "")
    else:
        # HTML 获取失败（Playwright 渲染失败或超时），用 manifest 元数据兜底
        meta = {}
        extraction_status = "failed"
        content = article.get("summary", "")

    # 构建失败/部分提取时的提示语
    if extraction_status == "failed":
        if bot_blocked:
            body = f"> **⚠️ 正文抓取失败**：Playwright 渲染后仍检测到反爬拦截，无法提取正文\n\n{content}".strip()
        else:
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
        created=created,
    )

    output_path = target_dir / f"{article_id}.md"
    write_frontmatter(output_path, fm, body)

    # 标记为已处理（线程安全）
    state.mark_seen(article_id)

    return output_path


def _try_producthunt_ingest(
    article: dict,
    source_name: str,
    target_dir: Path,
    state: "IngestState",
    source_config: dict,
    article_id: str,
    created: Optional[str] = None,
    session: Optional["BrowserSession"] = None,
) -> Optional[Path]:
    """
    使用 Product Hunt 专用兜底抓取产品页。

    设计理由：
        Product Hunt 产品页会把通用 curl/Playwright 引向反爬页。专用逻辑
        会把产品页可公开读取的核心字段整理成稳定 Markdown，避免失败摘要
        流入后续 LLM 阶段。
    """
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.ingestion.ingest.producthunt import fetch_producthunt_article
    from pipeline.utils.frontmatter import write_frontmatter

    result = fetch_producthunt_article(article, source_config, session=session)
    if result is None:
        return None

    url = article.get("url", "")
    fm = build_ingestion_frontmatter(
        title=result.title or article.get("title", ""),
        url=url,
        published=article.get("published", ""),
        author=article.get("author", ""),
        description=result.description or article.get("summary", ""),
        source_name=source_name,
        article_id=article_id,
        extraction_status="success",
        created=created,
    )

    output_path = target_dir / f"{article_id}.md"
    write_frontmatter(output_path, fm, apply_truncation(result.content, source_config))
    state.mark_seen(article_id)
    logger.info("Product Hunt 专用兜底成功 source=%s url=%s", source_name, url)
    return output_path


def _try_hackernews_ingest(
    article: dict,
    source_name: str,
    target_dir: Path,
    state: "IngestState",
    source_config: dict,
    article_id: str,
    created: Optional[str] = None,
) -> Optional[Path]:
    """
    使用 Hacker News 条目的备用链接修复少数高价值文章的抓取失败。

    设计理由：
        HN manifest 的 summary 经常包含 archive.ph/archive.md 备份链接；
        StackExchange 页面也可通过官方 StackPrinter 输出绕过前端安全验证。
        这些备用入口只在 HN 源内使用，避免改变其他数据源的抓取语义。
    """
    from pipeline.core.frontmatter_utils import build_ingestion_frontmatter
    from pipeline.core.web_utils import extract_article_content, extract_metadata, fetch_url, is_bot_challenge_html
    from pipeline.utils.frontmatter import write_frontmatter

    original_url = article.get("url", "")
    candidates = _build_hackernews_candidate_urls(article)
    if len(candidates) <= 1:
        return None

    timeout = source_config.get("timeout", 30)
    for candidate_url in candidates[1:]:
        html = fetch_url(candidate_url, timeout=timeout)
        if not html or is_bot_challenge_html(html):
            continue

        meta = extract_metadata(html, candidate_url)
        content = extract_article_content(html, candidate_url)
        if not content or _is_hackernews_fallback_error(content):
            continue

        fm = build_ingestion_frontmatter(
            title=meta.get("title") or article.get("title", ""),
            url=original_url,
            published=meta.get("date") or article.get("published", ""),
            author=meta.get("author") or article.get("author", ""),
            description=meta.get("description") or article.get("summary", ""),
            source_name=source_name,
            article_id=article_id,
            extraction_status="success",
            created=created,
        )
        output_path = target_dir / f"{article_id}.md"
        body = (
            f"> 备用抓取来源：{candidate_url}\n\n"
            f"{apply_truncation(content, source_config)}"
        )
        write_frontmatter(output_path, fm, body)
        state.mark_seen(article_id)
        logger.info("Hacker News 备用链接抓取成功 source=%s url=%s fallback=%s", source_name, original_url, candidate_url)
        return output_path

    return None


def _build_hackernews_candidate_urls(article: dict) -> list[str]:
    """
    为 HN 条目构造按优先级排列的抓取 URL。

    返回值始终以原始 URL 开头，后续才是 archive/StackPrinter 等备用入口。
    """
    url = article.get("url", "")
    summary = article.get("summary", "")
    candidates = [url] if url else []

    for match in re.finditer(r"https?://(?:archive\.(?:ph|md|is|today))/[^\s<>)]+", summary):
        candidates.append(match.group(0))

    stackprinter_url = _build_stackprinter_url(url)
    if stackprinter_url:
        candidates.append(stackprinter_url)

    seen: set[str] = set()
    unique_candidates: list[str] = []
    for candidate in candidates:
        if candidate and candidate not in seen:
            unique_candidates.append(candidate)
            seen.add(candidate)
    return unique_candidates


def _build_stackprinter_url(url: str) -> Optional[str]:
    """
    将 StackExchange 问题页转换为 StackPrinter 导出 URL。

    StackPrinter 是 StackExchange 官方提供的轻量 HTML 输出，比常规页面
    更适合离线抓取，也能避开部分前端安全验证页面。
    """
    parsed = urlparse(url)
    if not parsed.netloc.endswith("stackexchange.com"):
        return None

    match = re.search(r"/questions/(\d+)", parsed.path)
    if not match:
        return None

    question_id = match.group(1)
    service = parsed.netloc.removesuffix(".com")
    return (
        "https://stackprinter.appspot.com/export"
        f"?question={question_id}"
        f"&service={service}"
        "&language=en"
        "&hideAnswers=false"
        "&showAll=true"
        "&width=700"
    )


def _is_hackernews_fallback_error(content: str) -> bool:
    """
    判断 HN 备用入口是否返回了工具错误页。

    StackPrinter 参数错误时也会返回可提取文本，必须显式拒绝，避免把
    "Unsupported service" 这类错误页写成 success。
    """
    lowered = content.lower()
    return "unsupported service" in lowered or "server too busy" in lowered
