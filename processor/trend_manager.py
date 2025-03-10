from collectors.google_trends_collector import GoogleTrendsCollector
from collectors.newyorktimes_collector import NYTimesCollector
from collectors.reddit_collector import RedditCollector
from collectors.stackoverflow_collector import StackOverflowCollector
from collectors.twiiter_collector import TwitterCollector
from collectors.youtube_collectory import YouTubeCollector
from config.config import Config
from processor.trend_processor import TrendProcessor
from repository.csv_repository import CSVRepository


class TrendManager:
    def __init__(self, config: Config):
        # Collector들
        self.collectors = [
            GoogleTrendsCollector(config),
            TwitterCollector(config),
            RedditCollector(config),
            YouTubeCollector(config),
            NYTimesCollector(config),
            StackOverflowCollector(config)
        ]

        # Repository
        self.repository = CSVRepository(file_path="trends_data.csv")

        # Processor
        self.processor = TrendProcessor()



    def collect_and_store(self):
        """모든 Collector로부터 데이터 수집 → 전처리 → 저장"""
        all_trends = []
        for collector in self.collectors:
            data = collector.fetch_data()
            all_trends.extend(data)

        # 전처리(중복 제거 등)
        cleaned = self.processor.process(all_trends)

        # 저장
        self.repository.save_trends(cleaned)
        return cleaned