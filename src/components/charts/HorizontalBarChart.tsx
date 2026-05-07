"use client";

import { BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from "recharts";
import { ChartContainer } from "./ChartContainer";

export type BarDatum = {
  label: string;
  value: number;
  color?: string;
};

type HorizontalBarChartProps = {
  data: BarDatum[];
  tone?: "accent" | "warm" | "cool";
  height?: number;
};

const gradients = {
  accent: ["oklch(0.55 0.13 200)", "oklch(0.62 0.10 190)"],
  warm: ["oklch(0.60 0.16 85)", "oklch(0.67 0.14 78)"],
  cool: ["oklch(0.45 0.16 340)", "oklch(0.52 0.14 330)"],
};

export function HorizontalBarChart({ data, tone = "accent", height }: HorizontalBarChartProps) {
  const [startColor, endColor] = gradients[tone];
  const hasPerItemColors = data.some((d) => d.color);
  const chartData = data.map((d) => ({ ...d, name: d.label }));
  const barCount = data.length;
  const computedHeight = height ?? Math.max(260, barCount * 40);

  return (
    <ChartContainer minHeight={computedHeight}>
      <BarChart
        data={chartData}
        layout="vertical"
        margin={{ top: 0, right: 20, left: 10, bottom: 0 }}
      >
        <defs>
          <linearGradient id={`bar-grad-${tone}`} x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stopColor={startColor} />
            <stop offset="100%" stopColor={endColor} />
          </linearGradient>
        </defs>
        <XAxis type="number" hide />
        <YAxis
          type="category"
          dataKey="name"
          tick={{ fontSize: 12, fill: "oklch(0.48 0.02 255)" }}
          tickLine={false}
          axisLine={false}
          width={130}
          interval={0}
        />
        <Tooltip
          contentStyle={{
            background: "oklch(1 0 0)",
            border: "1px solid oklch(0.88 0.012 260)",
            borderRadius: "8px",
            fontSize: "13px",
            boxShadow: "0 4px 12px oklch(0.18 0.02 260 / 0.08)",
          }}
          formatter={(value) => [String(value ?? ""), ""]}
        />
        <Bar
          dataKey="value"
          radius={[0, 6, 6, 0]}
          barSize={18}
          fill={`url(#bar-grad-${tone})`}
        >
          {hasPerItemColors
            ? data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color ?? `url(#bar-grad-${tone})`} />
              ))
            : undefined}
        </Bar>
      </BarChart>
    </ChartContainer>
  );
}
