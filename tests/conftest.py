import pytest
from datetime import datetime

@pytest.fixture
def valid_date_string():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def another_valid_date():
    return "1999-12-31"

@pytest.fixture
def invalid_date_string():
    return "1999-12-32"

@pytest.fixture
def another_invalid_date_string():
    return "the date"

@pytest.fixture
def empty_date_string():
    return ""
