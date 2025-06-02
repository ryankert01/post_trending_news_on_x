import tweepy
import logging

logger = logging.getLogger(__name__)

class TwitterClient:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str, max_length: int = 150):
        self.client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
        self.max_length = max_length

    def post_tweet(self, content: str) -> str:
        try:
            truncated_content = content[:self.max_length]
            response = self.client.create_tweet(text=truncated_content)
            tweet_url = f"https://twitter.com/user/status/{response.data['id']}"
            logger.info(f"Tweet posted: {tweet_url}")
            return tweet_url
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return ""
