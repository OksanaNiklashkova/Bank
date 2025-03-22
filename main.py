from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from pathlib import Path
import os

if __name__ == '__main__':
    # Maestro 1596837868705199
    # Счет 64686473678894779589
    # MasterCard 7158300734726758
    # Счет 35383033474447895560
    # Visa Classic 6831982476737658
    # Visa Platinum 8990922113665229
    # Visa Gold 5999414228426353
    # Счет 73654108430135874305
    base_dir = Path(__file__).parent
    file_path = base_dir / 'data' / 'data_for_example.txt'
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as file:
            input_information = file.readlines()
            print(input_information)
            common_for_mask = input_information[input(int("Введите номер строки от 1 до 8:"))]
            print(f"""Входные данные данные - {common_for_mask}
            Результат обработки - {mask_account_card(common_for_mask)}""")

        # 2024-03-11T02:26:18.671407
            input_date = str(input_information[input(int("Введите номер строки от 11 до 13:"))])
            print(f"""Входные данные данные - {input_date}
            Результат обработки - {get_date(input_date)}""")


    operations: list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(operations, state="EXECUTED"))

    print(sort_by_date(operations, flow=True))
