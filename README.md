# Project Bank

Этот проект предоставляет возможность обработки банковских данных, с помощью функций: маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка информации об операциях.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number`: Маскирует номер карты, скрывая часть цифр в середине.
-   `get_mask_account`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card`: Возвращает информацию о карте или счете клиента, маскируя номер.
-   `get_date`: Преобразует системную дату в формат 'ДД.ММ.ГГГГ'.
-   `filter_by_state`: Фильтрует список операций по успешности выполнения, на основе значения ключа `state`.
-   `sort_by_date`: Сортирует список операций по дате, на основе значения ключа 'date'.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone git@github.com:OksanaNiklashkova/Bank_Widget.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd project_bank
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    ```

## Использование

Примеры использования функций:

~~~
from datetime import datetime
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date
from typing import List

Маскировка номера карты
card_number = "1234567890123456"
masked_number = get_mask_card_number(card_number)
print(f"Информация о карте: {masked_number}") # Output: 1234 56** **** 3456

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Информация о счете: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
input_information = "Visa Classic 1234567890123456"
masked_information = mask_account_card(input_information)
print(f"Информация о карте/счете: {masked_information}") # Output: Visa Classic 1234 56** **** 3456

Преобразование даты
input_date = "2023-03-06T00:00:00"
formated_date = get_date(input_date)
print(f"Дата операции: {formated_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
operations = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
list_of_operation = filter_by_state(operations, state="EXECUTED")
print(f"Успешные операции: \n{list_of_operation}")

Сортировка по дате
sort_by_date_list = sort_by_date(operations)
print(f"Список операций: \n{sort_by_date_list}")

~~~

## Зависимости

Проект использует следующие зависимости:

*   Python 3.13
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
