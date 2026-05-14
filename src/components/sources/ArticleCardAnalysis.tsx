import {
  HYPE_LEVEL_LABELS,
  ACTIONABLE_INSIGHT_LABELS,
} from "@/lib/data/status";
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

function DimensionCard({
  label,
  icon,
  accentColor,
  children,
}: {
  label: string;
  icon: React.ReactNode;
  accentColor: string;
  children: React.ReactNode;
}) {
  return (
    <div
      className="rounded-xl p-4"
      style={{ backgroundColor: "var(--surface)" }}
    >
      <div className="flex items-center gap-2 mb-3">
        <div
          className="flex items-center justify-center w-5 h-5 rounded text-[11px]"
          style={{
            backgroundColor: `${accentColor} / 0.1`,
            color: accentColor,
          }}
        >
          {icon}
        </div>
        <span className="text-[13px] font-bold text-foreground/70">{label}</span>
      </div>
      {children}
    </div>
  );
}

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
    <div className="flex items-center gap-3">
      <span className="text-[13px] font-medium text-muted/50 w-12 shrink-0">
        {label}
      </span>
      <div
        className="h-2 flex-1 rounded-full overflow-hidden"
        style={{ backgroundColor: "var(--line)" }}
      >
        <div
          className="h-full rounded-full transition-all"
          style={{ width: `${pct}%`, backgroundColor: color }}
        />
      </div>
      <span className="text-[12px] font-mono font-semibold tabular-nums shrink-0" style={{ color }}>
        {level === "high" ? "高" : level === "medium" ? "中" : "低"}
      </span>
    </div>
  );
}

function ScoreHero({
  score,
  label,
  reason,
}: {
  score: number;
  label: string;
  reason?: string;
}) {
  const color =
    score >= 7 ? "var(--cool)" : score >= 4 ? "var(--warm)" : "var(--muted)";
  const pct = Math.min(Math.max(score * 10, 4), 100);

  return (
    <div className="flex items-start gap-4">
      <div
        className="flex flex-col items-center justify-center w-16 h-16 rounded-xl shrink-0"
        style={{
          backgroundColor: `${color} / 0.06`,
          border: `1.5px solid ${color} / 0.15`,
        }}
      >
        <span
          className="text-[22px] font-bold font-mono tabular-nums leading-none"
          style={{ color }}
        >
          {score.toFixed(1)}
        </span>
        <span className="text-[10px] font-semibold mt-1" style={{ color: `${color} / 0.6` }}>
          /10
        </span>
      </div>
      <div className="flex-1 min-w-0 pt-1">
        <div className="text-[13px] font-semibold text-foreground/60 mb-1.5">{label}</div>
        <div
          className="h-2.5 rounded-full overflow-hidden"
          style={{ backgroundColor: "var(--line)" }}
        >
          <div
            className="h-full rounded-full transition-all"
            style={{
              width: `${pct}%`,
              backgroundImage: `linear-gradient(90deg, ${color}, ${color} / 0.6)`,
            }}
          />
        </div>
        {reason && (
          <p className="mt-2 text-[13px] leading-[1.7] text-foreground/45 line-clamp-2">
            {reason}
          </p>
        )}
      </div>
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
    <div className="space-y-4">
      {impactScore && (
        <DimensionCard
          label="影响力评估"
          icon={
            <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
              <path d="M8 1l2 5h5l-4 3 1.5 5L8 11 3.5 14 5 9 1 6h5z" />
            </svg>
          }
          accentColor="var(--cool)"
        >
          <ScoreHero
            score={impactScore.score}
            label="影响力评分"
            reason={impactScore.reason}
          />
        </DimensionCard>
      )}

      <DimensionCard
        label="情绪与 Hype"
        icon={
          <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
            <path d="M8 14s-5.5-3.5-5.5-7.5A3.5 3.5 0 018 3.5 3.5 3.5 0 0113.5 6.5C13.5 10.5 8 14 8 14z" />
          </svg>
        }
        accentColor="var(--accent)"
      >
        <div className="space-y-3">
          <div className="flex flex-wrap items-center gap-3">
            {sentiment && <SentimentIndicator sentiment={sentiment} />}
            {hypeAssessment && hypeAssessment.level in HYPE_LEVEL_LABELS && (
              <span
                className="inline-flex items-center gap-2 rounded-full px-3.5 py-1.5 text-[13px] font-semibold"
                style={{
                  backgroundColor: `${HYPE_LEVEL_LABELS[hypeAssessment.level].color} / 0.08`,
                  color: HYPE_LEVEL_LABELS[hypeAssessment.level].color,
                }}
                title={hypeAssessment.reason}
              >
                <span className="text-[15px] leading-none">
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
          {hypeAssessment?.reason && (
            <p className="text-[13px] leading-[1.7] text-foreground/45">
              {hypeAssessment.reason}
            </p>
          )}
          {developerSentiment && (
            <div
              className="pl-4 py-2.5 rounded-lg"
              style={{
                borderLeft: "3px solid var(--warm) / 0.3",
                backgroundColor: "var(--warm) / 0.03",
              }}
            >
              <span className="text-[13px] font-semibold text-muted/50">
                开发者情绪
              </span>
              <span className="mx-2 text-muted/20">·</span>
              <span className="text-[14px] text-foreground/60">
                {developerSentiment.primary_focus}
              </span>
            </div>
          )}
        </div>
      </DimensionCard>

      {(compoundValue || domainDisruption) && (
        <DimensionCard
          label="价值网络"
          icon={
            <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
              <circle cx="8" cy="8" r="6" />
              <path d="M2 8h12M8 2a9 9 0 014 6 9 9 0 01-4 6 9 9 0 01-4-6 9 9 0 014-6z" />
            </svg>
          }
          accentColor="var(--warm)"
        >
          <div className="space-y-4">
            {compoundValue && (
              <ScoreHero
                score={compoundValue.score}
                label="复合价值评分"
                reason={compoundValue.reason}
              />
            )}

            {domainDisruption && (
              <div className="grid grid-cols-1 gap-3">
                <div
                  className="p-3 rounded-lg"
                  style={{
                    borderLeft: "3px solid var(--accent) / 0.4",
                    backgroundColor: "var(--accent) / 0.02",
                  }}
                >
                  <div className="text-[12px] font-bold text-accent/60 mb-1.5">技术颠覆</div>
                  <p className="text-[14px] leading-[1.75] text-foreground/65">
                    {domainDisruption.technical_innovation}
                  </p>
                </div>
                <div
                  className="p-3 rounded-lg"
                  style={{
                    borderLeft: "3px solid var(--warm) / 0.4",
                    backgroundColor: "var(--warm) / 0.02",
                  }}
                >
                  <div className="text-[12px] font-bold text-warm/60 mb-1.5">商业模式</div>
                  <p className="text-[14px] leading-[1.75] text-foreground/65">
                    {domainDisruption.business_model}
                  </p>
                </div>
              </div>
            )}

            {(keyBeneficiaries && keyBeneficiaries.length > 0) ||
            (competitiveCasualty && competitiveCasualty.length > 0) ? (
              <div className="grid grid-cols-2 gap-3">
                {keyBeneficiaries && keyBeneficiaries.length > 0 && (
                  <div
                    className="p-3 rounded-lg"
                    style={{ backgroundColor: "var(--positive) / 0.03" }}
                  >
                    <div className="text-[12px] font-bold text-positive/60 mb-2 flex items-center gap-1.5">
                      <span>▲</span> 受益方
                    </div>
                    <div className="space-y-1">
                      {keyBeneficiaries.slice(0, 4).map((b, i) => (
                        <div key={i} className="text-[13px] text-foreground/60 leading-relaxed">
                          {b}
                        </div>
                      ))}
                      {keyBeneficiaries.length > 4 && (
                        <div className="text-[12px] text-muted/40">+{keyBeneficiaries.length - 4} 更多</div>
                      )}
                    </div>
                  </div>
                )}
                {competitiveCasualty && competitiveCasualty.length > 0 && (
                  <div
                    className="p-3 rounded-lg"
                    style={{ backgroundColor: "var(--negative) / 0.03" }}
                  >
                    <div className="text-[12px] font-bold text-negative/60 mb-2 flex items-center gap-1.5">
                      <span>▼</span> 受损方
                    </div>
                    <div className="space-y-1">
                      {competitiveCasualty.slice(0, 4).map((c, i) => (
                        <div key={i} className="text-[13px] text-foreground/60 leading-relaxed">
                          {c}
                        </div>
                      ))}
                      {competitiveCasualty.length > 4 && (
                        <div className="text-[12px] text-muted/40">+{competitiveCasualty.length - 4} 更多</div>
                      )}
                    </div>
                  </div>
                )}
              </div>
            ) : null}
          </div>
        </DimensionCard>
      )}

      {(actionableInsight || riskMatrix || marketOpportunities) && (
        <DimensionCard
          label="前瞻研判"
          icon={
            <svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
              <path d="M2 8l4 4L14 4" />
            </svg>
          }
          accentColor="var(--cool)"
        >
          <div className="space-y-4">
            {actionableInsight &&
              actionableInsight in ACTIONABLE_INSIGHT_LABELS && (
                <div
                  className="flex items-center gap-3 p-3 rounded-lg"
                  style={{
                    backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[actionableInsight].color} / 0.04`,
                  }}
                >
                  <span
                    className="inline-flex items-center gap-2 rounded-full px-4 py-2 text-[14px] font-bold"
                    style={{
                      backgroundColor: `${ACTIONABLE_INSIGHT_LABELS[actionableInsight].color} / 0.1`,
                      color: ACTIONABLE_INSIGHT_LABELS[actionableInsight].color,
                    }}
                  >
                    <span className="text-[17px] leading-none">◆</span>
                    {ACTIONABLE_INSIGHT_LABELS[actionableInsight].label}
                  </span>
                  {confidence && (
                    <span className="text-[12px] text-muted/35 font-mono leading-snug">
                      {(confidence.impact && `影响 ${confidence.impact}`) ?? ""}
                      {(confidence.compound && ` · 价值 ${confidence.compound}`) ?? ""}
                      {(confidence.hype && ` · hype ${confidence.hype}`) ?? ""}
                    </span>
                  )}
                </div>
              )}

            {confidence && (
              <div className="space-y-2 ml-1">
                <ConfidenceBar label="影响" level={confidence.impact} />
                <ConfidenceBar label="价值" level={confidence.compound} />
                <ConfidenceBar label="Hype" level={confidence.hype} />
              </div>
            )}

            {marketOpportunities && marketOpportunities.length > 0 && (
              <div>
                <div className="text-[12px] font-bold text-muted/40 uppercase tracking-widest mb-2">
                  市场机会
                </div>
                <div className="space-y-2">
                  {marketOpportunities.map((opp, i) => (
                    <div
                      key={i}
                      className="flex items-start gap-2.5 p-2.5 rounded-lg"
                      style={{ backgroundColor: "var(--accent) / 0.02" }}
                    >
                      <span className="text-accent/50 mt-0.5 shrink-0">→</span>
                      <span className="text-[14px] leading-[1.75] text-foreground/60">
                        {opp}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <RiskSignals riskMatrix={riskMatrix} />
          </div>
        </DimensionCard>
      )}
    </div>
  );
}
