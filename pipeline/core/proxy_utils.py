"""
代理工具

从 pipeline/config/proxy.json 读取代理配置并注入环境变量。
所有 HTTP 库 (curl, feedparser, trafilatura) 自动继承这些环境变量。
参考 knowledge-scout/shared/proxy_utils.py 实现。
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
