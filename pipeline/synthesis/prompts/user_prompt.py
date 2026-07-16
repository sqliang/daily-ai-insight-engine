"""
pipeline/synthesis/prompts/user_prompt.py — Stage 4b Editor-in-Chief user prompt builder

从 all_articles.json 构建用户提示词，包含：
    - 统计摘要（文章数、信源覆盖、语言分布、实体频次）
    - Top-N 文章的完整 frontmatter
    - 剩余文章标题列表
    - 项目 / 产品洞察候选文章的统计概览与候选对象

专题洞察上下文：
    项目洞察候选主要来自 source_dir == "github-trending" 且带有 specialized_tags.github
    的文章；产品洞察候选主要来自 producthunt / whytryai 且带有 specialized_tags.product
    的文章。候选对象经去重后注入 prompt，供主编 Agent 生成 specializedBrief 中的
    githubHighlights / projectInsights / productHighlights / productInsights。
    论文洞察当前由 Agent 基于 arxiv-cs-ai 及 specialized_tags.paper 文章归纳，
    不单独构造候选区。
"""

from collections import Counter
from typing import Optional


# GitHub 项目领域中文标签映射（仅用于 prompt 展示）
_GITHUB_DOMAIN_LABELS = {
    "ai_ml": "AI/ML",
    "web_frontend": "Web 前端",
    "web_backend": "Web 后端",
    "devops_infra": "DevOps",
    "database_storage": "数据库",
    "programming_languages": "编程语言",
    "developer_tools": "开发者工具",
    "security": "安全",
    "mobile": "移动端",
    "blockchain": "区块链",
    "data_engineering": "数据工程",
    "game_development": "游戏开发",
    "documentation": "文档",
    "iot_embedded": "IoT/嵌入式",
    "other": "其他",
}

# 产品发布上下文中文标签映射（仅用于 prompt 展示）
_PRODUCT_LAUNCH_LABELS = {
    "new_launch": "新产品",
    "major_update": "重大更新",
    "pivot": "战略转型",
    "funding_announcement": "融资发布",
}

# 产品定价模式中文标签映射（仅用于 prompt 展示）
_PRODUCT_PRICING_LABELS = {
    "freemium": "Freemium",
    "subscription": "订阅制",
    "usage_based": "按量计费",
    "open_source": "开源",
    "free": "免费",
    "enterprise": "企业版",
    "unknown": "未公布",
}


def _compute_statistics(articles: list[dict]) -> dict:
    """从所有文章中计算统计分布。"""
    event_type_dist = Counter()
    sentiment_dist = Counter()
    source_type_dist = Counter()
    epistemic_dist = Counter()
    source_dist = Counter()
    entity_freq: Counter = Counter()

    for a in articles:
        event_type_dist[a.get("event_type", "unknown")] += 1
        sentiment_dist[a.get("sentiment", "neutral")] += 1
        source_type_dist[a.get("source_type", "unknown")] += 1
        epistemic_dist[a.get("epistemic_status", "unknown")] += 1
        source_dist[a.get("source_dir", "unknown")] += 1

        entities = a.get("entities", {})
        if isinstance(entities, dict):
            for company in entities.get("companies", []) or []:
                entity_freq[(company, "company")] += 1
            for tech in entities.get("technologies", []) or []:
                entity_freq[(tech, "technology")] += 1
            for person in entities.get("key_people", []) or []:
                entity_freq[(person, "person")] += 1

    return {
        "event_type_distribution": dict(event_type_dist),
        "sentiment_distribution": dict(sentiment_dist),
        "source_type_distribution": dict(source_type_dist),
        "epistemic_status_distribution": dict(epistemic_dist),
        "source_distribution": dict(source_dist),
        "entity_frequencies": [
            {"entity": entity, "count": count, "type": etype}
            for (entity, etype), count in entity_freq.most_common(50)
        ],
    }


def _compute_github_statistics(github_articles: list[dict]) -> dict:
    """
    从项目洞察候选文章中计算当日简报所需的统计分布。

    统计项：
        - total: 项目总数（已跨天去重后）
        - domain_distribution: 通用领域分布
        - ai_category_distribution: AI 子领域分布（仅汇总 ai_detail.primary_categories）
        - top_projects: 项目名列表，按原始顺序保留

    参数：
        github_articles: source_dir == "github-trending" 的文章列表

    返回：
        dict: {total, domain_distribution, ai_category_distribution, top_projects}
    """
    domain_dist: Counter = Counter()
    ai_cat_dist: Counter = Counter()
    top_projects: list[str] = []

    for a in github_articles:
        gh = a.get("specialized_tags", {}).get("github", {}) if isinstance(a.get("specialized_tags"), dict) else {}
        project_name = gh.get("project_name") or gh.get("projectName") or a.get("title", "")
        if project_name:
            top_projects.append(project_name)

        domain = gh.get("domain") or "other"
        domain_dist[domain] += 1

        ai_detail = gh.get("ai_detail") or gh.get("aiDetail")
        if isinstance(ai_detail, dict):
            for cat in ai_detail.get("primary_categories") or ai_detail.get("primaryCategories") or []:
                ai_cat_dist[cat] += 1

    return {
        "total": len(github_articles),
        "domain_distribution": dict(domain_dist),
        "ai_category_distribution": dict(ai_cat_dist),
        "top_projects": top_projects,
    }


def _format_github_statistics(stats: dict) -> str:
    """格式化项目洞察统计为 prompt 文本。"""
    lines = [
        f"Total GitHub projects today: {stats['total']}",
        "",
        "### Domain Distribution",
        _format_distribution(
            stats["domain_distribution"],
            label_map=_GITHUB_DOMAIN_LABELS,
        ) if stats["domain_distribution"] else "  (no domain data)",
    ]

    if stats["ai_category_distribution"]:
        lines.extend([
            "",
            "### AI Category Distribution",
            _format_distribution(stats["ai_category_distribution"]),
        ])

    if stats["top_projects"]:
        lines.extend([
            "",
            "### Notable Projects",
        ])
        for i, name in enumerate(stats["top_projects"][:10], 1):
            lines.append(f"  {i}. {name}")

    return "\n".join(lines)


def _compute_product_statistics(product_articles: list[dict]) -> dict:
    """
    从产品洞察候选文章中计算当日简报所需的统计分布。

    统计项：
        - total: 产品总数（已跨天去重后）
        - launch_context_distribution: 发布上下文分布
        - pricing_model_distribution: 定价模式分布
        - top_products: 产品名列表，按原始顺序保留

    参数：
        product_articles: source_dir == "producthunt" 或 "whytryai" 的文章列表

    返回：
        dict: {total, launch_context_distribution, pricing_model_distribution, top_products}
    """
    launch_dist: Counter = Counter()
    pricing_dist: Counter = Counter()
    top_products: list[str] = []

    for a in product_articles:
        product = a.get("specialized_tags", {}).get("product", {}) if isinstance(a.get("specialized_tags"), dict) else {}
        product_name = product.get("product_name") or product.get("productName") or a.get("title", "")
        if product_name:
            top_products.append(product_name)

        launch_context = product.get("launch_context") or product.get("launchContext") or "unknown"
        launch_dist[launch_context] += 1

        pricing_model = product.get("pricing_model") or product.get("pricingModel") or "unknown"
        pricing_dist[pricing_model] += 1

    return {
        "total": len(product_articles),
        "launch_context_distribution": dict(launch_dist),
        "pricing_model_distribution": dict(pricing_dist),
        "top_products": top_products,
    }


def _format_product_statistics(stats: dict) -> str:
    """格式化产品洞察统计为 prompt 文本。"""
    lines = [
        f"Total AI products today: {stats['total']}",
        "",
        "### Launch Context Distribution",
        _format_distribution(
            stats["launch_context_distribution"],
            label_map=_PRODUCT_LAUNCH_LABELS,
        ) if stats["launch_context_distribution"] else "  (no launch context data)",
    ]

    if stats["pricing_model_distribution"]:
        lines.extend([
            "",
            "### Pricing Model Distribution",
            _format_distribution(
                stats["pricing_model_distribution"],
                label_map=_PRODUCT_PRICING_LABELS,
            ),
        ])

    if stats["top_products"]:
        lines.extend([
            "",
            "### Notable Products",
        ])
        for i, name in enumerate(stats["top_products"][:10], 1):
            lines.append(f"  {i}. {name}")

    return "\n".join(lines)


def _object_type_value(item: dict) -> str:
    """兼容 snake_case/camelCase 的 objectType 读取。"""
    return item.get("object_type") or item.get("objectType") or ""


def _object_key(item: dict) -> str:
    """为跨文章对象合并生成稳定 key。"""
    canonical = item.get("canonical_name") or item.get("canonicalName") or item.get("name") or ""
    url = item.get("url") or ""
    return f"{str(canonical).strip().lower()}|{str(url).strip().lower()}"


def _source_payload(article: dict) -> dict:
    """构造专题对象引用来源。"""
    return {
        "articleId": article.get("id", ""),
        "title": article.get("title", ""),
        "sourceDir": article.get("source_dir", ""),
        "url": article.get("source", ""),
    }


def _collect_object_candidates(articles: list[dict], object_type: str) -> list[dict]:
    """
    从所有文章聚合项目/产品对象候选。

    优先使用 Stage 3 object_insights；没有洞察时使用 Stage 2 object_mentions 兜底。
    同一对象按 canonicalName + url 合并，并保留所有 articleIds/sources/evidence。
    """
    merged: dict[str, dict] = {}

    for article in articles:
        source = _source_payload(article)
        article_id = source["articleId"]

        for insight in article.get("object_insights", []) or article.get("objectInsights", []) or []:
            if not isinstance(insight, dict) or _object_type_value(insight) != object_type:
                continue
            key = _object_key(insight)
            if not key.strip("|"):
                continue
            entry = merged.setdefault(key, {
                "name": insight.get("name") or insight.get("canonicalName") or insight.get("canonical_name", ""),
                "canonicalName": insight.get("canonical_name") or insight.get("canonicalName") or insight.get("name", ""),
                "url": insight.get("url"),
                "insights": [],
                "mentions": [],
                "articleIds": [],
                "sources": [],
                "evidenceSnippets": [],
            })
            entry["insights"].append(insight)
            for aid in insight.get("article_ids") or insight.get("articleIds") or [article_id]:
                if aid and aid not in entry["articleIds"]:
                    entry["articleIds"].append(aid)
            if source["url"] and source not in entry["sources"]:
                entry["sources"].append(source)
            for ev in insight.get("evidence_snippets") or insight.get("evidenceSnippets") or []:
                if ev and ev not in entry["evidenceSnippets"]:
                    entry["evidenceSnippets"].append(ev)

        for mention in article.get("object_mentions", []) or article.get("objectMentions", []) or []:
            if not isinstance(mention, dict) or _object_type_value(mention) != object_type:
                continue
            key = _object_key(mention)
            if not key.strip("|"):
                continue
            entry = merged.setdefault(key, {
                "name": mention.get("name") or mention.get("canonicalName") or mention.get("canonical_name", ""),
                "canonicalName": mention.get("canonical_name") or mention.get("canonicalName") or mention.get("name", ""),
                "url": mention.get("url"),
                "insights": [],
                "mentions": [],
                "articleIds": [],
                "sources": [],
                "evidenceSnippets": [],
            })
            entry["mentions"].append(mention)
            if article_id and article_id not in entry["articleIds"]:
                entry["articleIds"].append(article_id)
            if source["url"] and source not in entry["sources"]:
                entry["sources"].append(source)
            for ev in mention.get("evidence_snippets") or mention.get("evidenceSnippets") or []:
                if ev and ev not in entry["evidenceSnippets"]:
                    entry["evidenceSnippets"].append(ev)

    return sorted(
        merged.values(),
        key=lambda item: (
            -len(item["sources"]),
            -max([float(i.get("score", 0) or 0) for i in item["insights"]] or [0]),
            item["canonicalName"],
        ),
    )


def _format_object_candidates(title: str, candidates: list[dict]) -> str:
    """格式化对象候选，供主编 Agent 生成专题洞察。"""
    if not candidates:
        return f"## {title}\n\n(no object candidates)"

    lines = [f"## {title}", ""]
    for i, item in enumerate(candidates[:20], 1):
        lines.extend([
            f"### {i}. {item['canonicalName'] or item['name']}",
            f"URL: {item.get('url') or 'N/A'}",
            f"Article IDs: {', '.join(item['articleIds'])}",
            f"Sources: {json_like_sources(item['sources'])}",
            f"Evidence: {'; '.join(item['evidenceSnippets'][:5]) or 'N/A'}",
        ])
        if item["insights"]:
            lines.append("Stage 3 objectInsights:")
            for insight in item["insights"][:3]:
                lines.append(f"  - {insight}")
        else:
            lines.append("Stage 3 objectInsights: N/A")
        lines.append("")
    return "\n".join(lines)


def json_like_sources(sources: list[dict]) -> str:
    """压缩来源列表，避免 prompt 中出现过长 JSON。"""
    return "; ".join(
        f"{s.get('articleId')}|{s.get('sourceDir')}|{s.get('title')}"
        for s in sources[:6]
    )


def _format_distribution(dist: dict, label_map: dict = None) -> str:
    """格式化分布字典为文本。"""
    items = sorted(dist.items(), key=lambda x: x[1], reverse=True)
    lines = []
    for key, count in items:
        label = (label_map or {}).get(key, key)
        lines.append(f"  {label}: {count}")
    return "\n".join(lines)


def _format_article_detail(article: dict, index: int) -> str:
    """格式化单篇文章的完整 frontmatter 摘要。"""
    fields = [
        f"### {index}. {article.get('title', '无标题')}",
        f"  ID: {article.get('id', 'N/A')}",
        f"  来源: {article.get('source_dir', '?')} | 类型: {article.get('source_type', '?')}",
        f"  发布时间: {article.get('published', article.get('created', '?'))}",
        f"  TLDR: {article.get('tldr', '无')}",
        f"  事件类型: {article.get('event_type', '?')} | 认识论状态: {article.get('epistemic_status', '?')}",
    ]

    impact = article.get("impact_score", {})
    if isinstance(impact, dict):
        fields.append(f"  冲击力评分: {impact.get('score', '?')}/10 — {impact.get('reason', '')}")
    elif impact:
        fields.append(f"  冲击力评分: {impact}/10")

    dev_sent = article.get("developer_sentiment", {})
    if isinstance(dev_sent, dict):
        fields.append(f"  开发者情绪: {dev_sent.get('tone', '?')} — 焦点: {dev_sent.get('primary_focus', '')}")

    hype = article.get("hype_assessment", {})
    if isinstance(hype, dict):
        fields.append(f"  水分预警: {hype.get('level', '?')} — {hype.get('reason', '')}")

    fields.append(f"  信息熵: {article.get('information_entropy', '?')}")
    fields.append(f"  工程复杂度: {article.get('engineering_complexity', '?')}")

    domain = article.get("domain_disruption", {})
    if isinstance(domain, dict):
        fields.append(f"  技术突破: {domain.get('technical_innovation', 'N/A')}")
        fields.append(f"  商业模式: {domain.get('business_model', 'N/A')}")

    compound = article.get("compound_value", {})
    if isinstance(compound, dict):
        fields.append(f"  长期价值: {compound.get('score', '?')}/10 — {compound.get('reason', '')}")

    fields.append(f"  价值捕获层: {article.get('value_capture_layer', '?')}")
    fields.append(f"  护城河影响: {article.get('moat_impact', '?')}")
    fields.append(f"  关键受益方: {', '.join(article.get('key_beneficiaries', []))}")
    fields.append(f"  竞争受损方: {', '.join(article.get('competitive_casualty', []))}")

    opportunities = article.get("market_opportunities", [])
    if opportunities:
        fields.append(f"  市场机会: {'; '.join(opportunities)}")

    risk = article.get("risk_matrix", {})
    if isinstance(risk, dict):
        for rk, rv in risk.items():
            if rv and rv != "无" and rv != "[]":
                fields.append(f"  风险-{rk}: {rv}")

    fields.append(f"  行动建议: {article.get('actionable_insight', '?')}")

    logic = article.get("key_logic_flow", [])
    if logic:
        fields.append("  关键逻辑脉络:")
        for item in logic[:6]:
            fields.append(f"    - {item}")

    entities = article.get("entities", {})
    if isinstance(entities, dict):
        companies = entities.get("companies", [])
        techs = entities.get("technologies", [])
        people = entities.get("key_people", [])
        if companies or techs or people:
            fields.append(f"  实体: 公司={companies}, 技术={techs}, 人物={people}")

    return "\n".join(fields)


def build_user_prompt(
    all_articles: list[dict],
    max_detail: int = 30,
    target_date: Optional[str] = None,
    github_articles: Optional[list[dict]] = None,
    product_articles: Optional[list[dict]] = None,
) -> str:
    """
    构造 Editor-in-Chief 的用户提示词。

    结构：
        0. 报告日期（当指定 target_date 时）
        1. 统计概览（全部文章）
        2. 项目洞察统计（Phase 1 恢复）
        3. 产品洞察统计（Phase 2 恢复）
        4. Top-N 文章完整 frontmatter
        5. 剩余文章标题列表

    参数：
        all_articles: 所有文章记录列表
        max_detail: 包含完整 frontmatter 的文章数上限
        target_date: 目标报告日期（YYYY-MM-DD），None 时使用 today
        github_articles: 当日项目洞察候选文章列表（已跨天去重），None 或空时不生成项目统计
        product_articles: 当日产品洞察候选文章列表（已跨天去重），None 或空时不生成产品统计
    """
    # 按 impactScore 降序排列
    def _impact_score(a: dict) -> float:
        iscore = a.get("impact_score", {})
        if isinstance(iscore, dict):
            return float(iscore.get("score", 0))
        return float(iscore) if iscore else 0.0

    sorted_articles = sorted(all_articles, key=_impact_score, reverse=True)
    top_articles = sorted_articles[:max_detail]
    remaining = sorted_articles[max_detail:]

    stats = _compute_statistics(sorted_articles)
    project_candidates = _collect_object_candidates(sorted_articles, "project")
    product_candidates = _collect_object_candidates(sorted_articles, "product")

    # 确定报告日期：target_date 优先，否则用今天
    from datetime import date as _date
    report_date = target_date or _date.today().isoformat()

    sections = [
        f"## 0. REPORT DATE",
        "",
        f"The report date is **{report_date}**. All analysis and commentary should be written as of this date.",
        "",
        "## 1. STATISTICAL OVERVIEW (ALL ARTICLES)",
        "",
        f"Total articles: {len(sorted_articles)}",
        "",
        "### Event Type Distribution",
        _format_distribution(stats["event_type_distribution"]),
        "",
        "### Sentiment Distribution",
        _format_distribution(stats["sentiment_distribution"]),
        "",
        "### Source Type Distribution",
        _format_distribution(stats["source_type_distribution"]),
        "",
        "### Epistemic Status Distribution",
        _format_distribution(stats["epistemic_status_distribution"]),
        "",
        "### Source Distribution (by directory)",
        _format_distribution(stats["source_distribution"]),
        "",
        "### Top Entities by Frequency (companies, technologies, people)",
    ]
    for item in stats["entity_frequencies"][:50]:
        sections.append(f"  {item['entity']} ({item['type']}): {item['count']}")

    # 项目洞察统计（Phase 1 恢复）
    if github_articles:
        gh_stats = _compute_github_statistics(github_articles)
        sections.extend([
            "",
            "## 2. GITHUB SPECIALIZED OVERVIEW (DEDUPLICATED DAILY BRIEF)",
            "",
            _format_github_statistics(gh_stats),
        ])

    # 产品洞察统计（Phase 2 恢复）
    if product_articles:
        product_stats = _compute_product_statistics(product_articles)
        sections.extend([
            "",
            "## 3. PRODUCT SPECIALIZED OVERVIEW (DEDUPLICATED DAILY BRIEF)",
            "",
            _format_product_statistics(product_stats),
        ])

    sections.extend([
        "",
        "## 3A. PROJECT OBJECT CANDIDATES (ALL ARTICLES, MERGED BY CANONICAL NAME + URL)",
        "",
        _format_object_candidates("Project candidates", project_candidates),
        "",
        "## 3B. PRODUCT OBJECT CANDIDATES (ALL ARTICLES, MERGED BY CANONICAL NAME + URL)",
        "",
        _format_object_candidates("Product candidates", product_candidates),
    ])

    sections.extend([
        "",
        f"## 4. TOP {len(top_articles)} ARTICLES BY IMPACT SCORE (FULL ANALYSIS)",
        "",
    ])
    for i, article in enumerate(top_articles, 1):
        sections.append(_format_article_detail(article, i))
        sections.append("")

    sections.extend([
        f"## 5. REMAINING {len(remaining)} ARTICLES (TITLES + KEY STATS ONLY)",
        "",
    ])
    for i, article in enumerate(remaining, 1):
        iscore = _impact_score(article)
        sections.append(
            f"  {i}. [{article.get('source_dir', '?')}] {article.get('title', '无标题')} "
            f"| impact={iscore} | event={article.get('event_type', '?')} "
            f"| sentiment={article.get('sentiment', '?')}"
        )

    sections.extend([
        "",
        "## 6. INSTRUCTIONS",
        "",
        f"Generate the daily report JSON based on the data above. Key reminders:",
        f"- eventTypeDistribution and sentimentDistribution must aggregate from ALL {len(sorted_articles)} articles using the statistical overview",
        f"- topEvents: select 5, prioritize high impactScore + high informationEntropy, cross-reference across sources",
        f"- deepDives: select 3 strategically significant events (consider compoundValue and moatImpact)",
        f"- trendInsights: cover all 4 dimensions (technology, application, policy, capital)",
        f"- riskSignals/opportunitySignals: 4-7 each, grounded in source articles' risk_matrix and market_opportunities",
        f"- entityFrequency: merge companies, technologies, and keyPeople from entities field across ALL articles",
        f"- specializedBrief.githubHighlights: ONLY output when GitHub statistics are provided above. Use the exact articleCount, domainDistribution, and topProjects from the GitHub overview. Do NOT fabricate.",
        f"- specializedBrief.productHighlights: ONLY output when product statistics are provided above. Use the exact articleCount, launchContextDistribution, and notableProducts from the product overview. Do NOT fabricate.",
        f"- specializedBrief.projectInsights: output when Project candidates are provided above. Merge duplicate objects by canonicalName + url. Every item must include at least one articleIds entry and sources entry.",
        f"- specializedBrief.productInsights: output when Product candidates are provided above. Merge duplicate objects by canonicalName + url. Every item must include at least one articleIds entry and sources entry.",
        f"- For projectInsights/productInsights, prioritize objectInsights when available and use objectMentions as fallback evidence. Do NOT create objects that are absent from the candidate sections.",
        f"- Do NOT output paperHighlights.",
        f"- Language: Chinese for all text fields, English for enum values",
        f"- Output ONLY valid JSON, no markdown wrappers",
    ])

    return "\n".join(sections)
