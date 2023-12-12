from pathlib import Path

try:
    from pep_parse.settings import FEEDS, ITEM_PIPELINES
except ModuleNotFoundError as exc:
    raise AssertionError(
        'Не найден файл `settings.py` по пути '
        f'`pep_parse.{exc.name.split(".")[0]}`',
    )
except ImportError as exc:
    raise AssertionError(
        f'Не найдены настройки `{exc.args[0].split()[3]}` в файле {exc.name}',
    )


def test_settings_feeds():
    assert isinstance(FEEDS, dict), (
        'В файле settings.py необходимо объявить переменную `FEEDS` '
        'типа `dict` согласно документации.\n'
        'Ссылка на документацию: '
        'https://docs.scrapy.org/en/latest/topics/feed-exports.html?highlight=feeds#feeds'
    )
    feeds_path = list(FEEDS.keys())
    assert len(feeds_path) == 1, (
        'В `FEEDS` необходимо объявить только 1 ключ с путём сохранения файла.'
    )
    if isinstance(feeds_path[0], Path):
        feeds_path[0] = str(feeds_path[0])
    splited_path = feeds_path[0].split('/')
    assert splited_path[0] == 'results', (
        'Убедитесь, что в ключе словаря `FEEDS` перед именем файла указан '
        'путь к директории `results/`'
    )
    assert splited_path[1] == 'pep_%(time)s.csv', (
        'В имени файла с перечнем PEP должен быть префикс pep_ '
        'и подстановка даты `%(time)s`'
    )
    path_key = list(FEEDS.keys())[0]
    fields_format_keys = FEEDS.get(path_key)
    assert fields_format_keys.get('fields') == ['number', 'name', 'status'], (
        'Убедитесь, что в FEEDS есть все необходимые поля: '
        '`number, name, status`'
    )
    assert fields_format_keys.get('format') == 'csv', (
        'Проверьте формат вывода файла в FEEDS'
    )


def test_item_pipelines():
    assert isinstance(ITEM_PIPELINES, dict), (
        'В файле settings.py необходимо объявить переменную `ITEM_PIPELINES` '
        'типа `dict` согласно документации.\n'
        'Ссылка на документацию: '
        'https://docs.scrapy.org/en/latest/topics/settings.html?highlight=ITEM_PIPELINES#item-pipelines'
    )
    item_pipelines = list(ITEM_PIPELINES.keys())
    assert len(item_pipelines) == 1, (
        'В `ITEM_PIPELINES` необходимо объявить 1 ключ с именем пайплайна.'
    )
    assert item_pipelines[0] == 'pep_parse.pipelines.PepParsePipeline', (
        'Ключом пайплайна в настройках `ITEM_PIPELINES` должен быть класс.'
    )
    assert ITEM_PIPELINES['pep_parse.pipelines.PepParsePipeline'] in range(1000), (
        'В качестве значения для ключа `pep_parse.pipelines.PepParsePipeline` '
        'в настройках укажите значение из диапазона от `0` и до `1000`'
    )
