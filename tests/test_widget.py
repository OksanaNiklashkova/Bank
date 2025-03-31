import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_information, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счёт 64686473678894779589", "Счёт **9589"),
        ("MasterCard 71583007347267584", "Проверьте правильность ввода!"),
        ("Счет 3538303347444789556", "Проверьте правильность ввода!"),
        ("Visa Classic 6831 9824 7673 7658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 599941422842635", "Проверьте правильность ввода!"),
        ("Счет 7365 4108 4301 3587 4305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_information: str, expected: str) -> None:
    """Тесты для проверки функции маскировки банковских данных"""
    assert mask_account_card(input_information) == expected


def test_get_date_with_valid_date(valid_date_string: str) -> None:
    """Тест для функции преобразования даты - норма"""
    assert get_date(valid_date_string) == "11.03.2024"


def test_get_date_with_another_valid_date(another_valid_date: str) -> None:
    """Тест для функции преобразования даты - вариант нормы"""
    assert get_date(another_valid_date) == "31.12.1999"


def test_get_date_with_invalid_date_string(invalid_date_string: str) -> None:
    """Тест для функции преобразования даты - несуществующая дата"""
    assert get_date(invalid_date_string) == "Проверьте правильность ввода!"


def test_get_date_with_another_invalid_date_string(another_invalid_date_string: str) -> None:
    """Тест для функции преобразования даты - строка, не преобразуемая в дату"""
    assert get_date(another_invalid_date_string) == "Проверьте правильность ввода!"


def test_get_date_with_empty_date_string(empty_date_string: str) -> None:
    """Тест для функции преобразования даты - пустая строка"""
    assert get_date(empty_date_string) == "Проверьте правильность ввода!"
