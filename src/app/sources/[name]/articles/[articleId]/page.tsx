// ============================================================================
// /sources/[name]/articles/[articleId] — 数据源文章详情页
//
// 将单篇文章呈现为站点统一风格的情报详情页：顶部复用 source hero 的深色
// 情报看板语言，正文用卡片分区完整展示 extraction 与 analyze 结果。
// ============================================================================

import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { PageShell } from "@/components/layout/PageShell";
import { ArticleDecisionAnalysis, ArticleImpactAnalysis } from "@/components/sources/ArticleDetailAnalysis";
import { ArticleCardExtraction } from "@/components/sources/ArticleCardExtraction";
import { EntityChips } from "@/components/sources/EntityChips";
import { StatusBadge } from "@/components/sources/StatusBadge";
import {
  getSourceArticleDetail,
  type DateRange,
  type EnrichedArticle,
} from "@/lib/data/sources";
import { buildArticleDetailHref } from "@/lib/data/sources/article-route";
import {
  ACTIONABLE_INSIGHT_LABELS,
  EPISTEMIC_STATUS_LABELS,
  EVENT_TYPE_LABELS,
  HYPE_LEVEL_LABELS,
  SENTIMENT_LABELS,
} from "@/lib/data/status";
import { SOURCE_TYPE_LABELS } from "@/lib/data/tiers";

export const dynamic = "force-dynamic";

type PageProps = {
  params: Promise<{ name: string; articleId: string }>;
  searchParams: Promise<{ from?: string; to?: string; preset?: string; sort?: string }>;
};

// ---------------------------------------------------------------------------
// 数据格式化
// ---------------------------------------------------------------------------

function resolveDateRange(sp: { from?: string; to?: string; preset?: string }): DateRange | undefined {
  if (sp.preset === "latest") return undefined;
  if (sp.from || sp.to) return { from: sp.from, to: sp.to };

  const pad = (value: number) => String(value).padStart(2, "0");
  const today = new Date();
  const to = `${today.getFullYear()}-${pad(today.getMonth() + 1)}-${pad(today.getDate())}`;
  const fromDate = new Date(today);
  fromDate.setDate(fromDate.getDate() - 14);
  const from = `${fromDate.getFullYear()}-${pad(fromDate.getMonth() + 1)}-${pad(fromDate.getDate())}`;
  return { from, to };
}

function getDomain(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

function getScoreColor(score?: number): string {
  if (score === undefined) return "var(--muted)";
  if (score >= 7) return "var(--cool)";
  if (score >= 4) return "var(--warm)";
  return "var(--muted)";
}

function cleanArticleDescription(description?: string): string | undefined {
  if (!description) return undefined;
  return description
    .replace(/^arXiv:\S+\s+Announce Type:\s*\S+\s+Abstract:\s*/i, "")
    .trim();
}

function looksIncompleteSummary(summary?: string): boolean {
  if (!summary) return true;
  const trimmed = summary.trim();
  return /[，,、:]$/.test(trimmed);
}

function getDetailObjectiveSummary(article: EnrichedArticle): string | undefined {
  const extractedSummary = article.enriched?.objective_summary?.trim();
  if (extractedSummary && !looksIncompleteSummary(extractedSummary)) {
    return extractedSummary;
  }

  return (
    cleanArticleDescription(article.enriched?.description) ||
    article.summary?.trim() ||
    extractedSummary
  );
}

function getSentimentMeaning(sentiment?: string): string {
  switch (sentiment) {
    case "positive":
      return "整体偏利好，可优先看它带来的机会、受益方和后续扩散可能。";
    case "negative":
      return "整体偏负面或约束较多，建议先看风险矩阵和可能受损的对象。";
    case "mixed":
      return "有价值信号，也有明显限制；不要简单当成利好或利空，需要结合正文证据判断。";
    case "neutral":
      return "更像事实更新或研究记录，情绪不强；按影响力和复合价值决定阅读深度。";
    default:
      return "当前信息不足，暂时不能稳定判断这篇文章的市场或社区情绪。";
  }
}

function getHypeMeaning(level?: string): string {
  switch (level) {
    case "low":
      return "噪声较低，信息更接近事实或研究贡献；重点看证据是否扎实。";
    case "medium":
      return "有一定叙事包装，阅读时需要同时看亮点和限制。";
    case "high":
      return "宣传或概念成分较高，先验证证据，再决定是否投入时间。";
    default:
      return "暂无足够信息判断热度是否来自真实进展。";
  }
}

function getActionMeaning(action?: string): string {
  switch (action) {
    case "strategic_invest":
      return "值得进入重点池，后续可沉淀为主题、竞品或投资观察。";
    case "monitor":
      return "先保持观察，等后续产品、论文或市场反馈再升级判断。";
    case "deep_dive":
      return "需要细读正文与风险机会区，适合做专题研判或内部讨论。";
    case "speculative_watch":
      return "前瞻性强但不确定，适合放入观察清单，不急于行动。";
    case "ignore":
      return "当前信号较弱，除非与已有主题相关，否则不需要投入太多时间。";
    default:
      return "暂无明确后续动作，建议先按影响力和风险信息判断是否继续读。";
  }
}

function getConfidenceMeaning(value?: string): string {
  switch (value) {
    case "high":
      return "依据较充分";
    case "medium":
      return "可参考";
    case "low":
      return "需谨慎";
    default:
      return "未评估";
  }
}

// ---------------------------------------------------------------------------
// 页面局部组件
// ---------------------------------------------------------------------------

function ScoreMetricCard({
  label,
  score,
  reason,
  description,
  tone,
}: {
  label: string;
  score?: number;
  reason?: string;
  description: string;
  tone: "accent" | "warm";
}) {
  const color = getScoreColor(score);
  const percentage = score === undefined ? 0 : Math.min(Math.max(score * 10, 4), 100);
  const toneStyle = tone === "accent"
    ? {
        background:
          "linear-gradient(135deg, color-mix(in oklch, var(--accent) 14%, var(--panel)) 0%, var(--panel) 56%, color-mix(in oklch, var(--cool) 7%, var(--panel)) 100%)",
        borderColor: "color-mix(in oklch, var(--accent) 34%, var(--line))",
      }
    : {
        background:
          "linear-gradient(135deg, color-mix(in oklch, var(--warm) 18%, var(--panel)) 0%, var(--panel) 58%, color-mix(in oklch, var(--accent) 6%, var(--panel)) 100%)",
        borderColor: "color-mix(in oklch, var(--warm) 38%, var(--line))",
      };

  return (
    <div className="relative min-w-0 overflow-hidden rounded-xl border p-4 shadow-sm md:p-5" style={toneStyle}>
      <div className="absolute inset-x-0 top-0 h-1" style={{ backgroundColor: color }} />
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div className="min-w-0">
          <p className="text-[12px] font-bold text-foreground/78">{label}</p>
          <p className="mt-1 text-[13px] leading-6 text-foreground/62">{description}</p>
        </div>
        <p className="shrink-0 text-[34px] font-bold leading-none tabular-nums" style={{ color }}>
          {score === undefined ? "N/A" : score.toFixed(1)}
        </p>
      </div>
      <div className="mt-4 h-2 overflow-hidden rounded-full bg-line/70">
        <div className="h-full rounded-full" style={{ width: `${percentage}%`, backgroundColor: color }} />
      </div>
      {reason && <p className="mt-4 rounded-lg bg-white/55 px-3 py-2 text-[14px] leading-7 text-foreground/74 shadow-[inset_0_0_0_1px_color-mix(in_oklch,var(--line)_70%,transparent)]">{reason}</p>}
    </div>
  );
}

function JudgementMetricCard({
  label,
  value,
  description,
  detail,
  color = "var(--muted)",
}: {
  label: string;
  value: string;
  description: string;
  detail?: string;
  color?: string;
}) {
  return (
    <div
      className="relative min-w-0 overflow-hidden rounded-xl border p-4 shadow-sm"
      style={{
        background:
          "linear-gradient(135deg, color-mix(in oklch, var(--metric-color) 11%, var(--panel)) 0%, var(--panel) 64%)",
        borderColor: "color-mix(in oklch, var(--metric-color) 30%, var(--line))",
        "--metric-color": color,
      } as React.CSSProperties}
    >
      <div className="absolute inset-x-0 top-0 h-1" style={{ backgroundColor: color }} />
      <p className="text-[12px] font-bold text-foreground/76">{label}</p>
      <p className="mt-2 text-[24px] font-bold leading-tight break-words" style={{ color }}>
        {value}
      </p>
      <p className="mt-2 text-[13px] leading-6 text-foreground/64">{description}</p>
      {detail && <p className="mt-3 rounded-lg bg-white/58 px-3 py-2 text-[13px] leading-6 text-foreground/72 shadow-[inset_0_0_0_1px_color-mix(in_oklch,var(--line)_70%,transparent)]">{detail}</p>}
    </div>
  );
}

function ConfidenceMetricCard({
  confidence,
}: {
  confidence?: { impact?: string; compound?: string; hype?: string };
}) {
  const rows = [
    ["影响判断", confidence?.impact],
    ["价值判断", confidence?.compound],
    ["热度判断", confidence?.hype],
  ].filter(([, value]) => value);

  return (
    <div className="relative min-w-0 overflow-hidden rounded-xl border border-cool/25 bg-gradient-to-br from-cool/10 via-panel to-panel p-4 shadow-sm">
      <div className="absolute inset-x-0 top-0 h-1 bg-cool" />
      <p className="text-[12px] font-bold text-foreground/76">置信度</p>
      <p className="mt-2 text-[13px] leading-6 text-foreground/64">
        分别对应影响力、复合价值与 Hype 判断的可信程度。
      </p>
      {rows.length > 0 ? (
        <div className="mt-3 grid gap-2">
          {rows.map(([label, value]) => (
            <div key={label} className="flex items-center justify-between gap-3 rounded-lg bg-white/58 px-3 py-2 shadow-[inset_0_0_0_1px_color-mix(in_oklch,var(--line)_70%,transparent)]">
              <span className="text-[12px] font-semibold text-foreground/62">{label}</span>
              <span className="text-right text-[12px] font-bold text-foreground/78">
                {value}
                <span className="ml-1 font-normal text-muted/65">· {getConfidenceMeaning(value)}</span>
              </span>
            </div>
          ))}
        </div>
      ) : (
        <p className="mt-3 rounded-lg bg-white/58 px-3 py-2 font-mono text-[13px] font-bold text-muted/55">N/A</p>
      )}
    </div>
  );
}

function MetricsStrip({ article }: { article: EnrichedArticle }) {
  const enriched = article.enriched;
  if (!enriched) {
    return (
      <div className="rounded-2xl border border-line/60 bg-panel/80 p-5 text-[14px] leading-7 text-muted/75 shadow-sm">
        当前文章只有 scout 基础信息，尚无提取或分析指标。
      </div>
    );
  }

  const sentiment = enriched.sentiment ? SENTIMENT_LABELS[enriched.sentiment] : undefined;
  const hype = enriched.hype_assessment?.level ? HYPE_LEVEL_LABELS[enriched.hype_assessment.level] : undefined;
  const action = enriched.actionable_insight ? ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight] : undefined;

  return (
    <section
      aria-label="核心判断"
      className="rounded-2xl border border-accent/18 p-4 shadow-sm backdrop-blur-sm md:p-5"
      style={{
        background:
          "linear-gradient(135deg, color-mix(in oklch, var(--accent) 8%, var(--panel)) 0%, var(--panel) 42%, color-mix(in oklch, var(--warm) 6%, var(--panel)) 100%)",
      }}
    >
      <div className="flex flex-wrap items-end justify-between gap-3 border-b border-line/55 pb-4">
        <div>
          <p className="text-[12px] font-bold uppercase tracking-wide text-accent">核心指标</p>
          <h2 className="mt-1 text-[19px] font-bold text-foreground">先判断这篇文章值不值得继续读</h2>
        </div>
        <p className="max-w-xl text-[13px] leading-6 text-muted/72">
          评分用于衡量信号强度，判断类指标用于解释方向、热度、后续动作与可信程度。
        </p>
      </div>

      <div className="mt-4 grid gap-4 lg:grid-cols-2">
        <ScoreMetricCard
          label="影响力"
          score={enriched.impact_score?.score}
          reason={enriched.impact_score?.reason}
          description="衡量事件对技术、产业或生态的外部影响强度。"
          tone="accent"
        />
        <ScoreMetricCard
          label="复合价值"
          score={enriched.compound_value?.score}
          reason={enriched.compound_value?.reason}
          description="综合新颖性、可执行性与长期观察价值。"
          tone="warm"
        />
      </div>

      <div className="mt-4 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <JudgementMetricCard
          label="情绪"
          value={sentiment?.label ?? "N/A"}
          description={getSentimentMeaning(enriched.sentiment)}
          color={sentiment?.color}
        />
        <JudgementMetricCard
          label="Hype"
          value={hype?.label ?? "N/A"}
          description={getHypeMeaning(enriched.hype_assessment?.level)}
          detail={enriched.hype_assessment?.reason}
          color={hype?.color}
        />
        <JudgementMetricCard
          label="行动建议"
          value={action?.label ?? "N/A"}
          description={getActionMeaning(enriched.actionable_insight)}
          color={action?.color}
        />
        <ConfidenceMetricCard confidence={enriched.confidence} />
      </div>
    </section>
  );
}

function SectionHeader({
  number,
  title,
  description,
}: {
  number: string;
  title: string;
  description: string;
}) {
  return (
    <div className="flex items-start gap-3">
      <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-accent/10 font-mono text-[12px] font-bold tabular-nums text-accent">
        {number}
      </span>
      <div>
        <h2 className="text-[21px] font-bold leading-tight text-foreground">{title}</h2>
        <p className="mt-1 text-[14px] leading-6 text-muted/78">{description}</p>
      </div>
    </div>
  );
}

function DetailSection({
  id,
  number,
  title,
  description,
  children,
}: {
  id: string;
  number: string;
  title: string;
  description: string;
  children: React.ReactNode;
}) {
  return (
    <section id={id} className="rounded-2xl border border-line/60 bg-panel/88 p-5 shadow-sm backdrop-blur-sm md:p-6">
      <SectionHeader number={number} title={title} description={description} />
      <div className="mt-6">{children}</div>
    </section>
  );
}

function GuideBlock({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-xl border border-line/55 bg-background/55 p-4">
      <h2 className="text-[12px] font-bold uppercase tracking-wide text-muted/65">{title}</h2>
      <div className="mt-3">{children}</div>
    </section>
  );
}

function NeighborLink({
  label,
  href,
  article,
}: {
  label: string;
  href: string | null;
  article: EnrichedArticle | null;
}) {
  if (!href || !article) return <p className="text-[13px] text-muted/60">{label}不可用</p>;

  return (
    <Link
      href={href}
      className="group block rounded-lg border border-line/55 bg-panel/70 p-3 transition-colors hover:border-accent/30 hover:bg-accent/5 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent"
    >
      <span className="text-[12px] font-semibold text-accent">{label}</span>
      <span className="mt-1 block text-[14px] leading-6 text-foreground/80 transition-colors group-hover:text-accent">
        {article.title || "无标题"}
      </span>
    </Link>
  );
}

function ReadingGuide({
  article,
  previousHref,
  nextHref,
  previousArticle,
  nextArticle,
}: {
  article: EnrichedArticle;
  previousHref: string | null;
  nextHref: string | null;
  previousArticle: EnrichedArticle | null;
  nextArticle: EnrichedArticle | null;
}) {
  const enriched = article.enriched;
  const hasEntities = Boolean(enriched?.entities && Object.values(enriched.entities).some((items) => items.length > 0));
  const hasImpact = Boolean(enriched?.key_beneficiaries?.length || enriched?.competitive_casualty?.length);

  return (
    <aside className="space-y-4 lg:sticky lg:top-24 lg:self-start" aria-label="文章阅读导览">
      <div className="rounded-2xl border border-accent/20 bg-gradient-to-br from-accent/8 via-panel to-panel p-5 shadow-sm backdrop-blur-sm">
        <div className="flex items-center justify-between gap-3">
          <div>
            <p className="text-[12px] font-bold uppercase tracking-wide text-accent">阅读导览</p>
            <p className="mt-1 text-[12px] leading-5 text-muted/65">点击跳转到正文区块</p>
          </div>
          <span className="rounded-full bg-accent/10 px-2.5 py-1 font-mono text-[11px] font-bold text-accent">NAV</span>
        </div>
        <nav className="mt-4 grid gap-2 text-[14px] leading-6" aria-label="文章内导航">
          <a href="#facts" className="group flex items-center justify-between gap-3 rounded-xl border border-accent/15 bg-white/55 px-3 py-3 font-semibold text-foreground/72 transition-colors hover:border-accent/35 hover:bg-accent/8 hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent">
            <span className="flex items-center gap-3"><span className="font-mono text-[12px] text-accent">01</span>提取事实</span>
            <span className="text-accent opacity-60 transition-transform group-hover:translate-x-0.5">↘</span>
          </a>
          <a href="#impact" className="group flex items-center justify-between gap-3 rounded-xl border border-accent/15 bg-white/55 px-3 py-3 font-semibold text-foreground/72 transition-colors hover:border-accent/35 hover:bg-accent/8 hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent">
            <span className="flex items-center gap-3"><span className="font-mono text-[12px] text-accent">02</span>影响与价值</span>
            <span className="text-accent opacity-60 transition-transform group-hover:translate-x-0.5">↘</span>
          </a>
          <a href="#decision" className="group flex items-center justify-between gap-3 rounded-xl border border-accent/15 bg-white/55 px-3 py-3 font-semibold text-foreground/72 transition-colors hover:border-accent/35 hover:bg-accent/8 hover:text-accent focus:outline-none focus-visible:ring-2 focus-visible:ring-accent">
            <span className="flex items-center gap-3"><span className="font-mono text-[12px] text-accent">03</span>风险、机会与行动</span>
            <span className="text-accent opacity-60 transition-transform group-hover:translate-x-0.5">↘</span>
          </a>
        </nav>
      </div>

      {(enriched?.event_type || enriched?.source_type || enriched?.epistemic_status) && (
        <GuideBlock title="文章属性">
          <div className="flex flex-wrap gap-2">
            {enriched.event_type && EVENT_TYPE_LABELS[enriched.event_type] && (
              <span className="rounded-full bg-accent/8 px-3 py-1 text-[13px] font-semibold text-foreground/80">
                {EVENT_TYPE_LABELS[enriched.event_type].label}
              </span>
            )}
            {enriched.source_type && SOURCE_TYPE_LABELS[enriched.source_type] && (
              <span className="rounded-full bg-warm/10 px-3 py-1 text-[13px] font-semibold text-foreground/80">
                {SOURCE_TYPE_LABELS[enriched.source_type]}
              </span>
            )}
            {enriched.epistemic_status && EPISTEMIC_STATUS_LABELS[enriched.epistemic_status] && (
              <span className="rounded-full bg-cool/10 px-3 py-1 text-[13px] font-semibold text-foreground/80">
                {EPISTEMIC_STATUS_LABELS[enriched.epistemic_status]}
              </span>
            )}
          </div>
        </GuideBlock>
      )}

      {hasEntities && (
        <GuideBlock title="关键实体">
          <EntityChips
            companies={enriched!.entities!.companies ?? []}
            technologies={enriched!.entities!.technologies ?? []}
            key_people={enriched!.entities!.key_people ?? []}
          />
        </GuideBlock>
      )}

      {hasImpact && (
        <GuideBlock title="影响对象">
          <div className="space-y-5">
            {enriched!.key_beneficiaries.length > 0 && (
              <div>
                <h3 className="text-[13px] font-semibold text-positive">受益方</h3>
                <ul className="mt-2 space-y-2 text-[14px] leading-6 text-foreground/75">
                  {enriched!.key_beneficiaries.map((item) => (
                    <li key={item} className="rounded-lg bg-positive/5 px-3 py-2">{item}</li>
                  ))}
                </ul>
              </div>
            )}
            {enriched!.competitive_casualty.length > 0 && (
              <div>
                <h3 className="text-[13px] font-semibold text-negative">受损方</h3>
                <ul className="mt-2 space-y-2 text-[14px] leading-6 text-foreground/75">
                  {enriched!.competitive_casualty.map((item) => (
                    <li key={item} className="rounded-lg bg-negative/5 px-3 py-2">{item}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </GuideBlock>
      )}

      <GuideBlock title="同源文章">
        <div className="space-y-3">
          <NeighborLink label="上一篇" href={previousHref} article={previousArticle} />
          <NeighborLink label="下一篇" href={nextHref} article={nextArticle} />
        </div>
      </GuideBlock>
    </aside>
  );
}

// ---------------------------------------------------------------------------
// Next.js 页面入口
// ---------------------------------------------------------------------------

/**
 * 为详情页构造浏览器标题。
 */
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { name, articleId } = await params;
  return { title: `${articleId} - ${name} 文章详情` };
}

/**
 * 渲染数据源内单篇文章的完整情报详情。
 *
 * 保留列表页传入的日期与排序上下文，使返回和相邻文章导航维持原有浏览路径。
 */
export default async function SourceArticleDetailPage({ params, searchParams }: PageProps) {
  const { name, articleId } = await params;
  const sp = await searchParams;
  const dateRange = resolveDateRange(sp);
  const sort = sp.sort === "impact" ? "impact" : null;
  const detail = await getSourceArticleDetail(name, articleId, dateRange, sort);
  if (!detail) notFound();

  const { source, article, previousArticle, nextArticle, listHref, originalHref } = detail;
  const enriched = article.enriched;
  const neighborParams = new URLSearchParams();
  if (sp.from) neighborParams.set("from", sp.from);
  if (sp.to) neighborParams.set("to", sp.to);
  if (sp.preset) neighborParams.set("preset", sp.preset);
  if (sort === "impact") neighborParams.set("sort", "impact");
  const previousHref = previousArticle ? buildArticleDetailHref(source.name, previousArticle, neighborParams) : null;
  const nextHref = nextArticle ? buildArticleDetailHref(source.name, nextArticle, neighborParams) : null;
  const summary = enriched?.tldr || enriched?.objective_summary || article.summary;
  const objectiveSummary = getDetailObjectiveSummary(article);

  return (
    <PageShell>
      <header
        className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-foreground via-foreground to-accent-dark p-6 shadow-lg md:p-9"
        style={{
          backgroundImage: source.tier === "B"
            ? "linear-gradient(135deg, var(--foreground), oklch(0.18 0.02 260), oklch(0.38 0.12 85))"
            : source.tier === "C"
              ? "linear-gradient(135deg, var(--foreground), oklch(0.18 0.02 260), oklch(0.33 0.12 340))"
              : undefined,
        }}
      >
        <svg
          className="pointer-events-none absolute inset-0 h-full w-full"
          aria-hidden="true"
          viewBox="0 0 1200 420"
          preserveAspectRatio="none"
        >
          <circle cx="1050" cy="50" r="160" fill="oklch(0.55 0.13 200 / 0.10)" />
          <circle cx="1080" cy="30" r="90" fill="oklch(0.55 0.13 200 / 0.08)" />
          <circle cx="80" cy="360" r="120" fill="oklch(0.45 0.16 340 / 0.08)" />
          {Array.from({ length: 5 }).flatMap((_, row) =>
            Array.from({ length: 5 }).map((_, col) => (
              <circle
                key={`${row}-${col}`}
                cx={30 + col * 22}
                cy={20 + row * 22}
                r="1"
                fill="oklch(1 0 0 / 0.15)"
              />
            )),
          )}
        </svg>

        <div className="relative">
          <Link href={listHref} className="inline-flex items-center gap-1.5 text-[12px] font-medium text-white/55 transition-colors hover:text-accent-light focus:outline-none focus-visible:ring-2 focus-visible:ring-accent-light">
            <span aria-hidden="true">←</span> 返回 {source.display_name}
          </Link>

          <div className="mt-5 flex flex-wrap items-center gap-2.5 text-[13px] text-white/65">
            <StatusBadge status={article.status} />
            <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1 font-mono backdrop-blur">{getDomain(article.url)}</span>
            {article.published && <time className="rounded-full border border-white/10 bg-white/5 px-3 py-1 backdrop-blur">{article.published}</time>}
          </div>

          <div className="mt-5 grid gap-6 lg:grid-cols-[minmax(0,1fr)_220px] lg:items-end">
            <div className="min-w-0">
              <p className="text-[11px] font-semibold uppercase tracking-widest text-accent-light/80">Article Intelligence</p>
              <h1 className="mt-3 max-w-5xl text-3xl font-bold leading-[1.22] tracking-tight text-white md:text-5xl">
                {article.title || "无标题"}
              </h1>
            </div>
            <a
              href={originalHref}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex shrink-0 items-center justify-center gap-2 rounded-xl border border-white/12 bg-white/8 px-4 py-3 text-[14px] font-bold text-white/85 shadow-sm backdrop-blur transition-colors hover:border-accent-light/40 hover:bg-white/12 hover:text-accent-light focus:outline-none focus-visible:ring-2 focus-visible:ring-accent-light"
            >
              打开原文 <span aria-hidden="true">↗</span>
            </a>
          </div>

          {summary && (
            <div className="mt-6 rounded-xl border border-white/10 bg-white/[0.045] p-4 backdrop-blur md:p-5">
              <p className="text-[12px] font-semibold uppercase tracking-wider text-accent-light/70">先看结论</p>
              <p className="mt-2 text-[15px] font-medium leading-8 text-white/78 md:text-[16px]">
                {summary}
              </p>
            </div>
          )}
        </div>
      </header>

      <div className="mt-7">
        <MetricsStrip article={article} />
      </div>

      <div className="mt-8 grid gap-6 lg:grid-cols-[minmax(0,1fr)_320px] lg:gap-7">
        <main className="min-w-0 space-y-6">
          <DetailSection id="facts" number="01" title="提取事实" description="结构化事实、实体识别与逻辑链">
            {enriched ? (
              <ArticleCardExtraction
                tldr={enriched.tldr}
                objectiveSummary={objectiveSummary}
                eventType={enriched.event_type}
                sourceType={enriched.source_type}
                entities={enriched.entities}
                keyLogicFlow={enriched.key_logic_flow}
                epistemicStatus={enriched.epistemic_status}
              />
            ) : (
              <p className="text-[15px] leading-7 text-muted/75">这篇文章尚未完成 extraction，当前只展示 manifest 中的基础信息。</p>
            )}
          </DetailSection>

          <DetailSection id="impact" number="02" title="影响与价值" description="技术/商业影响、关注焦点与受影响对象">
            {enriched ? (
              <ArticleImpactAnalysis
                domainDisruption={enriched.domain_disruption}
                developerSentiment={enriched.developer_sentiment}
                keyBeneficiaries={enriched.key_beneficiaries}
                competitiveCasualty={enriched.competitive_casualty}
              />
            ) : (
              <p className="text-[15px] leading-7 text-muted/75">这篇文章尚未完成 analyze，暂无影响与价值判断。</p>
            )}
          </DetailSection>

          <DetailSection id="decision" number="03" title="风险、机会与行动" description="结合机会清单和风险矩阵判断后续关注重点">
            {enriched ? (
              <ArticleDecisionAnalysis
                marketOpportunities={enriched.market_opportunities}
                riskMatrix={enriched.risk_matrix}
              />
            ) : (
              <p className="text-[15px] leading-7 text-muted/75">这篇文章尚未完成 analyze，暂无风险与行动判断。</p>
            )}
          </DetailSection>
        </main>

        <ReadingGuide
          article={article}
          previousArticle={previousArticle}
          nextArticle={nextArticle}
          previousHref={previousHref}
          nextHref={nextHref}
        />
      </div>
    </PageShell>
  );
}
