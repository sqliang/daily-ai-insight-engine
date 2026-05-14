import { SENTIMENT_LABELS } from "@/lib/data/status";

type SentimentIndicatorProps = {
  sentiment?: string;
};

export function SentimentIndicator({ sentiment }: SentimentIndicatorProps) {
  if (!sentiment || !(sentiment in SENTIMENT_LABELS)) return null;

  const cfg = SENTIMENT_LABELS[sentiment];

  return (
    <span
      className="inline-flex items-center gap-2 rounded-full px-3.5 py-1.5 text-[13px] font-semibold border"
      style={{
        backgroundColor: `${cfg.color} / 0.08`,
        borderColor: `${cfg.color} / 0.2`,
        color: cfg.color,
      }}
    >
      <span className="text-[15px] leading-none">{cfg.icon}</span>
      {cfg.label}
    </span>
  );
}
