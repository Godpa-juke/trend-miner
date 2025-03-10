from datetime import datetime

import requests

from collectors.base_collector import BaseCollector
from config.config import Config


class YouTubeCollector(BaseCollector):

    def __init__(self, config: Config):
        super().__init__(config)

    def fetch_data(self):
        try:
            url = "https://www.googleapis.com/youtube/v3/videos"
            params = {
                "part": "snippet,statistics",
                "chart": "mostPopular",
                "regionCode": "US",
                "maxResults": 10,
                "key": self.config.YOUTUBE_API_KEY
            }
            response = requests.get(url, params=params)
            data = response.json()
            results = []
            for item in data.get("items", []):
                title = item["snippet"]["title"]
                video_id = item["id"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                results.append({
                    "keyword": title,
                    "source": "YouTube",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": video_url
                })
            return results
        except Exception as e:
            print(f"[YouTubeCollector] Error: {e}")
            return []

