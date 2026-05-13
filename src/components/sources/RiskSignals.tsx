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
      <span className="text-[12px] font-semibold text-muted/35 uppercase tracking-wider">
        风险信号
      </span>
      <div className="mt-2 space-y-2">
        {RISK_DIMENSIONS.map(({ key, label }) => {
          const text = riskMatrix[key];
          const hasRisk = text && text !== "无";
          return (
            <div
              key={key}
              className="flex items-start gap-2.5 pl-2"
              style={{
                borderLeft: hasRisk
                  ? "2px solid var(--negative) / 0.3"
                  : "2px solid transparent",
              }}
            >
              <span
                className="inline-block h-2 w-2 rounded-full mt-1 shrink-0"
                style={{
                  backgroundColor: hasRisk ? "var(--negative)" : "var(--line)",
                }}
              />
              <span className="text-[12px] font-medium text-muted/40 w-8 shrink-0">
                {label}
              </span>
              <span
                className="text-[13px] leading-relaxed"
                style={{
                  color: hasRisk
                    ? "var(--foreground) / 0.7"
                    : "var(--muted) / 0.3",
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
              className="flex items-start gap-2 pl-[18px]"
            >
              <span className="text-[13px] leading-relaxed text-foreground/55">
                · {r}
              </span>
            </div>
          ))}
      </div>
    </div>
  );
}
