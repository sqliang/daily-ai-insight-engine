import { SENTIMENT_LABELS } from "@/lib/data/status";

type SentimentIndicatorProps = {
  sentiment?: string;
};

/**
 * 情绪倾向指示器，以色块图标 + 标签展示分析结果的情绪分类。
 *
 * 用于 ArticleCard 内的分析子卡片，与 RiskSignals、LogicFlow 并列展示。
 * 无法识别时返回 null 不渲染。
 */
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
