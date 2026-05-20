"""
网络代理配置模块

功能描述
- 从 pipeline/config/proxy.json 读取代理配置并注入环境变量。
- 所有 HTTP 库 (curl, feedparser, trafilatura) 自动继承这些环境变量。
- 自动注入到当前进程环境变量
- 后续所有网络请求（curl / subprocess）自动走代理

设计背景：
- 很多开发环境无法直连外网，需要代理才能访问 HN 等站点
- 代理地址不应硬编码在代码里，通过配置文件管理
- 程序启动时最早执行，确保后续所有网络请求都生效

使用方式：
    from shared.proxy_utils import setup_proxy
    setup_proxy()  # 在任何网络请求前调用

配置文件格式（config/proxy.json）：
    {
      "proxy": {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
        "all": "socks5://127.0.0.1:7890"
      }
    }

环境变量说明：
- http_proxy / HTTP_PROXY: HTTP 请求代理
- https_proxy / HTTPS_PROXY: HTTPS 请求代理
- all_proxy / ALL_PROXY: 所有协议代理（兜底）

注意：
- 同时设置大写版本是为了兼容不同工具的大小写敏感行为
- proxychains 类工具依赖 all_proxy，需要 socks5 协议

"""

import json
import os
import subprocess
from pathlib import Path
from typing import Dict, Optional

from .file_utils import get_project_root


def load_proxy_config() -> Optional[Dict[str, str]]:
    """
    读取 pipeline/config/proxy.json 中的代理配置。
    返回 {"http": "...", "https": "...", "all": "..."} 或 None。
    """
    proxy_path = get_project_root() / "pipeline" / "config" / "proxy.json"
    if not proxy_path.exists():
        return None
    try:
        with open(proxy_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("proxy", {})
    except (json.JSONDecodeError, IOError):
        return None


def setup_proxy() -> bool:
    """
    将代理配置写入 os.environ。
    同时设置大小写两种变量名，兼容不同工具的需求。
    返回 True 表示代理已配置。
    """
    proxy = load_proxy_config()
    if not proxy:
        return False

    # HTTP/HTTPS 代理
    for scheme in ("http", "https"):
        url = proxy.get(scheme)
        if url:
            os.environ[scheme + "_proxy"] = url
            os.environ[scheme.upper() + "_PROXY"] = url

    # SOCKS5 全协议代理
    all_url = proxy.get("all")
    if all_url:
        os.environ["all_proxy"] = all_url
        os.environ["ALL_PROXY"] = all_url

    return True


def check_proxy(timeout: int = 10) -> bool:
    """
    验证代理连通性：通过代理访问一个可靠的 HTTPS 地址。
    返回 True 表示代理可正常访问外网。
    """
    env = os.environ.copy()
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                "--max-time", str(timeout),
                "https://news.ycombinator.com/",
            ],
            capture_output=True, text=True, env=env, timeout=timeout + 5,
        )
        return result.stdout.strip() == "200"
    except Exception:
        return False
