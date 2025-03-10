from abc import ABC, abstractmethod
from config.config import Config

class BaseCollector(ABC):
    """
    모든 Collector의 공통 뼈대를 정의.
    필요하다면 공통 메서드나 에러처리, 로깅 로직을 넣을 수 있음.
    """
    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    def fetch_data(self):
        """
        실제 데이터 수집 로직을 각 서브 클래스가 구현.
        반환 값은 [
            { "keyword": str, "source": str, "timestamp": str, "url": str or None },
            ...
        ] 형태를 권장.
        """
        pass