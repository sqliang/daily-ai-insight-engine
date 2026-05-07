"use client";

import { useEffect, useRef, useState } from "react";

type MetricCardProps = {
  label: string;
  value: string | number;
  helper: string;
  icon: React.ReactNode;
  accent?: string;
};

export function MetricCard({ label, value, helper, icon, accent = "accent" }: MetricCardProps) {
  const [displayValue, setDisplayValue] = useState<string>("0");
  const ref = useRef<HTMLDivElement>(null);
  const animated = useRef(false);

  useEffect(() => {
    if (animated.current) return;
    animated.current = true;

    const numValue = typeof value === "number" ? value : parseInt(String(value), 10);
    if (isNaN(numValue)) {
      setDisplayValue(String(value));
      return;
    }

    let start: number | null = null;
    const duration = 800;
    const animate = (timestamp: number) => {
      if (!start) start = timestamp;
      const progress = Math.min((timestamp - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplayValue(Math.round(eased * numValue).toString());
      if (progress < 1) requestAnimationFrame(animate);
    };
    requestAnimationFrame(animate);
  }, [value]);

  const accentColor: Record<string, string> = {
    accent: "var(--accent)",
    warm: "var(--warm)",
    cool: "var(--cool)",
  };

  return (
    <section
      ref={ref}
      className="rounded-xl border border-line bg-panel p-5 shadow-sm transition-shadow hover:shadow-md"
      style={{ borderTop: `2px solid ${accentColor[accent] ?? "var(--accent)"}` }}
    >
      <div className="flex items-center gap-2">
        <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-accent-light text-accent">
          {icon}
        </span>
        <p className="text-sm text-muted">{label}</p>
      </div>
      <p className="mt-3 text-4xl font-bold tracking-tight tabular-nums">{displayValue}</p>
      <p className="mt-1.5 text-sm leading-6 text-muted">{helper}</p>
    </section>
  );
}
