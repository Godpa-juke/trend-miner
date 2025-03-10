from datetime import datetime

import requests


class StackOverflowCollector:
    def fetch_data(self):
        """Stack Overflow에서 인기 태그 가져오기"""
        try:
            url = "https://api.stackexchange.com/2.3/tags"
            params = {
                "order": "desc",
                "sort": "popular",
                "site": "stackoverflow"
            }
            response = requests.get(url, params=params)
            data = response.json()
            results = []
            for tag in data.get("items", [])[:10]:
                results.append({
                    "keyword": tag['name'],
                    "source": "StackOverflow",
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": f"https://stackoverflow.com/tags/{tag['name']}/info"
                })
            return results
        except Exception as e:
            print(f"[StackOverflowCollector] Error: {e}")
            return []
