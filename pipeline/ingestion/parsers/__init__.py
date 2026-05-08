"""
解析器注册表

每个 key 对应 config.yaml 中的 source.name。
添加新解析器时只需在此注册表中增加一行，无需修改 scout.py。
"""

from .tldrai import parse_tldrai
from .anthropic import parse_anthropic
from .zhihu import parse_zhihu_browser
from .machine_heart import parse_machine_heart, parse_machine_heart_browser

# curl-based scrape 策略解析器
SCRAPE_PARSERS = {
    "tldrai": parse_tldrai,
    "anthropic-blog": parse_anthropic,
    "machine-heart": parse_machine_heart,
}

# Playwright browser 策略解析器
BROWSER_PARSERS = {
    "zhihu": parse_zhihu_browser,
    "machine-heart": parse_machine_heart_browser,
}
