import pandas as pd
import os

class CSVRepository:
    def __init__(self, file_path="trends_data.csv"):
        self.file_path = file_path

    def save_trends(self, trends_list):
        """
        트렌드 데이터를 CSV 파일에 저장.
        append 모드로 저장하고, 컬럼이 없으면 헤더 작성.
        """
        if not trends_list:
            return

        df = pd.DataFrame(trends_list)
        write_header = not os.path.exists(self.file_path)
        df.to_csv(self.file_path, mode='a', index=False, header=write_header)
        print(f"[CSVRepository] {len(trends_list)}개 항목을 '{self.file_path}'에 저장 완료.")
