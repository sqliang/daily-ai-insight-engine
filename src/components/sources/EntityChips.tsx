// ============================================================================
// EntityChips.tsx — 实体识别结果展示
//
// 以分组彩色 chip 列出公司（accent）、技术（cool）、关键人物（warm）三类实体。
// 被 ArticleCardExtraction 的实体识别区块消费，空分组自动隐藏。
// ============================================================================

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
    <div className="flex items-start gap-2.5">
      <span
        className="text-[13px] font-semibold shrink-0 mt-0.5 tracking-wide"
        style={{ color: `${color} / 0.6` }}
      >
        {label}
      </span>
      <div className="flex flex-wrap gap-2">
        {items.map((item, i) => (
          <span
            key={i}
            className="inline-block rounded-full px-3 py-1 text-[12px] font-medium"
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

/**
 * 实体识别结果展示组件，以分组色块形式列出公司、技术和关键人物。
 *
 * 用于 ArticleCardExtraction 的实体识别区块，三类实体分别以
 * accent / cool / warm 色系区分，空分组自动隐藏。
 */
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
    <div className="space-y-2.5">
      <ChipGroup label="公司" items={companies} color="var(--accent)" />
      <ChipGroup label="技术" items={technologies} color="var(--cool)" />
      <ChipGroup label="人物" items={key_people} color="var(--warm)" />
    </div>
  );
}
