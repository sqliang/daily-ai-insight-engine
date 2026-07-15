// ============================================================================
// ArticleDetailAnalysis.tsx — 文章详情页深度分析展示
//
// 将 Stage 3 的分析结果按“影响与价值”“风险、机会与行动”拆分为卡片区块。
// 由文章详情页消费，完整展示评分依据与列表内容，并贴合站点看板视觉。
// ============================================================================

import { RiskSignals } from "./RiskSignals";

type ArticleDetailAnalysisProps = {
  domainDisruption?: { technical_innovation: string; business_model: string };
  developerSentiment?: { tone: string; primary_focus: string };
  riskMatrix?: {
    regulatory?: string;
    technological?: string;
    competitive?: string;
    ethical?: string;
    additional?: string[];
  };
  keyBeneficiaries?: string[];
  competitiveCasualty?: string[];
  marketOpportunities?: string[];
};

function AnalysisList({
  title,
  items,
  color,
}: {
  title: string;
  items?: string[];
  color: string;
}) {
  if (!items || items.length === 0) return null;

  return (
    <div className="rounded-xl border border-line/55 bg-background/55 p-4">
      <h3 className="text-[13px] font-semibold" style={{ color }}>{title}</h3>
      <ul className="mt-2.5 space-y-2">
        {items.map((item) => (
          <li key={item} className="flex gap-2.5 rounded-lg bg-panel/70 px-3 py-2 text-[15px] leading-7 text-foreground/75">
            <span className="mt-3 h-1.5 w-1.5 shrink-0 rounded-full" style={{ backgroundColor: color }} />
            <span>{item}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

/**
 * 文章详情页的“影响与价值”分析区块。
 *
 * 在核心指标之后补充技术/商业影响、开发者关注点和受益/受损对象。
 */
export function ArticleImpactAnalysis({
  domainDisruption,
  developerSentiment,
  keyBeneficiaries,
  competitiveCasualty,
}: ArticleDetailAnalysisProps) {
  const hasContent = domainDisruption || developerSentiment || keyBeneficiaries?.length || competitiveCasualty?.length;
  if (!hasContent) return null;

  return (
    <div className="space-y-5">
      {developerSentiment && (
        <div className="rounded-xl border border-line/55 bg-background/55 p-4">
          <h3 className="text-[13px] font-semibold text-warm">开发者关注点</h3>
          <p className="mt-2 text-[15px] leading-7 text-foreground/75">
            {developerSentiment.primary_focus}
          </p>
        </div>
      )}

      {domainDisruption && (
        <div className="grid gap-4 md:grid-cols-2">
          <div className="rounded-xl border border-accent/20 bg-accent/6 p-4">
            <h3 className="text-[13px] font-semibold text-accent">技术颠覆</h3>
            <p className="mt-2 text-[15px] leading-7 text-foreground/75">{domainDisruption.technical_innovation}</p>
          </div>
          <div className="rounded-xl border border-warm/25 bg-warm/6 p-4">
            <h3 className="text-[13px] font-semibold text-warm">商业模式</h3>
            <p className="mt-2 text-[15px] leading-7 text-foreground/75">{domainDisruption.business_model}</p>
          </div>
        </div>
      )}

      {(keyBeneficiaries?.length || competitiveCasualty?.length) && (
        <div className="grid gap-4 md:grid-cols-2">
          <AnalysisList title="关键受益方" items={keyBeneficiaries} color="var(--positive)" />
          <AnalysisList title="竞争受损方" items={competitiveCasualty} color="var(--negative)" />
        </div>
      )}
    </div>
  );
}

/**
 * 文章详情页的“风险、机会与行动”分析区块。
 *
 * 在核心行动建议之后补充机会清单与风险矩阵。
 */
export function ArticleDecisionAnalysis({
  marketOpportunities,
  riskMatrix,
}: ArticleDetailAnalysisProps) {
  const hasContent = marketOpportunities?.length || riskMatrix;
  if (!hasContent) return null;

  return (
    <div className="space-y-5">
      <AnalysisList title="可关注的市场机会" items={marketOpportunities} color="var(--accent)" />
      <RiskSignals riskMatrix={riskMatrix} />
    </div>
  );
}
