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


@pytest.fixture
def make_transactions1() -> list:
    """Фикстура для функции фильтрации по коду валюты - норма"""
    return [
        {"id": 939719570, "currency_code": "USD", "description": "Перевод организации"},
        {"id": 939719577, "currency_code": "USD", "description": "Перевод со счета на счет"},
        {"id": 873106923, "currency_code": "RUB", "description": "Перевод с карты на карту"},
        {"id": 594226727, "currency_code": "RUB", "description": "Перевод организации"},
    ]


@pytest.fixture
def make_transactions2() -> list:
    """Фикстура для тестов функции фильтрации по коду валюты и
    функции получения описания транзакций - пустой список для обработки"""
    return []


@pytest.fixture
def make_transactions3() -> list:
    """Фикстура для теста функции фильтрации по коду валюты -
    'operationAmount' не является словарем,
    для теста функции получения описаний транзакций -
    отсутствует ключ "description" """
    return [
        {"id": 939719570, "code": "USD"},
        {"id": 939719577, "currency_code": "USD", "description": "Перевод со счета на счет"},
    ]


@pytest.fixture
def make_transactions4() -> list:
    """Фикстура для теста функции фильтрации по коду валюты -
    нет ключа currency в одном из словарей"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def make_transactions5() -> list:
    """Фикстура для теста функции фильтрации по коду валюты -
    нет ключа "operationAmount" в одном из словарей"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "Amount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def make_descriptions1() -> list:
    """Фикстура для создания списка описаний транзакций - норма"""
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def make_descriptions3() -> list:
    """Фикстура для создания списка описаний транзакций - ошибка"""
    return ["Ошибка! Отсутствует описание транзакции", "Перевод со счета на счет"]


@pytest.fixture
def make_operation_for_get_amount_1() -> dict:
    """Фикстура для функции получения суммы операции в рублях
    - норма, валюта - рубль"""
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def make_operation_for_get_amount_2() -> dict:
    """Фикстура для функции получения суммы операции в рублях
    - ошибка, валюта не обрабатывается функционалом"""
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "CNY", "code": "CNY"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def make_csv_transaction() -> list:
    """Фикстура для функции чтения csv"""
    return [{"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]


@pytest.fixture
def make_xlsx_transaction1() -> dict:
    """Фикстура для функции преобразования xlsx - норма"""
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


@pytest.fixture
def make_xlsx_transaction2() -> dict:
    """Фикстура для функции преобразования xlsx, нет значения amount"""
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
