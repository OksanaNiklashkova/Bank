import pytest


@pytest.fixture
def valid_date_string() -> str:
    """Фикстура для проверки преобразования даты - норма"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def another_valid_date() -> str:
    """Фикстура для проверки преобразования даты - вариант нормы"""
    return "1999-12-31"


@pytest.fixture
def invalid_date_string() -> str:
    """Фикстура для проверки преобразования даты - несуществующая дата"""
    return "1999-12-32"


@pytest.fixture
def another_invalid_date_string() -> str:
    """Фикстура для проверки преобразования даты - не преобразумый формат данных"""
    return "the date"


@pytest.fixture
def empty_date_string() -> str:
    """Фикстура для проверки преобразования даты - пустая строка"""
    return ""


@pytest.fixture
def make_operations1() -> list:
    """Фикстура для функций фильтрации/сортировки - норма"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def make_operations2() -> list:
    """Фикстура
    для функции фильтрации - нет статусов 'EXECUTED'/
    для функции сортировки - несуществующая дата"""
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-32T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def make_operations3() -> list:
    """Фикстура
    для функции фильтрации - нет значений по ключу 'state'/
    для функции сортировки - другой формат даты, вариант нормы"""
    return [
        {"id": 41428829, "date": "2019-07-03"},
        {"id": 939719570, "date": "2018-06-30"},
        {"id": 594226727, "date": "2018-09-12"},
        {"id": 615064591, "date": "2018-10-14"},
    ]


@pytest.fixture
def make_operations4() -> list:
    """Фикстура
    для функции фильтрации - в части словарей нет значений по ключу 'state'/
    для функции сортировки - в части словарей нет значений по ключу 'date'"""
    return [
        {"id": 41428829, "state": "CANCELED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def make_operations5() -> list:
    """Фикстура для функций фильтрации/сортировки - пустой список"""
    return []
