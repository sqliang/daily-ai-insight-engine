"""
pipeline/ingestion/ingest/truncation.py — 正文截断规则

支持三种截断模式（由 config.yaml 中每个源的 truncation 字段控制）：
  - first_n_chars: 保留前 N 个字符，在段落边界截断
  - abstract_only: 仅保留 "> Abstract" 开头的块引用段落
  - none: 不截断

消费方：worker.py 中的 ingest_article() / ingest_browser_article()。
"""


def apply_truncation(body: str, source_config: dict) -> str:
    """
    按源配置的 truncation 规则裁剪正文长度。

    source_config.truncation 字段：
        mode: "first_n_chars" (默认) | "abstract_only" | "none"
        limit: int (默认 3000，仅 first_n_chars 模式使用)
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
                    continue
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
