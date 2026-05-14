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
    <div>
      <span className="text-[13px] font-semibold text-muted/40 uppercase tracking-wider">
        风险信号
      </span>
      <div className="mt-3 space-y-2.5">
        {RISK_DIMENSIONS.map(({ key, label }) => {
          const text = riskMatrix[key];
          const hasRisk = text && text !== "无";
          return (
            <div
              key={key}
              className="flex items-start gap-3 pl-3 py-1.5 rounded-lg"
              style={{
                borderLeft: hasRisk
                  ? "3px solid var(--negative) / 0.4"
                  : "3px solid transparent",
                backgroundColor: hasRisk ? "var(--negative) / 0.02" : "transparent",
              }}
            >
              <span
                className="inline-block h-2.5 w-2.5 rounded-full mt-1 shrink-0"
                style={{
                  backgroundColor: hasRisk ? "var(--negative)" : "var(--line)",
                }}
              />
              <span className="text-[13px] font-medium text-muted/50 w-10 shrink-0">
                {label}
              </span>
              <span
                className="text-[14px] leading-relaxed"
                style={{
                  color: hasRisk
                    ? "var(--foreground) / 0.7"
                    : "var(--muted) / 0.35",
                }}
              >
                {text || "—"}
              </span>
            </div>
          );
        })}
        {riskMatrix.additional &&
          riskMatrix.additional.length > 0 &&
          riskMatrix.additional.map((r, i) => (
            <div
              key={`add-${i}`}
              className="flex items-start gap-2 pl-[22px]"
            >
              <span className="text-[14px] leading-relaxed text-foreground/55">
                · {r}
              </span>
            </div>
          ))}
      </div>
    </div>
  );
}
