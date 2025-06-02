import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    RSS_URL: str = "https://trends.google.com/trending/rss?geo=TW"
    MODEL_ID: str = "gemini-2.5-flash-preview-05-20"
    MAX_TRENDS: int = 1
    POST_MAX_LENGTH: int = 150

    GEMINI_API_KEY: Optional[str] = None
    CONSUMER_KEY: Optional[str] = None
    CONSUMER_SECRET: Optional[str] = None
    ACCESS_TOKEN: Optional[str] = None
    ACCESS_TOKEN_SECRET: Optional[str] = None

    def __post_init__(self):
        self.GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
        self.CONSUMER_KEY = os.getenv('CONSUMER_KEY')
        self.CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
        self.ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
        self.ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    def validate(self) -> bool:
        required_keys = [
            self.GEMINI_API_KEY,
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET,
            self.ACCESS_TOKEN,
            self.ACCESS_TOKEN_SECRET
        ]
        return all(key is not None for key in required_keys)
