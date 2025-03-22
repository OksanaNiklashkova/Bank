from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
import json

if __name__ == "__main__":
    # открываем файл с примерами обрабатываемой функциями информацией
    with open("data/data_for_example", "r", encoding="utf-8") as file:
        input_information = file.readlines()

# функция, маскирующая данные о счете или карте
common_for_mask = input_information[int(input("Введите номер строки от 1 до 8: "))]
print(
    f"""Входные данные данные - {common_for_mask}
Результат обработки - {mask_account_card(common_for_mask)}"""
)

# функция, преобразующая дату в стандартный формат
input_date = str(input_information[int(input("Введите номер строки от 10 до 12: "))])
print(
    f"""Входные данные данные - {input_date}
Результат обработки - {get_date(input_date)}"""
)

# функции сортировки операций по статусу и дате
operations = [json.loads(line) for line in input_information[15:19]]

state_check = int(
    input(
        """Выберите статус операции:
              1 - успешно проведена
              0 - отменена
              - """
    )
)
if state_check == False:
    state = "CANCELED"
else:
    state = "EXECUTED"
print(filter_by_state(operations, state))

flow = int(
    input(
        """Выберите направление сортировки операции по дате:
              1 - по убыванию
              0 - по возрастанию
              - """
    )
)
print(sort_by_date(operations, flow))
