import tweepy
from collectors.base_collector import BaseCollector
from config.config import Config
from datetime import datetime

class TwitterCollector(BaseCollector):
    def __init__(self, config: Config):
        super().__init__(config)
        auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
        self.twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

    def fetch_data(self):
        """Twitter 트렌드 (미국 WOEID=23424977)"""
        try:
            trends = self.twitter_api.get_place_trends(id=23424977)
            results = []
            for trend in trends[0]['trends']:
                results.append({
                    "keyword": trend['name'],
                    "source": "Twitter",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": trend.get('url')
                })
            return results
        except Exception as e:
            print(f"[TwitterCollector] Error: {e}")
            return []