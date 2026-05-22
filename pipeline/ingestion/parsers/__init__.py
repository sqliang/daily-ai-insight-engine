"""
解析器注册表

每个 key 对应 config.yaml 中的 source.name。
添加新解析器时只需在此注册表中增加一行，无需修改 scout 包。
"""

from .tldrai import parse_tldrai
from .anthropic import parse_anthropic
from .zhihu import parse_zhihu_browser
from .openai import parse_openai_browser

# curl-based scrape 策略解析器
SCRAPE_PARSERS = {
    "tldrai": parse_tldrai,
    "anthropic-blog": parse_anthropic,
    # machine-heart 已移除: jiqizhixin.com 网站改版为数据服务营销页，不再展示文章列表
}

# Playwright browser 策略解析器
BROWSER_PARSERS = {
    "zhihu": parse_zhihu_browser,
    "openai-blog": parse_openai_browser,
    # machine-heart 已移除: 同上原因
}
