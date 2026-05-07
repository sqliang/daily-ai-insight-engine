import type { ReactNode } from "react";

type PageShellProps = {
  children: ReactNode;
};

export function PageShell({ children }: PageShellProps) {
  return (
    <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6 md:px-8 md:py-8">
      {children}
    </main>
  );
}
