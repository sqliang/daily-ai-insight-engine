import { type ProcessingStatus, STATUS_CONFIG } from "@/lib/data/status";

type StatusBadgeProps = {
  status: ProcessingStatus;
};

export function StatusBadge({ status }: StatusBadgeProps) {
  const cfg = STATUS_CONFIG[status];
  return (
    <span
      className="inline-flex items-center gap-1.5 rounded-full border px-3.5 py-1.5 text-[12px] font-semibold backdrop-blur"
      style={{
        borderColor: `${cfg.color} / 0.2`,
        backgroundColor: `${cfg.color} / 0.06`,
        color: cfg.color,
      }}
      title={cfg.description}
    >
      {cfg.english}
      <span className="font-normal opacity-50">·</span>
      <span className="font-medium">{cfg.label}</span>
    </span>
  );
}
