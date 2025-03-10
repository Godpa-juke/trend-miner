from collectors.base_collector import BaseCollector
from config.config import Config
from pytrends.request import TrendReq
from datetime import datetime

class GoogleTrendsCollector(BaseCollector):
    def __init__(self, config: Config):
        super().__init__(config)
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def fetch_data(self):
        try:
            trending_searches = self.pytrends.trending_searches(pn='united_states')
            results = []
            for keyword in trending_searches[0].tolist():
                results.append({
                    "keyword": keyword,
                    "source": "GoogleTrends",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": None
                })
            return results
        except Exception as e:
            print(f"[GoogleTrendsCollector] Error: {e}")
            return []