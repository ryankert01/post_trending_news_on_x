import time
import logging
from google import genai
from google.genai.types import Tool, GenerateContentConfig, UrlContext

logger = logging.getLogger(__name__)

class PostGenerator:
    def __init__(self, api_key: str, model_id: str):
        self.client = genai.Client(api_key=api_key)
        self.model_id = model_id
        self.rate_limit_delay = 1

    def generate_post(self, trend: dict) -> str:
        try:
            logger.info(f"Generating post for trend: {trend['title']}")
            prompt = self._create_prompt(trend)
            config = GenerateContentConfig(tools=[Tool(url_context=UrlContext)], response_modalities=["TEXT"])
            time.sleep(self.rate_limit_delay)
            response = self.client.models.generate_content(model=self.model_id, contents=prompt, config=config)
            return "\n".join(part.text for part in response.candidates[0].content.parts)
        except Exception as e:
            logger.error(f"Error generating post: {e}")
            return ""

    def _create_prompt(self, trend: dict) -> str:
        prompt = f"你是一位爆紅潛力的台灣在地KOL，請用繁體中文、約50字，幽默風趣地寫一則X（Twitter）貼文，主題是「{trend['title']}」。"
        urls = [news["url"] for news in trend["news_items"] if news.get("url")]
        if urls:
            prompt += "\n".join(f"{i+1}. {url}" for i, url in enumerate(urls))
        else:
            prompt += "\n（沒有相關新聞）"
        return prompt
