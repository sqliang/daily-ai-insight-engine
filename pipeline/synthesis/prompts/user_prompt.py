"""
Stage 4b Editor-in-Chief user prompt builder

从 all_articles.json 构建包含统计摘要 + Top-N 文章详情 + 剩余文章列表的用户提示词。
"""

import json
from collections import Counter
from typing import Optional


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

    # --- 专题标注统计 (Phase 1: GitHub) ---
    github_domains: Counter = Counter()
    github_ai_cats: Counter = Counter()
    github_count = 0

    for a in articles:
        spec_tags = a.get("specialized_tags", {})
        if isinstance(spec_tags, dict):
            gh = spec_tags.get("github")
            if isinstance(gh, dict):
                github_count += 1
                domain = gh.get("domain", "other")
                github_domains[domain] += 1

                ai_detail = gh.get("aiDetail") or gh.get("ai_detail")
                if isinstance(ai_detail, dict):
                    for cat in ai_detail.get("primaryCategories", []) or []:
                        github_ai_cats[cat] += 1

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
        "specialized_stats": {
            "github": {
                "count": github_count,
                "domain_distribution": dict(github_domains),
                "ai_category_distribution": dict(github_ai_cats) if github_ai_cats else None,
            },
        },
    }


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


def build_user_prompt(all_articles: list[dict], max_detail: int = 30, target_date: Optional[str] = None) -> str:
    """
    构造 Editor-in-Chief 的用户提示词。

    结构：
        0. 报告日期（当指定 target_date 时）
        1. 统计概览（全部文章）
        2. Top-N 文章完整 frontmatter
        3. 剩余文章标题列表

    参数：
        all_articles: 所有文章记录列表
        max_detail: 包含完整 frontmatter 的文章数上限
        target_date: 目标报告日期（YYYY-MM-DD），None 时使用 today
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

    # 专题标注统计
    spec_stats = stats.get("specialized_stats", {})
    gh_stats = spec_stats.get("github", {})
    if gh_stats.get("count", 0) > 0:
        sections.extend([
            "",
            "### Specialized Tags: GitHub Trending",
            f"  Total GitHub projects: {gh_stats['count']}",
            f"  Domain distribution: {_format_distribution(gh_stats.get('domain_distribution', {}))}",
        ])
        if gh_stats.get("ai_category_distribution"):
            sections.append(f"  AI sub-category distribution: {_format_distribution(gh_stats['ai_category_distribution'])}")

    sections.extend([
        "",
        f"## 2. TOP {len(top_articles)} ARTICLES BY IMPACT SCORE (FULL ANALYSIS)",
        "",
    ])
    for i, article in enumerate(top_articles, 1):
        sections.append(_format_article_detail(article, i))
        sections.append("")

    sections.extend([
        f"## 3. REMAINING {len(remaining)} ARTICLES (TITLES + KEY STATS ONLY)",
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
        "## 4. INSTRUCTIONS",
        "",
        f"Generate the daily report JSON based on the data above. Key reminders:",
        f"- eventTypeDistribution and sentimentDistribution must aggregate from ALL {len(sorted_articles)} articles using the statistical overview",
        f"- topEvents: select 5, prioritize high impactScore + high informationEntropy, cross-reference across sources",
        f"- deepDives: select 3 strategically significant events (consider compoundValue and moatImpact)",
        f"- trendInsights: cover all 4 dimensions (technology, application, policy, capital)",
        f"- riskSignals/opportunitySignals: 4-7 each, grounded in source articles' risk_matrix and market_opportunities",
        f"- entityFrequency: merge companies, technologies, and keyPeople from entities field across ALL articles",
        f"- specializedBrief: if specialized_stats shows github projects, output githubHighlights with summary, topProjects, domainDistribution, and aiCategoryDistribution from the stats",
        f"- Language: Chinese for all text fields, English for enum values",
        f"- Output ONLY valid JSON, no markdown wrappers",
    ])

    return "\n".join(sections)
