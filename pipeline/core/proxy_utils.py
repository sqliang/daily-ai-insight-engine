"""
pipeline/core/proxy_utils.py — 网络代理配置模块

在 pipeline/run.py 入口最先调用，确保所有后续网络请求自动走代理。
curl / subprocess / requests / httpx / feedparser / trafilatura 均会继承 os.environ 中的代理变量。

设计决策：
- 代理地址不硬编码，通过 pipeline/config/proxy.json 管理
- 配置文件不存在或不合法时不阻断程序，打印警告后走直连
- 同时设置大小写变量名，兼容不同工具的大小写敏感行为
- all_proxy (SOCKS5) 用于 proxychains 等全局代理场景

配置文件格式（pipeline/config/proxy.json）：
    {
      "proxy": {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
        "all": "socks5://127.0.0.1:7890"
      }
    }

环境变量注入说明：
- http_proxy / HTTP_PROXY: HTTP 请求代理
- https_proxy / HTTPS_PROXY: HTTPS 请求代理
- all_proxy / ALL_PROXY: 所有协议代理（兜底，用于 proxychains 等工具）
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, Dict

# ---------------------------------------------------------------------------
# 配置常量
# ---------------------------------------------------------------------------

# proxy.json 路径：pipeline/core/proxy_utils.py → parent.parent → pipeline/config/proxy.json
_PROXY_CONFIG_PATH: Path = Path(__file__).resolve().parent.parent / "config" / "proxy.json"

# 代理连通性测试 URL，用于 check_proxy()
# 选择 GitHub 是因为它是项目实际需要访问的 Git 托管平台
_PROXY_TEST_URL: str = "https://github.com/"

# 代理连通性测试超时（秒）
# 10 秒足够判断代理是否可用，超时直接判定不可达
_PROXY_TEST_TIMEOUT: int = 10


# ---------------------------------------------------------------------------
# 代理配置加载
# ---------------------------------------------------------------------------

def load_proxy_config() -> Optional[Dict[str, str]]:
    """
    从 pipeline/config/proxy.json 读取代理配置。

    返回：
        dict: {"http": "...", "https": "...", "all": "..."}
        None: 配置文件不存在或格式错误

    设计理由：
        返回 None 而非抛出异常 — 代理是可选的，无代理时程序应能运行（直连模式），
        只是网络请求可能因环境限制而失败。
    """
    if not _PROXY_CONFIG_PATH.exists():
        return None

    try:
        with open(_PROXY_CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 兼容两种 JSON 结构：顶层含 "proxy" 包装 key，或直接就是代理字段
        if "proxy" in data and isinstance(data["proxy"], dict):
            return data["proxy"]

        # 顶层直接包含 http/https/all 字段
        if isinstance(data, dict) and ("http" in data or "https" in data or "all" in data):
            return data

        return None

    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️  代理配置文件解析失败: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# 代理注入
# ---------------------------------------------------------------------------

def setup_proxy() -> bool:
    """
    将代理配置写入 os.environ，所有后续网络请求自动继承。

    调用时机：
        必须在任何网络请求之前调用，建议在入口脚本最早期执行。

    返回：
        True: 代理已成功注入环境变量
        False: 未找到有效代理配置，走直连

    实现细节：
        - 同时设置大小写变量名（如 http_proxy 和 HTTP_PROXY），兼容 curl、wget、requests 等
        - all_proxy 为 SOCKS5 兜底，供 proxychains 等工具使用
        - 未配置的协议不会被设置，避免误用
    """
    proxy = load_proxy_config()

    if not proxy:
        print("⚠️  未找到代理配置，将尝试直连网络", file=sys.stderr)
        return False

    if "http" in proxy:
        os.environ["http_proxy"] = proxy["http"]
        os.environ["HTTP_PROXY"] = proxy["http"]

    if "https" in proxy:
        os.environ["https_proxy"] = proxy["https"]
        os.environ["HTTPS_PROXY"] = proxy["https"]

    if "all" in proxy:
        os.environ["all_proxy"] = proxy["all"]
        os.environ["ALL_PROXY"] = proxy["all"]

    # 打印确认信息，优先展示 HTTPS 代理（大多数场景使用 HTTPS）
    display_url = proxy.get("https") or proxy.get("http") or proxy.get("all", "")
    print(f"✅ 代理已配置: {display_url}")
    return True


# ---------------------------------------------------------------------------
# 代理连通性校验（可选）
# ---------------------------------------------------------------------------

def check_proxy(timeout: int = _PROXY_TEST_TIMEOUT) -> bool:
    """
    通过实际发起 HTTPS 请求校验代理连通性。

    参数：
        timeout: 请求超时时间（秒），默认 10

    返回：
        True: 代理可用（收到 HTTP 200）
        False: 代理不可达或网络故障

    设计理由：
        此函数独立于 setup_proxy()，不自动调用，原因：
        - setup_proxy() 应无感知运行，不应因网络波动阻断程序
        - 用户可自行决定是否需要连通性校验
        - 避免在 CI / 单元测试中因网络不可达而失败
    """
    try:
        result = subprocess.run(
            [
                "curl", "-s",            # -s: 静默，不显示进度条
                "-o", "/dev/null",       # 丢弃响应体，只关心状态码
                "-w", "%{http_code}",    # 只输出 HTTP 状态码
                "--max-time", str(timeout),
                _PROXY_TEST_URL,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 5,          # subprocess 超时比 curl 超时多 5 秒
        )
        return result.stdout.strip() == "200"
    except Exception:
        return False


# ---------------------------------------------------------------------------
# 独立运行：校验代理配置是否正确
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    setup_proxy()

    print("-" * 40)
    if check_proxy():
        print("✅ 代理连通性正常")
        sys.exit(0)
    else:
        print("❌ 代理连通性测试失败，请检查代理服务是否运行")
        sys.exit(1)
