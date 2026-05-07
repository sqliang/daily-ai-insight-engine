"use client";

import { PieChart, Pie, Cell, Tooltip } from "recharts";
import { ChartContainer } from "./ChartContainer";

export type DonutDatum = {
  name: string;
  value: number;
  color: string;
};

type DonutChartProps = {
  data: DonutDatum[];
  centerLabel: string;
  height?: number;
};

export function DonutChart({ data, centerLabel, height = 260 }: DonutChartProps) {
  return (
    <ChartContainer minHeight={height}>
      <PieChart>
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          innerRadius={58}
          outerRadius={88}
          paddingAngle={3}
          dataKey="value"
          stroke="none"
        >
          {data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={entry.color} />
          ))}
        </Pie>
        <Tooltip
          contentStyle={{
            background: "oklch(1 0 0)",
            border: "1px solid oklch(0.88 0.012 260)",
            borderRadius: "8px",
            fontSize: "13px",
            boxShadow: "0 4px 12px oklch(0.18 0.02 260 / 0.08)",
          }}
        />
        <text
          x="50%"
          y="50%"
          textAnchor="middle"
          dominantBaseline="middle"
          className="fill-foreground"
          style={{ fontSize: "15px", fontWeight: 600 }}
        >
          {centerLabel}
        </text>
      </PieChart>
    </ChartContainer>
  );
}
