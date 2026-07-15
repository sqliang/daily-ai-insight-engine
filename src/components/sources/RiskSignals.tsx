// ============================================================================
// RiskSignals.tsx — 四维风险信号矩阵
//
// 展示监管、技术、竞争、伦理四维风险评估结果，并完整列出附加风险项。
// 被文章详情页的风险与行动区块消费。
// ============================================================================

type RiskSignalsProps = {
  riskMatrix?: {
    regulatory?: string;
    technological?: string;
    competitive?: string;
    ethical?: string;
    additional?: string[];
  };
};

const RISK_DIMENSIONS: Array<{
  key: "regulatory" | "technological" | "competitive" | "ethical";
  label: string;
}> = [
  { key: "regulatory", label: "监管" },
  { key: "technological", label: "技术" },
  { key: "competitive", label: "竞争" },
  { key: "ethical", label: "伦理" },
];

/**
 * 风险信号矩阵组件，展示四维风险评估结果及附加风险项。
 *
 * 用于文章详情页的分析区块。四维度：监管、技术、竞争、伦理；
 * 有风险项以语义色标识，所有判断维持可读对比度。
 */
export function RiskSignals({ riskMatrix }: RiskSignalsProps) {
  if (!riskMatrix) return null;

  const hasAny =
    riskMatrix.regulatory ||
    riskMatrix.technological ||
    riskMatrix.competitive ||
    riskMatrix.ethical ||
    (riskMatrix.additional && riskMatrix.additional.length > 0);

  if (!hasAny) return null;

  return (
    <div className="rounded-xl border border-line/55 bg-background/55 p-4">
      <span className="text-[13px] font-semibold text-muted/80">
        风险信号
      </span>
      <div className="mt-3 grid gap-2.5 sm:grid-cols-2">
        {RISK_DIMENSIONS.map(({ key, label }) => {
          const text = riskMatrix[key];
          const hasRisk = text && text !== "无";
          return (
            <div
              key={key}
              className="rounded-lg border border-line/50 bg-panel/70 p-3"
            >
              <div className="flex items-center gap-2">
                <span
                  className="inline-block h-2.5 w-2.5 shrink-0 rounded-full"
                  style={{
                    backgroundColor: hasRisk ? "var(--negative)" : "var(--line)",
                  }}
                />
                <span className="text-[13px] font-semibold text-muted/80">
                  {label}
                </span>
              </div>
              <span
                className="mt-2 block text-[14px] leading-6"
                style={{
                  color: hasRisk
                    ? "var(--foreground)"
                    : "var(--muted)",
                }}
              >
                {text || "—"}
              </span>
            </div>
          );
        })}
      </div>
      {riskMatrix.additional &&
        riskMatrix.additional.length > 0 && (
          <div className="mt-3 space-y-2">
            {riskMatrix.additional.map((r, i) => (
              <p key={`add-${i}`} className="rounded-lg bg-negative/5 px-3 py-2 text-[14px] leading-6 text-foreground/75">
                {r}
              </p>
            ))}
          </div>
        )}
    </div>
  );
}
