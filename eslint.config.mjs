import js from "@eslint/js";
import tseslint from "typescript-eslint";
import reactHooks from "eslint-plugin-react-hooks";

// ============================================================================
// eslint.config.mjs — ESLint flat config
//
// 规则说明：
//   - 继承 @eslint/js recommended 和 typescript-eslint recommended
//   - 忽略 .next / node_modules / out 等构建产物目录
//   - 未使用变量检查：允许以下划线开头的参数（如 _req），
//     常见的 TypeScript 模式用于标记占位参数
// ============================================================================

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    ignores: [".next/**", "node_modules/**", "out/**", ".claude/**", ".venv/**", ".understand-anything/**"],
  },
  {
    files: ["**/*.{ts,tsx}"],
    plugins: { "react-hooks": reactHooks },
    rules: {
      "@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn",
    },
  },
];
