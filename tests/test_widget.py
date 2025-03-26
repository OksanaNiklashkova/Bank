import pytest
from typing import List, Optional
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_information, expected", List[str]
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
def test_mask_account_card(input_information: str,
                           expected: str) -> None:
    """Тесты для проверки функции маскировки банковских данных"""
    assert mask_account_card(input_information) == expected
