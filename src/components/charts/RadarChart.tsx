"use client";

import {
  RadarChart as RechartsRadar,
  PolarGrid,
  PolarAngleAxis,
  Radar,
  ResponsiveContainer,
} from "recharts";

export type RadarDimension = {
  dimension: string;
  value: number;
};

type RadarChartProps = {
  data: RadarDimension[];
  height?: number;
};

export function RadarChart({ data, height = 300 }: RadarChartProps) {
  const chartData = data.map((d) => ({ dimension: d.dimension, value: d.value, fullMark: 5 }));

  return (
    <div style={{ width: "100%", height }}>
      <ResponsiveContainer width="100%" height={height}>
        <RechartsRadar data={chartData} cx="50%" cy="50%" outerRadius="70%">
          <PolarGrid
            stroke="oklch(0.88 0.012 260)"
            strokeDasharray="4 4"
          />
          <PolarAngleAxis
            dataKey="dimension"
            tick={{ fontSize: 12, fill: "oklch(0.48 0.02 255)", fontWeight: 500 }}
            tickLine={false}
          />
          <Radar
            name="信号强度"
            dataKey="value"
            stroke="oklch(0.55 0.13 200)"
            fill="oklch(0.55 0.13 200)"
            fillOpacity={0.15}
            strokeWidth={2}
            dot={{
              r: 4,
              fill: "oklch(0.55 0.13 200)",
              stroke: "oklch(1 0 0)",
              strokeWidth: 2,
            }}
          />
        </RechartsRadar>
      </ResponsiveContainer>
    </div>
  );
}
