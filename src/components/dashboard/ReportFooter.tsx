type ReportFooterProps = {
  selectionRationale: string;
};

export function ReportFooter({ selectionRationale }: ReportFooterProps) {
  return (
    <footer className="mt-8 border-t-2 border-accent-light pt-5 text-sm leading-7 text-muted">
      <span className="text-[11px] font-semibold uppercase tracking-wider text-accent">
        信源说明
      </span>
      <p className="mt-1">{selectionRationale}</p>
    </footer>
  );
}
