import time
import schedule
from config.config import Config
from connection_test.connection_test import test_twitter, test_google_trends, test_reddit, test_youtube, test_nytimes
from processor.trend_manager import TrendManager


def job_collect(manager: TrendManager):
    print("[Scheduler] 트렌드 수집 및 저장 시작...")
    data = manager.collect_and_store()
    print(f"[Scheduler] 수집 완료. {len(data)}개 항목 수집/저장.\n")


def job_publish(manager: TrendManager):
    print("[Scheduler] 블로그 게시 시작...")
    # 여기서는 간단히 새로 수집한 데이터로 즉시 게시
    # (원한다면 '최근 1시간 내 수집된 데이터만' 등 추가 로직 가능)
    data = manager.collect_and_store()
    manager.publish_post(data)
    print("[Scheduler] 게시 완료.\n")

def main():
    config = Config()
    manager = TrendManager(config)

    # 1) 1시간마다 수집/저장
    schedule.every(1).hours.do(job_collect, manager)

    # 2) 2시간마다 블로그 게시 (ex. 하루 12회)
    schedule.every(2).hours.do(job_publish, manager)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    # main()
    # test_twitter()

    # 필요한 다른 플랫폼도 테스트하려면 주석 해제
    test_google_trends()
    # test_reddit()
    # test_youtube()
    # test_nytimes()