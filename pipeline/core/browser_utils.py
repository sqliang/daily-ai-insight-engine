"""
Playwright 浏览器工具

封装 Playwright sync API，提供浏览器生命周期管理和页面抓取能力。
所有 browser 策略的数据源共用同一个 BrowserSession，一次 stage 运行中复用。

Usage:
    from pipeline.core.browser_utils import BrowserSession, fetch_rendered_html

    # Scout / Ingest: 在 stage 入口创建 session，传入解析器
    with BrowserSession() as session:
        html = session.fetch_page_html("https://example.com", wait_for=".content")
"""

from typing import Optional


class BrowserSession:
    """
    Playwright headless Chromium 会话管理器 (同步 API)。

    作为 context manager 使用，在 __enter__ 中启动浏览器和持久 context，
    在 __exit__ 中自动关闭。一次 stage 运行中创建一次，所有同策略源共用。

    Proxy: 读取 config/proxy.json 并传入浏览器 launch context。
    反检测: 默认配置真实 Chrome UA、viewport、bypass_csp。
    """

    def __init__(
        self,
        headless: bool = True,
        proxy: Optional[dict] = None,
        user_agent: Optional[str] = None,
        locale: str = "zh-CN",
    ):
        self._headless = headless
        self._proxy = proxy
        self._user_agent = user_agent or (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/130.0.0.0 Safari/537.36"
        )
        self._locale = locale

        self._playwright = None
        self._browser = None
        self.context = None

    # ---------------------------------------------------------------
    # Context Manager
    # ---------------------------------------------------------------

    def __enter__(self) -> "BrowserSession":
        from playwright.sync_api import sync_playwright

        self._playwright = sync_playwright().start()
        launch_args = self._build_launch_args()
        self._browser = self._playwright.chromium.launch(**launch_args)
        self.context = self._browser.new_context(**self._build_context_args())
        return self

    def __exit__(self, *args):
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()

    # ---------------------------------------------------------------
    # Page Operations
    # ---------------------------------------------------------------

    def new_page(self):
        """在持久 context 中创建新页面。"""
        return self.context.new_page()

    def fetch_page_html(
        self,
        url: str,
        wait_for: Optional[str] = None,
        wait_ms: int = 2000,
        timeout: int = 30000,
        wait_until: str = "domcontentloaded",
        wait_for_fn: Optional[str] = None,
    ) -> Optional[str]:
        """
        导航到 URL，等待 JS 渲染完成后返回 page.content()。

        wait_for:    CSS 选择器，等待该元素出现后再返回 HTML
        wait_ms:     当 wait_for/wait_for_fn 均未指定时，固定等待毫秒数
        timeout:     导航超时 (毫秒)
        wait_until:  导航等待策略，默认 domcontentloaded，
                     可设为 networkidle 等待网络空闲（用于 Cloudflare 等 JS 重定向页面）
        wait_for_fn: JavaScript 表达式，轮询直到其返回 truthy 值再返回 HTML。
                     用于等待 Cloudflare 验证通过后页面内容出现，
                     如 "document.body.innerText.length > 200"
        """
        page = self.new_page()
        try:
            page.goto(url, timeout=timeout, wait_until=wait_until)
            if wait_for:
                page.wait_for_selector(wait_for, timeout=timeout)
            elif wait_for_fn:
                page.wait_for_function(wait_for_fn, timeout=timeout)
            else:
                page.wait_for_timeout(wait_ms)
            return page.content()
        except Exception as e:
            print(f"         [browser] 页面加载失败: {e}")
            return None
        finally:
            page.close()

    # ---------------------------------------------------------------
    # Internal
    # ---------------------------------------------------------------

    def _build_launch_args(self) -> dict:
        args = {
            "headless": self._headless,
            "args": [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ],
        }
        return args

    def _build_context_args(self) -> dict:
        ctx = {
            "user_agent": self._user_agent,
            "viewport": {"width": 1920, "height": 1080},
            "locale": self._locale,
            "bypass_csp": True,
        }
        proxy_config = self._resolve_proxy()
        if proxy_config:
            ctx["proxy"] = proxy_config
        return ctx

    def _resolve_proxy(self) -> Optional[dict]:
        proxy = self._proxy
        if proxy is None:
            try:
                from pipeline.core.proxy_utils import load_proxy_config
                proxy = load_proxy_config()
            except Exception:
                proxy = None
        if not proxy:
            return None
        server = proxy.get("https") or proxy.get("http") or proxy.get("all")
        if not server:
            return None
        return {"server": server}


def fetch_rendered_html(
    url: str,
    wait_for: Optional[str] = None,
    wait_ms: int = 2000,
    timeout: int = 30000,
    headless: bool = True,
    wait_until: str = "domcontentloaded",
    wait_for_fn: Optional[str] = None,
) -> Optional[str]:
    """
    一次性获取 JS 渲染后的页面 HTML。
    适用于不需要复用浏览器 session 的场景 (如 ingest 单独抓取一篇)。
    """
    with BrowserSession(headless=headless) as session:
        return session.fetch_page_html(
            url, wait_for=wait_for, wait_ms=wait_ms,
            timeout=timeout, wait_until=wait_until,
            wait_for_fn=wait_for_fn,
        )
