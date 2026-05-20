---
name: tailwind-css-patterns
description: Tailwind CSS v4 best practices for styling React components. Use this skill whenever writing component styles, building layouts, or applying visual design — prefer Tailwind utility classes over CSS Modules, inline styles, or custom CSS. Only fall back to CSS Modules when Tailwind genuinely cannot achieve the result (complex animations, intricate pseudo-selectors, browser-specific hacks).
---

# Tailwind CSS Best Practices

Use Tailwind CSS v4.1+ utility classes as the **primary** styling method. CSS Modules are a **last resort** — only when Tailwind cannot achieve the result.

## Tailwind First, CSS Modules Last

The decision tree for every styling task:

1. **Tailwind utility class** — always the first choice
2. **Arbitrary value** (`[color]`, `[length]`, `[custom-prop]`) — when the design token doesn't exist in the default scale
3. **`@utility` or `@theme`** — when the same arbitrary value repeats across components
4. **CSS Module** — only when the above options fail (complex keyframe animations, `:has()` parent selection, vendor-prefixed pseudo-elements)

Don't reach for CSS Modules out of habit. Most things people historically did with custom CSS are one-liners in Tailwind.

## Core Conventions

### Mobile-first always

Start with mobile styles, layer on breakpoints upward:

```html
<!-- DO: build up from mobile -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">...</div>

<!-- DON'T: desktop-first with max-width overrides -->
<div class="grid grid-cols-4 max-md:grid-cols-1">...</div>
```

### Use gap, not margin for spacing children

`gap` works in flexbox and grid, avoids margin-collapse surprises, and doesn't leave unwanted spacing on the last child.

```html
<!-- DO -->
<div class="flex gap-4">...</div>

<!-- DON'T -->
<div class="flex [&>*]:mr-4">...</div>
```

### Prefer semantic spacing scale

Stick to Tailwind's spacing scale (4, 8, 12, 16, 24, 32...) rather than arbitrary pixel values. It enforces visual consistency.

```html
<!-- DO -->
<div class="p-6 rounded-xl gap-4">...</div>

<!-- DON'T: random arbitrary values -->
<div class="p-[18px] rounded-[7px] gap-[13px]">...</div>
```

### Use `@theme` for design tokens, not JS config

v4.1 CSS-first configuration is the default. Only use `tailwind.config.js` when integrating with a legacy project.

```css
@import "tailwindcss";

@theme {
  --color-brand: #3b82f6;
  --color-brand-light: #60a5fa;
  --font-display: "Inter", system-ui, sans-serif;
}
```

### Avoid `@apply` for component styles

`@apply` couples styles to CSS files, defeats the utility-first workflow, and produces worse dead-code elimination. If you find yourself reaching for `@apply`, extract a React component instead.

```tsx
// DO: extract a component
function Card({ children }: { children: React.ReactNode }) {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      {children}
    </div>
  );
}

// DON'T: @apply in CSS
// .card { @apply bg-white rounded-xl shadow-lg p-6; }
```

### Avoid premature utility extraction

Don't pull every repeated class string into a variable or component. Two identical `<button>` class strings are fine — extraction should happen when the *meaning* is shared (a button variant, a card), not just the classes.

## What Tailwind Can't Do

These genuinely require CSS Modules:

- **Complex `@keyframes` animations** with multiple intermediate stops
- **`:has()` parent-affecting selectors** (limited browser support anyway)
- **Vendor-prefixed pseudo-elements** (`::-webkit-scrollbar`, `::cue`)
- **CSS Grid with subgrid** or complex named template areas spanning many rows
- **`@container` queries beyond what Tailwind's built-in `@container` supports**

When you do use a CSS Module, add a comment explaining why Tailwind couldn't work:

```css
/* .scrollbar.module.css — Tailwind can't target ::-webkit-scrollbar pseudo-element */
.scrollbar::-webkit-scrollbar-thumb {
  background: #94a3b8;
  border-radius: 9999px;
}
```

## Common Patterns

### Centering

```html
<!-- Horizontal center: mx-auto on block/flex items -->
<div class="mx-auto max-w-lg">...</div>

<!-- Full centering (login pages, modals) -->
<div class="flex items-center justify-center min-h-screen">...</div>

<!-- Vertical centering in a row -->
<div class="flex items-center gap-2">
  <Avatar />
  <span>Name</span>
</div>
```

### Cards

```html
<div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow">
  <div class="p-6">
    <h3 class="text-lg font-semibold text-gray-900">Title</h3>
    <p class="mt-2 text-sm text-gray-600">Description</p>
  </div>
</div>
```

### Responsive grid that fits content

```html
<!-- Auto-fit: columns size to content, no media queries needed -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-6">
  <!-- cards -->
</div>
```

### Sticky frosted nav

```html
<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
  <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-16">
    ...
  </div>
</nav>
```

### Line-clamp text

```html
<p class="line-clamp-3 text-sm text-gray-600">
  Long text that gets truncated after 3 lines...
</p>
```

### Skeleton loading

```html
<div class="animate-pulse space-y-3">
  <div class="h-4 bg-gray-200 rounded w-3/4" />
  <div class="h-4 bg-gray-200 rounded" />
  <div class="h-4 bg-gray-200 rounded w-1/2" />
</div>
```

### Accessible focus rings

```html
<!-- Replace default outline with visible ring, respect focus-visible -->
<button class="focus:outline-none focus-visible:ring-2 focus-visible:ring-brand focus-visible:ring-offset-2">
  Action
</button>
```

### Transition defaults

```html
<!-- Standard hover transition -->
<button class="transition-colors duration-200 hover:bg-brand-light">
  Hover me
</button>

<!-- For transforms, use transform-gpu for hardware acceleration -->
<div class="transition-transform duration-300 transform-gpu hover:scale-105">...</div>
```

## Interaction Patterns

### Group hover

```html
<div class="group cursor-pointer">
  <h3 class="group-hover:text-brand transition-colors">Title</h3>
  <p class="text-gray-500 group-hover:text-gray-700 transition-colors">Desc</p>
</div>
```

### Peer-based form states

```html
<label>
  <input type="checkbox" class="peer sr-only" />
  <span class="peer-checked:bg-brand peer-checked:text-white ...">Toggle</span>
</label>
```

### Disabled / loading states

```html
<button
  disabled
  class="bg-brand text-white px-4 py-2 rounded-lg
         hover:bg-brand-dark
         disabled:opacity-50 disabled:cursor-not-allowed"
>
  Submit
</button>
```

## Dark Mode

Use `dark:` prefix with `class` strategy:

```html
<div class="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">
  <h2 class="text-gray-900 dark:text-white">Title</h2>
  <p class="text-gray-600 dark:text-gray-400">Body</p>
</div>
```

## Motion Respect

Always wrap animations with `motion-reduce:` or `motion-safe:`:

```html
<div class="transition-transform motion-reduce:transition-none hover:scale-105">...</div>
<div class="motion-safe:animate-fade-in">...</div>
```

## Performance

- Use `transform-gpu` instead of `transform` for hardware-accelerated transforms
- Use `content-visibility-auto` on below-the-fold heavy sections
- Use `aspect-ratio` on images/videos to prevent layout shift (CLS)
- Don't use `@apply` — it bloats CSS and defeats purging

## Accessibility Checklist

Every interactive element should have:
- Visible focus indicator (`focus-visible:ring-2`)
- `aria-label` on icon-only buttons
- Sufficient color contrast (Tailwind defaults are fine for gray-900 on white)
- `motion-reduce` support for animations
- Touch target at least `min-h-10 min-w-10` (44px) on mobile

## Quick Reference: What to use instead of...

| Instead of | Use Tailwind |
|---|---|
| `display: flex; align-items: center; justify-content: space-between` | `flex items-center justify-between` |
| `position: fixed; top: 0; left: 0; right: 0` | `fixed inset-x-0 top-0` |
| `text-overflow: ellipsis; overflow: hidden; white-space: nowrap` | `truncate` |
| `box-shadow: ...` values by hand | `shadow-sm` / `shadow-md` / `shadow-lg` / `shadow-xl` |
| Custom `@media` queries | `sm:` / `md:` / `lg:` / `xl:` / `2xl:` |
| CSS `gap` in flexbox | `gap-{n}` (Tailwind v4 supported everywhere) |
| Custom CSS `::before`/`::after` | `before:` / `after:` pseudo-element utilities |
