import inspect

try:
    from pep_parse.pipelines import PepParsePipeline
except ModuleNotFoundError as exc:
    raise AssertionError(
        'Не найден файл `pipelines.py` по пути '
        f'`pep_parse.{exc.name.split(".")[0]}`',
    )
except ImportError as exc:
    raise AssertionError(
        f'Не найден класс `PepParsePipeline` в файле {exc.name}',
    )


def test_pep_parse_pipeline():
    assert inspect.isclass(PepParsePipeline), (
        '`PepParsePipeline` должен быть классом.'
    )


def test_pipeline_open_spider():
    got = PepParsePipeline()
    assert hasattr(got, 'open_spider'), (
        f'В классе `{got.__class__.__name__}` должен быть метод `open_spider`.'
    )
    assert callable(got.open_spider), (
        f'`open_spider` класса {got.__class__.__name__} должен '
        'быть вызываемым методом.'
    )
    pep_pipeline_signature = list(
        inspect.signature(got.open_spider).parameters,
    )
    assert pep_pipeline_signature == ['spider'], (
        f'Метод `open_spider` класса {got.__class__.__name__} должен '
        'принимать параметр `spider`'
    )


def test_pipeline_process_item():
    got = PepParsePipeline()
    assert hasattr(got, 'process_item'), (
        f'В классе `{got.__class__.__name__}` '
        'должен быть метод `process_item`.'
    )
    assert callable(got.process_item), (
        f'`process_item` класса {got.__class__.__name__} должен '
        'быть вызываемым методом.'
    )
    pep_parse_pipeline_signature = list(
        inspect.signature(got.process_item).parameters,
    )
    assert pep_parse_pipeline_signature == ['item', 'spider'], (
        f'Метод `process_item` класса {got.__class__.__name__} должен '
        'принимать параметры `item, spider`'
    )


def test_pipeline_close_spider():
    got = PepParsePipeline()
    assert hasattr(got, 'close_spider'), (
        f'В классе `{got.__class__.__name__}` '
        'должен быть метод `close_spider`.'
    )
    assert callable(got.close_spider), (
        f'`close_spider` класса {got.__class__.__name__} должен '
        'быть вызываемым методом.'
    )
    pep_parse_pipeline_signature = list(
        inspect.signature(got.close_spider).parameters,
    )
    assert pep_parse_pipeline_signature == ['spider'], (
        f'Метод `close_spider` класса {got.__class__.__name__} должен '
        'принимать параметр `spider`'
    )
