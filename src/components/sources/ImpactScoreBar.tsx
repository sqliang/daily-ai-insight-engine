type ImpactScoreBarProps = {
  score: number;
  label?: string;
  reason?: string;
  compact?: boolean;
};

function getImpactColor(score: number): string {
  if (score >= 7) return "var(--cool)";
  if (score >= 4) return "var(--warm)";
  return "var(--muted)";
}

export function ImpactScoreBar({
  score,
  label = "影响力",
  reason,
  compact = false,
}: ImpactScoreBarProps) {
  const pct = Math.min(Math.max(score * 10, 4), 100);
  const color = getImpactColor(score);
  const barH = compact ? "h-2" : "h-3";
  const labelSize = compact ? "text-[12px]" : "text-[13px]";
  const scoreSize = compact ? "text-[15px]" : "text-[16px]";

  return (
    <div className="flex items-center gap-3" title={reason}>
      <span
        className={`${labelSize} font-semibold text-muted/55 w-14 shrink-0 tracking-wide`}
      >
        {label}
      </span>
      <div
        className={`${barH} flex-1 rounded-full overflow-hidden`}
        style={{
          backgroundColor: "var(--line)",
        }}
      >
        <div
          className="h-full rounded-full transition-all"
          style={{
            width: `${pct}%`,
            backgroundImage: `linear-gradient(90deg, ${color}, ${color} / 0.65)`,
          }}
        />
      </div>
      <span
        className={`${scoreSize} font-bold tabular-nums shrink-0 font-mono`}
        style={{ color }}
      >
        {score.toFixed(1)}
      </span>
    </div>
  );
}
