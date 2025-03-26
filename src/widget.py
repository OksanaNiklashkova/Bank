from datetime import datetime
from typing import List

from src.masks import get_mask_account, get_mask_card_number


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


def get_date(input_date: str) -> str:
    """Функция переводит дату в формат ДД.ММ.ГГГГ"""
    formated_date = datetime.strptime(input_date[:10], "%Y-%m-%d")
    return f"{formated_date.day:02}.{formated_date.month:02}.{formated_date.year}"
