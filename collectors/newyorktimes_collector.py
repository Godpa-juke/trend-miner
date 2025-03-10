from datetime import datetime

import requests

from collectors.base_collector import BaseCollector
from config.config import Config


class NYTimesCollector(BaseCollector):
    def __init__(self, config: Config):
        super().__init__(config)

    def fetch_data(self):
        try:
            url = "https://api.nytimes.com/svc/topstories/v2/home.json"
            params = {
                "api-key": self.config.NYTIMES_API_KEY
            }
            response = requests.get(url, params=params)
            data = response.json()
            results = []
            for article in data.get("results", []):
                results.append({
                    "keyword": article['title'],
                    "source": "NYTimes",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": article.get('url')
                })
            return results
        except Exception as e:
            print(f"[NYTimesCollector] Error: {e}")
            return []