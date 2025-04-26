import os
import random

import requests
from dotenv import load_dotenv

from src.decorators import log
from src.utils import get_operations

load_dotenv()
API_KEY = os.getenv("API_KEY")


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def get_amount_transaction(transaction: dict | None = None) -> str | None:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях. Если валюта - USD или EUR, происходит запрос курса
    и осуществляется расчет суммы в рублях"""
    if transaction is None:
        transaction = get_operations()[random.randint(0, 101)]

    currency = transaction["operationAmount"]["currency"].get("code", None)
    amount_t = float(transaction["operationAmount"].get("amount", "0.0"))
    transaction_date = transaction["date"][:10]

    # если валюта - рубль, возвращаем сумму транзакции
    if currency == "RUB":
        amount_r = amount_t
        return f"Сумма по операции в рублях: {amount_r}"

    # если валюта - доллар или евро, делаем запрос для расчета суммы в рублях
    # по курсу на день транзакции
    elif currency == "USD" or currency == "EUR":
        try:
            url = "https://api.apilayer.com/exchangerates_data/convert"
            headers = {"apikey": API_KEY}
            params = {"from": currency, "to": "RUB", "amount": amount_t, "date": transaction_date}
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            # если ответ содержит ключ 'success', т.е. запрос обработан успешно:
            # получаем сумму в рублях по ключу 'result', округляем до 2 знаков
            if not data.get("success", False):
                print("Ошибка API: запрос не успешен")
                return None
            amount_r = round(float(data["result"]), 2)
            return f"Сумма по операции в рублях: {amount_r}"
        # если ответ не получен или не корректен, обрабатываем ошибку
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None
    # сюда попадаем, если транзакция содержит другой код валюты или код валюты не указан
    else:
        print("Ошибка запроса! Код валюты не распознан!")
        return None


print(get_amount_transaction(get_operations()[2]))
