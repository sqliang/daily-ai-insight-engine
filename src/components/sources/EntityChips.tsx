type EntityChipsProps = {
  companies: string[];
  technologies: string[];
  key_people: string[];
};

function ChipGroup({
  label,
  items,
  color,
}: {
  label: string;
  items: string[];
  color: string;
}) {
  if (items.length === 0) return null;
  return (
    <div className="flex items-start gap-2">
      <span
        className="text-[12px] font-semibold shrink-0 mt-0.5 tracking-wide"
        style={{ color: `${color} / 0.55` }}
      >
        {label}
      </span>
      <div className="flex flex-wrap gap-1.5">
        {items.map((item, i) => (
          <span
            key={i}
            className="inline-block rounded-full px-2.5 py-0.5 text-[11px] font-medium"
            style={{
              backgroundColor: `${color} / 0.06`,
              color,
            }}
          >
            {item}
          </span>
        ))}
      </div>
    </div>
  );
}

export function EntityChips({
  companies,
  technologies,
  key_people,
}: EntityChipsProps) {
  if (
    companies.length === 0 &&
    technologies.length === 0 &&
    key_people.length === 0
  )
    return null;

  return (
    <div className="space-y-2">
      <ChipGroup label="公司" items={companies} color="var(--accent)" />
      <ChipGroup label="技术" items={technologies} color="var(--cool)" />
      <ChipGroup label="人物" items={key_people} color="var(--warm)" />
    </div>
  );
}
