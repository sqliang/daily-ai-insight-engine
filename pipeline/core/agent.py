"""
pipeline/core/agent.py — Claude Agent SDK 共享传输层

提供统一的 Agent 调用封装，被 extraction 和 analysis 两个 stage 共用，包括：
    - call_agent(): 核心 SDK 调用，流式收集响应文本
    - call_agent_with_retry(): 带指数退避重试的包装
    - parse_json_response(): 从 Agent 响应中提取 JSON（5 级回退策略）
    - build_agent_options(): 构造标准 ClaudeAgentOptions

设计原则：
    - 所有 Agent 调用都经过本模块，便于统一管理重试、超时、错误信息
    - Agent 不需要文件系统工具（allowed_tools=[]），只做思考+文本输出
    - bypassPermissions 模式避免交互式权限提示
    - 遵循 config.yaml 中的 retry 配置（最大重试 3 次、指数退避、初始延迟 2s）
"""

import asyncio
import json
import logging
import os
import re
import tempfile
from dataclasses import dataclass, field
from typing import Optional

from claude_agent_sdk import query, ClaudeAgentOptions
from claude_agent_sdk.types import AssistantMessage, TextBlock, ResultMessage

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 数据结构
# ---------------------------------------------------------------------------


@dataclass
class StageResult:
    """
    单个文件的提取结果。

    字段：
        input_path: 输入文件路径
        output_path: 输出文件路径
        success: 是否成功完成
        fields_extracted: 成功提取的字段名列表
        error: 失败原因（仅在 success=False 时有值）
        skipped: 是否因已有所有字段而跳过
    """

    input_path: str
    output_path: str
    success: bool
    fields_extracted: list = field(default_factory=list)
    error: str = ""
    skipped: bool = False


# ---------------------------------------------------------------------------
# 异常定义
# ---------------------------------------------------------------------------


class AgentCallError(Exception):
    """Agent 调用失败异常。retryable=True 时可重试，False 时直接向上抛出。"""

    def __init__(self, message: str, retryable: bool = True) -> None:
        super().__init__(message)
        self.message = message
        self.retryable = retryable


# ---------------------------------------------------------------------------
# 核心函数：调用 Claude Agent
# ---------------------------------------------------------------------------


async def call_agent(
    prompt: str,
    system_prompt: str = "",
    *,
    model: Optional[str] = None,
    max_turns: int = 3,
    max_tokens: Optional[int] = None,
) -> str:
    """
    调用 claude-agent-sdk query() 并收集完整文本响应。

    工作流程：
        1. 构造 ClaudeAgentOptions（system_prompt、model、permissions 等）
        2. 调用 query() 获取异步消息流
        3. 遍历消息流：
            - AssistantMessage → 收集所有 TextBlock 文本
            - ResultMessage → 检查是否有错误（is_error）
        4. 返回拼接后的完整文本

    参数：
        prompt: 用户提示词（包含文章正文和提取要求）
        system_prompt: 系统提示词（定义 Agent 角色和输出格式）
        model: 模型名称，None 时使用 CLI 默认模型
        max_turns: 最大对话轮数（默认 3，提取任务不需要多轮交互）
        max_tokens: 输出 token 上限。通过 CLAUDE_CODE_MAX_OUTPUT_TOKENS 环境变量透传给
            CLI 子进程（ClaudeAgentOptions 无 max_tokens 字段、CLI 无 --max-tokens flag）。
            None 时不设 env，使用 CLI 默认输出上限。

    返回：
        Agent 响应的完整文本

    异常：
        AgentCallError: 当 Agent 返回错误或未产生任何文本时抛出
    """
    # 使用临时文件捕获 Claude CLI 的 stderr，便于诊断 "Command failed with exit code 1"
    stderr_fd, stderr_path = tempfile.mkstemp(suffix=".log", prefix="claude_agent_stderr_")
    stderr_file = os.fdopen(stderr_fd, "w")

    options = build_agent_options(
        system_prompt=system_prompt,
        model=model,
        max_turns=max_turns,
        max_tokens=max_tokens,
        stderr=stderr_file,
    )

    collected_text: list[str] = []
    has_error = False
    error_messages: list[str] = []

    def _read_stderr() -> str:
        """读取已写入的 stderr 内容并清理临时文件。"""
        try:
            stderr_file.flush()
            with open(stderr_path, "r", encoding="utf-8") as f:
                content = f.read()
            return content
        finally:
            try:
                os.unlink(stderr_path)
            except OSError:
                pass

    try:
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        collected_text.append(block.text)

            elif isinstance(message, ResultMessage):
                if message.is_error:
                    has_error = True
                    if message.errors:
                        error_messages.extend(message.errors)

    except Exception as exc:
        stderr_content = _read_stderr()
        detail = f"\nClaude CLI stderr:\n{stderr_content}" if stderr_content else ""
        raise AgentCallError(
            message=f"Agent SDK 调用异常: {exc}{detail}",
            retryable=True,
        ) from exc
    finally:
        stderr_file.close()

    if has_error:
        stderr_content = _read_stderr()
        error_text = "; ".join(error_messages) if error_messages else "未知错误"
        detail = f"\nClaude CLI stderr:\n{stderr_content}" if stderr_content else ""
        raise AgentCallError(
            message=f"Agent 返回错误: {error_text}{detail}",
            retryable=True,
        )

    full_text = "".join(collected_text)

    if not full_text:
        raise AgentCallError(
            message="Agent 未返回任何文本内容",
            retryable=True,
        )

    return full_text


# ---------------------------------------------------------------------------
# 重试逻辑
# ---------------------------------------------------------------------------


async def call_agent_with_retry(
    prompt: str,
    system_prompt: str = "",
    *,
    model: Optional[str] = None,
    max_turns: int = 3,
    max_retries: int = 3,
    initial_delay: float = 2.0,
    max_tokens: Optional[int] = None,
) -> str:
    """
    带指数退避重试的 Agent 调用包装。

    重试策略（来自 config.yaml llm.retry）：
        - 指数退避: delay = initial_delay * (2 ** attempt)
        - 最大重试 3 次
        - 初始延迟 2 秒

    可重试的错误类型：
        - 网络错误（Agent SDK 调用异常）
        - 服务端错误（Agent 返回 is_error=True）
        - 空响应（Agent 未返回文本）

    不可重试的错误类型：
        - 认证失败（API Key 无效）
        - 参数错误（400 Bad Request）

    参数：
        prompt: 用户提示词
        system_prompt: 系统提示词
        model: 模型名称
        max_turns: 最大对话轮数
        max_retries: 最大重试次数（含首次调用）
        initial_delay: 初始延迟秒数
        max_tokens: 输出 token 上限。通过 CLAUDE_CODE_MAX_OUTPUT_TOKENS 环境变量透传给
            CLI 子进程，None 时使用 CLI 默认输出上限。

    返回：
        Agent 响应的完整文本

    异常：
        AgentCallError: 所有重试耗尽后仍失败
    """
    last_error: Optional[Exception] = None

    for attempt in range(max_retries):
        try:
            return await call_agent(
                prompt=prompt,
                system_prompt=system_prompt,
                model=model,
                max_turns=max_turns,
                max_tokens=max_tokens,
            )
        except AgentCallError as exc:
            last_error = exc

            if not exc.retryable:
                raise

            if attempt == max_retries - 1:
                break

            delay = initial_delay * (2 ** attempt)
            logger.warning(
                "Agent 调用失败 (第 %d/%d 次): %s — %0.1fs 后重试",
                attempt + 1,
                max_retries,
                exc.message,
                delay,
            )
            await asyncio.sleep(delay)

    raise AgentCallError(
        message=f"Agent 调用失败（已重试 {max_retries} 次）: {last_error}",
        retryable=False,
    )


# ---------------------------------------------------------------------------
# JSON 解析
# ---------------------------------------------------------------------------

_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*\n?(.*?)\n?```", re.DOTALL)


def _close_json(partial: str) -> str:
    """
    补全截断 JSON 中未闭合的括号、引号和花括号。

    遍历字符串，追踪是否处于字符串内部（含转义处理），
    统计未闭合的 { 和 [ 数量，按数组先、对象后的顺序补全。
    如果截断点位于字符串值内部，先补引号再补括号。

    参数：
        partial: 截断的 JSON 片段（从第一个 { 开始）

    返回：
        补全后的 JSON 字符串
    """
    in_string = False
    escape = False
    open_braces = 0
    open_brackets = 0

    for ch in partial:
        if escape:
            escape = False
            continue
        if ch == "\\":
            escape = True
            continue
        if ch == '"' and not in_string:
            in_string = True
            continue
        if ch == '"' and in_string:
            in_string = False
            continue
        if in_string:
            continue
        if ch == "{":
            open_braces += 1
        elif ch == "}":
            open_braces -= 1
        elif ch == "[":
            open_brackets += 1
        elif ch == "]":
            open_brackets -= 1

    result = partial
    if in_string:
        result += '"'
    result += "]" * max(0, open_brackets)
    result += "}" * max(0, open_braces)
    return result


def _try_recover_truncated_json(text: str) -> Optional[dict]:
    """
    尝试从截断的 JSON 文本中恢复可解析的 dict。

    策略：
        1. 在完整文本上调用 _close_json() 补全括号，尝试解析
        2. 如果失败，从末尾逐步向前截断（每次去掉 1 个字符），
           对每个截断点调用 _close_json() 再尝试 json.loads()
        3. 逐步截断可以处理截断点位于字符串值或键名中间的情况

    参数：
        text: 包含截断 JSON 的原始文本

    返回：
        解析成功的 dict，所有尝试失败时返回 None
    """
    start = text.find("{")
    if start == -1:
        return None

    truncated = text[start:]

    closed = _close_json(truncated)
    try:
        result = json.loads(closed)
        logger.info("截断 JSON 恢复成功（无需修剪）")
        return result
    except json.JSONDecodeError:
        pass

    max_trim = min(len(truncated), 500)
    for trim in range(1, max_trim + 1):
        candidate = truncated[: len(truncated) - trim]
        closed = _close_json(candidate)
        try:
            result = json.loads(closed)
            logger.info("截断 JSON 恢复成功（修剪 %d 字符后）", trim)
            return result
        except json.JSONDecodeError:
            continue

    return None


def _fix_unescaped_quotes(text: str) -> str:
    """
    修复 JSON 字符串值中未转义的双引号。

    策略：
        用状态机遍历文本，跟踪是否处于字符串内部。
        遇到可能结束字符串的 '"' 时，检查其后第一个非空白字符：
        - 若是 ',' '}' ']' ':' 或 EOF → 合法的字符串结束
        - 否则 → 字符串值中的裸引号，在前面补 '\\' 转义

    参数：
        text: 包含未转义引号的 JSON 文本

    返回：
        修复后的 JSON 文本（如果无需修复则返回原文本）
    """
    result: list[str] = []
    i = 0
    in_string = False
    n = len(text)

    while i < n:
        ch = text[i]

        if ch == "\\" and in_string:
            # 保持已有转义序列不变
            result.append(ch)
            i += 1
            if i < n:
                result.append(text[i])
            i += 1
            continue

        if ch == '"' and not in_string:
            in_string = True
            result.append(ch)
        elif ch == '"' and in_string:
            # 检查下一个非空白字符，判断是否合法字符串结束
            j = i + 1
            while j < n and text[j] in " \t\n\r":
                j += 1
            next_ch = text[j] if j < n else ","
            if next_ch in (",", "}", "]", ":"):
                in_string = False
                result.append(ch)
            else:
                # 字符串值内的未转义引号
                result.append('\\"')
        else:
            result.append(ch)

        i += 1

    return "".join(result)


def parse_json_response(text: str) -> dict:
    """
    从 Agent 响应文本中提取 JSON 对象。

    5 级回退策略（按优先级）：
        1. 直接 json.loads() — 响应就是纯 JSON 对象
        2. 正则提取 ```json ... ``` 代码块 — Agent 可能用 Markdown 包裹
        3. 正则提取第一个 { ... } 对 — 行内 JSON 片段
        4. 去除 Markdown 代码块标记后重试 — 处理不规范的包裹
        5. 截断 JSON 恢复 — 补全未闭合括号/引号，处理 Agent 中途截断

    参数：
        text: Agent 返回的原始文本

    返回：
        解析后的 dict

    异常：
        ValueError: 所有策略都失败时抛出，附带原始文本用于调试
    """
    if not text:
        raise ValueError("Agent 响应为空")

    cleaned = text.strip().lstrip("﻿")

    # 策略 1: 直接解析
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 策略 2: 提取 ```json ... ``` 或 ``` ... ``` 代码块
    fence_matches = _JSON_FENCE_RE.findall(cleaned)
    for match in fence_matches:
        stripped = match.strip()
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            continue

    # 策略 3: 查找第一个 { 和最后一个 }
    brace_candidate: str = ""
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1 and end > start:
        brace_candidate = cleaned[start : end + 1]
        try:
            return json.loads(brace_candidate)
        except json.JSONDecodeError:
            pass

    # 策略 4: 行级处理 — 去掉 Markdown 代码块标记
    lines = cleaned.split("\n")
    stripped_lines = [l for l in lines if not l.strip().startswith("```")]
    plain_text = "\n".join(stripped_lines).strip()
    if plain_text != cleaned:
        try:
            return json.loads(plain_text)
        except json.JSONDecodeError:
            pass

    # 收集用于后续修复策略的候选 JSON 文本
    # 按优先级排列：fence 提取 > brace 提取 > 行级处理 > 原始文本
    candidates_for_quote_fix: list[str] = []
    for m in fence_matches:
        s = m.strip()
        if s:
            candidates_for_quote_fix.append(s)
    if brace_candidate:
        candidates_for_quote_fix.append(brace_candidate)
    if plain_text != cleaned and plain_text:
        candidates_for_quote_fix.append(plain_text)
    candidates_for_quote_fix.append(cleaned)

    # 策略 5: 修复未转义的双引号（Agent 可能在 JSON 字符串值中输出裸引号）
    # 如 "AI"slop"" → "AI\"slop\""
    # 必须在截断恢复之前执行——截断恢复可能产出不完整数据
    for candidate_text in candidates_for_quote_fix:
        try:
            fixed = _fix_unescaped_quotes(candidate_text)
            if fixed != candidate_text:
                result = json.loads(fixed)
                logger.info("JSON 修复成功（转义字符串内未转义引号）")
                return result
        except (json.JSONDecodeError, Exception):
            continue

    # 策略 6: 截断 JSON 恢复
    try:
        recovered = _try_recover_truncated_json(cleaned)
        if recovered is not None:
            logger.warning("从截断 JSON 中恢复了解析结果")
            return recovered
    except Exception:
        pass

    # 也尝试对候选文本做截断恢复
    for candidate_text in candidates_for_quote_fix:
        if candidate_text == cleaned:
            continue  # 已尝试
        try:
            recovered = _try_recover_truncated_json(candidate_text)
            if recovered is not None:
                logger.warning("从截断 JSON 中恢复了解析结果（候选文本）")
                return recovered
        except Exception:
            continue

    preview = text[:500] + "..." if len(text) > 500 else text
    raise ValueError(f"无法从 Agent 响应中提取有效 JSON。响应预览:\n{preview}")


# ---------------------------------------------------------------------------
# 选项构造
# ---------------------------------------------------------------------------


def build_agent_options(
    system_prompt: str = "",
    *,
    model: Optional[str] = None,
    max_turns: int = 3,
    max_tokens: Optional[int] = None,
    stderr: Optional[object] = None,
) -> ClaudeAgentOptions:
    """
    构造标准 ClaudeAgentOptions。

    设计决策：
        - permission_mode="bypassPermissions": 不进行交互式权限询问
        - allowed_tools=[]: Agent 无需文件系统工具，只做思考→输出文本
        - tools=[]: 禁用所有内置工具，减少不必要的 tool_use 消耗
        - mcp_servers={} + strict_mcp_config=True: 彻底隔离用户的 Claude Code 环境。
          背景（2026-07-29 排查）：SDK 每次调用都会拉起一个 claude CLI 子进程，
          CLI 启动时默认加载用户级安装的插件（如 playwright 官方插件），
          插件自带的 @playwright/mcp 会随之启动并弹出有窗口的 Chrome——
          每次 LLM 调用弹一次，并发时浏览器窗口源源不断。
          allowed_tools=[] 只禁止 agent「调用」工具，管不到 CLI 启动阶段的插件加载；
          setting_sources=[] 实测也无效（插件注册信息在 ~/.claude/plugins/ 下，
          不走 settings 文件）。只有显式置空 MCP 配置并开启严格模式，
          才能阻止 CLI 加载任何外部 MCP server（已实测验证：0 个 MCP 进程拉起）。
          原则：浏览器只允许在抓取阶段（ingest/repair 的 BrowserSession）按需使用，
          LLM 阶段只做纯思考，绝不应该碰浏览器。
        - max_turns: 控制最大对话轮数（提取任务 1 轮即可完成）
        - max_tokens: 输出 token 上限。ClaudeAgentOptions 无 max_tokens 字段、CLI 无
          --max-tokens flag，唯一出口是 CLAUDE_CODE_MAX_OUTPUT_TOKENS 环境变量——
          经 env 字段合并进 CLI 子进程环境（显式 env 永远覆盖继承环境）。
          None 时 env 置空 dict，等价于不设，沿用 CLI 默认输出上限。
        - stderr: 捕获 Claude CLI 子进程 stderr，用于诊断底层错误

    参数：
        system_prompt: 系统提示词
        model: 模型名称
        max_turns: 最大对话轮数
        max_tokens: 输出 token 上限（透传为 CLAUDE_CODE_MAX_OUTPUT_TOKENS），None 时不设
        stderr: 文件对象，用于接收 CLI stderr

    返回：
        配置好的 ClaudeAgentOptions 实例
    """
    # 输出 token 上限只能经环境变量透传（见上方 docstring）；空 dict 合并为 no-op，
    # 与不设 env 的现状行为等价，避免回归
    env = {"CLAUDE_CODE_MAX_OUTPUT_TOKENS": str(max_tokens)} if max_tokens is not None else {}

    return ClaudeAgentOptions(
        system_prompt=system_prompt,
        model=model,
        max_turns=max_turns,
        permission_mode="bypassPermissions",
        allowed_tools=[],
        tools=[],
        # 显式置空 MCP 配置 + 严格模式：CLI 只使用此处给出的（空）MCP 配置，
        # 不加载用户 Claude Code 环境中的任何插件 MCP（详见上方 docstring）
        mcp_servers={},
        strict_mcp_config=True,
        stderr=stderr,
        env=env,
    )
