import logging
from dotenv import load_dotenv
from config import Config
from src.rss_parser import RSSParser
from src.post_generator import PostGenerator
from src.twitter_client import TwitterClient

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    setup_logging()
    load_dotenv()
    config = Config()
    if not config.validate():
        logging.error("Missing API keys. Check your environment variables.")
        return

    rss_parser = RSSParser()
    post_generator = PostGenerator(config.GEMINI_API_KEY, config.MODEL_ID)
    twitter_client = TwitterClient(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    trends = rss_parser.fetch_and_parse_rss(config.RSS_URL)
    for trend in trends[:config.MAX_TRENDS]:
        post = post_generator.generate_post(trend)
        if post:
            twitter_client.post_tweet(post)

if __name__ == "__main__":
    main()
