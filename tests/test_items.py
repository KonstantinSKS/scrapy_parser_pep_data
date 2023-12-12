import inspect

import scrapy

try:
    from pep_parse.items import PepParseItem
except ModuleNotFoundError:
    raise AssertionError('Не найден файл `items.py`')
except ImportError as exc:
    raise AssertionError(f'Не найден класс `PepParseItem` в файле {exc.name}')


def test_items_fields():
    assert inspect.isclass(PepParseItem), (
        '`PepParseItem` должен быть классом.'
    )
    assert issubclass(PepParseItem, scrapy.Item), (
        '`PepParseItem` должен наследоваться от `scrapy.Item`'
    )
    fields = ['number', 'name', 'status']
    for field in fields:
        assert field in list(PepParseItem.fields.keys()), (
            f'В `PepParseItem` не хватает атрибута `{field}`'
        )
