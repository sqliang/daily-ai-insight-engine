"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/report", label: "Full Report" },
];

export function NavBar() {
  const pathname = usePathname();

  return (
    <nav className="sticky top-0 z-50 h-12 border-b border-line/50 bg-background/75 backdrop-blur-xl saturate-150">
      <div className="mx-auto flex h-full max-w-7xl items-center justify-between px-5 md:px-8">
        {/* Brand */}
        <Link href="/" className="group flex items-center gap-2.5">
          <svg
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            className="text-accent transition-transform duration-300 group-hover:rotate-[-8deg]"
          >
            <path d="M12 2L2 7l10 5 10-5-10-5z" strokeLinecap="round" strokeLinejoin="round" />
            <path d="M2 17l10 5 10-5" strokeLinecap="round" strokeLinejoin="round" />
            <path d="M2 12l10 5 10-5" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          <span className="text-[13px] font-semibold tracking-tight text-foreground">
            Daily AI Insight
          </span>
        </Link>

        {/* Nav links */}
        <div className="flex items-center">
          {links.map(({ href, label }) => {
            const active = pathname === href;
            return (
              <Link
                key={href}
                href={href}
                className={`relative px-3 py-1.5 text-[13px] font-medium transition-colors duration-200 ${
                  active
                    ? "text-foreground"
                    : "text-muted/70 hover:text-muted"
                }`}
              >
                {label}
                {active && (
                  <span className="absolute bottom-0 left-1/2 h-[2px] w-4/5 -translate-x-1/2 rounded-full bg-gradient-to-r from-accent to-accent-dark" />
                )}
              </Link>
            );
          })}
        </div>
      </div>
    </nav>
  );
}
