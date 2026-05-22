"use client";

import { useState } from "react";
import type { EnrichedArticle } from "@/lib/data/sources";
import { StatusBadge } from "./StatusBadge";
import { ArticleCardBasic } from "./ArticleCardBasic";
import { ArticleCardExtraction } from "./ArticleCardExtraction";
import { ArticleCardAnalysis } from "./ArticleCardAnalysis";
import { ImpactScoreBar } from "./ImpactScoreBar";
import { SentimentIndicator } from "./SentimentIndicator";
import { ACTIONABLE_INSIGHT_LABELS } from "@/lib/data/status";

type ArticleCardProps = {
  article: EnrichedArticle;
};

function getImpactBorderColor(
  enriched: EnrichedArticle["enriched"],
): string {
  const score =
    enriched?.impact_score?.score ?? enriched?.compound_value?.score;
  if (score === undefined) return "var(--line)";
  if (score >= 7) return "var(--cool)";
  if (score >= 4) return "var(--warm)";
  return "var(--muted)";
}

function CollapsedPreview({
  article,
}: {
  article: EnrichedArticle;
}) {
  const { enriched, title, url, status } = article;
  const isProcessed = status !== "scout" && enriched;
  const displayTldr = isProcessed ? enriched.tldr : undefined;
  const displaySummary = isProcessed
    ? enriched.objective_summary
    : article.summary;
  const hasMetrics =
    enriched?.impact_score || enriched?.sentiment || enriched?.actionable_insight;

  return (
    <div className="flex items-start gap-5">
      <div className="flex-1 min-w-0">
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="block"
        >
          <h3
            className="text-[17px] font-bold leading-snug text-foreground
                       group-hover:text-accent transition-colors duration-200 truncate"
          >
            {title || "无标题"}
          </h3>
        </a>
        {displayTldr && (
          <p className="mt-2.5 text-[15px] font-semibold leading-[1.6] text-foreground/80 line-clamp-2">
            {displayTldr}
          </p>
        )}
        {displaySummary && (
          <p className={`text-[14px] leading-[1.7] text-foreground/55 line-clamp-2 ${displayTldr ? "mt-1.5" : "mt-2"}`}>
            {displaySummary}
          </p>
        )}
      </div>

      {hasMetrics && enriched && (
        <div className="flex items-center gap-3 shrink-0 pt-0.5">
          {enriched.impact_score && (
            <span
              className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-[14px] font-bold font-mono tabular-nums"
              style={{
                backgroundColor: `${getImpactBorderColor(enriched)} / 0.08`,
                color: getImpactBorderColor(enriched),
              }}
            >
              {enriched.impact_score.score.toFixed(1)}
            </span>
          )}
          {enriched.sentiment && enriched.sentiment in
            ({ positive: 1, negative: 1, neutral: 1, mixed: 1 } as Record<string, unknown>) && (
            <SentimentIndicator sentiment={enriched.sentiment} />
          )}
          {enriched.actionable_insight &&
            enriched.actionable_insight in ACTIONABLE_INSIGHT_LABELS && (
              <span
                className="inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-[13px] font-bold"
                style={{
                  backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight].color} / 0.1`,
                  color: ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight].color,
                }}
              >
                ◆ {ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight].label}
              </span>
            )}
        </div>
      )}
    </div>
  );
}

function HeroStrip({
  enriched,
}: {
  enriched: NonNullable<EnrichedArticle["enriched"]>;
}) {
  const hasImpact = enriched.impact_score !== undefined;
  const hasSentiment =
    enriched.sentiment !== undefined && enriched.sentiment !== "";
  const hasInsight =
    enriched.actionable_insight !== undefined &&
    enriched.actionable_insight !== "" &&
    enriched.actionable_insight in ACTIONABLE_INSIGHT_LABELS;

  if (!hasImpact && !hasSentiment && !hasInsight) return null;

  return (
    <div
      className="flex flex-wrap items-center gap-x-5 gap-y-3 mb-6 px-4 py-3 rounded-lg"
      style={{ backgroundColor: "var(--surface)" }}
    >
      {hasImpact && (
        <ImpactScoreBar
          score={enriched.impact_score!.score}
          label="影响力"
          compact
        />
      )}
      {hasSentiment && <SentimentIndicator sentiment={enriched.sentiment} />}
      {hasInsight && (
        <span
          className="inline-flex items-center gap-1.5 rounded-full px-3.5 py-1.5 text-[13px] font-bold"
          style={{
            backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight!].color} / 0.1`,
            color: ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight!].color,
          }}
        >
          ◆ {ACTIONABLE_INSIGHT_LABELS[enriched.actionable_insight!].label}
        </span>
      )}
    </div>
  );
}

function StepCircle({
  stage,
  color,
}: {
  stage: number;
  color: string;
}) {
  return (
    <div
      className="flex items-center justify-center w-9 h-9 rounded-full text-[15px] font-bold shrink-0"
      style={{
        backgroundColor: `${color} / 0.1`,
        color,
        boxShadow: `0 0 0 3px ${color} / 0.06, inset 0 0 0 1px ${color} / 0.12`,
      }}
    >
      {stage}
    </div>
  );
}

function StageBanner({
  stage,
  title,
  subtitle,
  accentColor,
}: {
  stage: number;
  title: string;
  subtitle: string;
  accentColor: string;
}) {
  return (
    <div
      className="flex items-center gap-4 px-4 py-3 rounded-xl"
      style={{ backgroundColor: `${accentColor} / 0.04` }}
    >
      <StepCircle stage={stage} color={accentColor} />
      <div className="min-w-0">
        <div className="text-[16px] font-bold text-foreground/90 leading-tight">{title}</div>
        <div className="text-[12px] text-muted/50 mt-0.5">{subtitle}</div>
      </div>
    </div>
  );
}

export function ArticleCard({ article }: ArticleCardProps) {
  const { enriched, status } = article;
  const [collapsed, setCollapsed] = useState(true);
  const hasAnalysis = status === "analyzed" && enriched;
  const hasExtraction = status !== "scout" && enriched;
  const hasRichContent = hasExtraction || hasAnalysis;

  return (
    <article
      className="group rounded-2xl border border-line/60 bg-panel/80 backdrop-blur-sm
                 transition-all duration-300 ease-out overflow-hidden
                 hover:shadow-lg hover:-translate-y-0.5 hover:border-accent/20"
      style={{
        borderLeft: `4px solid ${getImpactBorderColor(enriched)}`,
        boxShadow: "var(--shadow-sm)",
      }}
    >
      <div className="p-7">
        <div className="flex items-center justify-between mb-4">
          <StatusBadge status={status} />
          {hasRichContent && (
            <button
              type="button"
              onClick={() => setCollapsed((p) => !p)}
              className="inline-flex items-center gap-2 rounded-lg px-3.5 py-1.5
                         text-[13px] font-semibold
                         transition-all duration-200
                         hover:bg-surface"
              style={{ color: collapsed ? "var(--accent)" : "var(--muted)" }}
            >
              {collapsed ? (
                <>
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 16 16"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                  >
                    <polyline points="4 10 8 6 12 10" />
                  </svg>
                  展开详情
                  {enriched?.impact_score && (
                    <span className="font-mono font-bold tabular-nums text-[12px]" style={{ color: getImpactBorderColor(enriched) }}>
                      {enriched.impact_score.score.toFixed(1)}
                    </span>
                  )}
                </>
              ) : (
                <>
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 16 16"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                  >
                    <polyline points="4 6 8 10 12 6" />
                  </svg>
                  收起
                </>
              )}
            </button>
          )}
        </div>

        {collapsed ? (
          <CollapsedPreview article={article} />
        ) : (
          <>
            {enriched && <HeroStrip enriched={enriched} />}

            <ArticleCardBasic
              title={article.title}
              url={article.url}
              published={article.published}
              author={article.author}
              summary={article.summary}
              id={article.id}
            />

            {hasRichContent && (
              <div className="relative mt-8">
                <div
                  className="absolute left-[18px] top-[52px] bottom-[18px] w-[2px] rounded-full"
                  style={{
                    background: hasAnalysis
                      ? "linear-gradient(to bottom, var(--accent) / 0.25, var(--warm) / 0.25)"
                      : "var(--accent) / 0.2",
                  }}
                />

                <div className="space-y-8">
                  {hasExtraction && (
                    <div>
                      <StageBanner
                        stage={1}
                        title="信息提取"
                        subtitle="LLM 结构化提取 · 关键信息摘要与实体识别"
                        accentColor="var(--accent)"
                      />
                      <div className="mt-4 pl-2">
                        <ArticleCardExtraction
                          tldr={enriched!.tldr}
                          objectiveSummary={enriched!.objective_summary}
                          eventType={enriched!.event_type}
                          sourceType={enriched!.source_type}
                          entities={enriched!.entities}
                          keyLogicFlow={enriched!.key_logic_flow}
                          epistemicStatus={enriched!.epistemic_status}
                        />
                      </div>
                    </div>
                  )}

                  {hasAnalysis && (
                    <div>
                      <StageBanner
                        stage={2}
                        title="深度分析"
                        subtitle="多维度定性评估 · 价值网络与前瞻研判"
                        accentColor="var(--warm)"
                      />
                      <div className="mt-4 pl-2">
                        <ArticleCardAnalysis
                          impactScore={enriched!.impact_score}
                          compoundValue={enriched!.compound_value}
                          sentiment={enriched!.sentiment}
                          hypeAssessment={enriched!.hype_assessment}
                          domainDisruption={enriched!.domain_disruption}
                          developerSentiment={enriched!.developer_sentiment}
                          riskMatrix={enriched!.risk_matrix}
                          confidence={enriched!.confidence}
                          actionableInsight={enriched!.actionable_insight}
                          keyBeneficiaries={enriched!.key_beneficiaries}
                          competitiveCasualty={enriched!.competitive_casualty}
                          marketOpportunities={enriched!.market_opportunities}
                        />
                      </div>
                    </div>
                  )}
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </article>
  );
}
