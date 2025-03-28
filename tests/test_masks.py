from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """Тесты для функции максировки номера карты"""
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    assert get_mask_card_number("1234 5678 9123 4567") == "1234 56** **** 4567"
    assert get_mask_card_number("12345678912345678") == "Проверьте правильность введенного номера карты!"
    assert get_mask_card_number("123456789123456") == "Проверьте правильность введенного номера карты!"
    assert get_mask_card_number("") == "Проверьте правильность введенного номера карты!"
    assert get_mask_card_number("A23456789123456") == "Проверьте правильность введенного номера карты!"


def test_get_mask_account() -> None:
    """Тесты для функции маскировки номера счета"""
    assert get_mask_account("12345678912345678912") == "**8912"
    assert get_mask_account("1234 5678 9123 4567 8912") == "**8912"
    assert get_mask_account("123456789123456789123") == "Проверьте правильность введенного номера счета!"
    assert get_mask_account("1234567891234567891") == "Проверьте правильность введенного номера счета!"
    assert get_mask_account("") == "Проверьте правильность введенного номера счета!"
    assert get_mask_account("A2345678912345678912") == "Проверьте правильность введенного номера счета!"
