import requests
from lxml import etree
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class RSSParser:
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.ns = {'ht': 'https://trends.google.com/trending/rss'}

    def fetch_and_parse_rss(self, url: str) -> List[Dict]:
        try:
            logger.info(f"Fetching RSS from: {url}")
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            root = etree.fromstring(response.content)
            return self._parse_items(root)
        except Exception as e:
            logger.error(f"Error fetching or parsing RSS: {e}")
            return []

    def _parse_items(self, root) -> List[Dict]:
        items = []
        for item in root.xpath("//item"):
            title = item.findtext("title")
            traffic = item.findtext("ht:approx_traffic", namespaces=self.ns)
            news_items = [
                {
                    "title": news.findtext("ht:news_item_title", namespaces=self.ns),
                    "url": news.findtext("ht:news_item_url", namespaces=self.ns),
                    "source": news.findtext("ht:news_item_source", namespaces=self.ns)
                }
                for news in item.findall("ht:news_item", namespaces=self.ns)
            ]
            if news_items:
                items.append({"title": title, "approx_traffic": traffic, "news_items": news_items})
        return items
