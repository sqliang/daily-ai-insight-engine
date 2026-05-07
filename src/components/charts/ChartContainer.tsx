"use client";

import { ReactNode } from "react";
import { ResponsiveContainer } from "recharts";

type ChartContainerProps = {
  children: ReactNode;
  minHeight?: number;
};

export function ChartContainer({ children, minHeight = 260 }: ChartContainerProps) {
  return (
    <div style={{ width: "100%", minHeight }}>
      <ResponsiveContainer width="100%" height={minHeight}>
        {children as any}
      </ResponsiveContainer>
    </div>
  );
}
