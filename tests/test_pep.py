import inspect

import scrapy

try:
    from pep_parse.spiders.pep import PepSpider
except ModuleNotFoundError:
    raise AssertionError('Не найден файл `pep.py`')
except ImportError as exc:
    raise AssertionError(
        f'Не найден класс `{exc.args[0].split()[3]}` в файле {exc.name}',
    )


def test_pep_spider():
    assert inspect.isclass(PepSpider), (
        '`PepSpider` должен быть классом.'
    )
    assert issubclass(PepSpider, scrapy.Spider), (
        '`PepSpider` должен наследоваться от `scrapy.Spider`'
    )


def test_pep_spider_attrs():
    assert PepSpider.name, (
        'Класс `PepSpider` должен иметь атрибут `name`.'
    )
    assert PepSpider.name == 'pep', (
        'Значением атрибута `name` класса `PepSpider` лучше задать `pep`'
    )
    assert hasattr(PepSpider, 'start_urls'), (
        'Класс `PepSpider` должен иметь атрибут `start_urls`.'
    )
    assert PepSpider.start_urls == ['https://peps.python.org/'], (
        'В классе PepSpider для атрибута start_urls установите список со значением '
        'https://peps.python.org/'
    )


def test_pep_spider_parse():
    got = PepSpider()
    assert hasattr(got, 'parse'), (
        f'Класс `{got.__class__.__name__}` должен иметь метод `parse`.'
    )
    assert callable(got.parse), (
        f'Убедитесь, что `parse` в классе {got.__class__.__name__} '
        '- это вызываемый метод.'
    )


def test_pep_spider_parse_pep():
    got = PepSpider()
    assert hasattr(got, 'parse_pep'), (
        f'В классе `{got.__class__.__name__}` должен быть метод `parse_pep`.'
    )
    assert callable(got.parse_pep), (
        f'Убедитесь, что `parse_pep` в классе {got.__class__.__name__} '
        '- это вызываемый метод.'
    )
