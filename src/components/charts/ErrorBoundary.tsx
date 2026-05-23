"use client";

import { Component, type ReactNode } from "react";

type Props = {
  fallback?: ReactNode;
  children: ReactNode;
  sectionName?: string;
};

type State = { hasError: boolean; error: Error | null };

export class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error(
      `Chart error boundary${this.props.sectionName ? ` [${this.props.sectionName}]` : ""}:`,
      error,
      info.componentStack,
    );
  }

  render() {
    if (this.state.hasError) {
      return (
        this.props.fallback ?? (
          <div className="flex flex-col items-center justify-center rounded-xl border border-line bg-panel p-6 text-center">
            <p className="text-sm font-medium text-muted">
              {this.props.sectionName
                ? `「${this.props.sectionName}」渲染失败`
                : "图表渲染失败"}
            </p>
            <p className="mt-1 font-mono text-xs text-muted/70">
              {this.state.error?.message ?? "未知错误"}
            </p>
            <button
              onClick={() => this.setState({ hasError: false, error: null })}
              className="mt-3 rounded-md bg-accent px-3 py-1.5 text-xs font-medium text-white transition hover:opacity-90"
            >
              重试
            </button>
          </div>
        )
      );
    }

    return this.props.children;
  }
}
