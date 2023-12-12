import re

import pytest
from pep_parse import pipelines
from scrapy.crawler import CrawlerProcess

try:
    from pep_parse.spiders.pep import PepSpider
except ModuleNotFoundError:
    raise AssertionError(
        'В директории pep_parse.spiders не найден файл `pep.py`',
    )


def test_run_scrapy(monkeypatch, temp_dir):
    mock_base_dir = temp_dir
    monkeypatch.setattr(pipelines, 'BASE_DIR', mock_base_dir)

    process = CrawlerProcess(settings={
        'LOG_ENABLED': False,
        'LOG_LEVEL': 'ERROR',
        'HTTP_CACHE': True,
        'HTTPCACHE_ENABLED': True,
        'ITEM_PIPELINES': {
            'pep_parse.pipelines.PepParsePipeline': 300,
        },
        'FEEDS': {
            mock_base_dir / 'results/pep_%(time)s.csv': {
                'format': 'csv',
                'fields': ['number', 'name', 'status'],
            },
        },
    })
    process.crawl(PepSpider)
    process.start()

    dirs = [
        directory.name for directory in mock_base_dir.iterdir()
        if directory.is_dir()
    ]
    output_files = [
        file for file in mock_base_dir.glob('**/*')
        if str(file).endswith('.csv')
    ]
    assert 'results' in dirs, (
        'Убедитесь что в директории проекта создается директория `results` для '
        'вывода в файл результатов.'
    )
    assert len(output_files) == 2, (
        'Убедитесь, что создано два csv-файла с результами парсинга'
    )
    assert any('pep_' in str(file) for file in output_files), (
        'Убедитесь, что список PEP сохраняется в файл с префиксом `pep_`'
    )
    assert any('status_summary_' in str(file) for file in output_files), (
        'Убедитесь, что сводка о числе документов в каждом статусе '
        'сохраняется в файл с префиксом `status_summary_`'
    )


@pytest.mark.skip()
def test_check_correct_output_files():
    with open(
        [file for file in output_files if 'pep' in str(file)][0], 'r',
    ) as file:
        file_result = file.read()
        pep_pattern = re.compile(r'(\d)+\,PEP\s?(\d)+\s?(.)+')
        assert re.search(pep_pattern, file_result), (
            'Проверьте формат записи строк в файл `pep_`.'
            'Строки должны соответствовать виду '
            '"20,PEP 20 – The Zen of Python,Active"'
        )
    with open(
        [
            file for file in output_files if 'status_summary_' in str(file)
        ][0], 'r',
    ) as file:
        file_result = file.read()
        active_pattern = re.compile(r'Active,(\d)+')
        assert re.search(active_pattern, file_result), (
            'Убедитесь, что строки в файле `status_summary_` '
            'записываются в правильном формате: `Статус,Количество`'
        )
