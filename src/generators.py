import json
from typing import Any
import os
from src.decorators import log


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def filter_by_currency(transaction_list: list, currency: str) -> Any:
    """Функция обрабатывает список транзакций и поочередно
    выдает транзакции, где валюта операции соответствует заданной"""
    if len(transaction_list) == 0:
        yield "Отсутствуют данные для обработки"
    elif any(
        not isinstance(transaction.get("operationAmount"), dict) or "currency" not in transaction["operationAmount"]
        for transaction in transaction_list
    ):
        yield "Для одной или нескольких транзакций значение валюты не задано"
    elif not any(
        transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        for transaction in transaction_list
    ):
        yield "В списке отсутствуют транзакции с данной валютой"
    else:
        yield from (
            transaction
            for transaction in transaction_list
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        )


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def transaction_descriptions(transaction_list: list) -> Any:
    """Функция обрабатывает список транзакций и поочередно
    возвращает описание каждой из них"""
    if len(transaction_list) == 0:
        yield "Отсутствуют данные для обработки"
    else:
        for transaction in transaction_list:
            yield transaction.get("description", "Ошибка! Отсутствует описание транзакции")


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def card_number_generator(start: int, stop: int) -> Any:
    """Функция представляет собой генератор номеров банковских карт:
    создает номера в заданном диапазоне и возвращает их
    в формате XXXX XXXX XXXX XXXX"""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Неверный формат данных!")
    if start <= 0 or len(str(start)) > 16 or len(str(stop)) > 16:
        raise ValueError("Ошибка при вводе значений границ диапазона!")
    elif start >= stop:
        raise ValueError("Ошибка: начальное значение должно быть меньше конечного!")
    else:
        current = start
        while current != stop:
            zero_count = 16 - len(str(current))
            result = "0" * zero_count + str(current)
            card_number = f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:]}"
            yield card_number
            current += 1
