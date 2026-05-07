// ============================================================================
// postcss.config.mjs — PostCSS 构建配置
//
// 只启用 @tailwindcss/postcss 插件（Tailwind CSS v4 的新 PostCSS 插件）。
// Tailwind v4 使用原生 CSS @import "tailwindcss" 语法，
// 不再需要 tailwindcss/nesting 等额外插件。
// ============================================================================

const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

export default config;
