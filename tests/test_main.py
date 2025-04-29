from unittest.mock import patch

import pytest

from main import main


def test_main1(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции main - норма"""
    input_responses = [
        "1",  # EXECUTED
        "1",  # Сортировать по дате? Да
        "1",  # По убыванию
        "1",  # Только рублевые транзакции? Да
        "1",  # Фильтр по слову? Да
        "ПЕРЕВОД",
    ]
    with (
        patch("builtins.input", side_effect=input_responses),
        patch("main.make_transactions") as mock_make_transactions,
        patch("main.search_transactions") as mock_search_transactions,
    ):
        mock_make_transactions.return_value = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "RUB",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": "5380041",
                "state": "CANCELED",
                "date": "2021-02-01T11:54:58Z",
                "amount": "23789",
                "currency_name": "Peso",
                "currency_code": "UYU",
                "from": "",
                "to": "Счет 23294994494356835683",
                "description": "Открытие вклада",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
        ]
        mock_search_transactions.return_value = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "руб.",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
        ]

        main()
        captured = capsys.readouterr()
        assert "Распечатываю итоговый список транзакций..." in captured.out
        assert "Всего банковских операций в выборке: 2" in captured.out
        assert "руб." in captured.out
        assert "Перевод" in captured.out


def test_main2(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции main - ошибка ввода, нет операций,
    соответствующих критериям"""
    input_responses = [
        "7",  # ошибка ввода
        "1",  # EXECUTED
        "1",  # Сортировать по дате? Да
        "1",  # По убыванию
        "1",  # Только рублевые транзакции? Да
        "1",  # Фильтр по слову? Да
        "USD",
    ]
    with (
        patch("builtins.input", side_effect=input_responses),
        patch("main.make_transactions") as mock_make_transactions,
        patch("main.search_transactions") as mock_search_transactions,
    ):
        mock_make_transactions.return_value = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "RUB",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": "5380041",
                "state": "CANCELED",
                "date": "2021-02-01T11:54:58Z",
                "amount": "23789",
                "currency_name": "Peso",
                "currency_code": "UYU",
                "from": "",
                "to": "Счет 23294994494356835683",
                "description": "Открытие вклада",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
        ]
        mock_search_transactions.return_value = []

        main()
        captured = capsys.readouterr()
        assert 'Статус операции "7" недоступен' in captured.out
        assert "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации" in captured.out
