import pytest
from unittest.mock import patch
from src.external_api import get_amount_transaction, API_KEY


@patch("requests.get")
def test_get_amount_transaction(mock_get) -> None:
    mock_get.return_value.json.return_value = {
        'success': True,
        'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07},
        'info': {'timestamp': 1530403199, 'rate': 62.785038},
        'date': '2018-06-30',
        'historical': True,
        'result': 616804.608265
    }
    transaction = {"date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      },
    },}
    assert get_amount_transaction(transaction) == "Сумма по операции в рублях: 616804.61"
    mock_get.assert_called_once_with(f'https://api.apilayer.com/exchangerates_data/convert',
                                     headers={'apikey': API_KEY},
                                     params={'from': 'USD', 'to': 'RUB', 'amount': 9824.07, 'date': '2018-06-30'})

