class TrendProcessor:
    @staticmethod
    def remove_duplicates(trends):
        seen = set()
        unique_list = []
        for t in trends:
            # (keyword, source) 기준으로 중복 제거 예시
            uid = (t["keyword"], t["source"])
            if uid not in seen:
                seen.add(uid)
                unique_list.append(t)
        return unique_list

    @staticmethod
    def process(trends):
        """추가 전처리/필터링/랭킹/요약 로직을 여기서 구현 가능"""
        cleaned = TrendProcessor.remove_duplicates(trends)
        return cleaned
