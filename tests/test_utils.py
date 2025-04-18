from src.utils import get_operations


def test_get_operations1() -> None:
    """Тест для функции чтения банковских операций
    из json-файла - норма"""
    assert get_operations()[1] == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_get_operations2() -> None:
    """Тест для функции чтения банковских операций
    из json-файла - ошибка"""
    data_path = "..tests"
    assert get_operations(data_path) == []
