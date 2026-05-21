"""
pipeline/ingestion/ingest/orchestrator.py — Stage 1b 正文抓取业务逻辑

负责从 manifest 清单读取文章 URL，逐篇抓取正文并写入 .md 文件。
提供 run_ingest() 主编排函数，被 cli.py 消费。

设计理由:
    将业务逻辑与 CLI 契约分离到不同文件，遵循 scout 包结构模式。
"""

import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

# 确保项目根目录在 sys.path 中，支持从任意目录运行
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from pipeline.core.config_loader import get_source_by_name
from pipeline.core.file_utils import (
    ensure_dir,
    read_json,
    resolve_data_dir,
    resolve_state_file,
    write_json,
)
from pipeline.core.frontmatter_utils import build_ingestion_frontmatter, write_frontmatter
from pipeline.core.id_utils import generate_id
from pipeline.core.web_utils import extract_article_content, extract_metadata, fetch_url


def _ensure_browser_session():
    """创建浏览器会话，仅在需要 browser fetch_strategy 时调用。"""
    from pipeline.core.browser_utils import BrowserSession
    return BrowserSession()


def run_ingest(manifest_name: Optional[str] = None, force: bool = False) -> List[Path]:
    """
    主入口：读取清单文件，抓取正文，生成 .md 文件。

    参数:
        manifest_name: 指定清单文件名 (不含路径)，为 None 时处理今日所有清单。
        force: 忽略去重状态，强制重新抓取。

    返回:
        生成的文件路径列表。
    """
    today_str = date.today().isoformat()
    manifest_dir = resolve_data_dir("manifest")
    raw_dir = resolve_data_dir("raw")

    # 选择要处理的清单文件
    if manifest_name:
        manifest_paths = [manifest_dir / manifest_name]
    else:
        manifest_paths = sorted(manifest_dir.glob(f"*_{today_str}.json"))

    if not manifest_paths:
        print("未找到清单文件，请先运行 scout")
        return []

    # 加载去重状态
    state = _load_state()
    seen_hashes: Set[str] = set(state.get("seen_hashes", [])) if not force else set()

    # 检测是否有 browser 策略的源，提前创建 browser session
    needs_browser = False
    for manifest_path in manifest_paths:
        manifest_data = read_json(manifest_path)
        if manifest_data:
            src = get_source_by_name(manifest_data.get("source", ""))
            if src and src.get("fetch_strategy") == "browser":
                needs_browser = True
                break
    browser_session = None
    if needs_browser:
        browser_session = _ensure_browser_session().__enter__()

    output_files: List[Path] = []
    total_ingested = 0
    total_skipped = 0

    try:
        for manifest_path in manifest_paths:
            manifest = read_json(manifest_path)
            if not manifest:
                continue

            source_name = manifest.get("source", "")
            source_config = get_source_by_name(source_name) or {}
            target_dir_name = source_config.get("target_dir", source_name)
            target_dir = raw_dir / target_dir_name
            ensure_dir(target_dir)

            articles = manifest.get("articles", [])
            print(f"\n处理: {source_name} ({len(articles)} 篇) → {target_dir_name}/")

            for article in articles:
                url = article.get("url", "")
                if not url:
                    continue

                # 去重检查：使用 00_manifest 阶段生成的 SHA-256 ID 替代旧的 MD5 哈希
                article_id = article.get("id") or generate_id(url)
                if not force and article_id in seen_hashes:
                    total_skipped += 1
                    continue

                print(f"  [抓取] {article.get('title', url)[:60]}...")

                result = _ingest_one(article, source_config, browser_session)
                if result is None:
                    print(f"         失败: 无法提取正文")
                    continue

                # 使用预生成的文章 ID 作为文件名
                output_path = target_dir / f"{article_id}.md"

                # 构建 frontmatter + 正文
                fm = build_ingestion_frontmatter(
                    title=result.get("title") or article.get("title", ""),
                    url=url,
                    published=result.get("published") or article.get("published", ""),
                    author=result.get("author") or article.get("author", ""),
                    description=result.get("description") or article.get("summary", ""),
                    source_name=source_name,
                    article_id=article_id,
                )

                # 正文截断
                body = result.get("content", "")
                body = _apply_truncation(body, source_config)

                write_frontmatter(output_path, fm, body)
                output_files.append(output_path)

                # 更新去重状态（使用统一的 SHA-256 ID 替代旧的 MD5 hash）
                seen_hashes.add(article_id)
                total_ingested += 1

    finally:
        if browser_session:
            browser_session.__exit__(None, None, None)

    # 持久化去重状态
    state["seen_hashes"] = sorted(seen_hashes)
    state["last_ingest"] = datetime.now(timezone.utc).isoformat()
    _save_state(state)

    print(f"\n=== 完成: 新增 {total_ingested} 篇, 跳过 {total_skipped} 篇 ===")
    return output_files


def _ingest_one(article: dict, source_config: dict, browser_session=None) -> Optional[dict]:
    """
    抓取单篇文章：获取 HTML → 提取元数据 → 提取正文。

    当 source 的 fetch_strategy 为 browser 时，使用 Playwright 获取渲染后 HTML。

    返回:
        {"title", "author", "published", "description", "content"} 或 None。
    """
    url = article.get("url", "")
    timeout = source_config.get("timeout", 30)
    strategy = source_config.get("fetch_strategy", "rss")

    if strategy == "browser":
        wait_for = source_config.get("wait_for")
        if browser_session:
            html = browser_session.fetch_page_html(
                url, wait_for=wait_for, timeout=timeout * 1000
            )
        else:
            from pipeline.core.browser_utils import fetch_rendered_html
            html = fetch_rendered_html(
                url, wait_for=wait_for, timeout=timeout * 1000
            )
    else:
        html = fetch_url(url, timeout=timeout)

    if not html:
        return None

    meta = extract_metadata(html, url)
    content = extract_article_content(html, url)
    if not content:
        return None

    return {
        "title": meta.get("title") or article.get("title", ""),
        "author": meta.get("author") or article.get("author", ""),
        "published": meta.get("date") or article.get("published", ""),
        "description": meta.get("description") or article.get("summary", ""),
        "content": content,
    }


# ================================================================
# 正文截断
# ================================================================

def _apply_truncation(body: str, source_config: dict) -> str:
    """
    按源配置的 truncation 规则裁剪正文长度。

    支持三种模式:
        - first_n_chars: 保留前 N 个字符
        - abstract_only: 仅保留摘要段 (以 '> Abstract' 开头的块引用)
        - none: 不裁剪
    """
    trunc = source_config.get("truncation", {})
    mode = trunc.get("mode", "first_n_chars")

    if mode == "none":
        return body
    elif mode == "abstract_only":
        lines = body.split("\n")
        abstract_lines = []
        in_abstract = False
        for line in lines:
            if line.strip().startswith("> Abstract"):
                in_abstract = True
                abstract_lines.append(line)
            elif in_abstract:
                if line.strip().startswith(">"):
                    abstract_lines.append(line)
                elif line.strip() == "" and abstract_lines:
                    continue  # 空行可能还在 abstract 内部
                else:
                    if line.strip() and not line.startswith(">"):
                        break
        return "\n".join(abstract_lines) if abstract_lines else body[:3000]
    elif mode == "first_n_chars":
        limit = trunc.get("limit", 3000)
        if len(body) > limit:
            # 在最近的段落边界处截断
            cut = body.rfind("\n\n", 0, limit)
            if cut > limit // 2:
                return body[:cut].strip()
            return body[:limit]
        return body
    else:
        return body


# ================================================================
# 去重状态管理
# ================================================================

def _get_state_path() -> Path:
    """去重状态文件路径（从 config.yaml 读取）。"""
    return resolve_state_file()


def _load_state() -> dict:
    """
    加载去重状态。

    自动检测并迁移旧格式：旧版 ingest.py 使用 MD5 哈希（12 位），
    新版统一为 SHA-256 ID（16 位）。检测到旧格式时自动重置去重列表。
    """
    path = _get_state_path()
    if not path.exists():
        return {"seen_hashes": [], "last_ingest": ""}

    state = read_json(path) or {"seen_hashes": [], "last_ingest": ""}
    hashes = state.get("seen_hashes", [])

    # 检测旧格式 MD5 哈希（12 位）→ 重置为空白列表
    if hashes and len(hashes[0]) == 12:
        print("  [迁移] 检测到旧格式 MD5 去重数据（12位），已自动切换为 SHA-256 ID（16位）")
        state["seen_hashes"] = []

    return state


def _save_state(state: dict) -> None:
    """持久化去重状态。"""
    write_json(_get_state_path(), state)
