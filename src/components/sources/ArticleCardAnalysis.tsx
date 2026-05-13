import {
  HYPE_LEVEL_LABELS,
  ACTIONABLE_INSIGHT_LABELS,
} from "@/lib/data/status";
import { ImpactScoreBar } from "./ImpactScoreBar";
import { SentimentIndicator } from "./SentimentIndicator";
import { RiskSignals } from "./RiskSignals";

type ArticleCardAnalysisProps = {
  impactScore?: { score: number; reason: string };
  compoundValue?: { score: number; reason: string };
  sentiment?: string;
  hypeAssessment?: { level: string; reason: string };
  domainDisruption?: { technical_innovation: string; business_model: string };
  developerSentiment?: { tone: string; primary_focus: string };
  riskMatrix?: {
    regulatory?: string;
    technological?: string;
    competitive?: string;
    ethical?: string;
    additional?: string[];
  };
  confidence?: { impact?: string; compound?: string; hype?: string };
  actionableInsight?: string;
  keyBeneficiaries?: string[];
  competitiveCasualty?: string[];
  marketOpportunities?: string[];
};

function ConfidenceBar({
  label,
  level,
}: {
  label: string;
  level?: string;
}) {
  if (!level) return null;
  const pct = level === "high" ? 100 : level === "medium" ? 50 : 20;
  const color =
    level === "high"
      ? "var(--positive)"
      : level === "medium"
        ? "var(--warm)"
        : "var(--muted)";
  return (
    <div className="flex items-center gap-2">
      <span className="text-[11px] font-medium text-muted/40 w-10 shrink-0">
        {label}
      </span>
      <div
        className="h-1.5 flex-1 rounded-full overflow-hidden"
        style={{ backgroundColor: "var(--line)" }}
      >
        <div
          className="h-full rounded-full"
          style={{ width: `${pct}%`, backgroundColor: color }}
        />
      </div>
      <span className="text-[11px] font-mono font-medium tabular-nums shrink-0" style={{ color }}>
        {level}
      </span>
    </div>
  );
}

export function ArticleCardAnalysis({
  impactScore,
  compoundValue,
  sentiment,
  hypeAssessment,
  domainDisruption,
  developerSentiment,
  riskMatrix,
  confidence,
  actionableInsight,
  keyBeneficiaries,
  competitiveCasualty,
  marketOpportunities,
}: ArticleCardAnalysisProps) {
  const hasAnalysis = impactScore || compoundValue || sentiment;
  if (!hasAnalysis) return null;

  return (
    <div
      className="border-t pt-5 mt-3 space-y-5"
      style={{ borderColor: "var(--line) / 0.4" }}
    >
      {/* ================================================================
          Qualitative Assessment
          ================================================================ */}
      <div
        className="rounded-xl p-4"
        style={{ backgroundColor: "var(--surface)" }}
      >
        <div className="flex items-center gap-2 mb-3">
          <div
            className="w-1 h-4 rounded-full"
            style={{ backgroundColor: "var(--accent)" }}
          />
          <span className="text-[12px] font-bold text-muted/50 uppercase tracking-wider">
            定性评估
          </span>
        </div>

        <div className="space-y-3">
          {impactScore && (
            <div>
              <ImpactScoreBar
                score={impactScore.score}
                label="影响力"
                reason={impactScore.reason}
              />
              {impactScore.reason && (
                <p className="mt-1.5 ml-[56px] text-[12px] leading-relaxed text-foreground/40 line-clamp-2">
                  {impactScore.reason}
                </p>
              )}
            </div>
          )}

          <div className="flex flex-wrap items-center gap-2.5">
            {sentiment && <SentimentIndicator sentiment={sentiment} />}
            {hypeAssessment && hypeAssessment.level in HYPE_LEVEL_LABELS && (
              <span
                className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] font-semibold"
                style={{
                  backgroundColor: `${HYPE_LEVEL_LABELS[hypeAssessment.level].color} / 0.08`,
                  color: HYPE_LEVEL_LABELS[hypeAssessment.level].color,
                }}
                title={hypeAssessment.reason}
              >
                <span className="text-[14px] leading-none">
                  {hypeAssessment.level === "low"
                    ? "◉"
                    : hypeAssessment.level === "medium"
                      ? "◐"
                      : "●"}
                </span>
                {HYPE_LEVEL_LABELS[hypeAssessment.level].label}
              </span>
            )}
          </div>

          {developerSentiment && (
            <p
              className="text-[13px] leading-relaxed text-foreground/55 pl-3"
              style={{ borderLeft: "2px solid var(--warm) / 0.2" }}
            >
              <span className="font-semibold text-muted/40">
                开发者情绪
              </span>
              <span className="mx-2 text-muted/15">|</span>
              {developerSentiment.primary_focus}
            </p>
          )}
        </div>
      </div>

      {/* ================================================================
          Value Network
          ================================================================ */}
      {(compoundValue || domainDisruption) && (
        <div
          className="rounded-xl p-4"
          style={{ backgroundColor: "var(--surface)" }}
        >
          <div className="flex items-center gap-2 mb-3">
            <div
              className="w-1 h-4 rounded-full"
              style={{ backgroundColor: "var(--warm)" }}
            />
            <span className="text-[12px] font-bold text-muted/50 uppercase tracking-wider">
              价值网络
            </span>
          </div>

          <div className="space-y-3">
            {compoundValue && (
              <div>
                <ImpactScoreBar
                  score={compoundValue.score}
                  label="复合价值"
                  reason={compoundValue.reason}
                />
                {compoundValue.reason && (
                  <p className="mt-1.5 ml-[56px] text-[12px] leading-relaxed text-foreground/40 line-clamp-2">
                    {compoundValue.reason}
                  </p>
                )}
              </div>
            )}

            {domainDisruption && (
              <div className="space-y-2">
                <div className="flex items-start gap-2.5">
                  <span
                    className="inline-flex items-center rounded-md px-2 py-0.5 text-[11px] font-semibold shrink-0 mt-0.5"
                    style={{
                      backgroundColor: "var(--accent) / 0.08",
                      color: "var(--accent)",
                    }}
                  >
                    技术颠覆
                  </span>
                  <p className="text-[13px] leading-[1.75] text-foreground/60">
                    {domainDisruption.technical_innovation}
                  </p>
                </div>
                <div className="flex items-start gap-2.5">
                  <span
                    className="inline-flex items-center rounded-md px-2 py-0.5 text-[11px] font-semibold shrink-0 mt-0.5"
                    style={{
                      backgroundColor: "var(--warm) / 0.08",
                      color: "var(--warm)",
                    }}
                  >
                    商业模式
                  </span>
                  <p className="text-[13px] leading-[1.75] text-foreground/60">
                    {domainDisruption.business_model}
                  </p>
                </div>
              </div>
            )}

            {(keyBeneficiaries && keyBeneficiaries.length > 0) ||
            (competitiveCasualty && competitiveCasualty.length > 0) ? (
              <div className="flex flex-wrap gap-x-5 gap-y-1.5 pt-1">
                {keyBeneficiaries && keyBeneficiaries.length > 0 && (
                  <div className="flex items-start gap-1.5">
                    <span className="text-[12px] font-semibold text-positive/60 shrink-0 mt-0.5">
                      ▲ 受益
                    </span>
                    <span className="text-[13px] text-foreground/55 line-clamp-1 leading-relaxed">
                      {keyBeneficiaries.slice(0, 3).join(" · ")}
                      {keyBeneficiaries.length > 3 &&
                        ` +${keyBeneficiaries.length - 3}`}
                    </span>
                  </div>
                )}
                {competitiveCasualty && competitiveCasualty.length > 0 && (
                  <div className="flex items-start gap-1.5">
                    <span className="text-[12px] font-semibold text-negative/60 shrink-0 mt-0.5">
                      ▼ 受损
                    </span>
                    <span className="text-[13px] text-foreground/55 line-clamp-1 leading-relaxed">
                      {competitiveCasualty.slice(0, 3).join(" · ")}
                      {competitiveCasualty.length > 3 &&
                        ` +${competitiveCasualty.length - 3}`}
                    </span>
                  </div>
                )}
              </div>
            ) : null}
          </div>
        </div>
      )}

      {/* ================================================================
          Foresight
          ================================================================ */}
      {(actionableInsight || riskMatrix || marketOpportunities) && (
        <div
          className="rounded-xl p-4"
          style={{ backgroundColor: "var(--surface)" }}
        >
          <div className="flex items-center gap-2 mb-3">
            <div
              className="w-1 h-4 rounded-full"
              style={{ backgroundColor: "var(--cool)" }}
            />
            <span className="text-[12px] font-bold text-muted/50 uppercase tracking-wider">
              前瞻研判
            </span>
          </div>

          <div className="space-y-3">
            {/* Actionable insight — prominent verdict */}
            {actionableInsight &&
              actionableInsight in ACTIONABLE_INSIGHT_LABELS && (
                <div className="flex items-center gap-3">
                  <span
                    className="inline-flex items-center gap-2 rounded-full px-3.5 py-1.5 text-[13px] font-bold"
                    style={{
                      backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[actionableInsight].color} / 0.1`,
                      color: ACTIONABLE_INSIGHT_LABELS[actionableInsight].color,
                    }}
                  >
                    <span className="text-[16px] leading-none">◆</span>
                    {ACTIONABLE_INSIGHT_LABELS[actionableInsight].label}
                  </span>
                  {confidence && (
                    <span className="text-[11px] text-muted/30 font-mono leading-snug">
                      {(confidence.impact && `影响 ${confidence.impact}`) ?? ""}
                      {(confidence.compound && ` · 价值 ${confidence.compound}`) ?? ""}
                      {(confidence.hype && ` · hype ${confidence.hype}`) ?? ""}
                    </span>
                  )}
                </div>
              )}

            {/* Confidence bars */}
            {confidence && (
              <div className="space-y-1.5 ml-1">
                <ConfidenceBar label="影响" level={confidence.impact} />
                <ConfidenceBar label="价值" level={confidence.compound} />
                <ConfidenceBar label="Hype" level={confidence.hype} />
              </div>
            )}

            {/* Market opportunities */}
            {marketOpportunities && marketOpportunities.length > 0 && (
              <div>
                {marketOpportunities.map((opp, i) => (
                  <p
                    key={i}
                    className="text-[13px] leading-[1.8] text-foreground/55 pl-3.5"
                    style={{ textIndent: "-0.5rem" }}
                  >
                    <span className="text-muted/25 mr-1">→</span> {opp}
                  </p>
                ))}
              </div>
            )}

            <RiskSignals riskMatrix={riskMatrix} />
          </div>
        </div>
      )}
    </div>
  );
}
