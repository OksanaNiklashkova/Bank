from datetime import datetime
from typing import List

from src.masks import get_mask_account, get_mask_card_number
from src.decorators import log


@log()
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


@log()
def get_date(input_date: str) -> str:
    """Функция переводит дату в формат ДД.ММ.ГГГГ"""
    try:
        formated_date = datetime.strptime(input_date[:10], "%Y-%m-%d")
        return f"{formated_date.day:02}.{formated_date.month:02}.{formated_date.year}"
    except ValueError:
        return "Проверьте правильность ввода!"


if __name__ == "__main__":
    print(mask_account_card('Счёт 7158 3524 8007 3472 6758'))
    print(mask_account_card('Счёт 7158 3524 8007 3472 6758 1575'))
    print(get_date('2024-03-11T02:26:18.671407'))
    print(get_date('2024-13-11T02:26:18.671407'))