from datetime import datetime

import praw

from collectors.base_collector import BaseCollector
from config.config import Config


class RedditCollector(BaseCollector):
    def __init__(self, config: Config):
        super().__init__(config)
        self.reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=config.REDDIT_USER_AGENT
        )

    def fetch_data(self):
        """Reddit 인기 게시글 제목 가져오기 (popular Subreddit)"""
        try:
            subreddit = self.reddit.subreddit("popular")
            results = []
            for post in subreddit.hot(limit=10):
                results.append({
                    "keyword": post.title,
                    "source": "Reddit",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": f"https://www.reddit.com{post.permalink}"
                })
            return results
        except Exception as e:
            print(f"[RedditCollector] Error: {e}")
            return []