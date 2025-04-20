from typing import Any
from unittest.mock import patch

import pytest
import requests

from src.external_api import API_KEY, get_amount_transaction


def test_get_amount_transaction1(make_operation_for_get_amount_1: dict) -> None:
    """Тест для функции расчета суммы операции в рублях, исходная сумма в рублях - норма"""
    assert get_amount_transaction(make_operation_for_get_amount_1) == "Сумма по операции в рублях: 31957.58"


def test_get_amount_transaction2(make_operation_for_get_amount_2: dict, capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции расчета суммы операции в рублях - не обрабатываемый код валюты"""
    get_amount_transaction(make_operation_for_get_amount_2)
    captured = capsys.readouterr()
    assert captured.out == "Ошибка запроса! Код валюты не распознан!\n"


@patch("requests.get")
def test_get_amount_transaction3(mock_get: Any) -> None:
    """Тест для функции расчета суммы операции в рублях, исходная сумма в USD - норма"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1530403199, "rate": 62.785038},
        "date": "2018-06-30",
        "historical": True,
        "result": 616804.608265,
    }
    transaction = {
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
    }
    assert get_amount_transaction(transaction) == "Сумма по операции в рублях: 616804.61"
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": API_KEY},
        params={"from": "USD", "to": "RUB", "amount": 9824.07, "date": "2018-06-30"},
    )


def test_get_amount_transaction4(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции расчета суммы операции в рублях: статус ответа на API-запрос 500"""
    mock_response = requests.Response()
    mock_response.status_code = 500
    mock_response._content = b"Internal Server Error"
    with patch("requests.get", return_value=mock_response) as mock_get:
        transaction = {
            "operationAmount": {"amount": "100.0", "currency": {"code": "USD"}},
            "date": "2023-01-01T00:00:00",
        }
        get_amount_transaction(transaction)
        captured = capsys.readouterr()
        assert captured.out == "Ошибка запроса: 500 Server Error: None for url: None\n"
        mock_get.assert_called_once()


@patch("requests.get")
def test_get_amount_transaction5(mock_get: Any, capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции расчета суммы операции в рублях: ошибка API-запросa"""
    mock_get.return_value.json.return_value = {
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "date": "2018-06-30",
        "historical": True,
        "result": None,
    }
    transaction = {
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
    }
    get_amount_transaction(transaction)
    captured = capsys.readouterr()
    assert captured.out == "Ошибка API: запрос не успешен\n"
    mock_get.assert_called_once()
