import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULT_DIR = 'results'


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        pep_status = item['status']
        self.results[pep_status] = self.results.get(pep_status, 0) + 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_DIR
        now = dt.datetime.now()
        now_format = now.strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now_format}.csv'
        file_path = results_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for key, value in self.results.items():
                total += value
                f.write(f'{key},{value}\n')
            f.write(f'Total,{total}\n')
