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
    <div className="flex flex-wrap items-center gap-x-5 gap-y-2.5 mb-5">
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
          className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-bold"
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

export function ArticleCard({ article }: ArticleCardProps) {
  const { enriched, status } = article;
  const [collapsed, setCollapsed] = useState(false);
  const hasAnalysis = status === "analyzed" && enriched;

  return (
    <article
      className="group rounded-xl border border-line bg-panel/80 backdrop-blur-sm p-6
                 transition-all duration-300 ease-out overflow-hidden
                 hover:shadow-lg hover:-translate-y-0.5 hover:border-accent/25"
      style={{
        borderLeft: `4px solid ${getImpactBorderColor(enriched)}`,
        borderTop: "1px solid var(--panel)",
        boxShadow:
          "0 1px 0 oklch(1 0 0 / 0.5) inset, 0 0 0 oklch(0.55 0.13 200 / 0)",
      }}
    >
      {/* Status badge — top right */}
      <div className="flex justify-end mb-3">
        <StatusBadge status={status} />
      </div>

      {/* Hero strip — at-a-glance key metrics (analyzed only) */}
      {enriched && <HeroStrip enriched={enriched} />}

      {/* Basic section — always visible */}
      <ArticleCardBasic
        title={article.title}
        url={article.url}
        published={article.published}
        author={article.author}
        summary={article.summary}
        id={article.id}
      />

      {/* Extraction section — available when extracted or analyzed */}
      {status !== "scout" && enriched && (
        <ArticleCardExtraction
          tldr={enriched.tldr}
          objectiveSummary={enriched.objective_summary}
          eventType={enriched.event_type}
          entities={enriched.entities}
          keyLogicFlow={enriched.key_logic_flow}
          epistemicStatus={enriched.epistemic_status}
        />
      )}

      {/* Analysis section — only when fully analyzed, collapsible */}
      {hasAnalysis && (
        <div
          className={`transition-all duration-300 ease-out ${
            collapsed
              ? "max-h-0 opacity-0 overflow-hidden mt-0"
              : "max-h-[4000px] opacity-100 mt-0"
          }`}
        >
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
      )}

      {/* Collapse toggle — only for analyzed cards */}
      {hasAnalysis && (
        <div className="mt-4 pt-3 border-t" style={{ borderColor: "var(--line) / 0.3" }}>
          <button
            type="button"
            onClick={() => setCollapsed((p) => !p)}
            className="inline-flex items-center gap-2 text-[12px] font-semibold text-muted/35
                       hover:text-accent transition-colors duration-200"
          >
            {collapsed ? (
              <>
                <svg
                  width="12"
                  height="12"
                  viewBox="0 0 16 16"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                >
                  <polyline points="4 10 8 6 12 10" />
                </svg>
                展开分析
                {enriched && (
                  <span className="font-normal text-muted/25">
                    {enriched.impact_score
                      ? ` · 影响力 ${enriched.impact_score.score.toFixed(1)}`
                      : ""}
                  </span>
                )}
              </>
            ) : (
              <>
                <svg
                  width="12"
                  height="12"
                  viewBox="0 0 16 16"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                >
                  <polyline points="4 6 8 10 12 6" />
                </svg>
                收起分析
              </>
            )}
          </button>
        </div>
      )}
    </article>
  );
}
