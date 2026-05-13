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
  const barH = compact ? "h-1.5" : "h-2.5";
  const labelSize = compact ? "text-[11px]" : "text-[12px]";
  const scoreSize = compact ? "text-[13px]" : "text-[14px]";

  return (
    <div className="flex items-center gap-2.5" title={reason}>
      <span
        className={`${labelSize} font-medium text-muted/45 w-12 shrink-0 tracking-wide`}
      >
        {label}
      </span>
      <div
        className={`${barH} flex-1 rounded-full overflow-hidden`}
        style={{
          backgroundColor: "var(--line)",
          boxShadow: "inset 0 1px 2px oklch(0.18 0.02 260 / 0.06)",
        }}
      >
        <div
          className={`h-full rounded-full transition-all bg-gradient-to-r`}
          style={{
            width: `${pct}%`,
            backgroundImage: `linear-gradient(90deg, ${color}, ${color} / 0.7)`,
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
