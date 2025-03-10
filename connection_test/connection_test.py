from collectors.google_trends_collector import GoogleTrendsCollector
from collectors.newyorktimes_collector import NYTimesCollector
from collectors.reddit_collector import RedditCollector
from collectors.twiiter_collector import TwitterCollector
from collectors.youtube_collectory import YouTubeCollector
from config.config import Config


def test_twitter():
    """TwitterCollector를 단발성으로 테스트해보는 예시"""
    config = Config()
    collector = TwitterCollector(config)
    data = collector.fetch_data()

    print("\n========== [Twitter Test] ==========")
    print(f"총 {len(data)}개의 트렌드가 수집되었습니다.\n예시 데이터:")
    for item in data[:5]:
        print(item)

def test_google_trends():
    """GoogleTrendsCollector 단발성 테스트"""
    config = Config()
    collector = GoogleTrendsCollector(config)
    data = collector.fetch_data()

    print("\n========== [GoogleTrends Test] ==========")
    print(f"총 {len(data)}개의 트렌드가 수집되었습니다.\n예시 데이터:")
    for item in data[:5]:
        print(item)

def test_reddit():
    """RedditCollector 단발성 테스트"""
    config = Config()
    collector = RedditCollector(config)
    data = collector.fetch_data()

    print("\n========== [Reddit Test] ==========")
    print(f"총 {len(data)}개의 트렌드가 수집되었습니다.\n예시 데이터:")
    for item in data[:5]:
        print(item)

def test_youtube():
    """YouTubeCollector 단발성 테스트"""
    config = Config()
    collector = YouTubeCollector(config)
    data = collector.fetch_data()

    print("\n========== [YouTube Test] ==========")
    print(f"총 {len(data)}개의 트렌드가 수집되었습니다.\n예시 데이터:")
    for item in data[:5]:
        print(item)

def test_nytimes():
    """NYTimesCollector 단발성 테스트"""
    config = Config()
    collector = NYTimesCollector(config)
    data = collector.fetch_data()

    print("\n========== [NYTimes Test] ==========")
    print(f"총 {len(data)}개의 트렌드가 수집되었습니다.\n예시 데이터:")
    for item in data[:5]:
        print(item)