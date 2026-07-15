"""
pipeline/extraction/repair.py — 自动修复 extract 失败的文章

扫描 data/02_extracted/ 中 extract_result 为 failed 的文章，
重新运行 extract_base_info() 和 extract_fact_extraction()。
如果正文疑似反爬页面（Cloudflare 验证等），先用 Jina AI Reader 兜底获取真实内容。

作为 Stage 2c，可在 extract 完成后按需调用：
    uv run python pipeline/run.py extract-repair [--target-date YYYY-MM-DD]

设计理由：
    与 pipeline/ingestion/repair.py 保持一致的扫描-修复-汇总模式，
    只是目标目录从 01_raw 变为 02_extracted，修复手段从 BrowserSession
    变为 force re-extract + Jina AI 兜底。
"""

import asyncio
import logging
from datetime import date
from pathlib import Path

from pipeline.core.config_loader import resolve_data_dir
from pipeline.utils.frontmatter import read_frontmatter, write_frontmatter

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Jina AI 兜底
# ---------------------------------------------------------------------------


def _try_jina_fallback(url: str) -> str | None:
    """
    使用 Jina AI Reader 获取干净的 Markdown 内容。
    委托给 pipeline.core.web_utils.fetch_via_jina()，方便 Stage 1b 和 Stage 2c 共用。
    """
    from pipeline.core.web_utils import fetch_via_jina
    return fetch_via_jina(url)


def _body_looks_like_antibot(body: str) -> bool:
    """
    检测正文是否疑似反爬验证页面。

    判断依据：同时命中 2 个以上 Cloudflare/JS Challenge 关键词。

    参数：
        body: 文章正文文本

    返回：
        True 如果正文疑似反爬页面
    """
    if not body:
        return False
    lower = body.lower()
    indicators = [
        "cloudflare",
        "verify you are a human",
        "enable javascript",
        "just a moment",
        "checking your browser",
        "ddos protection",
        "正在进行安全验证",
        "安全服务防护",
    ]
    return sum(1 for i in indicators if i in lower) >= 2


# ---------------------------------------------------------------------------
# 主修复函数
# ---------------------------------------------------------------------------

def repair_failed_extractions(
    target_date: date | None = None,
    model: str | None = None,
) -> dict:
    """
    扫描 data/02_extracted/ 中所有 extract_result 为 failed 的文章，
    重新执行 extract_base_info() + extract_fact_extraction()。

    对于正文疑似反爬页面的文章，先尝试 Jina AI 兜底获取真实内容。

    参数：
        target_date: 只修复 created == target_date 的文章（None = 今天）
        model: LLM 模型名称（None 时从 config.yaml 读取）

    返回：
        dict: {total: 发现数, repaired: 修复成功数, still_failed: 仍失败数, repaired_files: [...]}
    """
    if target_date is None:
        target_date = date.today()

    extracted_dir = resolve_data_dir("extracted")
    target_date_str = target_date.isoformat()

    # --- 发现失败文件 ---
    failed_files: list[Path] = []
    for fp in sorted(extracted_dir.rglob("*.md")):
        if not fp.is_file():
            continue
        # 跳过不在 source 子目录下的文件
        if fp.parent == extracted_dir:
            continue
        try:
            fm, _ = read_frontmatter(fp)
        except Exception:
            continue

        extract_result = fm.get("extract_result", "")
        created = fm.get("created", "")
        # 兼容 date 对象和字符串
        if isinstance(created, date):
            created_str = created.isoformat()
        else:
            created_str = str(created)[:10]

        if extract_result == "failed" and created_str == target_date_str:
            failed_files.append(fp)

    total = len(failed_files)
    if total == 0:
        logger.info("Extract-Repair: 未发现需要修复的文章")
        return {"total": 0, "repaired": 0, "still_failed": 0, "repaired_files": []}

    print(f"\nExtract-Repair: 发现 {total} 篇需要修复的文章")

    repaired = 0
    still_failed = 0
    repaired_files: list[str] = []

    for fp in failed_files:
        try:
            fm, body = read_frontmatter(fp)
        except Exception:
            still_failed += 1
            continue

        title = fm.get("title", fp.name)
        source_url = fm.get("source", "")
        rel_path = fp.relative_to(extracted_dir)

        # --- Jina AI 兜底：正文疑似反爬页面 ---
        if _body_looks_like_antibot(body) and source_url:
            jina_body = _try_jina_fallback(source_url)
            if jina_body:
                write_frontmatter(fp, fm, jina_body)
                body = jina_body
                print(f"  📥 Jina AI 兜底成功: {title[:60]}")
                logger.info("Jina AI 兜底成功: %s", title[:60])

        # --- 重新运行 extract_base_info + extract_fact_extraction ---
        print(f"  🔧 重新提取: {title[:60]}")
        base_info_ok = True
        fact_ok = True

        try:
            from pipeline.extraction.base_info.extractor import extract_base_info
            from pipeline.extraction.fact_extraction.extractor import extract_fact_extraction

            async def _repair_single():
                nonlocal base_info_ok, fact_ok
                r1 = await extract_base_info(
                    input_path=fp,
                    output_path=fp,
                    model=model,
                    skip_existing=False,
                )
                base_info_ok = r1.success
                if not r1.success:
                    return
                r2 = await extract_fact_extraction(
                    input_path=fp,
                    output_path=fp,
                    model=model,
                    skip_existing=False,
                )
                fact_ok = r2.success

            loop = asyncio.new_event_loop()
            try:
                loop.run_until_complete(_repair_single())
            finally:
                loop.close()

        except Exception as exc:
            logger.error("Extract-Repair 异常 %s: %s", fp, exc)
            base_info_ok = False
            fact_ok = False

        # --- 更新 extract_result ---
        try:
            fm, body = read_frontmatter(fp)
            if base_info_ok and fact_ok:
                fm["extract_result"] = "success"
                write_frontmatter(fp, fm, body)
                repaired += 1
                repaired_files.append(str(rel_path))
                print(f"  ✅ 修复成功: {title[:60]}")
            else:
                fm["extract_result"] = "failed"
                write_frontmatter(fp, fm, body)
                still_failed += 1
                error_detail = "BaseInfo 失败" if not base_info_ok else "FactExtraction 失败"
                print(f"  ❌ 修复失败 ({error_detail}): {title[:60]}")
        except Exception:
            still_failed += 1
            print(f"  ❌ 状态写入失败: {title[:60]}")

    result = {
        "total": total,
        "repaired": repaired,
        "still_failed": still_failed,
        "repaired_files": repaired_files,
    }
    logger.info(
        "Extract-Repair 完成: total=%d repaired=%d still_failed=%d",
        total, repaired, still_failed,
    )
    return result
