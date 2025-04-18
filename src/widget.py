import os
from datetime import datetime
from typing import List

from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def mask_account_card(input_information: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты
    или счета и возвращает строку с замаскированным номером"""
    parts: List[str] = input_information.split()
    number: str = ""
    bill_information: List[str] = []
    for item in parts:
        if item.isdigit():
            number += item
        else:
            bill_information.append(item)

    if len(number) == 16:
        return f'{" ".join(bill_information)} {get_mask_card_number(number)}'
    elif len(number) == 20:
        return f'{" ".join(bill_information)} {get_mask_account(number)}'
    else:
        return "Проверьте правильность ввода!"


@log(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "my_log.txt"))
def get_date(input_date: str) -> str:
    """Функция переводит дату в формат ДД.ММ.ГГГГ"""
    try:
        formated_date = datetime.strptime(input_date[:10], "%Y-%m-%d")
        return f"{formated_date.day:02}.{formated_date.month:02}.{formated_date.year}"
    except ValueError:
        return "Проверьте правильность ввода!"
