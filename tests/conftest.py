import shutil
import os
from pathlib import Path

import pytest

try:
    import pep_parse
except ModuleNotFoundError:
    raise AssertionError('Назовите проект `pep_parse`')


@pytest.fixture
def temp_dir():
    file_path = Path(__file__).parent
    tmp_path = Path(os.path.relpath(file_path / '_tmp'))
    tmp_path.mkdir(exist_ok=True)
    yield tmp_path
    shutil.rmtree(tmp_path, ignore_errors=True)
